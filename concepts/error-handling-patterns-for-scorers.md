---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 408eb83bd942020d8cf799977b1263805eaa3bca47da76bb3818d4e8983dd235
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - error-handling-patterns-for-scorers
    - EHPFS
    - Error Handling and Resilience Patterns
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Error handling patterns for scorers
description: "MLflow supports two error handling approaches: letting exceptions propagate (recommended) or catching exceptions and returning Feedback with AssessmentError details."
tags:
  - mlflow
  - scoring
  - error-handling
timestamp: "2026-06-19T17:45:03.405Z"
---

# Error Handling Patterns for Scorers

**Error handling patterns for scorers** describes the recommended approaches for managing and reporting errors that occur during evaluation in code-based scorers. When a scorer encounters an error for a trace, MLflow provides mechanisms to capture error details while continuing execution gracefully.

## Overview

Scorers evaluate AI application outputs and may encounter various errors during their assessment logic. MLflow supports two primary error handling approaches: letting exceptions propagate (recommended) or handling exceptions explicitly. Both approaches allow the scorer to continue processing subsequent traces without interruption. ^[code-based-scorer-reference-databricks-on-aws.md]

## Recommended Approach: Let Exceptions Propagate

The simplest and recommended error handling pattern is to let exceptions throw naturally within the scorer function. MLflow automatically captures the exception and creates a [Feedback](/concepts/feedback-object.md) object with the following error details:

- `value`: Set to `None`
- `error`: Contains the exception details, including the exception object, error message, and stack trace

The error information is then displayed in the evaluation results. Users can open the corresponding row to view the detailed error information. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def my_custom_scorer(outputs):
    # Some logic that might raise an exception
    return len(outputs.split())
```

## Explicit Error Handling Pattern

For custom error handling or to provide specific, structured error messages, scorers can catch exceptions explicitly and return a [Feedback](/concepts/feedback-object.md) object with `None` value and error details. This pattern gives the scorer author full control over the error reporting format. ^[code-based-scorer-reference-databricks-on-aws.md]

The `error` parameter in [Feedback](/concepts/feedback-object.md) accepts the following types:

- **Python Exception**: Pass the exception object directly
- **AssessmentError**: For structured error reporting with error codes

```python
from mlflow.entities import AssessmentError, Feedback

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
        return Feedback(error=e)
```

## When to Use Each Pattern

- **Let exceptions propagate (recommended)**: Use when you want MLflow to automatically capture and report error details with minimal code. This is the simplest approach and works well for most scenarios.
- **Handle exceptions explicitly**: Use when you need custom error messages, structured error codes, or specific error handling logic that differs from the default exception behavior.

## Best Practices

- Let exceptions propagate for straightforward error handling to minimize code complexity.
- Handle exceptions explicitly only when you need to provide specific error messages or structured error reporting.
- Return [Feedback](/concepts/feedback-object.md) objects with `None` value and error details when using explicit handling.
- Use AssessmentError for structured error reporting that requires error codes.

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
