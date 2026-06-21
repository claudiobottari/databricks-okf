---
title: Tracing LiteLLM🚄 | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/litellm
ingestedAt: "2026-06-18T08:17:22.415Z"
---

![LiteLLM Tracing using autolog](https://docs.databricks.com/aws/en/assets/images/litellm-tracing-39a2a3e58fdb3d8cce0ecdba1f4f70e8.png)

[LiteLLM](https://www.litellm.ai/) is an open-source LLM Gateway that allow accessing 100+ LLMs in the unified interface.

[MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) provides automatic tracing capability for LiteLLM. By enabling auto tracing for LiteLLM by calling the [`mlflow.litellm.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.litellm.html#mlflow.litellm.autolog) function, MLflow will capture traces for LLM invocation and log them to the active MLflow Experiment.

Python

    import mlflowmlflow.litellm.autolog()

MLflow trace automatically captures the following information about LiteLLM calls:

*   Prompts and completion responses
*   Latencies
*   Metadata about the LLM provider, such as model name and endpoint URL
*   Token usages and cost
*   Cache hit
*   Any exception if raised

note

On serverless compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.litellm.autolog()` to enable automatic tracing for this integration.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before running the examples below, make sure you have:

1.  **Databricks credentials configured**: If running outside of Databricks, set your environment variables:
    
    Bash
    
        export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"export DATABRICKS_TOKEN="your-personal-access-token"
    
    tip
    
    If you're running inside a Databricks notebook, these are automatically set for you.
    
2.  **LLM provider API keys**: Ensure your API keys are configured. For production environments, use [AI Gateway or Databricks secrets](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/#secure-api-key-management) instead of hardcoded values for secure API key management.
    
    Bash
    
        export ANTHROPIC_API_KEY="your-anthropic-api-key"  # For Anthropic modelsexport OPENAI_API_KEY="your-openai-api-key"        # For OpenAI models# Add other provider keys as needed
    

### Basic Example[​](#basic-example "Direct link to Basic Example")

Python

    import mlflowimport litellm# Enable auto-tracing for LiteLLMmlflow.litellm.autolog()# Set up MLflow tracking on Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/litellm-demo")# Call Anthropic API using LiteLLMresponse = litellm.completion(    model="claude-3-5-sonnet-20241022",    messages=[{"role": "user", "content": "Hey! how's it going?"}],)

### Async API[​](#async-api "Direct link to Async API")

MLflow supports tracing LiteLLM's async APIs:

Python

    mlflow.litellm.autolog()response = await litellm.acompletion(    model="claude-3-5-sonnet-20241022",    messages=[{"role": "user", "content": "Hey! how's it going?"}],)

### Streaming[​](#streaming "Direct link to Streaming")

MLflow supports tracing LiteLLM's sync and async streaming APIs:

Python

    mlflow.litellm.autolog()response = litellm.completion(    model="claude-3-5-sonnet-20241022",    messages=[{"role": "user", "content": "Hey! how's it going?"}],    stream=True,)for chunk in response:    print(chunk.choices[0].delta.content, end="|")

MLflow will record concatenated outputs from the stream chunks as a span output.

### Disable auto-tracing[​](#disable-auto-tracing "Direct link to Disable auto-tracing")

Auto tracing for LiteLLM can be disabled globally by calling `mlflow.litellm.autolog(disable=True)` or `mlflow.autolog(disable=True)`.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Understand tracing concepts](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101) - Learn how MLflow captures and organizes trace data
*   [Debug and observe your app](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/) - Use the Trace UI to analyze your LiteLLM application's behavior
*   [Evaluate your app's quality](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Set up quality assessment for your multi-provider LLM application
