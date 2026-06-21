---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b94ce53b06a8a0a96ff7473ed42de3aa319e108595da273e57dc7e747c72acf9
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-naming-conventions-mlflow
    - SNC(
    - SYNC
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Scorer Naming Conventions (MLflow)
description: Rules determining how metric names are derived from decorator function names, Feedback object name fields, or Scorer class name fields.
tags:
  - mlflow
  - scorers
  - naming
  - metrics
timestamp: "2026-06-19T09:14:27.074Z"
---

# Scorer Naming Conventions (MLflow)

**Scorer Naming Conventions in MLflow** define how metric names are assigned to [custom code-based scorers](/concepts/code-based-scorers.md) during evaluation with `mlflow.genai.evaluate()`. The naming behavior depends on whether the scorer returns a primitive value, a single [Feedback Object](/concepts/feedback-object.md), or multiple feedback objects, and whether the scorer is defined using the `@scorer` decorator or the [Scorer base class](/concepts/scorer-class.md). ^[code-based-scorer-examples-databricks-on-aws.md]

## Overview

The naming conventions for MLflow [GenAI](/concepts/mlflow-genai-evaluate-api.md) scorers determine how evaluation results appear in the MLflow UI and in returned data structures. Each [[Scorers|scorer]] function or class instance produces one or more metric names. These conventions apply to both offline evaluation and [Production Monitoring](/concepts/production-monitoring.md) contexts, though production monitoring has specific limitations on which scorer types can be used. ^[code-based-scorer-examples-databricks-on-aws.md]

## Naming Conventions by Return Type

### Primitive Value (without a name)

When a scorer returns a primitive value (such as `int`, `float`, `bool`, or `str`) without an explicit name, the metric name is derived from the scorer function name. This is the default behavior for `@scorer`-decorated functions that return simple types. ^[code-based-scorer-examples-databricks-on-aws.md]

**Example:** `@scorerdef decorator_primitive(outputs: str) -> int` creates a metric named `"decorator_primitive"`. ^[code-based-scorer-examples-databricks-on-aws.md]

### Single Feedback Object without a Name

When a scorer returns a single [Feedback](/concepts/feedback-object.md) object without specifying a `name` parameter, the metric name is derived from the scorer function name. This is the default for `@scorer`-decorated functions returning `Feedback` objects without an explicit name. ^[code-based-scorer-examples-databricks-on-aws.md]

**Example:** `@scorerdef decorator_unnamed_feedback(outputs: Any) -> Feedback` creates a metric named `"decorator_unnamed_feedback"`. ^[code-based-scorer-examples-databricks-on-aws.md]

### Single Feedback Object with an Explicit Name

When a scorer returns a single `Feedback` object with an explicit `name` parameter, that name is used as the metric name. The `name` parameter overrides the default function-based naming. ^[code-based-scorer-examples-databricks-on-aws.md]

**Example:** `Feedback(name="decorator_named_feedback", value=True)` creates a metric named `"decorator_named_feedback"`. ^[code-based-scorer-examples-databricks-on-aws.md]

### Multiple Feedback Objects

When a scorer returns multiple `Feedback` objects (as a `list[Feedback]`), each `Feedback` object must specify a unique `name` parameter. The names specified in each `Feedback` object are preserved as separate metric names. ^[code-based-scorer-examples-databricks-on-aws.md]

**Example:** `return [Feedback(name="decorator_named_feedback_1", value=True), Feedback(name="decorator_named_feedback_2", value=0.9)]` creates two metrics: `"decorator_named_feedback_1"` and `"decorator_named_feedback_2"`. ^[code-based-scorer-examples-databricks-on-aws.md]

## Naming Conventions by Scorer Type

### `@scorer` Decorator Functions

Functions decorated with `@scorer` follow the naming conventions described above. The function name becomes the metric name unless overridden by an explicit `Feedback.name` or by returning multiple named `Feedback` objects. ^[code-based-scorer-examples-databricks-on-aws.md]

### Class-Based Scorers

When using the [Scorer base class](/concepts/scorer-class.md) with `Scorer(name: str)`, the `name` field is mandatory. For class-based scorers returning a primitive value, the metric name is the `name` field value. For class-based scorers returning a `Feedback` object without an explicit name, the metric name is the `name` field value. For class-based scorers returning a `Feedback` object with an explicit name, the `Feedback.name` overrides the class `name` field. For class-based scorers returning multiple `Feedback` objects, each `Feedback.name` is used as the metric name, and the class `name` field is not used. ^[code-based-scorer-examples-databricks-on-aws.md]

**Example:** `class ScorerFeedbackNamed(Scorer): name: str = "scorer_feedback_named"` creates a metric named `"scorer_feedback_named"`. ^[code-based-scorer-examples-databricks-on-aws.md]

## Summary Table

| Return Type | Naming Source | Example |
|---|---|---|
| Primitive value | Function/class name | `decorator_primitive` |
| Single `Feedback` (no name) | Function/class name | `decorator_unnamed_feedback` |
| Single `Feedback` (with name) | `Feedback.name` | `decorator_named_feedback` |
| Multiple `Feedback` objects | Unique `Feedback.name` for each | `decorator_named_feedback_1`, `decorator_named_feedback_2` |

## Best Practices

- Use unique names for each `Feedback` object in multi-feedback scorers to avoid metric collisions. ^[code-based-scorer-examples-databricks-on-aws.md]
- For production monitoring, use the `@scorer` decorator rather than class-based scorers, as class-based scorers are not supported for registration. ^[code-based-scorer-examples-databricks-on-aws.md]
- When returning multiple feedback objects, ensure each `Feedback` object has a distinct, descriptive name that clearly identifies the quality facet being assessed. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — Implementation patterns for custom evaluation metrics
- [Feedback objects](/concepts/feedback-objects.md) — Data structure for scorer results
- MLflow Evaluation for GenAI — Framework for evaluating AI agents
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying scorers for continuous evaluation

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
