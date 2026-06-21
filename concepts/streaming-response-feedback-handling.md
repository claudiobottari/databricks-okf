---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74abb563399c4c4779fecdf6024d71888348cb60bcd3a5afe825f8c85d63d77f
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-response-feedback-handling
    - SRFH
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Streaming Response Feedback Handling
description: Special approach for collecting user feedback on streaming responses where trace IDs are only available after stream completion, requiring deferred feedback UI design.
tags:
  - mlflow
  - streaming
  - feedback
  - sse
timestamp: "2026-06-18T11:00:37.662Z"
---

# Streaming Response Feedback Handling

**Streaming Response Feedback Handling** refers to the techniques and best practices for collecting user feedback on GenAI applications that deliver responses incrementally via streaming protocols such as Server-Sent Events (SSE) or WebSockets. Because the trace ID is only available after the stream completes, feedback collection must be deferred and coordinated with the end of the streaming session.^[collect-user-feedback-databricks-on-aws.md]

## Why Streaming Requires a Different Approach

In traditional synchronous request-response patterns, the complete response and its associated trace ID are returned together. This allows a feedback UI to be presented immediately. With streaming responses:

1. **Tokens arrive incrementally** — the response is built up over time as tokens stream from the LLM.
2. **Trace completion is deferred** — the trace ID is generated only after the entire stream finishes.
3. **Feedback UI must wait** — users cannot provide feedback until they have both the complete response and the trace ID.

Thus, a streaming-aware implementation must signal the trace ID as part of the stream’s final event, and the frontend must enable feedback controls only after that event is received.^[collect-user-feedback-databricks-on-aws.md]

## Backend Implementation with Server-Sent Events (SSE)

The backend should stream tokens from the LLM, and once the stream ends, send a final `done` event containing the trace ID. The following FastAPI example demonstrates this pattern:

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
            "X-Accel-Buffering": "no",  # Disable proxy buffering
        }
    )
```

^[collect-user-feedback-databricks-on-aws.md]

Sending a structured event with a `type` field (e.g., `token`, `done`, `error`) makes parsing reliable on the client side.^[collect-user-feedback-databricks-on-aws.md]

## Frontend Implementation

The frontend must parse SSE events, accumulate the streamed content, and wait for the `done` event to extract the trace ID before enabling feedback controls. Below is a conceptual React hook and component:

```javascript
// Hook managing streaming state and trace ID
function useStreamingChat() {
  const [isStreaming, setIsStreaming] = useState(false);
  const [streamingContent, setStreamingContent] = useState('');
  const [traceId, setTraceId] = useState(null);
  const [error, setError] = useState(null);

  const sendStreamingMessage = useCallback(async (message) => {
    setIsStreaming(true);
    setStreamingContent('');
    setTraceId(null);
    setError(null);

    try {
      const response = await fetch('/chat/stream', { /* ... */ });
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = JSON.parse(line.slice(6));
            switch (data.type) {
              case 'token': setStreamingContent(prev => prev + data.content); break;
              case 'done':
                setTraceId(data.trace_id);
                setIsStreaming(false);
                break;
              case 'error':
                setError(data.error);
                setIsStreaming(false);
                break;
            }
          }
        }
      }
    } catch (error) { /* ... */ }
  }, []);

  return { sendStreamingMessage, streamingContent, isStreaming, traceId, error };
}
```

In the component, feedback buttons are disabled until `traceId` is set, and they become enabled once streaming finishes and the trace ID is available. After feedback is submitted, the buttons are disabled again.^[collect-user-feedback-databricks-on-aws.md]

## Key Considerations

When implementing streaming feedback handling, keep the following points in mind:

- **Trace ID timing**: Design the UI to handle the delay gracefully by disabling feedback controls until the trace ID is received.^[collect-user-feedback-databricks-on-aws.md]
- **Event structure**: Use a consistent event format with a `type` field to distinguish between content tokens, completion events, and errors. This makes parsing more reliable.^[collect-user-feedback-databricks-on-aws.md]
- **State management**: Track both the streaming content and trace ID separately. Reset all state at the start of each new interaction to prevent stale data issues.^[collect-user-feedback-databricks-on-aws.md]
- **Error handling**: Include error events in the stream to gracefully handle failures. Ensure errors are logged to the trace when possible for debugging.^[collect-user-feedback-databricks-on-aws.md]
- **Buffer management**:
  - Use the `X-Accel-Buffering: no` header to disable proxy buffering.
  - Implement proper line buffering in the frontend to handle partial SSE messages.
  - Consider implementing reconnection logic for network interruptions.^[collect-user-feedback-databricks-on-aws.md]
- **Performance optimization**:
  - Add small delays between tokens (e.g., `asyncio.sleep(0.01)`) to prevent overwhelming clients.
  - Batch multiple tokens if they arrive too quickly.
  - Consider implementing backpressure mechanisms for slow clients.^[collect-user-feedback-databricks-on-aws.md]

## Logging Feedback After Stream Completion

Once the trace ID is available, feedback is logged using the same `mlflow.log_feedback()` API used for non-streaming responses. The trace ID is passed to the feedback endpoint, which creates an assessment attached to the trace. This ensures feedback is permanently associated with the streaming interaction.^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- User feedback collection — general patterns for collecting feedback on GenAI responses
- [MLflow Tracing](/concepts/mlflow-tracing.md) — the tracing framework used to capture and store interaction data
- [MLflow Assessment](/concepts/mlflow-genai-assessment.md) — the data model for feedback attached to traces
- Server-Sent Events (SSE) — the streaming protocol commonly used with GenAI applications
- Logging feedback in production — best practices for production deployments of feedback collection
- Production monitoring with MLflow — monitoring quality metrics based on collected feedback

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
