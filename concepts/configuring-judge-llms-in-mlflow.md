---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c53f70bf5ed2b2751abc27b6104b8eb7932138f923330c19c9b821de539858e
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - configuring-judge-llms-in-mlflow
    - CJLIM
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: Configuring Judge LLMs in MLflow
description: The ability to customize which LLM powers the built-in judges by specifying a model in '<provider>:/<model-name>' format, supporting LiteLLM-compatible providers including Databricks serving endpoints.
tags:
  - mlflow
  - llm-configuration
  - judges
timestamp: "2026-06-19T17:34:10.875Z"
---

# Configuring Judge LLMs in MLflow

In MLflow, built-in LLM judges—such as `RelevanceToQuery` and `RetrievalRelevance—use a language model to evaluate the quality of GenAI applications. By default, each built-in judge is powered by a Databricks-hosted LLM designed specifically for quality assessment. You can override this default by specifying a different judge model when you instantiate the scorer. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Specifying a Judge Model

To configure a custom judge model, use the `model` argument when creating the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the provider, the model name is the same as the serving endpoint name. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

The following example shows how to change the judge model for both `RelevanceToQuery` and `RetrievalRelevance`: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RelevanceToQuery, RetrievalRelevance

# Use different judge models
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"  # Or any LiteLLM-compatible model
)
retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)

# Use in evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[relevance_judge, retrieval_judge]
)
```

The configured judge model is then used for every call within the evaluation, including direct invocation or through `mlflow.genai.evaluate`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Requirements

To run an evaluation using a custom judge LLM, you must have MLflow and required packages installed (at least `mlflow[databricks]>=3.4.0`). You also need an existing [MLflow Experiment](/concepts/mlflow-experiment.md) set up as described in the [setup quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment). ^[answer-and-context-relevance-judges-databricks-on-aws.md]

When using a custom judge model, the model endpoint must be accessible to the evaluation environment. For a `databricks` provider, the endpoint name must be a valid Databricks serving endpoint that the caller has permission to query. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – The set of predefined scorers (relevance, groundedness, safety, correctness) that can be customized.
- [RelevanceToQuery](/concepts/relevancetoquery.md) – Judge for response-to-query relevance.
- [RetrievalRelevance](/concepts/retrievalrelevance.md) – Judge for document-level retrieval relevance.
- LiteLLM Providers – The format for specifying model providers and endpoint names.
- [MLflow GenAI Evaluate](/concepts/mlflow-genai-evaluation.md) – The function that accepts configured judges for dataset evaluation.

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
