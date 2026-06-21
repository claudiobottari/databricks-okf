---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a71ac071a8c7723e708fe99f7407876116d2c88f99d97af7560c55132141f032
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-object-structure
    - FOS
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: Feedback Object Structure
description: The output format of MLflow relevance judges, consisting of a 'value' field (yes/no) indicating relevance and a 'rationale' field explaining the judge's reasoning.
tags:
  - mlflow
  - llm-evaluation
  - api-design
timestamp: "2026-06-18T10:46:25.783Z"
---

# Feedback Object Structure

The **Feedback Object Structure** is the output format produced by MLflow's built-in GenAI judges (including `RelevanceToQuery` and `RetrievalRelevance`) when they evaluate the performance of a retrieval-augmented generation (RAG) or other AI application. The structure provides a standardized way to return assessment results with both a verdict and an explanation.

## Structure

A Feedback object contains two primary fields: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

- **`value`**: A string indicating the judge's verdict. This is `"yes"` if the context or response is relevant, and `"no"` if it is not relevant. ^[answer-and-context-relevance-judges-databricks-on-aws.md]
- **`rationale`**: A human-readable string explaining why the judge reached its verdict. This provides insight into the reasoning behind the assessment. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Usage

The Feedback object is returned when you invoke a judge directly for testing, or when you pass a judge to `mlflow.genai.evaluate` for running full evaluation on a dataset. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

When you invoke a judge directly, it returns a Feedback object that you can inspect immediately:

```python
assessment = RelevanceToQuery(name="my_relevance_to_query")(
    inputs={"question": "What is the capital of France?"},
    outputs="The capital of France is Paris.",
)
print(assessment)
# Feedback object with value and rationale
```

When you use a judge with `mlflow.genai.evaluate`, the function returns evaluation results that contain Feedback objects for each evaluated item. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Example

Here is a typical Feedback object as it would appear when printed:

```
Feedback(value="yes", rationale="The response directly addresses the question by stating that Paris is the capital of France.")
```

## Related concepts

- [RelevanceToQuery](/concepts/relevancetoquery.md) — The judge that produces a Feedback object evaluating if an app's response addresses the user's input
- [RetrievalRelevance](/concepts/retrievalrelevance.md) — The judge that produces a Feedback object evaluating if each retrieved document is relevant
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The framework for evaluating GenAI applications
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-built judges including relevance, groundedness, safety, and correctness
- Custom Judge Creation with make_judge|Custom Judge Creation — How to build specialized judges that also return Feedback objects

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
