---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ecea31b35a50a06ca9c00d97633671a9f147ede5ff3b1cfee8ec11cb1ec65b7
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - class-based-vs-decorator-based-scorer-definitions
    - CVDSD
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Class-based vs decorator-based scorer definitions
description: "Two approaches to defining MLflow scorers: the @scorer decorator for stateless functions (supported in both offline and production monitoring) and the Scorer base class for stateful Pydantic objects (offline evaluation only)."
tags:
  - mlflow
  - scorers
  - patterns
timestamp: "2026-06-19T17:44:24.907Z"
---

# Class-based vs Decorator-based Scorer Definitions

In MLflow Evaluation for GenAI, custom code-based scorers can be defined using either a decorator-based approach ([`@scorer`]()) or a class-based approach (subclassing [`Scorer`]()). Both approaches allow you to implement flexible evaluation metrics for AI agents and applications, but they differ in complexity, state management, and deployment options. ^[code-based-scorer-examples-databricks-on-aws.md]

## Decorator-Based Scorer Definitions

The decorator-based approach uses the `@scorer` decorator on a Python function. This is the simpler and more common pattern. The decorated function receives inputs such as `trace`, `inputs`, `outputs`, and `expectations`, and can return a primitive value, a [`Feedback`]() object, or a list of `Feedback` objects. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def exact_match(outputs: str, expectations: dict) -> bool:
    return outputs == expectations["expected_response"]
```

The decorator-based approach is well-suited for stateless scoring logic. It is the only form of custom scorer that can be registered for [Production Monitoring](/concepts/production-monitoring.md). ^[code-based-scorer-examples-databricks-on-aws.md]

## Class-Based Scorer Definitions

For scorers that require **state** – such as configuration fields, pre-loaded data, or settable thresholds – the decorator-based approach may not suffice. MLflow provides the [`Scorer`]() base class, which is a Pydantic object. You subclass it, define additional fields, and implement the scoring logic in the `__call__` method. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback

class ResponseQualityScorer(Scorer):
    name: str = "response_quality"          # mandatory field
    min_length: int = 50
    required_sections: list[str] | None = None

    def __call__(self, outputs: str) -> Feedback:
        # ... evaluation logic ...
        return Feedback(value=True, rationale="Response meets all quality criteria")
```

The class-based approach allows you to encapsulate complex evaluation logic with configurable parameters. However, it is **only supported for offline evaluation** using `mlflow.genai.evaluate()`. It cannot be registered for production monitoring. ^[code-based-scorer-examples-databricks-on-aws.md]

## Comparison & When to Use Each

| Aspect | Decorator-based (`@scorer`) | Class-based (`Scorer` subclass) |
| ------ | --------------------------- | ------------------------------- |
| **State management** | Stateless (no extra fields) | Can include state via Pydantic fields |
| **Complexity** | Simple, concise | More complex, but more flexible |
| **Offline evaluation** | Yes | Yes |
| **Production monitoring** | Yes | **No** |
| **Default metric name** | Function name (or explicit name in `Feedback`) | `name` field on the class (or explicit name in `Feedback`) |

Use the **decorator-based** approach for stateless scorers that you intend to deploy in production. Use the **class-based** approach when your scorer requires configurable parameters and will only be used during offline evaluation. ^[code-based-scorer-examples-databricks-on-aws.md]

## Naming Conventions (Common to Both Approaches)

The naming behavior for code-based scorers is consistent regardless of definition style:

- **Primitive return or single `Feedback` without a name:** The function name (for decorator) or the `name` field (for class) becomes the metric name.
- **Single `Feedback` with an explicit name:** The name in the `Feedback` object is used as the metric name.
- **Multiple `Feedback` objects:** Each must have a unique `name`, and those names become the metric names. The function or class `name` field is ignored. ^[code-based-scorer-examples-databricks-on-aws.md]

## Limitations

- **Production monitoring** is only possible with the decorator-based approach. Class-based `Scorer` subclasses cannot be registered for continuous monitoring of live traffic. ^[code-based-scorer-examples-databricks-on-aws.md]
- If a scorer requires state and also needs production deployment, you must refactor it to use the decorator pattern, typically by externalizing state (e.g., reading from configuration files or environment variables) rather than embedding it in the scorer object.

## Related Concepts

- Custom Code-Based Scorers – Overview of writing custom scorers in MLflow.
- [Production Monitoring](/concepts/production-monitoring.md) – Deploying scorers for continuous evaluation.
- MLflow Evaluation for GenAI – The broader evaluation framework.
- [Feedback Object](/concepts/feedback-object.md) – Data structure returned by scorers.
- [[MLflow Trace]] – Runtime execution data accessible inside scorers.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
