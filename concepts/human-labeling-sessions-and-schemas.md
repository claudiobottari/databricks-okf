---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 451edbf8b7c33b51ea8f99f73008f06fec3c983638f6c664cfb178dcc46120bd
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - human-labeling-sessions-and-schemas
    - "Schemas and Human Labeling: Sessions"
    - HLSAS
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: "Human Labeling: Sessions and Schemas"
description: Labeling sessions organize traces for domain expert review, while labeling schemas define the structured questions and response types (ratings, free text) for consistent label collection.
tags:
  - mlflow
  - human-feedback
  - labeling
  - domain-experts
timestamp: "2026-06-19T17:49:34.003Z"
---

# Human Labeling: Sessions and Schemas

## Overview

Within MLflow for GenAI, **human labeling** is a component of the data model that supports the collection of expert feedback and ground-truth data. It is organized through two interrelated concepts: **labeling sessions** and **labeling schemas**. These structures allow domain experts to review traces and produce consistent assessments that can be used to improve application quality. ^[concepts-data-model-databricks-on-aws.md]

## Labeling Sessions

A **labeling session** is a queue of [Traces](/concepts/traces.md) that have been selected for human review by domain experts. Each session contains the traces that need expert inspection along with the [Assessments](/concepts/assessments.md) that result from that review. ^[concepts-data-model-databricks-on-aws.md]

Labeling sessions serve two main purposes:  
- Collecting expert feedback on complex or ambiguous cases.  
- Creating ground truth data (expectations) that can be used to build [Evaluation Datasets](/concepts/evaluation-datasets.md).  

To structure the assessments collected during a session, the session uses a **labeling schema**. ^[concepts-data-model-databricks-on-aws.md]

Domain experts interact with labeling sessions through the [review app](/concepts/mlflow-review-app.md), a web UI that presents traces and captures assessments based on the schema defined for the session. ^[concepts-data-model-databricks-on-aws.md]

## Labeling Schemas

A **labeling schema** defines the set of assessments that are collected within a labeling session. It ensures that every domain expert reviews traces using the same criteria, producing consistent, comparable labels. ^[concepts-data-model-databricks-on-aws.md]

A schema specifies:
- **What questions to ask** the reviewer — for example, “Is this response accurate?”
- **The valid response types** — such as thumbs‑up/thumbs‑down, 1–5 scales, or free‑text comments. ^[concepts-data-model-databricks-on-aws.md]

By standardizing the format of assessments, labeling schemas make it possible to aggregate expert feedback reliably across multiple reviewers and over time. ^[concepts-data-model-databricks-on-aws.md]

## Relationship Between Sessions and Schemas

Sessions and schemas work together as part of the human labeling workflow: a session **uses** a schema to define the labeling task, and the schema is applied to every trace within that session. This coupling guarantees that all assessments produced from a given session follow an identical structure, facilitating later analysis and use in evaluation. ^[concepts-data-model-databricks-on-aws.md]

## Related Concepts

- [Assessments](/concepts/assessments.md) – The quality measurements (feedback or expectations) produced by human labelers.
- [Traces](/concepts/traces.md) – Execution logs that are queued in labeling sessions for review.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Ground truth datasets that can be built from the expectations collected during labeling.
- Review app – The web UI where domain experts label traces according to the session’s schema.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The container that holds all labeling data for a given GenAI application.

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
