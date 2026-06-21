---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1a197aa88aa06cb04d4e946f591f2c1b24f83ada7eadf74f91267e78d791559
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assessment-source-tracking-in-mlflow
    - ASTIM
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Assessment Source Tracking in MLflow
description: Tagging feedback with AssessmentSource and AssessmentSourceType to distinguish feedback provenance (end users, developers, or expert reviewers) for traceability
tags:
  - mlflow
  - assessment
  - provenance
  - metadata
timestamp: "2026-06-19T21:53:21.144Z"
---

# Assessment Source Tracking in MLflow

**Assessment Source Tracking in MLflow** refers to the mechanism for recording and attributing feedback, evaluations, and annotations associated with MLflow traces. This system enables teams to distinguish between feedback provided by different types of evaluators — such as end users, developers, and domain experts — and to trace the provenance of each assessment back to its source.

## Overview

MLflow provides the ability to collect and store human feedback alongside [[MLflow Trace|MLflow Traces]]. When feedback is logged, the system captures not only the assessment value and rationale, but also metadata about who or what provided that assessment. This metadata is stored using the `AssessmentSource` class, which specifies both the type of source and a unique identifier for the specific evaluator. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Assessment Source Types

Assessment sources are categorized using the `AssessmentSourceType` enum. MLflow supports multiple source types to accommodate different feedback workflows:

### HUMAN Source Type

The `HUMAN` source type is used for feedback provided by people. This includes both end users interacting with a deployed application and developers or experts reviewing traces through the UI or SDK. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Other Source Types

While the human source type is the primary example demonstrated, the `AssessmentSourceType` enum is designed to support additional source types for programmatic or automated feedback providers.

## Source Identification

Each assessment is associated with a `source_id` string that uniquely identifies the evaluator within the context of the source type. For example, when logging end-user feedback, the `source_id` should correspond to the actual user ID from the production application. This allows teams to track which users are providing feedback and to correlate assessments with specific user interactions. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Logging Assessments with Source Tracking

Assessments are logged using the `mlflow.log_feedback()` function, which accepts a `source` parameter of type `AssessmentSource`. The assessment source is constructed with two fields:
- `source_type`: An `AssessmentSourceType` value (e.g., `AssessmentSourceType.HUMAN`)
- `source_id`: A string identifier for the specific evaluator

The following example demonstrates logging end-user feedback with source tracking:

```python
from mlflow.entities.assessment import AssessmentSource, AssessmentSourceType

mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=False,
    rationale="Missing details about key features",
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="enduser_123",
    ),
)
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Viewing Assessment Sources in the UI

Assessment sources are displayed in the MLflow UI alongside the associated traces. When viewing a trace in the **Logs** tab, the **Assessments** section on the right side of the trace details dialog shows each assessment's name, value, and source information. This provides a clear audit trail for understanding who evaluated each trace and what feedback they provided. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Use Cases

### End-User Feedback Collection

In production deployments, applications can capture feedback from end users (e.g., thumbs up/down buttons) and log it with the user's unique identifier as the `source_id`. This allows teams to segment feedback by user and investigate patterns in user satisfaction. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Developer Annotations

Developers can add annotations directly through the MLflow UI, creating assessments that are attributed to their user identity. These annotations can include numerical scores, categorical ratings, or qualitative notes about trace quality. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Expert Review Sessions

Domain experts can provide authoritative feedback through [Labeling Sessions](/concepts/labeling-sessions.md). When traces are added to a labeling session, experts can assess responses and provide ground truth labels. These expert assessments can then be used to evaluate application quality using MLflow's scoring functions, such as `Correctness()`, which compares application outputs against expert-provided expectations. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The execution records that assessments are attached to
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — The broader workflow for collecting and using human assessments
- [Labeling Sessions](/concepts/labeling-sessions.md) — Structured expert review workflows that generate authoritative assessments
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that uses assessments, including expert labels, to score application quality
- [AssessmentSource](/concepts/assessmentsource-entity.md) — The entity class for tracking assessment provenance
- AssessmentSourceType — The enum for categorizing assessment providers

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
