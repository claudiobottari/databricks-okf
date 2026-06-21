---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6964982e97f6d3d5c8ca30c4261d9134a4bc7dc4dabb29b0c4f07474abf1b489
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - assessments-feedback-vs-expectation
    - AFVE
    - assessment-data-feedback-vs-expectation
    - AD(VE
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: "Assessments: Feedback vs Expectation"
description: "The two types of human-generated labels that can be captured in labeling sessions: Feedback (subjective evaluation) and Expectation (ground-truth reference data)."
tags:
  - mlflow
  - labeling
  - assessments
  - human-feedback
timestamp: "2026-06-19T17:59:04.941Z"
---

# Assessments: Feedback vs Expectation

**Assessments** are human-generated labels collected through [Labeling Sessions](/concepts/labeling-sessions.md) that capture domain expert evaluations of GenAI application behavior. Within the MLflow Review App, assessments can capture two distinct types of data: **Feedback** and **Expectation**. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

When domain experts review traces in a labeling session, they provide assessments that MLflow stores on the traces. These assessments serve different purposes depending on whether they capture subjective opinions (Feedback) or objective ground truth (Expectation). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Feedback

**Feedback** assessments capture subjective, qualitative evaluations from reviewers. These are typically opinion-based ratings or judgments about the quality, appropriateness, or helpfulness of a model's response. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

Feedback is useful for:
- Gathering human preferences on response quality
- Collecting ratings on dimensions like helpfulness, safety, or tone
- Capturing nuanced expert opinions that cannot be reduced to a single correct answer

## Expectation

**Expectation** assessments capture objective, verifiable ground truth data. These represent what the model *should* have produced or what facts it *should* have included, independent of the actual model output. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

Expectation is useful for:
- Building [Evaluation Datasets](/concepts/evaluation-datasets.md) with known correct answers
- Creating test cases for automated evaluation
- Establishing ground truth for systematic model improvement

## Key Differences

| Aspect | Feedback | Expectation |
|--------|----------|-------------|
| Nature | Subjective, opinion-based | Objective, verifiable |
| Purpose | Capture human preferences | Establish ground truth |
| Reusability | Context-dependent | Can be synced to evaluation datasets |
| Automation | Difficult to automate | Can be used for automated evaluation |

## Syncing Expectations to Evaluation Datasets

Expectations collected through labeling sessions can be synchronized to [Evaluation Datasets](/concepts/evaluation-datasets.md) using the `sync()` method. This operation performs an intelligent upsert: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- Each trace's inputs serve as a unique key to identify records in the dataset.
- For traces with matching inputs, expectations from the labeling session overwrite existing expectations when the expectation names are the same.
- Traces from the labeling session that do not match existing trace inputs are added as new records.
- Existing dataset records with different inputs remain unchanged.

This approach enables iterative improvement of evaluation datasets by adding new examples and updating ground truth for existing examples. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Labeling Schemas

Both Feedback and Expectation assessments are collected using [Labeling Schemas](/concepts/labeling-schemas.md), which define the questions and format for feedback collection. Built-in schemas include: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- `EXPECTED_FACTS` — Captures factual expectations
- `EXPECTED_RESPONSE` — Captures expected response content
- `GUIDELINES` — Captures adherence to guidelines

Custom schemas can also be created to capture specific Feedback or Expectation data tailored to particular evaluation goals. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — The container for traces and their associated assessments
- [Labeling Schemas](/concepts/labeling-schemas.md) — The structure defining what assessments to collect
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Datasets that can incorporate Expectation assessments
- [[MLflow Trace|MLflow Traces]] — The application traces being assessed
- [Human Feedback in GenAI](/concepts/multi-level-human-feedback-in-genai-pipelines.md) — Broader context for human evaluation workflows

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
