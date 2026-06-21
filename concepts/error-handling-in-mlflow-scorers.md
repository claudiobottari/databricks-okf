---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6219fb40e43a96d19e87a041075f7174be7ed4c8be280b485f8b0713c9807430
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - error-handling-in-mlflow-scorers
    - EHIMS
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Error handling in MLflow scorers
description: "Two approaches for handling scorer errors: letting exceptions propagate (recommended) for automatic capture, or handling exceptions explicitly with Feedback and AssessmentError."
tags:
  - mlflow
  - error-handling
  - evaluation
timestamp: "2026-06-18T14:36:54.813Z"
---

# Error handling in MLflow scorers

**Error handling in MLflow scorers** refers to the mechanisms and best practices for managing failures that occur during code-based scoring of MLflow traces, enabling graceful degradation and detailed error capture without disrupting the overall evaluation or monitoring workflow.

## Overview

When a scorer encounters an error while processing a trace, MLflow provides two approaches for capturing error details and continuing execution: letting exceptions propagate automatically, or handling them explicitly for custom error reporting. Both approaches produce structured error information that appears in evaluation results. ^[code-based-scorer-reference-databricks-on-aws.md]

## Let exceptions propagate (recommended)

The simplest approach is to **let exceptions throw naturally**. MLflow automatically catches the exception and creates a [Feedback](/concepts/feedback-object.md) object with the following error details:

- `value`: set to `None`
- `error`: the exception details, including the exception object, error message, and stack trace

These error details are displayed in the evaluation results UI. Users can open the corresponding row in the results table to view the captured error information. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def my_scorer(outputs):
    # MLflow will automatically catch any exception thrown here
    # and create a Feedback object with error details
    data = json.loads(outputs)  # If this raises an exception, MLflow captures it
    # ... rest of scoring logic
```

## Handle exceptions explicitly

For **custom error handling** or when you need to provide specific error messages, catch exceptions manually and return a [Feedback](/concepts/feedback-object.md) object with `None` value and explicit error details. The `error` parameter accepts two types of values:

- **Python Exception**: Pass the exception object directly
- **AssessmentError**: For structured error reporting with error codes ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentError, Feedback
from mlflow.genai.scorers import scorer

@scorer
def is_valid_response(outputs):
    import json
    try:
        data = json.loads(outputs)
        required_fields = ["summary", "confidence", "sources"]
        missing = [f for f in required_fields if f not in data]
        if missing:
            return Feedback(
                error=AssessmentError(
                    error_code="MISSING_REQUIRED_FIELDS",
                    error_message=f"Missing required fields: {missing}",
                ),
            )
        return Feedback(
            value=True,
            rationale="Valid JSON with all required fields"
        )
    except json.JSONDecodeError as e:
        return Feedback(error=e)  # Can pass exception object directly
```

## Error feedback structure

When a scorer returns or produces a `Feedback` object with error information, the following fields are populated:

| Field | Description |
|-------|-------------|
| `value` | Set to `None` when an error occurs |
| `error` | Contains either the original exception or an `AssessmentError` with an error code and message |

The error information is displayed in the evaluation results UI, where users can click on the corresponding row to see the full error details, including the stack trace. ^[code-based-scorer-reference-databricks-on-aws.md]

## Best practices

- **Let exceptions propagate** for most cases, as this requires no additional code and MLflow handles error capture automatically.
- **Use explicit handling** when you need to distinguish between different failure modes, provide human-readable error codes, or log additional context.
- **Always return a `Feedback` object** from explicit error handling to maintain consistent output structure.
- **Use `AssessmentError`** for structured error reporting when errors have known categories that downstream systems might need to process programmatically.

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — The framework for defining custom scoring logic
- [Feedback objects](/concepts/feedback-objects.md) — The data structure for representing scorer outputs and errors
- AssessmentError — Structured error representation with error codes
- [Production monitoring with scorers](/concepts/production-monitoring-with-custom-scorer-functions.md) — Deploying scorers in production and handling errors at scale

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
