---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1a47bc626928d7b52229fd00f232f9dc3579bba506d797087ffafcaef68383a
  pageDirectory: concepts
  sources:
    - third-party-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - arize-phoenix-scorers-integration
    - APSI
    - API
    - Arize Phoenix integration
  citations:
    - file: third-party-scorers-databricks-on-aws.md
title: Arize Phoenix Scorers Integration
description: MLflow integration with Arize Phoenix offering a lightweight set of scorers for hallucination detection, relevance, toxicity, QA correctness, and summarization quality
tags:
  - mlflow
  - phoenix
  - evaluation
  - third-party
timestamp: "2026-06-19T23:07:25.809Z"
---

# [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) Integration

The **Arize Phoenix [[scorers|Scorers]] integration** is a third-party evaluation framework that wraps Arize Phoenix metrics as [MLflow Scorers](/concepts/mlflow-scorers.md). It plugs directly into `mlflow.genai.evaluate()`, giving you access to a focused set of evaluation metrics through the same unified interface used for [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and other custom [[scorers|Scorers]]. ^[third-party-scorers-databricks-on-aws.md]

## Why use [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md)

[Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) are designed for use cases that need a **lightweight, focused set of metrics** without the overhead of larger frameworks. The integration provides [[scorers|Scorers]] for: ^[third-party-scorers-databricks-on-aws.md]

- Hallucination detection
- Relevance assessment
- Toxicity identification
- QA correctness
- Summarization quality

These metrics complement [Built-in LLM Judges](/concepts/built-in-llm-judges.md) when you need domain-specific or deterministic evaluation that [Built-in Judges](/concepts/built-in-judges.md) do not cover. ^[third-party-scorers-databricks-on-aws.md]

## Integration overview

To use [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md), install the framework's package, import the desired scorer, and pass it to `mlflow.genai.evaluate()`. The integration follows the same pattern as other third-party scorers on Databricks (e.g., DeepEval, RAGAS, TruLens, Guardrails AI). ^[third-party-scorers-databricks-on-aws.md]

The combination of multiple third-party frameworks in a single `mlflow.genai.evaluate()` call is supported, allowing you to mix [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) with [[scorers|Scorers]] from other frameworks. Results are visualized together in the [MLflow](/concepts/mlflow.md) UI. ^[third-party-scorers-databricks-on-aws.md]

## When to use Arize Phoenix vs. other [[scorers|Scorers]]

Start with [Built-in LLM Judges](/concepts/built-in-llm-judges.md) for common needs like correctness, groundedness, and safety. Add [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) when you: ^[third-party-scorers-databricks-on-aws.md]

- Need a lightweight, focused set of metrics without requiring a full framework.
- Require hallucination detection, relevance assessment, toxicity identification, QA correctness, or summarization quality.
- Want deterministic, non-LLM evaluation metrics (e.g., semantic similarity without LLM calls) where applicable.
- Already use Arize Phoenix in your workflows and want to leverage other [MLflow](/concepts/mlflow.md) features.

## Related concepts

- [Third-party scorers](/concepts/third-party-scorers-in-mlflow-genai.md) – Overview of integrating external evaluation frameworks with [MLflow](/concepts/mlflow.md).
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Default [MLflow](/concepts/mlflow.md) evaluation metrics for common tasks.
- [Code-based Scorers](/concepts/code-based-scorers.md) – Custom [[scorers|Scorers]] implemented directly in Python.
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) – The unifying evaluation function for GenAI workloads.
- [DeepEval Scorers Integration](/concepts/deepeval-scorers-integration.md), [RAGAS Scorers Integration](/concepts/ragas-scorers-integration.md), [TruLens Scorers Integration](/concepts/trulens-scorers-integration.md), [Guardrails AI Scorers Integration](/concepts/guardrails-ai-scorers-integration.md) – Other supported third-party integrations.

## Sources

- third-party-scorers-databricks-on-aws.md

# Citations

1. [third-party-scorers-databricks-on-aws.md](/references/third-party-scorers-databricks-on-aws-3248b9c8.md)
