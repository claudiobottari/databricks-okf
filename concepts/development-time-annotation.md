---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 508eb19935c0cb37d6151b9b047c6088dfc1b1e75fc1281ee09ce02f839f45c3
  pageDirectory: concepts
  sources:
    - label-during-development-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - development-time-annotation
  citations:
    - file: label-during-development-databricks-on-aws.md
title: Development-time Annotation
description: Adding assessment labels (feedback or expectations) to MLflow traces during GenAI application development, before formal evaluation is set up.
tags:
  - mlflow
  - genai
  - annotation
  - development-workflow
timestamp: "2026-06-19T19:11:32.695Z"
---

# Development-time Annotation

**Development-time Annotation** is the practice of adding structured feedback, expectations, or notes directly to [MLflow traces](/concepts/mlflow-tracing.md) during the application development phase, before setting up formal evaluation pipelines. This allows developers to track quality issues, mark successful examples, and record ground truth while building a GenAI application. ^[label-during-development-databricks-on-aws.md]

## Overview

As you build a GenAI application, [MLflow Tracing](/concepts/mlflow-tracing.md) lets you add feedback or expectations directly to traces. You can record quality issues, mark successful examples, or add notes for future reference. This allows you to track quality during development, before setting up formal evaluation. ^[label-during-development-databricks-on-aws.md]

## Prerequisites

Development-time annotation requires:
- Your application is instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md)
- You have generated traces by running your application

^[label-during-development-databricks-on-aws.md]

## Adding Assessment Labels

Assessments attach structured feedback, scores, or ground truth to traces and spans for quality evaluation and improvement in MLflow. ^[label-during-development-databricks-on-aws.md]

You can add annotations using three interfaces:
- **Databricks UI** (including inline Trace UI in notebooks)
- **MLflow SDK**
- **Databricks REST API**

^[label-during-development-databricks-on-aws.md]

### Via the Databricks UI

1. Navigate to the **Traces** tab in the MLflow Experiment UI.
2. Open an individual trace.
3. Within the trace UI, click the specific span you want to label.
   - Selecting the root span attaches feedback to the entire trace.
4. Expand the **Assessments** tab at the far right.
5. Fill in the form to add your feedback.

^[label-during-development-databricks-on-aws.md]

#### Assessment Fields

- **Assessment Type**
  - *Feedback*: Subjective assessment of quality (ratings, comments)
  - *Expectation*: The expected output or value (what should have been produced)
- **Assessment Name**: A unique name for what the feedback is about
- **Data Type**: Number, Boolean, or String
- **Value**: Your assessment
- **Rationale**: Optional notes about the value

^[label-during-development-databricks-on-aws.md]

### Saving

Click **Create** to save your label. When you return to the Traces tab, your label appears as a new column. ^[label-during-development-databricks-on-aws.md]

## Benefits

Development-time annotation enables early quality tracking during development, before formal evaluation is set up. It helps maintain a record of edge cases, failures, and desired behaviors discovered during iterative development. Labeled traces can later be used to build evaluation datasets for more systematic assessment. ^[label-during-development-databricks-on-aws.md]

## Next Steps

After annotating during development, you can:
- [Collect domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md) — Set up structured labeling sessions
- Build evaluation datasets — Use your labeled traces to create test datasets
- [Collect end-user feedback](/concepts/end-user-feedback-collection-via-sdk.md) — Capture feedback from deployed applications

^[label-during-development-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The instrumentation framework that makes trace annotation possible
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where traces are stored
- [Labeling Schemas](/concepts/labeling-schemas.md) — Structured feedback collection definitions
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — Broader category including development-time, expert, and end-user feedback
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Test datasets built from labeled traces
- GenAI Application Development — The broader development lifecycle

## Sources

- label-during-development-databricks-on-aws.md

# Citations

1. [label-during-development-databricks-on-aws.md](/references/label-during-development-databricks-on-aws-8241bcbb.md)
