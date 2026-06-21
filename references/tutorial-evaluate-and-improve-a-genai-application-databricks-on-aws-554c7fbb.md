---
title: "Tutorial: Evaluate and improve a GenAI application | Databricks on AWS"
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app
ingestedAt: "2026-06-18T08:15:22.962Z"
---

This tutorial shows you how to use evaluation datasets to evaluate quality, identify issues, and iteratively improve a generative AI application.

This guide steps you through evaluating an email generation app that uses Retrieval-Augmented Generation (RAG). The app simulates retrieving customer information from a database and generates personalized follow-up emails based on the retrieved information.

For a shorter introduction to evaluation, see [10-minute demo: Evaluate a GenAI app](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/eval).

This tutorial includes the following steps:

*   Create [evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-datasets) from real usage data.
*   Evaluate quality with MLflow's [LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) using the [evaluation harness](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness).
*   Interpret results to identify quality issues.
*   Improve your app based on evaluation results.
*   Compare versions to verify improvements worked and did not cause regressions.

The tutorial uses traces from a deployed app to create the evaluation dataset, but the same workflow applies no matter how you created your evaluation dataset. For other approaches to creating an evaluation dataset, see [Building MLflow evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset). For information about tracing, see [MLflow Tracing - GenAI observability](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/).

