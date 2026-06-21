---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7f780c8ac23139788b600dff37106c160217ed6bf3e8339e8be81d842c73def
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-response-feedback-collection
    - SRFC
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Streaming Response Feedback Collection
description: Technique for collecting user feedback when using SSE/WebSocket streaming responses, where the trace ID is only available after stream completion
tags:
  - mlflow
  - streaming
  - feedback
timestamp: "2026-06-19T17:46:53.124Z"
---



# Streaming Response Feedback Collection

**Streaming Response Feedback Collection** refers to the process of capturing and logging user assessments when GenAI application responses are delivered incrementally via Server-Sent Events (SSE) or WebSockets, where the trace ID is only available after the stream completes. ^[collect-user-feedback-databricks-on-aws.md]

## Why Streaming Is Different

In traditional request-response patterns, the client receives the complete response and its trace ID together, enabling immediate feedback submission. With streaming responses, the feedback collection sequence changes fundamentally: ^[collect-user-feedback-databricks-on-aws.md]

1. **Tokens arrive incrementally**: The response is built up over time as tokens stream from the LLM. ^[collect-user-feedback-databricks-on-aws.md]
2. **Trace completion is deferred**: The trace ID is only generated after the entire stream finishes. ^[collect-user-feedback-databricks-on-aws.md]
3. **Feedback UI must wait**: Users cannot provide feedback until they have both the complete response and the trace ID. ^[collect-user-feedback-databricks-on-aws.md]

This timing mismatch means that feedback controls must remain disabled during the streaming phase and only become active once the final trace ID event is delivered. ^[collect-user-feedback-databricks-on-aws.md]

## Architecture Overview

### Backend Implementation with SSE

The backend sends the trace ID as the final event in the SSE stream, after all content tokens have been delivered. The stream uses a consistent event format with a `type` field to distinguish between content tokens, completion events, and errors. ^[collect-user-feedback-databricks-on-aws.md]

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import mlflow
import json
import asyncio
from typing import AsyncGenerator

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Stream chat responses with trace ID sent at completion."""
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
                    await asyncio.sleep(0.01)  # Prevent overwhelming the client
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
            "X-Accel-Buffering": "no"
        }
    )
```

### Frontend Implementation

The frontend handles the streaming events and enables feedback controls only after receiving the trace ID. Key state management considerations include: ^[collect-user-feedback-databricks-on-aws.md]

- **Track streaming content and trace ID separately**: Reset all state at the start of each new interaction.
- **Disable feedback controls during streaming**: Buttons should only become active when `traceId` is non-null and streaming has completed.
- **Handle partial SSE messages**: Implement proper line buffering to parse events reliably.

## Key Considerations

### Trace ID Timing

The trace ID is only available after the streaming completes. Design your UI to handle this gracefully by disabling feedback controls until the trace ID is received. ^[collect-user-feedback-databricks-on-aws.md]

### Event Structure

Use a consistent event format with a `type` field to distinguish between content tokens, completion events, and errors. This makes parsing and handling events more reliable. ^[collect-user-feedback-databricks-on-aws.md]

### State Management

Track both the streaming content and trace ID separately. Reset all state at the start of each new interaction to prevent stale data issues. ^[collect-user-feedback-databricks-on-aws.md]

### Error Handling

Include error events in the stream to gracefully handle failures. Ensure errors are logged to the trace when possible for debugging. ^[collect-user-feedback-databricks-on-aws.md]

### Buffer Management

Use `X-Accel-Buffering: no` header to disable proxy buffering. Implement proper line buffering in the frontend to handle partial SSE messages. Consider implementing reconnection logic for network interruptions. ^[collect-user-feedback-databricks-on-aws.md]

### Performance Optimization

Add small delays between tokens (e.g., `asyncio.sleep(0.01)`) to prevent overwhelming clients. Batch multiple tokens if they arrive too quickly. Consider implementing backpressure mechanisms for slow clients. ^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [Trace Assessments](/concepts/trace-assessments.md) — The mechanism for storing user feedback as assessments on traces
- [Feedback Entity](/concepts/feedback-object.md) — The structured data model for capturing feedback values, source, rationale, and metadata
- MLflow log_feedback API|log_feedback API — The MLflow API for recording user feedback programmatically
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Using collected feedback for continuous quality monitoring

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
