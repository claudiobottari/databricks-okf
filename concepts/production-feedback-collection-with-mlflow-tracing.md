---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7dd9934e8f5f4c18885833a8514ae59543d5df3f3106617631fd0b2db415a049
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - production-feedback-collection-with-mlflow-tracing
    - PFCWM
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Production Feedback Collection with mlflow-tracing
description: The optimized production deployment pattern using the mlflow-tracing package with minimal dependencies and the log_feedback API, requiring MLflow 3 and supporting both trace ID and client request ID approaches.
tags:
  - mlflow
  - production
  - deployment
  - tracing
timestamp: "2026-06-19T14:17:12.350Z"
---

# Production Feedback Collection with mlflow-tracing

**Production Feedback Collection with mlflow-tracing** refers to the process of capturing, storing, and analyzing user feedback on GenAI application outputs in production environments using the `mlflow-tracing` package. This enables teams to track real-world quality signals, identify improvement areas, and build evaluation datasets from live user interactions.

## Overview

Collecting and logging user feedback is essential for understanding the real-world quality of a GenAI application. MLflow provides a structured way to capture feedback as assessments on traces, enabling teams to track quality over time, identify patterns in negative feedback, and build high-quality evaluation datasets from production data. ^[collect-user-feedback-databricks-on-aws.md]

User feedback provides ground truth about application performance, supporting:

- **Real-world quality signals** — Understanding how actual users perceive application outputs
- **Continuous improvement** — Identifying patterns in negative feedback to guide development
- **Training data creation** — Using feedback to build high-quality evaluation datasets
- **Quality monitoring** — Tracking satisfaction metrics over time and across user segments
- **Model fine-tuning** — Leveraging feedback data to improve underlying models

^[collect-user-feedback-databricks-on-aws.md]

## Prerequisites

For production deployments, install the `mlflow-tracing` package, which is optimized for production use with minimal dependencies and better performance characteristics:

```
pip install --upgrade mlflow-tracing
```

The `log_feedback` API is available in both the full `mlflow` package and the lightweight `mlflow-tracing` package, so feedback collection works regardless of installation method. MLflow 3 is required — MLflow 2.x is not supported due to performance limitations and missing features essential for production use. ^[collect-user-feedback-databricks-on-aws.md]

## Feedback Data Model

In MLflow, user feedback is captured using the **Feedback** entity, a type of [Assessment](/concepts/assessments.md) that can be attached to [Traces](/concepts/traces.md) or specific spans. The Feedback entity provides a structured way to store:

- **Value**: The actual feedback (boolean, numeric, text, or structured data)
- **Source**: Information about who or what provided the feedback (human user, LLM judge, or code)
- **Rationale**: Optional explanation for the feedback
- **Metadata**: Additional context like timestamps or custom attributes

Understanding this data model helps design effective feedback collection systems that integrate seamlessly with MLflow's evaluation and monitoring capabilities. ^[collect-user-feedback-databricks-on-aws.md]

## Implementation Approaches

When implementing feedback collection in production, you need to link user feedback to specific traces. Two approaches are available:

### Using MLflow Trace IDs

The simplest approach uses the trace ID that MLflow automatically generates for each trace. During request processing, retrieve this ID and return it to the client:

```python
import mlflow
from mlflow.entities import AssessmentSource

def chat(request):
    # Your GenAI application logic here
    response = process_message(request.message)
    
    # Get the current trace ID
    trace_id = mlflow.get_current_active_span().trace_id
    
    return {
        "response": response,
        "trace_id": trace_id
    }

def submit_feedback(trace_id, is_correct, user_id=None, comment=None):
    mlflow.log_feedback(
        trace_id=trace_id,
        name="user_feedback",
        value=is_correct,
        source=AssessmentSource(
            source_type="HUMAN",
            source_id=user_id
        ),
        rationale=comment
    )
```

^[collect-user-feedback-databricks-on-aws.md]

### Using Client Request IDs

Generate your own unique IDs when processing requests and reference them later for feedback. This approach is useful when you need to correlate feedback with your existing request tracking system. ^[collect-user-feedback-databricks-on-aws.md]

## Handling Streaming Responses

Streaming responses present a unique challenge for feedback collection because the trace ID is not available until the stream completes. In traditional request-response patterns, the response and trace ID are received together, but with streaming:

1. Tokens arrive incrementally as the response builds
2. Trace completion is deferred — the trace ID is only generated after the entire stream finishes
3. Feedback UI must wait until users have both the complete response and the trace ID

^[collect-user-feedback-databricks-on-aws.md]

### Backend Implementation with SSE

For server-sent events (SSE) streaming, send the trace ID as a final event after the stream completes:

```python
from fastapi.responses import StreamingResponse
import mlflow
import json

@app.post("/chat/stream")
async def chat_stream(request):
    async def generate():
        with mlflow.start_span(name="streaming_chat") as span:
            full_response = ""
            async for token in your_llm_stream_function(request.message):
                full_response += token
                yield f"data: {json.dumps({'type': 'token', 'content': token})}\n\n"
            
            # Get trace ID after completion
            trace_id = span.trace_id
            
            # Send trace ID as final event
            yield f"data: {json.dumps({'type': 'done', 'trace_id': trace_id})}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")
```