![Offline monitoring workflow diagram](https://docs.databricks.com/aws/en/assets/images/offline-eval-bf825a15a0e3636185bb11081747acdf.png)

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

1.  Install required packages:
    
    Python
    
        %pip install -q --upgrade "mlflow[databricks]>=3.1.0" openaidbutils.library.restartPython()
    
2.  Create an MLflow experiment. If you are using a Databricks notebook, you can skip this step and use the default notebook experiment. Otherwise, follow the [environment setup quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment) to create the experiment and connect to the MLflow Tracking server.
    
3.  To create an evaluation dataset, you must have `CREATE TABLE` permissions on a schema in Unity Catalog.
    
    If you are using a [Databricks trial account](https://docs.databricks.com/aws/en/getting-started/express-setup), you must have CREATE TABLE permissions on the Unity Catalog schema `workspace.default`.
    

## Step 1: Create your application[​](#step-1-create-your-application "Direct link to Step 1: Create your application")

The first step is to create the email generation app. The retrieval component is marked with [`span_type="RETRIEVER"`](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/span-concepts#retriever-spans) to enable MLflow's retrieval-specific LLM judges.

1.  Initialize an OpenAI client to connect to either Databricks-hosted LLMs or LLMs hosted by OpenAI.
    
    *   Databricks-hosted LLMs
    *   OpenAI-hosted LLMs
    
    Use `databricks-openai` to get an OpenAI client that connects to Databricks-hosted LLMs. Select a model from the [available foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).
    
    Python
    
        import mlflowfrom databricks_openai import DatabricksOpenAI# Enable MLflow's autologging to instrument your application with Tracingmlflow.openai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/docs-demo")# Create an OpenAI client that is connected to Databricks-hosted LLMsclient = DatabricksOpenAI()# Select an LLMmodel_name = "databricks-claude-sonnet-4"
    
2.  Create the email generation app:
    
    Python
    
        from mlflow.entities import Documentfrom typing import List, Dict# Simulated customer relationship management databaseCRM_DATA = {    "Acme Corp": {        "contact_name": "Alice Chen",        "recent_meeting": "Product demo on Monday, very interested in enterprise features. They asked about: advanced analytics, real-time dashboards, API integrations, custom reporting, multi-user support, SSO authentication, data export capabilities, and pricing for 500+ users",        "support_tickets": ["Ticket #123: API latency issue (resolved last week)", "Ticket #124: Feature request for bulk import", "Ticket #125: Question about GDPR compliance"],        "account_manager": "Sarah Johnson"    },    "TechStart": {        "contact_name": "Bob Martinez",        "recent_meeting": "Initial sales call last Thursday, requested pricing",        "support_tickets": ["Ticket #456: Login issues (open - critical)", "Ticket #457: Performance degradation reported", "Ticket #458: Integration failing with their CRM"],        "account_manager": "Mike Thompson"    },    "Global Retail": {        "contact_name": "Carol Wang",        "recent_meeting": "Quarterly review yesterday, happy with platform performance",        "support_tickets": [],        "account_manager": "Sarah Johnson"    }}# Use a retriever span to enable MLflow's predefined RetrievalGroundedness judge to work@mlflow.trace(span_type="RETRIEVER")def retrieve_customer_info(customer_name: str) -> List[Document]:    """Retrieve customer information from CRM database"""    if customer_name in CRM_DATA:        data = CRM_DATA[customer_name]        return [            Document(                id=f"{customer_name}_meeting",                page_content=f"Recent meeting: {data['recent_meeting']}",                metadata={"type": "meeting_notes"}            ),            Document(                id=f"{customer_name}_tickets",                page_content=f"Support tickets: {', '.join(data['support_tickets']) if data['support_tickets'] else 'No open tickets'}",                metadata={"type": "support_status"}            ),            Document(                id=f"{customer_name}_contact",                page_content=f"Contact: {data['contact_name']}, Account Manager: {data['account_manager']}",                metadata={"type": "contact_info"}            )        ]    return []@mlflow.tracedef generate_sales_email(customer_name: str, user_instructions: str) -> Dict[str, str]:    """Generate personalized sales email based on customer data & a sale's rep's instructions."""    # Retrieve customer information    customer_docs = retrieve_customer_info(customer_name)    # Combine retrieved context    context = "\n".join([doc.page_content for doc in customer_docs])    # Generate email using retrieved context    prompt = f"""You are a sales representative. Based on the customer information below,    write a brief follow-up email that addresses their request.    Customer Information:    {context}    User instructions: {user_instructions}    Keep the email concise and personalized."""    response = client.chat.completions.create(        model=model_name, # This example uses a Databricks hosted LLM - you can replace this with any AI Gateway or Model Serving endpoint. If you provide your own OpenAI credentials, replace with a valid OpenAI model e.g., gpt-4o, etc.        messages=[            {"role": "system", "content": "You are a helpful sales assistant."},            {"role": "user", "content": prompt}        ],        max_tokens=2000    )    return {"email": response.choices[0].message.content}# Test the applicationresult = generate_sales_email("Acme Corp", "Follow up after product demo")print(result["email"])
    

![Evaluation app trace](https://assets.docs.databricks.com/_static/images/mlflow3-genai/new-images/eval-app-guide-initial-trace.gif)

## Step 2: Simulate production traffic[​](#step-2-simulate-production-traffic "Direct link to Step 2: Simulate production traffic")

This step simulates traffic for demonstration purposes. In practice, you would use traces from actual usage to create your evaluation dataset.

Python

    # Simulate beta testing traffic with scenarios designed to fail guidelinestest_requests = [    {"customer_name": "Acme Corp", "user_instructions": "Follow up after product demo"},    {"customer_name": "TechStart", "user_instructions": "Check on support ticket status"},    {"customer_name": "Global Retail", "user_instructions": "Send quarterly review summary"},    {"customer_name": "Acme Corp", "user_instructions": "Write a very detailed email explaining all our product features, pricing tiers, implementation timeline, and support options"},    {"customer_name": "TechStart", "user_instructions": "Send an enthusiastic thank you for their business!"},    {"customer_name": "Global Retail", "user_instructions": "Send a follow-up email"},    {"customer_name": "Acme Corp", "user_instructions": "Just check in to see how things are going"},]# Run requests and capture tracesprint("Simulating production traffic...")for req in test_requests:    try:        result = generate_sales_email(**req)        print(f"✓ Generated email for {req['customer_name']}")    except Exception as e:        print(f"✗ Error for {req['customer_name']}: {e}")

## Step 3: Create evaluation dataset[​](#step-3-create-evaluation-dataset "Direct link to Step 3: Create evaluation dataset")

In this step you save the traces to an evaluation dataset. Storing the traces in an evaluation dataset allows you to link evaluation results to the dataset so you can track changes to the dataset over time and see all evaluation results generated using this dataset.

*   UI
*   SDK

1.  Click **Experiments** in the sidebar to display the Experiments page.
    
2.  Click on the name of your experiment to open it.
    
    ![Open experiment](https://docs.databricks.com/aws/en/assets/images/experiments-page-ce16367da375cf850a6aaac58669ab42.png)
    
3.  In the left sidebar, click **Traces**.
    
4.  Use the checkboxes on the left side of the trace list to select the traces you want to add. To select all traces on the current page, click the checkbox next to **Trace ID** in the column header.
    
    ![Select traces](https://docs.databricks.com/aws/en/assets/images/select-traces-6574a81a57967370c4bccde8c4445e0f.gif)
    
5.  Click **Actions**. The button label shows the number of selected traces, for example **Actions (3)**.
    
    ![Actions menu](https://docs.databricks.com/aws/en/assets/images/actions-menu-eval-dataset-0166eee400c80913e174a333f0b1472c.png)
    
6.  Under **Use for evaluation**, select **Add to evaluation dataset**. The **Add traces to evaluation dataset** dialog opens.
    
7.  If no evaluation datasets exist for this experiment, or if you want to add traces to a new dataset, follow these steps to create a new evaluation dataset:
    
    1.  Click **Create new dataset**.
    2.  Select the Unity Catalog schema to hold the new dataset.
    3.  Enter a name for the dataset and click **Create Dataset**.
    4.  Click **Export** and then click **Done**.
    
    ![Add traces dialog if no evaluation datasets exist](https://docs.databricks.com/aws/en/assets/images/add-traces-dialog-none-existing-5e3febb1de1fa97e5fef1bb25bc327dc.png)
    
    If evaluation datasets already exist for the experiment, click **Export** to the right of the dataset you want to add the traces to. You can export to more than one dataset. When you've finished exporting, click **Done**.
    
    ![Add traces dialog if with existing evaluation datasets](https://docs.databricks.com/aws/en/assets/images/add-traces-eval-set-dialog-a2b335379d8c5cded02f1c4c63e7213f.png)
    

## Step 4: Run evaluation with LLM judges[​](#step-4-run-evaluation-with-llm-judges "Direct link to Step 4: Run evaluation with LLM judges")

In this step, you use MLflow's built-in LLM judges to automatically evaluate different aspects of the GenAI app's quality. To learn more, see [LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) and [code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers).

Python

    from mlflow.genai.scorers import (    RetrievalGroundedness,    RelevanceToQuery,    Safety,    Guidelines,)# Save the LLM judges as a variable so you can re-use them in step 7email_judges = [        RetrievalGroundedness(),  # Checks if email content is grounded in retrieved data        Guidelines(            name="follows_instructions",            guidelines="The generated email must follow the user_instructions in the request.",        ),        Guidelines(            name="concise_communication",            guidelines="The email MUST be concise and to the point. The email should communicate the key message efficiently without being overly brief or losing important context.",        ),        Guidelines(            name="mentions_contact_name",            guidelines="The email MUST explicitly mention the customer contact's first name (e.g., Alice, Bob, Carol) in the greeting. Generic greetings like 'Hello' or 'Dear Customer' are not acceptable.",        ),        Guidelines(            name="professional_tone",            guidelines="The email must be in a professional tone.",        ),        Guidelines(            name="includes_next_steps",            guidelines="The email MUST end with a specific, actionable next step that includes a concrete timeline.",        ),        RelevanceToQuery(),  # Checks if email addresses the user's request        Safety(),  # Checks for harmful or inappropriate content    ]# Run evaluation with LLM judgeseval_results = mlflow.genai.evaluate(    data=eval_dataset,    predict_fn=generate_sales_email,    scorers=email_judges,)

## Step 5: View and interpret results[​](#step-5-view-and-interpret-results "Direct link to Step 5: View and interpret results")

Running [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate) creates an evaluation run. For details, see [Evaluation runs in MLflow](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/evaluation-runs).

An evaluation run is like a test report that captures everything about how your app performed on a specific dataset. The evaluation run contains a trace for each row in your evaluation dataset annotated with [feedback](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations) from each judge.

Using the evaluation run, you can view aggregate metrics and investigate test cases where your app performed poorly.

This evaluation shows several issues:

*   **Poor instruction following** - The agent frequently provides responses that don't match user requests, such as sending detailed product information when asked for simple check-ins, or providing support ticket updates when asked for enthusiastic thank-you messages.
*   **Lack of conciseness** - Most emails are unnecessarily long and include excessive details that dilute the key message, failing to communicate efficiently despite instructions to keep emails "concise and personalized".
*   **Missing concrete next steps** - The majority of emails fail to end with specific, actionable next steps that include concrete timelines, which was identified as a required element.

*   UI
*   SDK

### Assessment summary[​](#assessment-summary "Direct link to Assessment summary")

1.  Click **Experiments** in the sidebar to display the Experiments page.
    
2.  Click on the name of your experiment to open it.
    
3.  In the left sidebar, click **Evaluation runs**. The right pane shows a table of traces.
    
    ![Evaluation runs table](https://docs.databricks.com/aws/en/assets/images/eval-runs-table-2c75f5ca715d14ce725027781b63ceab.png)
    
    If you do not see the Assessments with their **Pass** and **Fail** labels, scroll to the right or hover over the pane separator and click the left-pointing arrow.
    
    ![Expand table](https://docs.databricks.com/aws/en/assets/images/expand-pane-fbb56a0c40834f8da51bff95d8690b1e.gif)
    
4.  To see the rationale for the **Pass** or **Fail** label, hover over the label.
    
    ![Hover over label to show rationale](https://docs.databricks.com/aws/en/assets/images/rationale-9cc9a86e3ec21c1e060890d8485741e7.gif)
    

### Details and add feedback[​](#details-and-add-feedback "Direct link to Details and add feedback")

To see more details for each trace:

1.  Click on the request identifier in the **Request** column. A window appears showing the full trace, including inputs and outputs for each step.
    
    ![Request details window](https://docs.databricks.com/aws/en/assets/images/request-details-e0ca5297702b7bdcd95efa9b7c598b15.png)
    
2.  At the right, you can add Feedback or Expectations to apply to the response for this request. If you do not see the Assessments pane, click ![Assessments button](data:image/png;base64,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). To add a new Assessment, scroll down and click ![Add new assessment button](data:image/png;base64,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).
    
3.  You can use the arrows at either side of this window to step through the requests.
    
    ![Step through requests using arrows](https://docs.databricks.com/aws/en/assets/images/step-through-requests-6ba8423d7bfd92825d6e83b0682a79d7.png)
    

## Step 6: Create an improved version[​](#step-6-create-an-improved-version "Direct link to Step 6: Create an improved version")

Use the evaluation results to create an improved version that addresses the identified issues.

When creating an improved version, focus on targeted changes based on evaluation results. Common improvement strategies include:

*   Prompt engineering: Refine system prompts to address specific failure patterns, add explicit guidelines for edge cases, include examples demonstrating correct handling, or adjust tone or style.
*   Guardrails: Implement validation steps in application logic and add post-processing to check outputs before presenting to users.
*   :Retrieval improvements (for RAG apps): Enhance retrieval mechanisms if relevant documents aren't being found by examining retrieval spans, improving embedding models, or refining chunking strategies.
*   Reasoning enhancements: Break complex tasks into multiple spans, implement chain-of-thought techniques, or add verification steps for critical outputs.

The code below shows prompt engineering improvements based on the evaluation results:

Python

    @mlflow.tracedef generate_sales_email_v2(customer_name: str, user_instructions: str) -> Dict[str, str]:    """Generate personalized sales email based on customer data & a sale's rep's instructions."""    # Retrieve customer information    customer_docs = retrieve_customer_info(customer_name) # retrive_customer_info is defined in Step 1    if not customer_docs:        return {"error": f"No customer data found for {customer_name}"}    # Combine retrieved context    context = "\n".join([doc.page_content for doc in customer_docs])    # Generate email using retrieved context with better instruction following    prompt = f"""You are a sales representative writing an email.MOST IMPORTANT: Follow these specific user instructions exactly:{user_instructions}Customer context (only use what's relevant to the instructions):{context}Guidelines:1. PRIORITIZE the user instructions above all else2. Keep the email CONCISE - only include information directly relevant to the user's request3. End with a specific, actionable next step that includes a concrete timeline (e.g., "I'll follow up with pricing by Friday" or "Let's schedule a 15-minute call this week")4. Only reference customer information if it's directly relevant to the user's instructionsWrite a brief, focused email that satisfies the user's exact request."""    response = client.chat.completions.create(        model="databricks-claude-sonnet-4-5",        messages=[            {"role": "system", "content": "You are a helpful sales assistant who writes concise, instruction-focused emails."},            {"role": "user", "content": prompt}        ],        max_tokens=2000    )    return {"email": response.choices[0].message.content}# Test the applicationresult = generate_sales_email("Acme Corp", "Follow up after product demo")print(result["email"])

## Step 7: Evaluate the new version and compare[​](#step-7-evaluate-the-new-version-and-compare "Direct link to Step 7: Evaluate the new version and compare")

Run the evaluation on the improved version using the same judges and dataset to see if you've successfully addressed the issues.

Python

    import mlflow# Run evaluation of the new version with the same judges as before# Use start_run to name the evaluation run in the UIwith mlflow.start_run(run_name="v2"):    eval_results_v2 = mlflow.genai.evaluate(        data=eval_dataset, # same eval dataset        predict_fn=generate_sales_email_v2, # new app version        scorers=email_judges, # same judges as step 4    )

## Step 8: Compare results[​](#-step-8-compare-results "Direct link to -step-8-compare-results")

Compare the results to understand if the changes improved quality.

*   UI
*   SDK

1.  Click **Experiments** in the sidebar to display the Experiments page.
    
2.  Click on the name of your experiment to open it.
    
3.  In the left sidebar, click **Evaluation runs**. The left pane shows a a list of evaluation runs for this experiment.
    
    ![Runs pane](https://docs.databricks.com/aws/en/assets/images/runs-pane-ed3cedf178b03ee7edf07431e0c11eb8.png)
    
4.  Check the boxes for the runs you want to compare.
    
5.  From the **Actions** drop-down menu, select **Compare**.
    
    ![Select runs to compare](https://docs.databricks.com/aws/en/assets/images/select-compare-3a93bef79f5b2b3f2c88cf9ded74facf.png)
    
6.  The right pane displays a comparison of each trace in the selected runs.
    
    ![Trace comparison screen](https://docs.databricks.com/aws/en/assets/images/run-comparison-table-2da879050fada7d5e7c1c06e8b28ba47.png)
    
7.  For more details, click on the request identifier in the **Request** column. A window appears showing the full traces for the request from each run selected for comparison.
    
    ![Comparison details window](https://docs.databricks.com/aws/en/assets/images/comparison-details-8e325bfa52fc542009d4d06c36bc4fcd.png)
    
    To see the details of each assessment, click **See details**. To see the trace details, click **See detailed trace view**.
    

## Step 9: Continue iterating[​](#step-9-continue-iterating "Direct link to Step 9: Continue iterating")

Based on the evaluation results, you can continue iterating to improve the application's quality and test each new fix.

## Example notebook[​](#-example-notebook "Direct link to -example-notebook")

The following notebook includes all of the code on this page.

#### Evaluating a GenAI app quickstart notebook

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Build evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) - Prepare data for consistent evaluation runs
*   [Evaluate conversations](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-conversations) - Assess multi-turn conversations with specialized scorers
*   [Conversation simulation](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/conversation-simulation) - Generate synthetic conversations to test your agent with diverse scenarios
*   [Create custom LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) - Further customize the LLM judges used in this guide
*   [Align judges with human feedback](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges) - Improve judge accuracy by 30-50% to match your team's standards
*   [Create custom code scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers) - Evaluate your app with deterministic code-based scorers
*   [Set up production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Use the same scorers to monitor quality in production
*   [Track app and prompt versions](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/track-prompts-app-versions) - Track application and prompt versions with MLflow.

## Reference guides[​](#reference-guides "Direct link to Reference guides")

*   [Evaluation Harness](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness) - Comprehensive reference for [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate)
*   [Scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) - Deep dive into how scorers assess quality
*   [Evaluation Datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-datasets) - Learn about versioned datasets for consistent testing
