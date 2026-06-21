---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0205eb34230d66c2830ad36aa285742b89a7cfe04a4f0ce2b24271f9d7e8795
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - relevancetoquery
    - RelevanceToQuery Scorer
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: RelevanceToQuery
description: An MLflow LLM judge that evaluates whether a GenAI app's response directly addresses the user's input without deviating into unrelated topics
tags:
  - llm-judge
  - relevance
  - mlflow
timestamp: "2026-06-19T09:00:12.800Z"
---

# RelevanceToQuery

**`RelevanceToQuery`** is a built-in [LLM judge](/concepts/llm-judges.md) provided by [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that evaluates whether a GenAI application’s response directly addresses the user’s input without deviating into unrelated topics. It is part of a set of relevance judges that help diagnose quality issues in RAG applications and other conversational systems.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Overview

The judge assesses if the response is relevant to the query. If the context retrieved by a RAG pipeline is not relevant, the generation step cannot produce a helpful response, so `RelevanceToQuery` is often used together with [RetrievalRelevance](/concepts/retrievalrelevance.md) to cover both the retrieval and generation stages.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Prerequisites

Before using `RelevanceToQuery`, set up the environment by installing MLflow and required packages, and create an MLflow experiment as described in the [setup quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
%pip install --upgrade "mlflow[databricks]>=3.4.0" openai "databricks-connect>=16.1"
dbutils.library.restartPython()
```

## Usage

`RelevanceToQuery` can be invoked directly on a single input for testing, or passed to `mlflow.genai.evaluate()` for batch evaluation on a dataset. The judge requires that the `inputs` and `outputs` fields are present on the Trace’s root span.^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Direct invocation example:**

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery

assessment = RelevanceToQuery(name="my_relevance_to_query")(
    inputs={"question": "What is the capital of France?"},
    outputs="The capital of France is Paris.",
)
print(assessment)
```

**Evaluation with `mlflow.genai.evaluate()`:**

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_app,
    scorers=[RelevanceToQuery()]
)
```

## Selecting the Judge Model

By default, `RelevanceToQuery` uses a Databricks-hosted LLM designed for quality assessments. You can override the judge model by providing the `model` argument in the format `<provider>:/<model-name>`. For example, to use a different Databricks serving endpoint:^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"
)
```

The `model` argument accepts any LiteLLM-compatible model provider. If `databricks` is used as the provider, the model name corresponds to the serving endpoint name.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Interpreting Results

The judge returns a `Feedback` object containing:

- **`value`**: `"yes"` if the response is relevant to the query, `"no"` if not.
- **`rationale`**: An explanation of why the judge determined relevance or irrelevance.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [RetrievalRelevance](/concepts/retrievalrelevance.md) – Evaluates relevance of retrieved documents.
- [LLM Judges](/concepts/llm-judges.md) – Overview of built-in and custom evaluators.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Framework for assessing GenAI applications.
- [Custom Judges](/concepts/custom-judges.md) – Creating specialized judges for specific criteria.
- [RAG evaluation](/concepts/evaluation-run.md) – Applying relevance judges in comprehensive evaluation.

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
