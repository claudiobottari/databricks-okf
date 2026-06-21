---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a65cc42807565bb49e9f34734bb0a43b90cedfb1ba27a87d9892ee8af1a40465
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-feedback-data-model
    - MFDM
    - Feedback data model
    - feedback data model
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: MLflow Feedback Data Model
description: A structured entity (a type of Assessment) for capturing user feedback on traces, storing value, source, rationale, and metadata
tags:
  - mlflow
  - data-model
  - feedback
timestamp: "2026-06-19T17:46:00.758Z"
---

# MLflow Feedback Data Model

The **MLflow Feedback Data Model** provides a structured framework for capturing, storing, and analyzing user feedback on GenAI application outputs within MLflow. This model enables practitioners to track quality over time, identify improvement areas, and build evaluation datasets from production data. ^[collect-user-feedback-databricks-on-aws.md]

## Core Entity Structure

In MLflow, user feedback is captured using the **Feedback** entity, which is a type of [Assessment](/concepts/assessments.md) that can be attached to [[MLflow Trace|MLflow Traces]] or specific spans. The Feedback entity provides a structured way to store the following components: ^[collect-user-feedback-databricks-on-aws.md]

- **Value**: The actual feedback data, which can be boolean, numeric, text, or structured data
- **Source**: Information about who or what provided the feedback (human user, LLM judge, or code)
- **Rationale**: Optional explanation for the feedback
- **Metadata**: Additional context such as timestamps or custom attributes

## AssessmentSource Object

The `AssessmentSource` object identifies the origin of the feedback: ^[collect-user-feedback-databricks-on-aws.md]

- `source_type`: Can be `"HUMAN"` for user feedback or `"LLM_JUDGE"` for automated evaluation
- `source_id`: Identifies the specific user or system providing feedback

## Supported Feedback Types

MLflow supports various feedback types through its assessment system, including: ^[collect-user-feedback-databricks-on-aws.md]

- **Boolean feedback**: Simple thumbs up/thumbs down (true/false)
- **Numeric ratings**: Scaled ratings such as 1-5 for specific dimensions
- **Text feedback**: Free-form comments and rationales
- **Multi-dimensional feedback**: Separate ratings for different aspects (accuracy, helpfulness, relevance)

## Feedback Storage and Association

Feedback is stored as assessments permanently associated with the specific interaction trace. This means feedback is: ^[collect-user-feedback-databricks-on-aws.md]

- **Permanently linked** to the original trace or span
- **Queryable** alongside trace data
- **Visible** in the MLflow UI when viewing the trace

## Feedback Collection Flow

The feedback collection process follows a consistent pattern regardless of the implementation approach: ^[collect-user-feedback-databricks-on-aws.md]

1. **During initial request**: The application generates a unique client request ID or retrieves the MLflow-generated trace ID
2. **After receiving response**: The user provides feedback by referencing either ID
3. **Feedback logging**: MLflow's `log_feedback` API creates an assessment attached to the original trace
4. **Analysis and monitoring**: Feedback can be queried and analyzed across all traces

## The `log_feedback` API

The `log_feedback` API is available in both `mlflow` and `mlflow-tracing` packages, enabling feedback collection regardless of installation method. MLflow 3 is required for collecting user feedback, as MLflow 2.x is not supported due to performance limitations and missing features essential for production use. ^[collect-user-feedback-databricks-on-aws.md]

### Basic usage:

```python
mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=feedback_value,
    source=AssessmentSource(
        source_type="HUMAN",
        source_id=user_id
    ),
    rationale=feedback_comment
)
```

^[collect-user-feedback-databricks-on-aws.md]

## Streaming Response Considerations

When using streaming responses (Server-Sent Events or WebSockets), the trace ID is not available until the stream completes. This requires a different approach for feedback collection: ^[collect-user-feedback-databricks-on-aws.md]

- The trace ID is only generated after the entire stream finishes
- Feedback UI controls must remain disabled until the trace ID is received
- A consistent event format with a `type` field helps distinguish between content tokens, completion events, and errors
- State must track both streaming content and trace ID separately, with all state reset at the start of each new interaction

## Analysis Capabilities

### Viewing in Trace UI

Feedback can be viewed directly in the MLflow UI when examining traces, with visual indicators for assessments. ^[collect-user-feedback-databricks-on-aws.md]

### SDK-Based Analysis

Using the MlflowClient, practitioners can: ^[collect-user-feedback-databricks-on-aws.md]

- Retrieve traces from specific time windows using `search_traces()`
- Access full trace details including assessments via `get_trace()`
- Extract and analyze feedback patterns, including feedback rates and positive/negative ratios
- Analyze multi-dimensional feedback to calculate average ratings per dimension

## Benefits of Feedback Collection

Collecting user feedback through this data model provides several key benefits: ^[collect-user-feedback-databricks-on-aws.md]

1. **Real-world quality signals**: Understanding how actual users perceive application outputs
2. **Continuous improvement**: Identifying patterns in negative feedback to guide development
3. **Training data creation**: Building high-quality evaluation datasets from production data
4. **Quality monitoring**: Tracking satisfaction metrics over time and across different user segments
5. **Model fine-tuning**: Leveraging feedback data to improve underlying models

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure that feedback assessments attach to
- [Assessment](/concepts/assessments.md) — The parent entity type for feedback in MLflow
- [Production Monitoring](/concepts/production-monitoring.md) — Monitoring quality metrics based on feedback data
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Building test datasets from collected feedback
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Broader context for collecting human annotations

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
