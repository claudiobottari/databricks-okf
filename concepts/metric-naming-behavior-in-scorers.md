---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 280fc26108753a027f1c93ee66525c64bc4473d344274e564e7236781cac34dd
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metric-naming-behavior-in-scorers
    - MNBIS
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Metric naming behavior in scorers
description: "Rules for how metric names are derived from scorers: Feedback.name takes precedence over function/Scorer.name, and all metrics must have distinct names."
tags:
  - mlflow
  - evaluation
  - naming-conventions
timestamp: "2026-06-18T14:36:47.775Z"
---

#Metric naming behavior in scorers

**Metric naming behavior in scorers** describes how [MLflow](/concepts/mlflow.md) derives the metric names that appear in evaluation and monitoring results when custom code-based scorers are used. Understanding this behavior is essential for creating clear, consistent dashboards and avoiding naming conflicts. ^[code-based-scorer-reference-databricks-on-aws.md]

## Precedence rules

When a scorer is defined using the [`@scorer` decorator](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/code-based-scorer-reference#-scorer-decorator) or the [`Scorer` class](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/code-based-scorer-reference#-scorer-class), the metric name is determined by the following rules, in order of precedence: ^[code-based-scorer-reference-databricks-on-aws.md]

1.  **`Feedback.name` takes precedence.** If the scorer returns one or more [Feedback](/concepts/feedback-object.md) objects, the `name` field of each `Feedback` object is used as the metric name, provided it is specified. ^[code-based-scorer-reference-databricks-on-aws.md]
2.  **Fall back to the function or scorer name.** For primitive return values (e.g., `int`, `float`, `bool`, `str`) or unnamed `Feedback` objects, the metric name is:
    - The **function name** when using the `@scorer` decorator.
    - The **`Scorer.name` field** when using the `Scorer` class. ^[code-based-scorer-reference-databricks-on-aws.md]

The following table summarizes the naming behavior: ^[code-based-scorer-reference-databricks-on-aws.md]

| Return type         | Source of metric name                                    |
|---------------------|----------------------------------------------------------|
| Primitive (int, float, bool, str) | Function name (decorator) or `Scorer.name` (class)                |
| Single `Feedback`   | `Feedback.name` if specified; otherwise function or `Scorer.name` |
| `List[Feedback]`    | Each `Feedback.name` (must be distinct)                  |

## Distinctness requirement

All metrics in an evaluation or monitoring run must have distinct names. When a scorer returns a list of `Feedback` objects, each `Feedback` in that list must have a unique `name` to avoid naming conflicts. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming conventions

Databricks recommends using clear, consistent names that indicate the scorer's purpose. Follow MLflow naming conventions such as `safety_check` or `relevance_monitor`. These names appear in [Evaluation Runs](/concepts/evaluation-runs.md) and production monitoring dashboards. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [@scorer decorator](/concepts/scorer-decorator.md) – The recommended way to define code-based scorers.
- [Scorer class](/concepts/scorer-class.md) – For scorers requiring internal state or advanced customization.
- [Feedback Object](/concepts/feedback-object.md) – The rich return type that supports named metrics, rationales, and metadata.
- [Custom code-based scorers](/concepts/code-based-scorers.md) – Overview of how to create and use scorers.
- [Naming conventions in scorers](/concepts/metric-naming-conventions-for-scorers.md) – Examples of naming patterns for common scenarios.
- [Evaluation Runs](/concepts/evaluation-runs.md) – The MLflow artifact that records metric names and values.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Where these metric names are used in dashboards.

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
