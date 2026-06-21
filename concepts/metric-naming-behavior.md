---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e540996129c8ff318d14b894cfb7f978c509ba0669bc1d5771de82df7d60ebf3
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metric-naming-behavior
    - MNB
    - metric-naming-behavior-in-scorers
    - MNBIS
    - metric-naming-conventions-for-mlflow-scorers
    - MNCFMS
    - metric-naming-conventions-for-scorers
    - MNCFS
    - Naming conventions in scorers
    - metric-naming-in-mlflow-scorers
    - MNIMS
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Metric naming behavior
description: Rules for how scorer metric names are derived from function names, Feedback.name fields, and Scorer.name fields
tags:
  - mlflow
  - scorers
  - naming
timestamp: "2026-06-18T10:58:07.094Z"
---

# Metric naming behavior

**Metric naming behavior** defines how MLflow determines the metric names that appear in evaluation and monitoring results when using code-based scorers. The naming rules depend on whether the scorer returns primitive values, [`Feedback`] objects, or lists of `Feedback` objects. Clear, consistent metric names are essential for readable evaluation results and dashboards, and all metrics must have distinct names. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming rules

When you define scorers using either the [`@scorer`] decorator or the [`Scorer`] class, MLflow applies the following rules to determine metric names: ^[code-based-scorer-reference-databricks-on-aws.md]

1. **If the scorer returns one or more `Feedback` objects**, the `Feedback.name` fields take precedence, when specified.
2. **For primitive return values or unnamed `Feedback` objects**, the function name (for the `@scorer` decorator) or the `Scorer.name` field (for the `Scorer` class) is used.

The following table summarizes metric naming behavior:

| Scorer return type | Metric name source |
|---|---|
| Primitive value (int, float, bool, str) | Function name (decorator) or `Scorer.name` (class) |
| Single `Feedback` object with `name` | `Feedback.name` |
| Single `Feedback` object without `name` | Function name (decorator) or `Scorer.name` (class) |
| `List[Feedback]` | Each `Feedback.name` (must be distinct) |

^[code-based-scorer-reference-databricks-on-aws.md]

## Distinct names requirement

For evaluation and monitoring, all metrics must have distinct names. If a scorer returns `List[Feedback]`, then each `Feedback` in the list must have a distinct name. Duplicate names can cause ambiguous results or errors in evaluation runs. ^[code-based-scorer-reference-databricks-on-aws.md]

## Best practices

Use clear, consistent names that indicate the scorer's purpose. Follow MLflow naming conventions such as `safety_check` or `relevance_monitor`. These names appear as metric names in your evaluation and monitoring results and dashboards. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Code-based scorer](/concepts/code-based-scorers.md) — Custom scoring functions for evaluating AI applications
- [@scorer decorator](/concepts/scorer-decorator.md) — The recommended way to define code-based scorers
- [Scorer class](/concepts/scorer-class.md) — Alternative approach for scorers requiring state management
- [Feedback Object](/concepts/feedback-object.md) — Rich assessment values with scores, rationales, and metadata
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The broader evaluation framework that uses scorers
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Captures spans and metadata used by scorers

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
