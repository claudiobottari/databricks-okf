---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9df5337091344a0d9be8fe8de4896f9dd38a1cd729f512cfe1c708387e6b8ca
  pageDirectory: concepts
  sources:
    - label-during-development-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-ui-label-column
    - MTULC
  citations:
    - file: label-during-development-databricks-on-aws.md
title: MLflow Trace UI Label Column
description: Labels added to traces through the MLflow Experiment UI appear as new columns in the Traces tab, enabling trace-level filtering and organization by annotation value.
tags:
  - mlflow
  - ui
  - traces
timestamp: "2026-06-19T19:12:03.178Z"
---

# MLflow Trace UI Label Column

**MLflow Trace UI Label Column** refers to a column that appears in the Traces tab of the MLflow Experiment UI after a user adds an assessment label to a trace. This column displays the feedback or expectation values that were assigned to individual traces, making them visible alongside other trace metadata in the experiment view.

## Overview

When you add an assessment label to a trace through the MLflow Trace UI, the label is automatically surfaced as a new column in the Traces tab of the MLflow Experiment UI. This allows you to quickly view and compare labeled traces without needing to open each trace individually. ^[label-during-development-databricks-on-aws.md]

## How Labels Appear as Columns

The label column is created automatically when you save an assessment on a trace. The column name corresponds to the **Assessment Name** you provided when creating the label, and the values in the column reflect the **Value** you assigned. ^[label-during-development-databricks-on-aws.md]

For example, if you create an assessment named "Quality Score" with a numeric value, a column titled "Quality Score" appears in the Traces tab, and the trace you labeled shows the numeric score in that column.

## Adding Labels That Create Columns

To create a label column in the Trace UI:

1. Navigate to the **Traces tab** in the MLflow Experiment UI.
2. Open an individual trace.
3. Click the specific span you want to label (selecting the root span attaches feedback to the entire trace).
4. Expand the **Assessments** tab at the far right.
5. Fill in the form with the following fields:
   - **Assessment Type**: Choose either *Feedback* (subjective quality assessment) or *Expectation* (expected output or value)
   - **Assessment Name**: A unique name for what the feedback is about (this becomes the column name)
   - **Data Type**: Number, Boolean, or String
   - **Value**: Your assessment value
   - **Rationale**: Optional notes about the value
6. Click **Create** to save your label.
7. When you return to the Traces tab, your label appears as a new column.

^[label-during-development-databricks-on-aws.md]

## Data Types for Column Values

The label column can contain values of the following data types, which you specify when creating the assessment:

- **Number**: Numeric ratings or scores (e.g., 4.5, 85)
- **Boolean**: True/False assessments (e.g., correct/incorrect)
- **String**: Text feedback or categorical labels (e.g., "good", "needs improvement")

^[label-during-development-databricks-on-aws.md]

## Use Cases

The Label Column feature supports several development workflows:

- **Quality tracking**: Add numeric ratings to traces and see all ratings in a single column for comparison
- **Flagging issues**: Use Boolean labels to mark traces that contain errors or unexpected behavior
- **Categorizing traces**: Assign string labels to group traces by type, severity, or topic
- **Recording ground truth**: Set expectation labels to document what the correct output should be

^[label-during-development-databricks-on-aws.md]

## Availability

This feature is available in the MLflow Trace UI, which can be accessed both from the MLflow Experiment UI in your web browser and inline within a Databricks notebook. The inline version provides the same labeling functionality directly in your notebook environment. ^[label-during-development-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The system that captures and stores trace data for GenAI applications
- [MLflow Experiment UI](/concepts/mlflow-experiment.md) — The interface where trace labels appear as columns
- Assessment Labels — The structured feedback objects that populate the label columns
- [Labeling Schemas](/concepts/labeling-schemas.md) — Definitions for structured feedback collection
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — The broader workflow for incorporating human assessments into MLflow

## Sources

- label-during-development-databricks-on-aws.md

# Citations

1. [label-during-development-databricks-on-aws.md](/references/label-during-development-databricks-on-aws-8241bcbb.md)
