---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17d57cb1b5705dcf495352160707636a579a53b0f7333215dbe44c588d0a57ed
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema-input-types
    - LSIT
    - Labeling schemas input types
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling Schema Input Types
description: "The five supported input types for labeling schemas: InputCategorical, InputCategoricalList, InputText, InputTextList, and InputNumeric, each with configurable validation rules and constraints."
tags:
  - genai
  - input-types
  - schema-design
timestamp: "2026-06-18T11:19:14.259Z"
---

# Labeling Schema Input Types

**Labeling Schema Input Types** define the specific format and constraints for collecting feedback from domain experts during [Labeling Sessions](/concepts/labeling-sessions.md) in the [Review App](/concepts/mlflow-review-app.md). These input types determine how reviewers provide structured assessments—whether through categorical choices, free-form text, numeric ratings, or combinations thereof. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

When creating a [Labeling Schema](/concepts/labeling-schema.md) for an [MLflow Experiment](/concepts/mlflow-experiment.md), the **Input type** field dictates the kind of data a reviewer will submit as part of an assessment. Each schema represents either a `Feedback` (subjective rating, opinion) or an `Expectation` (objective ground truth, correct answer). The input type controls:

- **The question** shown to the reviewer (via `title` and optional `instruction`).
- **The interactive widget** rendered in the Review App (drop-down, text box, slider, etc.).
- **Validation rules**—length limits, option exclusivity, numeric ranges.
- **Optional comments** (`enable_comment`) that let reviewers add explanatory notes.

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

MLflow provides five built-in input types: `InputCategorical`, `InputCategoricalList`, `InputText`, `InputTextList`, and `InputNumeric`. Each maps to a particular kind of human judgment.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Input Types Reference

### `InputCategorical`

A single-select categorical choice. The reviewer picks exactly one option from a list. This is the most common type for **ratings, binary flags, or compact quality scales**.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputCategorical

# Rating scale
rating_input = InputCategorical(
    options=["1 - Poor", "2 - Below Average",
             "3 - Average", "4 - Good", "5 - Excellent"]
)

# Binary choice
safety_input = InputCategorical(
    options=["Safe", "Unsafe"]
)

# Multi-category error detection
error_type_input = InputCategorical(
    options=[
        "Factual Error",
        "Logical Error",
        "Formatting Error",
        "No Error"
    ]
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputCategoricalList`

A multi-select categorical choice. The reviewer selects **multiple options** from a predefined list. Options are rendered as checkboxes; the reviewer marks all that apply. This is useful when an assessment can contain **several concurrent issues** or **multiple content categories**.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputCategoricalList

# Multiple error types
errors_input = InputCategoricalList(
    options=[
        "Factual inaccuracy",
        "Missing context",
        "Inappropriate tone",
        "Formatting issues",
        "Off-topic content"
    ]
)

# Multiple content categories
content_types = InputCategoricalList(
    options=[
        "Technical details",
        "Examples",
        "References",
        "Code samples"
    ]
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputText`

A single free-form text entry. The reviewer types a short phrase or sentence. This is suitable for **concise feedback, single-line corrections, or short explanatory notes**.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputText

# General feedback with a length limit
feedback_input = InputText(max_length=500)

# Specific correction suggestion
improvement_input = InputText(
    max_length=200  # Limit length for focused feedback
)

# Very short answer
summary_input = InputText(max_length=100)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputTextList`

A list of free-form text entries. The reviewer provides **multiple distinct text items**, each subject to a maximum character limit and a cap on the total number. This is ideal for **enumerating required facts, expected behaviors, or improvement suggestions**.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputTextList

# List of factual errors (max 10 items)
errors_input = InputTextList(
    max_count=10,
    max_length_each=150  # Each error description limited to 150 chars
)

# Missing information (max 5 items)
missing_input = InputTextList(
    max_count=5,
    max_length_each=200
)

# Improvement suggestions without per-item limit
suggestions_input = InputTextList(max_count=3)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputNumeric`

A numerical (integer or float) input with optional min/max bounds. The reviewer enters a number within the defined range. This is appropriate for **confidence scores, quality scales, or cost estimates** where a numeric value maps to a continuous judgment.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputNumeric

# Confidence score (0.0–1.0)
confidence_input = InputNumeric(
    min_value=0.0,
    max_value=1.0
)

# Rating scale (1–10)
rating_input = InputNumeric(
    min_value=1,
    max_value=10
)

# Cost estimate (no upper bound)
cost_input = InputNumeric(min_value=0)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Choosing an Input Type by Assessment Kind

| Assessment Type | Recommended Input | Example Use Case |
|----------------|-------------------|------------------|
| **Quality rating** (single choice from a scale) | `InputCategorical` | "Rate response quality: Good / Fair / Poor" |
| **Issue identification** (multiple concurrent problems) | `InputCategoricalList` | "Select all issues present in this response" |
| **Short factual correction** (one piece of text) | `InputText` | "Enter the corrected fact" |
| **List of required facts** (multiple text items) | `InputTextList` | "List the key facts a correct answer must contain" |
| **Confidence / cost score** (continuous number) | `InputNumeric` | "Rate confidence from 1 (low) to 10 (high)" |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Interaction with the Review App

When a [Labeling Session](/concepts/labeling-session.md) uses a schema, the Review App renders the input type as a **form field** matching the input type class. The reviewer sees:

- For `InputCategorical` → a **dropdown** (single-select).
- For `InputCategoricalList` → **checkboxes** (multi-select).
- For `InputText` → a **single-line text box** subject to `max_length`.
- For `InputTextList` → an **addable list** of text boxes (up to `max_count` items).
- For `InputNumeric` → a **number input** with slider or spin buttons.

Validation rules (max length, required fields, range constraints) are enforced client-side before the assessment is saved.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Compatibility with Built-in LLM Judges

MLflow provides **predefined schema names** (e.g., `EXPECTED_FACTS`, `GUIDELINES`, `EXPECTED_RESPONSE`) that use `InputTextList` or `InputText` as their input type. When you create a custom schema with one of these predefined names, you must match the expected input type so that the [Built-in LLM Judges](/concepts/built-in-llm-judges.md) can process the collected labels.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

- **Write questions as clear, specific prompts.** Each `title` and `instruction` should guide the reviewer precisely.
- **Set reasonable limits.** Use `max_length` on text inputs and `max_count` on lists to keep responses focused. Avoid unbounded text inputs where possible.
- **Ensure options are mutually exclusive** in `InputCategorical`. Include an "Other" or "None" option when the list may not cover all cases.
- **Use `InputCategoricalList` for multi-issue assessments**, not `InputCategorical`, when more than one issue can be present.
- **Validate numeric ranges** with `min_value` and `max_value` on `InputNumeric` to prevent out-of-range submissions.
- **Document schema changes** for team awareness. When updating a schema with `overwrite=True`, existing labeling sessions may no longer match the updated input type.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schema](/concepts/labeling-schema.md) – The complete definition including input type, name, and title
- [Labeling Session](/concepts/labeling-session.md) – A review workflow that associates schemas with traces
- [Review App](/concepts/mlflow-review-app.md) – The UI where reviewers fill in schema-based forms
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Predefined scorers that consume labeled expectations
- Input Types API Reference – `mlflow.genai.label_schemas` module for all input classes
- [Create and manage labeling schemas](/concepts/labeling-schemas.md) – Full guide on schema CRUD operations

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
