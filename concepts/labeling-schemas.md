---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dcc203ae2f590d4935be6f8cfb6f4d871ed686189e793b79236092b3509e09ae
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schemas
    - Create and Manage Labeling Schemas
    - Create and manage labeling schemas
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Labeling Schemas
description: Definitions of the questions and input types (categorical, numeric, free-text) that domain experts use to provide feedback or expectations on traces within the Review App.
tags:
  - mlflow
  - labeling
  - configuration
timestamp: "2026-06-19T17:45:59.596Z"
---

# Labeling Schemas

**Labeling schemas** define the questions and input types that domain experts use to provide feedback on traces during a labeling session. They are a core component of MLflow's Review App, enabling structured collection of human feedback—either as subjective assessments or as ground-truth expectations.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Types of Labeling Schemas

There are two main types of labeling schemas:^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

- **Expectation Type (`type="expectation"`)**: Used when the expert provides a "ground truth" or a correct answer—for example, supplying the `expected_facts` for a RAG system's response. These labels can be directly used in evaluation datasets.
- **Feedback Type (`type="feedback"`)**: Used for subjective assessments, ratings, or classifications—for example, rating a response on a scale of 1–5 for politeness, or classifying whether a response met certain criteria.

## Input Methods

Schemas support several input methods to match the kind of feedback being collected:^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

- **Categorical choices** – a fixed set of options (e.g., "Yes" / "No").
- **Numeric scales** – a numerical range for ratings.
- **Free-form text** – open-ended text input.

These input types are provided through MLflow's `InputCategorical`, `InputText`, and related classes.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Defining a Schema

Labeling schemas are created using the `create_label_schema` function from `mlflow.genai.label_schemas`. Each schema must have a name, a type (`"feedback"` or `"expectation"`), a title visible to reviewers, and an input definition. Additional options include an instruction text, an `enable_comment` flag, and `overwrite` behavior.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

The following example creates two schemas: one for collecting a categorical quality rating, and one for collecting a ground-truth summary:^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText

summary_quality = create_label_schema(
    name="summary_quality",
    type="feedback",
    title="Is this summary concise and helpful?",
    input=InputCategorical(options=["Yes", "No"]),
    instruction="Please provide a rationale below.",
    enable_comment=True,
    overwrite=True,
)

expected_summary = create_label_schema(
    name="expected_summary",
    type="expectation",
    title="Please provide the correct summary for the user's request.",
    input=InputText(),
    overwrite=True,
)
```

## Usage in Labeling Sessions

Labeling schemas are attached to a [Labeling Session](/concepts/labeling-session.md) when it is created. Domain experts use the Review App to view traces and provide responses according to each schema. The collected labels are stored as [Assessment](/concepts/assessments.md) objects on the traces within the session.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Built-in Schemas

MLflow provides built-in schemas that can be used directly without creating custom definitions. These include `EXPECTED_FACTS`, `EXPECTED_RESPONSE`, and `GUIDELINES`. Built-in schemas are accessed through `mlflow.genai.label_schemas` and can be mixed with custom schemas in the same labeling session.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Converting Labels to Evaluation Datasets

Labels of the `expectation` type are particularly useful for creating [Evaluation Datasets](/concepts/evaluation-datasets.md). These datasets can then be used with `mlflow.genai.evaluate()` to systematically test new versions of a GenAI application against expert-defined ground truth.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

The `sync()` method on labeling sessions performs an intelligent upsert operation that synchronizes expectations to evaluation datasets. Each trace's inputs serve as a unique key to identify records in the dataset, and expectations from the labeling session overwrite existing expectations when the expectation names match.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) – the mechanism for organizing traces and schemas for review
- [Review App](/concepts/mlflow-review-app.md) – the user interface where domain experts use schemas to label traces
- [Assessment (MLflow)](/concepts/assessments-mlflow-genai.md) – the stored label object on a trace
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – datasets built from expectation-type labels
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – the broader framework for evaluating and monitoring GenAI applications

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
2. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
