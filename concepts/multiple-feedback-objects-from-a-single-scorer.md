---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8fb67f8ee2b7420671624a71c1feeefb9cee88fbea455f9081070c7aa20be2f
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple-feedback-objects-from-a-single-scorer
    - MFOFASS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Multiple Feedback objects from a single scorer
description: A single custom scorer can return a list of Feedback objects, each with a unique name, to assess multiple quality facets (e.g., PII, sentiment, conciseness) simultaneously.
tags:
  - mlflow
  - scorers
  - feedback
  - evaluation
timestamp: "2026-06-18T14:36:28.083Z"
---

# Multiple Feedback objects from a single scorer

A single code-based scorer can return a **list** of `Feedback` objects, allowing one function to assess multiple quality facets—such as PII, sentiment, conciseness, or response length—simultaneously. This pattern reduces the number of separate scorers you need to define and evaluate, especially when several lightweight checks naturally belong together. ^[code-based-scorer-examples-databricks-on-aws.md]

## How it works

When a [@scorer-decorated function](/concepts/scorer-decorator.md) returns a `list[Feedback]`, each element must have a **unique `name`**. That name becomes the metric name in the evaluation results. The MLflow evaluation framework automatically registers each named `Feedback` as a separate column in the output table. ^[code-based-scorer-examples-databricks-on-aws.md]

The example below defines a single scorer that returns two pieces of feedback:

1. `is_not_empty_check` – a boolean indicating whether the response is non-empty.
2. `response_char_length` – a numeric value for the character length of the response.

```python
import mlflow
from mlflow.genai.scorers import scorer
from mlflow.entities import Feedback, Trace
from typing import Any, Optional

@scorer
def comprehensive_response_checker(outputs: str) -> list[Feedback]:
    feedbacks = []
    # 1. Check if the response is not empty
    feedbacks.append(
        Feedback(name="is_not_empty_check", value="yes" if outputs != "" else "no")
    )
    # 2. Calculate response character length
    char_length = len(outputs)
    feedbacks.append(Feedback(name="response_char_length", value=char_length))
    return feedbacks

# Evaluate the scorer using the pre-generated traces
multi_feedback_eval_results = mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[comprehensive_response_checker]
)
```

After evaluation, the results contain two metric columns: `is_not_empty_check` and `response_char_length`. ^[code-based-scorer-examples-databricks-on-aws.md]

![Multi-feedback results](https://docs.databricks.com/aws/en/assets/images/multi-feedback-results-6498c7ba09fe1005adabf32abe6cc782.png)

## Naming conventions for multiple Feedback objects

When a scorer returns a list of `Feedback` objects, the names specified inside each `Feedback` object are used as the metric names. The following rules apply:

- Each `Feedback` in the list **must** have a distinct `name`.
- The function or class name of the scorer is **not used** when multiple `Feedback` objects are returned; the individual `Feedback.name` values take precedence. ^[code-based-scorer-examples-databricks-on-aws.md]

For example:

```python
@scorer
def decorator_named_feedbacks(outputs) -> list[Feedback]:
    return [
        Feedback(name="decorator_named_feedback_1", value=True, rationale="No errors"),
        Feedback(name="decorator_named_feedback_2", value=0.9, rationale="Very clear"),
    ]
```

This produces two metrics: `decorator_named_feedback_1` and `decorator_named_feedback_2`. ^[code-based-scorer-examples-databricks-on-aws.md]

The same rule holds for [Scorer (base class)|class-based scorers](/concepts/scorer-class.md):

```python
class ScorerNamedFeedbacks(Scorer):
    name: str = "scorer_named_feedbacks"  # Not used
    def __call__(self, outputs: str) -> List[Feedback]:
        return [
          Feedback(name="scorer_named_feedback_1", value=True, rationale="Good"),
          Feedback(name="scorer_named_feedback_2", value=1, rationale="ok"),
        ]
```

Here the class-level `name` is ignored, and the two `Feedback.name` values become the metric names. ^[code-based-scorer-examples-databricks-on-aws.md]

## Requirements

- The scorer must be defined using the `@scorer` decorator (or as a subclass of `Scorer`) and return a `list[Feedback]`.
- Each `Feedback` object must have a `name` attribute that is unique within the list.
- If a `Feedback` object does not specify a `name` and is returned inside a list, MLflow will raise an error or fall back to undefined behavior; the documentation strongly recommends always providing explicit names when returning multiple `Feedback` objects. ^[code-based-scorer-examples-databricks-on-aws.md]

## Use cases

- **PII detection + sentiment + conciseness**: A single scorer can check a response for personally identifiable information, gauge its tone, and measure its length.
- **Response quality + adherence to guidelines**: Combine an automated quality check with a rule-based compliance check.
- **Any scenario where multiple lightweight checks are logically related and you want to minimize the number of scorer definitions.**

## Supported evaluation modes

Multiple `Feedback` objects from a single scorer work in offline evaluation with `mlflow.genai.evaluate()`. For [Production monitoring for GenAI|production monitoring](/concepts/production-monitoring-for-genai-applications.md), custom scorers must use the `@scorer` decorator; class-based scorers are not supported in production. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) – Overview of the custom scorer framework.
- [Feedback (MLflow entity)](/concepts/feedback-mlflow-evaluation.md) – The data object that holds per-metric results.
- [@scorer decorator](/concepts/scorer-decorator.md) – The primary way to define a code-based scorer.
- [Scorer (base class)](/concepts/scorer-class.md) – Alternative definition approach for stateful scorers (offline only).
- MLflow Evaluation for GenAI – Offline and online evaluation pipeline.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
