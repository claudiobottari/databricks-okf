---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23e4c92a022819a01eb7ababb3f0ad2a05db4b34fea6776e8cdcec79c4704c63
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-scorer-error-handling
    - MSEH
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: MLflow Scorer Error Handling
description: "Two approaches for handling errors in custom scorers: returning AssessmentError in a Feedback object, or letting exceptions propagate for MLflow to handle gracefully."
tags:
  - mlflow
  - scorers
  - error-handling
  - evaluation
timestamp: "2026-06-19T14:12:35.228Z"
---

# MLflow Scorer Error Handling

**MLflow Scorer Error Handling** refers to the mechanisms by which MLflow surfaces errors that occur during custom scorer execution in offline evaluation, and the patterns scorers can use to handle failures gracefully without aborting the entire evaluation run.

## Overview

When a custom code-based scorer encounters an error — for example, missing required input fields, malformed responses, or an external API failure — MLflow catches the exception and records it as part of the assessment results. This allows evaluation to continue for other records and scorers instead of failing immediately.^[code-based-scorer-examples-databricks-on-aws.md]

## Two Error-Handling Approaches

MLflow supports two distinct approaches for handling errors in custom scorers:

1. **Return a `Feedback` object with an `AssessmentError`** – The scorer detects the problem and returns a `Feedback` object where the `error` field is set to an `AssessmentError` containing an error code and message. The `value` field is set to `None` to indicate the assessment failed.
2. **Raise an exception** – The scorer raises a Python exception. MLflow catches it, records it as an error, and the evaluation loop moves on to the next record or scorer.

Both approaches can be combined within a single scorer, as shown in the example below.^[code-based-scorer-examples-databricks-on-aws.md]

## Example: Resilient Scorer

The following scorer demonstrates both patterns. It first checks whether the `outputs` dictionary contains a `response` key. If not, it returns a `Feedback` with an `AssessmentError`. For any other unexpected error inside the try block, it re-raises the exception and lets MLflow handle it.

```python
from mlflow.genai.scorers import scorer
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
        # Your evaluation logic
        return Feedback(value=True, rationale="Valid response")
    except Exception as e:
        # Let MLflow handle the error gracefully
        raise

results = mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[resilient_scorer]
)
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Graceful Handling of Missing Data

When designing scorers intended for both offline evaluation and [Production Monitoring](/concepts/production-monitoring.md), it is important to handle missing data gracefully. For example, production monitoring typically does not include `expectations` (ground truth), while offline evaluation often does. Scorers should check for the presence of optional fields like `expectations` and avoid crashing when they are absent.^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) – How to define flexible evaluation metrics using the `@scorer` decorator or `Scorer` base class.
- [Feedback Object](/concepts/feedback-object.md) – The structured return type for scorer assessments, which can include error details.
- AssessmentError – The entity used to represent a failed assessment within a `Feedback` object.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying scorers for continuous online evaluation where expectations are often absent.
- MLflow Evaluation for GenAI – The broader framework for evaluating generative AI agents and applications.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
