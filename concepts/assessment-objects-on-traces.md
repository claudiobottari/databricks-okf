---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4096b8f4165583997d081feb1ce47f1edd475dc5f94056330edfc127bffbfd98
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assessment-objects-on-traces
    - AOOT
    - assessment-objects-in-mlflow-tracing
    - AOIMT
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Assessment Objects on Traces
description: Labels collected from domain experts are stored as Assessment objects on each Trace within a labeling session, retrievable via MLflow SDK for analysis and evaluation dataset creation.
tags:
  - mlflow
  - data-model
  - labeling
timestamp: "2026-06-18T10:59:58.293Z"
---

# Assessment Objects on Traces

In MLflow GenAI, expert feedback and expectations collected through labeling sessions are stored as **`Assessment` objects** on each [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) within the labeling session. These objects provide a structured way to attach human-generated labels to specific application interactions, enabling later analysis, evaluation dataset creation, and automated judge alignment. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## How Assessment Objects Are Created

When domain experts use the [Review App](/concepts/mlflow-review-app.md) (or a customized version) to label existing traces, their responses to the labeling schemas defined for the session are recorded as `Assessment` objects. Each labeling schema specifies a question and input type – for example, a categorical rating (“Yes”/“No”) or free‑form text – and the expert’s answer becomes part of an `Assessment` attached to the trace they reviewed. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Labels can be of type **feedback** (subjective assessments, ratings, classifications) or **expectation** (ground‑truth answers). Both types are stored as `Assessment` objects on the trace. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Storing Assessments on Traces

When a labeling session is created and traces are added to it, the traces are copied into the session’s run so that any labels added during the review do not alter the original logged traces. The `Assessment` objects are then attached to each copied trace within that labeling session run. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Retrieving Assessments

After experts have completed their reviews, you can retrieve the collected labels programmatically using the MLflow SDK. The following example fetches all traces from a labeling session’s run and extracts the assessments into a pandas DataFrame for analysis: ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

```python
labeled_traces_df = mlflow.search_traces(run_id=label_summaries.mlflow_run_id)
```

Each row in the resulting DataFrame corresponds to a trace; the `Assessment` objects can be accessed through the trace’s attributes, such as `trace.assessments` (depending on the MLflow version). The exact API for inspecting individual assessments on a trace is documented in the [MLflow entity reference](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Assessment). ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Using Assessments

Assessment objects are the foundation for turning expert knowledge into reusable evaluation data. Expectation-type labels (e.g., a corrected summary) are particularly valuable because they can be directly used to create [Evaluation Datasets](/concepts/evaluation-datasets.md) for automated testing with `mlflow.genai.evaluate()`. Feedback-type labels can be used to refine automated judges or to monitor quality trends over time. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [Trace](/concepts/traces.md) – The core execution record that carries assessments
- [Labeling Sessions](/concepts/labeling-sessions.md) – Organize traces for expert review
- [Labeling Schemas](/concepts/labeling-schemas.md) – Define the questions and input types for assessments
- [Review App](/concepts/mlflow-review-app.md) – The UI where experts apply assessments
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Can be built from expectation-type assessments
- Feedback (MLflow) – The output object used in code‑based scorers

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
