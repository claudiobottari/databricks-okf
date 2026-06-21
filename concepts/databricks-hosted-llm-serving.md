---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d2fd1e3bc9bd66911d378a9dceb2eedc5775bda0c83054d4701128e5fed641d
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-llm-serving
    - DLS
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: optimize-multiple-prompts-together-databricks-on-aws.md
title: Databricks-hosted LLM Serving
description: Using Databricks-hosted foundation models (e.g., Claude Sonnet) via OpenAI-compatible API endpoints with Databricks credentials for GenAI application development.
tags:
  - databricks
  - llm-serving
  - model-deployment
timestamp: "2026-06-18T10:35:28.030Z"
---

# Databricks-hosted LLM Serving

**Databricks-hosted LLM Serving** provides managed inference endpoints for large language models (LLMs) within the Databricks platform. This service enables developers to access foundation models through a standardized API without managing underlying infrastructure, making it suitable for both development and production GenAI workloads.

## Overview

Databricks-hosted LLM Serving offers access to a variety of models through serving endpoints. These endpoints can be used with the OpenAI-compatible API, allowing seamless integration with existing tooling and libraries. The service handles model hosting, scaling, and request routing, abstracting away infrastructure management. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

Models available through Databricks-hosted endpoints include Claude Sonnet (e.g., `databricks-claude-sonnet-4-5`) and other foundation models. These endpoints are accessible via the standard OpenAI client by configuring the base URL and API key appropriately. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## API Access

To use a Databricks-hosted LLM endpoint, configure the OpenAI client with Databricks credentials:

```python
from openai import OpenAI
import mlflow

mlflow_creds = mlflow.utils.databricks_utils.get_databricks_host_creds()

client = OpenAI(
    api_key=mlflow_creds.token,
    base_url=f"{mlflow_creds.host}/serving-endpoints"
)
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The `base_url` points to the Databricks workspace's serving endpoints path. The API key is typically a Databricks personal access token. In Databricks notebooks, credentials are automatically available; outside notebooks, you must set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Model Selection

When making requests, specify the model name using the format `databricks-{model-name}`. For example:

```python
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[...]
)
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

Available model names depend on your Databricks workspace configuration and the models deployed to serving endpoints.

## Integration with MLflow

Databricks-hosted LLM Serving integrates naturally with [MLflow GenAI](/concepts/mlflow-3-for-genai.md) capabilities. The service can be used with:

- **[MLflow Tracing](/concepts/mlflow-tracing.md)**: Automatic tracing of LLM calls is enabled via `mlflow.openai.autolog()`, capturing inputs, outputs, and metadata for each request. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **[MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)**: Models accessed through Databricks-hosted endpoints can be evaluated using MLflow scorers, including the [MLflow Correctness Scorer](/concepts/mlflow-correctness-scorer.md) and other built-in evaluators. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **[MLflow Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md)**: Responses from hosted models can be associated with human feedback through tracing, enabling end-user ratings, developer annotations, and expert review. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Use Cases

Databricks-hosted LLM Serving supports a range of GenAI application patterns:

- **Sentence completion and text generation**: Filling templates, creative writing, and content generation. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Chat applications**: Multi-turn conversational interfaces using the chat completions API.
- **Evaluation targets**: Serving as the model under test in MLflow evaluation workflows, where outputs are compared against ground truth or assessed by LLM judges. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Prompt optimization**: Used with tools like [GepaPromptOptimizer](/concepts/gepapromptoptimizer.md) to refine prompts across multiple components of an agent system. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Best Practices

- **Enable tracing**: Use `mlflow.openai.autolog()` to automatically capture request/response data for debugging and evaluation. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Use appropriate model names**: Verify available model names in your workspace and use the `databricks-` prefix convention.
- **Handle credentials securely**: In production, use Databricks secrets or service principals rather than hard-coded tokens.
- **Combine with evaluation**: Regularly evaluate model outputs using [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) scorers to monitor quality and detect regressions.

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — MLflow's framework for generative AI applications
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Automatic instrumentation of LLM calls
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Quantitative assessment of model outputs
- [MLflow Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Gathering end-user, developer, and expert feedback
- [MLflow Correctness Scorer](/concepts/mlflow-correctness-scorer.md) — Comparing outputs against expected responses

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
- optimize-multiple-prompts-together-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [optimize-multiple-prompts-together-databricks-on-aws.md](/references/optimize-multiple-prompts-together-databricks-on-aws-a41f0275.md)
