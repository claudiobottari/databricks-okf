---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37c4e1239afd66431d97271d25e31ba1fbf708d0d44d1d126939c65818f6fddf
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - input-types-for-custom-labeling-schemas
    - ITFCLS
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Input Types for Custom Labeling Schemas
description: "Six supported input types for collecting feedback in custom schemas: InputCategorical, InputCategoricalList, InputText, InputTextList, and InputNumeric — each with configurable constraints."
tags:
  - mlflow
  - schema-design
  - input-types
timestamp: "2026-06-19T14:33:13.419Z"
---

# Input Types for Custom Labeling Schemas

**Input types for custom labeling schemas** define the specific format and constraints for collecting feedback from domain experts when labeling traces in the Review App. MLflow provides five input types that control how reviewers provide their assessments, including validation rules, length limits, and selection options. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

When creating a custom labeling schema, the input type determines the user interface element presented to reviewers and the structure of the collected data. Each input type supports different validation parameters, such as allowed options for categorical inputs, character limits for text inputs, or numeric ranges for numerical inputs. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Input types are specified when creating a schema using the MLflow UI or the `create_label_schema()` API. The available types are: `InputCategorical`, `InputCategoricalList`, `InputText`, `InputTextList`, and `InputNumeric`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Input Type Reference

### `InputCategorical`

`InputCategorical` presents a single-select dropdown menu to reviewers. It is used for collecting a single choice from a predefined set of options. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputCategorical

# Rating scale
rating_input = InputCategorical(
    options=["1 - Poor", "2 - Below Average", "3 - Average", "4 - Good", "5 - Excellent"]
)

# Binary choice
safety_input = InputCategorical(options=["Safe", "Unsafe"])

# Multiple categories
error_type_input = InputCategorical(
    options=["Factual Error", "Logical Error", "Formatting Error", "No Error"]
)
```

### `InputCategoricalList`

`InputCategoricalList` presents a multi-select interface, allowing reviewers to select multiple options from a predefined list. This is useful when multiple issues or attributes can apply simultaneously. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputCategoricalList

# Multiple error types can be present
errors_input = InputCategoricalList(
    options=[
        "Factual inaccuracy",
        "Missing context",
        "Inappropriate tone",
        "Formatting issues",
        "Off-topic content"
    ]
)

# Multiple content types
content_input = InputCategoricalList(
    options=["Technical details", "Examples", "References", "Code samples"]
)
```

### `InputText`

`InputText` provides a free-text input field for collecting open-ended feedback. It supports an optional `max_length` parameter to limit the number of characters. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputText

# General feedback
feedback_input = InputText(max_length=500)

# Specific improvement suggestions
improvement_input = InputText(
    max_length=200  # Limit length for focused feedback
)

# Short answers
summary_input = InputText(max_length=100)
```

### `InputTextList`

`InputTextList` allows reviewers to provide multiple text entries, such as a list of facts or issues. It supports `max_count` to limit the number of items and `max_length_each` to limit the length of each individual entry. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputTextList

# List of factual errors
errors_input = InputTextList(
    max_count=10,        # Maximum 10 errors
    max_length_each=150  # Each error description limited to 150 chars
)

# Missing information
missing_input = InputTextList(
    max_count=5,
    max_length_each=200
)

# Improvement suggestions
suggestions_input = InputTextList(max_count=3)  # No length limit per item
```

### `InputNumeric`

`InputNumeric` provides a numeric input field with optional `min_value` and `max_value` constraints. It is suitable for ratings, confidence scores, or any numerical assessment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputNumeric

# Confidence score
confidence_input = InputNumeric(
    min_value=0.0,
    max_value=1.0
)

# Rating scale
rating_input = InputNumeric(
    min_value=1,
    max_value=10
)

# Cost estimate
cost_input = InputNumeric(min_value=0)  # No maximum limit
```

## Usage in Schema Creation

Input types are passed as the `input` parameter when creating a labeling schema. The schema also requires a `name`, `type` (either `"feedback"` or `"expectation"`), and `title`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical, InputText

# Create a feedback schema for rating response quality
quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness when rating."
)
```

## UI Behavior

When creating schemas in the MLflow UI, selecting an input type dynamically changes the available fields below it to let you specify detailed requirements, such as length limits for text, options for categorical choices, or a numeric range. A preview box updates in real-time to reflect the schema being created. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

- For categorical inputs, ensure options are mutually exclusive and comprehensive. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Set reasonable limits on text length and list counts to guide reviewers toward focused feedback. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Use `InputCategoricalList` when multiple attributes can apply simultaneously, and `InputCategorical` when only one selection is valid. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- For numeric inputs, always specify `min_value` and `max_value` when the range is known to prevent out-of-range entries. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — The overall structure that uses input types
- [Create and Manage Labeling Schemas](/concepts/labeling-schemas.md) — Full guide for schema creation and management
- [Labeling Sessions](/concepts/labeling-sessions.md) — How schemas are applied during review workflows
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — The broader process of collecting expert annotations
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined schemas compatible with MLflow's evaluation framework

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
