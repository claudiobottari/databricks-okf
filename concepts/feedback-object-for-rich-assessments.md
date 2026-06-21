---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1e08fddfe8f6e4b435487e9ce203973dfcf2e3ca343e9c6fd19d07ac64ad933
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-object-for-rich-assessments
    - FOFRA
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Feedback object for rich assessments
description: Scorers can return Feedback objects with value, rationale, source, and metadata for detailed multi-metric evaluations.
tags:
  - mlflow
  - scoring
  - feedback
timestamp: "2026-06-19T17:44:32.687Z"
---

# Feedback object for rich assessments

The **Feedback object** is a structured data type in MLflow that enables detailed assessments with scores, rationales, and metadata, as opposed to simple scalar return values. It is the primary mechanism for returning rich evaluation results from custom code-based scorers in MLflow's evaluation and monitoring framework. ^[code-based-scorer-reference-databricks-on-aws.md]

## Overview

When a scorer returns a `Feedback` object (or a list of `Feedback` objects), the evaluation results include not only a score but also explanatory rationale, source attribution, and arbitrary metadata. This makes `Feedback` suitable for human review, LLM-as-judge evaluations, and any scenario where a simple pass/fail or numeric value is insufficient. ^[code-based-scorer-reference-databricks-on-aws.md]

## Structure

The `Feedback` object is defined in the `mlflow.entities` module. Its key fields are:

- **`value`**: The assessment score. Can be numeric, boolean, string, or other types. ^[code-based-scorer-reference-databricks-on-aws.md]
- **`rationale`**: A human-readable explanation of the assessment. ^[code-based-scorer-reference-databricks-on-aws.md]
- **`source`**: An optional `AssessmentSource` object indicating the origin of the assessment. Supported source types include `"HUMAN"`, `"CODE"`, and `"LLM_JUDGE"`. The `source_id` field can identify the specific annotator or tool. ^[code-based-scorer-reference-databricks-on-aws.md]
- **`metadata`**: An optional dictionary of additional metadata about the assessment, such as annotator email or version information. ^[code-based-scorer-reference-databricks-on-aws.md]
- **`name`**: An optional name for the feedback metric. When returning multiple `Feedback` objects, each must have a distinct `name`. ^[code-based-scorer-reference-databricks-on-aws.md]
- **`error`**: An optional field for capturing error details. Accepts a Python exception object directly or an `AssessmentError` object for structured error reporting with error codes. ^[code-based-scorer-reference-databricks-on-aws.md]

## Usage

### Single feedback

A scorer can return a single `Feedback` object for a detailed assessment:

```python
from mlflow.entities import Feedback, AssessmentSource

@scorer
def content_quality(outputs):
    return Feedback(
        value=0.85,
        rationale="Clear and accurate, minor grammar issues",
        source=AssessmentSource(
            source_type="HUMAN",
            source_id="grammar_checker_v1"
        ),
        metadata={
            "annotator": "me@example.com",
        }
    )
```

^[code-based-scorer-reference-databricks-on-aws.md]

### Multiple feedbacks

A scorer can return a list of `Feedback` objects to produce multiple distinct metrics from a single evaluation:

```python
@scorer
def comprehensive_check(inputs, outputs):
    return [
        Feedback(name="relevance", value=True, rationale="Directly addresses query"),
        Feedback(name="tone", value="professional", rationale="Appropriate for audience"),
        Feedback(name="length", value=150, rationale="Word count within limits")
    ]
```

^[code-based-scorer-reference-databricks-on-aws.md]

## Metric naming

When a scorer returns `Feedback` objects, the metric names displayed in evaluation results follow these rules:

- If the `Feedback` object has a `name` field specified, that name is used as the metric name.
- If the `Feedback` object has no `name`, the function name (for the `@scorer` decorator) or the `Scorer.name` field (for the `Scorer` class) is used.

All metrics must have distinct names. When returning a list of `Feedback` objects, each must have a distinct `name`. ^[code-based-scorer-reference-databricks-on-aws.md]

## Error handling

The `Feedback` object supports structured error reporting through its `error` parameter. When a scorer encounters an error, it can return a `Feedback` with `value=None` and error details:

```python
from mlflow.entities import AssessmentError, Feedback

@scorer
def is_valid_response(outputs):
    import json
    try:
        data = json.loads(outputs)
        # ... validation logic ...
        return Feedback(value=True, rationale="Valid JSON")
    except json.JSONDecodeError as e:
        return Feedback(error=e)  # Pass exception object directly
```

The `error` parameter accepts:
- **Python Exception**: Pass the exception object directly.
- **`AssessmentError`**: For structured error reporting with error codes and messages. ^[code-based-scorer-reference-databricks-on-aws.md]

Alternatively, MLflow can automatically capture exceptions that propagate from a scorer and create a `Feedback` object with `value=None` and the error details. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — The framework for defining custom evaluation logic.
- [@scorer decorator](/concepts/scorer-decorator.md) — The recommended way to define scorers that return Feedback objects.
- [Scorer class](/concepts/scorer-class.md) — An alternative for scorers requiring internal state (not supported for production monitoring).
- [MLflow Evaluation Runs](/concepts/mlflow-evaluation-runs.md) — Where Feedback-based metrics are displayed.
- [Production Monitoring](/concepts/production-monitoring.md) — Production monitoring uses Feedback objects for ongoing quality assessment.
- [AssessmentSource](/concepts/assessmentsource-entity.md) — The object for attributing the source of a feedback assessment.
- AssessmentError — The object for structured error reporting in feedback.

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
