---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd2e7bd5fc9e3433756901f7b0a9dfcaa60efdc9ec8ffd38e22d7c4f653682b4
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-value-types-in-judges
    - FVTIJ
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Feedback Value Types in Judges
description: The return types for custom judges, supporting Literal string types (e.g., 'fully_resolved') and bool types for different grading scales.
tags:
  - MLflow
  - GenAI
  - evaluation
  - judges
timestamp: "2026-06-19T17:54:39.095Z"
---

# Feedback Value Types in Judges

**Feedback Value Types** specify the allowed output type that an LLM-based judge returns when evaluating a GenAI agent. When creating a custom judge with `make_judge()`, the `feedback_value_type` parameter defines the set of possible values the judge can assign to each evaluation. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Overview

Judges are [Custom Judge|custom LLM-based scorers](/concepts/custom-judges-llm-based-scorers.md) that assess agent responses against specific quality criteria. The `feedback_value_type` controls the shape of the feedback the judge produces. Supported types include `bool` (a simple true/false) or a `Literal` type with a fixed set of string values (e.g., `Literal["fully_resolved", "partially_resolved", "needs_follow_up"]`). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The `feedback_value_type` is passed directly to the `make_judge()` function alongside `name`, `instructions`, and optionally a `model`. The judge returns an `mlflow.entities.Feedback` object whose value conforms to the declared type. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Supported Types

- **`bool`**: Returns `True` or `False`. Used for simple pass/fail criteria, such as whether the agent called appropriate tools. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **`Literal[...]`**: Returns one of a predefined set of string values. Common for graded assessments (e.g., `"fully_resolved"`, `"partially_resolved"`, `"needs_follow_up"`). The literal values are defined inline using Python's `typing.Literal`. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## How It Is Used

The `feedback_value_type` is specified when defining a judge with `make_judge()`. For example:

```python
from mlflow.genai.judges import make_judge
from typing import Literal

issue_resolution_judge = make_judge(
    name="issue_resolution",
    instructions="Evaluate if the customer's issue was resolved...",
    feedback_value_type=Literal["fully_resolved", "partially_resolved", "needs_follow_up"],
)
```

The judge evaluates each agent response and returns a value from the specified type. The instructions can reference `{{ inputs }}`, `{{ outputs }}`, `{{ trace }}`, or `{{ expectations }}` to provide context for the evaluation. When `{{ trace }}` is included, the judge becomes trace‑based and gains autonomous trace exploration capabilities. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- make_judge() – The function that creates a custom judge with a defined feedback type.
- [Custom Judge](/concepts/custom-judges.md) – Overview of LLM‑based scorers for evaluating GenAI agents.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – How judges are used with `mlflow.genai.evaluate()`.
- [Trace-Based Judge](/concepts/trace-based-judges.md) – A judge that analyzes execution traces by including `{{ trace }}` in instructions.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
