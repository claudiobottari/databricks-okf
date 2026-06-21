---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc9d63b0c76f3545f85df65e49e89062fe44e965308efe36115db4b05b85d062
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assessmentsource-entity
    - AssessmentSourceType
    - AssessmentSource
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: AssessmentSource Entity
description: An MLflow entity that identifies who or what provided feedback, supporting source_type (HUMAN or LLM_JUDGE) and source_id fields
tags:
  - mlflow
  - data-model
  - source-tracking
timestamp: "2026-06-19T17:46:18.514Z"
---

---

title: AssessmentSource Entity
summary: An MLflow entity that identifies the origin of feedback with source_type (HUMAN, LLM_JUDGE, or code) and source_id for identifying the specific user or system providing the assessment.
sources:
  - collect-user-feedback-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:16:52.595Z"
updatedAt: "2026-06-19T14:17:21.079Z"
tags:
  - mlflow
  - feedback
  - entity
  - provenance
aliases:
  - assessmentsource-entity
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AssessmentSource Entity

**AssessmentSource Entity** is a data structure in [MLflow](/concepts/mlflow.md) that identifies the origin of a feedback assessment attached to a [GenAI trace](/concepts/mlflow-genai-trace.md). It records whether the assessment came from a human user, an automated LLM judge, or programmatic logic, and optionally captures a specific identifier for the source.

## Overview

The `AssessmentSource` entity is part of MLflow's [feedback data model](/concepts/mlflow-feedback-data-model.md). It is used by the `log_feedback` API to attribute each assessment to its originator. The entity stores two fields: `source_type` (a string indicating the category of source) and `source_id` (an optional string that further identifies the specific user, system, or process that provided the assessment). ^[collect-user-feedback-databricks-on-aws.md]

## Fields

- **`source_type`**: A string that identifies the kind of source. Valid values include `"HUMAN"` (for end‑user feedback), `"LLM_JUDGE"` (for automated evaluation), or `"CODE"` (for programmatically generated assessments). ^[collect-user-feedback-databricks-on-aws.md]
- **`source_id`**: An optional string that identifies the specific user, system, or process that created the assessment. For example, when collecting human feedback the `source_id` might hold a user identifier, and when collecting LLM‑judge feedback it might hold the name of the judge. ^[collect-user-feedback-databricks-on-aws.md]

## Usage Pattern

The typical instantiation in Python code is:

```python
from mlflow.entities import AssessmentSource

source = AssessmentSource(
    source_type="HUMAN",
    source_id=user_id          # e.g. "alice" or "user‑123"
)
```

The `AssessmentSource` object is then passed as the `source` argument to `mlflow.log_feedback()`, which attaches it to the trace as an assessment. ^[collect-user-feedback-databricks-on-aws.md]

## Relationship to Other MLflow Entities

The `AssessmentSource` entity is a field of the [Feedback](/concepts/feedback-object.md) entity, which is itself a type of [Assessment](/concepts/assessments.md) in MLflow. The Feedback entity is the top‑level container for user feedback; the `AssessmentSource` inside it records the provenance of that feedback. Because the Feedback entity is linked to a Span or [Trace](/concepts/traces.md), the `AssessmentSource` effectively records the provenance of the evaluation for a specific span or trace. ^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [Feedback data model](/concepts/mlflow-feedback-data-model.md) – The overall schema for collecting user feedback in MLflow.
- [Assessment (MLflow)](/concepts/assessments-mlflow-genai.md) – The broader concept of evaluations on traces.
- [GenAI trace](/concepts/mlflow-genai-trace.md) – The execution trace to which an assessment is attached.
- MLflow log_feedback API|log_feedback API – The API that uses `AssessmentSource` to record the provenance of a feedback item.

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
