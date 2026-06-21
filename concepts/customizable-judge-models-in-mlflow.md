---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1998a7546efe83bd5fe04f97dc5c336c6adfecaf5eb2b543c3ff3f981d7b4234
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizable-judge-models-in-mlflow
    - CJMIM
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: Customizable Judge Models in MLflow
description: The ability to select which LLM powers a built-in MLflow judge by specifying a model in `<provider>:/<model-name>` format, with support for LiteLLM-compatible providers including Databricks serving endpoints.
tags:
  - mlflow
  - llm-evaluation
  - genai
timestamp: "2026-06-19T22:06:37.768Z"
---

# Customizable Judge Models in MLflow

**Customizable Judge Models in MLflow** refers to the ability to configure which large language model (LLM) powers the built-in evaluation judges used for assessing GenAI application quality. By default, MLflow uses a Databricks-hosted LLM designed specifically for quality assessments, but users can substitute any LiteLLM-compatible model to meet their specific evaluation requirements. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Overview

MLflow provides several built-in LLM judges for evaluating GenAI applications, including [RelevanceToQuery](/concepts/relevancetoquery.md) (which checks if responses address user input) and [RetrievalRelevance](/concepts/retrievalrelevance.md) (which checks if retrieved documents are relevant to queries). Each judge uses an underlying LLM to perform its assessments. The `model` parameter allows users to override the default judge model with a different LLM. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Specifying a Custom Judge Model

When creating a judge instance, pass the `model` argument with a string in the format `<provider>:/<model-name>`. The provider must be compatible with LiteLLM. If you use `databricks` as the provider, the model name corresponds to a Databricks Model Serving endpoint name. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RelevanceToQuery, RetrievalRelevance

# Use a different Databricks-hosted model
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"
)

# Use a LiteLLM-compatible model from another provider
retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Usage with MLflow Evaluation

Custom judge models work with both direct invocation and the `mlflow.genai.evaluate` workflow. When passed to `evaluate()`, the specified model powers all judge assessments performed during evaluation runs. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RelevanceToQuery(
            model="databricks:/databricks-gpt-5-mini"
        ),
        RetrievalRelevance(
            model="databricks:/databricks-claude-opus-4-5"
        )
    ]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Considerations for Selecting a Judge Model

The choice of judge model can affect evaluation outcomes. Consider the following when selecting a custom model:

- **Consistency**: Different LLMs may produce different quality assessments for the same input. Using a consistent judge model across evaluations helps maintain comparability of results. ^[answer-and-context-relevance-judges-databricks-on-aws.md]
- **Cost and latency**: Larger or more capable models typically incur higher costs and longer inference times for judge assessments. ^[answer-and-context-relevance-judges-databricks-on-aws.md]
- **Domain alignment**: Models fine-tuned on domain-specific data may provide more accurate relevance assessments for specialized applications. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Default Model Behavior

If no `model` argument is provided, built-in judges use a default Databricks-hosted LLM that is optimized for GenAI quality assessment tasks. This default model requires no additional configuration and works out of the box. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Interpretable Results

Regardless of which judge model is used, judges return a `Feedback` object containing:

- **`value`**: "yes" if the criterion is met (e.g., context is relevant), "no" if not
- **`rationale`**: An explanation of why the judge reached that conclusion

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [LLM Judge Evaluation](/concepts/llm-as-a-judge-evaluation.md) — Overview of using LLMs as evaluators for GenAI applications
- [RelevanceToQuery](/concepts/relevancetoquery.md) — Judge that evaluates response relevance to user queries
- [RetrievalRelevance](/concepts/retrievalrelevance.md) — Judge that evaluates document relevance in retrieval-augmented generation
- [Custom LLM Judges](/concepts/custom-llm-judges.md) — Creating specialized judges for domain-specific evaluation needs
- LiteLLM Integration — Framework for accessing multiple LLM providers through a unified interface
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Comprehensive evaluation framework for generative AI applications
- [Databricks Model Serving](/concepts/databricks-model-serving.md) — Infrastructure for deploying and serving custom models

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
