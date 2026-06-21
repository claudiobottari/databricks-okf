---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d137ec00e395a13ec521c54a63f9b190387262a71bc71398299bae1503d3c6d6
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - output-reducers
    - Output Reducer
    - output-reducers-for-streaming-traces
    - ORFST
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Output Reducers
description: Custom aggregation functions for streaming traces that consolidate yielded elements into a single span output, with patterns for token aggregation, metrics, and error collection.
tags:
  - mlflow
  - tracing
  - streaming
  - aggregation
timestamp: "2026-06-19T10:41:15.556Z"
---

# Output Reducers

**Output Reducers** are a mechanism in [MLflow Tracing](/concepts/mlflow-tracing.md) that allow you to aggregate the yielded elements of a streaming generator function into a single, consolidated output for a trace span. When a function decorated with [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) returns a generator or iterator, MLflow normally captures all yielded values as a list. An output reducer replaces that list with a custom aggregation of your choice. ^[function-decorators-databricks-on-aws.md]

## Overview

Streaming functions – for example, token-based LLM generation or real‑time metrics pipelines – produce multiple values over time. By default, a span created from a generator stores the full list of yielded elements in its output. The `output_reducer` parameter lets you specify a function that transforms that list into a single, meaningful result.

- The reducer receives all yielded elements (as a list) once the generator is exhausted.
- The return value of the reducer becomes the span’s `output` field.
- The raw individual chunks remain accessible in the **Events** tab of the span in the MLflow Trace UI, preserving full debug information. ^[function-decorators-databricks-on-aws.md]

## How Output Reducers Work

1. **Define a reducer function** that takes `List[Any]` (the list of yielded chunks) and returns a single aggregated value.
2. **Apply the reducer** by passing it as the `output_reducer` argument to `@mlflow.trace`.
3. **The generator is consumed** – the span remains open until the iterator is exhausted or an exception is raised. ^[function-decorators-databricks-on-aws.md]

### Minimal Example

```python
from typing import List

@mlflow.trace(output_reducer=lambda x: ",".join(x))
def stream_data():
    for c in "hello":
        yield c
```

The span’s output will be `"h,e,l,l,o"` instead of the list `['h','e','l','l','o']`. ^[function-decorators-databricks-on-aws.md]

## Common Output Reducer Patterns

The source document provides several reusable patterns:

### Token Aggregation

```python
from typing import List

def aggregate_tokens(chunks: List[str]) -> str:
    """Concatenate streaming tokens into complete text"""
    return "".join(chunks)

@mlflow.trace(output_reducer=aggregate_tokens)
def stream_text():
    for word in ["Hello", " ", "World", "!"]:
        yield word
```

### Metrics Aggregation

```python
from typing import List, Dict, Any

def aggregate_metrics(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Aggregate streaming metrics into summary statistics"""
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

```python
from typing import List, Dict, Any

def collect_results_and_errors(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Separate successful results from errors"""
    results = []
    errors = []
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

## Advanced Example: OpenAI Streaming

A realistic use case is consolidating `ChatCompletionChunk` objects from OpenAI into a single `ChatCompletion` message. ^[function-decorators-databricks-on-aws.md]

```python
import mlflow
import openai
from openai.types.chat import *
from typing import Optional

def aggregate_chunks(outputs: list[ChatCompletionChunk]) -> Optional[ChatCompletion]:
    """Consolidate ChatCompletionChunks to a single ChatCompletion"""
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

The output reducer turns the stream of `ChatCompletionChunk` objects into a single `ChatCompletion` object. For production use, the document recommends using [MLflow OpenAI Autologging](/concepts/mlflow-openai-autolog.md) which handles this automatically. ^[function-decorators-databricks-on-aws.md]

### Structured Output Generation with JSON Parsing

The source shows how to build a reducer that accumulates tokens, cleans markdown wrappers, and parses the result as JSON. This pattern is useful when an LLM streams structured data. ^[function-decorators-databricks-on-aws.md]

```python
import json
from typing import List, Dict, Any

def structured_output_reducer(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    content_parts = []
    trace_id = None
    model_info = None
    errors = []
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
        response["error_position"] = e.pos if hasattr(e, 'pos') else None
    return response
```

## Testing Output Reducers

Because output reducers are pure functions (they take a list of chunks and return a value), they can be tested independently of the tracing framework. The source provides a unit test example using `unittest`. ^[function-decorators-databricks-on-aws.md]

```python
import unittest

class TestOutputReducer(unittest.TestCase):
    def test_normal_case(self):
        chunks = [{"value": 10}, {"value": 20}, {"value": 30}]
        result = my_reducer(chunks)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["total"], 60)
        self.assertEqual(result["average"], 20.0)

    def test_empty_input(self):
        result = my_reducer([])
        self.assertEqual(result["status"], "empty")
        self.assertEqual(result["total"], 0)

    def test_error_handling(self):
        chunks = [{"value": 10}, {"error": "Network timeout"}, {"value": 20}]
        result = my_reducer(chunks)
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["total"], 30)
        self.assertEqual(result["error_count"], 1)
```

## Performance Considerations

- Output reducers receive **all chunks in memory** at once. For very large streams, consider implementing streaming alternatives or chunking strategies.
- The span remains open until the generator is fully consumed, which affects latency metrics.
- Reducers should be **stateless** and avoid side effects for predictable behavior. ^[function-decorators-databricks-on-aws.md]

## Related Concepts

- Function decorators – The `@mlflow.trace` decorator that supports `output_reducer`.
- Span tracing – Lower-level span creation for manual control.
- [OpenAI autologging](/concepts/mlflow-openai-autolog.md) – Automatic tracing for OpenAI calls (recommended over manual output reducers for OpenAI).
- [Trace events](/concepts/traces.md) – Raw chunks remain visible in span Events for debugging.
- [Streaming outputs](/concepts/streaming-output-tracing.md) – General concept of generator‑based tracing.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
