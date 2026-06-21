---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eeffe131a3f9588bbb4cb293c696accb2ef3fb404e12d73480c9aea5d6777ede
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - developer-annotations-via-mlflow-ui
    - DAVMU
    - Developer Annotations via UI
    - Developer Annotations
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Developer Annotations via MLflow UI
description: Interactive method for developers to add feedback scores and rationale directly in the MLflow UI's Assessments tab on individual trace spans.
tags:
  - mlflow
  - annotations
  - ui
  - feedback
timestamp: "2026-06-19T17:22:49.921Z"
---

Here is the wiki page for "Developer Annotations via MLflow UI".

---

## Developer Annotations via MLflow UI

**Developer Annotations via MLflow UI** is a feature that allows developers and domain experts to add structured feedback, notes, and assessments to specific spans within an [MLflow](/concepts/mlflow.md) trace. This annotation workflow is part of the broader human feedback system in Databricks MLflow 3 (MLflow 3), enabling users to record qualitative and quantitative evaluations directly in the [MLflow UI](/concepts/mlflow.md) without requiring SDK calls.

## Overview

Developer annotations are a type of [Assessment](/concepts/assessments.md) that can be added to any span in a trace, including the root span. They are distinct from end-user feedback in that they provide a developer's or expert's perspective on the quality of a response. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Adding an Annotation via the UI

To add a developer annotation:

1.  Navigate to your [MLflow Experiment](/concepts/mlflow-experiment.md) in the MLflow UI.
2.  Open the **Logs** tab to view your traces.
3.  Click on a trace to open the trace details dialog.
4.  Select a span (for trace-level feedback, you can select the root span).
5.  In the **Assessments** panel on the right, click **Add new assessment**.
6.  Fill in the following fields in the assessment form:
    *   **Type**: `Feedback`. (This indicates you are providing developer feedback.)
    *   **Name**: A descriptive name, such as `accuracy_score`.
    *   **Value**: A numerical or categorical value, such as `.75`.
    *   **Rationale**: A text explanation providing context for the assessment, such as why the response was scored a certain way.
7.  Click **Create**.

After creation, the new assessment appears in the **Assessments** section of the trace details. Upon refreshing the page, columns for the newly created assessments become visible in the **Logs** table. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Purpose and Use

Developers use annotations to evaluate the quality of a [GenAI](/concepts/mlflow-genai-evaluate-api.md) application's output during the development and testing phase. This is particularly useful for:

- Identifying gaps in a model's response, such as missing key features or context.
- Providing a quantitative score (e.g., `.75` out of `1.0`) for a specific quality metric.
- Recording the rationale for a score to guide future improvements or to provide context for expert reviewers. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Relationship to Other Feedback Types

Developer annotations are one of three primary feedback collection methods within the MLflow human feedback system:

1.  **End-user feedback**: Collected programmatically via `mlflow.log_feedback()` from the application, simulating a user action (e.g., a thumbs-up/down). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
2.  **Developer annotations**: Added manually via the MLflow UI as described above. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
3.  **Expert review**: Collected by creating a [Labeling Session](/concepts/labeling-session.md) for structured expert review, which can then be used to evaluate the app with scorers like `Correctness`. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The mechanism that captures and records traces for GenAI applications.
- [Assessment](/concepts/assessments.md) – The generic object type for storing feedback and annotations.
- [MLflow UI](/concepts/mlflow.md) – The web interface for viewing and managing MLflow experiments, runs, and traces.
- [Human Feedback System](/concepts/human-feedback-collection-in-mlflow.md) – The overarching framework for collecting and using human input.
- [Labeling Session](/concepts/labeling-session.md) – A structured review workflow for expert feedback.
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The process of evaluating app quality using collected annotations and expert expectations.

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
