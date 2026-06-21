---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 352ea8d1b66087f2c396e627cc6989366ae0f23184aa320a3346ed599b3e457a
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-feedback-entity-and-assessment-data-model
    - Assessment Data Model and MLflow Feedback Entity
    - MFEAADM
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: MLflow Feedback Entity and Assessment Data Model
description: A structured data model where user feedback is captured as Assessment entities attached to traces or spans, containing value, source, rationale, and metadata fields.
tags:
  - mlflow
  - data-model
  - feedback
  - tracing
timestamp: "2026-06-19T14:16:33.190Z"
---

# MLflow Feedback Entity and Assessment Data Model

The **Feedback entity** is a structured data type in MLflow used to capture human or automated assessments on [Trace](/concepts/traces.md) objects. Feedback is stored as an [Assessment](/concepts/assessments.md) that can be attached to a complete trace or to individual spans within it, enabling quality monitoring, evaluation dataset creation, and root‑cause analysis of GenAI application outputs. ^[collect-user-feedback-databricks-on-aws.md]

## Overview

In MLflow, user feedback is captured using the `Feedback` entity, a concrete type of `Assessment`. The entity provides a schema for storing the evaluation result, the source of that evaluation (human user, LLM judge, or code), an optional rationale, and additional metadata. Understanding this data model is essential for designing feedback collection systems that integrate seamlessly with MLflow’s evaluation and monitoring capabilities. ^[collect-user-feedback-databricks-on-aws.md]

## Feedback entity fields

The Feedback entity includes the following core fields:

| Field      | Description                                                                 | Example                               |
|------------|-----------------------------------------------------------------------------|---------------------------------------|
| `value`    | The actual feedback – can be boolean, numeric, text, or a structured object. | `True`, `0.85`, `"helpful"`           |
| `source`   | An [#AssessmentSource](/concepts/assessmentsource-entity.md) object identifying who or what provided the feedback. | `AssessmentSource(source_type="HUMAN", source_id="user_abc")` |
| `rationale`| An optional free‑text explanation for the feedback value.                    | `"The response correctly answered the user's question."` |
| `metadata` | Additional context, such as timestamps or custom attributes (dict).         | `{"timestamp": "2025-01-01T12:00:00Z"}` |

^[collect-user-feedback-databricks-on-aws.md]

## AssessmentSource

The `AssessmentSource` object identifies the origin of the feedback. It has two fields:

- **`source_type`**: A string classifying the source. Supported values include `"HUMAN"` (for end‑user or annotator feedback) and `"LLM_JUDGE"` (for automated evaluation by an LLM). ^[collect-user-feedback-databricks-on-aws.md]
- **`source_id`**: An optional identifier for the specific user or system that provided the feedback. For example, a user ID or a service name. ^[collect-user-feedback-databricks-on-aws.md]

This structure allows MLflow to distinguish between different feedback origins and to trace the provenance of each assessment. ^[collect-user-feedback-databricks-on-aws.md]

## Feedback types

MLflow supports several value types for feedback, chosen to suit different evaluation scenarios:

- **Boolean** – e.g., thumbs‑up/thumbs‑down, correct/incorrect. ^[collect-user-feedback-databricks-on-aws.md]
- **Numeric** – e.g., rating on a scale (normalized to 0–1). ^[collect-user-feedback-databricks-on-aws.md]
- **Text** – e.g., a comment or free‑form critique. ^[collect-user-feedback-databricks-on-aws.md]
- **Structured data** – e.g., a JSON object with multiple dimensions. ^[collect-user-feedback-databricks-on-aws.md]

When logging feedback, the developer chooses the `value` type that best fits the evaluation goal. For multi‑dimensional feedback (e.g., separate ratings for accuracy, helpfulness, relevance), each dimension is typically logged as a separate assessment with its own name and value. ^[collect-user-feedback-databricks-on-aws.md]

## Storage and retrieval

Feedback is stored as an assessment permanently associated with the trace. This means:

- The assessment is visible in the MLflow Trace UI alongside the trace data. ^[collect-user-feedback-databricks-on-aws.md]
- It can be queried programmatically using the `mlflow.client.MlflowClient` API (e.g., `get_trace(trace_id)` and inspecting `trace.data.assessments`). ^[collect-user-feedback-databricks-on-aws.md]
- The same `log_feedback` API is used for both development (`mlflow.genai.evaluate()`) and production monitoring contexts. ^[collect-user-feedback-databricks-on-aws.md]

The `log_feedback` function accepts a `trace_id` (or client request ID), a name for the assessment, the value, the `AssessmentSource`, and an optional rationale. Example usage:

```python
mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=True,
    source=AssessmentSource(source_type="HUMAN", source_id=user_id),
    rationale="The response was accurate and complete."
)
```

^[collect-user-feedback-databricks-on-aws.md]

## Related concepts

- [Trace](/concepts/traces.md) – the full record of a GenAI request/response that feedback is attached to.
- Span – a sub‑component of a trace; feedback can also be attached to individual spans.
- [AssessmentSource](/concepts/assessmentsource-entity.md) – the structured provenance of a feedback entry.
- [Production Monitoring](/concepts/production-monitoring.md) – using registered scorers and feedback for ongoing quality tracking.
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) – the `mlflow.genai.evaluate()` API for offline assessment.

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
