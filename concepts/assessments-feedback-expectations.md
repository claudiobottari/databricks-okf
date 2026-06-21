---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c3f5868f8231c971ef40556d89aff909935b57e8e9c8f0d9d0eae7466a102dd
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assessments-feedback-expectations
    - A(&E
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Assessments (Feedback & Expectations)
description: The human-generated labels collected through labeling sessions, consisting of either Feedback (opinion-based ratings) or Expectations (ground-truth data) that can drive evaluation and improvement workflows.
tags:
  - labeling
  - feedback
  - evaluation
  - assessments
timestamp: "2026-06-19T14:33:30.921Z"
---

# Assessments (Feedback & Expectations)

**Assessments (Feedback & Expectations)** refer to the human-generated labels collected during [Labeling Sessions](/concepts/labeling-sessions.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md). These assessments capture domain‑expert evaluations of [[MLflow Trace|MLflow Traces]] and are used to systematically improve GenAI applications through evaluation and fine‑tuning. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

The goal of a labeling session is to collect human-generated assessments on existing MLflow traces. Each assessment is stored as structured data on the trace and can be either **Feedback** or **Expectation** data. Assessments can be retrieved programmatically or viewed in the MLflow UI, and expectations can be synchronized to evaluation datasets for iterative improvement. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Types of Assessments

### Feedback

Feedback assessments capture subjective ratings or qualitative judgments from reviewers. They are defined through **labeling schemas** of type `feedback`. For example, a feedback schema might ask a reviewer to rate response quality on a categorical scale (Poor, Fair, Good, Excellent) or to provide a numerical score. The responses are stored as feedback on the trace. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Expectations

Expectations capture ground‑truth information that the agent’s output should satisfy. Built‑in schema types include `EXPECTED_FACTS`, `EXPECTED_RESPONSE`, and `GUIDELINES`. When a labeling session collects expectations, these can later be synced to an [Evaluation Dataset](/concepts/evaluation-dataset.md), where they serve as the target against which agent outputs are compared. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Collection via Labeling Sessions

Assessments are collected within a labeling session, a special type of [MLflow Run](/concepts/mlflow-run.md) that contains a curated set of traces. The workflow is:

1. **Create a labeling session** – Define a name, assigned users, and one or more labeling schemas (built‑in or custom). For example, a session might use the `EXPECTED_FACTS` schema to collect factual expectations. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

2. **Add traces to the session** – Select traces from your experiment (via the UI or the `add_traces()` API) that you want reviewers to evaluate. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

3. **Reviewers label the traces** – Assigned domain experts use the [Review App](/concepts/mlflow-review-app.md) to examine each trace and provide feedback or expectations according to the specified schemas. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

4. **Retrieve assessments** – After labeling completes, MLflow stores the responses as `Assessments` on the traces. You can view them in the UI (click **Assessments** in the session view) or use the MLflow API to retrieve them programmatically. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Using Assessments in Evaluation

### Syncing Expectations to Evaluation Datasets

Expectations collected during labeling can be synchronized to an evaluation dataset using the `sync()` method on a labeling session. This performs an intelligent upsert: each trace’s inputs act as a unique key; matching expectations are overwritten, new traces are added, and unrelated records remain unchanged. This allows teams to iteratively improve their evaluation datasets with ground‑truth annotations. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Systematic Evaluation

Both feedback and expectation assessments feed into the broader evaluation workflow. Feedback scores can be used to compute quality metrics, while expectations serve as the basis for automated judge‑based scoring. This combination helps developers identify regressions and validate improvements before deploying agent changes. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Session organization** – Use descriptive, date‑stamped names (e.g., `customer_service_review_march_2024`) and keep sessions focused on a single evaluation goal. Aim for 25‑100 traces per session to avoid reviewer fatigue. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **User management** – Assign reviewers based on domain expertise. All Databricks workspace users can be assigned; the system grants necessary `WRITE` permissions on the experiment automatically. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Iterative improvement** – Regularly sync expectations to your evaluation datasets to keep ground truth up to date as the application evolves. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) – The container for collecting assessments.
- [[MLflow Trace|MLflow Traces]] – The execution records being assessed.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Datasets that absorb expectations for automated testing.
- [Labeling Schemas](/concepts/labeling-schemas.md) – Templates that define the questions and format for assessments.
- [Review App](/concepts/mlflow-review-app.md) – The UI used by domain experts to provide assessments.
- Human Feedback Alignment – Aligning automated judges with human preferences using these assessments.
- GenAI Agent Evaluation – The broader evaluation pipeline that consumes assessments.

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
