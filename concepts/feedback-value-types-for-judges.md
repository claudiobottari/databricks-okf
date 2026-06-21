---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3fa1d314aa6084416e6a2757e53ad83c00e33d0bc173efbb35d5fce7b0f8bf8b
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-value-types-for-judges
    - FVTFJ
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Feedback Value Types for Judges
description: Custom judges can return various feedback value types including boolean (`bool`), string literals (e.g., `fully_resolved`, `partially_resolved`, `needs_follow_up`), and other types defined via Python's `Literal` type annotation.
tags:
  - mlflow
  - genai
  - type-system
timestamp: "2026-06-18T11:12:41.503Z"
---

# Feedback Value Types for Judges

**Feedback value types** define the set of possible values a custom [judge (MLflow)](/concepts/built-in-judges-mlflow.md) can assign when evaluating a GenAI agent’s output. In the `make_judge()` API, the `feedback_value_type` parameter specifies the valid return values that the judge’s `Feedback` object will carry. This parameter is a core part of declaring a judge’s evaluation scale. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Supported Value Types

The `feedback_value_type` can be given as a `Literal` type (a union of allowed string literals) or as `bool`. The type must be a valid Python type annotation. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The source material shows the following concrete examples:

| Judge purpose | `feedback_value_type` declaration |
|---------------|-----------------------------------|
| Issue resolution | `Literal["fully_resolved", "partially_resolved", "needs_follow_up"]` |
| Expected behaviors | `Literal["meets_expectations", "partially_meets", "does_not_meet"]` |
| Tool call correctness | `bool` (true/false) |

These examples illustrate that a judge’s output can be a ternary categorical value, a binary boolean, or any other `Literal`‑based set of strings. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Relation to the Feedback Object

Judges created with `make_judge()` return [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) objects. The `multiple_choice` / `value` attribute of that object conforms to the type declared in `feedback_value_type`. For example, if the judge’s type is `Literal["fully_resolved", "partially_resolved", "needs_follow_up"]`, the returned `Feedback` object will carry a `value` that is exactly one of those three strings. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Usage in Evaluation

When you supply a judge (via `make_judge()`) to `mlflow.genai.evaluate()`, MLflow reads the `feedback_value_type` annotation to validate and structure the judge’s outputs. The value type appears in the evaluation results and can be used for downstream analysis or aggregation. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The type also influences how the judge’s LLM prompt is constructed: the judge is instructed to produce one of the allowed values, and the output is parsed accordingly. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Best Practices

- Choose value types that are meaningful and mutually exclusive. Categorical labels (like `"fully_resolved"`, `"partially_resolved"`, `"needs_follow_up"`) give more nuance than a simple boolean.
- For binary assessments, prefer `bool` over a two‑value `Literal` to keep the annotation concise.
- Align the value type with the judge’s instructions: the names in the instruction should match the allowed values exactly. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- make_judge() – Function used to declare custom judges, including the `feedback_value_type` parameter.
- Feedback (MLflow) – The structured object returned by a judge, whose value follows the declared type.
- [Custom Judges](/concepts/custom-judges.md) – General concept of LLM‑based scorers for evaluating GenAI agents.
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) – The evaluation API that accepts judges and returns results containing the feedback values.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
