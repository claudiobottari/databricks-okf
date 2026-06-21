---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 656253adffa619ef6449e926d92ebe0ac19379c6a64804703caa15376ded2663
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-value-types
    - FVT
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Feedback Value Types
description: A typing mechanism using Python's Literal and bool to define the output format and possible values returned by custom judges, such as categorical labels or boolean assessments.
tags:
  - mlflow
  - typing
  - evaluation
  - judges
timestamp: "2026-06-19T09:26:48.073Z"
---

# Feedback Value Types

**Feedback Value Types** define the grading scale that a custom judge uses to evaluate GenAI agent outputs. They specify the set of possible scores or categories a judge can return, shaping the quality criteria used in evaluation.

## Overview

When creating a custom judge with `make_judge()`, you supply a `feedback_value_type` argument that determines the type of feedback the judge will produce. This type can be a primitive Python type like `bool`, or a `Literal` type that enumerates specific string values. The chosen type directly defines the evaluation rubric—for example, a binary true/false judgment or a multi‑level classification such as `"fully_resolved"`, `"partially_resolved"`, or `"needs_follow_up"`. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Judges created with `make_judge()` return [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) objects whose values conform to the declared type.

## Usage in Custom Judges

The `feedback_value_type` parameter is required when calling `make_judge()`. It restricts the LLM‑based scorer to only output values of that type, ensuring consistent and predictable evaluation results. The type also governs how the judge’s outputs are aggregated and compared across evaluation runs. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Examples

| Feedback Value Type | Example Use Case | Possible Values |
|---------------------|------------------|-----------------|
| `bool` | Validate whether the agent called the correct tool | `True` / `False` |
| `Literal["fully_resolved", "partially_resolved", "needs_follow_up"]` | Assess issue resolution in customer support | Three discrete categories |
| `Literal["meets_expectations", "partially_meets", "does_not_meet"]` | Check expected behaviors against predefined criteria | Three discrete categories |

#### Binary (bool) Judge
```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions="Analyze the execution {{ trace }} ...",
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

#### Categorical (Literal) Judge
```python
issue_resolution_judge = make_judge(
    name="issue_resolution",
    instructions=(
        "Evaluate if the customer's issue was resolved ... "
        "User's messages: {{ inputs }}\n"
        "Agent's responses: {{ outputs }}"
    ),
    feedback_value_type=Literal[
        "fully_resolved",
        "partially_resolved",
        "needs_follow_up"
    ],
)
```

## Using Feedback Values in A/B Comparisons

In [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md), the same set of judges with identical `feedback_value_type` definitions is applied to all agent variants. The structured feedback values (e.g., `true`/`false` or `fully_resolved`) enable direct comparison of score distributions across configurations, revealing which variant better satisfies the defined quality criteria. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) – LLM‑based scorers that use feedback value types.
- make_judge()|Make Judge API – The `make_judge()` function where `feedback_value_type` is specified.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The evaluation framework that consumes judge feedback.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Using consistent feedback value types to compare agent variants.
- Align judges with human feedback – Improving judge accuracy by refining evaluation criteria.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
