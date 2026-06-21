---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04a0ec4a3d4f528c068bb78d3c0360a2c3a361db5e7ddd64e3c949f6154e091e
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - genai-app-evaluation-workflow-on-databricks
    - GAEWOD
    - GenAI Evaluation on Databricks
    - GenAI applications on Databricks
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: GenAI App Evaluation Workflow on Databricks
description: "End-to-end workflow pattern: instrument a GenAI app with tracing, collect end-user feedback, add developer annotations, conduct expert review via labeling sessions, and evaluate with scorers."
tags:
  - databricks
  - workflow
  - evaluation
  - genai
timestamp: "2026-06-19T08:46:25.473Z"
---

Here is the wiki page for "GenAI App Evaluation Workflow on Databricks".

---

## GenAI App Evaluation Workflow on Databricks

**GenAI App Evaluation Workflow on Databricks** is a structured approach to assessing the quality of generative AI applications by collecting and incorporating human feedback at multiple stages of the development lifecycle. This workflow enables teams to move from simple subjective checks to systematic, expert-validated evaluations.

### Overview

The evaluation workflow on Databricks allows you to instrument a GenAI app, collect feedback from end-users and developers, and then use expert annotations as a ground truth to score your application’s performance against specific quality criteria. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Step 1: Create and Trace a Simple App

The first step is to create a GenAI application using an LLM with [MLflow Tracing](/concepts/mlflow-tracing.md). Tracing captures the full execution path of an app call, including internal steps like context retrieval, making it possible to later associate feedback with specific traces. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Step 2: Collect End-User Feedback

When users interact with your app, you can collect their feedback—such as thumbs up/down—through the SDK. This end-user feedback is logged against the specific trace ID of the interaction, linking the feedback directly to the app’s response. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Step 3: View Feedback in the UI

Feedback appears in the MLflow UI alongside the trace. In the **Logs** tab, you can click on a trace to see the **Assessments** panel, where both end-user feedback and developer annotations are displayed. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Step 4: Add Developer Annotations Using the UI

Developers can add their own feedback directly in the UI by clicking on any span within a trace. This allows for qualitative notes or numerical scores (e.g., an `accuracy_score` of `0.75`) that provide a quick developer perspective on response quality. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Step 5: Send Trace for Expert Review

To get authoritative feedback, you create a **labeling session**. This session defines a schema for the feedback you want to collect (e.g., categorical accuracy ratings like "Accurate", "Partially Accurate", "Inaccurate") and an expected ideal response. Traces are added to the session and shared with expert reviewers via a Review App URL. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Step 6: Use Feedback to Evaluate Your App

After experts provide their ground truth annotations in the labeling session, you can use those labels as inputs to an MLflow scorer—such as the `Correctness` scorer—to evaluate your app. This produces quantitative scores that compare your app’s outputs against the expert-provided expectations. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Labeling Sessions](/concepts/mlflow-labeling-sessions.md)
- [MLflow Scorers](/concepts/mlflow-scorers.md)
- [Human Feedback in GenAI](/concepts/multi-level-human-feedback-in-genai-pipelines.md)
- Build Evaluation Datasets for GenAI

### Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
