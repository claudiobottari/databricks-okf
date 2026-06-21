---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 066fa98604ecc4589a90516757ea720bf3b31f4ce58517d4b8ff2be0c7284542
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metric-naming-in-mlflow-scorers
    - MNIMS
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Metric naming in MLflow scorers
description: Rules for how metric names are derived from scorers, with Feedback.name fields taking precedence over function/class names, requiring distinct names for multiple feedbacks.
tags:
  - mlflow
  - naming
  - metrics
  - scoring
timestamp: "2026-06-19T09:14:30.475Z"
---

# Metric naming in MLflow scorers

**Metric naming in MLflow scorers** refers to the rules and conventions that determine how evaluation metrics are named in [MLflow Evaluation Runs](/concepts/mlflow-evaluation-runs.md) and [Production Monitoring](/concepts/production-monitoring.md) dashboards. The naming behavior depends on whether a scorer returns primitive values, `Feedback` objects, or lists of `Feedback` objects, and whether the scorer is defined using the `@scorer` decorator or the `Scorer` class. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming rules

When you define scorers using either the `@scorer` decorator or the `Scorer` class, the metric names in evaluation runs follow two rules: ^[code-based-scorer-reference-databricks-on-aws.md]

1. If the scorer returns one or more `Feedback` objects, then `Feedback.name` fields take precedence, if specified.
2. For primitive return values or unnamed `Feedback`s, the function name (for the `@scorer` decorator) or the `Scorer.name` field (for the `Scorer` class) is used.

For evaluation and monitoring, all metrics must have distinct names. If a scorer returns `List[Feedback]`, then each `Feedback` in the list must have a distinct name. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming by scorer type

### `@scorer` decorator with primitive return values

When a scorer defined with the `@scorer` decorator returns a primitive value (such as `int`, `float`, `bool`, or `str`), the metric name is the function name. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def response_length(outputs: str) -> int:
    return len(outputs.split())
```

In this example, the metric appears as `response_length` in evaluation results.

### `@scorer` decorator with `Feedback` objects

When a scorer returns a single `Feedback` object, the metric name is the `Feedback.name` field if specified. If `Feedback.name` is not set, the function name is used instead. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def content_quality(outputs):
    return Feedback(
        name="quality_score",
        value=0.85,
        rationale="Clear and accurate, minor grammar issues"
    )
```

Here the metric appears as `quality_score`, not `content_quality`.

### `@scorer` decorator with lists of `Feedback` objects

When a scorer returns a list of `Feedback` objects, each `Feedback` must have a distinct `name` field. Those names are displayed as separate metrics in the evaluation results. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def comprehensive_check(inputs, outputs):
    return [
        Feedback(name="relevance", value=True, rationale="Directly addresses query"),
        Feedback(name="tone", value="professional", rationale="Appropriate for audience"),
        Feedback(name="length", value=150, rationale="Word count within limits")
    ]
```

This produces three separate metrics: `relevance`, `tone`, and `length`.

### `Scorer` class

When using the `Scorer` class, the `name` field is mandatory and sets the metric name. If you return a list of `Feedback` objects, you must set the `name` field in each `Feedback` to avoid naming conflicts. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
class CustomScorer(Scorer):
    name: str = "response_quality"
    # ...
```

The metric appears as `response_quality` in evaluation results.

## Naming conventions

Use clear, consistent names that indicate the scorer's purpose. Follow MLflow naming conventions such as `safety_check` or `relevance_monitor`. These names appear as metric names in evaluation and monitoring results and dashboards. ^[code-based-scorer-reference-databricks-on-aws.md]

## Summary table

| Scorer definition | Return type | Metric name used |
|---|---|---|
| `@scorer` decorator | Primitive value | Function name |
| `@scorer` decorator | Single `Feedback` | `Feedback.name` (if specified), otherwise function name |
| `@scorer` decorator | `List[Feedback]` | Each `Feedback.name` (must be distinct) |
| `Scorer` class | Primitive value | `Scorer.name` field |
| `Scorer` class | `Feedback` or `List[Feedback]` | `Feedback.name` (if specified), otherwise `Scorer.name` field |

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — How to define custom scorers using the `@scorer` decorator and `Scorer` class
- [Feedback objects](/concepts/feedback-objects.md) — Rich assessment objects with scores, rationales, and metadata
- [MLflow Evaluation Runs](/concepts/mlflow-evaluation-runs.md) — Where metric names appear in evaluation results
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
