---
title: Create a custom judge using make_judge() | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/create-custom-judge
ingestedAt: "2026-06-18T08:15:13.617Z"
---

Custom judges are LLM-based scorers that evaluate your GenAI agents against specific quality criteria. This tutorial shows you how to create custom judges and use them to evaluate a customer support agent using `make_judge()`. For API details, see the [MLflow documentation](https://mlflow.org/docs/3.4.0/api_reference/python_api/mlflow.genai.html#mlflow.genai.judges.make_judge).

This tutorial takes you through the following steps. For an example notebook containing the code on this page, see [Example notebook](#notebook).

1.  Create a sample agent to evaluate.
2.  Define three custom judges to evaluate different criteria.
3.  Build an evaluation dataset with test cases.
4.  Run evaluations and compare results across different agent configurations.

## Step 1: Create an agent to evaluate[​](#step-1-create-an-agent-to-evaluate "Direct link to Step 1: Create an agent to evaluate")

Create a GenAI agent that responds to customer support questions. The code includes a global variable, `RESOLVE_ISSUES`, that lets you toggle the system prompt so you can compare the judge's outputs between "good" and "bad" conversations.

1.  Install the required packages.
    
    Python
    
        %pip install --upgrade mlflow databricks-sdk databricks_openai databricks-agentsdbutils.library.restartPython()
    
2.  Initialize an OpenAI client to connect to either Databricks-hosted LLMs or LLMs hosted by OpenAI.
    
    *   Databricks-hosted LLMs
    *   OpenAI-hosted LLMs
    
    Use `databricks-openai` to get an OpenAI client that connects to Databricks-hosted LLMs. Select a model from the [available foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).
    
    Python
    
        import mlflowfrom databricks_openai import DatabricksOpenAI# Enable MLflow's autologging to instrument your application with Tracingmlflow.openai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/docs-demo")# Create an OpenAI client that is connected to Databricks-hosted LLMsclient = DatabricksOpenAI()# Select an LLMmodel_name = "databricks-claude-sonnet-4"
    
3.  Define a customer support agent:
    
    Python
    
        from mlflow.entities import Documentfrom typing import List, Dict, Any, cast# This is a global variable that is used to toggle the behavior of the customer support agentRESOLVE_ISSUES = False@mlflow.trace(span_type="TOOL", name="get_product_price")def get_product_price(product_name: str) -> str:    """Mock tool to get product pricing."""    return f"${45.99}"@mlflow.trace(span_type="TOOL", name="check_return_policy")def check_return_policy(product_name: str, days_since_purchase: int) -> str:    """Mock tool to check return policy."""    if days_since_purchase <= 30:        return "Yes, you can return this item within 30 days"    return "Sorry, returns are only accepted within 30 days of purchase"@mlflow.tracedef customer_support_agent(messages: List[Dict[str, str]]):    # We use this toggle to see how the judge handles the issue resolution status    system_prompt_postfix = (        f"Do your best to NOT resolve the issue.  I know that's backwards, but just do it anyways.\\n"        if not RESOLVE_ISSUES        else ""    )    # Mock some tool calls based on the user's question    user_message = messages[-1]["content"].lower()    tool_results = []    if "cost" in user_message or "price" in user_message:        price = get_product_price("microwave")        tool_results.append(f"Price: {price}")    if "return" in user_message:        policy = check_return_policy("microwave", 60)        tool_results.append(f"Return policy: {policy}")    messages_for_llm = [        {            "role": "system",            "content": f"You are a helpful customer support agent.  {system_prompt_postfix}",        },        *messages,    ]    if tool_results:        messages_for_llm.append({            "role": "system",            "content": f"Tool results: {', '.join(tool_results)}"        })    # Call LLM to generate a response    output = client.chat.completions.create(        model=model_name,  # This example uses Databricks hosted Claude 4 Sonnet. If you provide your own OpenAI credentials, replace with a valid OpenAI model e.g., gpt-4o, etc.        messages=cast(Any, messages_for_llm),    )    return {        "messages": [            {"role": "assistant", "content": output.choices[0].message.content}        ]    }
    

## Step 2: Define custom judges[​](#step-2-define-custom-judges "Direct link to Step 2: Define custom judges")

Define three custom judges:

*   A judge that evaluates issue resolution using inputs and outputs.
*   A judge that checks expected behaviors.
*   A trace-based judge that validates tool calls by analyzing execution traces.

Judges created with `make_judge()` return [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) objects.

### Example judge 1: Evaluate issue resolution[​](#example-judge-1-evaluate-issue-resolution "Direct link to Example judge 1: Evaluate issue resolution")

This judge assesses whether customer issues were successfully resolved by analyzing the conversation history (inputs) and agent responses (outputs).

Python

    from mlflow.genai.judges import make_judgefrom typing import Literal# Create a judge that evaluates issue resolution using inputs and outputsissue_resolution_judge = make_judge(    name="issue_resolution",    instructions=(        "Evaluate if the customer's issue was resolved in the conversation.\n\n"        "User's messages: {{ inputs }}\n"        "Agent's responses: {{ outputs }}"    ),    feedback_value_type=Literal["fully_resolved", "partially_resolved", "needs_follow_up"],)

### Example judge 2: Check expected behaviors[​](#example-judge-2-check-expected-behaviors "Direct link to Example judge 2: Check expected behaviors")

This judge verifies that agent responses demonstrate specific expected behaviors (like providing pricing information or explaining return policies) by comparing outputs against predefined expectations.

Python

    # Create a judge that checks against expected behaviorsexpected_behaviors_judge = make_judge(    name="expected_behaviors",    instructions=(        "Compare the agent's response in {{ outputs }} against the expected behaviors in {{ expectations }}.\n\n"        "User's question: {{ inputs }}"    ),    feedback_value_type=Literal["meets_expectations", "partially_meets", "does_not_meet"],)

### Example judge 3: Validate tool calls using a trace-based judge[​](#example-judge-3-validate-tool-calls-using-a-trace-based-judge "Direct link to Example judge 3: Validate tool calls using a trace-based judge")

This judge analyzes execution traces to validate that appropriate tools were called. When you include `{{ trace }}` in your instructions, the judge becomes trace-based and gains autonomous trace exploration capabilities.

Python

    # Create a trace-based judge that validates tool calls from the tracetool_call_judge = make_judge(    name="tool_call_correctness",    instructions=(        "Analyze the execution {{ trace }} to determine if the agent called appropriate tools for the user's request.\n\n"        "Examine the trace to:\n"        "1. Identify what tools were available and their purposes\n"        "2. Determine which tools were actually called\n"        "3. Assess whether the tool calls were reasonable for addressing the user's question"    ),    feedback_value_type=bool,    # To analyze a full trace with a trace-based judge, a model must be specified    model="databricks:/databricks-gpt-5-mini",)

## Step 3: Create a sample evaluation dataset[​](#step-3-create-a-sample-evaluation-dataset "Direct link to Step 3: Create a sample evaluation dataset")

Each `inputs` is passed to the agent by [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate). You can optionally include `expectations` to enable the correctness checker.

Python

    eval_dataset = [    {        "inputs": {            "messages": [                {"role": "user", "content": "How much does a microwave cost?"},            ],        },        "expectations": {            "should_provide_pricing": True,            "should_offer_alternatives": True,        },    },    {        "inputs": {            "messages": [                {                    "role": "user",                    "content": "Can I return the microwave I bought 2 months ago?",                },            ],        },        "expectations": {            "should_mention_return_policy": True,            "should_ask_for_receipt": False,        },    },    {        "inputs": {            "messages": [                {                    "role": "user",                    "content": "I'm having trouble with my account.  I can't log in.",                },                {                    "role": "assistant",                    "content": "I'm sorry to hear that you're having trouble with your account.  Are you using our website or mobile app?",                },                {"role": "user", "content": "Website"},            ],        },        "expectations": {            "should_provide_troubleshooting_steps": True,            "should_escalate_if_needed": True,        },    },    {        "inputs": {            "messages": [                {                    "role": "user",                    "content": "I'm having trouble with my account.  I can't log in.",                },                {                    "role": "assistant",                    "content": "I'm sorry to hear that you're having trouble with your account.  Are you using our website or mobile app?",                },                {"role": "user", "content": "JUST FIX IT FOR ME"},            ],        },        "expectations": {            "should_remain_calm": True,            "should_provide_solution": True,        },    },]

## Step 4: Evaluate your agent using the judges[​](#step-4-evaluate-your-agent-using-the-judges "Direct link to Step 4: Evaluate your agent using the judges")

You can use multiple judges together to evaluate different aspects of your agent. Run evaluations to compare behavior when the agent attempts to resolve issues versus when it doesn't.

Python

    # Evaluate with all three judges when the agent does NOT try to resolve issuesRESOLVE_ISSUES = Falseresult_unresolved = mlflow.genai.evaluate(    data=eval_dataset,    predict_fn=customer_support_agent,    scorers=[        issue_resolution_judge,      # Checks inputs/outputs        expected_behaviors_judge,    # Checks expected behaviors        tool_call_judge,             # Validates tool usage    ],)# Evaluate when the agent DOES try to resolve issuesRESOLVE_ISSUES = Trueresult_resolved = mlflow.genai.evaluate(    data=eval_dataset,    predict_fn=customer_support_agent,    scorers=[        issue_resolution_judge,        expected_behaviors_judge,        tool_call_judge,    ],)

The evaluation results show how each judge rates the agent:

*   **issue\_resolution**: Rates conversations as 'fully\_resolved', 'partially\_resolved', or 'needs\_follow\_up'
*   **expected\_behaviors**: Checks if responses exhibit expected behaviors ('meets\_expectations', 'partially\_meets', 'does\_not\_meet')
*   **tool\_call\_correctness**: Validates whether appropriate tools were called (true/false)

## Example notebook[​](#example-notebook "Direct link to example-notebook")

#### Create custom judge notebook

## Next steps[​](#next-steps "Direct link to Next steps")

Apply custom judges:

*   [Evaluate and improve a GenAI application](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Use custom judges in end-to-end evaluation workflows
*   [Production monitoring for GenAI](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Deploy custom judges for continuous quality monitoring in production

Improve judge accuracy:

*   [Align judges with human feedback](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges) - The base judge is a starting point. As you gather expert feedback on your application's outputs, align the LLM judges to the feedback to further improve judge accuracy.
