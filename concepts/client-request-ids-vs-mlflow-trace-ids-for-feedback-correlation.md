---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48341e01fc671006f4a7ca8716905ae92a7c2fcd4dd367f44aac945aea374cb7
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-request-ids-vs-mlflow-trace-ids-for-feedback-correlation
    - CRIVMTIFFC
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Client Request IDs vs MLflow Trace IDs for Feedback Correlation
description: "Two approaches for linking user feedback to specific traces: using MLflow's auto-generated trace IDs or using application-generated client request IDs."
tags:
  - mlflow
  - tracing
  - feedback
  - ids
timestamp: "2026-06-18T14:38:59.134Z"
---

# Client Request IDs vs MLflow Trace IDs for Feedback Correlation

**Client Request IDs vs MLflow Trace IDs for Feedback Correlation** refers to the two distinct approaches for linking user feedback to specific traces in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) applications. When collecting feedback in production, you must associate each piece of feedback with the trace that produced the response. MLflow supports two mechanisms for this correlation: using a client-generated request ID or using the MLflow-generated trace ID. ^[collect-user-feedback-databricks-on-aws.md]

## Overview

Both approaches follow the same general pattern: during the initial request, your application either generates a unique client request ID or retrieves the MLflow-generated trace ID; after the user receives the response, they provide feedback by referencing either ID; MLflow's `log_feedback` API creates an assessment attached to the original trace; and you can then query and analyze feedback across all traces. ^[collect-user-feedback-databricks-on-aws.md]

## Approach 1: Using MLflow Trace IDs

The simplest approach is to use the trace ID that MLflow automatically generates for each trace. You retrieve this ID during request processing and return it to the client in the response payload. ^[collect-user-feedback-databricks-on-aws.md]

### Backend Implementation

In a typical FastAPI application, you can retrieve the current trace ID using `mlflow.get_current_active_span().trace_id` and include it in the response:

```python
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = process_message(request.message)
    trace_id = mlflow.get_current_active_span().trace_id
    return ChatResponse(response=response, trace_id=trace_id)
```

The client then submits feedback by sending the trace ID back to a feedback endpoint:

```python
@app.post("/feedback")
def submit_feedback(trace_id: str, feedback: FeedbackRequest, user_id: Optional[str] = None):
    mlflow.log_feedback(
        trace_id=trace_id,
        name="user_feedback",
        value=feedback.is_correct,
        source=AssessmentSource(source_type="HUMAN", source_id=user_id),
        rationale=feedback.comment
    )
```

^[collect-user-feedback-databricks-on-aws.md]

### Advantages

- **No ID generation required** — MLflow handles trace ID creation automatically.
- **Guaranteed uniqueness** — Trace IDs are unique within the MLflow tracking system.
- **Simpler client code** — The client only needs to store and return the trace ID.

### Disadvantages

- **Trace ID timing** — The trace ID is only available after the trace is created, which may be after the response is fully generated. This is particularly relevant for streaming responses, where the trace ID is only available after the stream completes. ^[collect-user-feedback-databricks-on-aws.md]

## Approach 2: Using Client Request IDs

With this approach, you generate your own unique IDs when processing requests and reference them later for feedback. The client request ID is typically generated at the application entry point before any [MLflow Tracing](/concepts/mlflow-tracing.md) begins. ^[collect-user-feedback-databricks-on-aws.md]

### Implementation

The client generates a unique ID (e.g., a UUID) at the start of each request and includes it in the request payload. The backend stores this ID and associates it with the trace. When feedback is submitted, the client sends the same client request ID, and the backend maps it to the corresponding trace before calling `log_feedback`.

### Advantages

- **Available before tracing** — The client request ID can be generated before any MLflow operations begin, making it suitable for streaming scenarios where the trace ID is not immediately available.
- **Client-controlled** — The client can use its own ID format and naming conventions, which may integrate better with existing client-side infrastructure.
- **Idempotency** — Client request IDs can be used for deduplication if the same feedback is submitted multiple times.

### Disadvantages

- **Requires ID generation logic** — The client must implement its own ID generation and management.
- **Requires ID mapping** — The backend must maintain a mapping between client request IDs and MLflow trace IDs, adding complexity.
- **Potential collisions** — Without careful design, client-generated IDs may collide across different clients or sessions.

## Streaming Considerations

When using streaming responses (Server-Sent Events or WebSockets), the trace ID is not available until the stream completes. This makes client request IDs particularly useful for streaming scenarios. ^[collect-user-feedback-databricks-on-aws.md]

### Backend Implementation with SSE

In a streaming implementation, the trace ID is sent as the final event in the stream:

```python
async def generate() -> AsyncGenerator[str, None]:
    with mlflow.start_span(name="streaming_chat") as span:
        full_response = ""
        async for token in your_llm_stream_function(request.message):
            full_response += token
            yield f"data: {json.dumps({'type': 'token', 'content': token})}\n\n"
        span.set_attribute("response", full_response)
        trace_id = span.trace_id
        yield f"data: {json.dumps({'type': 'done', 'trace_id': trace_id})}\n\n"
```

### Frontend Implementation

The frontend must handle the streaming events and enable feedback controls only after receiving the trace ID:

```javascript
// React hook for streaming chat with feedback
function useStreamingChat() {
  const [isStreaming, setIsStreaming] = useState(false);
  const [streamingContent, setStreamingContent] = useState('');
  const [traceId, setTraceId] = useState(null);
  // ... event handling logic that sets traceId on 'done' event
}
```

^[collect-user-feedback-databricks-on-aws.md]

## Choosing Between the Two Approaches

| Factor | MLflow Trace IDs | Client Request IDs |
|--------|-----------------|-------------------|
| Setup complexity | Minimal | Moderate |
| ID availability | After trace creation | Before request processing |
| Streaming support | Requires deferred delivery | Available immediately |
| Client integration | Simple (return trace ID) | Requires ID generation |
| Uniqueness guarantee | Built-in | Client responsibility |

Use MLflow trace IDs when your application uses synchronous request-response patterns and you want the simplest integration. Use client request IDs when you need IDs before tracing begins (e.g., for streaming), when you need to integrate with existing client-side ID systems, or when you need client-controlled deduplication. ^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [User Feedback Collection](/concepts/end-user-feedback-collection-via-sdk.md) — The broader process of collecting and logging user feedback in MLflow
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure that captures GenAI application execution
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Monitoring quality metrics based on feedback
- [AssessmentSource](/concepts/assessmentsource-entity.md) — The entity that identifies who or what provided feedback
- Streaming Responses — Handling feedback collection with streaming LLM outputs

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
