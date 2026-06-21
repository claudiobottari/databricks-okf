---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d0b0f7ee75b6ab375a9384b94e90db8873c1f318147aade61d56e5064e1f259
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-collection-approaches-trace-ids-vs-client-request-ids
    - FCATIVCRI
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: "Feedback Collection Approaches: Trace IDs vs Client Request IDs"
description: "Two methods for linking user feedback to specific traces: using MLflow's auto-generated trace IDs or generating unique client request IDs."
tags:
  - mlflow
  - architecture
  - feedback
  - tracing
timestamp: "2026-06-18T11:00:28.990Z"
---

# Feedback Collection Approaches: Trace IDs vs Client Request IDs

**Feedback Collection Approaches: Trace IDs vs Client Request IDs** refers to two distinct strategies for linking user feedback to specific traces in MLflow GenAI applications. When collecting feedback in production, you must associate feedback with the correct interaction trace. MLflow supports two approaches: using the MLflow-generated trace ID or using a client-generated request ID that you define.^[collect-user-feedback-databricks-on-aws.md]

## Why Feedback Collection Matters

User feedback provides ground truth about an application's performance. It enables real-world quality signals, continuous improvement through pattern identification, training data creation from production data, quality monitoring across user segments, and model fine-tuning.^[collect-user-feedback-databricks-on-aws.md]

MLflow captures feedback using the **Feedback** entity, which is a type of [Assessment (MLflow)|Assessment](/concepts/mlflow-assessment-and-assessmentsource-api.md) attached to traces or specific spans. The Feedback entity stores a value, source information (human user, LLM judge, or code), an optional rationale, and metadata such as timestamps or custom attributes.^[collect-user-feedback-databricks-on-aws.md]

## The Common Feedback Collection Flow

Both approaches follow the same pattern:

1. **During the initial request**: Your application either retrieves the MLflow-generated trace ID or generates a unique client request ID.
2. **After receiving the response**: The user provides feedback by referencing either ID.
3. **Feedback is logged**: MLflow's `log_feedback` API creates an assessment attached to the original trace.
4. **Analysis and monitoring**: You can query and analyze feedback across all traces.

^[collect-user-feedback-databricks-on-aws.md]

## Approach 1: Using MLflow Trace IDs

The simplest approach is to use the trace ID that MLflow automatically generates for each trace. You retrieve this ID during request processing and return it to the client, which then submits it with feedback.^[collect-user-feedback-databricks-on-aws.md]

### Backend Implementation

```python
import mlflow
from fastapi import FastAPI, Query
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
    # Get the current trace ID
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

### Advantages

- **No ID generation required** — MLflow handles tracing automatically.
- **Guaranteed uniqueness** — Trace IDs are system-generated and unique.
- **Simpler client logic** — The frontend only needs to capture and return whatever the server sends.

### Disadvantages

- **Not available until trace completion** — With streaming responses, the trace ID is only generated after the stream finishes, requiring the UI to delay feedback controls until that point.
- **Coupling to MLflow internals** — Clients must handle MLflow-specific IDs, making it harder to switch tracing backends.

## Approach 2: Using Client Request IDs

With client request IDs, your application generates its own unique IDs when processing requests and references them later for feedback. This decouples feedback collection from MLflow's internal trace ID system.^[collect-user-feedback-databricks-on-aws.md]

### Implementation Strategy

You generate a unique client request ID (for example, a UUID) at the start of each request, pass it through your application logic, and return it to the client. When the client submits feedback, it includes this client request ID. Your feedback endpoint must then resolve the client request ID to the corresponding MLflow trace ID before calling `log_feedback`.^[collect-user-feedback-databricks-on-aws.md]

### Advantages

- **Works with any tracing system** — The client request ID is agnostic to the underlying tracing implementation.
- **Available immediately** — You can generate the ID before the trace even starts, enabling feedback collection during streaming without waiting for trace completion.
- **Easier integration with existing systems** — If you already have a request ID scheme, you can reuse it without changes to the client.

### Disadvantages

- **Requires ID mapping** — You must maintain a lookup table or mapping from client request IDs to MLflow trace IDs.
- **Additional server-side logic** — The feedback endpoint must resolve the mapping before logging.
- **Potential for ID collision** — You are responsible for ensuring uniqueness of generated IDs.

## Handling Feedback with Streaming Responses

Streaming responses present a unique challenge because the trace ID is not available until the stream completes. This affects both approaches differently.^[collect-user-feedback-databricks-on-aws.md]

### With Trace IDs

When using Server-Sent Events (SSE) or WebSockets, tokens arrive incrementally and the trace ID is only generated after the stream finishes. The backend must send the trace ID as the final event in the stream.^[collect-user-feedback-databricks-on-aws.md]

```python
async def generate() -> AsyncGenerator[str, None]:
    with mlflow.start_span(name="streaming_chat") as span:
        full_response = ""
        async for token in your_llm_stream_function(request.message):
            full_response += token
            yield f"data: {json.dumps({'type': 'token', 'content': token})}\n\n"
        # Get trace ID after completion
        trace_id = span.trace_id
        yield f"data: {json.dumps({'type': 'done', 'trace_id': trace_id})}\n\n"
```

On the frontend, feedback controls must remain disabled until the trace ID event is received.^[collect-user-feedback-databricks-on-aws.md]

### With Client Request IDs

You can generate a client request ID before the stream starts and return it in the first event of the stream (or as a response header), enabling the UI to show feedback controls immediately — even as the stream continues. The feedback is logged later once the trace completes and you can resolve the mapping.^[collect-user-feedback-databricks-on-aws.md]

## Choosing Between Approaches

| Consideration | Trace IDs | Client Request IDs |
|---|---|---|
| **Simplicity** | No ID generation needed | Requires ID mapping infrastructure |
| **Streaming support** | Feedback delayed until trace completion | Feedback available immediately |
| **Backend coupling** | Coupled to MLflow | Agnostic to tracing backend |
| **ID uniqueness** | Guaranteed by system | Must be ensured by application |
| **Integration with existing systems** | Requires client to handle MLflow IDs | Can reuse existing request ID schemes |

^[collect-user-feedback-databricks-on-aws.md]

## Analyzing Feedback Data

Regardless of which approach you use, you retrieve traces with feedback using the MLflow client SDK:^[collect-user-feedback-databricks-on-aws.md]

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

You can then analyze feedback patterns, satisfaction rates, and multi-dimensional ratings from the retrieved traces.^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure that underlies feedback collection
- Feedback (MLflow) — The structured entity for capturing user feedback on traces
- [Assessment (MLflow)](/concepts/assessments.md) — The parent entity type for feedback
- Production Tracing — Deploying tracing in production environments
- [Build Evaluation Datasets](/concepts/evaluation-datasets.md) — Using collected feedback to create test datasets
- [Production Monitoring](/concepts/production-monitoring.md) — Monitoring quality metrics based on feedback
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Offline evaluation using `mlflow.genai.evaluate()`
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation functions for GenAI applications

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
