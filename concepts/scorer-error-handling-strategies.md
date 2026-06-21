---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82aaeae6eb074eeafa27362a17b49bf5f7802f508fc1184ca96953f444b07d8e
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-error-handling-strategies
    - SEHS
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Scorer error handling strategies
description: "Two approaches for handling errors in MLflow scorers: letting exceptions propagate naturally or handling them explicitly with AssessmentError."
tags:
  - mlflow
  - error-handling
  - scoring
timestamp: "2026-06-19T14:13:10.090Z"
---

# Scorer error handling strategies

**Scorer error handling strategies** refer to the two approaches that [MLflow](/concepts/mlflow.md) provides for capturing and reporting errors when a custom [[Scorers|scorer]] fails during evaluation or monitoring. Proper error handling ensures that a single failing trace does not halt the entire evaluation run, and that error details are preserved for debugging.

## Overview

When a scorer encounters an error for a trace, MLflow can capture error details for that trace and then continue executing gracefully. MLflow supports two approaches: letting exceptions propagate (recommended) so that MLflow captures error messages automatically, or handling exceptions explicitly for customized error reporting. ^[code-based-scorer-reference-databricks-on-aws.md]

## Error Handling Approaches

### Let exceptions propagate (recommended)

The simplest and recommended approach is to let exceptions throw naturally from the scorer function. MLflow automatically catches the exception and creates a [Feedback](/concepts/feedback-object.md) object with:

- `value`: `None`
- `error`: The exception details, including the exception object, error message, and stack trace

The error information is then displayed in the evaluation results. Opening the corresponding row reveals the error details. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def my_scorer(outputs: str) -> float:
    # If this raises an exception, MLflow captures it automatically
    return len(outputs)
```

### Handle exceptions explicitly

For custom error handling or when you need to provide specific error messages, catch exceptions within the scorer and return a [Feedback](/concepts/feedback-object.md) object with `None` value and error details. The `error` parameter accepts:

- **Python Exception**: Pass the exception object directly.
- **AssessmentError**: For structured error reporting with an error code and message.

^[code-based-scorer-reference-databricks-on-aws.md]

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
        return Feedback(error=e)  # Can pass exception object directly
```

## Error details display

When an error occurs, the evaluation results show the error for the affected trace. Users can expand the corresponding row to see the full error message, exception type, and stack trace. This applies to both development evaluation and production monitoring workflows. ^[code-based-scorer-reference-databricks-on-aws.md]

## Best practices

- **Let exceptions propagate** unless you need to customize error codes or messages, as it reduces code complexity and ensures consistent error formatting. ^[code-based-scorer-reference-databricks-on-aws.md]
- When handling exceptions explicitly, use AssessmentError with descriptive `error_code` and `error_message` values to make debugging easier in dashboards. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- Code-based scorer reference – Full reference for scorer definitions
- [Feedback](/concepts/feedback-object.md) – The object used to return assessments and errors
- AssessmentError – Structured error reporting for scorers
- [@scorer decorator](/concepts/scorer-decorator.md) – The decorator used to define most scorers
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – How evaluators consume scorer results
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Where scorers run continuously

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
