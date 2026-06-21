---
title: Test an app version with the Review App's Chat UI | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/expert-feedback/live-app-testing
ingestedAt: "2026-06-18T08:16:06.260Z"
---

The MLflow Review App includes a built-in chat interface that allows domain experts to interactively test your GenAI application and provide immediate feedback. Use the Chat UI as a way to vibe check your app.

![Review App chat UI](https://assets.docs.databricks.com/_static/images/mlflow3-genai/tracing/review-app-chat-ui.gif)

## When to use Chat UI testing[​](#when-to-use-chat-ui-testing "Direct link to When to use Chat UI testing")

Chat UI testing is ideal when you want to:

*   Test conversational flows and multi-turn interactions with domain experts
*   Collect expert feedback on application responses and behavior
*   Validate updates in a safe environment before production deployment

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   MLflow and required packages must be installed. The features described in this guide require MLflow version 3.1.0 or above. Run the following command to install or upgrade the MLflow SDK, including extras needed for Databricks integration:
    
    Bash
    
        pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
    
*   Your development environment must be connected to the [MLflow Experiment](https://docs.databricks.com/aws/en/mlflow3/genai/concepts/) where your GenAI application traces are logged.
    
    *   Follow [Tutorial: Connect your development environment to MLflow](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment) to connect your development environment.
*   Domain experts must have the following permissions to use the Review App's Chat UI:
    
    *   **Account access**: Must be provisioned in your Databricks account, but do not need access to your workspace.
        
        For users without workspace access, account admins can:
        
        *   Use account-level SCIM provisioning to sync users from your identity provider
        *   Manually register users and groups in Databricks
        
        See [User and group management](https://docs.databricks.com/aws/en/admin/users-groups/scim/) for details.
        
    *   **Endpoint access**: **CAN\_QUERY** permission to the model serving endpoint.
        

## Set up and collect feedback with the Chat UI[​](#set-up-and-collect-feedback-with-the-chat-ui "Direct link to set-up-and-collect-feedback-with-the-chat-ui")

The MLflow Review App's Chat UI connects to a deployed version of your GenAI application, allowing domain experts to chat with your app and provide immediate feedback. Follow these steps to set up the Chat UI and collect feedback:

1.  [Package your app using Custom Agents](https://docs.databricks.com/aws/en/generative-ai/agent-framework/author-agent-model-serving) and [deploy it using Deploy on Apps](https://docs.databricks.com/aws/en/generative-ai/agent-framework/deploy-agent) as a Model Serving endpoint.
    
2.  Add the endpoint to your experiment's review app:
    
    note
    
    The below example adds a Databricks hosted LLM to the review app. Replace the endpoint with your app's endpoint from step 1.
    
    Python
    
        from mlflow.genai.labeling import get_review_app# Get review app for current MLflow experimentreview_app = get_review_app()# Connect your deployed agent endpointreview_app.add_agent(    agent_name="claude-sonnet",    model_serving_endpoint="databricks-claude-sonnet-4-5",)print(f"Share this URL: {review_app.url}/chat")
    
3.  Once configured, share the Review App URL with your domain experts. They'll be able to:
    

*   Access the chat interface through their web browser
*   Interact with your application by typing questions
*   Provide feedback after each response using the built-in feedback controls
*   Continue the conversation to test multiple interactions

## Review App content rendering[​](#review-app-content-rendering "Direct link to Review App content rendering")

The Chat UI uses domain expert queries as input, live agent endpoint responses as output, and stores results in MLflow traces. You don't need to provide a custom labeling schema, as this approach uses fixed feedback questions.

The Review App automatically renders different content types from your MLflow Trace:

*   **Retrieved documents**: Documents within a [`RETRIEVER` span](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/span-concepts#retriever-spans) are rendered for display
*   **OpenAI format messages**: Inputs and outputs of the MLflow Trace following OpenAI chat conversations are rendered:
    *   `outputs` that contain an OpenAI format [ChatCompletions](https://platform.openai.com/docs/api-reference/chat/object) object
    *   `inputs` or `outputs` dicts that contain a `messages` key with an [array of OpenAI format chat messages](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages)
        *   If the `messages` array contains OpenAI format tool calls, they are also rendered
*   **Dictionaries**: Inputs and outputs of the MLflow Trace that are dicts are rendered as pretty-printed JSONs

Otherwise, the content of the `input` and `output` from the root span of each trace are used as the primary content for review.

## View chat feedback[​](#view-chat-feedback "Direct link to View chat feedback")

All interactions and feedback collected through the Chat UI are automatically captured as traces in MLflow.

To view the traces from chat interactions:

1.  Navigate to the MLflow UI
2.  Find the experiment associated with your Review App session
3.  Browse the traces to see the full conversation history
4.  Review the feedback attached to each response

## Next steps[​](#next-steps "Direct link to Next steps")

*   Learn how to [label existing traces](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/expert-feedback/label-existing-traces) for more systematic feedback collection
*   Explore [end-user feedback collection](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/collect-user-feedback/) for production applications
