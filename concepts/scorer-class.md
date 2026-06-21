---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd3695afee00331e352c4963d9b8ed4e8a77d79463607127f78ef8ed9b89a3b4
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-class
    - Scorer (base class)
    - Scorer Base Class
    - Scorer base class
    - Scorer (base class)|class-based scorers
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Scorer class
description: A Pydantic-based base class for defining scorers with internal state and custom logic, offering more flexibility than the @scorer decorator but not supported for production monitoring.
tags:
  - mlflow
  - evaluation
  - scoring
timestamp: "2026-06-19T09:14:09.031Z"
---

# Scorer class

The **`Scorer` class** is a [Pydantic](https://docs.pydantic.dev/latest/concepts/models/)-based base class in MLflow for defining custom evaluation scorers with internal state or advanced customization. It serves as an alternative to the [`@scorer` decorator](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorer-reference#-scorer-decorator) and provides greater flexibility for complex scoring logic that requires state management or additional configuration fields.^[code-based-scorer-reference-databricks-on-aws.md]

## When to use the `Scorer` class

For most use cases, the `@scorer` decorator is recommended because it is simpler and fully supported for both development evaluation and production monitoring. The `Scorer` class should be used only when your scoring logic requires internal state management or additional customization that cannot be achieved with the decorator.^[code-based-scorer-reference-databricks-on-aws.md]

> **Important**: Scorers defined using the `Scorer` class are **not supported** for production monitoring. For production monitoring, use the `@scorer` decorator exclusively.^[code-based-scorer-reference-databricks-on-aws.md]

## Definition requirements

A `Scorer` subclass must:

1. **Set the `name` field** – This defines the metric name that appears in evaluation results. If you return a list of [`Feedback`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/evaluation-runs) objects, each `Feedback` must also have a distinct `name` field to avoid naming conflicts.
2. **Override the `__call__` method** – This method implements the actual scoring logic. It receives the same inputs as a decorator-based scorer (`inputs`, `outputs`, `expectations`, `trace`) and must return a primitive value or one or more `Feedback` objects.
3. **Optional: Define additional fields** – Because `Scorer` is a Pydantic model, you can define extra instance fields and use them inside `__call__`.^[code-based-scorer-reference-databricks-on-aws.md]

### Example

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

^[code-based-scorer-reference-databricks-on-aws.md]

## State management

When using the `Scorer` class, state must be managed with **instance attributes**, not mutable class attributes. Mutable class attributes are shared across all instances of the scorer and can cause unexpected behavior during evaluation or monitoring.^[code-based-scorer-reference-databricks-on-aws.md]

### Correct vs. incorrect usage

```python
# WRONG: Don't use mutable class attributes
class BadScorer(Scorer):
    results = []  # Shared across all instances!
    name: str = "bad_scorer"
    def __call__(self, outputs, **kwargs):
        self.results.append(outputs)  # Causes issues
        return Feedback(value=True)

# CORRECT: Use instance attributes
class GoodScorer(Scorer):
    results: list[str] = None
    name: str = "good_scorer"
    def __init__(self):
        self.results = []  # Per-instance state
    def __call__(self, outputs, **kwargs):
        self.results.append(outputs)  # Safe
        return Feedback(value=True)
```

^[code-based-scorer-reference-databricks-on-aws.md]

## Naming behavior

Metric names in evaluation runs follow these rules for `Scorer` class scorers:

- If the scorer returns one or more `Feedback` objects, the `Feedback.name` fields take precedence (if specified).
- For primitive return values or unnamed `Feedback`s, the `Scorer.name` field is used as the metric name.

All metrics within a single evaluation run must have distinct names. When returning a list of `Feedback` objects, each must have a unique `name`.^[code-based-scorer-reference-databricks-on-aws.md]

## Limitations

- **Not supported for production monitoring** – Only the `@scorer` decorator is valid for registering scorers that run in production inference tables.^[code-based-scorer-reference-databricks-on-aws.md]
- **Requires explicit state management** – Developers must be careful to use instance attributes rather than mutable class attributes.^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [@scorer decorator](/concepts/scorer-decorator.md) – The recommended, simpler alternative for defining custom scorers
- MLflow log_feedback API|MLflow Feedback – Rich assessment object that can be returned from scorers
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The trace object passed to scorers containing span-level information
- [Production Monitoring](/concepts/production-monitoring.md) – Environment where `Scorer` class scorers are not supported
- Pydantic – The data validation library that `Scorer` is built on
- [Evaluation Runs](/concepts/evaluation-runs.md) – The evaluation context where scorers produce metrics
- [Code-based Scorers](/concepts/code-based-scorers.md) – General concept page for custom scorer definitions

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
