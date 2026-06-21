---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 09cbcf56cf78a95411da8dbbf4f77d65ed5d84971fefb771533521698cdfbd3c
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-feedback-scorer-pattern
    - MSP
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Multi-Feedback Scorer Pattern
description: A single custom scorer returning a list of Feedback objects to assess multiple quality facets in one pass, each with a unique metric name.
tags:
  - mlflow
  - scorers
  - feedback
  - multiple-metrics
timestamp: "2026-06-19T09:13:52.994Z"
---

# Multi-Feedback Scorer Pattern

The **Multi-Feedback Scorer Pattern** is a design pattern in MLflow Evaluation for GenAI where a single custom scorer returns multiple [Feedback](/concepts/feedback-object.md) objects, allowing one scorer to assess multiple quality facets of an AI agent's response simultaneously. This pattern reduces code duplication and provides a consolidated view of different evaluation dimensions within a single evaluation run. ^[code-based-scorer-examples-databricks-on-aws.md]

## Overview

In MLflow's evaluation framework, custom scorers can return either a single value or multiple [Feedback](/concepts/feedback-object.md) objects. The Multi-Feedback Scorer Pattern leverages the ability to return a list of `Feedback` objects, each with a unique name that becomes a separate metric name in the evaluation results. This enables a single scorer to evaluate aspects such as PII presence, sentiment, conciseness, and other quality criteria in one pass. ^[code-based-scorer-examples-databricks-on-aws.md]

## Implementation

To implement the Multi-Feedback Scorer Pattern, define a scorer function using the `@scorer` decorator that returns a list of `Feedback` objects. Each `Feedback` object must have a unique `name` attribute, which serves as the metric name in the evaluation output. ^[code-based-scorer-examples-databricks-on-aws.md]

### Basic Example

The following example demonstrates a scorer that returns two distinct feedback items for each trace: ^[code-based-scorer-examples-databricks-on-aws.md]

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
```

### Naming Conventions

When returning multiple `Feedback` objects, each must have a unique name specified in the `Feedback` object. The names become the metric names in the evaluation results. This differs from single-feedback scorers, where the function name or class name may serve as the metric name. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def decorator_named_feedbacks(outputs) -> list[Feedback]:
    return [
        Feedback(name="decorator_named_feedback_1", value=True, rationale="No errors"),
        Feedback(name="decorator_named_feedback_2", value=0.9, rationale="Very clear"),
    ]
```

For class-based scorers (offline evaluation only), the same pattern applies: ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback
from typing import List

class ScorerNamedFeedbacks(Scorer):
    name: str = "scorer_named_feedbacks"  # Not used when returning multiple Feedback objects
    
    def __call__(self, outputs: str) -> List[Feedback]:
        return [
            Feedback(name="scorer_named_feedback_1", value=True, rationale="Good"),
            Feedback(name="scorer_named_feedback_2", value=1, rationale="ok"),
        ]
```

## Use Cases

The Multi-Feedback Scorer Pattern is particularly useful for: ^[code-based-scorer-examples-databricks-on-aws.md]

- **Combined quality checks**: Evaluating multiple response quality dimensions (e.g., completeness, accuracy, tone) in a single scorer.
- **Content safety and compliance**: Checking for PII, profanity, and policy violations together.
- **Performance metrics**: Returning both boolean pass/fail indicators and numeric measurements (e.g., response length, latency).
- **Structured evaluation**: Providing both a score and a rationale for each assessment dimension.

## Results

When using the Multi-Feedback Scorer Pattern, the evaluation results contain separate columns for each named feedback item. For example, the `comprehensive_response_checker` scorer produces two columns: `is_not_empty_check` and `response_char_length`. ^[code-based-scorer-examples-databricks-on-aws.md]

## Limitations

- Class-based `Scorer` subclasses that return multiple feedback objects are supported for offline evaluation with `mlflow.genai.evaluate()` only. They cannot be registered for [Production Monitoring](/concepts/production-monitoring.md). ^[code-based-scorer-examples-databricks-on-aws.md]
- Each `Feedback` object in the returned list must have a unique name to avoid metric name collisions. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- Custom Code-Based Scorers — The general framework for defining evaluation metrics
- [Feedback Object](/concepts/feedback-object.md) — The data structure used to return evaluation results
- MLflow Evaluation for GenAI — The overall evaluation system
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous monitoring
- [@scorer decorator](/concepts/scorer-decorator.md) — The `@scorer` decorator for defining custom scorers

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
