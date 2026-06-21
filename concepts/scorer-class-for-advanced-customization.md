---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3748a4c84fcccb0e63a54574115d711c2ae9e139bcad04e6bc9de4e3cfe21aa
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-class-for-advanced-customization
    - SCFAC
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Scorer class for advanced customization
description: An alternative to the decorator pattern, using a Pydantic-based Scorer base class that supports internal state and custom fields, but not supported for production monitoring.
tags:
  - mlflow
  - scoring
  - pydantic
timestamp: "2026-06-19T17:44:44.514Z"
---

# Scorer class for advanced customization

The **`Scorer` class** is an alternative to the [`@scorer` decorator](code-based-scorer-reference-databricks-on-aws.md#-scorer-decorator) for defining custom code-based scorers in MLflow, intended for cases that require internal state or additional customization beyond what the decorator offers. The `Scorer` class is a [Pydantic object](https://docs.pydantic.dev/latest/concepts/models/), allowing you to define additional fields and use them within the `__call__` method. ^[code-based-scorer-reference-databricks-on-aws.md]

For most evaluation and monitoring scenarios, the `@scorer` decorator is recommended; the `Scorer` class should be used when your logic requires stateful behavior or more complex configuration. ^[code-based-scorer-reference-databricks-on-aws.md]

## Defining a Scorer

To create a custom scorer using the `Scorer` class, subclass `mlflow.genai.scorers.Scorer` and override the `__call__` method. The `name` field is mandatory and sets the metric name displayed in evaluation results. If the scorer returns a list of [`Feedback` objects](code-based-scorer-reference-databricks-on-aws.md#-rich-feedback), each `Feedback` must have a distinct `name` field to avoid naming conflicts. ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback
from typing import Optional

class CustomScorer(Scorer):
    # The `name` field is mandatory
    name: str = "response_quality"

    # Define additional fields
    my_custom_field_1: int = 50
    my_custom_field_2: Optional[list[str]] = None

    # Override the __call__ method to implement the scorer logic
    def __call__(self, outputs: str) -> Feedback:
        # Your logic here
        return Feedback(
            value=True,
            rationale="Response meets all quality criteria"
        )
```

## Production monitoring limitation

Scorers defined using the `Scorer` class are **not supported** for production monitoring. Only scorers created with the `@scorer` decorator can be used with production monitoring workflows. ^[code-based-scorer-reference-databricks-on-aws.md]

## State management

Because the `Scorer` class is a Pydantic object and can hold state, you must be careful to use instance attributes rather than mutable class attributes. Mutable class attributes are shared across all instances of the scorer, which can lead to unexpected behavior. ^[code-based-scorer-reference-databricks-on-aws.md]

**Incorrect** — shared state across instances:

```python
class BadScorer(Scorer):
    results = []  # Shared across all instances!
    name: str = "bad_scorer"

    def __call__(self, outputs, **kwargs):
        self.results.append(outputs)  # Causes issues
        return Feedback(value=True)
```

**Correct** — per-instance state:

```python
class GoodScorer(Scorer):
    results: list[str] = None
    name: str = "good_scorer"

    def __init__(self):
        self.results = []  # Per-instance state

    def __call__(self, outputs, **kwargs):
        self.results.append(outputs)  # Safe
        return Feedback(value=True)
```

## Related Concepts

- [Code-based Scorer](/concepts/code-based-scorers.md) – Overview of custom scorers
- [@scorer decorator](/concepts/scorer-decorator.md) – Recommended approach for most cases
- [Feedback](/concepts/feedback-object.md) – Rich output object for detailed assessments
- [Production Monitoring](/concepts/production-monitoring.md) – Feature that does not support Scorer class scorers
- [Evaluation Runs](/concepts/evaluation-runs.md) – Where metric names from Scorer classes appear

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
