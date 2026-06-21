---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9bf34685554bb2ef8da3491c44e736277bc1d383ee2c15cfc9d21e6dad252f84
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - span-attributes-and-search
    - Search and Span Attributes
    - SAAS
    - Search for traces by OTel span attributes
    - Searching Traces by OTel Attributes
    - Span Attributes
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Span Attributes and Search
description: Spans carry typed attributes accessible via get_attribute() and SpanAttributeKey constants, and can be searched by name (exact or regex), span type, span ID, or combination of criteria using trace.search_spans().
tags:
  - mlflow
  - tracing
  - spans
  - search
timestamp: "2026-06-19T13:52:54.346Z"
---

# Span Attributes and Search

**Span Attributes and Search** refers to the mechanisms for accessing, querying, and filtering the metadata and state associated with individual spans within an [[MLflow Trace]]. Spans represent discrete operations or units of work in a trace, and their attributes provide detailed information about execution behavior, inputs, outputs, and custom instrumentation data.

## Overview

Each Span in a trace carries a set of attributes that describe its execution. These attributes can be accessed programmatically using the `get_attribute()` method or by iterating over the span's `.attributes` dictionary. The SpanAttributeKey constant enum provides predefined keys for accessing commonly used attributes, particularly for chat model spans. ^[access-trace-data-databricks-on-aws.md]

## Accessing Span Attributes

### Basic Attribute Access

Span attributes are available as a dictionary on the span object. You can retrieve all attributes or query specific ones using the `get_attribute()` method. ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.tracing.constant import SpanAttributeKey

# Get all attributes
print("All span attributes:")
for key, value in chat_span.attributes.items():
    print(f"  {key}: {value}")

# Get a specific attribute
specific_attr = chat_span.get_attribute("custom_attribute")
print(f"Custom attribute: {specific_attr}")
```

### Chat-Specific Attributes

For spans of type `CHAT_MODEL`, the `SpanAttributeKey` enum provides convenient access to chat-related data: ^[access-trace-data-databricks-on-aws.md]

```python
# Access chat-specific attributes using SpanAttributeKey
messages = chat_span.get_attribute(SpanAttributeKey.CHAT_MESSAGES)
tools = chat_span.get_attribute(SpanAttributeKey.CHAT_TOOLS)
print(f"Chat messages: {messages}")
print(f"Available tools: {tools}")
```

### Token Usage Attributes

Token consumption information is stored as span attributes and can be accessed at the individual span level: ^[access-trace-data-databricks-on-aws.md]

```python
# Access token usage from span
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")
print(f"Span token usage - Input: {input_tokens}, Output: {output_tokens}")
```

## Searching Spans

The [Trace.search_spans()](/concepts/trace-search-query-syntax.md) method allows filtering spans by name, span type, or span ID. Searches support exact names, regular expressions, and combined criteria. ^[access-trace-data-databricks-on-aws.md]

### Search by Name

```python
import re

# Search by exact name
retriever_spans = trace.search_spans(name="retrieve_documents")
print(f"Found {len(retriever_spans)} [[retriever-spans|RETRIEVER Spans]]")

# Search by regex pattern
pattern = re.compile(r".*_tool$")
tool_spans = trace.search_spans(name=pattern)
print(f"Found {len(tool_spans)} tool spans")
```

### Search by Span Type

The SpanType enum defines the available span types. Searches accept either the enum member or its string value. ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.entities import SpanType

# Search by span type (using enum or string)
chat_spans = trace.search_spans(span_type=SpanType.CHAT_MODEL)
llm_spans = trace.search_spans(span_type="CHAT_MODEL")
print(f"Found {len(chat_spans)} chat model spans")
```

### Combined Criteria and Specific Span ID

```python
# Search by span ID
specific_span = trace.search_spans(span_id=retriever_spans[0].span_id)
print(f"Found span: {specific_span[0].name if specific_span else 'Not found'}")

# Combine criteria
tool_fact_check = trace.search_spans(
    name="fact_check_tool",
    span_type=SpanType.TOOL
)
print(f"Found {len(tool_fact_check)} fact check tool spans")

# Get all spans of a type
all_tools = trace.search_spans(span_type=SpanType.TOOL)
for tool in all_tools:
    print(f"Tool: {tool.name}")
```

## Span Properties

Each span provides the following core properties beyond its attributes: ^[access-trace-data-databricks-on-aws.md]

| Property | Description |
|----------|-------------|
| `span_id` | Unique identifier for the span |
| `name` | Human-readable name of the operation |
| `span_type` | Type of span (e.g., CHAT_MODEL, TOOL, RETRIEVER) |
| `trace_id` | ID of the parent trace |
| `parent_id` | ID of the parent span (None for root spans) |
| `start_time_ns` | Start time in nanoseconds |
| `end_time_ns` | End time in nanoseconds |
| `status` | Span status object with `status_code` and `description` |
| `inputs` | Input data for the span |
| `outputs` | Output data from the span |

## Related Concepts

- [[MLflow Trace]] — The container for spans and execution data
- SpanType Enum — Enumeration of available span types for search filtering
- SpanAttributeKey — Predefined keys for accessing common span attributes
- [Token Usage Tracking](/concepts/mlflow-token-usage-tracking.md) — Accessing token counts from spans and traces
- [Trace Analysis Examples](/concepts/genai-trace-analysis-and-debugging.md) — Practical use cases for span analysis

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
