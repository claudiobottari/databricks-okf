---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e57d3f6b0caaf6c2e56351c157df3031a70c421e03d4baadcce4f7b3c1709c6e
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-sessions-and-schemas-mlflow-genai
    - Schemas (MLflow GenAI) and Labeling Sessions
    - LSAS(G
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: Labeling Sessions and Schemas (MLflow GenAI)
description: Infrastructure for collecting domain expert feedback, where sessions queue traces for review and schemas define structured questions for consistent labeling.
tags:
  - mlflow
  - human-feedback
  - labeling
timestamp: "2026-06-18T14:41:40.807Z"
---

# Labeling Sessions and Schemas (MLflow GenAI)

**Labeling Sessions and Schemas** are the two core entities in the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) human labeling data model that enable structured collection of expert feedback and ground truth labels on [Traces](/concepts/traces.md).

## Overview

Labeling sessions and labeling schemas work together to organize and standardize the collection of [Assessments](/concepts/assessments.md) from domain experts. Labeling sessions queue selected traces for human review, while labeling schemas define the structure of the assessments that experts will provide. Together, they ensure consistent, high-quality feedback across multiple reviewers. ^[concepts-data-model-databricks-on-aws.md]

## Labeling Sessions

[Labeling sessions](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/concepts/labeling-sessions) organize traces for human review by domain experts. They:

- Queue selected traces that need expert review and contain the assessments from that review.
- Use labeling schemas to structure the assessments for experts to label. ^[concepts-data-model-databricks-on-aws.md]

Labeling sessions serve two main purposes:

- **Collect expert feedback** on complex or ambiguous cases that automated [[scorers]] may handle poorly.
- **Create ground truth data** for [Evaluation Datasets](/concepts/evaluation-datasets.md), enabling more accurate quality assessment in future development. ^[concepts-data-model-databricks-on-aws.md]

## Labeling Schemas

[Labeling schemas](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/concepts/labeling-schemas) define the assessments that are collected in a labeling session, ensuring consistent label collection across domain experts. They:

- Specify what questions to ask reviewers (for example, "Is this response accurate?").
- Define the valid responses to a question (for example, thumbs up/down, 1-5 scales, or free text comments). ^[concepts-data-model-databricks-on-aws.md]

By standardizing the structure of assessments, labeling schemas prevent subjective drift between different reviewers and make the collected feedback directly comparable for analysis.

## Relationship to Other Data Model Entities

Labeling sessions and schemas exist within the broader MLflow GenAI data model under experiments. They complement other quality-related entities:

- **[Traces](/concepts/traces.md)**: The app execution logs that labeling sessions queue for review.
- **[Assessments](/concepts/assessments.md)**: The quality measurements that result from labeling, including both feedback (judgments) and expectations (ground truth).
- **[Evaluation Datasets](/concepts/evaluation-datasets.md)**: Curated test cases that can be enriched with ground truth from labeling sessions.

## Using Labeling Sessions and Schemas

The primary interface for domain experts to interact with labeling sessions is the **review app**, a web UI where experts label traces with assessments. The review app presents traces from labeling sessions and collects assessments based on the configured labeling schemas. ^[concepts-data-model-databricks-on-aws.md]

Practitioners can:

- Follow the guide to [collect domain expert feedback](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/expert-feedback/label-existing-traces) by creating labeling sessions from existing traces.
- Use [labeling during development](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations) to annotate traces as they are created.

## Related Concepts

- Concepts & Data Model (MLflow GenAI) — The full data model that includes labeling sessions and schemas
- [Assessments](/concepts/assessments.md) — The feedback and expectations collected through labeling
- [[Scorers]] — Automated assessment functions that complement human labeling
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Curated test cases that can incorporate ground truth from labeling
- [Review App](/concepts/mlflow-review-app.md) — Web UI for domain expert labeling

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
