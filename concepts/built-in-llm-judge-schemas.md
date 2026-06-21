---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6276d49e3df4b1cf0d2e355195c525da79750e561b6ae6ce8cbd85679349449
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-llm-judge-schemas
    - BLJS
    - built-in-llm-judge-labeling-schemas
    - BLJLS
    - built-in-llm-judges-predefined-schemas
    - BLJPS
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Built-in LLM Judge schemas
description: Predefined labeling schema names (EXPECTED_FACTS, GUIDELINES, EXPECTED_RESPONSE) provided by MLflow for compatibility with built-in LLM Judges.
tags:
  - mlflow
  - llm-judges
  - evaluation
  - predefined-schemas
timestamp: "2026-06-19T17:58:59.373Z"
---

# Built-in LLM Judge Schemas

**Built-in LLM Judge Schemas** are predefined labeling schema names provided by [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that correspond to the built-in LLM judges used for automated evaluation. These schemas define the structure for collecting human feedback that aligns with the expectations used by built-in judges, enabling compatibility between human labeling workflows and automated evaluation. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

Labeling schemas define the specific questions that domain experts answer when labeling existing traces in the Review App. They structure the feedback collection process, ensuring consistent and relevant information for evaluating your GenAI application. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

MLflow provides predefined schema names for the built-in LLM judges that use expectations. You can create custom schemas using these names to ensure compatibility with the built-in evaluation functionality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Predefined Labeling Schemas

The following table shows the predefined labeling schemas and their usage:

| Schema Name | Type | Purpose |
|-------------|------|---------|
| `EXPECTED_FACTS` | Expectation | Collects a list of facts that should appear in a correct response |
| `GUIDELINES` | Expectation | Collects guidelines that the model's output is expected to adhere to |
| `EXPECTED_RESPONSE` | Expectation | Collects a correct agent response |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Creating Built-in Judge Schemas

To create a labeling schema for a built-in LLM judge, use `mlflow.genai.label_schemas.create_label_schema()` with the predefined schema name. All schemas require a name, type, title, and input specification. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Expected Facts Schema

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import LabelSchemaType, InputTextList

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

### Guidelines Schema

```python
guidelines_schema = schemas.create_label_schema(
    name=schemas.GUIDELINES,
    type=LabelSchemaType.EXPECTATION,
    title="Guidelines",
    input=InputTextList(max_length_each=500),
    instruction="Please provide guidelines that the model's output is expected to adhere to.",
    overwrite=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Expected Response Schema

```python
from mlflow.genai.label_schemas import InputText

expected_response_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_RESPONSE,
    type=LabelSchemaType.EXPECTATION,
    title="Expected response",
    input=InputText(),
    instruction="Please provide a correct agent response.",
    overwrite=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Schema Types

Schemas are one of two types: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

- **`feedback`**: Subjective assessments like ratings, preferences, or opinions.
- **`expectation`**: Objective ground truth like correct answers or expected behavior.

Built-in LLM judge schemas are all of type `expectation`, as they define the expected behavior or content that judges evaluate against. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Integration with Labeling Sessions

When you create a labeling session, you associate it with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. The schemas control: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

- The question shown to reviewers.
- The input method (for example, drop-down menu or text box).
- Validation rules and constraints.
- Optional instructions and comments.

Built-in judge schemas are automatically available when creating labeling sessions. The Review App presents questions based on your schema definitions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
# Example: Using schemas in a session
session_schemas = [
    "service_quality",      # Your custom schema
    "response_issues",      # Your custom schema
    schemas.EXPECTED_FACTS  # Built-in schema
]
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Managing Schemas

### List Schemas

To get information about an existing schema, use `mlflow.genai.label_schemas.get_label_schema()`. You must provide the name of the schema. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

schema = schemas.get_label_schema("response_quality")
print(f"Schema: {schema.name}")
print(f"Type: {schema.type}")
print(f"Title: {schema.title}")
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Update Schemas

To update an existing schema, use `create_label_schema()` and set the `overwrite` parameter to `True`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
updated_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality (updated question)",
    input=InputCategorical(options=["Excellent", "Good", "Fair", "Poor", "Very Poor"]),
    instruction="Updated: Focus on factual accuracy above all else.",
    overwrite=True  # Replace existing schema
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Delete Schemas

To delete a labeling schema, use `mlflow.genai.label_schemas.delete_label_schema()`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schemas.delete_label_schema("old_schema_name")
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Input Types

MLflow supports several input types for collecting different kinds of feedback in labeling schemas: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

| Input Type | Description | Use Case |
|------------|-------------|----------|
| `InputCategorical` | Single selection from options | Rating scales, binary choices |
| `InputCategoricalList` | Multiple selection from options | Identifying multiple issues |
| `InputText` | Free-form text input | General feedback, short answers |
| `InputTextList` | List of text items | Expected facts, guidelines |
| `InputNumeric` | Numeric range input | Confidence scores, ratings |

## Best Practices

- **Write questions as clear, specific prompts.** Provide context to guide reviewers. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Set reasonable limits** on text length and list counts to keep feedback focused. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Use descriptive, consistent names** across your schemas. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **When updating schemas**, consider the impact on existing labeling sessions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Delete unused schemas** to keep your workspace organized. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — The general concept of defining feedback collection structures
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — The automated evaluation judges that use these schemas
- [Labeling Sessions](/concepts/labeling-sessions.md) — Organizing review workflows using schemas
- Human Feedback Alignment — Aligning judge accuracy with expert annotations
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Transforming labeled data into test datasets

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
