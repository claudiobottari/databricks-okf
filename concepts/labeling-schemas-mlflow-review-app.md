---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad93700c90fc83a77c91b597d5c18f82a688a412c41583fc3ed27d259d92ec72
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schemas-mlflow-review-app
    - LS(RA
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling schemas (MLflow Review App)
description: Structured question definitions that domain experts answer when labeling existing traces in the MLflow Review App for GenAI evaluation.
tags:
  - mlflow
  - human-feedback
  - genai
  - evaluation
timestamp: "2026-06-18T14:51:29.438Z"
---

# Labeling Schemas (MLflow Review App)

**Labeling schemas** define the specific questions that domain experts answer when labeling existing traces in the MLflow Review App. They structure the feedback collection process, ensuring consistent and relevant information for evaluating GenAI applications. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

Labeling schemas apply only when using the Review App to label existing traces, and are not used for vibe checks in the Review App Chat UI. When a labeling session is created, it is associated with one or more labeling schemas. Each schema represents an assessment that is attached to a trace, and assessments are either `Feedback` or `Expectation`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### What Schemas Control

Schemas control the question shown to reviewers, the input method (e.g., drop-down menu or text box), validation rules and constraints, and optional instructions and comments. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Schema Types

Schemas are one of two types:

- **Feedback**: Subjective assessments like ratings, preferences, or opinions.
- **Expectation**: Objective ground truth like correct answers or expected behavior. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Labeling Schemas for Built-in LLM Judges

MLflow provides predefined schema names for [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that use expectations. Custom schemas can be created using these names to ensure compatibility with the built-in evaluation functionality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The predefined labeling schemas include:

| Schema Name | Type | Purpose |
|-------------|------|---------|
| `EXPECTED_FACTS` | Expectation | Collect expected facts for a correct response |
| `GUIDELINES` | Expectation | Collect guidelines the output should adhere to |
| `EXPECTED_RESPONSE` | Expectation | Collect a correct agent response |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Example: Predefined Schema Usage

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import LabelSchemaType, InputTextList, InputText

# Schema for collecting expected facts
expected_facts_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_FACTS,
    type=LabelSchemaType.EXPECTATION,
    title="Expected facts",
    input=InputTextList(max_length_each=1000),
    instruction="Please provide a list of facts that you expect to see in a correct response.",
    overwrite=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Creating Custom Labeling Schemas

Custom schemas can be created using either the MLflow UI or the API. Schemas are scoped to experiments, so schema names must be unique within an MLflow experiment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Creating Schemas via the UI

1. In the Databricks workspace, click **Experiments** in the left sidebar.
2. Click the name of your experiment to open it.
3. Click **Labeling schemas** in the sidebar.
4. Click **Add Label Schema** and edit the fields.
5. When you select the **Input type**, the fields change to let you specify detailed requirements such as length limits for text, options for categorical choices, or a numeric range.
6. Click **Save** when done. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Creating Schemas via the API

Schemas are created using `mlflow.genai.label_schemas.create_label_schema()`. All schemas require a name, type, title, and input specification. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

#### Basic Schema Example

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

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

#### Custom Schema Feedback Example

```python
from mlflow.genai.label_schemas import InputCategorical

# Feedback schema for subjective assessment
tone_schema = schemas.create_label_schema(
    name="response_tone",
    type="feedback",
    title="Is the response tone appropriate for the context?",
    input=InputCategorical(options=["Too formal", "Just right", "Too casual"]),
    enable_comment=True  # Allow additional comments
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

#### Custom Schema Expectation Example

```python
from mlflow.genai.label_schemas import InputTextList

# Expectation schema for ground truth
facts_schema = schemas.create_label_schema(
    name="required_facts",
    type="expectation",
    title="What facts must be included in a correct response?",
    input=InputTextList(max_count=5, max_length_each=200),
    instruction="List key facts that any correct response must contain."
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Input Types for Custom Schemas

MLflow supports the following input types for collecting different kinds of feedback:

### InputCategorical

Used for single-selection from a list of options. Examples include rating scales, binary choices, and error type selection. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputCategorical

# Rating scale
rating_input = InputCategorical(
    options=["1 - Poor", "2 - Below Average", "3 - Average", "4 - Good", "5 - Excellent"]
)
```

### InputCategoricalList

Used for multiple selections from a list of options. Examples include selecting multiple error types present or content types included. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

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
```

### InputText

Used for single text entry with an optional maximum length. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputText

# General feedback
feedback_input = InputText(max_length=500)
```

### InputTextList

Used for multiple text entries with configurable maximum count and per-item length limits. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputTextList

# List of factual errors
errors_input = InputTextList(
    max_count=10,        # Maximum 10 errors
    max_length_each=150  # Each error description limited to 150 chars
)
```

### InputNumeric

Used for numeric input within a specified range, with optional minimum and maximum values. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputNumeric

# Confidence score
confidence_input = InputNumeric(
    min_value=0.0,
    max_value=1.0
)
```

## Managing Labeling Schemas

### Listing Schemas

To get information about an existing schema, use `get_label_schema()` with the schema name. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

schema = schemas.get_label_schema("response_quality")
print(f"Schema: {schema.name}")
print(f"Type: {schema.type}")
print(f"Title: {schema.title}")
```

### Updating Schemas

To update an existing schema, use `create_label_schema()` with the `overwrite` parameter set to `True`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import InputCategorical

updated_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality (updated question)",
    input=InputCategorical(options=["Excellent", "Good", "Fair", "Poor", "Very Poor"]),
    instruction="Updated: Focus on factual accuracy above all else.",
    overwrite=True  # Replace existing schema
)
```

### Deleting Schemas

To delete a labeling schema, use `delete_label_schema()`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

schemas.delete_label_schema("old_schema_name")
```

## Integration with Labeling Sessions

Schemas are automatically available when creating labeling sessions. The Review App presents questions based on the schema definitions associated with a session. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
# Schemas are referenced when creating labeling sessions
session_schemas = [
    "service_quality",      # Custom schema
    "response_issues",      # Custom schema
    schemas.EXPECTED_FACTS  # Built-in schema
]
```

## Best Practices

### Schema Design

- Write questions as clear, specific prompts.
- Provide context to guide reviewers.
- Set reasonable limits on text length and list counts.
- For categorical inputs, ensure options are mutually exclusive and comprehensive. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Schema Management

- Use descriptive, consistent names across schemas.
- When updating schemas, consider the impact on existing sessions.
- Delete unused schemas to keep your workspace organized. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — Organize review workflows using schemas
- [Review App](/concepts/mlflow-review-app.md) — The interface where domain experts apply schemas
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined evaluators that use expectation schemas
- [Feedback vs. Expectation](/concepts/feedback-vs-expectation-labels.md) — The two types of assessments schemas can represent
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The scope within which schemas must have unique names

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
