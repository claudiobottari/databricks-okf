---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fb0ca649996947db008e84558cb4e39ca8599b559a3bbb1637d92d82fe7a986
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - label-schemas-for-structured-feedback
    - LSFSF
    - structured feedback
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Label Schemas for Structured Feedback
description: Defining structured feedback schemas using create_label_schema() with InputCategorical and InputText types to standardize expert review criteria and expected responses
tags:
  - mlflow
  - schemas
  - feedback
  - labeling
timestamp: "2026-06-19T21:53:28.417Z"
---

```markdown
---
title: Label Schemas for Structured Feedback
summary: Defining structured feedback templates using create_label_schema() with input types like InputCategorical and InputText to standardize expert annotations.
sources:
  - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T17:22:21.545Z"
updatedAt: "2026-06-19T17:22:21.545Z"
tags:
  - mlflow
  - label-schemas
  - feedback
  - annotation
aliases:
  - label-schemas-for-structured-feedback
  - LSFSF
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Label Schemas for Structured Feedback

**Label Schemas for Structured Feedback** define the fields and data types used to collect human feedback in a [[MLflow 3 for GenAI|MLflow GenAI]] labeling session. They allow developers and domain experts to provide structured evaluations (such as accuracy ratings) and expected ideal responses for traces, which can then be used for quantitative evaluation of a generative AI application.

## Overview

A label schema specifies the *type* of feedback to collect, its *name*, a human-readable *title*, and the *input format* (categorical or free‑text). Schemas are created programmatically using the `mlflow.genai.label_schemas` module and are attached to a [[Labeling Sessions|labeling session]] to guide expert reviewers. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Creating a Label Schema

Use `mlflow.genai.label_schemas.create_label_schema()` to define a schema. The function accepts the following key parameters: ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

- `name` – The identifier for the schema (e.g., `"response_accuracy"`).
- `type` – Either `"feedback"` (for evaluations like accuracy, relevance) or `"expectation"` (for an ideal answer that the app *should* produce).
- `title` – A human‑readable question or instruction shown to the reviewer.
- `input` – The type of input widget. Use `InputCategorical(options=[...])` for a set of choices, or `InputText()` for a plain‑text box.
- `overwrite` – When `True`, allows the schema to be replaced if it already exists (useful during iterative development).

## Input Types

### InputCategorical

Presents a list of predefined options to the reviewer. The resulting feedback is one of the supplied values. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### InputText

Provides an open text field where reviewers can enter free‑form responses, often used for the *expectation* type to capture the correct or ideal answer. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Usage with Labeling Sessions

After creating one or more label schemas, they are passed as a list to `create_labeling_session()`. The session’s `label_schemas` parameter determines which fields expert reviewers will see and fill in. Traces added to the session can then be evaluated against the collected labels. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Example workflow:
1. Define a `"response_accuracy"` schema of type `"feedback"` using `InputCategorical`.
2. Define an `"expected_response"` schema of type `"expectation"` using `InputText`.
3. Create a labeling session with `label_schemas=[accuracy_schema.name, expected_response_schema.name]`.
4. Add traces to the session.
5. Expert reviewers submit their structured feedback via the review UI or API.
6. Use the feedback (e.g., the `expected_response` field) with scorers like [[Correctness Scorer]] to evaluate the app.

## Related Concepts

- [[MLflow 3 for GenAI|MLflow GenAI]] – The broader feature set for developing and monitoring generative AI applications.
- [[MLflow Human Feedback Collection|Human Feedback]] – Overview of collecting end‑user and expert feedback.
- Expert Review – Methods for obtaining authoritative assessments from domain experts.
- [[Labeling Sessions]] – Containers that group traces and schemas for expert review.
- [[GluonTS Evaluation Metrics|Evaluation Metrics]] – Quantitative measures computed from expert‑provided labels.
- [[MLflow Tracing]] – The instrumentation layer that captures trace data for each interaction.

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md
```

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
