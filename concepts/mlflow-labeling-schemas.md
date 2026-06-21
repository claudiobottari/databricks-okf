---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73548180b3aed9a87e4197fb61afb4f8617b3528301e9ecca88deb3a73d65ac9
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-labeling-schemas
    - MLS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: MLflow Labeling Schemas
description: Predefined or custom templates that define the questions, format, and structure for collecting feedback or expectations during labeling sessions.
tags:
  - mlflow
  - human-feedback
  - schemas
  - labeling
timestamp: "2026-06-19T17:59:26.095Z"
---

# MLflow Labeling Schemas

**MLflow Labeling Schemas** define the structure and format of feedback questions that domain experts answer when reviewing [[MLflow Trace|MLflow Traces]] in a [Labeling Session](/concepts/labeling-session.md). They determine what types of human-generated assessments — either `Feedback` or `Expectation` data — are collected from reviewers via the [MLflow Review App](/concepts/mlflow-review-app.md). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

Every labeling session must include at least one labeling schema. Schemas specify the questions presented to reviewers and the format of the expected answers, such as categorical options or open-ended text. MLflow provides several built-in schemas and supports the creation of custom schemas for project-specific evaluation needs. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Built-in Schemas

MLflow includes the following built-in labeling schemas, accessible from `mlflow.genai.label_schemas`: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

| Schema Constant | Purpose |
|----------------|---------|
| `EXPECTED_FACTS` | Collects factual statements the response should contain |
| `EXPECTED_RESPONSE` | Captures the ideal or expected response text |
| `GUIDELINES` | Gathers assessment against predefined guidelines or policies |

These schemas cover common evaluation scenarios and can be referenced directly when creating a labeling session: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

session = labeling.create_labeling_session(
    name="customer_service_review",
    assigned_users=["alice@company.com"],
    label_schemas=[schemas.EXPECTED_FACTS],  # At least one schema required
)
```

## Creating Custom Schemas

When built-in schemas do not meet the evaluation criteria, you can create custom schemas using the `create_label_schema` function. A custom schema specifies a `name`, a `type` (either `"feedback"` or `"expectation"`), a human-readable `title`, and an `input` format (such as `InputCategorical` for multiple-choice options). The `overwrite=True` flag allows reusing the same schema name in subsequent calls. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality",
    input=schemas.InputCategorical(
        options=["Poor", "Fair", "Good", "Excellent"]
    ),
    overwrite=True,
)
```

After creation, custom schemas are referenced by their name string and can be combined with built-in schemas: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
session = labeling.create_labeling_session(
    name="quality_assessment_session",
    assigned_users=["expert@company.com"],
    label_schemas=["response_quality", schemas.EXPECTED_FACTS],
)
```

## Using Schemas in Labeling Sessions

When a labeling session is created, the selected schemas determine how reviewers see and answer questions for each trace in the session. The **Label preview** section of the UI shows how the questions will appear before the session is saved. After reviewers provide their assessments, responses are stored as `Assessments` on the traces and can be retrieved programmatically via the MLflow API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — The container that groups traces and schemas for review
- [MLflow Review App](/concepts/mlflow-review-app.md) — The UI where reviewers interact with schemas and traces
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Datasets that can be populated from labeled expectations via `sync()`
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — Collecting and using human assessments in GenAI development
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader framework for tracking, evaluating, and monitoring generative AI applications

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
