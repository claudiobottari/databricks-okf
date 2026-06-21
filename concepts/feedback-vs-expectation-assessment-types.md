---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c28dfd4eb4bc486ccbe63e99394137fdc3f04ddca6dedcc72475a93ee3d618b6
  pageDirectory: concepts
  sources:
    - label-during-development-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-vs-expectation-assessment-types
    - FVEAT
    - Expectation Assessments
  citations:
    - file: label-during-development-databricks-on-aws.md
title: Feedback vs Expectation Assessment Types
description: "Two distinct assessment types in MLflow: Feedback for subjective quality ratings/comments, and Expectation for recording what output should have been produced (ground truth)."
tags:
  - mlflow
  - annotation
  - assessment-types
timestamp: "2026-06-19T19:12:09.512Z"
---

I’ll update the page to reflect the source material provided, then append the required citation and linking.

---

title: Feedback vs Expectation Assessment Types
summary: "Two categories for labeling traces: Feedback (subjective assessments like ratings or comments) and Expectation (ground-truth outputs or values that should have been produced)."
sources:
  - label-during-development-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:32:41.764Z"
updatedAt: "2026-06-19T09:32:41.764Z"
tags:
  - mlflow
  - labeling
  - assessment-types
aliases:
  - feedback-vs-expectation-assessment-types
  - FVEAT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0

---

## Feedback vs Expectation Assessment Types

**Feedback vs Expectation Assessment Types** are the two fundamental categories of labels you can attach to traces or spans when evaluating a GenAI agent. During development, you can add these assessments directly through the [MLflow Tracing](/concepts/mlflow-tracing.md) interface, the MLflow SDK, or the Databricks REST API. The type you choose determines whether the label captures a subjective human judgment or an objective ground‑truth value. ^[label-during-development-databricks-on-aws.md]

### Feedback

A **Feedback** assessment records a subjective evaluation of quality. It is intended for opinions, ratings, or comments about the agent’s output. Examples include a numeric score for helpfulness, a boolean “is this response safe?”, or a free‑text comment. Because feedback reflects personal judgment, different reviewers may reasonably assign different values. ^[label-during-development-databricks-on-aws.md]

### Expectation

An **Expectation** assessment captures the expected output or value that the agent *should* have produced. It represents ground truth — for example, the correct answer, the required set of facts, or a guideline the response must follow. Expectations are objective and verifiable; if the agent’s actual output matches the expectation, the assessment is considered satisfied. ^[label-during-development-databricks-on-aws.md]

### Adding an Assessment

When you add an assessment to a trace or span (either in the UI, via the SDK, or through the REST API), you specify:

- **Assessment Type** – choose `Feedback` or `Expectation`.
- **Assessment Name** – a unique identifier for what the feedback is about.
- **Data Type** – `Number`, `Boolean`, or `String`.
- **Value** – your assessment (e.g., a rating, a flag, or the expected text).
- **Rationale** – optional notes explaining the value.

After saving, the label appears as a new column in the Traces tab of the MLflow Experiment UI. ^[label-during-development-databricks-on-aws.md]

### Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) – structured templates for collecting feedback and expectations in formal labeling sessions.
- [Labeling Sessions](/concepts/labeling-sessions.md) – review workflows that apply schemas to traces for expert annotation.
- Build evaluation datasets – using labeled traces (especially expectations) to create test datasets.
- [Collect end-user feedback](/concepts/end-user-feedback-collection-via-sdk.md) – capturing feedback from deployed applications.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – the instrumentation framework that produces traces and spans.

### Sources

- label-during-development-databricks-on-aws.md

# Citations

1. [label-during-development-databricks-on-aws.md](/references/label-during-development-databricks-on-aws-8241bcbb.md)
