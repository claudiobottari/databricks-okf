---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee943d4958b3c377c865af220c5529e97075516714fd72c08d9469a7904dc97a
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.75
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - assessment-data-feedback-vs-expectation
    - AD(VE
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Assessment Data (Feedback vs Expectation)
description: "The two types of human-generated assessments collected during labeling sessions: Feedback (subjective quality ratings) and Expectations (ground-truth reference responses)."
tags:
  - mlflow
  - assessments
  - feedback
  - expectations
timestamp: "2026-06-18T14:51:57.221Z"
---

# Assessment Data (Feedback vs Expectation)

**Assessment Data (Feedback vs Expectation)** describes the two types of human-generated evaluations that can be collected during [Labeling Sessions](/concepts/labeling-sessions.md) in the MLflow Review App. Understanding the distinction between *Feedback* and *Expectation* data is fundamental to designing effective human evaluation workflows for GenAI applications.

## Overview

When domain experts review traces in a labeling session, they produce assessments that fall into one of two categories: **Feedback** or **Expectation**. The type of data collected is determined by the [Labeling Schemas](/concepts/labeling-schemas.md) configured for the session. Both types serve different purposes in the evaluation and improvement lifecycle of GenAI applications. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Feedback

**Feedback** refers to subjective evaluations of an agent's response or behavior. Feedback assessments typically capture a reviewer's qualitative judgment about the quality, appropriateness, or correctness of the agent's output.

### Characteristics

- Subjective in nature — different reviewers may provide different ratings for the same trace
- Typically uses categorical ratings (e.g., "Poor", "Fair", "Good", "Excellent")
- Reflects human preference judgments
- Can be used to train reward models or refine system prompts

### Example

A `response_quality` schema with input type `InputCategorical` and options `["Poor", "Fair", "Good", "Excellent"]` collects feedback assessments. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Expectation

**Expectation** refers to objective, ground-truth assessments that specify what the agent *should* have done or produced in a given scenario. Expectations define the correct or expected behavior against which agent performance can be measured.

### Characteristics

- Objective in nature — the correct answer is not subjective
- Defines a ground truth for evaluation
- Can consist of expected facts, expected responses, or guidelines
- Used to create [Evaluation Datasets](/concepts/evaluation-datasets.md) with established baselines

### Types of Expectations

Built-in expectation schemas include:

- `EXPECTED_FACTS` — Facts that the agent's response should contain
- `EXPECTED_RESPONSE` — The ideal or correct response the agent should produce
- `GUIDELINES` — Behavioral rules the agent should follow

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Practical Distinction

| Aspect | Feedback | Expectation |
|--------|----------|-------------|
| Nature | Subjective judgment | Objective ground truth |
| Question style | "How good was this response?" | "What should the response contain?" |
| Schema examples | `response_quality` (categorical) | `EXPECTED_FACTS`, `EXPECTED_RESPONSE` |
| Usage | Human preference alignment | Dataset creation, offline evaluation |
| Reviewer variance | High (varies by reviewer) | Low (agreement expected) |

## Working with Assessment Data

### Collecting Assessments

Reviewers provide assessments through the MLflow Review App during labeling sessions. MLflow stores their responses as `Assessments` on the traces in the session. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Using Expectations for Evaluation Datasets

Collecting `Expectations` is particularly valuable for building [Evaluation Datasets](/concepts/evaluation-datasets.md). The `sync()` method on a labeling session can transfer expectations from a completed labeling session into an evaluation dataset. This enables systematic, repeatable evaluation workflows. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
# Sync expectations from a completed labeling session to an evaluation dataset
session.sync(to_dataset="customer_service_eval_dataset")
```

### Retrieving Assessments

After reviewers complete a labeling session, assessments can be retrieved through the MLflow UI or the MLflow API. In the UI, reviewers' responses appear under the **Assessments** section of each trace. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Use feedback for exploration**: When you are uncertain about quality criteria, use feedback schemas to gather human preferences and identify patterns.
- **Use expectations for measurement**: When quality criteria are well-defined, use expectation schemas to establish ground truth for systematic evaluation.
- **Iterate on schemas**: Start with feedback during early development, then refine to expectations as evaluation criteria become clearer.
- **Leverage the sync workflow**: Use the labeling session `sync()` method to convert expert-validated expectations into reusable evaluation datasets. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md)
- [Labeling Schemas](/concepts/labeling-schemas.md)
- [Evaluation Datasets](/concepts/evaluation-datasets.md)
- [MLflow Review App](/concepts/mlflow-review-app.md)
- [Human Feedback for GenAI](/concepts/human-feedback-collection-for-judge-alignment.md)
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
