---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8f3d740d1f2a0cb01e74c96114d5712a599f36cb5176f78d77149c5767e5e61
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - best-practices-for-labeling-schema-design
    - BPFLSD
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Best practices for labeling schema design
description: Guidelines for writing clear questions, providing reviewer context, setting reasonable input limits, ensuring mutually exclusive categorical options, and managing schema lifecycles.
tags:
  - mlflow
  - best-practices
  - labeling-schemas
timestamp: "2026-06-18T14:50:57.499Z"
---

# Best practices for labeling schema design

**Labeling schemas** define the specific questions that domain experts answer when labeling existing traces in the [Review App](/concepts/mlflow-review-app.md). They structure the feedback collection process, ensuring consistent and relevant information for evaluating your [GenAI](/concepts/mlflow-genai-evaluate-api.md) application.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Well-designed labeling schemas reduce ambiguity for reviewers, improve data quality, and make it easier to build evaluation datasets. The following practices are drawn from the MLflow documentation on creating and managing labeling schemas.

## Schema design

- **Write questions as clear, specific prompts.** Avoid vague or open-ended phrasing that could lead to inconsistent interpretations across reviewers.^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Provide context to guide reviewers.** Adding instructions or comments helps reviewers understand what you are asking and what criteria to apply.^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Set reasonable limits on text length and list counts.** Use `max_length`, `max_count`, and `max_length_each` parameters to keep feedback focused and manageable.^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **For categorical inputs, ensure options are mutually exclusive and comprehensive.** Overlapping or incomplete choices force reviewers to pick inaccurately. For multiple-selection questions, use `InputCategoricalList` to allow selecting all that apply.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Schema management

- **Use descriptive, consistent names across your schemas.** Name schemas after the concept they measure (e.g., `service_quality`, `medical_safety`) to make them easy to find and reuse.^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **When updating schemas, consider the impact on existing sessions.** Changing a schema’s question or options after a labeling session has started can break consistency. If the change is significant, consider creating a new schema version instead of overwriting.^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Delete unused schemas to keep your workspace organized.** Use the API `delete_label_schema` to remove schemas that are no longer needed.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Schema scope and type

Schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md), so schema names must be unique within an experiment.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Choose the schema type carefully:

- **`feedback`** – Subjective assessments like ratings, preferences, or opinions.
- **`expectation`** – Objective ground truth like correct answers or expected behavior.

Using the correct type ensures that built-in judges (like the [Built-in LLM Judges](/concepts/built-in-llm-judges.md)) can interpret the schema correctly.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Matching input types to the question

The provided input type determines the reviewer's interaction. Choose the one that best fits your question:

- **`InputCategorical`** – Single-choice selection (e.g., quality rating, safe/unsafe).
- **`InputCategoricalList`** – Multiple-choice selection (e.g., select all issues present).
- **`InputText`** – Open-ended text with optional length limit.
- **`InputTextList`** – List of text entries (e.g., list expected facts).
- **`InputNumeric`** – Numeric score with optional min/max range.

Using the right input type reduces reviewer effort and improves consistency.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related concepts

- [Labeling Schemas](/concepts/labeling-schemas.md)
- [Review App](/concepts/mlflow-review-app.md)
- Label existing traces
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Create labeling sessions](/concepts/labeling-sessions.md)
- Build evaluation datasets
- [MLflow experiments](/concepts/mlflow-experiment.md)
- Label during development

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
