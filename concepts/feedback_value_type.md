---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b78524c7c70032544091332714f99f9b7b8641d5da8568ba148f9440f8cde4c
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: feedback_value_type
description: Parameter in make_judge() that defines the return type of a custom judge, supporting Literal string unions or bool
tags:
  - mlflow
  - api
  - judges
timestamp: "2026-06-19T14:28:52.531Z"
---

# feedback\_value\_type

**`feedback_value_type`** is a parameter of the [`make_judge()`](/make-judge-api) function in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that defines the data type of the feedback value returned by a custom judge. It determines the structure and expected values that the judge will output when evaluating an agent's behavior. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## How It Works

When creating a custom judge with `make_judge()`, you supply a `feedback_value_type` that can be either a `typing.Literal` type containing a set of allowed string values, or the Python `bool` type. The judge then returns an `mlflow.entities.Feedback` object whose `value` property is constrained to the type you specified. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Examples

### Literal String Type

Use `Literal` to define a set of ordered or unordered categories for the judge's rating:

```python
from mlflow.genai.judges import make_judge
from typing import Literal

issue_resolution_judge = make_judge(
    name="issue_resolution",
    instructions="Evaluate if the customer's issue was resolved...",
    feedback_value_type=Literal["fully_resolved", "partially_resolved", "needs_follow_up"],
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Boolean Type

Use `bool` for a binary pass/fail evaluation, such as verifying whether appropriate tools were called:

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions="Analyze the execution trace...",
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Role in Agent Evaluation

Each judge's `feedback_value_type` determines the range of values that can be compared across different agent configurations during an [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md). For example, `issue_resolution` returns one of three string literals, while `tool_call_correctness` returns a boolean. These structured values make it easy to aggregate and compare scores across evaluation runs. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that use `feedback_value_type` to define their output format.
- make_judge()|Make Judge API — The function that accepts `feedback_value_type` as a required parameter.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The evaluation framework in which judges are used.
- [Feedback Object](/concepts/feedback-object.md) — The object returned by `make_judge` judges, whose value conforms to the declared type.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Evaluation workflows that rely on consistent `feedback_value_type` definitions for comparison.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
