---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10a23bbdfbe2d78cc597032dd5012770f6f0f541922fac7ce3953c822cb0559d
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - error-handling-patterns-for-mlflow-scorers
    - EHPFMS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Error handling patterns for MLflow scorers
description: "Approaches for handling failures in custom scorers: returning AssessmentError via Feedback for graceful degradation, or raising exceptions to let MLflow handle errors, ensuring evaluation continues even when some scorers fail."
tags:
  - mlflow
  - scorers
  - error-handling
timestamp: "2026-06-19T17:44:08.794Z"
---

# Error handling patterns for MLflow scorers

When building custom code-based scorers for MLflow Evaluation, robust error handling ensures that evaluation runs continue even when individual scorers encounter problems. MLflow provides two complementary error-handling approaches that can be used singly or combined in the same scorer. ^[code-based-scorer-examples-databricks-on-aws.md]

## Pattern 1: Return `Feedback` with `AssessmentError` (expected errors)

For known, anticipated issues — such as a missing field in the trace output or an invalid input format — a scorer can return a [`Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object that contains an [`AssessmentError`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.AssessmentError). The `AssessmentError` carries an `error_code` string and a human-readable `error_message`. This approach lets the scorer communicate exactly why it could not produce a grade without halting the evaluation. The metric value for that sample is set to `None`. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.entities import Feedback, AssessmentError

@scorer
def resilient_scorer(outputs, trace=None):
    try:
        response = outputs.get("response")
        if not response:
            return Feedback(
                value=None,
                error=AssessmentError(
                    error_code="MISSING_RESPONSE",
                    error_message="No response field in outputs"
                )
            )
        # Normal evaluation logic ...
        return Feedback(value=True, rationale="Valid response")
    except Exception as e:
        # Pattern 2: let MLflow handle the error
        raise
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Pattern 2: Raise an exception (unexpected errors)

For unforeseen failures — such as an API call timeout or an unexpected data structure — the scorer can simply raise an exception. MLflow catches the exception, logs the error, and continues evaluating the remaining samples and scorers. This pattern is simpler to implement and is appropriate when there is no sensible way to produce a partial result. ^[code-based-scorer-examples-databricks-on-aws.md]

In the example above, the final `raise` statement re-throws any exception not handled by the `AssessmentError` path, letting MLflow manage the error automatically. ^[code-based-scorer-examples-databricks-on-aws.md]

## Graceful degradation of evaluation

Regardless of which pattern is used, MLflow ensures that a failing scorer does not abort the entire `mlflow.genai.evaluate()` run. Evaluation continues for other samples and other scorers, and the results table includes the error information for traces where the scorer failed. For details about how MLflow surfaces scorer errors in the evaluation output, see the [custom scorer reference](/concepts/custom-scorers-mlflow-genai.md)(https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorer-reference#error-handling). ^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- [Feedback](/concepts/feedback-object.md) — The object returned by a scorer to communicate grades, rationales, and errors.
- AssessmentError — The error structure returned inside a `Feedback` object for expected failures.
- [Custom scorers in MLflow](/concepts/custom-scorers-mlflow-genai.md) — Overview of defining and using code-based scorers.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that runs scorers against traces or datasets.
- [Production Monitoring](/concepts/production-monitoring.md) — Note: class-based scorers that use error handling are not supported in production monitoring; use the `@scorer` decorator instead.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
