---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b9b514eeebd006e9ac917999b1a057dd53ca6fa681a32d170ba2ee11486b52b
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - class-based-scorer-definition
    - CSD
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Class-based Scorer Definition
description: A stateful, Pydantic-based approach to defining MLflow scorers by subclassing the Scorer base class, supporting additional fields and complex logic (offline evaluation only).
tags:
  - mlflow
  - scorers
  - pydantic
  - evaluation
timestamp: "2026-06-19T14:12:49.177Z"
---

---

title: Class-Based Scorer Definition
summary: A stateful Scorer base class (Pydantic) for complex scorers requiring fields and initialization, supported for offline evaluation only.
sources:
  - code-based-scorer-examples-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:36:34.524Z"
updatedAt: "2026-06-19T09:13:41.986Z"
tags:
  - mlflow
  - scorers
  - class-based
  - offline
aliases:
  - class-based-scorer-definition
  - CSD
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Class-Based Scorer Definition

In [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) for GenAI, a **class-based scorer** is a custom scorer defined by subclassing the [`Scorer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer) base class, rather than using the [`@scorer` decorator](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.scorer). The `Scorer` class is a Pydantic object, so you can define additional fields and state that are available inside the scoring logic. ^[code-based-scorer-examples-databricks-on-aws.md]

## When to Use a Class-Based Scorer

The `@scorer` decorator is the simpler, stateless approach and is sufficient for most scoring tasks. A class-based scorer is only necessary when the scorer requires state — for example, configuration parameters such as a minimum response length, a list of required sections, or a reference to an external model client. These fields are declared on the class and can be set at instantiation. ^[code-based-scorer-examples-databricks-on-aws.md]

## Usage

To create a class-based scorer, subclass `Scorer`, define a mandatory `name` field, declare any additional fields, and override the `__call__` method with the scoring logic. The `__call__` method receives the same parameters as a decorator-based scorer (e.g., `outputs`, `inputs`, `trace`, `expectations`) and must return either a primitive value, a single [`Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html?highlight=feedback#mlflow.entities.Feedback) object, or a list of `Feedback` objects. ^[code-based-scorer-examples-databricks-on-aws.md]

The following example defines a `ResponseQualityScorer` that checks for minimum word count and required sections: ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback
from typing import Optional

class ResponseQualityScorer(Scorer):
    name: str = "response_quality"
    min_length: int = 50
    required_sections: Optional[list[str]] = None

    def __call__(self, outputs: str) -> Feedback:
        issues = []
        if len(outputs.split()) < self.min_length:
            issues.append(f"Too short (minimum {self.min_length} words)")
        missing = [s for s in self.required_sections if s not in outputs]
        if missing:
            issues.append(f"Missing sections: {', '.join(missing)}")
        if issues:
            return Feedback(value=False, rationale="; ".join(issues))
        return Feedback(value=True, rationale="Response meets all quality criteria")

response_quality_scorer = ResponseQualityScorer(required_sections=["# Summary", "# Sources"])
```

The instance can then be passed to `mlflow.genai.evaluate()`: ^[code-based-scorer-examples-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_quality_scorer]
)
```

## Naming Conventions

For class-based scorers, the metric name displayed in evaluation results is determined as follows: ^[code-based-scorer-examples-databricks-on-aws.md]

- **Returning a primitive value:** The metric name is the value of the `name` field on the class.
- **Returning a single `Feedback` object without a name:** The metric name is the `name` field of the class.
- **Returning a single `Feedback` object with a name:** That explicit name on the `Feedback` object overrides the class `name` field.
- **Returning a list of `Feedback` objects:** Each `Feedback` object must have a unique `name`. Those names become the metric names; the class `name` field is not used.

## Limitations

Class-based `Scorer` subclasses are **only supported for offline evaluation** with `mlflow.genai.evaluate()`. They cannot be registered for [Production Monitoring](/concepts/production-monitoring.md). To use custom scorers in production monitoring, you must use the [`@scorer` decorator](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers#scorer-decorator). ^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) — Overview of all types of custom scorers.
- [@scorer decorator](/concepts/scorer-decorator.md) — Simpler, stateless way to define a scorer.
- [Scorer Base Class](/concepts/scorer-class.md) — API reference for the `Scorer` class.
- [Feedback Object](/concepts/feedback-object.md) — The return type for complex scoring results.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deployment of scorers for continuous evaluation.
- Naming of Custom Scorers — Full rules for metric naming.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
