---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a020d2fd315df9d5ddb7436d4c743cbeed4cd63091383213ce38c6b96db1bb11
  pageDirectory: concepts
  sources:
    - tracing-ollama-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ollama
    - Llama
    - Tracing Ollama
  citations:
    - file: tracing-ollama-databricks-on-aws.md
title: Ollama
description: An open-source platform for running large language models (LLMs) locally on personal devices, supporting models like Llama 3.2, Gemma 2, and Mistral.
tags:
  - llm
  - open-source
  - local-inference
timestamp: "2026-06-19T23:12:35.321Z"
---

# Ollama

**Ollama** is an open-source platform that enables users to run large language models (LLMs) locally on their devices. It supports models such as Llama 3.2, Gemma 2, Mistral, Code Llama, and many others.^[tracing-ollama-databricks-on-aws.md]

## Architecture

Ollama serves local LLMs through a REST endpoint that is compatible with the OpenAI API. This compatibility means that any application or library designed to work with OpenAI's API can seamlessly interact with Ollama by simply changing the base URL to the local endpoint.^[tracing-ollama-databricks-on-aws.md]

## Tracing on Databricks

On Databricks, Ollama [Traces](/concepts/traces.md) can be captured and recorded using [MLflow](/concepts/mlflow.md)'s auto-logging capabilities. Because Ollama's local endpoint is OpenAI API-compatible, you can enable tracing by calling `mlflow.openai.autolog()`. Any LLM interactions via Ollama will then be recorded to the active [MLflow Experiment](/concepts/mlflow-experiment.md).^[tracing-ollama-databricks-on-aws.md]

### Important Note

On [serverless compute clusters](/concepts/serverless-gpu-compute-databricks.md), [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.^[tracing-ollama-databricks-on-aws.md]

## Example Usage

To use Ollama with [MLflow Tracing](/concepts/mlflow-tracing.md) on Databricks:

1. **Run the Ollama server** with the desired LLM model on your local device.
2. **Enable auto-tracing** for the OpenAI SDK:
   ```python
   import [[mlflow|MLflow]]
   [[mlflow|MLflow]].openai.autolog()
   [[mlflow|MLflow]].set_tracking_uri("databricks")
   [[mlflow|MLflow]].set_experiment("/Shared/ollama-demo")
   ```
3. **Query the LLM** using the OpenAI Python client:
   ```python
   from openai import OpenAI
   
   client = OpenAI(
       base_url="http://localhost:11434/v1",  # The local Ollama REST endpoint
       api_key="dummy",  # Required to instantiate OpenAI client, it can be a random string
   )
   
   response = client.chat.completions.create(
       model="llama3.2:1b",
       messages=[
           {"role": "system", "content": "You are a science teacher."},
           {"role": "user", "content": "Why is the sky blue?"},
       ],
   )
   ```

After running this code, [Traces](/concepts/traces.md) of the LLM interaction will appear in the [MLflow UI](/concepts/mlflow.md).^[tracing-ollama-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto tracing for Ollama can be disabled globally by calling `mlflow.openai.autolog(disable=True)` or `mlflow.autolog(disable=True)`.^[tracing-ollama-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — The platform used for tracking and tracing Ollama interactions
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — The type of models served by Ollama
- OpenAI API — The API standard that Ollama's endpoint is compatible with
- Local LLM Deployment — The paradigm of running LLMs on local hardware
- Databricks Serverless Compute — The compute environment requiring explicit autologging

## Sources

- tracing-ollama-databricks-on-aws.md

# Citations

1. [tracing-ollama-databricks-on-aws.md](/references/tracing-ollama-databricks-on-aws-d0fc7add.md)
