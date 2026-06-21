---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 628ba7b4ae0189bc32d3b00e93d80f95c4213f3e80582d47d79d46c905fc5ba0
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-sessions-and-schemas
    - Schemas and Labeling Sessions
    - LSAS
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: Labeling Sessions and Schemas
description: Labeling sessions queue traces for human expert review, while labeling schemas define structured questions and valid responses to ensure consistent assessment collection across domain experts.
tags:
  - mlflow
  - human-feedback
  - labeling
timestamp: "2026-06-19T14:22:27.021Z"
---

# Labeling Sessions and Schemas

**Labeling Sessions** and **Labeling Schemas** are two closely related entities in the MLflow data model that support systematic human review of GenAI application traces. Labeling sessions organize traces for domain expert review, while labeling schemas define the structure of the assessments that experts collect during that review. ^[concepts-data-model-databricks-on-aws.md]

## Overview

When developing and monitoring GenAI applications, automated evaluation with [[scorers]] and [LLM Judges](/concepts/llm-judges.md) provides broad coverage, but certain cases benefit from human judgment. Labeling sessions and schemas enable this by queuing selected [Traces](/concepts/traces.md) for expert review and ensuring consistent, structured feedback collection across multiple reviewers. ^[concepts-data-model-databricks-on-aws.md]

## Labeling Sessions

**Labeling sessions** are containers within an [MLflow Experiment](/concepts/mlflow-experiment.md) that organize selected traces for human review by domain experts. ^[concepts-data-model-databricks-on-aws.md]

### Key Characteristics

- Labeling sessions queue traces that need expert review and contain the assessments produced from that review. ^[concepts-data-model-databricks-on-aws.md]
- Each labeling session uses a [Labeling Schema](/concepts/labeling-schema.md) to structure the assessments that experts collect. ^[concepts-data-model-databricks-on-aws.md]

### Use Cases

Labeling sessions are used for two primary purposes:

1. **Collecting expert feedback** on complex or ambiguous cases that automated scorers cannot reliably evaluate. ^[concepts-data-model-databricks-on-aws.md]
2. **Creating ground truth data** for [Evaluation Datasets](/concepts/evaluation-datasets.md), enabling more rigorous quality assessment in future development cycles. ^[concepts-data-model-databricks-on-aws.md]

### Workflow

Domain experts interact with labeling sessions through the [Review App](/concepts/mlflow-review-app.md), a web UI that presents traces from the session and collects assessments based on the session's labeling schema. ^[concepts-data-model-databricks-on-aws.md]

## Labeling Schemas

**Labeling schemas** define the assessments that are collected within a labeling session, ensuring consistent label collection across domain experts. ^[concepts-data-model-databricks-on-aws.md]

### Key Characteristics

- Labeling schemas specify what questions to ask reviewers — for example, "Is this response accurate?" ^[concepts-data-model-databricks-on-aws.md]
- They define the valid responses to each question, such as thumbs up/down ratings, 1–5 scales, or free text comments. ^[concepts-data-model-databricks-on-aws.md]

### Purpose

By enforcing a consistent structure, labeling schemas ensure that assessments collected from multiple reviewers are comparable and can be reliably aggregated. This is essential both for obtaining high-quality feedback and for building ground truth datasets. ^[concepts-data-model-databricks-on-aws.md]

## Relationship to Assessments

Both labeling sessions and schemas are part of the [Assessments](/concepts/assessments.md) system in MLflow. While automated [[scorers]] and [LLM Judges](/concepts/llm-judges.md) produce feedback assessments programmatically, labeling sessions capture assessments from human reviewers. The assessments generated through labeling sessions can include both:

- **Feedback** — judgments about the quality of the app's outputs (for example, a domain expert's rating of response accuracy).
- **Expectations** — ground truth labels that define the correct output for a given input (for example, the expected response to a question). ^[concepts-data-model-databricks-on-aws.md]

## Related Concepts

- [Traces](/concepts/traces.md) — The app execution records that labeling sessions queue for review.
- [Assessments](/concepts/assessments.md) — Quality measurements and ground truth labels, including those collected through labeling sessions.
- [Review App](/concepts/mlflow-review-app.md) — The web UI where domain experts label traces using labeling schemas.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Curated test cases that can be enriched with ground truth from labeling sessions.
- [[Scorers]] — Automated functions that also produce assessments, complementing human review.
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The parent container that holds all labeling sessions and schemas for an application.

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
