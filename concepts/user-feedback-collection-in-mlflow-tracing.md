---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 79f2c89089d6245ad7bbbf60891d5d082a751d50b707c808741f23ff25744663
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - user-feedback-collection-in-mlflow-tracing
    - UFCIMT
    - User Feedback on Traces
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: User Feedback Collection in MLflow Tracing
description: MLflow provides a structured way to capture user feedback as assessments on traces, enabling quality tracking and evaluation dataset creation for GenAI applications.
tags:
  - mlflow
  - feedback
  - tracing
  - genai
timestamp: "2026-06-18T11:01:46.448Z"
---

# User Feedback Collection in [MLflow Tracing](/concepts/mlflow-tracing.md)

**User Feedback Collection in MLflow Tracing** is the structured process of capturing, storing, and analyzing end-user assessments of GenAI application outputs within MLflow's tracing framework. MLflow provides a dedicated `Feedback` entity — a subtype of `Assessment` — that can be attached to traces or individual spans, enabling organizations to track real-world quality signals, identify improvement areas, and build evaluation datasets from production data.^[collect-user-feedback-databricks-on-aws.md]

## Prerequisites

MLflow 3 is required for collecting user feedback. MLflow 2.x is not supported due to performance limitations and missing features essential for production use. ^[collect-user-feedback-databricks-on-aws.md]

For production deployments, install the `mlflow-tracing` package, which is optimized for minimal dependencies and better performance:

```bash
pip install --upgrade mlflow-tracing
```

The `log_feedback` API is available in both the full MLflow package and `mlflow-tracing`, so user feedback collection works regardless of the installation method.^[collect-user-feedback-databricks-on-aws.md]

## Why Collect User Feedback

User feedback provides ground truth about application performance:

- **Real-world quality signals** — Understand how actual users perceive outputs.
- **Continuous improvement** — Identify patterns in negative feedback to guide development.
- **Training data creation** — Build high-quality evaluation datasets from production interactions.
- **Quality monitoring** — Track satisfaction metrics over time and across user segments.
- **Model fine-tuning** — Leverage feedback data to improve underlying models.^[collect-user-feedback-databricks-on-aws.md]

## Feedback Data Model

In MLflow, user feedback is captured using the **Feedback** entity, a type of [Assessments (MLflow GenAI)](/concepts/assessments.md) that attaches to traces or specific spans. Each Feedback entity stores:

- **Value**: The actual feedback — boolean, numeric, text, or structured data.
- **Source**: Information about who or what provided the feedback (human user, LLM judge, or code), represented by an `AssessmentSource` object.
- **Rationale**: Optional explanation for the feedback.
- **Metadata**: Additional context such as timestamps or custom attributes.^[collect-user-feedback-databricks-on-aws.md]

The `AssessmentSource` object has two fields:
- `source_type`: Can be `"HUMAN"` for user feedback or `"LLM_JUDGE"` for automated evaluation.
- `source_id`: Identifies the specific user or system providing feedback.^[collect-user-feedback-databricks-on-aws.md]

## End-User Feedback Collection Flow

When implementing feedback collection in production, you link user feedback to specific traces. The process follows a consistent pattern:

1. **During the initial request**: Your application either generates a unique client request ID or retrieves the MLflow-generated trace ID.
2. **After receiving the response**: The user provides feedback by referencing either ID.
3. **Feedback is logged**: MLflow's `log_feedback` API creates an assessment attached to the original trace.
4. **Analysis and monitoring**: You query and analyze feedback across all traces.^[collect-user-feedback-databricks-on-aws.md]

### Approach 1: Using MLflow Trace IDs

The simplest approach uses the trace ID that MLflow automatically generates. Retrieve this ID during request processing and return it to the client:

```python
import mlflow
from fastapi import FastAPI, Query
from mlflow.client import MlflowClient
from mlflow.entities import AssessmentSource
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    trace_id: str  # Include the trace ID in the response

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = process_message(request.message)
    trace_id = mlflow.get_current_active_span().trace_id
    return ChatResponse(response=response, trace_id=trace_id)

class FeedbackRequest(BaseModel):
    is_correct: bool
    comment: Optional[str] = None

@app.post("/feedback")
def submit_feedback(
    trace_id: str = Query(..., description="The trace ID from the chat response"),
    feedback: FeedbackRequest = ...,
    user_id: Optional[str] = Query(None, description="User identifier")
):
    mlflow.log_feedback(
        trace_id=trace_id,
        name="user_feedback",
        value=feedback.is_correct,
        source=AssessmentSource(source_type="HUMAN", source_id=user_id),
        rationale=feedback.comment
    )
    return {"status": "success", "trace_id": trace_id}
```

^[collect-user-feedback-databricks-on-aws.md]

### Approach 2: Using Client Request IDs

Generate your own unique IDs when processing requests and reference them later for feedback. This approach provides more control over ID generation and can be useful when trace IDs must be decoupled from the feedback submission flow.^[collect-user-feedback-databricks-on-aws.md]

## Handling Feedback with Streaming Responses

Streaming responses (Server-Sent Events or WebSockets) present a unique challenge: the trace ID is not available until the stream completes. In traditional request-response patterns, the response and trace ID arrive together. With streaming:

1. Tokens arrive incrementally as the LLM generates them.
2. The trace ID is only generated after the entire stream finishes.
3. The feedback UI must wait until both the complete response and trace ID are available.^[collect-user-feedback-databricks-on-aws.md]

### Backend Implementation with SSE

