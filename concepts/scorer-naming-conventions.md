---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a493d50404d57185c3e74ac4a28c3c2683cd0431bdf36be8c02b800fcb15116
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-naming-conventions
    - SNC
    - scorer-metric-naming-conventions
    - SMNC
    - scorer-naming-conventions-mlflow
    - SNC(
    - SYNC
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Scorer Naming Conventions
description: Rules for how metric names are derived from code-based scorers, based on function names, Feedback object names, or class names depending on return type.
tags:
  - mlflow
  - scorers
  - naming
  - evaluation
timestamp: "2026-06-19T14:12:43.337Z"
---

# Scorer Naming Conventions

**Scorer naming conventions** define how metric names are derived for code-based [custom scorers](/concepts/custom-scorers-mlflow-genai.md) used with `mlflow.genai.evaluate()`. The naming rules differ depending on whether the scorer is defined using the `@scorer` decorator or the `Scorer` base class, and on the return type (primitive, single `Feedback`, or list of `Feedback`).^[code-based-scorer-examples-databricks-on-aws.md]

## Naming Rules

### Decorator-based scorers (`@scorer`)

- **Returning a primitive value (bool, int, float, str) or a single `Feedback` without an explicit name:**  
  The name of the decorator function becomes the metric name.  
  *Example:* a function named `decorator_primitive` yields the metric name `decorator_primitive`.^[code-based-scorer-examples-databricks-on-aws.md]

- **Returning a single `Feedback` with an explicit `name` parameter:**  
  The value of `Feedback.name` is used as the metric name, overriding the function name.  
  *Example:* `Feedback(name="decorator_named_feedback", ...)` produces a metric named `decorator_named_feedback`.^[code-based-scorer-examples-databricks-on-aws.md]

- **Returning multiple `Feedback` objects:**  
  Each `Feedback` object must specify a unique `name`, and each name becomes a separate metric. The function name is ignored.  
  *Example:* returning `[Feedback(name="scorer_named_feedback_1", ...), Feedback(name="scorer_named_feedback_2", ...)]` creates two metrics.^[code-based-scorer-examples-databricks-on-aws.md]

### Class-based scorers (`Scorer` subclass)

Class-based scorers use the `name` field (a mandatory attribute of the Pydantic `Scorer` class) as the metric name, unless the `__call__` method returns a `Feedback` object with an explicit `name`.

- **Returning a primitive value:**  
  Metric name = `Scorer.name`.  
  *Example:* `ScorerPrimitive` with `name: str = "scorer_primitive"` yields metric `scorer_primitive`.^[code-based-scorer-examples-databricks-on-aws.md]

- **Returning a single `Feedback` without a name:**  
  Metric name = `Scorer.name`.  
  *Example:* `ScorerFeedbackUnnamed` with `name = "scorer_named_feedback"` produces metric `scorer_named_feedback`.^[code-based-scorer-examples-databricks-on-aws.md]

- **Returning a single `Feedback` with an explicit name:**  
  Metric name = `Feedback.name`, overriding `Scorer.name`.  
  *Example:* `ScorerFeedbackNamed` with `name = "scorer_feedback_named"` but returning `Feedback(name="scorer_named_feedback", ...)` yields metric `scorer_named_feedback`.^[code-based-scorer-examples-databricks-on-aws.md]

- **Returning multiple `Feedback` objects:**  
  Each `Feedback` must have a unique `name`, and those names become the metric names. The `Scorer.name` field is not used.  
  *Example:* `ScorerNamedFeedbacks` returning two `Feedback` objects with names `scorer_named_feedback_1` and `scorer_named_feedback_2`.^[code-based-scorer-examples-databricks-on-aws.md]

## Summary Table

| Definition method | Return type | Metric name source |
|------------------|-------------|--------------------|
| `@scorer` decorator | primitive or unnamed `Feedback` | Decorator function name |
| `@scorer` decorator | named `Feedback` | `Feedback.name` |
| `@scorer` decorator | list of `Feedback` | Each `Feedback.name` (must be unique) |
| `Scorer` subclass | primitive or unnamed `Feedback` | `Scorer.name` field |
| `Scorer` subclass | named `Feedback` | `Feedback.name` |
| `Scorer` subclass | list of `Feedback` | Each `Feedback.name` (must be unique) |

## Related Concepts

- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) – How to define code-based scorers for MLflow GenAI evaluation.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API that consumes scorers.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying scorers for continuous monitoring (class-based scorers are not supported for production monitoring).
- [Feedback Object](/concepts/feedback-object.md) – The `mlflow.entities.Feedback` structure used to return evaluation results.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
