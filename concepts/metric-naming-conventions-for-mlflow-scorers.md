---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f88230aa9bafc14f409b80e34135faab47b802697494ac15a8aff9377163739a
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metric-naming-conventions-for-mlflow-scorers
    - MNCFMS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Metric naming conventions for MLflow scorers
description: "Rules for how evaluation metric names are derived from scorers: function name for decorator-based scorers, Feedback.name for named feedback, class name for class-based scorers, with unique names required when returning multiple Feedback objects."
tags:
  - mlflow
  - scorers
  - naming
timestamp: "2026-06-19T17:44:01.474Z"
---

# Metric naming conventions for MLflow scorers

**Metric naming conventions for MLflow scorers** define how metric names are determined when using code-based scorers during MLflow Evaluation for GenAI. The naming behavior depends on the scorer's return type and whether the scorer is defined with the `@scorer` decorator or as a class-based `Scorer` subclass.

## Primitive return values

When a scorer returns a primitive value such as `bool`, `int`, `float`, or `str`, the scorer function name becomes the metric name. For decorator-based scorers, the metric name is the function name. For class-based scorers, the metric name is the value of the `name` field. ^[code-based-scorer-examples-databricks-on-aws.md]

## Single Feedback without a name

When a scorer returns a single [Feedback](/concepts/feedback-object.md) object without an explicit `name` parameter, the metric name defaults to the scorer function name (for decorator-based scorers) or the class `name` field (for class-based scorers). ^[code-based-scorer-examples-databricks-on-aws.md]

## Single Feedback with an explicit name

When a scorer returns a single `Feedback` object that includes an explicit `name` parameter, that name overrides the function name or class name and becomes the metric name. ^[code-based-scorer-examples-databricks-on-aws.md]

## Multiple Feedback objects

When a scorer returns a list of `Feedback` objects, each object must specify a unique `name` parameter. These names become the individual metric names in the evaluation results. The function name or class name is not used in this case. ^[code-based-scorer-examples-databricks-on-aws.md]

## Summary table

The following table summarizes how metric names are determined for each scenario:

| Return type | `Feedback.name` set? | Metric name |
|---|---|---|
| Primitive (bool, int, float, str) | N/A | Function name / class `name` field |
| Single `Feedback` | No | Function name / class `name` field |
| Single `Feedback` | Yes | Value of `Feedback.name` |
| List of `Feedback` | Yes (required for each) | Values of each `Feedback.name` |

When returning a list of `Feedback` objects, you must specify a unique name for each `Feedback`. The function name or class name is not used when multiple `Feedback` objects are returned. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- [Code-based scorer examples](/concepts/code-based-scorers.md) — Comprehensive examples of different scorer patterns
- [Custom code-based scorers](/concepts/code-based-scorers.md) — Guide to defining custom scorers for MLflow Evaluation
- [Feedback Object](/concepts/feedback-object.md) — The feedback structure used to convey scorer results
- [Scorer class](/concepts/scorer-class.md) — Base class for stateful scorer implementations
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying scorers for continuous monitoring (note: class-based scorers are not supported for production monitoring, only for offline evaluation)

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
