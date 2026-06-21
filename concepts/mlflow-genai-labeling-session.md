---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e8ee3e88f9666d1de29f5099cba11a4b7f18d662215383045e7a20e12933920f
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-labeling-session
    - MGLS
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: MLflow GenAI Labeling Session
description: An organized queue of traces prepared for human review by domain experts, using labeling schemas to structure the assessments collected.
tags:
  - mlflow
  - human-feedback
  - labeling
timestamp: "2026-06-18T11:05:45.292Z"
---

# MLflow GenAI Labeling Session

A **labeling session** is an MLflow GenAI data model entity that organizes traces for human review by domain experts. Labeling sessions queue selected traces that need expert evaluation and contain the assessments resulting from that review. They use [Labeling Schemas](/concepts/labeling-schemas.md) to structure the assessments that experts are asked to provide. ^[concepts-data-model-databricks-on-aws.md]

## Purpose

Labeling sessions serve two primary purposes in the MLflow GenAI evaluation workflow:

- **Collect expert feedback** on complex or ambiguous cases that automated scorers cannot reliably evaluate. ^[concepts-data-model-databricks-on-aws.md]
- **Create ground truth data** for evaluation datasets, enabling systematic quality measurement using expert-labeled expectations. ^[concepts-data-model-databricks-on-aws.md]

## Relationship to Other Entities

Labeling sessions are part of the human labeling data category within the MLflow data model. They sit alongside [Traces](/concepts/traces.md), [Assessments](/concepts/assessments.md), [Evaluation Datasets](/concepts/evaluation-datasets.md), [Evaluation Runs](/concepts/evaluation-runs.md), [prompts](/concepts/prompt-versioning.md), and [Logged Models](/concepts/logged-models.md) within an [experiment](/concepts/mlflow-experiment.md). While traces capture application execution logs and assessments capture quality measurements, labeling sessions specifically manage the workflow of sending those traces to human reviewers and collecting their structured feedback. ^[concepts-data-model-databricks-on-aws.md]

## Labeling Schemas

Each labeling session uses a [Labeling Schema](/concepts/labeling-schema.md) to define what questions reviewers are asked and what valid responses are accepted. A schema might include yes/no questions, 1–5 rating scales, thumbs up/down judgments, or free-text comments. Using a schema ensures consistent label collection across multiple domain experts reviewing the same session. ^[concepts-data-model-databricks-on-aws.md]

## Review App

The primary user interface for interacting with labeling sessions is the [Review App](/concepts/mlflow-review-app.md), a web UI where domain experts label traces with assessments. The review app presents traces from labeling sessions and collects assessments based on the associated labeling schemas. ^[concepts-data-model-databricks-on-aws.md]

## Workflow Examples

### Label Existing Traces

Domain experts can use labeling sessions to review production or development traces, providing assessments that are attached back to the source traces. This workflow is documented in the guide to [collect domain expert feedback](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/expert-feedback/label-existing-traces). ^[concepts-data-model-databricks-on-aws.md]

### Label During Development

Labeling sessions also support collecting assessments during the development phase, allowing developers to annotate traces as they build and iterate on their application. This is documented in the guide on [logging assessments during development](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations). ^[concepts-data-model-databricks-on-aws.md]

## Related Concepts

- [Experiment](/concepts/mlflow-experiment.md) — The container for a single application's data, including all labeling sessions
- [Trace](/concepts/traces.md) — The app execution log that gets queued for review in a labeling session
- [Assessment](/concepts/assessments.md) — Quality measurements and ground truth labels attached to traces as a result of labeling
- [Labeling Schema](/concepts/labeling-schema.md) — Defines the structured questions and valid responses for a labeling session
- [Feedback](/concepts/feedback-object.md) — A type of assessment representing judgments about the quality of outputs
- Expectations — A type of assessment representing ground truth labels
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — Curated test cases that can be created from labeled traces
- [Review App](/concepts/mlflow-review-app.md) — Web UI for domain experts to complete labeling sessions

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
