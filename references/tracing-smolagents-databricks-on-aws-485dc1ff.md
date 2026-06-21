---
title: Tracing Smolagents | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/smolagents
ingestedAt: "2026-06-18T08:17:38.865Z"
---

[Smolagents](https://github.com/huggingface/smolagents) is a lightweight agent framework that emphasizes minimalism and composability.

[MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) integrates with Smolagents to capture streamlined traces of lightweight agent workflows. Enable it with [`mlflow.smolagents.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.smolagents.html#mlflow.smolagents.autolog).

note

MLflow auto-tracing only supports synchronous calls. Asynchronous API and streaming methods are not traced.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To use MLflow Tracing with Smolagents, you need to install MLflow and the relevant Smolagents packages.

*   Development
*   Production

For development environments, install the full MLflow package with Databricks extras and Smolagents:

Bash

    pip install --upgrade "mlflow[databricks]>=3.1" smolagents openai

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks.

note

MLflow 3 is recommended for the best tracing experience.

Before running the examples, you'll need to configure your environment:

**For users outside Databricks notebooks**: Set your Databricks environment variables:

Bash

    export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"export DATABRICKS_TOKEN="your-personal-access-token"

**For users inside Databricks notebooks**: These credentials are automatically set for you.

**API Keys**: Ensure your LLM provider API keys are configured. For production environments, use [AI Gateway or Databricks secrets](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/#secure-api-key-management) instead of hardcoded values for secure API key management.

Bash

    export OPENAI_API_KEY="your-openai-api-key"# Add other provider keys as needed

## Example usage[​](#example-usage "Direct link to Example usage")

note

On serverless compute clusters, autologging for genAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.

Python

    import mlflowmlflow.smolagents.autolog()from smolagents import CodeAgent, LiteLLMModelimport mlflow# Turn on auto tracing for Smolagents by calling mlflow.smolagents.autolog()mlflow.smolagents.autolog()model = LiteLLMModel(model_id="openai/gpt-4o-mini", api_key=API_KEY)agent = CodeAgent(tools=[], model=model, add_base_tools=True)result = agent.run(    "Could you give me the 118th number in the Fibonacci sequence?",)

Run your Smolagents workflow as usual. Traces will appear in the experiment UI.

## Token tracking usage[​](#token-tracking-usage "Direct link to Token tracking usage")

MLflow logs token usage for each Agent callto the `mlflow.chat.tokenUsage` attribute. The total token usage throughout the trace is available in the `token_usage` field of the trace info object.

Python

    import jsonimport mlflowmlflow.smolagents.autolog()model = LiteLLMModel(model_id="openai/gpt-4o-mini", api_key=API_KEY)agent = CodeAgent(tools=[], model=model, add_base_tools=True)result = agent.run(    "Could you give me the 118th number in the Fibonacci sequence?",)# Get the trace object just createdlast_trace_id = mlflow.get_last_active_trace_id()trace = mlflow.get_trace(trace_id=last_trace_id)# Print the token usagetotal_usage = trace.info.token_usageprint("== Total token usage: ==")print(f"  Input tokens: {total_usage['input_tokens']}")print(f"  Output tokens: {total_usage['output_tokens']}")print(f"  Total tokens: {total_usage['total_tokens']}")# Print the token usage for each LLM callprint("\n== Detailed usage for each LLM call: ==")for span in trace.data.spans:    if usage := span.get_attribute("mlflow.chat.tokenUsage"):        print(f"{span.name}:")        print(f"  Input tokens: {usage['input_tokens']}")        print(f"  Output tokens: {usage['output_tokens']}")        print(f"  Total tokens: {usage['total_tokens']}")

## Disable auto-tracing[​](#disable-auto-tracing "Direct link to Disable auto-tracing")

Disable with [`mlflow.smolagents.autolog(disable=True)`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.smolagents.html#mlflow.smolagents.autolog) or globally with [`mlflow.autolog(disable=True)`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.autolog).
