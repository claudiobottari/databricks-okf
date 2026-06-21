---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 939cc4908688e363b745715d149aa7383c393b70267971f7a3733c85a4b6fc68
  pageDirectory: concepts
  sources:
    - retrievalgroundedness-judge-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-claude-model-integration
    - DCMI
  citations:
    - file: retrievalgroundedness-judge-databricks-on-aws.md
title: Databricks-hosted Claude model integration
description: Use of Databricks-hosted Claude models (via databricks:/ paths) as judges or generation models within MLflow GenAI evaluation workflows.
tags:
  - databricks
  - claude
  - mlflow
  - llm
timestamp: "2026-06-19T20:15:01.336Z"
---

# Databricks-hosted Claude Model Integration

**Databricks-hosted Claude model integration** refers to the ability to use Anthropic's Claude models that are hosted and served directly within the Databricks platform, eliminating the need for external API credentials or third-party service configurations. This integration is available through Databricks' model serving infrastructure and can be used in various MLflow workflows, including evaluation and scoring tasks. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Overview

When using Databricks-hosted Claude models, users can reference the model by name in their code without providing external API keys or endpoint URLs. The model is served from within the Databricks environment, which simplifies configuration and keeps all data processing within the platform's security boundary. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Usage in MLflow Evaluation

Databricks-hosted Claude models can be used as the underlying model for [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation judges. For example, when using the [RetrievalGroundedness judge](/concepts/retrievalgroundedness-judge.md), you can specify a Databricks-hosted model as the evaluation model: ^[retrievalgroundedness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalGroundedness

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalGroundedness(
            model="databricks:/databricks-gpt-oss-120b",  # Databricks-hosted model
        )
    ]
)
```

The `model` parameter accepts a Databricks model reference in the format `databricks:/model-name`. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Usage in RAG Applications

In [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications, Databricks-hosted Claude models can be used as the generation model. The model is referenced by name when creating chat completions: ^[retrievalgroundedness-judge-databricks-on-aws.md]

```python
response = client.chat.completions.create(
    model=model_name,  # Databricks-hosted Claude model name
    messages=messages
)
```

## Comparison with External Models

The documentation contrasts Databricks-hosted models with external models like OpenAI's GPT models. When using Databricks-hosted Claude, no external credentials are required. If you provide your own OpenAI credentials, you would replace the Databricks model reference with a valid OpenAI model name (e.g., `gpt-4o`). ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Benefits

- **Simplified configuration**: No need to manage external API keys or service connections
- **Data residency**: All data processing stays within the Databricks environment
- **Unified workflow**: Models are referenced using the same Databricks model serving infrastructure
- **Integration with MLflow**: Seamless use with [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) judges and scoring workflows

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow module for generative AI evaluation and monitoring
- [RetrievalGroundedness judge](/concepts/retrievalgroundedness-judge.md) — An MLflow judge that evaluates whether responses are grounded in retrieved context
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Architecture pattern combining retrieval with LLM generation
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — Infrastructure for hosting and serving models within Databricks
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — Framework for evaluating LLM-based applications

## Sources

- retrievalgroundedness-judge-databricks-on-aws.md

# Citations

1. [retrievalgroundedness-judge-databricks-on-aws.md](/references/retrievalgroundedness-judge-databricks-on-aws-595883b7.md)
