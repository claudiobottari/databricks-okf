---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47d972dd596eff993b50b936be787b95bf6eb4e024b2565dc3cfe8739a9df6ca
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-llm-serving-endpoints
    - DLSE
    - Databricks Serving Endpoint
    - Databricks serving endpoint
    - databricks-llm-serving-endpoints-via-openai-sdk
    - DLSEVOS
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Databricks LLM Serving Endpoints
description: An OpenAI-compatible API for accessing Databricks-hosted LLMs (e.g., Claude Sonnet) using Databricks credentials, enabling seamless integration with MLflow evaluation.
tags:
  - databricks
  - llm-serving
  - api
timestamp: "2026-06-19T17:23:18.276Z"
---

---
title: Databricks LLM Serving Endpoints
summary: Databricks-hosted LLM inference endpoints (e.g., Claude Sonnet) accessible via an OpenAI-compatible API, used for serving models in GenAI evaluation workflows.
sources:
  - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  - create-a-custom-judge-using-make_judge-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T13:50:02.697Z"
updatedAt: "2026-06-19T13:50:02.697Z"
tags:
  - databricks
  - llm-serving
  - inference
aliases:
  - databricks-llm-serving-endpoints
  - DLSE
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Databricks LLM Serving Endpoints

**Databricks LLM Serving Endpoints** provide REST API access to large language models (LLMs) hosted on the Databricks platform. These endpoints allow applications and evaluation frameworks to call models like Claude Sonnet 4-5 or GPT-5 Mini as a standard OpenAI-compatible service.

## Overview

An LLM serving endpoint exposes a model at a URL of the form `https://<workspace-host>/serving-endpoints/<model-name>`. Databricks users can authenticate using a personal access token (or notebook credentials) and use the endpoint with any OpenAI-compatible client. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

In MLflow GenAI, serving endpoints are used to power model scoring, evaluation, and custom judges. For example, a custom judge created with `make_judge` can reference a Databricks model specifier such as `"databricks:/databricks-gpt-5-mini"` to use the hosted model for evaluation. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Using a Serving Endpoint

To call an LLM serving endpoint from Python, create an OpenAI client with the Databricks workspace host and token:

```python
import mlflow
from openai import OpenAI

mlflow_creds = mlflow.utils.databricks_utils.get_databricks_host_creds()
client = OpenAI(
    api_key=mlflow_creds.token,
    base_url=f"{mlflow_creds.host}/serving-endpoints"
)
```

Then choose a deployed model, for example `"databricks-claude-sonnet-4-5"`, and send a chat completion request:

```python
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

The response follows the standard OpenAI chat completion format. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Models and Availability

The exact set of models available through serving endpoints depends on the Databricks workspace configuration. The sources reference both `databricks-claude-sonnet-4-5` (Anthropic's Claude Sonnet 4.5) and `databricks-gpt-5-mini`, indicating support for both external and Databricks-hosted models. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Use Cases

- **GenAI evaluation** – Evaluating prompts and app quality by calling the endpoint inside a `predict_fn` and scoring outputs with [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md). ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Custom judges** – Creating LLM-as-a-judge evaluators that use a serving endpoint to rate agent outputs. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Production inference** – Integrating Databricks-hosted LLMs into interactive applications via the same REST interface.

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)
- [Custom Judges](/concepts/custom-judges.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
