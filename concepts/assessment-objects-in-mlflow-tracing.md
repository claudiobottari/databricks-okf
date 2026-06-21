---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 422a8fc1c68a6ce7d7d32005b8ac1e269b5bf97528f45d1004692029c0a87bd2
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - assessment-objects-in-mlflow-tracing
    - AOIMT
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Assessment Objects in MLflow Tracing
description: Labels collected from domain experts are stored as Assessment objects on each Trace within a labeling session, retrievable programmatically for analysis or evaluation dataset creation
tags:
  - mlflow
  - tracing
  - data-model
  - evaluation
timestamp: "2026-06-18T14:38:42.649Z"
---

---
title: Assessment Objects in [MLflow Tracing](/concepts/mlflow-tracing.md)
summary: Structured containers that store expert feedback and expectations collected during labeling sessions, attached directly to individual MLflow Trace records.
sources:
  - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:13:02.271Z"
updatedAt: "2026-06-18T11:13:02.271Z"
tags:
  - mlflow
  - tracing
  - assessment
  - feedback
aliases:
  - assessment-objects-mlflow-tracing
  - MLflow Assessment Objects
  - assessment-objects
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Assessment Objects in [MLflow Tracing](/concepts/mlflow-tracing.md)

**Assessment Objects** are structured data containers in [MLflow Tracing](/concepts/mlflow-tracing.md) that store the labels collected from domain expert review sessions. When experts provide feedback or expectations on a trace through the Review App, MLflow stores that information as one or more `Assessment` objects attached to the corresponding [Trace](/concepts/traces.md) entity. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Relationship to Labeling Sessions

Assessment objects are created as part of a [Labeling Session](/concepts/labeling-session.md). When a labeling session is populated with traces and experts submit their evaluations, MLflow persists the resulting feedback and expectations as `Assessment` objects on each trace within the session. Because traces are copied into the labeling session at the time of addition, the assessment objects do not modify the original logged traces. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Two main types of labels map to different kinds of assessment content:

- **Expectation type** (label schema `type="expectation"`) — used when the expert provides a "ground truth" or correct answer, such as an expected summary. These are particularly valuable for constructing [Evaluation Datasets](/concepts/evaluation-datasets.md).
- **Feedback type** (label schema `type="feedback"`) — used for subjective ratings, classifications, or open‑ended comments, such as whether a summary was concise and helpful.

Both types are stored as `Assessment` objects on the trace. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Accessing Assessment Objects

After experts have completed their reviews, you can retrieve the assessment data programmatically or through the MLflow UI.

### MLflow UI

Navigate to the MLflow experiment. The assessments collected for each labeling session are visible under the experiment’s trace list, allowing you to review feedback side‑by‑side with the original trace inputs and outputs. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### MLflow SDK

Use `mlflow.search_traces()` with the labeling session’s run ID to obtain a DataFrame of all traces in that session. Each trace object contains a list of `Assessment` attachments. You can inspect these attachments to extract the collected labels for analysis or export. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

```python
labeled_traces_df = mlflow.search_traces(run_id=label_summaries.mlflow_run_id)
# Each row corresponds to a Trace; assessments can be accessed via the trace object.
```

## Using Assessments to Improve Your Application

Assessment objects serve as a bridge between human judgment and automated evaluation. When expectation‑type labels are collected, they can be converted directly into an [Evaluation Dataset](/concepts/evaluation-dataset.md) and used with `mlflow.genai.evaluate()` to systematically test new versions of your GenAI application against expert‑defined ground truth. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Feedback‑type assessments can also be analyzed to identify patterns (e.g., common failure modes) and to inform improvements to prompt engineering, tool selection, or retrieval quality. Over time, the accumulated assessment data can be used to [align judges with human feedback](/concepts/aligning-judges-with-human-experts.md), increasing the reliability of automated scoring.

## Related Concepts

- [Trace](/concepts/traces.md) — The core execution record that holds assessment objects.
- [Labeling Session](/concepts/labeling-session.md) — The container that groups traces and schemas for expert review.
- [Review App](/concepts/mlflow-review-app.md) — The UI through which experts submit assessments.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Datasets created from expectation labels for offline testing.
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — The broader practice of incorporating expert judgment into MLflow workflows.

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
