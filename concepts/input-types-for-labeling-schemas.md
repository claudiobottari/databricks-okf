---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e685a680e40f3238957876346df77326b91e211bcb9f44b0f672856baf868007
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - input-types-for-labeling-schemas
    - ITFLS
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Input types for labeling schemas
description: "Supported input types for custom labeling schemas: InputCategorical, InputCategoricalList, InputText, InputTextList, and InputNumeric, each with specific constraints."
tags:
  - mlflow
  - input-types
  - labeling
  - api
timestamp: "2026-06-19T17:58:39.717Z"
---

# Input Types for Labeling Schemas

**Input types for labeling schemas** define the method by which domain experts provide feedback when labeling traces in the Review App. Each input type determines the user interface element presented to reviewers — such as a drop-down menu, text box, or numeric slider — along with its validation rules and constraints. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

When creating a custom labeling schema, you must specify an input type that controls how reviewers enter their assessments. MLflow provides five input types, each suited to different kinds of feedback collection. The input type is set via the `input` parameter of `create_label_schema()`, and the available fields change depending on which type you select. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Input types apply only when using the Review App to label existing traces. They are not used for vibe checks in the Review App Chat UI. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Available Input Types

### `InputCategorical`

`InputCategorical` presents a single-select drop-down menu with predefined options. Use this type when reviewers must choose exactly one value from a set of mutually exclusive choices. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Common use cases include:
- Rating scales (e.g., "Poor", "Fair", "Good", "Excellent")
- Binary choices (e.g., "Safe", "Unsafe")
- Single-category classification (e.g., "Factual Error", "Logical Error", "Formatting Error", "No Error")

The `options` parameter accepts a list of strings representing the available choices. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputCategoricalList`

`InputCategoricalList` presents a multi-select list where reviewers can choose multiple options from a predefined set. Use this type when multiple categories can apply simultaneously. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Common use cases include:
- Identifying multiple error types present in a response
- Selecting all applicable content categories
- Flagging multiple issues in a single assessment

The `options` parameter accepts a list of strings. Unlike `InputCategorical`, reviewers can select zero, one, or many options. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputText`

`InputText` provides a free-text input field for open-ended feedback. Use this type when reviewers need to provide unstructured written responses. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The `max_length` parameter sets a character limit on the response. Common use cases include:
- General feedback or comments
- Specific improvement suggestions
- Short summary answers

### `InputTextList`

`InputTextList` provides a list of free-text fields, allowing reviewers to enter multiple distinct text items. Use this type when reviewers need to provide a structured list of items, such as facts, steps, or errors. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Parameters include:
- `max_count`: Maximum number of items in the list
- `max_length_each`: Maximum character length per item

Common use cases include:
- Listing factual errors in a response
- Specifying missing information
- Providing improvement suggestions

### `InputNumeric`

`InputNumeric` provides a numeric input field with optional minimum and maximum constraints. Use this type when reviewers need to provide a numerical score or value. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Parameters include:
- `min_value`: Minimum allowed value (optional)
- `max_value`: Maximum allowed value (optional)

Common use cases include:
- Confidence scores (e.g., 0.0 to 1.0)
- Rating scales (e.g., 1 to 10)
- Cost estimates or accuracy percentages

## Selecting an Input Type

When creating a labeling schema in the MLflow UI, selecting an **Input type** dynamically changes the fields below it to let you specify detailed requirements, such as length limits for text, options for categorical choices, or a numeric range. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

- For categorical inputs, ensure options are mutually exclusive (for `InputCategorical`) and comprehensive (for both categorical types). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Set reasonable limits on text length and list counts to focus reviewer feedback. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Choose the input type that best matches the nature of the assessment: subjective ratings work well with categorical or numeric inputs, while objective ground truth often requires text or text list inputs. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — The overall structure that defines questions, input types, and validation rules for the Review App.
- [Labeling Sessions](/concepts/labeling-sessions.md) — Workflows that associate schemas with traces for structured feedback collection.
- [Review App](/concepts/mlflow-review-app.md) — The interface where domain experts label traces using schemas.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined schemas that use specific input types for automated evaluation.
- Feedback vs Expectation — The two schema types that determine whether an assessment is subjective or objective.

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
