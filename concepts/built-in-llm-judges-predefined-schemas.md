---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 849202f98904086854e3045e4259e82c01ad051b0acd96d9590ace4999d8aea0
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-llm-judges-predefined-schemas
    - BLJPS
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Built-in LLM judges predefined schemas
description: Predefined labeling schema names (EXPECTED_FACTS, GUIDELINES, EXPECTED_RESPONSE) that ensure compatibility with MLflow's built-in LLM evaluation judges.
tags:
  - mlflow
  - llm-judges
  - evaluation
timestamp: "2026-06-18T14:51:09.561Z"
---

# Built-in LLM Judges Predefined Schemas

**Built-in LLM judges predefined schemas** are preconfigured [Labeling Schema](/concepts/labeling-schema.md) names provided by [MLflow](/concepts/mlflow.md) that correspond to the built-in [LLM judges (scorers)](/concepts/llm-judges-and-scorers.md). These schemas define the structure for collecting [expectations (ground truth)](/concepts/expectations-in-mlflow-evaluation.md) that the built-in judges use during evaluation, enabling consistent feedback collection that is directly compatible with MLflow's automated evaluation functionality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

MLflow provides predefined schema names for the built-in LLM judges that use expectations. When you create a labeling schema using one of these predefined names, the schema is automatically compatible with the corresponding built-in judge's evaluation logic. This ensures that the [expectations](/concepts/expectation-vs-feedback-labels.md) collected from human reviewers through the [Review App](/concepts/mlflow-review-app.md) can be directly used by the built-in judges during automated evaluation. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

These predefined schemas apply only when using the Review App to label existing traces. They are not used for vibe checks in the Review App Chat UI. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Predefined Schema Names

MLflow exposes the following predefined schema names as constants in the `mlflow.genai.label_schemas` module:

| Constant | Description |
|----------|-------------|
| `EXPECTED_FACTS` | Schema for collecting a list of facts that the judge expects to see in a correct response |
| `GUIDELINES` | Schema for collecting guidelines that the model's output is expected to follow |
| `EXPECTED_RESPONSE` | Schema for collecting a complete correct agent response |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Usage Pattern

To create a labeling schema using a predefined name, you call `schemas.create_label_schema()` with the corresponding constant as the `name` parameter. Each schema type has specific input requirements:

### Expected Facts Schema

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import LabelSchemaType, InputTextList

expected_facts_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_FACTS,                    # Predefined name
    type=LabelSchemaType.EXPECTATION,                # Must be EXPECTATION
    title="Expected facts",
    input=InputTextList(max_length_each=1000),       # List of text items
    instruction="Please provide a list of facts that you expect to see in a correct response.",
    overwrite=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Guidelines Schema

```python
guidelines_schema = schemas.create_label_schema(
    name=schemas.GUIDELINES,                         # Predefined name
    type=LabelSchemaType.EXPECTATION,
    title="Guidelines",
    input=InputTextList(max_length_each=500),        # List of text items
    instruction="Please provide guidelines that the model's output is expected to adhere to.",
    overwrite=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Expected Response Schema

```python
from mlflow.genai.label_schemas import InputText

expected_response_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_RESPONSE,                  # Predefined name
    type=LabelSchemaType.EXPECTATION,
    title="Expected response",
    input=InputText(),                               # Single text input
    instruction="Please provide a correct agent response.",
    overwrite=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Schema Type Requirement

All predefined schemas for built-in LLM judges must be of type `EXPECTATION`. This is because built-in judges rely on objective ground truth (expectations) to evaluate model outputs, rather than subjective ratings (feedback). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Using Predefined Schemas in Labeling Sessions

Once created, predefined schemas are automatically available when creating [Labeling Sessions](/concepts/labeling-sessions.md). The Review App will present the questions defined by the schema to human reviewers, and the collected expectations can then be used by the corresponding built-in judges during evaluation. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
# Schemas are available by name when creating labeling sessions
session_schemas = [
    "service_quality",      # Custom schema
    "response_issues",      # Custom schema
    schemas.EXPECTED_FACTS  # Built-in schema (constant or string)
]
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Managing Predefined Schemas

Predefined schemas follow the same management rules as custom schemas:

- **Unique names**: Schema names must be unique within an [MLflow Experiment](/concepts/mlflow-experiment.md). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Overwrite**: To update a predefined schema, call `create_label_schema()` with `overwrite=True`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Delete**: Use `schemas.delete_label_schema()` to remove schemas that are no longer needed. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Retrieve**: Use `schemas.get_label_schema()` to inspect an existing schema's configuration. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

- Always use the `overwrite=True` parameter when recreating an existing schema to avoid conflicts. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Ensure the input type matches the judge's expectations (e.g., `InputTextList` for lists of facts or guidelines, `InputText` for a single expected response). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Provide clear instructions to guide human reviewers in providing consistent, high-quality expectations. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — General concept for defining feedback collection structures
- [LLM judges (scorers)](/concepts/llm-judges-and-scorers.md) — Automated evaluators that use these schemas
- [Review App](/concepts/mlflow-review-app.md) — Interface for human reviewers to provide labels
- [Labeling Sessions](/concepts/labeling-sessions.md) — Organized review workflows using schemas
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Transformed labeled data for testing
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — Overall framework for GenAI application evaluation
- [Human feedback alignment](/concepts/human-feedback-for-llm-judge-alignment.md) — Process of aligning judges with expert annotations

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
