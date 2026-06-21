---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8f699edc390441ed52edd4f0f69543c749d233545c10a0f003ce044f5630c6c
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - feedback-vs-expectation-labels
    - FVEL
    - Feedback vs Expectation
    - Feedback vs. Expectation
    - Expectation
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Feedback vs Expectation Labels
description: The two types of human-generated assessments captured in labeling sessions — Feedback (subjective ratings) and Expectation (ground-truth annotations) — used to improve GenAI apps through systematic evaluation.
tags:
  - mlflow
  - human-feedback
  - labeling-schemas
timestamp: "2026-06-19T09:34:12.239Z"
---

---
title: Feedback vs Expectation Labels
summary: Two distinct types of human-generated assessments that can be collected on traces via labeling sessions: Feedback captures subjective ratings and qualitative opinions, while Expectations capture objective ground-truth data.
sources:
  - create-and-manage-labeling-sessions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:30:00.000Z"
updatedAt: "2026-06-19T10:30:00.000Z"
tags:
  - mlflow
  - genai
  - evaluation
  - human-feedback
  - labeling
aliases:
  - feedback-vs-expectation-labels
  - FVEL
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Feedback vs Expectation Labels

**Feedback vs Expectation Labels** describes the two categories of human-generated assessments that can be collected on [[MLflow Trace|MLflow Traces]] through [Labeling Sessions](/concepts/labeling-sessions.md). When domain experts review traces in the MLflow Review App, they can provide either **Feedback** (subjective, qualitative ratings) or **Expectations** (objective, ground-truth annotations). The choice between these label types depends on the evaluation goal and the nature of the quality criteria being assessed. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

Labeling sessions serve as a structured mechanism for collecting human assessments on existing traces. The collected data can then be used to improve GenAI applications through systematic evaluation and model refinement. The two label types serve different purposes in this workflow. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Feedback Labels

**Feedback** labels capture subjective, qualitative assessments from human reviewers. They represent human opinions about the quality, appropriateness, or effectiveness of a model's response. Feedback is typically collected using [Label Schemas](/concepts/label-schemas.md) that define rating scales or categorical options for reviewers to select.

Common use cases for feedback include:
- Rating the overall quality of a response (e.g., Poor, Fair, Good, Excellent)
- Assessing tone, helpfulness, or empathy
- Evaluating the completeness or clarity of an answer

Feedback labels are valuable for understanding how humans perceive an application's outputs and for identifying areas where the model may need improvement from a user experience perspective. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Expectation Labels

**Expectations** labels capture objective, factual ground-truth data. They represent what the correct or expected response should have been for a given input. Unlike feedback, which is inherently subjective, expectations provide a definitive reference point against which model outputs can be measured.

Built-in expectation schemas include expected_facts vs expected_response|EXPECTED_FACTS and expected_facts vs expected_response|EXPECTED_RESPONSE. These can be used to:
- Document what factual information should have been included in the response
- Capture the ideal or correct response for a given input
- Establish ground-truth data for automated evaluation pipelines

Expectations are particularly useful for creating high-quality evaluation datasets and for enabling systematic measurement of model accuracy and factual correctness. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Key Differences

| Dimension | Feedback | Expectations |
|-----------|----------|--------------|
| Nature | Subjective, qualitative | Objective, factual |
| Purpose | Capture human opinion | Define ground truth |
| Repeatability | May vary between reviewers | Should be consistent when correct |
| Schema types | Categorical ratings, scales | Fact lists, ideal responses |
| Usage | UX improvement, perception analysis | Evaluation datasets, accuracy measurement |

## Synchronization to Evaluation Datasets

A critical distinction arises when synchronizing collected labels to [Evaluation Datasets](/concepts/evaluation-datasets.md). The `sync()` method on a labeling session specifically synchronizes only **Expectations** to evaluation datasets. This is because expectations provide the ground-truth reference data that automated judges and metrics can compare against. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

The synchronization process performs an intelligent upsert:
- Each trace's inputs serve as a unique key to identify records in the dataset
- For traces with matching inputs, expectations overwrite existing expectations when the expectation names are the same
- Traces from the labeling session that do not match existing trace inputs are added as new records
- Existing dataset records with different inputs remain unchanged

This allows teams to iteratively improve their evaluation datasets by adding new examples and updating ground truth for existing examples based on expert annotations. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Choosing Between Feedback and Expectations

The choice between feedback and expectation labels depends on the evaluation objective:

- **Use Feedback** when assessing subjective qualities like helpfulness, tone, or user satisfaction that require human judgment.
- **Use Expectations** when establishing objective benchmarks for accuracy, factual correctness, or ideal response quality that can be reused in automated evaluation.

Both label types can be collected within the same labeling session using multiple [Label Schemas](/concepts/label-schemas.md), enabling comprehensive assessment of GenAI application performance. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — The container for collecting feedback and expectations
- [Label Schemas](/concepts/label-schemas.md) — The questions and format for feedback collection
- expected_facts vs expected_response|EXPECTED_FACTS — Built-in schema for factual expectations
- expected_facts vs expected_response|EXPECTED_RESPONSE — Built-in schema for expected model responses
- GUIDELINES — Built-in schema for guideline-based evaluation
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Where expectations are synced for automated testing
- [Human Feedback for GenAI](/concepts/human-feedback-collection-for-judge-alignment.md) — Broader workflow for incorporating human assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Using feedback for ongoing quality monitoring

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
