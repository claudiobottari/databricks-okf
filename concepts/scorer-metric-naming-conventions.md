---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7737e0b77b197b9902a6ce4ff9281f78a17503d35f5cef750f6c3f1e2eadfef1
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-metric-naming-conventions
    - SMNC
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Scorer metric naming conventions
description: Rules for how metric names are derived in MLflow evaluation runs from Feedback.name fields, function names, or Scorer.name fields.
tags:
  - mlflow
  - evaluation
  - naming
timestamp: "2026-06-19T14:12:59.812Z"
---

# Scorer metric naming conventions

**Scorer metric naming conventions** define how the names of custom [Code-based Scorers](/concepts/code-based-scorers.md) are translated into metric names in [MLflow Evaluation Runs](/concepts/mlflow-evaluation-runs.md) and monitoring dashboards. Following these conventions ensures that metrics are clearly identifiable and that naming conflicts are avoided.

## Overview

When you define scorers using either the `@scorer` decorator or the `Scorer` class, the metric names in the evaluation runs created by evaluation and monitoring follow specific rules. Use clear, consistent names that indicate each scorer's purpose, such as `safety_check` or `relevance_monitor`. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming rules

The metric naming behavior depends on the return type of the scorer:

1. If the scorer returns one or more [Feedback](/concepts/feedback-object.md) objects, then `Feedback.name` fields take precedence, if specified.
2. For primitive return values or unnamed `Feedback` objects, the function name (for the `@scorer` decorator) or the `Scorer.name` field (for the `Scorer` class) is used. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming with the `@scorer` decorator

When using the `@scorer` decorator, the function name serves as the default metric name for primitive return values:

```python
@scorer
def response_length(outputs: str) -> int:
    return len(outputs.split())
```

In this example, the metric name in evaluation results would be `response_length`. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming with the `Scorer` class

When using the `Scorer` class, you must define the `name` field to set the metric name:

```python
class CustomScorer(Scorer):
    name: str = "response_quality"
    # ...
```

If you return a list of `Feedback` objects, you must set the `name` field in each `Feedback` to avoid naming conflicts. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming with Feedback objects

When returning `Feedback` objects, the `Feedback.name` field takes precedence over the function or class name. This allows a single scorer to produce multiple named metrics:

```python
@scorer
def comprehensive_check(inputs, outputs):
    return [
        Feedback(name="relevance", value=True, rationale="Directly addresses query"),
        Feedback(name="tone", value="professional", rationale="Appropriate for audience"),
        Feedback(name="length", value=150, rationale="Word count within limits")
    ]
```

These would appear as separate metrics named `relevance`, `tone`, and `length` in the evaluation results. ^[code-based-scorer-reference-databricks-on-aws.md]

## Uniqueness requirements

For evaluation and monitoring, all metrics must have distinct names. If a scorer returns `List[Feedback]`, then each `Feedback` in the list must have a distinct name. ^[code-based-scorer-reference-databricks-on-aws.md]

## Best practices

When defining scorers, use clear, consistent names that indicate the scorer's purpose. These names appear as metric names in your evaluation and monitoring results and dashboards. Follow MLflow naming conventions such as `safety_check` or `relevance_monitor`. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md)
- [Feedback Objects in MLflow](/concepts/feedback-objects-in-mlflow.md)
- [MLflow Evaluation Runs](/concepts/mlflow-evaluation-runs.md)
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
