---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f23d2038e66114986ef5d9f243e0759b289251233be707cf7adf4af9aed0849
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - retrieval-focused-evaluation
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Retrieval-Focused Evaluation
description: A family of built-in judges (RetrievalRelevance, RetrievalGroundedness, RetrievalSufficiency) that specifically evaluate the quality of retrieved context in RAG-based applications.
tags:
  - llm-evaluation
  - rag
  - retrieval
timestamp: "2026-06-19T09:11:54.632Z"
---

# Retrieval-Focused Evaluation

**Retrieval-Focused Evaluation** refers to the practice of assessing the quality of the retrieval component in a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) system. It evaluates how well the system retrieves relevant context from a knowledge base to support the generation of accurate, grounded responses.

## Overview

In RAG systems, the retrieval step is critical: if the wrong context is retrieved, even the best generative model cannot produce a correct answer. Retrieval-focused evaluation measures the relevance, sufficiency, and groundedness of the retrieved context independently from the quality of the generated response. ^[built-in-llm-judges-databricks-on-aws.md]

## Key Evaluation Dimensions

### Retrieval Relevance

**Retrieval Relevance** evaluates whether the retrieved context is directly relevant to the user's request. This judge analyzes the `inputs` (user query) and `outputs` (retrieved context) to determine if the context addresses the query appropriately. It does not require ground truth data. ^[built-in-llm-judges-databricks-on-aws.md]

### Retrieval Groundedness

**Retrieval Groundedness** evaluates whether the generated response is grounded in the information provided in the retrieved context. This judge helps detect hallucination — instances where the model generates information not supported by the retrieved documents. It analyzes `inputs` and `outputs` without requiring ground truth. ^[built-in-llm-judges-databricks-on-aws.md]

### Retrieval Sufficiency

**Retrieval Sufficiency** evaluates whether the retrieved context provides all necessary information to generate a response that includes the ground truth facts. This judge requires `expectations` (ground truth) to determine if the context is complete enough to answer the query correctly. ^[built-in-llm-judges-databricks-on-aws.md]

## Built-in Retrieval Judges

MLflow provides predefined [LLM Judges](/concepts/llm-judges.md) for retrieval-focused evaluation that use Databricks-hosted LLMs to score these dimensions automatically. These judges are available as part of the [Built-in LLM Judges](/concepts/built-in-llm-judges.md) suite and can be used without custom configuration. ^[built-in-llm-judges-databricks-on-aws.md]

| Judge | Arguments | Requires Ground Truth | What It Evaluates |
|-------|-----------|----------------------|-------------------|
| `RetrievalRelevance` | `inputs`, `outputs` | No | Is the retrieved context directly relevant to the user's request? |
| `RetrievalGroundedness` | `inputs`, `outputs` | No | Is the response grounded in the information provided in the context? Is the agent hallucinating? |
| `RetrievalSufficiency` | `inputs`, `outputs`, `expectations` | Yes | Does the context provide all necessary information to generate a response that includes the ground truth facts? |

^[built-in-llm-judges-databricks-on-aws.md]

## When to Use Retrieval-Focused Evaluation

Retrieval-focused evaluation is particularly important when:

- **Debugging retrieval pipelines**: Isolate whether poor response quality stems from retrieval failures or generation failures.
- **Tuning retrieval parameters**: Compare different chunking strategies, embedding models, or retrieval top-k values.
- **Monitoring production RAG systems**: Detect degradation in retrieval quality over time before it impacts end-user experience.
- **A/B testing retrieval configurations**: Compare retrieval performance across different system versions using consistent evaluation criteria.

## Relationship to Other Evaluation Types

Retrieval-focused evaluation complements other evaluation approaches:

- **Response Quality Evaluation** — Assesses the final generated response for relevance, correctness, and safety.
- **End-to-End Evaluation** — Evaluates the complete system from query to response, combining retrieval and generation quality.
- **[Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md)** — Analyzes the full execution trace, including which documents were retrieved and how they were used.

## Best Practices

- **Evaluate retrieval independently**: Use retrieval-specific judges (like `RetrievalRelevance`) to isolate retrieval quality from generation quality.
- **Include sufficiency checks**: When ground truth is available, use `RetrievalSufficiency` to ensure the retrieved context contains all necessary information.
- **Monitor groundedness**: Use `RetrievalGroundedness` to detect hallucination patterns where the model generates content not supported by retrieved documents.
- **Combine with custom judges**: For domain-specific retrieval requirements, create [Custom LLM Judges](/concepts/custom-llm-judges.md) that evaluate retrieval against your specific knowledge base structure.

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Custom LLM Judges](/concepts/custom-llm-judges.md)
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [Hallucination Detection](/concepts/hallucination-scorer.md)
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md)

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
