---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7dcfc0728a99ac85bf25334c3379137704e7c4231c3dd4fa8e43e4ee2206fc5
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-human-feedback-collection
    - MHFC
    - Human Feedback Collection
    - Human feedback collection
    - Human Feedback
    - Human Feedback Annotations
    - Human Feedback Collection|human feedback
    - Human feedback
    - Human feedback for GenAI
    - feedback collection
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
title: MLflow Human Feedback Collection
description: System for collecting expert or human feedback on GenAI application traces using labeling schemas, labeling sessions, and the Review App UI.
tags:
  - mlflow
  - human-feedback
  - labeling
  - genai
timestamp: "2026-06-19T18:59:14.386Z"
---

---

title: MLflow Human Feedback Collection
summary: A framework for collecting human feedback on GenAI application traces using label schemas, labeling sessions, and the Review App, with support for end-user feedback via the MLflow SDK.
sources:
  - get-started-mlflow-3-for-genai-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:34:18.702Z"
updatedAt: "2026-06-18T14:14:46.100Z"
tags:
  - mlflow
  - human-feedback
  - genai
  - evaluation
aliases:
  - mlflow-human-feedback-collection
  - MHFC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0

---

# MLflow Human Feedback Collection

MLflow Human Feedback Collection provides a structured framework for gathering, managing, and using human feedback to evaluate and improve GenAI applications. It supports two primary feedback workflows: **end-user feedback** logged programmatically within an application, and **expert feedback** collected through structured labeling sessions and the Review App. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Overview

Human feedback complements automated LLM-as-a-judge evaluation by providing ground-truth assessments from domain experts and real-world user reactions. The typical workflow involves:

1. Tracing a GenAI application with [MLflow Tracing](/concepts/mlflow-tracing.md).
2. Collecting end-user feedback via `mlflow.log_feedback()`.
3. Defining label schemas that specify what feedback to collect from experts.
4. Creating labeling sessions and adding traces for review.
5. Sharing a Review App link with expert reviewers.
6. Viewing collected feedback in the MLflow UI or querying it programmatically.

^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## End-User Feedback

End-user feedback captures real-time reactions from application users (e.g., thumbs up/down, star ratings, comments). This feedback is logged to a specific trace using the `mlflow.log_feedback()` SDK call. The trace ID is typically returned to the frontend along with the model response; when the user provides feedback, the frontend calls a backend endpoint that invokes `log_feedback()` with the trace ID. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

For detailed usage, see the [Collect user feedback](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/collect-user-feedback/) documentation.

## Expert Feedback via Labeling Sessions

For authoritative assessments that serve as ground truth, MLflow provides structured labeling sessions. Domain experts review traces and provide standardized feedback using predefined label schemas.

### Label Schemas

A label schema defines the type of feedback to collect. MLflow supports **feedback schemas** (categorical ratings) and **expectation schemas** (free-text ideal responses). Schemas are created using `create_label_schema()` from `mlflow.genai.label_schemas`. The following example creates a feedback schema for rating humor: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical

humor_schema = create_label_schema(
    name="response_humor",
    type="feedback",
    title="Rate how funny the response is",
    input=InputCategorical(options=["Very funny", "Slightly funny", "Not funny"]),
    overwrite=True,
)
```

### Creating Labeling Sessions

Labeling sessions group traces for expert review. They are created using `create_labeling_session()` from `mlflow.genai.labeling`, which accepts a name and a list of label schema names. Traces are added to the session with `add_traces()`. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
from mlflow.genai.labeling import create_labeling_session

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[humor_schema.name],
)

traces = mlflow.search_traces(max_results=10)
labeling_session.add_traces(traces)

print(f"Share this link with reviewers: {labeling_session.url}")
```

Each labeling session generates a shareable URL that reviewers access through the **Review App**.

### Using the Review App

Expert reviewers open the provided URL to view traces, assess responses using the defined label schemas (e.g., selecting "Very funny", "Slightly funny", or "Not funny"), and optionally provide ideal responses or comments. The assessments are stored and associated with the trace. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Creating Sessions via the UI

Labeling sessions can also be created through the MLflow UI. On the Experiment page, click the **Labeling** tab. Use the **Sessions** and **Schemas** sub-tabs to add new label schemas and create sessions without writing code. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Viewing Feedback in the MLflow UI

Collected feedback appears in the MLflow Experiment UI. Open the active experiment and click the **Labeling** tab to see all sessions, schemas, and individual assessments. Expert ratings and end-user feedback are visible there. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Programmatic Access to Feedback

To work with feedback programmatically:
- Use `mlflow.search_traces()` to retrieve traces that include expert assessments. The assessments are stored as part of the trace data and can be filtered and analyzed.
- Use `mlflow.log_feedback()` to log end-user feedback within an application (see the [Collect user feedback](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/collect-user-feedback/) page for details).

^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Using Feedback for Evaluation

Expert-provided labels, especially expectation schemas that contain ideal responses, can be used as ground truth for automated evaluation. MLflow's `Correctness` scorer can compare application outputs against expected responses stored in labeled traces. For production use, Databricks recommends adding labeled traces to an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) for version tracking and lineage. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The foundation for associating feedback with specific application traces.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Automated evaluation using LLM-as-a-judge scorers.
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) — Versioned datasets for tracking evaluation data.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — MLflow's capabilities for generative AI applications.
- [Review App](/concepts/mlflow-review-app.md) — The UI used by expert reviewers to provide feedback.

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
