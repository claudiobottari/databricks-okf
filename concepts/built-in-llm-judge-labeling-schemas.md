---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8c7ad36608aa92b8ad01ef42c5be1769f0e8bd9a8cb64fd991b5c3131bc2229
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-llm-judge-labeling-schemas
    - BLJLS
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Built-in LLM Judge Labeling Schemas
description: Predefined schema names (e.g., EXPECTED_FACTS, GUIDELINES, EXPECTED_RESPONSE) provided by MLflow for compatibility with built-in LLM Judges that use the Expectation type.
tags:
  - mlflow
  - llm-judges
  - genai
timestamp: "2026-06-19T14:33:11.294Z"
---

# Built-in LLM Judge Labeling Schemas

**Built-in LLM Judge Labeling Schemas** are predefined labeling schemas provided by MLflow that correspond to the [Built-in LLM Judges](/concepts/built-in-llm-judges.md). They define the specific questions that domain experts answer when labeling existing traces in the [Review App](/concepts/mlflow-review-app.md), ensuring consistent collection of expectations that align with the automated judges’ criteria. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

A labeling schema is a structured question template that controls what reviewers see, the input method (e.g., drop‑down menu or text box), validation rules, and optional instructions. When you associate a labeling session with a schema, each trace in the session displays the schema’s question to the reviewer. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

MLflow ships a set of built-in LLM judges that evaluate [GenAI](/concepts/mlflow-genai-evaluate-api.md) outputs against expectations (objective ground truth). For each such judge, MLflow provides a predefined schema name you can use to create compatible labeling schemas. This allows human‑labeled expectations to serve as ground truth for the same criteria the automated judge uses. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Predefined Schema Names

The built-in schema names are constants in the `mlflow.genai.label_schemas` module. They all have the type `EXPECTATION` (as opposed to `FEEDBACK`). The source documentation lists the following predefined names via examples, though a complete table is referenced: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

| Predefined Constant | Purpose |
|---------------------|---------|
| `schemas.EXPECTED_FACTS` | Collects a list of facts that should appear in a correct response. |
| `schemas.GUIDELINES` | Collects guidelines the model’s output is expected to adhere to. |
| `schemas.EXPECTED_RESPONSE` | Collects a complete correct agent response. |

These schemas are designed to capture human‑provided ground truth that can be compared against the verdicts of the corresponding built-in LLM judges. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Creating Custom Schemas for Compatibility

You can create your own labeling schemas using these predefined names to ensure compatibility with the built-in judges. The `create_label_schema()` function in `mlflow.genai.label_schemas` accepts the constant name, a type (must be `LabelSchemaType.EXPECTATION` to match the built-in judge), a title, an input specification, and optional instructions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import LabelSchemaType, InputTextList, InputText

expected_facts_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_FACTS,
    type=LabelSchemaType.EXPECTATION,
    title="Expected facts",
    input=InputTextList(max_length_each=1000),
    instruction="Please provide a list of facts that you expect to see in a correct response.",
    overwrite=True
)
```

The `overwrite=True` parameter replaces any existing schema with the same name. The input types for built-in judges are typically `InputTextList` (for lists of facts or guidelines) or `InputText` (for a single expected response). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Usage in Labeling Sessions

After creating a labeling schema using a built-in judge name, the schema is automatically available when you create a [Labeling Session](/concepts/labeling-session.md) via the Review App or API. The Review App then presents the schema’s question to reviewers, who provide the ground‑truth expectations. These labels can later be used to evaluate the built-in judge’s accuracy or to build [Evaluation Datasets](/concepts/evaluation-datasets.md). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) – General mechanism for defining questions to human reviewers.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Automated scorers that use expectations for evaluation.
- [Review App](/concepts/mlflow-review-app.md) – The interface where experts label traces.
- [Expectation vs. Feedback](/concepts/expectation-vs-feedback-labels.md) – Distinction between objective ground truth (expectation) and subjective opinion (feedback).
- [Labeling Sessions](/concepts/labeling-sessions.md) – Organized review workflows that apply one or more schemas.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The broader MLflow module for generative AI evaluation and monitoring.

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
