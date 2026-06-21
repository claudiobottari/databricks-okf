---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c673792dc8d2f8ce879b467fa0be008d13c138ce8c7cea114793789eb5a48b9
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - relevancetoquery-judge
    - Relevance to Query Judge
    - Relevance Judge
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: RelevanceToQuery Judge
description: An MLflow built-in LLM judge that evaluates whether a GenAI application's response directly addresses the user's input question without deviating into unrelated topics.
tags:
  - mlflow
  - llm-evaluation
  - genai
timestamp: "2026-06-19T22:06:26.179Z"
---

# RelevanceToQuery Judge

The **`RelevanceToQuery` judge** is a built-in [MLflow](/concepts/mlflow.md) LLM judge that evaluates whether a GenAI application's response directly addresses the user's input query without deviating into unrelated topics. It helps diagnose quality issues in [GenAI](/concepts/mlflow-genai-evaluate-api.md) and [RAG](/concepts/retrieval-augmented-generation-rag.md) (Retrieval-Augmented Generation) workflows by assessing the relevance of the final generated output. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Overview

`RelevanceToQuery` is part of a broader set of relevance judges in MLflow. It evaluates if your app's response directly addresses the user's input, whereas the [RetrievalRelevance Judge](/concepts/retrievalrelevance-judge.md) evaluates whether each document returned by your app's retriever is relevant to the input request. These judges work together to help pinpoint quality issues—if context isn't relevant, the generation step cannot produce a helpful response. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

For detailed API documentation, see the [MLflow RelevanceToQuery API reference](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.RelevanceToQuery), the [MLflow RetrievalRelevance API reference](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.RetrievalRelevance), and the [MLflow Relevance judges documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/rag/relevance/). ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Prerequisites

To run the `RelevanceToQuery` judge, you must meet the following prerequisites: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

1. Install MLflow and required packages:
   ```
   %pip install --upgrade "mlflow[databricks]>=3.4.0" openai "databricks-connect>=16.1"
   dbutils.library.restartPython()
   ```
2. Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).

## Trace Requirements

To use the `RelevanceToQuery` judge, the MLflow Trace must have the `inputs` and `outputs` attributes present on the Trace's root span. If these are missing, the judge will not function correctly. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## How to Use

You can invoke the `RelevanceToQuery` scorer in two primary ways: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Direct Invocation

You can test the judge with a single input by creating a `RelevanceToQuery` scorer object and passing it the input and output directly:

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery

assessment = RelevanceToQuery(name="my_relevance_to_query")(
    inputs={"question": "What is the capital of France?"},
    outputs="The capital of France is Paris.",
)
print(assessment)
```

### Invoke with `evaluate()`

For running full evaluations on a dataset, pass the scorer to `mlflow.genai.evaluate`:

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[RelevanceToQuery(...)]
)
```

## Selecting the Judge Model

By default, built-in judges use a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model by using the `model` argument when you create the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

Example of using a different judge model:

```python
from mlflow.genai.scorers import RelevanceToQuery

relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"  # Or any LiteLLM-compatible model
)
```

## Interpreting Results

The `RelevanceToQuery` judge returns a `Feedback` object with the following attributes: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

- **`value`**: "yes" if the response is relevant to the query, "no" if it is not.
- **`rationale`**: An explanation of why the judge found the response relevant or irrelevant.

## Related Judges and Concepts

- [RetrievalRelevance Judge](/concepts/retrievalrelevance-judge.md) — Evaluates if each document returned by your app's retriever is relevant to the input request.
- Answer and Context Relevance Judges — The parent page describing both relevance judges.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that hosts these judges.
- [LLM Judges](/concepts/llm-judges.md) — General concept for using LLMs to evaluate GenAI outputs.
- [Custom Judges](/concepts/custom-judges.md) — How to build specialized judges for your use case.

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
