---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb74789db3884b9cd31ba704fbed65b4eaa79f2d6fb81be2b58fa6c071968f89
  pageDirectory: concepts
  sources:
    - ragas-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ragas-metric-categories
    - RMC
  citations:
    - file: ragas-scorers-databricks-on-aws.md
title: RAGAS Metric Categories
description: "The five categories of RAGAS metrics: RAG metrics, Agent and tool use metrics, Natural language comparison metrics, General purpose metrics, and Other tasks."
tags:
  - taxonomy
  - evaluation
  - categorization
timestamp: "2026-06-19T20:07:00.504Z"
---

# RAGAS Metric Categories

**RAGAS (Retrieval Augmented Generation Assessment)** metric categories group the evaluation metrics provided by the RAGAS framework into logical families based on what aspect of an LLM application they measure. MLflow integrates these metrics as scorers, allowing users to evaluate retrieval quality, answer generation, agent behavior, and text similarity. ^[ragas-scorers-databricks-on-aws.md]

## Available Categories

### RAG Metrics

These scorers evaluate retrieval quality and answer generation in retrieval-augmented generation (RAG) applications. They are the core metrics for assessing how well a RAG pipeline retrieves relevant context and generates faithful answers. Examples include Faithfulness and [ContextPrecision](/concepts/contextprecision-scorer.md). ^[ragas-scorers-databricks-on-aws.md]

### Agent and Tool Use Metrics

These scorers evaluate AI agent behavior, including tool invocation accuracy and goal achievement. They are designed for agentic workflows where an LLM must call external tools or take sequential actions. ^[ragas-scorers-databricks-on-aws.md]

### Natural Language Comparison

These scorers compare generated text against expected output using both semantic and deterministic methods. They are useful for tasks where a reference answer is available and the goal is to measure similarity or correctness. ^[ragas-scorers-databricks-on-aws.md]

### General Purpose

These scorers provide flexible, customizable evaluation logic. They can be adapted to different use cases by configuring the underlying metric definition. ^[ragas-scorers-databricks-on-aws.md]

### Other Tasks

This category includes additional metrics that do not fit neatly into the above groups, covering evaluation needs for specialized tasks. ^[ragas-scorers-databricks-on-aws.md]

## Using RAGAS Scorers in MLflow

All RAGAS metrics are available as scorers through `mlflow.genai.scorers.ragas`. LLM-based metrics require a `model` parameter (e.g., `model="databricks:/databricks-gpt-5-mini"`), while non-LLM metrics such as `ExactMatch` do not. Scorers can be called directly or used with `mlflow.genai.evaluate()`. A scorer can also be created dynamically by name using `get_scorer()`. ^[ragas-scorers-databricks-on-aws.md]

## Related Concepts

- [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) – The underlying evaluation framework.
- [MLflow](/concepts/mlflow.md) – The platform that integrates RAGAS scorers.
- [Retrieval Augmented Generation](/concepts/retrieval-augmented-generation-rag.md) – The application pattern these metrics evaluate.
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) – Broader context of evaluating LLM outputs.
- [Faithfulness Scorer](/concepts/faithfulness-scorer.md) – Example of an LLM-based RAG metric.
- [ContextPrecision Scorer](/concepts/contextprecision-scorer.md) – Example of a RAG metric.
- ExactMatch Scorer – Example of a non-LLM (deterministic) metric.

## Sources

- ragas-scorers-databricks-on-aws.md

# Citations

1. [ragas-scorers-databricks-on-aws.md](/references/ragas-scorers-databricks-on-aws-5240ee43.md)
