---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5be89228299df77825856156c654f5735b34032400d9b32a03ebcd36e7cb2b1
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-class-pydantic-base-class
    - SC(BC
    - Scorer (base class)
    - Scorer Base Class
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Scorer class (Pydantic base class)
description: An alternative, Pydantic-based base class for defining scorers with internal state and custom fields, supporting more flexibility than the @scorer decorator.
tags:
  - mlflow
  - evaluation
  - scoring
  - pydantic
timestamp: "2026-06-19T14:13:01.312Z"
---

# Scorer class (Pydantic base class)

The **`Scorer` class** is a Pydantic-based base class provided by `mlflow.genai.scorers` for defining custom code-based scorers with internal state and advanced customization. It serves as an alternative to the simpler [`@scorer` decorator] for cases where scorer logic requires mutable state or additional configuration fields.^[code-based-scorer-reference-databricks-on-aws.md]

## Overview

The `Scorer` class extends [`mlflow.genai.Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.Scorer) and is built on [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/). This design allows developers to define extra fields that are automatically validated and can be used within the evaluation logic. Scorers defined using this class are intended for offline evaluation via `mlflow.genai.evaluate()`; they are **not** supported for [production monitoring].^[code-based-scorer-reference-databricks-on-aws.md]

For most use cases, the `@scorer` decorator is recommended because it is simpler and fully compatible with production monitoring. Use the `Scorer` class only when you need internal state or parameterized logic that cannot be achieved with the decorator.^[code-based-scorer-reference-databricks-on-aws.md]

## Definition and required fields

When subclassing `Scorer`, the `name` field **must** be defined. This field sets the metric name that appears in evaluation results. If the scorer returns a list of [`Feedback`] objects, each `Feedback` in that list must also have its own `name` field to avoid naming conflicts.^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback
from typing import Optional

class CustomScorer(Scorer):
    # The `name` field is mandatory
    name: str = "response_quality"

    # Define additional fields for configuration or state
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

## The `__call__` method

The `__call__` method contains the actual evaluation logic. Its signature can accept any subset of the standard evaluation arguments: `inputs`, `outputs`, `expectations`, and `trace`. The method can return a single [`Feedback`] object, a list of `Feedback` objects, or a primitive value (`int`, `float`, `bool`, `str`).^[code-based-scorer-reference-databricks-on-aws.md]

## State management

Because the `Scorer` class is a Pydantic model, it is important to use **instance attributes** for mutable state, not **class attributes**. Mutable class attributes (like lists or dictionaries defined directly on the class body) are shared across all instances and can lead to unexpected behavior. The correct approach is to initialize such state in `__init__` or use a Pydantic `Field` with `default_factory`.^[code-based-scorer-reference-databricks-on-aws.md]

```python
# WRONG: mutable class attribute (shared across all instances)
class BadScorer(Scorer):
    results = []
    name: str = "bad_scorer"

    def __call__(self, outputs, **kwargs):
        self.results.append(outputs)  # Causes issues
        return Feedback(value=True)

# CORRECT: instance attribute (per-instance state)
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

## Limitations

- **Production monitoring**: Scorers defined using the `Scorer` class are **not supported** for [production monitoring] workflows. Only scorers created with the `@scorer` decorator (or the related [registered scorer API]) can be deployed for continuous monitoring.^[code-based-scorer-reference-databricks-on-aws.md]
- **Serialisation**: Because the `Scorer` class relies on Pydantic, ensure that any additional fields are serialisable if the scorer needs to be saved or logged.

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — Overview of custom scoring approaches
- [@scorer decorator](/concepts/scorer-decorator.md) — Recommended alternative for most use cases
- [Feedback](/concepts/feedback-object.md) — Rich assessment objects returned by scorers
- [Production Monitoring](/concepts/production-monitoring.md) — Continuous evaluation of deployed applications
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline scoring
- Code-based scorer reference — Full API documentation for inputs, outputs, and error handling

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
