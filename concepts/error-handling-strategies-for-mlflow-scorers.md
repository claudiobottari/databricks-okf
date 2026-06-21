---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2299187fc665aa9a9d98ddcaddc5b367a25da3a21b256b164f3e9b87dfd4a876
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - error-handling-strategies-for-mlflow-scorers
    - EHSFMS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Error handling strategies for MLflow scorers
description: "Two approaches for handling errors in custom scorers: returning structured AssessmentError within a Feedback object, or letting exceptions propagate for MLflow to handle gracefully"
tags:
  - mlflow
  - error-handling
  - evaluation
timestamp: "2026-06-18T10:57:47.751Z"
---

# Error handling strategies for MLflow scorers

Custom code-based scorers in MLflow Evaluation for GenAI must handle errors gracefully to avoid disrupting the overall evaluation. MLflow provides two complementary error-handling approaches, and scorers can combine both within a single implementation. ^[code-based-scorer-examples-databricks-on-aws.md]

## Overview

When a scorer encounters an issue (e.g., missing data, malformed input, or an unexpected failure), MLflow supports two patterns:

1.  **Explicit error feedback** – The scorer returns a `Feedback` object containing an `AssessmentError` with a structured error code and message.
2.  **Exception-based handling** – The scorer raises an exception and lets MLflow surface the error gracefully.

In both cases, evaluation continues for other scorers and evaluation records even if one scorer fails. ^[code-based-scorer-examples-databricks-on-aws.md]

## Explicit error feedback

Use the `AssessmentError` class (from `mlflow.entities`) to return a well-defined error instead of a normal assessment value. This approach is best when the scorer can detect a recoverable condition and wants to report it in a structured way.

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
        # ... evaluation logic ...
        return Feedback(value=True, rationale="Valid response")
    except Exception as e:
        raise
```

^[code-based-scorer-examples-databricks-on-aws.md]

The `AssessmentError` object accepts two fields:

- `error_code` – A machine-readable string identifier for the error type.
- `error_message` – A human-readable description of the problem.

When the scorer returns a `Feedback` with a non‑`None` `error`, MLflow records the error alongside the scorer’s results without raising an unhandled exception. ^[code-based-scorer-examples-databricks-on-aws.md]

## Exception-based handling

If a scorer raises an exception, MLflow catches it internally and continues processing the remaining scorers and evaluation records. This is the simplest approach when the error is unexpected or when the scorer cannot provide a meaningful fallback value.

```python
@scorer
def resilient_scorer(outputs, trace=None):
    try:
        # ... some logic that might fail ...
        return Feedback(value=True, rationale="Valid response")
    except Exception as e:
        # Let MLflow handle the error gracefully
        raise
```

^[code-based-scorer-examples-databricks-on-aws.md]

The comment “Let MLflow handle the error gracefully” appears in the official example, indicating that raising an exception from a scorer is an accepted pattern. Evaluation continues for other scorers and data rows. ^[code-based-scorer-examples-databricks-on-aws.md]

## Combining both approaches

A single scorer can mix both strategies: detect specific recoverable issues and return an explicit `AssessmentError`, while letting unexpected or unrecoverable conditions propagate as exceptions. This is shown in the `resilient_scorer` example, which uses a try/except block: the `try` returns an `AssessmentError` for a known missing‑field case, and the `except` re‑raises the exception. ^[code-based-scorer-examples-databricks-on-aws.md]

## Best practices

- Use explicit `AssessmentError` when you can identify the specific failure mode (e.g., missing key, timeout, invalid format). This makes the error easier to track in evaluation logs.
- Use exception raising for truly unexpected failures; MLflow will log the error details automatically.
- Always wrap fallible external calls (e.g., LLM judge requests, file reads) in try/except blocks so that the scorer can decide whether to return an error feedback or let the exception propagate.

## Related concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) – Definition and creation of scorers
- [Feedback](/concepts/feedback-object.md) – The object used to return assessment results, including error feedback
- AssessmentError – Structured error representation for scorer feedback
- MLflow Evaluation for GenAI – The evaluation framework that invokes scorers
- [Production Monitoring](/concepts/production-monitoring.md) – Deploying scorers for continuous monitoring

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
