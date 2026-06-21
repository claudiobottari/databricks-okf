---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12a7302847cde8e60b4a3671fa5068ebd0398e9223a046ae9e456d8f36d0358c
  pageDirectory: concepts
  sources:
    - label-during-development-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - span-level-labeling-in-mlflow
    - SLIM
  citations:
    - file: label-during-development-databricks-on-aws.md
title: Span-level Labeling in MLflow
description: The ability to attach assessments to individual spans within a trace, with the root span representing the entire trace, enabling granular feedback on specific components.
tags:
  - mlflow
  - tracing
  - spans
timestamp: "2026-06-19T19:11:39.132Z"
---

---
title: Span-level Labeling in MLflow
summary: Adding structured assessment labels to individual spans within an MLflow trace for quality evaluation during development.
sources:
  - label-during-development-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T20:00:00.000Z"
updatedAt: "2026-06-19T20:00:00.000Z"
tags:
  - mlflow
  - tracing
  - labeling
  - evaluation
aliases:
  - span-level-labeling-in-mlflow
  - span-labeling
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Span-level Labeling in MLflow

**Span-level Labeling** is the practice of attaching structured assessment labels to individual Span|spans within an [[MLflow Trace]]. This allows developers to record quality feedback, mark successful examples, or add expectations directly at the level of a specific operation in a generative AI application, before setting up formal evaluation pipelines. ^[label-during-development-databricks-on-aws.md]

## Overview

When your application is instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md), you can use the MLflow UI or SDK to add annotations (labels) to traces and spans. Selecting a specific span attaches feedback to that span, while selecting the root span attaches feedback to the entire trace. This granularity helps pinpoint which component of a multi-step pipeline produced an unexpected result. ^[label-during-development-databricks-on-aws.md]

## Labeling in the UI

To label a span through the Databricks UI:

1. Navigate to the **Traces** tab in the MLflow Experiment UI.
2. Open an individual trace.
3. Click the specific span you want to label.
4. Expand the **Assessments** tab at the far right.
5. Fill in the form:

   | Field | Description |
   |---|---|
   | **Assessment Type** | *Feedback* (subjective quality rating) or *Expectation* (expected output or value) |
   | **Assessment Name** | A unique name for the feedback category |
   | **Data Type** | Number, Boolean, or String |
   | **Value** | The assessment value |
   | **Rationale** | Optional notes about the value |

6. Click **Create** to save the label.

After saving, the label appears as a new column in the Traces tab. ^[label-during-development-databricks-on-aws.md]

If you are using a Databricks notebook, the Trace UI renders inline and supports the same labeling workflow. ^[label-during-development-databricks-on-aws.md]

## Assessment Types

- **Feedback** – Used for subjective quality assessments, such as ratings or comments. ^[label-during-development-databricks-on-aws.md]
- **Expectation** – Used to record the expected output or value that should have been produced, enabling ground-truth comparison. ^[label-during-development-databricks-on-aws.md]

## Next Steps

After labeling spans, you can:

- [Collect domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md) using structured labeling sessions.
- Build evaluation datasets from labeled traces.
- [Collect end-user feedback](/concepts/end-user-feedback-collection-via-sdk.md) from deployed applications.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Observability framework for generative AI applications.
- [Trace](/concepts/traces.md) – A record of a single request through an application.
- Span – A single unit of work within a trace.
- [Assessment](/concepts/assessments.md) – The structured label attached to a trace or span.
- [Labeling Schemas](/concepts/labeling-schemas.md) – Formal definitions for structured feedback collection.

## Sources

- label-during-development-databricks-on-aws.md

# Citations

1. [label-during-development-databricks-on-aws.md](/references/label-during-development-databricks-on-aws-8241bcbb.md)
