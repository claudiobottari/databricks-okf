---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 562ec51e13648fa98d0e0a948182d0c2f5cf56afc6663daf6d596fae386167be
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metric-naming-conventions-for-scorers
    - MNCFS
    - Naming conventions in scorers
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Metric naming conventions for scorers
description: Metric names in evaluation results are determined by Feedback.name fields (if present) or the scorer function/class name, with distinct naming requirements.
tags:
  - mlflow
  - scoring
  - naming
timestamp: "2026-06-19T17:44:46.205Z"
---

Here is the wiki page for "Metric naming conventions for scorers".

---

## Overview

Scorers are evaluation functions that assess model outputs or trace data. Each scorer returns one or more metrics, and the **name** of each metric is what appears in evaluation dashboards, monitoring UIs, and result tables. Clear, consistent naming is essential for distinguishing metrics at a glance — for example, `safety_check` versus `relevance_monitor`. ^[code-based-scorer-reference-databricks-on-aws.md]

## How metric names are determined

When you define a scorer (via the `@scorer` decorator or the `Scorer` class), the metric name that appears in evaluation runs is resolved according to these rules:

1. **If the scorer returns one or more `Feedback` objects and the `Feedback.name` field is set, that name takes precedence.**  
2. **If no `Feedback.name` is provided** (or the return value is a primitive type), the metric name falls back to:
   - The **function name** (for `@scorer`-decorated functions).
   - The **`Scorer.name` field** (for `Scorer`-based classes).

^[code-based-scorer-reference-databricks-on-aws.md]

### Example: `Feedback.name` takes precedence
```python
@scorer
def my_checker(outputs: str) -> Feedback:
    return Feedback(name="quality_score", value=0.85)
```
In this example the metric appears as `quality_score` in the results, not `my_checker`.

## Uniqueness requirement

All metrics in a single evaluation or monitoring run must have **distinct names**. If a scorer returns a `List[Feedback]`, each `Feedback` in the list must carry a unique `name` — duplicate names cause a conflict and will be rejected. ^[code-based-scorer-reference-databricks-on-aws.md]

## Naming conventions and best practices

- **Use descriptive, consistent names** that indicate the scorer’s purpose – e.g., `safety_check`, `relevance_monitor`, `response_length`. ^[code-based-scorer-reference-databricks-on-aws.md]
- **Avoid generic names** like `score` or `result`; they make dashboards harder to interpret.
- **Follow MLflow naming conventions** such as lowercase with underscores where helpful.
- **When returning multiple feedbacks**, ensure each has a unique `name` so they appear as separate metrics in evaluation results.

## Related concepts

- [[Scorers|Scorer]] – an evaluation function that returns metrics or feedback.
- [Feedback Object](/concepts/feedback-object.md) – a rich return type that can carry a name, value, rationale, and metadata.
- [MLflow Evaluation Runs](/concepts/mlflow-evaluation-runs.md) – the context in which metric names are displayed.
- [Code-based Scorer Reference](/concepts/code-based-scorers-mlflow-genai.md) – full API reference for `@scorer` and `Scorer` class.

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
