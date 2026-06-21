---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0f0133808c17d80068ea74a91d14fc62cdf470c7532d1f2c52cf04bda4f5c2d
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-output-tracing
    - SOT
    - Streaming outputs
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Streaming Output Tracing
description: Tracing of generator and iterator functions with @mlflow.trace, where spans start when the iterator is consumed and end when exhausted.
tags:
  - mlflow
  - tracing
  - streaming
  - generators
timestamp: "2026-06-19T10:41:50.885Z"
---

# Streaming Output Tracing

**Streaming Output Tracing** refers to the ability of [MLflow Tracing](/concepts/mlflow-tracing.md) to instrument Python functions that return a generator or an iterator, capturing each yielded element as part of a trace span. This feature, available since MLflow 2.20.2, enables observability for streaming workloads such as real-time text generation, incremental data processing, and chunked API responses. ^[function-decorators-databricks-on-aws.md]

## How It Works

When a generator function is decorated with [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace), the span does **not** start immediately upon calling the function. Instead, the span begins when the returned iterator is first consumed and ends when the iterator is exhausted or an exception is raised. ^[function-decorators-databricks-on-aws.md]

By default, MLflow collects all elements yielded by the generator into a list and stores that list as the span's output. For example, a generator yielding integers `0` through `4` will produce a span output of `[0, 1, 2, 3, 4]`. This raw list is visible in the span's output field in the MLflow Trace UI. ^[function-decorators-databricks-on-aws.md]

## Customizing Output with Output Reducers

To aggregate the streamed elements into a more meaningful single value, the `output_reducer` parameter can be passed to `@mlflow.trace`. This parameter accepts a callable that receives the full list of yielded chunks and returns the desired aggregated result. ^[function-decorators-databricks-on-aws.md]

Example — concatenating characters into a string:

```python
@mlflow.trace(output_reducer=lambda x: ",".join(x))
def stream_data():
    for c in "hello":
        yield c
```

The span output becomes `"h,e,l,l,o"`, while the individual yielded values remain accessible in the **Events** tab of the span for detailed debugging. ^[function-decorators-databricks-on-aws.md]

## Common Output Reducer Patterns

### Token Aggregation

Concatenates streaming tokens into a single complete text string. ^[function-decorators-databricks-on-aws.md]

```python
def aggregate_tokens(chunks: List[str]) -> str:
    """Concatenate streaming tokens into complete text"""
    return "".join(chunks)

@mlflow.trace(output_reducer=aggregate_tokens)
def stream_text():
    for word in ["Hello", " ", "World", "!"]:
        yield word
```

### Metrics Aggregation

Collects streaming data points and returns summary statistics. ^[function-decorators-databricks-on-aws.md]

```python
def aggregate_metrics(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    values = [c["value"] for c in chunks if "value" in c]
    return {
        "count": len(values),
        "sum": sum(values),
        "average": sum(values) / len(values) if values else 0,
        "max": max(values) if values else None,
        "min": min(values) if values else None,
    }

@mlflow.trace(output_reducer=aggregate_metrics)
def stream_metrics():
    for i in range(10):
        yield {"value": i * 2, "timestamp": time.time()}
```

### Error Collection

Separates successful results from errors and calculates a success rate. ^[function-decorators-databricks-on-aws.md]

```python
def collect_results_and_errors(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    results, errors = [], []
    for chunk in chunks:
        if chunk.get("error"):
            errors.append(chunk["error"])
        else:
            results.append(chunk.get("data"))
    return {
        "results": results,
        "errors": errors,
        "success_rate": len(results) / len(chunks) if chunks else 0,
        "has_errors": len(errors) > 0,
    }
```

## Real-World Use Cases

### OpenAI Streaming (Demonstration)

The following example shows a custom reducer that consolidates `ChatCompletionChunk` objects from OpenAI into a single `ChatCompletion` message. In production, the official [auto-tracing for OpenAI](/concepts/automatic-tracing-for-openai.md) handles this automatically, but the pattern illustrates the underlying mechanics. ^[function-decorators-databricks-on-aws.md]

