---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2a005d6e4688c49449498e880cbe5ab1a17b7d6731413f8c7067b7f71b5cc87
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-associated-feedback-collection
    - TFC
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Trace-Associated Feedback Collection
description: The pattern of linking user feedback to specific MLflow traces using either MLflow-generated trace IDs or custom client request IDs, enabling feedback to be permanently associated with interactions.
tags:
  - mlflow
  - feedback-collection
  - tracing
  - production
timestamp: "2026-06-19T14:17:20.090Z"
---

# Trace-Associated Feedback Collection

**Trace-Associated Feedback Collection** refers to the practice of capturing and logging user feedback by linking it to specific MLflow [Traces](/concepts/traces.md)—the recorded execution paths of GenAI application requests. By associating feedback directly with a trace, teams can attribute quality signals to individual interactions, enabling continuous improvement, quality monitoring, and the creation of evaluation datasets from production data. ^[collect-user-feedback-databricks-on-aws.md]

## Why Collect User Feedback

User feedback provides ground truth about an application’s performance in real-world scenarios. Key benefits include:

- **Real-world quality signals** – Understanding how actual users perceive outputs.
- **Continuous improvement** – Identifying patterns in negative feedback to guide development.
- **Training data creation** – Using feedback to build high-quality evaluation datasets.
- **Quality monitoring** – Tracking satisfaction metrics over time and across user segments.
- **Model fine-tuning** – Leveraging feedback data to improve underlying models.

^[collect-user-feedback-databricks-on-aws.md]

## Types of Feedback

MLflow supports various types of feedback through its assessment system. Feedback can be boolean (e.g., thumbs up/down), numeric (e.g., ratings on a 1–5 scale), text (e.g., comments), or structured data containing multiple dimensions. ^[collect-user-feedback-databricks-on-aws.md]

## Data Model

In MLflow, user feedback is captured using the **Feedback** entity, a type of [Assessment](/concepts/assessments.md) that can be attached to traces or specific spans. The Feedback entity includes:

- **Value** – The actual feedback (boolean, numeric, text, or structured data).
- **Source** – Information about who or what provided the feedback (human user, LLM judge, or code), represented by an `AssessmentSource` object with `source_type` (e.g., `"HUMAN"`, `"LLM_JUDGE"`) and `source_id`.
- **Rationale** – Optional explanation for the feedback.
- **Metadata** – Additional context such as timestamps or custom attributes.

^[collect-user-feedback-databricks-on-aws.md]

## Implementation Approaches

Feedback collection in production requires linking user feedback to specific traces. MLflow supports two primary approaches.

### Approach 1: Using MLflow Trace IDs

The simplest method: retrieve the MLflow-generated trace ID during request processing and return it to the client. The client then submits feedback using that trace ID via the `mlflow.log_feedback()` API. A backend endpoint typically accepts the trace ID, a feedback value, and optional user identification. ^[collect-user-feedback-databricks-on-aws.md]

Example backend implementation:

```python
@app.post("/feedback")
def submit_feedback(
    trace_id: str = Query(...),
    feedback: FeedbackRequest = ...,
    user_id: Optional[str] = Query(None)
):
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
    return {"status": "success"}
```

^[collect-user-feedback-databricks-on-aws.md]

### Approach 2: Using Client Request IDs

Alternatively, applications can generate their own unique client request IDs during request processing and later reference those IDs when logging feedback. This decouples feedback submission from trace ID generation and can be useful when the trace ID is not immediately available. ^[collect-user-feedback-databricks-on-aws.md]

### Handling Streaming Responses

When using streaming responses (Server-Sent Events or WebSockets), the trace ID is only generated after the stream completes. The typical pattern is:

1. The backend streams tokens and sends a final event containing the trace ID.
2. The frontend enables feedback controls only after receiving the trace ID.
3. The frontend stores the streaming content and trace ID separately for later feedback submission.

Implementation considerations include:
- Using a consistent event format with a `type` field to distinguish content tokens, completion events, and errors.
- Adding `X-Accel-Buffering: no` header to disable proxy buffering.
- Implementing proper line buffering in the frontend to handle partial SSE messages.
- Adding small delays between tokens to prevent overwhelming clients.

^[collect-user-feedback-databricks-on-aws.md]

## Analyzing Feedback Data

Once feedback is collected, it can be analyzed to gain insights about application quality and user satisfaction.

### Viewing Feedback in the Trace UI

The MLflow Trace UI displays assessments attached to traces, allowing manual inspection of user feedback along with the full interaction context. ^[collect-user-feedback-databricks-on-aws.md]

### Retrieving Traces with Feedback via SDK

Use `MlflowClient.search_traces()` to retrieve traces from a time window, then fetch full details including assessments:

```python
client = MlflowClient()
traces = client.search_traces(
    experiment_names=["/Shared/production-genai-app"],
    filter_string=f"trace.timestamp_ms > {cutoff_timestamp_ms}"
)
for trace in traces:
    trace_detail = client.get_trace(trace.info.trace_id)
    # Access trace_detail.data.assessments
```

^[collect-user-feedback-databricks-on-aws.md]

### Analyzing Feedback Patterns

Extract and aggregate feedback to compute metrics such as feedback rate, positive rate, and average ratings per dimension. For multi-dimensional feedback, individual assessments (e.g., `user_accuracy`, `user_helpfulness`, `user_relevance`) can be analyzed separately. ^[collect-user-feedback-databricks-on-aws.md]

## Next Steps

After implementing trace-associated feedback collection, teams can:

- [Deploy agents with tracing](/concepts/mlflow-genai-tracing.md) – Understand logging traces in production.
- Build evaluation datasets – Use collected feedback to create test datasets and analyze patterns.
- Set up production monitoring – Monitor quality metrics based on feedback.

^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [Traces](/concepts/traces.md) – The execution records that feedback is attached to.
- [Assessments](/concepts/assessments.md) – The broader entity type that includes user feedback and LLM judge evaluations.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The platform providing tracing and evaluation capabilities.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Continuous quality monitoring using feedback and assessments.

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