Send the trace ID as the final event in the stream:

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import mlflow
import json
import asyncio
from typing import AsyncGenerator

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    async def generate() -> AsyncGenerator[str, None]:
        try:
            with mlflow.start_span(name="streaming_chat") as span:
                mlflow.update_current_trace(
                    request_message=request.message,
                    stream_start_time=datetime.now().isoformat()
                )
                full_response = ""
                async for token in your_llm_stream_function(request.message):
                    full_response += token
                    yield f"data: {json.dumps({'type': 'token', 'content': token})}\n\n"
                    await asyncio.sleep(0.01)
                span.set_attribute("response", full_response)
                span.set_attribute("token_count", len(full_response.split()))
                trace_id = span.trace_id
                yield f"data: {json.dumps({'type': 'done', 'trace_id': trace_id})}\n\n"
        except Exception as e:
            if mlflow.get_current_active_span():
                mlflow.update_current_trace(error=str(e))
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )
```

^[collect-user-feedback-databricks-on-aws.md]

### Key Considerations for Streaming

- **Trace ID timing**: Design the UI to disable feedback controls until the trace ID is received.
- **Event structure**: Use a consistent format with a `type` field to distinguish tokens, completion events, and errors.
- **State management**: Track streaming content and trace ID separately; reset all state at each new interaction.
- **Error handling**: Include error events in the stream and log errors to the trace when possible.
- **Buffer management**: Use `X-Accel-Buffering: no` to disable proxy buffering; implement proper line buffering for partial SSE messages.
- **Performance optimization**: Add small delays between tokens and batch tokens that arrive too quickly.^[collect-user-feedback-databricks-on-aws.md]

## Multi-Dimensional Feedback

For more granular analysis, log each aspect of feedback as a separate assessment:

```python
from mlflow.entities import AssessmentSource

@app.post("/detailed-feedback")
def submit_detailed_feedback(
    trace_id: str,
    accuracy: int = Query(..., ge=1, le=5),
    helpfulness: int = Query(..., ge=1, le=5),
    relevance: int = Query(..., ge=1, le=5),
    user_id: str = Query(...),
    comment: Optional[str] = None
):
    dimensions = {"accuracy": accuracy, "helpfulness": helpfulness, "relevance": relevance}
    for dimension, score in dimensions.items():
        mlflow.log_feedback(
            trace_id=trace_id,
            name=f"user_{dimension}",
            value=score / 5.0,  # Normalize to 0-1 scale
            source=AssessmentSource(source_type="HUMAN", source_id=user_id),
            rationale=comment if dimension == "accuracy" else None
        )
    return {"status": "success", "trace_id": trace_id, "feedback_recorded": dimensions}
```

^[collect-user-feedback-databricks-on-aws.md]

## Analyzing Feedback Data

### Viewing Feedback in the Trace UI

Feedback is visible in the MLflow UI when viewing individual traces, appearing as assessments attached to the trace or span.^[collect-user-feedback-databricks-on-aws.md]

### Retrieving Traces with Feedback Using the SDK

First, retrieve traces from a specific time window:

```python
from mlflow.client import MlflowClient
from datetime import datetime, timedelta

def get_recent_traces(experiment_name: str, hours: int = 24):
    client = MlflowClient()
    cutoff_time = datetime.now() - timedelta(hours=hours)
    cutoff_timestamp_ms = int(cutoff_time.timestamp() * 1000)
    traces = client.search_traces(
        experiment_names=[experiment_name],
        filter_string=f"trace.timestamp_ms > {cutoff_timestamp_ms}"
    )
    return traces
```

^[collect-user-feedback-databricks-on-aws.md]

### Analyzing Feedback Patterns

Extract and analyze feedback from traces:

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

    feedback_rate = (traces_with_feedback / total_traces) * 100 if total_traces > 0 else 0
    positive_rate = (positive_count / traces_with_feedback) * 100 if traces_with_feedback > 0 else 0

    return {
        "total_traces": total_traces,
        "traces_with_feedback": traces_with_feedback,
        "feedback_rate": feedback_rate,
        "positive_rate": positive_rate,
        "positive_count": positive_count,
        "negative_count": negative_count
    }
```

^[collect-user-feedback-databricks-on-aws.md]

### Analyzing Multi-Dimensional Feedback

For rating-based feedback:

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

    average_ratings = {}
    for dimension, scores in ratings_by_dimension.items():
        if scores:
            average_ratings[dimension] = sum(scores) / len(scores)
    return average_ratings
```

^[collect-user-feedback-databricks-on-aws.md]

## Feedback Storage and Scope

Feedback is stored as assessments on the trace, meaning:

- It is permanently associated with the specific interaction.
- It can be queried alongside trace data.
- It is visible in the MLflow UI when viewing the trace.^[collect-user-feedback-databricks-on-aws.md]

## Next Steps

- [Production tracing](/concepts/production-monitoring.md) — Understand logging traces in production.
- [Build evaluation datasets from user feedback](/concepts/evaluation-datasets-for-genai.md) — Use collected feedback to create test datasets and analyze patterns for quality improvements.
- [Production monitoring (MLflow GenAI)](/concepts/production-quality-monitoring-mlflow-genai.md) — Monitor quality metrics based on feedback.

## Related Concepts

- [Assessments (MLflow GenAI)](/concepts/assessments.md) — The parent entity type for feedback and evaluations
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The foundation for trace-based monitoring in MLflow
- [Code-based Scorers](/concepts/code-based-scorers.md) — Programmatic evaluation functions that complement user feedback
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The offline assessment API for development testing

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