```python
import mlflow
import openai
from openai.types.chat import *
from typing import Optional

def aggregate_chunks(outputs: list[ChatCompletionChunk]) -> Optional[ChatCompletion]:
    if not outputs:
        return None
    first_chunk = outputs[0]
    delta = first_chunk.choices[0].delta
    message = ChatCompletionMessage(
        role=delta.role, content=delta.content, tool_calls=delta.tool_calls or []
    )
    finish_reason = first_chunk.choices[0].finish_reason
    for chunk in outputs[1:]:
        delta = chunk.choices[0].delta
        message.content += delta.content or ""
        message.tool_calls += delta.tool_calls or []
        finish_reason = finish_reason or chunk.choices[0].finish_reason
    base = ChatCompletion(
        id=first_chunk.id,
        choices=[Choice(index=0, message=message, finish_reason=finish_reason)],
        created=first_chunk.created,
        model=first_chunk.model,
        object="chat.completion",
    )
    return base

@mlflow.trace(output_reducer=aggregate_chunks)
def predict(messages: list[dict]):
    client = openai.OpenAI()
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        yield chunk
```

### Structured Output with JSON Parsing

A real-world reducer that accumulates tokens, strips markdown code block wrappers, and parses the resulting string as JSON, returning both the parsed data and raw content. ^[function-decorators-databricks-on-aws.md]

```python
def structured_output_reducer(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Aggregate streaming chunks into structured output with comprehensive error handling."""
    content_parts, trace_id, model_info, errors = [], None, None, []
    for chunk in chunks:
        chunk_type = chunk.get("type", "token")
        if chunk_type == "token":
            content_parts.append(chunk.get("content", ""))
        elif chunk_type == "trace_info":
            trace_id = chunk.get("trace_id")
            model_info = chunk.get("model")
        elif chunk_type == "error":
            errors.append(chunk.get("message"))
    full_content = "".join(content_parts)
    response = {"trace_id": trace_id, "model": model_info, "raw_content": full_content}
    if errors:
        response["status"] = "error"
        response["errors"] = errors
        return response
    try:
        json_content = full_content.strip()
        if json_content.startswith("```json") and json_content.endswith("```"):
            json_content = json_content[7:-3].strip()
        elif json_content.startswith("```") and json_content.endswith("```"):
            json_content = json_content[3:-3].strip()
        parsed_data = json.loads(json_content)
        response["status"] = "success"
        response["data"] = parsed_data
    except json.JSONDecodeError as e:
        response["status"] = "parse_error"
        response["error"] = f"JSON parsing failed: {str(e)}"
    return response
```

### Multi-Model Response Aggregation

Aggregates responses from multiple model calls and identifies the fastest model and whether consensus exists. ^[function-decorators-databricks-on-aws.md]

```python
def multi_model_reducer(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    responses, latencies = {}, {}
    for chunk in chunks:
        model = chunk.get("model")
        if model:
            responses[model] = chunk.get("response", "")
            latencies[model] = chunk.get("latency", 0)
    return {
        "responses": responses,
        "latencies": latencies,
        "fastest_model": min(latencies, key=latencies.get) if latencies else None,
        "consensus": len(set(responses.values())) == 1,
    }
```

## Testing Output Reducers

Output reducers can be tested independently of the tracing framework, making it easy to verify correct handling of normal cases, empty input, errors, and missing values. ^[function-decorators-databricks-on-aws.md]

```python
class TestOutputReducer(unittest.TestCase):
    def test_normal_case(self):
        chunks = [{"value": 10}, {"value": 20}, {"value": 30}]
        result = my_reducer(chunks)
        self.assertEqual(result["total"], 60)

    def test_empty_input(self):
        result = my_reducer([])
        self.assertEqual(result["status"], "empty")

    def test_error_handling(self):
        chunks = [{"value": 10}, {"error": "Network timeout"}, {"value": 20}]
        result = my_reducer(chunks)
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["error_count"], 1)
```

## Performance Considerations

- Output reducers receive **all chunks in memory at once**. For very large streams, consider implementing streaming alternatives or chunking strategies. ^[function-decorators-databricks-on-aws.md]
- The span remains open until the generator is fully consumed, which impacts latency metrics. ^[function-decorators-databricks-on-aws.md]
- Reducers should be **stateless** and avoid side effects for predictable behavior. ^[function-decorators-databricks-on-aws.md]

## Related Concepts

- @mlflow.trace – The decorator that enables streaming output tracing.
- [Function Decorators](/concepts/mlflowtrace-function-decorator.md) – General usage of `@mlflow.trace`.
- Span Tracing – Manual context manager based tracing.
- [Auto-tracing for OpenAI](/concepts/automatic-tracing-for-openai.md) – Built-in support that handles streaming automatically.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Evaluating streaming agent outputs.
- Observe with Traces – Debugging and observing traced applications.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
