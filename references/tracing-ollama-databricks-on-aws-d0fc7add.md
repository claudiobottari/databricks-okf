---
title: Tracing Ollama | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/ollama
ingestedAt: "2026-06-18T08:17:27.755Z"
---

![Ollama Tracing via autolog](https://docs.databricks.com/aws/en/assets/images/ollama-tracing-69a45b14d6b555fcbb9441a658445124.png)

[Ollama](https://ollama.com/) is an open-source platform that enables users to run large language models (LLMs) locally on their devices, such as Llama 3.2, Gemma 2, Mistral, Code Llama, and more.

Since the local LLM endpoint served by Ollama is compatible with the OpenAI API, you can query it via OpenAI SDK and enable tracing for Ollama with [`mlflow.openai.autolog()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.openai.html#mlflow.openai.autolog). Any LLM interactions via Ollama will be recorded to the active MLflow Experiment.

Python

    import mlflowmlflow.openai.autolog()

note

On serverless compute clusters, autologging for genAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.

### Example Usage[​](#example-usage "Direct link to Example Usage")

1.  Run the Ollama server with the desired LLM model.

2.  Enable auto-tracing for OpenAI SDK.

    import mlflow# Enable auto-tracing for OpenAImlflow.openai.autolog()# Set up MLflow tracking on Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/ollama-demo")

3.  Query the LLM and see the traces in the MLflow UI.

Python

    from openai import OpenAIclient = OpenAI(    base_url="http://localhost:11434/v1",  # The local Ollama REST endpoint    api_key="dummy",  # Required to instantiate OpenAI client, it can be a random string)response = client.chat.completions.create(    model="llama3.2:1b",    messages=[        {"role": "system", "content": "You are a science teacher."},        {"role": "user", "content": "Why is the sky blue?"},    ],)

### Disable auto-tracing[​](#disable-auto-tracing "Direct link to Disable auto-tracing")

Auto tracing for Ollama can be disabled globally by calling `mlflow.openai.autolog(disable=True)` or `mlflow.autolog(disable=True)`.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Understand tracing concepts](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101) - Learn how MLflow captures and organizes trace data
*   [Debug and observe your app](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/) - Use the Trace UI to analyze your locally-run Ollama models
*   [Evaluate your app's quality](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Set up quality assessment for your Ollama-powered application
