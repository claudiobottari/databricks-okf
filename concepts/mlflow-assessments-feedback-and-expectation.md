---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a58a8bc82412e7b4ea7ecf92d61c0d5aa04c463fb470895064ad53f39144695
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-assessments-feedback-and-expectation
    - Expectation) and MLflow Assessments (Feedback
    - MA(AE
    - Collect Feedback and Expectations by Labeling Existing Traces
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: MLflow Assessments (Feedback and Expectation)
description: The human-generated labels captured during a labeling session, stored as Assessments on MLflow Traces; can be either Feedback or Expectation data and later synced to evaluation datasets.
tags:
  - mlflow
  - assessments
  - feedback
  - expectations
timestamp: "2026-06-18T11:19:03.819Z"
---

# MLflow Assessments (Feedback and Expectation)

**MLflow Assessments** are structured human-generated evaluations captured on [[MLflow Trace|MLflow Traces]] during labeling sessions. Assessments enable domain experts to provide qualitative feedback and define expected behavior for GenAI applications, which can then be used to improve application quality through systematic evaluation. Assessments are stored in two forms: **Feedback** and **Expectation**.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

Assessments are collected through [Labeling Sessions](/concepts/labeling-sessions.md), which are special types of MLflow runs that contain a specific set of traces for domain experts to review using the [MLflow Review App](/concepts/mlflow-review-app.md). When reviewers complete their evaluations, MLflow stores their responses as Assessments on the traces in the session. These assessments can be retrieved through the MLflow UI or the MLflow API.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Types of Assessments

### Feedback

Feedback assessments capture qualitative evaluations from domain experts about the behavior of a GenAI application. Feedback is unstructured or semi-structured input that reflects the reviewer's subjective judgment on aspects such as response quality, helpfulness, or correctness. Feedback assessments are defined using labeling schemas with the type set to `"feedback"`.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Expectation

Expectation assessments capture structured, ground-truth information about what the correct or expected output should be for a given input. Expectations serve as reference standards that can be used for automated evaluation. They are collected through labeling schemas such as `EXPECTED_FACTS` or `EXPECTED_RESPONSE`.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

Expectations can be synchronized to [Evaluation Datasets](/concepts/evaluation-datasets.md) using the `sync()` method, which performs an intelligent upsert operation. This allows teams to iteratively improve their evaluation datasets by adding new examples and updating ground truth for existing examples.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Collecting Assessments

Assessments are collected during labeling sessions where domain experts review traces. The process involves:

1. **Creating a labeling session** with assigned users and labeling schemas that define the questions and format for feedback collection.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
2. **Adding traces to the session** — either from UI selections or programmatically using the `add_traces()` API.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
3. **Reviewers provide assessments** through the Review App interface, with responses stored on the traces.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Labeling Schemas

Labeling schemas define the structure of assessments. Built-in schemas include:

| Schema | Type | Purpose |
|--------|------|---------|
| `EXPECTED_FACTS` | Expectation | Capture factual expectations for outputs |
| `EXPECTED_RESPONSE` | Expectation | Define expected response content |
| `GUIDELINES` | Expectation | Capture guideline-based expectations |

Custom schemas can also be created using `mlflow.genai.label_schemas.create_label_schema()` with either `"feedback"` or `"expectation"` types and structured input formats such as categorical options.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Retrieving Assessments

After reviewers complete a labeling session, assessments can be retrieved:

### In the UI

Open the **Experiments** UI, click the labeling session, then click a specific request. Click **Assessments** at the upper right to view each reviewer's responses.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### With the MLflow API

Because labeling sessions are logged as MLflow runs, assessments can be accessed using `mlflow.search_runs()`. The trace data and associated assessments are retrievable through standard MLflow APIs.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Synchronizing Expectations to Evaluation Datasets

The `sync()` method on a labeling session enables transferring collected Expectations to evaluation datasets. The synchronization process:

- Uses each trace's inputs as a unique key to identify records in the dataset.
- Overwrites existing expectations when expectation names match and trace inputs match.
- Adds traces from the labeling session as new records when they do not match existing trace inputs.
- Leaves existing dataset records with different inputs unchanged.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

This approach supports iterative improvement of evaluation datasets by continuously adding new examples and updating ground truth for existing examples based on expert feedback.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Use descriptive, date-stamped session names** such as `customer_service_review_march_2024` for clear organization.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Keep focused sessions** with 25-100 traces per session to avoid reviewer fatigue.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Store the session [MLflow Run](/concepts/mlflow-run.md) ID** for programmatic access instead of relying on session names, which may not be unique.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Use Expectations for automated evaluation pipelines** by syncing them to evaluation datasets for systematic quality measurement.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — The container for traces and their associated assessments
- [Labeling Schemas](/concepts/labeling-schemas.md) — The question and format definitions for feedback collection
- [[MLflow Trace|MLflow Traces]] — The execution traces that assessments are attached to
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Structured datasets that can incorporate Expectation assessments
- Human Feedback Alignment — Using expert assessments to improve judge accuracy
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying quality monitoring based on assessment criteria

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
