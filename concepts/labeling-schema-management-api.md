---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e803ff0c73fc7c023d82dada6e15159a912136e5db36677324614ffb3d6a2a1
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema-management-api
    - LSMA
    - labeling-schema-crud-management
    - LSCM
    - labeling-schema-lifecycle-management
    - LSLM
    - LLM
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling schema management API
description: "CRUD operations for labeling schemas via the MLflow API: create_label_schema, get_label_schema, and delete_label_schema, with overwrite support for updates."
tags:
  - mlflow
  - api
  - schema-management
timestamp: "2026-06-19T17:58:55.475Z"
---

# Labeling Schema Management API

The **Labeling Schema Management API** is a set of programmatic interfaces in MLflow that allow users to create, read, update, and delete labeling schemas for structured human feedback collection in GenAI applications. Labeling schemas define the specific questions that domain experts answer when labeling existing traces in the Review App, structuring the feedback collection process to ensure consistent and relevant information for evaluating GenAI applications. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

Labeling schemas control the question shown to reviewers, the input method (such as drop-down menus or text boxes), validation rules and constraints, and optional instructions and comments. Schemas are scoped to experiments, so schema names must be unique within an MLflow experiment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

When a labeling session is created, it is associated with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. Assessments are either `Feedback` (subjective assessments like ratings, preferences, or opinions) or `Expectation` (objective ground truth such as correct answers or expected behavior). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## API Functions

### Creating Schemas

Schemas are created using `mlflow.genai.label_schemas.create_label_schema()`. All schemas require a name, type, title, and input specification. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical, InputText

quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness when rating.",
)
```

### Retrieving Schemas

To get information about an existing schema, use `mlflow.genai.label_schemas.get_label_schema()` with the schema name: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schema = schemas.get_label_schema("response_quality")
print(f"Schema: {schema.name}")
print(f"Type: {schema.type}")
print(f"Title: {schema.title}")
```

### Updating Schemas

To update an existing schema, use `create_label_schema` with the `overwrite` parameter set to `True`: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
updated_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality (updated question)",
    input=InputCategorical(options=["Excellent", "Good", "Fair", "Poor", "Very Poor"]),
    instruction="Updated: Focus on factual accuracy above all else.",
    overwrite=True
)
```

### Deleting Schemas

To delete a labeling schema, use `mlflow.genai.label_schemas.delete_label_schema()`: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schemas.delete_label_schema("old_schema_name")
```

## Predefined Schemas for Built-in LLM Judges

MLflow provides predefined schema names for the built-in LLM Judges that use expectations. Custom schemas can be created using these names to ensure compatibility with built-in evaluation functionality. The predefined schemas include: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

- `schemas.EXPECTED_FACTS` — For collecting expected facts
- `schemas.GUIDELINES` — For collecting guidelines
- `schemas.EXPECTED_RESPONSE` — For collecting expected responses

## Input Types

The API supports several input types for collecting different kinds of feedback: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

| Input Type | Description | Example |
|---|---|---|
| `InputCategorical` | Single selection from a list of options | Rating scale, binary choices |
| `InputCategoricalList` | Multi-select from a list of options | Multiple error types |
| `InputText` | Free-form text with optional length limit | General feedback, short answers |
| `InputTextList` | List of text items with count and length limits | List of factual errors |
| `InputNumeric` | Numeric value with optional range | Confidence score, rating scale |

## Integration with Labeling Sessions

Schemas created through the API are automatically available when creating labeling sessions. The Review App presents questions based on schema definitions when reviewers label existing traces. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

**Schema design:** Write questions as clear, specific prompts. Provide context to guide reviewers. Set reasonable limits on text length and list counts. For categorical inputs, ensure options are mutually exclusive and comprehensive. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

**Schema management:** Use descriptive, consistent names across schemas. When updating schemas, consider the impact on existing sessions. Delete unused schemas to keep the workspace organized. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — Organizing review workflows using labeling schemas
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Structured feedback collection for GenAI evaluation
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined scorers for automated evaluation
- [Review App](/concepts/mlflow-review-app.md) — The UI where reviewers label traces using schemas
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Transforming labeled data into test datasets

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
