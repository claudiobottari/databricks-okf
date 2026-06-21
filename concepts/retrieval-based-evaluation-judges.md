---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15543f68e2171d0b7ba95ac1713f60377af3a5fe58f9334045ed805e113b6bd3
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - retrieval-based-evaluation-judges
    - REJ
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Retrieval-based evaluation judges
description: A family of built-in LLM judges (RetrievalRelevance, RetrievalGroundedness, RetrievalSufficiency) focused specifically on evaluating the quality of retrieval-augmented generation (RAG) systems.
tags:
  - rag
  - llm-evaluation
  - retrieval
  - mlflow
timestamp: "2026-06-18T10:55:19.511Z"
---

# Retrieval-based evaluation judges

**Retrieval-based evaluation judges** are a category of [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that assess the quality of retrieval-augmented generation (RAG) applications by evaluating how well retrieved context supports the generated response. These judges use Databricks-hosted LLMs to score dimensions such as relevance, groundedness, and sufficiency of retrieved information. ^[built-in-llm-judges-databricks-on-aws.md]

## Available retrieval judges

MLflow provides several predefined retrieval-based judges, each evaluating a specific quality dimension:

| Judge | Arguments | Requires ground truth | What it evaluates |
|-------|-----------|----------------------|-------------------|
| `RetrievalRelevance` | `inputs`, `outputs` | No | Is the retrieved context directly relevant to the user's request? |
| `RetrievalGroundedness` | `inputs`, `outputs` | No | Is the response grounded in the information provided in the context? Is the agent hallucinating? |
| `RetrievalSufficiency` | `inputs`, `outputs`, `expectations` | Yes | Does the context provide all necessary information to generate a response that includes the ground truth facts? |

^[built-in-llm-judges-databricks-on-aws.md]

## How retrieval judges work

Retrieval judges evaluate the relationship between the user's input, the retrieved context, and the model's output. They are designed specifically for RAG architectures where an external retrieval step provides context that the language model uses to generate its response. ^[built-in-llm-judges-databricks-on-aws.md]

### RetrievalRelevance

The `RetrievalRelevance` judge assesses whether the retrieved context chunks are directly relevant to the user's query. This helps identify cases where the retrieval system returns irrelevant or tangentially related documents that could degrade response quality. ^[built-in-llm-judges-databricks-on-aws.md]

### RetrievalGroundedness

The `RetrievalGroundedness` judge evaluates whether the model's response is factually supported by the retrieved context. This is critical for detecting hallucination — when the model generates information not present in the provided context. A low groundedness score indicates the model may be inventing facts or drawing unsupported conclusions. ^[built-in-llm-judges-databricks-on-aws.md]

### RetrievalSufficiency

The `RetrievalSufficiency` judge requires ground truth (`expectations`) and evaluates whether the retrieved context contains all the information needed to produce a response that includes the expected facts. This judge helps identify gaps in retrieval coverage where important information is missing from the context. ^[built-in-llm-judges-databricks-on-aws.md]

## Related judges

While not strictly retrieval-based, the `RelevanceToQuery` judge evaluates whether the final response is relevant to the user's request, complementing the retrieval-specific judges. The `Correctness` judge compares the response against ground truth to assess factual accuracy. ^[built-in-llm-judges-databricks-on-aws.md]

## When to use retrieval judges

Use retrieval-based judges when:

- Evaluating RAG applications where retrieval quality directly impacts response quality
- Debugging retrieval pipelines to identify irrelevant or missing context
- Monitoring production RAG systems for retrieval drift or degradation
- Comparing different retrieval strategies or chunking approaches

For situations where built-in judges don't fit your specific use case, you can build [Custom LLM Judges](/concepts/custom-llm-judges.md) or use Python [Code-based Scorers](/concepts/code-based-scorers.md). ^[built-in-llm-judges-databricks-on-aws.md]

## Next steps

- [Choose the LLM that powers a judge](/concepts/llm-as-a-judge.md)
- [Build a custom LLM judge](/concepts/custom-llm-judge.md) when built-in judges don't fit your use case
- Align judges with human feedback to improve accuracy on your domain

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
