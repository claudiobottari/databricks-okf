---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb1697c6d3e46df0f22c428bcb279a2fe4552a2df71be0ac2a9a2f0df4fe78df
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.93
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - retrieval-quality-judges
    - RQJ
    - retrieval quality
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Retrieval Quality Judges
description: A family of built-in LLM judges (RetrievalRelevance, RetrievalGroundedness, RetrievalSufficiency) that evaluate the quality of retrieved context in RAG applications.
tags:
  - rag
  - llm-evaluation
  - databricks
  - retrieval
timestamp: "2026-06-19T14:11:11.632Z"
---

# Retrieval Quality Judges

**Retrieval Quality Judges** are a category of [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that evaluate the quality of retrieved context in retrieval-augmented generation (RAG) applications. These judges assess whether a GenAI application retrieves relevant, sufficient, and grounded information to support its responses. ^[built-in-llm-judges-databricks-on-aws.md]

## Overview

Retrieval quality judges are predefined scorers powered by Databricks-hosted LLMs. They evaluate the retrieval component of RAG architectures by analyzing the relationship between user inputs, retrieved context, and model outputs. These judges do not require ground truth data to operate, making them suitable for evaluation during development and [Production Monitoring](/concepts/production-monitoring.md). ^[built-in-llm-judges-databricks-on-aws.md]

## Available Retrieval Quality Judges

### Retrieval Relevance

The `RetrievalRelevance` judge evaluates whether the retrieved context is directly relevant to the user's request. It takes `inputs` and `outputs` as arguments and does not require ground truth. This judge helps identify cases where the retrieval system returns irrelevant or off-topic documents. ^[built-in-llm-judges-databricks-on-aws.md]

### Retrieval Groundedness

The `RetrievalGroundedness` judge assesses whether the response is grounded in the information provided in the context. It evaluates whether the agent is hallucinating — generating information not supported by the retrieved documents. This judge takes `inputs` and `outputs` as arguments and does not require ground truth. ^[built-in-llm-judges-databricks-on-aws.md]

### Retrieval Sufficiency

The `RetrievalSufficiency` judge determines whether the retrieved context provides all necessary information to generate a response that includes the ground truth facts. Unlike the other retrieval judges, this judge requires `expectations` (ground truth) in addition to `inputs` and `outputs`. It helps identify cases where additional retrieval or different sources are needed to fully answer the user's query. ^[built-in-llm-judges-databricks-on-aws.md]

## Usage

Retrieval quality judges are instantiated and applied using the MLflow evaluation API. They are commonly combined with other judge types — such as `RelevanceToQuery`, `Safety`, and `Correctness` — to provide a comprehensive quality assessment of RAG applications. ^[built-in-llm-judges-databricks-on-aws.md]

For detailed documentation on each judge, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/). ^[built-in-llm-judges-databricks-on-aws.md]

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — The full catalog of predefined judges available on Databricks
- [Custom LLM Judges](/concepts/custom-llm-judges.md) — Building custom evaluators when built-in judges don't fit your use case
- [RAG evaluation](/concepts/evaluation-run.md) — Broader evaluation strategies for retrieval-augmented generation systems
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges in production environments
- Align judges with human feedback — Improving judge accuracy on domain-specific data

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
