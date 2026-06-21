---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e59d5d9d962138caaa6af161ac274c09505d93235193910401305c7366a65e0b
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema-crud-management
    - LSCM
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling schema CRUD management
description: "API-driven lifecycle management for labeling schemas: create (with overwrite), get, list, update, and delete operations scoped to MLflow experiments."
tags:
  - mlflow
  - api
  - schema-management
timestamp: "2026-06-18T14:51:03.090Z"
---

# Labeling Schema CRUD Management

**Labeling schema CRUD management** refers to the set of operations — Create, Read, Update, Delete — used to define, inspect, modify, and remove labeling schemas within MLflow. Labeling schemas structure the feedback that domain experts provide when reviewing traces in the Review App, ensuring consistent and relevant evaluation of GenAI applications.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

Labeling schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md); schema names must be unique within an experiment. Each schema represents either a `feedback` assessment (subjective ratings, opinions) or an `expectation` assessment (objective ground truth). The schema controls the question shown to reviewers, the input method (e.g., drop-down menu or text box), validation rules, and optional instructions.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Schemas are applied when creating [Labeling Sessions](/concepts/labeling-sessions.md). When a session is created, it is associated with one or more schemas; the Review App then presents the corresponding questions to the reviewer.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Creating Labeling Schemas

Schemas can be created through the MLflow UI or via the Python API.

### Using the UI

1. In the Databricks workspace, navigate to **Experiments** and open your experiment.
2. Click **Labeling schemas** in the sidebar.
3. Click **Add Label Schema** and fill in the fields:
   - **Name** – unique within the experiment.
   - **Type** – `Feedback` or `Expectation`.
   - **Title** – the prompt shown to reviewers.
   - **Input type** – one of the supported input types (see below). The UI dynamically shows relevant options such as length limits, categorical choices, or numeric ranges.
4. Click **Save**.[^ui]

[^create-and-manage-labeling-schemas-databricks-on-aws.md]: The UI creation process is described in the "Create custom schemas using the UI" section, including the dynamic form and save button.

### Using the API

Use `mlflow.genai.label_schemas.create_label_schema()`. All schemas require a name, type, title, and input specification.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical

quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the overall quality of this response",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness."
)
```

MLflow also provides predefined schema names for [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that use expectations (e.g., `EXPECTED_FACTS`, `GUIDELINES`, `EXPECTED_RESPONSE`). These can be created with the same API to ensure compatibility with built-in evaluation functionality.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Reading Labeling Schemas

To retrieve information about an existing schema, use `get_label_schema()` by name.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schema = schemas.get_label_schema("response_quality")
print(f"Name: {schema.name}, Type: {schema.type}, Title: {schema.title}")
```

## Updating Labeling Schemas

To update a schema, call `create_label_schema()` with the same name and set `overwrite=True`. This replaces the existing definition.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

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

Changes take effect immediately. When updating, consider the impact on any existing labeling sessions that already use the schema.

## Deleting Labeling Schemas

Use `delete_label_schema()` to remove a schema that is no longer needed.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schemas.delete_label_schema("old_schema_name")
```

Deleting a schema removes it from the experiment. Unused schemas should be cleaned up to keep the workspace organized.

## Input Types for Custom Schemas

MLflow supports five input types for collecting different kinds of feedback:^[create-and-manage-labeling-schemas-databricks-on-aws.md]

| Input Type | Description | Example Use |
|------------|-------------|-------------|
| `InputCategorical` | Single selection from a list of options | Rating scale, binary safe/unsafe |
| `InputCategoricalList` | Multiple selections from a list of options | Identifying all present issues |
| `InputText` | Single line or paragraph of text | Short feedback, improvement suggestions |
| `InputTextList` | List of text items with optional max count and per-item length | List of factual errors, required steps |
| `InputNumeric` | Numeric value within a specified range | Confidence score (0–1), accuracy rating |

Each input type accepts validation parameters such as `max_length`, `min_value`, `max_value`, `max_count`, and `options`. An `enable_comment` flag can be added to any schema to allow reviewers to include an extra free‑text comment.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

- **Schema design**: Write questions as clear, specific prompts. Provide context in the `instruction` field. Set reasonable limits on text length and list counts. For categorical inputs, ensure options are mutually exclusive and comprehensive.^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Schema management**: Use descriptive, consistent names. When updating schemas, consider the effect on existing labeling sessions. Delete unused schemas to keep the workspace organized.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — Organize review workflows using schemas
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined schema names for expectations
- [Review App](/concepts/mlflow-review-app.md) — Where schemas are presented to domain experts
- Label During Development — Detailed guide on feedback vs. expectation types
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Using labeled data for offline scoring

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
