---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c0e5f1f9656eed1cf0a1b0c4c6249b48c2549d74b79092c5a28df2f6992fa3f
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-objects
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
    - file: |-
        code-based-scorer-reference-databricks-on-aws.md |

        The `AssessmentSource` object itself has two fields: `source_type` (a string like `"HUMAN"`) and `source_id` (an optional identifier for the specific tool or person). ^[code-based-scorer-reference-databricks-on-aws.md
title: Feedback objects
description: Rich return type for scorers enabling detailed assessments with scores, rationales, metadata, and error information, supporting multiple feedback per scorer.
tags:
  - mlflow
  - evaluation
  - scoring
timestamp: "2026-06-19T09:14:54.465Z"
---

# Feedback Objects

**Feedback objects** are structured assessment results returned by [Code-based Scorers](/concepts/code-based-scorers.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md). They provide a rich, detailed evaluation of an AI application's output, including scores, rationales, source attribution, and metadata — in contrast to simple pass/fail or numeric values. ^[code-based-scorer-reference-databricks-on-aws.md]

## Purpose

Feedback objects allow scorers to communicate fine-grained quality judgments about a single trace or response. They are the primary mechanism for returning rich, multi‑dimensional evaluations from both development-time `mlflow.genai.evaluate()` calls and [production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) workflows. ^[code-based-scorer-reference-databricks-on-aws.md]

## Structure

A `Feedback` object is defined in `mlflow.entities` and supports the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `value` | Any (int, float, bool, string, etc.) | The assessment score or classification. ^[code-based-scorer-reference-databricks-on-aws.md] |
| `rationale` | Optional[str] | Free‑text explanation for the value. ^[code-based-scorer-reference-databricks-on-aws.md] |
| `source` | Optional[AssessmentSource] | Identifies the origin of the assessment (e.g., `"HUMAN"`, `"CODE"`, `"LLM_JUDGE"`). ^[code-based-scorer-reference-databricks-on-aws.md] |
| `metadata` | Optional[dict] | Arbitrary key‑value pairs for additional context (e.g., annotator email). ^[code-based-scorer-reference-databricks-on-aws.md] |
| `error` | Optional[AssessmentError] | Captures exception or structured error details (see [Error handling in scorers](/concepts/error-handling-in-scorers.md)). ^[code-based-scorer-reference-databricks-on-aws.md] |
| `name` | Optional[str] | A distinct name that becomes the metric name in evaluation results (see [Metric naming behavior](/concepts/metric-naming-behavior.md)). ^[code-based-scorer-reference-databricks-on-aws.md |

The `AssessmentSource` object itself has two fields: `source_type` (a string like `"HUMAN"`) and `source_id` (an optional identifier for the specific tool or person). ^[code-based-scorer-reference-databricks-on-aws.md]

## Usage in Scorers

Scorers (defined with the `@scorer` decorator or the `Scorer` class) return one or more `Feedback` objects to provide detailed assessment: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.entities import Feedback, AssessmentSource

@scorer
def content_quality(outputs):
    return Feedback(
        value=0.85,
        rationale="Clear and accurate, minor grammar issues",
        source=AssessmentSource(source_type="HUMAN", source_id="grammar_checker_v1"),
        metadata={"annotator": "me@example.com"},
    )
```

Multiple feedback objects can be returned as a list, each with a distinct name: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def comprehensive_check(inputs, outputs):
    return [
        Feedback(name="relevance", value=True, rationale="Directly addresses query"),
        Feedback(name="tone", value="professional", rationale="Appropriate for audience"),
        Feedback(name="length", value=150, rationale="Word count within limits"),
    ]
```

When a scorer returns a list of `Feedback` objects, every `Feedback` in the list must have a unique `name` field to avoid metric naming conflicts. ^[code-based-scorer-reference-databricks-on-aws.md]

## Error Handling

If a scorer encounters an error during evaluation, it can return a `Feedback` object with a `value` of `None` and populate the `error` field with either a Python exception object or a structured [`AssessmentError`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.AssessmentError) object. This allows the scorer to communicate error details (error code and message) gracefully without halting evaluation of other traces. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentError, Feedback

@scorer
def is_valid_response(outputs):
    try:
        # validation logic
        ...
    except ValueError as e:
        return Feedback(error=e)  # or AssessmentError
```

The `error` parameter accepts both Python exception objects and `AssessmentError` instances. When an exception propagates naturally from a scorer, MLflow automatically captures it and creates a `Feedback` object with the error details. ^[code-based-scorer-reference-databricks-on-aws.md]

## Metric Naming

When a scorer returns one or more `Feedback` objects, the metric name used in evaluation results is determined as follows: ^[code-based-scorer-reference-databricks-on-aws.md]

1. If a `Feedback` object has a `name` field, that value becomes the metric name.
2. For unnamed `Feedback` objects or primitive return values, the scorer's function name (with the `@scorer` decorator) or the `Scorer.name` field (for the `Scorer` class) is used.

All metrics in an evaluation run must have distinct names. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) – How to define scorers using the `@scorer` decorator or the `Scorer` class.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API that consumes Feedback objects.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying scorers that return Feedback objects in production.
- [AssessmentSource](/concepts/assessmentsource-entity.md) – Identifies the origin of a feedback assessment.
- AssessmentError – Structured error object for returning error details in a Feedback.
- [Metric naming behavior](/concepts/metric-naming-behavior.md) – Full reference for how metric names are derived from scorers.

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
2. code-based-scorer-reference-databricks-on-aws.md |

The `AssessmentSource` object itself has two fields: `source_type` (a string like `"HUMAN"`) and `source_id` (an optional identifier for the specific tool or person). ^[code-based-scorer-reference-databricks-on-aws.md
