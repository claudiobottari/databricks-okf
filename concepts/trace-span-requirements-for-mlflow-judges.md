---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 160750a2d2e20928668f615f5b328f3cd82104f53874252f1f6c652a237fc67a
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-span-requirements-for-mlflow-judges
    - TSRFMJ
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: Trace Span Requirements for MLflow Judges
description: "MLflow judges require specific trace span configurations: RelevanceToQuery needs inputs and outputs on the root span, while RetrievalRelevance requires at least one span with span_type set to RETRIEVER."
tags:
  - mlflow
  - tracing
  - llm-evaluation
  - observability
timestamp: "2026-06-18T10:46:29.437Z"
---

# Trace Span Requirements for MLflow Judges

MLflow’s built-in LLM judges for evaluating GenAI applications rely on specific trace span metadata to function correctly. These requirements ensure that the judge can locate the relevant inputs, outputs, and intermediate retrieval steps within the MLflow Trace. The two relevance judges—`RelevanceToQuery` and `RetrievalRelevance`—each impose distinct span-level prerequisites. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## RelevanceToQuery — root span requirements

The `RelevanceToQuery` judge assesses whether a model’s response directly answers the user’s question. For it to work, the MLflow Trace’s **root span** must contain both `inputs` and `outputs`. These fields are typically set automatically when you use `@mlflow.trace` on the top-level function of your application. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

- **`inputs`**: The user’s query or input prompt.
- **`outputs`**: The model’s generated response.

If either is missing from the root span, the judge cannot evaluate relevance. When invoking the judge directly with `RelevanceToQuery(...)(inputs=..., outputs=...)`, you provide these values explicitly as arguments. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## RetrievalRelevance — RETRIEVER span requirement

The `RetrievalRelevance` judge evaluates whether each document returned by a retriever is relevant to the input request. It requires that **at least one span in the Trace has its `span_type` set to `"RETRIEVER"`**. This is typically achieved by decorating the retrieval function with `@mlflow.trace(span_type="RETRIEVER")`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

Without a `RETRIEVER` span, the judge has no retrieval documents to assess and will either fail or return an empty result. The judge inspects the documents returned by that span (as `Document` objects) to compute relevance scores. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Summary of span requirements

| Judge | Span requirement | Notes |
|---|---|---|
| `RelevanceToQuery` | Root span must have `inputs` and `outputs`. | Can be supplied directly when calling the judge without a Trace. |
| `RetrievalRelevance` | At least one span with `span_type="RETRIEVER"`. | Typically created via `@mlflow.trace(span_type="RETRIEVER")` on a retrieval function. |

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## General best practices

- Always ensure your top-level application function is traced (e.g., `@mlflow.trace`) so that the root span captures `inputs` and `outputs`.
- For RAG pipelines, explicitly mark the retrieval step with `@mlflow.trace(span_type="RETRIEVER")` to enable `RetrievalRelevance` evaluation.
- Other built-in judges (e.g., AI Chat Evaluation Judges|Groundedness, Safety, and Correctness judges) may have their own span requirements; consult the MLflow GenAI Documentation|MLflow documentation for each specific scorer. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related concepts

- MLflow Trace Span Types — The complete list of span types used in [MLflow Tracing](/concepts/mlflow-tracing.md)
- [GenAI Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) — Overview of evaluating GenAI apps with MLflow judges
- [RAG Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) — Detailed guidance on evaluating retrieval-augmented generation
- [Custom MLflow Judges](/concepts/custom-llm-judges.md) — How to build judges tailored to your own span structure

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
