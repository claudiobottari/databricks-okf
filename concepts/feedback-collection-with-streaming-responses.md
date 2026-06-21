---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7681989df25a5c303594cdb68bf9a379e679d8856c7f3c30e309893e3d799c98
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-collection-with-streaming-responses
    - FCWSR
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Feedback Collection with Streaming Responses
description: Techniques for collecting user feedback when GenAI responses are streamed via SSE or WebSockets, where trace IDs are only available after stream completion.
tags:
  - mlflow
  - genai
  - streaming
  - feedback
timestamp: "2026-06-19T09:16:55.179Z"
---

# Feedback Collection with Streaming Responses

**Feedback Collection with Streaming Responses** refers to the specific techniques and design patterns required to capture user feedback when a GenAI application delivers responses incrementally via technologies such as Server-Sent Events (SSE) or WebSockets. Unlike traditional request-response patterns, streaming responses present unique challenges for linking feedback to the correct interaction because the trace identifier is not available until the stream completes.

## Why Streaming Is Different

In the classic request-response pattern, the application receives the complete output and its corresponding MLflow trace ID together, enabling the client to immediately submit feedback. With streaming:

1. **Tokens arrive incrementally** – The response is built up over time as tokens stream from the LLM.
2. **Trace completion is deferred** – The trace ID is only generated after the entire stream finishes.
3. **Feedback UI must wait** – Users cannot provide feedback until they have both the complete response and the trace ID.^[collect-user-feedback-databricks-on-aws.md]

This timing gap forces developers to adopt a different architecture for feedback collection, typically sending the trace ID as the final event in the stream.

## Backend Implementation with Server-Sent Events

A common approach is to use Server-Sent Events (SSE) and emit a special “done” event that carries the trace ID after all tokens have been streamed. The backend wraps the streaming logic in an MLflow trace (via `mlflow.start_span`), streams each token as an SSE data event, and then sends a final JSON event containing the trace ID. The following Python example (using FastAPI) illustrates the pattern:

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import mlflow, json, asyncio
from typing import AsyncGenerator

app = FastAPI()

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
                    await asyncio.sleep(0.01)  # prevent overwhelming the client

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
            "X-Accel-Buffering": "no",  # disable proxy buffering
        }
    )
```

^[collect-user-feedback-databricks-on-aws.md]

## Frontend Implementation

On the client side, the streaming logic must accumulate tokens, detect the trace ID from the final event, and only then enable feedback buttons. The following React hook demonstrates how to parse the SSE stream and manage state:

```javascript
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
      const response = await fetch('/chat/stream', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message }),
      });
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
              case 'token':
                setStreamingContent((prev) => prev + data.content);
                break;
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
    } catch (error) {
      setError(error.message);
      setIsStreaming(false);
    }
  }, []);

  return { sendStreamingMessage, streamingContent, isStreaming, traceId, error };
}
```

The feedback UI then checks that a `traceId` exists before showing the thumbs-up/thumbs-down buttons, preventing submissions before the trace is available.^[collect-user-feedback-databricks-on-aws.md]

## Key Considerations

- **Trace ID timing**: Design the UI to gracefully disable feedback controls until the “done” event arrives with the trace ID.^[collect-user-feedback-databricks-on-aws.md]
- **Event structure**: Use a consistent format with a `type` field (e.g., `token`, `done`, `error`) to make parsing reliable.^[collect-user-feedback-databricks-on-aws.md]
- **State management**: Reset all streaming and feedback state at the start of each new interaction to prevent stale data issues.^[collect-user-feedback-databricks-on-aws.md]
- **Error handling**: Include error events in the stream so that failures are communicated to the client and logged to the MLflow trace when possible.^[collect-user-feedback-databricks-on-aws.md]
- **Buffer management**:
  - Set the `X-Accel-Buffering: no` header to disable proxy-level buffering.
  - Implement line-based buffering on the frontend to handle partial SSE messages.
  - Consider adding reconnection logic for network interruptions.^[collect-user-feedback-databricks-on-aws.md]
- **Performance optimization**: Add small delays between token emissions (e.g., `asyncio.sleep(0.01)`) to avoid overwhelming clients, and batch tokens if they arrive faster than the client can process. Include backpressure mechanisms if appropriate.^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- [User Feedback Collection](/concepts/end-user-feedback-collection-via-sdk.md) – General approach to capturing human feedback on traces.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The infrastructure underlying trace recording and assessment.
- [AssessmentSource](/concepts/assessmentsource-entity.md) – The entity that identifies who or what provided the feedback (HUMAN, LLM_JUDGE, etc.).
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Using feedback data to monitor application quality in production.
- Build Evaluation Datasets from Production Data – How feedback can be turned into test datasets.

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
