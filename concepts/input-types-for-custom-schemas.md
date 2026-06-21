---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d4b78e9e77b3a21a89273fc17c8abbf37f8285cbf795169912ccf04b6a72e200
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - input-types-for-custom-schemas
    - ITFCS
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Input types for custom schemas
description: "The supported input types for collecting feedback in custom labeling schemas: InputCategorical, InputCategoricalList, InputText, InputTextList, and InputNumeric."
tags:
  - mlflow
  - input-types
  - labeling
timestamp: "2026-06-19T09:32:47.120Z"
---

# Input Types for Custom Schemas

**Input types for custom schemas** define the specific data formats that domain experts use when providing feedback through [Labeling Schemas](/concepts/labeling-schemas.md) in the [Review App](/concepts/mlflow-review-app.md). These input types structure how feedback is collected, ensuring consistent and relevant information for [GenAI](/concepts/mlflow-genai-evaluate-api.md) application evaluation.

## Overview

MLflow supports multiple input types for custom labeling schemas to collect different kinds of feedback. Each input type has specific parameters that control the format and constraints of the collected data. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Supported Input Types

### InputCategorical

`InputCategorical` provides a single-selection choice from a predefined list of options. This is ideal for ratings, binary decisions, or classification tasks. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

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

### InputCategoricalList

`InputCategoricalList` allows multiple selections from a list of options, enabling reviewers to identify all applicable categories in a response. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

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

### InputText

`InputText` provides a free-text field for open-ended feedback, with optional length limits to constrain responses. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

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

### InputTextList

`InputTextList` enables reviewers to provide multiple text entries as a list, with constraints on both the number of items and individual item lengths. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

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

### InputNumeric

`InputNumeric` provides a numeric input with optional minimum and maximum value constraints, suitable for confidence scores, ratings, or cost estimates. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

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

## Usage in Labeling Schemas

Input types are used when creating [Labeling Schemas](/concepts/labeling-schemas.md) with the `create_label_schema()` API. Each schema requires an input specification that matches the type of feedback being collected. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md), and schema names must be unique within each experiment. The input type selection determines whether the schema collects `feedback` (subjective assessments like ratings or preferences) or `expectation` (objective ground truth like correct answers or expected behavior). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) - Define assessment questions for domain experts
- [Labeling Sessions](/concepts/labeling-sessions.md) - Organize review workflows using schemas
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) - Predefined schema names for evaluation
- [Review App](/concepts/mlflow-review-app.md) - Interface for collecting structured feedback
- InputCategorical - Single-selection choice input
- InputCategoricalList - Multiple-selection list input
- InputText - Free-text input
- InputTextList - Multiple text entries
- InputNumeric - Numeric value input

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
