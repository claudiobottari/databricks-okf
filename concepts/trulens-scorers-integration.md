---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9592d73575fe69766e356ac0bdc2de86b22de68e47befc21d1171cc555b39c2e
  pageDirectory: concepts
  sources:
    - third-party-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trulens-scorers-integration
    - TSI
    - TruLens scorer documentation
    - TruLens scorers
    - TruLens scorers#Available TruLens scorers
  citations:
    - file: third-party-scorers-databricks-on-aws.md
title: TruLens Scorers Integration
description: MLflow integration with TruLens for analyzing agent execution traces with goal-plan-action alignment metrics like logical consistency and plan adherence
tags:
  - mlflow
  - trulens
  - evaluation
  - agents
timestamp: "2026-06-19T23:07:10.862Z"
---

# TruLens [[scorers|Scorers]] Integration

**TruLens [[scorers|Scorers]] Integration** enables you to use metrics from the TruLens evaluation framework directly within MLflow’s [`mlflow.genai.evaluate()`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).genai.html#mlflow.genai.evaluate) function. TruLens specializes in analyzing agent execution [Traces](/concepts/traces.md), providing goal‑plan‑action alignment metrics such as logical consistency, execution efficiency, plan adherence, and tool selection. ^[third-party-scorers-databricks-on-aws.md]

## Overview

TruLens [[scorers|Scorers]] are one of several third‑party integrations available through [MLflow](/concepts/mlflow.md). They are designed for use cases that require deep inspection of an agent’s reasoning and behavior across multiple steps. By plugging into the same unified evaluation interface, TruLens metrics can be combined with built‑in [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md) from other frameworks (e.g., DeepEval, RAGAS) in a single `mlflow.genai.evaluate()` call, with all results visualized together in the [MLflow](/concepts/mlflow.md) UI. ^[third-party-scorers-databricks-on-aws.md]

## When to Use TruLens [[scorers|Scorers]]

TruLens is most valuable when you need to analyze agent execution [Traces](/concepts/traces.md) with goal‑plan‑action alignment metrics. Specific situations include:

- Evaluating how well an agent’s plan aligns with the original goal.
- Measuring the logical consistency of a multi‑step reasoning chain.
- Assessing execution efficiency (e.g., number of steps taken vs. optimal).
- Checking whether the agent adheres to a predefined plan.
- Determining the appropriateness of tool selections during agent execution.

^[third-party-scorers-databricks-on-aws.md]

In general, start with [built‑in LLM judges](/concepts/built-in-llm-judges.md) for common tasks such as correctness, groundedness, and safety. Add third‑party [[scorers|Scorers]] like TruLens when you need specialized domain metrics that built‑in judges do not cover. ^[third-party-scorers-databricks-on-aws.md]

## How to Use

To use TruLens [[scorers|Scorers]] in [MLflow](/concepts/mlflow.md):

1. **Install the required package** – The TruLens Python package must be installed in your environment.
2. **Import the scorers** – Import the TruLens [Scorer class](/concepts/scorer-class.md) from `mlflow.genai.[[scorers|Scorers]].trulens` (exact module path depends on the integration; refer to the [TruLens scorer documentation](/concepts/trulens-scorers-integration.md) for the correct import).
3. **Create an instance** – Instantiate the scorer, optionally configuring thresholds or model references.
4. **Pass to `evaluate()`** – Include the scorer in the `scorers` list argument of `mlflow.genai.evaluate()`.

The general pattern is identical to the Quick example shown in the third‑party [[scorers|Scorers]] overview, except that the scorer import and instantiation reference the TruLens module. ^[third-party-scorers-databricks-on-aws.md]

## Related Concepts

- [Third-party scorers](/concepts/third-party-scorers-in-mlflow-genai.md) – Overview of all supported external evaluation frameworks.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Default evaluation metrics for common GenAI tasks.
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) – The core API for running [[scorers|Scorers]] and collecting results.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) – The broader practice of assessing agent behavior, for which TruLens provides targeted metrics.

## Sources

- third-party-scorers-databricks-on-aws.md

# Citations

1. [third-party-scorers-databricks-on-aws.md](/references/third-party-scorers-databricks-on-aws-3248b9c8.md)
