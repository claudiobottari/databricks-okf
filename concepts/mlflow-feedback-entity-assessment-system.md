---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e424e9bd177175fe50deb462d3003553b5fbe6facea6398d20ea9bb653479ca
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-feedback-entity-assessment-system
    - MFE(S
    - mlflow-feedback-entity-and-assessment-data-model
    - Assessment Data Model and MLflow Feedback Entity
    - MFEAADM
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: MLflow Feedback Entity (Assessment System)
description: Structured data model for capturing user feedback as assessments on traces, including value, source, rationale, and metadata fields.
tags:
  - mlflow
  - feedback
  - data-model
  - genai
timestamp: "2026-06-18T14:38:44.063Z"
---

# MLflow Feedback Entity (Assessment System)

The **MLflow Feedback Entity (Assessment System)** is a structured data model within [MLflow](/concepts/mlflow.md) that captures user feedback, automated evaluations, and other assessments on [Traces](/concepts/traces.md) and spans. It provides a unified way to store quality signals — whether from human raters, LLM judges, or programmatic sources — and associate them permanently with specific GenAI application interactions. ^[collect-user-feedback-databricks-on-aws.md]

## Overview

In MLflow, feedback is captured using the **Feedback** entity, which is a type of **Assessment** that can be attached to traces or individual spans. The Assessment system provides a structured way to store feedback values, source information, rationales, and metadata. This enables tracking quality over time, identifying areas for improvement, building evaluation datasets from production data, and leveraging feedback for model fine-tuning. ^[collect-user-feedback-databricks-on-aws.md]

## Data Model

The Feedback entity stores the following components:

- **Value**: The actual feedback content, which can be boolean, numeric, text, or structured data
- **Source**: Information about who or what provided the feedback, identified through an `AssessmentSource` object
- **Rationale**: An optional explanation for the feedback
- **Metadata**: Additional context such as timestamps or custom attributes

^[collect-user-feedback-databricks-on-aws.md]

### AssessmentSource

The `AssessmentSource` object identifies the origin of the feedback:

- `source_type`: Can be `"HUMAN"` for user feedback or `"LLM_JUDGE"` for automated evaluation
- `source_id`: Identifies the specific user or system providing the feedback

^[collect-user-feedback-databricks-on-aws.md]

## Types of Feedback

MLflow supports various types of feedback through its assessment system, including:

- **Binary feedback** (e.g., thumbs up/thumbs down)
- **Numeric ratings** (e.g., 1-5 scale for accuracy, helpfulness, relevance)
- **Text comments** with optional rationales
- **Multi-dimensional feedback** with separate ratings for different quality aspects

^[collect-user-feedback-databricks-on-aws.md]

## Feedback Collection Flow

The feedback collection process follows a consistent pattern:

1. **During the initial request**: The application either generates a unique client request ID or retrieves the MLflow-generated trace ID
2. **After receiving the response**: The user provides feedback by referencing either ID
3. **Feedback is logged**: MLflow's `log_feedback` API creates an assessment attached to the original trace
4. **Analysis and monitoring**: Feedback can be queried and analyzed across all traces

^[collect-user-feedback-databricks-on-aws.md]

### Using the log_feedback API

The `mlflow.log_feedback()` function is the primary API for recording assessments:

```python
mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=feedback.is_correct,
    source=AssessmentSource(
        source_type="HUMAN",
        source_id=user_id
    ),
    rationale=feedback.comment
)
```

^[collect-user-feedback-databricks-on-aws.md]

## Feedback Storage and Association

Feedback is stored as assessments on the trace, which means:

- It is permanently associated with the specific interaction
- It can be queried alongside the trace data
- It is visible in the MLflow UI when viewing the trace

^[collect-user-feedback-databricks-on-aws.md]

## Analyzing Feedback Data

### Viewing Feedback in the Trace UI

Feedback assessments are displayed in the MLflow Trace UI, allowing visual inspection of user ratings and comments attached to individual traces. ^[collect-user-feedback-databricks-on-aws.md]

### Retrieving Traces with Feedback

The `MlflowClient.search_traces()` API can retrieve traces from a specific time window, and `client.get_trace()` returns full trace details including assessments:

```python
client = MlflowClient()
traces = client.search_traces(
    experiment_names=[experiment_name],
    filter_string=f"trace.timestamp_ms > {cutoff_timestamp_ms}"
)
trace_detail = client.get_trace(trace.info.trace_id)
assessments = trace_detail.data.assessments
```

^[collect-user-feedback-databricks-on-aws.md]

### Analyzing Feedback Patterns

Feedback data can be analyzed to calculate metrics such as feedback rate, positive/negative ratios, and average ratings across different dimensions. This enables tracking satisfaction metrics over time and across different user segments. ^[collect-user-feedback-databricks-on-aws.md]

## Multi-Dimensional Feedback

The assessment system supports logging multiple feedback dimensions as separate assessments for granular analysis. For example, accuracy, helpfulness, and relevance can each be logged as individual assessments on the same trace, enabling per-dimension quality tracking. ^[collect-user-feedback-databricks-on-aws.md]

## Streaming Response Considerations

When using streaming responses (Server-Sent Events or WebSockets), the trace ID is only available after the stream completes. Feedback collection must account for this by:

- Disabling feedback controls until the trace ID is received
- Sending the trace ID as a final event in the stream
- Tracking both streaming content and trace ID separately in state management

^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that assessments are attached to
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — End-user feedback collection patterns
- [LLM Judges](/concepts/llm-judges.md) — Automated evaluation using LLM-based scorers
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying assessments for continuous quality monitoring
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Building test datasets from collected feedback
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
