---
title: Conversation simulation | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/conversation-simulation
ingestedAt: "2026-06-18T08:15:09.839Z"
---

Conversation simulation enables you to generate synthetic multi-turn conversations for testing your conversational AI agents. Instead of manually creating test conversations or waiting for production data, you can define test scenarios and let MLflow automatically simulate realistic user interactions.

note

Conversation simulation is [experimental](https://docs.databricks.com/aws/en/release-notes/release-types). The API and behavior might change in future releases.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Install MLflow 3.10.0 or later:

Bash

    pip install --upgrade 'mlflow[databricks]>=3.10'

## Why simulate conversations?[​](#why-simulate-conversations "Direct link to Why simulate conversations?")

Conversation simulation addresses these challenges by programmatically generating conversations based on defined goals and personas, enabling:

*   **Systematic evaluation**: Test different agent versions with consistent goals and personas
*   **Red-teaming**: Stress-test agents with diverse user behaviors at scale
*   **Rapid iteration**: Generate new test conversations instantly when requirements change

## Workflow[​](#workflow "Direct link to Workflow")

1.  **Define test cases or extract from existing conversations** - Specify goals, personas, and context for each simulated conversation, or generate them from production sessions.
2.  **Create simulator** - Initialize `ConversationSimulator` with your test cases and configuration.
3.  **Define your agent** - Implement your agent in a function that accepts conversation history.
4.  **Run evaluation** - Pass the simulator to `mlflow.genai.evaluate()` with your scorers.

## Quick start[​](#quick-start "Direct link to Quick start")

Here's a complete example that simulates conversations and evaluates them:

Python

    import mlflowfrom mlflow.genai.simulators import ConversationSimulatorfrom mlflow.genai.scorers import ConversationCompleteness, Safetyfrom openai import OpenAIclient = OpenAI()# 1. Define test cases with goals (required) and optional persona/contexttest_cases = [    {        "goal": "Successfully configure experiment tracking",    },    {        "goal": "Identify and fix a model deployment error",        "persona": "You are a frustrated data scientist who has been stuck on this issue for hours",    },    {        "goal": "Set up model versioning for a production pipeline",        "persona": "You are a beginner who needs step-by-step guidance",        "context": {            "user_id": "beginner_123"        },  # user_id is passed to predict_fn via kwargs    },]# 2. Create the simulatorsimulator = ConversationSimulator(    test_cases=test_cases,    max_turns=5,)# 3. Define your agent functiondef predict_fn(input: list[dict], **kwargs):    response = client.chat.completions.create(        model="gpt-4o-mini",        messages=input,    )    return response.choices[0].message.content# 4. Run evaluation with conversation and single-turn scorersresults = mlflow.genai.evaluate(    data=simulator,    predict_fn=predict_fn,    scorers=[        ConversationCompleteness(),  # Multi-turn scorer        Safety(),  # Single-turn scorer (applied to each turn)    ],)

## Defining test cases[​](#defining-test-cases "Direct link to Defining test cases")

Each test case represents a conversation scenario. Test cases support three fields:

### Goal[​](#goal "Direct link to Goal")

The goal describes what the simulated user wants to achieve. It should be specific enough to guide the conversation but open-ended enough to allow natural dialogue. Good goals describe the expected outcome so the simulator knows when the user's intent has been accomplished:

Python

    # Good goals - specific, actionable, and describe expected outcomes{"goal": "Successfully configure MLflow tracking for a distributed training job"}{"goal": "Understand when to use experiments vs. runs in MLflow"}{"goal": "Identify and fix why model artifacts aren't being logged"}# Less effective goals - too vague, no expected outcome{"goal": "Learn about MLflow"}{"goal": "Get help"}

### Persona[​](#persona "Direct link to Persona")

The persona shapes how the simulated user communicates. If not specified, a default helpful user persona is used:

Python

    # Technical expert who asks detailed questions{    "goal": "Reduce model serving latency below 100ms",    "persona": "You are a senior ML engineer who asks precise technical questions",}# Beginner who needs more guidance{    "goal": "Successfully set up experiment tracking",    "persona": "You are new to MLflow and need step-by-step explanations",}# Frustrated user testing agent resilience{    "goal": "Fix a deployment blocking production",    "persona": "You are impatient because this is blocking a release",}

### Context[​](#context "Direct link to Context")

The context field passes additional parameters to your predict function. This is useful for:

*   Passing user identifiers for personalization
*   Providing session state or configuration
*   Including metadata your agent needs

Python

    {    "goal": "Get personalized model recommendations",    "context": {        "user_id": "enterprise_user_42",  # user_id is passed to predict_fn via kwargs        "subscription_tier": "premium",        "preferred_framework": "pytorch",    },}

## Define test cases[​](#define-test-cases "Direct link to Define test cases")

The simplest way to define test cases is as a list of dictionaries or a DataFrame:

Python

    test_cases = [    {"goal": "Successfully configure experiment tracking"},    {"goal": "Debug a deployment error", "persona": "Senior engineer"},    {"goal": "Set up a CI/CD pipeline for ML", "context": {"team": "platform"}},]simulator = ConversationSimulator(test_cases=test_cases)

You can also use a DataFrame:

Python

    import pandas as pddf = pd.DataFrame(    [        {"goal": "Successfully configure experiment tracking"},        {"goal": "Debug a deployment error", "persona": "Senior engineer"},        {"goal": "Set up a CI/CD pipeline for ML"},    ])simulator = ConversationSimulator(test_cases=df)

## Generate test cases from existing conversations[​](#generate-test-cases-from-existing-conversations "Direct link to Generate test cases from existing conversations")

Generate test cases from existing conversation sessions using `generate_test_cases`. This is useful for creating test cases that reflect real user behavior from production conversations:

Python

    import mlflowfrom mlflow.genai.simulators import generate_test_cases, ConversationSimulator# Get existing sessions from your experimentsessions = mlflow.search_sessions(    locations=["<experiment-id>"],    max_results=50,)# Generate test cases by extracting goals and personas from sessionstest_cases = generate_test_cases(sessions)# Optionally, save generated test cases as a dataset for reproducibilityfrom mlflow.genai.datasets import create_datasetdataset = create_dataset(name="generated_scenarios")dataset.merge_records([{"inputs": tc} for tc in test_cases])# Use generated test cases with the simulatorsimulator = ConversationSimulator(test_cases=test_cases)

## Track test cases as MLflow dataset[​](#track-test-cases-as-mlflow-dataset "Direct link to Track test cases as MLflow dataset")

For reproducible testing, persist your test cases as an [MLflow Evaluation Dataset](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset):

Python

    from mlflow.genai.datasets import create_dataset, get_dataset# Create and populate a datasetdataset = create_dataset(name="conversation_test_cases")dataset.merge_records(    [        {"inputs": {"goal": "Successfully configure experiment tracking"}},        {"inputs": {"goal": "Debug a deployment error", "persona": "Senior engineer"}},    ])# Use the dataset with the simulatordataset = get_dataset(name="conversation_test_cases")simulator = ConversationSimulator(test_cases=dataset)

## Agent function interface[​](#agent-function-interface "Direct link to Agent function interface")

Your agent function receives the conversation history and returns a response. Two parameter names are supported:

*   **`input`**: Conversation history as a list of message dicts (Chat Completions response format)
*   **`messages`**: Equivalent alternative parameter name (Chat Completions request format)

Python

    def predict_fn(input: list[dict], **kwargs) -> str:    """    Args:        input: Conversation history as a list of message dicts.               Each message has "role" ("user" or "assistant") and "content".               Alternatively, use "messages" as the parameter name.        **kwargs: Additional arguments including:            - mlflow_session_id: Unique ID for this conversation session            - Any fields from your test case's "context"    Returns:        The assistant's response as a string.    """

*   Basic
*   With context
*   Stateful agent

Python

    from openai import OpenAIclient = OpenAI()def predict_fn(input: list[dict], **kwargs):    response = client.chat.completions.create(        model="gpt-4o-mini",        messages=input,    )    return response.choices[0].message.content

## Configuration options[​](#configuration-options "Direct link to Configuration options")

### ConversationSimulator parameters[​](#conversationsimulator-parameters "Direct link to ConversationSimulator parameters")

### Model selection[​](#model-selection "Direct link to Model selection")

The simulator uses an LLM to generate realistic user messages. You can specify a different model using the `user_model` parameter:

Python

    simulator = ConversationSimulator(    test_cases=test_cases,    user_model="anthropic:/claude-sonnet-4-20250514",    temperature=0.7,  # Passed to the user simulation LLM)

Supported model formats follow the pattern `"<provider>:/<model>"`. See the [MLflow documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/custom-judges/supported-models) for the full list of supported providers.

#### Information about the models powering conversation simulation[​](#information-about-the-models-powering-conversation-simulation "Direct link to Information about the models powering conversation simulation")

LLM-based conversation simulation might use third-party services to simulate user interactions, including Azure OpenAI operated by Microsoft.

For Azure OpenAI, Databricks has opted out of Abuse Monitoring so no prompts or responses are stored with Azure OpenAI.

For European Union (EU) workspaces, conversation simulation uses models hosted in the EU. All other regions use models hosted in the US.

Disabling Partner-powered AI features prevents conversation simulation from calling partner-powered models. You can still use conversation simulation by providing your own model.

### Conversation stopping[​](#conversation-stopping "Direct link to Conversation stopping")

Conversations stop when any of these conditions are met:

*   **Max turns reached**: The `max_turns` limit is hit
*   **Goal achieved**: The simulator detects the user's goal has been accomplished

## Viewing results[​](#viewing-results "Direct link to Viewing results")

Simulated conversations appear in the MLflow UI with special metadata:

*   **Session ID**: Each conversation has a unique session ID (prefixed with `sim-`)
*   **Simulation metadata**: Goal, persona, and turn number are stored on each trace

Navigate to the **Sessions** tab in your experiment to view conversations grouped by session. Select a session to see individual turns and their assessments.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Evaluate conversations](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-conversations) - Learn about static conversation evaluation and multi-turn scorers.
*   [Predefined scorers](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/) - Explore predefined scorers for conversation completeness, user frustration, and more.
*   [Evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) - Persist your test cases in evaluation datasets for reproducible testing.
