---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d05cef8de8c66682013f617710bc7c5d8f78b1ca9455a8e7639a32edd30fe972
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - feedback-object-in-mlflow-evaluation
    - FOIME
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Feedback Object in MLflow Evaluation
description: A structured result type carrying a value, rationale, optional name, error info, and assessment source metadata for scorer outputs.
tags:
  - mlflow
  - evaluation
  - feedback
timestamp: "2026-06-19T09:13:26.078Z"
---

# Feedback Object in MLflow Evaluation

The **Feedback Object** in MLflow Evaluation is a structured data container used by custom scorers to return evaluation results for GenAI agent outputs. It encapsulates the assessment value, a rationale explaining the judgment, and optional metadata such as error information and assessment source. ^[code-based-scorer-examples-databricks-on-aws.md]

## Overview

When building custom scorers for [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md), the `Feedback` object provides a standardized way to communicate evaluation results back to the MLflow tracking system. It is defined in the `mlflow.entities` module and is the recommended return type for scorers that need to provide rich, structured feedback beyond a simple primitive value. ^[code-based-scorer-examples-databricks-on-aws.md]

## Key Attributes

The `Feedback` object supports the following attributes:

- **`value`**: The assessment result, which can be a boolean, integer, float, string, or `None`. This is the primary metric value that appears in evaluation results. ^[code-based-scorer-examples-databricks-on-aws.md]
- **`rationale`**: A string explaining the reasoning behind the assessment. This provides interpretability for the evaluation result. ^[code-based-scorer-examples-databricks-on-aws.md]
- **`name`**: An optional string that becomes the metric name in evaluation results. When a scorer returns multiple `Feedback` objects, each must have a unique `name`. ^[code-based-scorer-examples-databricks-on-aws.md]
- **`error`**: An optional `AssessmentError` object for reporting errors gracefully without failing the entire evaluation. ^[code-based-scorer-examples-databricks-on-aws.md]
- **`source`**: An optional `AssessmentSource` object that indicates the origin of the assessment, such as an LLM judge. ^[code-based-scorer-examples-databricks-on-aws.md]

## Usage Patterns

### Returning a Single Feedback Object

The most common pattern is to return a single `Feedback` object from a scorer function:

```python
from mlflow.entities import Feedback
from mlflow.genai.scorers import scorer

@scorer
def response_quality_checker(outputs: str) -> Feedback:
    if len(outputs) > 0:
        return Feedback(
            value="yes",
            rationale="Response is non-empty and valid."
        )
    else:
        return Feedback(
            value="no",
            rationale="Response is empty."
        )
```

^[code-based-scorer-examples-databricks-on-aws.md]

### Returning Multiple Feedback Objects

A single scorer can return a list of `Feedback` objects to assess multiple quality facets simultaneously. Each `Feedback` must have a unique `name`:

```python
@scorer
def comprehensive_response_checker(outputs: str) -> list[Feedback]:
    feedbacks = []
    feedbacks.append(
        Feedback(name="is_not_empty_check", value="yes" if outputs != "" else "no")
    )
    char_length = len(outputs)
    feedbacks.append(Feedback(name="response_char_length", value=char_length))
    return feedbacks
```

^[code-based-scorer-examples-databricks-on-aws.md]

### Including Assessment Source

When using an LLM as a judge, you can set the `source` field to indicate the origin of the assessment:

```python
from mlflow.entities import AssessmentSource, AssessmentSourceType

return Feedback(
    value=parsed_score,
    rationale=parsed_rationale,
    source=AssessmentSource(
        source_type=AssessmentSourceType.LLM_JUDGE,
        source_id="claude-sonnet-4-5",
    )
)
```

^[code-based-scorer-examples-databricks-on-aws.md]

### Error Handling with Feedback

The `Feedback` object supports graceful error reporting through the `error` attribute:

```python
from mlflow.entities import AssessmentError

return Feedback(
    value=None,
    error=AssessmentError(
        error_code="MISSING_RESPONSE",
        error_message="No response field in outputs"
    )
)
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Metric Naming

The `name` attribute determines how the metric appears in evaluation results:

- If a scorer returns a primitive value or a single `Feedback` without a `name`, the scorer function name becomes the metric name.
- If a scorer returns a single `Feedback` with an explicit `name`, that name is used as the metric name.
- If a scorer returns multiple `Feedback` objects, each must have a unique `name`, and those names become the metric names. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) — Functions that return Feedback objects for evaluation
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework that consumes Feedback objects
- [AssessmentSource](/concepts/assessmentsource-entity.md) — Metadata for tracking the origin of assessments
- AssessmentError — Structured error reporting within Feedback objects
- [Code-Based Scorer Examples](/concepts/code-based-scorers.md) — Practical examples of Feedback object usage

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