^[collect-user-feedback-databricks-on-aws.md]

### Key Considerations for Streaming

- **Trace ID timing**: The trace ID is only available after streaming completes. Design UI to disable feedback controls until the trace ID is received.
- **Event structure**: Use a consistent event format with a `type` field to distinguish between content tokens, completion events, and errors.
- **State management**: Track streaming content and trace ID separately. Reset all state at the start of each new interaction.
- **Error handling**: Include error events in the stream and log errors to the trace when possible.
- **Buffer management**: Use the `X-Accel-Buffering: no` header to disable proxy buffering and implement proper line buffering for partial SSE messages.
- **Performance optimization**: Add small delays between tokens to prevent overwhelming clients, batch tokens that arrive too quickly, and consider backpressure mechanisms for slow clients.

^[collect-user-feedback-databricks-on-aws.md]

## Multi-Dimensional Feedback

Beyond simple thumbs up/down, you can collect structured feedback across multiple dimensions:

```python
@app.post("/detailed-feedback")
def submit_detailed_feedback(
    trace_id: str,
    accuracy: int = Query(..., ge=1, le=5),
    helpfulness: int = Query(..., ge=1, le=5),
    relevance: int = Query(..., ge=1, le=5),
    user_id: str,
    comment: Optional[str] = None
):
    dimensions = {
        "accuracy": accuracy,
        "helpfulness": helpfulness,
        "relevance": relevance
    }
    
    for dimension, score in dimensions.items():
        mlflow.log_feedback(
            trace_id=trace_id,
            name=f"user_{dimension}",
            value=score / 5.0,  # Normalize to 0-1 scale
            source=AssessmentSource(
                source_type="HUMAN",
                source_id=user_id
            ),
            rationale=comment if dimension == "accuracy" else None
        )
    
    return {"status": "success", "trace_id": trace_id}
```

^[collect-user-feedback-databricks-on-aws.md]

## Analyzing Feedback Data

### Retrieving Traces with Feedback

Use the `MlflowClient` to search for traces within a specific time window:

```python
from mlflow.client import MlflowClient
from datetime import datetime, timedelta

client = MlflowClient()
cutoff_time = datetime.now() - timedelta(hours=24)
cutoff_timestamp_ms = int(cutoff_time.timestamp() * 1000)

traces = client.search_traces(
    experiment_names=["/Shared/production-genai-app"],
    filter_string=f"trace.timestamp_ms > {cutoff_timestamp_ms}"
)
```

^[collect-user-feedback-databricks-on-aws.md]

### Analyzing Feedback Patterns

Extract and analyze feedback from traces to calculate key metrics:

```python
def analyze_user_feedback(traces):
    client = MlflowClient()
    total_traces = len(traces)
    traces_with_feedback = 0
    positive_count = 0
    negative_count = 0
    
    for trace in traces:
        trace_detail = client.get_trace(trace.info.trace_id)
        if trace_detail.data.assessments:
            traces_with_feedback += 1
            for assessment in trace_detail.data.assessments:
                if assessment.name == "user_feedback":
                    if assessment.value:
                        positive_count += 1
                    else:
                        negative_count += 1
    
    feedback_rate = (traces_with_feedback / total_traces) * 100 if traces_with_feedback > 0 else 0
    positive_rate = (positive_count / traces_with_feedback) * 100 if traces_with_feedback > 0 else 0
    
    return {
        "total_traces": total_traces,
        "feedback_rate": feedback_rate,
        "positive_rate": positive_rate,
        "positive_count": positive_count,
        "negative_count": negative_count
    }
```

^[collect-user-feedback-databricks-on-aws.md]

### Analyzing Multi-Dimensional Feedback

For rating-based feedback, calculate average scores per dimension:

```python
def analyze_ratings(traces):
    client = MlflowClient()
    ratings_by_dimension = {}
    
    for trace in traces:
        trace_detail = client.get_trace(trace.info.trace_id)
        if trace_detail.data.assessments:
            for assessment in trace_detail.data.assessments:
                if assessment.name.startswith("user_") and assessment.name != "user_feedback":
                    dimension = assessment.name.replace("user_", "")
                    if dimension not in ratings_by_dimension:
                        ratings_by_dimension[dimension] = []
                    ratings_by_dimension[dimension].append(assessment.value)
    
    return {
        dimension: sum(scores) / len(scores)
        for dimension, scores in ratings_by_dimension.items()
        if scores
    }
```

^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [Traces and Spans](/concepts/trace-spans.md) — The core observability primitives that feedback attaches to
- [Assessments](/concepts/assessments.md) — The entity type used to store feedback and evaluation results
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Monitoring quality metrics based on feedback
- [Build Evaluation Datasets](/concepts/evaluation-datasets.md) — Using collected feedback to create test datasets
- Human Feedback Alignment — Improving system quality with expert annotations
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Offline evaluation using similar assessment mechanisms

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
