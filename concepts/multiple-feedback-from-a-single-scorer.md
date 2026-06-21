---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 126b649bfa4ab528ee8a20e7836a25c85b93e0ae549b9800c3f13f2f50b27f7c
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple-feedback-from-a-single-scorer
    - MFFASS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Multiple feedback from a single scorer
description: A pattern where a single custom scorer returns a list of Feedback objects, each with a unique name, to assess multiple quality facets simultaneously in one evaluation pass
tags:
  - mlflow
  - evaluation
  - feedback
timestamp: "2026-06-18T10:57:30.636Z"
---

# Multiple feedback from a single scorer

**Multiple feedback from a single scorer** is a pattern in MLflow Evaluation for GenAI where a single custom code-based scorer returns multiple [`Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html?highlight=feedback#mlflow.entities.Feedback) objects, allowing one scorer to assess multiple quality facets (such as PII, sentiment, and conciseness) simultaneously. ^[code-based-scorer-examples-databricks-on-aws.md]

## How it works

A custom scorer decorated with `@scorer` can return a list of `Feedback` objects instead of a single value or `Feedback` object. Each `Feedback` object must have a unique `name`, which becomes the metric name in the evaluation results. ^[code-based-scorer-examples-databricks-on-aws.md]

## Example

The following example demonstrates a scorer that returns two distinct pieces of feedback for each trace:

1. `is_not_empty_check`: A boolean indicating if the response content is non-empty.
2. `response_char_length`: A numeric value for the character length of the response.

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

# Evaluate the scorer using pre-generated traces
multi_feedback_eval_results = mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[comprehensive_response_checker]
)
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Results

When using multiple feedback from a single scorer, the evaluation results will contain separate columns for each named `Feedback` object. In the example above, the result will have two columns: `is_not_empty_check` and `response_char_length` as assessments. ^[code-based-scorer-examples-databricks-on-aws.md]

## Naming conventions

When returning multiple `Feedback` objects from a single scorer, you must specify a unique name for each `Feedback`. The names specified in each `Feedback` object are preserved as the metric names in the evaluation results. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) — The framework for defining custom evaluation metrics
- MLflow Evaluation for GenAI — The evaluation system for generative AI applications
- [Feedback objects](/concepts/feedback-objects.md) — The data structure for returning evaluation results from scorers
- [@scorer decorator](/concepts/scorer-decorator.md) — The decorator used to define custom scorers

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
