---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a57d4c1c45546b77a2d02d10a72553a00c4133de742e0bcaa795f271e994ce0
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - error-handling-in-scorers
    - EHIS
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Error handling in scorers
description: "Two approaches for handling scorer errors: letting exceptions propagate (recommended) or handling exceptions explicitly with AssessmentError and Feedback"
tags:
  - mlflow
  - scorers
  - error-handling
timestamp: "2026-06-18T10:58:11.655Z"
---

# Error handling in scorers

**Error handling in scorers** refers to the mechanisms by which [MLflow](/concepts/mlflow.md)-based code-based scorers capture, report, and recover from failures during evaluation and monitoring of AI applications. MLflow provides two approaches for handling errors in custom scorers: letting exceptions propagate automatically, or handling exceptions explicitly for custom error reporting.^[code-based-scorer-reference-databricks-on-aws.md]

## Letting exceptions propagate (recommended)

The simplest and recommended approach is to let exceptions throw naturally from the scorer function without catching them. When an unhandled exception occurs, MLflow automatically captures the error and creates a [Feedback](/concepts/feedback-object.md) object with the following error details:^[code-based-scorer-reference-databricks-on-aws.md]

- `value`: Set to `None`
- `error`: Contains the exception details, including the exception object, error message, and stack trace

The captured error information is displayed in the evaluation results. Users can open the corresponding row in the evaluation interface to see the full error details, including the exception object, error message, and stack trace.^[code-based-scorer-reference-databricks-on-aws.md]

## Handling exceptions explicitly

For scenarios requiring custom error handling or more specific error messages, developers can catch exceptions within the scorer function and return a `Feedback` object with `None` value and error details. This approach allows for structured error reporting with defined error codes.^[code-based-scorer-reference-databricks-on-aws.md]

The `error` parameter of the `Feedback` object accepts two types of errors:^[code-based-scorer-reference-databricks-on-aws.md]

- **Python Exception**: Pass the exception object directly.
- **[`AssessmentError`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.AssessmentError)**: For structured error reporting with error codes.

### Example: Custom error handling with JSON validation

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

^[code-based-scorer-reference-databricks-on-aws.md]

## Graceful continuation

Both error handling approaches allow MLflow to continue processing remaining traces when a scorer encounters an error for a specific trace. The system captures the error details for that trace and moves on to evaluate the next trace, ensuring that a single failure does not cause the entire evaluation or monitoring run to fail.^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — How to define custom scorers using the `@scorer` decorator or `Scorer` class
- [Feedback objects](/concepts/feedback-objects.md) — The data structure used to return evaluation results and error details
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure that provides input data to scorers
- [Production Monitoring](/concepts/production-monitoring.md) — Applying scorers in production environments with error handling

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
