---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1620be2962ac0475b5dbe333c54770b1d2afbadec1dde9698ceeaa2769bf3e5d
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - error-handling-in-code-based-scorers
    - EHICS
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Error handling in code-based scorers
description: "Two approaches for handling scorer errors: letting exceptions propagate for automatic capture, or handling exceptions explicitly with Feedback objects and AssessmentError."
tags:
  - mlflow
  - error-handling
  - scoring
timestamp: "2026-06-19T09:14:19.576Z"
---

# Error handling in code-based scorers

**Error handling in code-based scorers** refers to the mechanisms by which [Code-based Scorers](/concepts/code-based-scorers.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) can gracefully capture evaluation failures without interrupting the entire evaluation run. When a scorer encounters an error for a single trace, MLflow can record the error details and continue processing the remaining traces. ^[code-based-scorer-reference-databricks-on-aws.md]

Two approaches are available: letting exceptions propagate (recommended) or handling exceptions explicitly. ^[code-based-scorer-reference-databricks-on-aws.md]

## Let exceptions propagate (recommended)[​](#let-exceptions-propagate-recommended "Direct link to Let exceptions propagate (recommended)")

The simplest approach is to let exceptions throw naturally. MLflow automatically captures the exception and creates a [`Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object with the following error details: ^[code-based-scorer-reference-databricks-on-aws.md]

- `value`: `None`
- `error`: The exception details, such as exception object, error message, and stack trace

The error information is displayed in the evaluation results. Opening the corresponding row in the UI reveals the error details (a screenshot shows an example of these error details). ^[code-based-scorer-reference-databricks-on-aws.md]

## Handle exceptions explicitly[​](#handle-exceptions-explicitly "Direct link to Handle exceptions explicitly")

For custom error handling or to provide specific error messages, you can catch exceptions manually and return a [`Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) with a `None` value and error details within the scorer function. The [`AssessmentError`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.AssessmentError) class provides structured error reporting with an error code. ^[code-based-scorer-reference-databricks-on-aws.md]

The following example validates that an output is valid JSON containing required fields, and returns a `Feedback` with an `AssessmentError` when fields are missing: ^[code-based-scorer-reference-databricks-on-aws.md]

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
        return Feedback(error=e)  # Can pass exception object directly to the error parameter
```

The `error` parameter accepts the following types of errors: ^[code-based-scorer-reference-databricks-on-aws.md]

- **Python Exception**: Pass the exception object directly.
- **[`AssessmentError`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.AssessmentError)**: For structured error reporting with error codes.

## Error details in Feedback[​](#error-details-in-feedback "Direct link to Error details in Feedback")

In both approaches, the resulting `Feedback` object stores error information. When a scorer returns a `Feedback` with an error, the evaluation run records the error alongside the trace, allowing you to inspect which traces failed and why. Open the corresponding row in the evaluation results to see the error details. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [Feedback Object](/concepts/feedback-object.md)
- AssessmentError
- [[MLflow Trace|MLflow traces]]

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
