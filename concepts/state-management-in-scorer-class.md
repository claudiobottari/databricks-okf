---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37c69caf0354da93293590cd0f46ce2a0d563066430ffff5c9563fb1e48bf8ae
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - state-management-in-scorer-class
    - SMISC
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: State management in Scorer class
description: When using the Scorer class, state must be managed with instance attributes (not mutable class attributes) to avoid sharing state across scorer instances.
tags:
  - mlflow
  - scoring
  - python
  - state-management
timestamp: "2026-06-19T17:44:42.697Z"
---

# State management in Scorer class

**State management in Scorer class** refers to the rules and patterns for managing mutable state when defining custom code-based scorers that use the [`Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.Scorer) base class. The `Scorer` class is a [Pydantic object](https://docs.pydantic.dev/latest/concepts/models/), which introduces specific considerations for how state is shared across instances. ^[code-based-scorer-reference-databricks-on-aws.md]

## The core rule: use instance attributes, not mutable class attributes

When writing scorers using the `Scorer` class, you must use instance attributes for any mutable state. Mutable class attributes — such as a `list` or `dict` defined directly in the class body — are **shared across all instances** of that scorer. This can lead to data corruption or unexpected behavior when multiple evaluations or monitoring runs use the same scorer class. ^[code-based-scorer-reference-databricks-on-aws.md]

The following example demonstrates the incorrect and correct patterns:

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback

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

## Why this matters

Because the `Scorer` class is a Pydantic object, class-level attributes with mutable default values (like `results = []`) are created once at class definition time and shared by all instances. When one instance appends data to the list, all other instances see the change. This can cause: ^[code-based-scorer-reference-databricks-on-aws.md]

- **Cross-contamination** between evaluation runs.
- **Unpredictable metrics** when state accumulates across evaluation calls.
- **Debugging difficulty** because the shared state is not obvious from inspecting a single instance.

By contrast, instance attributes initialized in `__init__` ensure each scorer instance has its own independent state. ^[code-based-scorer-reference-databricks-on-aws.md]

## Limitations for production monitoring

Scorers defined using the `Scorer` class are **not supported** for production monitoring. They can only be used in development evaluation with [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate). For production monitoring, use the [`@scorer` decorator](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.scorer) instead. The `@scorer` decorator does not require state management because it defines a function rather than a class. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — Overview of custom code-based scorers for evaluation and monitoring
- [@scorer decorator](/concepts/scorer-decorator.md) — The recommended alternative for defining scorers without class state management
- [Feedback objects](/concepts/feedback-objects.md) — Rich assessment objects that scorers can return
- [Custom scorer reference](/concepts/custom-scorers-mlflow-genai.md) — Complete reference for defining custom scorers

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
