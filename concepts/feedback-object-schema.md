---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64dabbaa14dc845a38253fbba695d94b282e5790c221b0a3c2c37ebc9c996be2
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-object-schema
    - FOS
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: Feedback Object Schema
description: The structured output format returned by MLflow LLM judges, containing a 'value' field (yes/no) and a 'rationale' field explaining the judge's decision.
tags:
  - mlflow
  - llm-evaluation
  - api
timestamp: "2026-06-19T22:06:37.837Z"
---

# Feedback Object Schema

The **Feedback Object Schema** defines the structure of the `Feedback` object returned by MLflow's built-in LLM judges when evaluating GenAI applications. This schema standardizes how assessment results are represented, enabling consistent interpretation across different evaluation scenarios.

## Schema Structure

The `Feedback` object contains two primary fields:

- **`value`**: A string indicating the judgment result. For relevance judges, this is typically `"yes"` if the context is relevant or `"no"` if it is not relevant.
- **`rationale`**: A string providing an explanation of the judge's reasoning for the assigned value.

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Usage Context

The Feedback Object Schema is used when invoking MLflow's built-in LLM judges, such as [RelevanceToQuery](/concepts/relevancetoquery.md) and [RetrievalRelevance](/concepts/retrievalrelevance.md). These judges evaluate aspects of [Generative AI Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) by assessing whether responses address user queries or whether retrieved documents are contextually relevant.

When called directly, a judge returns a `Feedback` object with the schema described above. When passed to `mlflow.genai.evaluate`, the same structured feedback is collected for each evaluation input. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Example

A typical `Feedback` object looks like:

```python
{
    "value": "yes",
    "rationale": "The response directly addresses the user's question about the capital of France."
}
```

## Interpreting Feedback Values

The `value` field provides a binary relevance determination, while the `rationale` field offers diagnostic information. This structure helps developers understand not just whether a response or retrieval was relevant, but why the judge arrived at that conclusion. This diagnostic capability is particularly useful for debugging and improving RAG Applications. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) — The framework for automated quality assessment of GenAI outputs
- [RelevanceToQuery](/concepts/relevancetoquery.md) — A judge that evaluates if responses address user input
- [RetrievalRelevance](/concepts/retrievalrelevance.md) — A judge that evaluates retrieved document relevance
- [Generative AI Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) — The broader practice of assessing GenAI application quality
- RAG Applications — Retrieval-augmented generation systems that benefit from relevance assessment
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that processes Feedback objects

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
