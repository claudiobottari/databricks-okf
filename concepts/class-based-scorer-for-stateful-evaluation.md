---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62d55c825bc427d33f5ec13694577172a7a1e069d394628cb4ec8b6e96746c0b
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - class-based-scorer-for-stateful-evaluation
    - CSFSE
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Class-based Scorer for stateful evaluation
description: A Pydantic-based Scorer base class for defining evaluation scorers that require state (additional fields), supported only for offline evaluation with mlflow.genai.evaluate()
tags:
  - mlflow
  - python
  - pydantic
timestamp: "2026-06-18T10:57:33.322Z"
---

# Class-based Scorer for stateful evaluation

**Class-based Scorer for stateful evaluation** refers to the practice of defining custom evaluation metrics in MLflow GenAI by subclassing the `Scorer` base class, which is a Pydantic object that can hold configuration state. This approach is used when a scorer requires persistent settings (e.g., length thresholds, required sections) that go beyond what the functional [`@scorer` decorator](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers#scorer-decorator) supports. Class-based scorers are supported only for offline evaluation with `mlflow.genai.evaluate()` and cannot be used for production monitoring. ^[code-based-scorer-examples-databricks-on-aws.md]

## When to use a class-based scorer

The `@scorer` decorator is the simplest way to define a custom scorer, but it cannot hold state across evaluations. If you need to parameterize a scorer — for example, setting a minimum response length or a list of required sections — the class-based approach allows you to define those constraints as fields on the scorer object. This design makes it easy to reuse the same scorer logic with different configurations. ^[code-based-scorer-examples-databricks-on-aws.md]

## Defining a class-based scorer

To create a class-based scorer:

1. Import `Scorer` from `mlflow.genai.scorers` and `Feedback` from `mlflow.entities`.
2. Subclass `Scorer` (which is a Pydantic `BaseModel`).
3. Declare a mandatory `name` field — this becomes the metric name in the evaluation results.
4. Add any additional fields you need (e.g., `min_length`, `required_sections`).
5. Override the `__call__` method to implement your scoring logic. The method can accept any combination of the standard parameters (`inputs`, `outputs`, `trace`, `expectations`, etc.) and must return a `Feedback` object (or a primitive value, or a list of `Feedback` objects).

Example from the documentation: ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback
from typing import Optional

class ResponseQualityScorer(Scorer):
    # The `name` field is mandatory
    name: str = "response_quality"

    # Define additional fields
    min_length: int = 50
    required_sections: Optional[list[str]] = None

    # Override the __call__ method to implement the scorer logic
    def __call__(self, outputs: str) -> Feedback:
        issues = []

        # Check length
        if len(outputs.split()) < self.min_length:
            issues.append(f"Too short (minimum {self.min_length} words)")

        # Check required sections
        missing = [s for s in self.required_sections if s not in outputs]
        if missing:
            issues.append(f"Missing sections: {', '.join(missing)}")

        if issues:
            return Feedback(
                value=False,
                rationale="; ".join(issues)
            )
        return Feedback(
            value=True,
            rationale="Response meets all quality criteria"
        )

# Instantiate with custom parameters
response_quality_scorer = ResponseQualityScorer(required_sections=["# Summary", "# Sources"])
```

## Using the scorer in evaluation

Pass the instantiated scorer to `mlflow.genai.evaluate()` in the `scorers` list, just as you would with a decorator-based scorer. The evaluation will run the `__call__` method on each record in the dataset. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
class_based_scorer_results = mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_quality_scorer]
)
```

## Naming conventions for class-based scorers

The metric name used in the output depends on the return type and the presence of a `name` inside the `Feedback` object. The following rules apply to class-based scorers: ^[code-based-scorer-examples-databricks-on-aws.md]

| Return type | `Feedback.name` set? | Metric name |
|---|---|---|
| Primitive (e.g., `int`) | N/A | The `name` field of the `Scorer` class |
| Single `Feedback` | No | The `name` field of the `Scorer` class |
| Single `Feedback` | Yes | The `Feedback.name` value |
| List of `Feedback` | Yes (each item) | Each `Feedback.name` value (must be unique) |

If the scorer returns multiple `Feedback` objects, each must have a unique `name`, and the class-level `name` field is not used as a metric name.

## Limitations

Class-based scorers are **only supported for offline evaluation** with `mlflow.genai.evaluate()`. They cannot be registered for production monitoring (online evaluation). To deploy custom scorers in production, you must use the `@scorer` decorator-based definition. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) — General overview of custom scorers in MLflow GenAI
- [@scorer decorator](/concepts/scorer-decorator.md) — The functional alternative for simple, stateless scorers
- [Feedback](/concepts/feedback-object.md) — The return object used by all custom scorers
- MLflow Evaluation for GenAI — The evaluation framework that uses these scorers
- [[MLflow Trace]] — The object that carries span and timing data accessible from scorers

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
