---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a55d780db604f73d82a0bfcf7f360e39bfac092ceb7233d0a28f816ec54ad82
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - output-reducers-for-streaming-traces
    - ORFST
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Output Reducers for Streaming Traces
description: A mechanism to aggregate elements yielded by a traced generator or iterator into a single span output using a custom reducer function, with support for token aggregation, metrics aggregation, and error collection.
tags:
  - mlflow
  - tracing
  - streaming
  - output-reducer
timestamp: "2026-06-19T18:57:42.883Z"
---

# Output Reducers for Streaming Traces

**Output reducers** are custom functions used with the `@mlflow.trace` decorator to aggregate elements yielded by a generator or iterator into a single span output. They allow you to transform streaming data — such as tokens from an LLM, metrics, or error events — into a consolidated representation while preserving the raw chunks for debugging. ^[function-decorators-databricks-on-aws.md]

## Overview

When tracing a function that returns a generator or iterator, MLflow captures all yielded elements as a list in the span's output by default. An output reducer overrides this behavior by specifying a custom aggregation function that takes the list of yielded elements and returns a single value. ^[function-decorators-databricks-on-aws.md]

Output reducers are available since MLflow 2.20.2. ^[function-decorators-databricks-on-aws.md]

## How Output Reducers Work

A span for a streaming function starts when the returned iterator begins to be consumed and ends when the iterator is exhausted or an exception is raised. The output reducer receives all chunks collected during the span's lifetime and returns the aggregated result. ^[function-decorators-databricks-on-aws.md]

The raw chunks remain accessible in the **Events** tab of the span in the MLflow Trace UI, allowing you to inspect individual yielded values when debugging. ^[function-decorators-databricks-on-aws.md]

## Basic Usage

Pass an `output_reducer` parameter to the `@mlflow.trace` decorator. The reducer is a callable that accepts a list of yielded elements and returns a single value.

```python
from typing import List, Any

@mlflow.trace(output_reducer=lambda x: ",".join(x))
def stream_data():
    for c in "hello":
        yield c
```

In this example, the span output is `"h,e,l,l,o"` instead of the default list `["h", "e", "l", "l", "o"]`. ^[function-decorators-databricks-on-aws.md]

## Common Patterns

### Token Aggregation

Concatenate streaming tokens into complete text:

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

^[function-decorators-databricks-on-aws.md]

### Metrics Aggregation

Aggregate streaming metrics into summary statistics:

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
        "min": min(values) if values else None
    }

@mlflow.trace(output_reducer=aggregate_metrics)
def stream_metrics():
    for i in range(10):
        yield {"value": i * 2, "timestamp": time.time()}
```

^[function-decorators-databricks-on-aws.md]

### Error Collection

Separate successful results from errors:

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
        "has_errors": len(errors) > 0
    }
```

^[function-decorators-databricks-on-aws.md]

## Advanced Example: OpenAI Streaming

The following example consolidates `ChatCompletionChunk` objects from an OpenAI LLM stream into a single `ChatCompletion` message:

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

^[function-decorators-databricks-on-aws.md]

## Testing Output Reducers

Output reducers can be tested independently of the tracing framework:

```python
import unittest
from typing import List, Dict, Any

def my_reducer(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not chunks:
        return {"status": "empty", "total": 0}
    total = sum(c.get("value", 0) for c in chunks)
    errors = [c for c in chunks if c.get("error")]
    return {
        "status": "error" if errors else "success",
        "total": total,
        "count": len(chunks),
        "average": total / len(chunks) if chunks else 0,
        "error_count": len(errors)
    }

class TestOutputReducer(unittest.TestCase):
    def test_normal_case(self):
        chunks = [{"value": 10}, {"value": 20}, {"value": 30}]
        result = my_reducer(chunks)
        self.assertEqual(result["status"], "success")
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

^[function-decorators-databricks-on-aws.md]

## Performance Considerations

- Output reducers receive all chunks in memory at once. For very large streams, consider implementing streaming alternatives or chunking strategies. ^[function-decorators-databricks-on-aws.md]
- The span remains open until the generator is fully consumed, which impacts latency metrics. ^[function-decorators-databricks-on-aws.md]
- Reducers should be stateless and avoid side effects for predictable behavior. ^[function-decorators-databricks-on-aws.md]

## Related Concepts

- [Function Decorators](/concepts/mlflowtrace-function-decorator.md) — The `@mlflow.trace` decorator for manual tracing
- Span Tracing — Tracing specific code blocks with context managers
- [Auto-Tracing for OpenAI](/concepts/automatic-tracing-for-openai.md) — Automatic tracing of OpenAI API calls
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of MLflow's tracing capabilities
- LiveSpan — The span object that can be modified during execution

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
