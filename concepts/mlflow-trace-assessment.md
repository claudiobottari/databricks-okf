---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c9afd887d9d1bd8c81ff06647903432ed56c2e870070a9a1179f19cceaa0cec6
  pageDirectory: concepts
  sources:
    - label-during-development-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-assessment
    - MTA
    - MLflow Assessment
  citations:
    - file: label-during-development-databricks-on-aws.md
title: MLflow Trace Assessment
description: Structured feedback, scores, or ground truth attached to traces and spans for quality evaluation in MLflow, with configurable type, name, data type, value, and rationale.
tags:
  - mlflow
  - evaluation
  - feedback
timestamp: "2026-06-19T19:11:33.560Z"
---

# MLflow Trace Assessment

**MLflow Trace Assessment** is the practice of adding structured feedback, scores, or ground truth directly to [traces](/concepts/mlflow-tracing.md) and spans during development. This allows developers to record quality issues, mark successful examples, or attach notes for future reference before setting up formal evaluation pipelines. ^[label-during-development-databricks-on-aws.md]

## Overview

When building a GenAI application instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md), you can attach assessment labels to individual traces or spans. These labels serve as a lightweight way to track quality during development, enabling you to capture subjective ratings, expected outputs, or other metadata alongside the trace data. Assessments become visible as columns in the Traces tab of the MLflow Experiment UI, making it easy to browse and filter by quality criteria. ^[label-during-development-databricks-on-aws.md]

## Assessment Types

MLflow supports two types of assessments:

| Assessment Type | Description |
|----------------|-------------|
| **Feedback** | A subjective assessment of quality, such as ratings or comments. |
| **Expectation** | The expected output or value — what should have been produced by the application. |

^[label-during-development-databricks-on-aws.md]

Each assessment also requires:
- **Assessment Name**: A unique label describing what the feedback is about.
- **Data Type**: `Number`, `Boolean`, or `String`.
- **Value**: The actual assessment value (e.g., a rating of 5, true/false, or a textual note).
- **Rationale** (optional): Supplementary notes explaining the value.

^[label-during-development-databricks-on-aws.md]

## Adding Assessments

Assessments can be added through the Databricks UI, the MLflow SDK, or the Databricks REST API. ^[label-during-development-databricks-on-aws.md]

### Using the UI

1. Navigate to the **Traces** tab in the MLflow Experiment UI.
2. Open an individual trace.
3. Click the specific span you want to label. Selecting the root span attaches feedback to the entire trace.
4. Expand the **Assessments** panel on the far right.
5. Fill in the form with the assessment type, name, data type, value, and optional rationale.
6. Click **Create** to save the label.

After saving, the assessment appears as a new column in the Traces tab. ^[label-during-development-databricks-on-aws.md]

### Using the SDK or REST API

Refer to the MLflow SDK documentation or Databricks REST API references for programmatic approaches to adding assessments. ^[label-during-development-databricks-on-aws.md]

### Prerequisites

- Your application must be instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md).
- You must have generated traces by running your application. ^[label-during-development-databricks-on-aws.md]

## Next Steps

Labeled traces can be used in several downstream workflows:

- [Collect domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md) – Set up structured labeling sessions with domain experts.
- Build evaluation datasets – Use your labeled traces to create test datasets for formal evaluation.
- [Collect end-user feedback](/concepts/end-user-feedback-collection-via-sdk.md) – Capture feedback from deployed applications via the tracing system.

^[label-during-development-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md)
- [Evaluation Datasets](/concepts/evaluation-datasets.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Labeling Schemas](/concepts/labeling-schemas.md)

## Sources

- label-during-development-databricks-on-aws.md

# Citations

1. [label-during-development-databricks-on-aws.md](/references/label-during-development-databricks-on-aws-8241bcbb.md)
