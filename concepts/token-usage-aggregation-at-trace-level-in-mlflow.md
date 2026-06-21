---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2cd82b1008b61ddf578470451121dbdd809b938acebc0df13bd293bba6ae7b1
  pageDirectory: concepts
  sources:
    - set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-usage-aggregation-at-trace-level-in-mlflow
    - TUAATLIM
  citations:
    - file: set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
title: Token Usage Aggregation at Trace Level in MLflow
description: Setting token counts (gen_ai.usage.input_tokens and gen_ai.usage.output_tokens) on the root span so MLflow aggregates them at the trace level for the UI summary.
tags:
  - open-telemetry
  - mlflow
  - tracing
  - token-usage
timestamp: "2026-06-19T23:04:28.440Z"
---

# Token Usage Aggregation at Trace Level in [MLflow](/concepts/mlflow.md)

**Token Usage Aggregation at Trace Level** refers to how [MLflow](/concepts/mlflow.md) collects and displays token count information from OpenTelemetry-instrumented [Traces](/concepts/traces.md). When using custom OTel instrumentation with [MLflow](/concepts/mlflow.md), token usage metrics must be set on the **root span** of a trace for [MLflow](/concepts/mlflow.md) to aggregate and display them correctly in the trace-level UI summary. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Overview

When sending [Traces](/concepts/traces.md) from a custom OpenTelemetry-instrumented application to Databricks [MLflow](/concepts/mlflow.md), token counts are aggregated at the trace level rather than per-span. [MLflow](/concepts/mlflow.md) reads token usage attributes specifically from the root span to populate the trace-level summary, including input, output, and total token counts displayed in the [MLflow](/concepts/mlflow.md) UI. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Required Attributes

To display token counts in the UI trace summary, set the following attributes on the root span using `span.set_attribute()`: ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### Input Tokens

Set `gen_ai.usage.input_tokens` to the number of tokens in the input prompt. [MLflow](/concepts/mlflow.md) aggregates this value at the trace level from the root span. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
root.set_attribute("gen_ai.usage.input_tokens", 150)
```

### Output Tokens

Set `gen_ai.usage.output_tokens` to the number of tokens generated in the response. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
root.set_attribute("gen_ai.usage.output_tokens", 42)
```

## Aggregation Behavior

[MLflow](/concepts/mlflow.md) reads token usage values exclusively from the **root span** of a trace. This means that even if child spans within the trace have their own token usage attributes, only the values set on the root span are used for trace-level aggregation and display. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

The trace summary in the [MLflow](/concepts/mlflow.md) UI displays:
- Input token count
- Output token count
- Total token count (calculated from the input and output values)

## Implementation Example

The following example shows token usage attributes set on both a child LLM span and the root span. [MLflow](/concepts/mlflow.md) reads only the root span's values for the trace summary: ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
import json
from opentelemetry import trace

tracer = trace.get_tracer("my-agent")

def run_agent(query: str) -> str:
    with tracer.start_as_current_span("agent-run") as root:
        # Child LLM span
        with tracer.start_as_current_span("chat") as llm:
            llm.set_attribute("gen_ai.operation.name", "chat")
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ]
            response = call_llm(messages)
            llm.set_attribute("gen_ai.input.messages", json.dumps(messages))
            llm.set_attribute("gen_ai.output.messages", json.dumps([
                {"role": "assistant", "content": response}
            ]))
            # Token usage on child span - not used for trace-level aggregation
            llm.set_attribute("gen_ai.usage.input_tokens", 150)
            llm.set_attribute("gen_ai.usage.output_tokens", 42)
        
        # Root span - [[mlflow|MLflow]] reads token usage from here for trace summary
        root.set_attribute("gen_ai.operation.name", "chat")
        root.set_attribute("gen_ai.input.messages", json.dumps([
            {"role": "user", "content": query}
        ]))
        root.set_attribute("gen_ai.output.messages", json.dumps([
            {"role": "assistant", "content": response}
        ]))
        # Token usage on root span - used for trace-level aggregation
        root.set_attribute("gen_ai.usage.input_tokens", 150)
        root.set_attribute("gen_ai.usage.output_tokens", 42)
        
        return response
```

## Verification in [MLflow](/concepts/mlflow.md) UI

After sending [Traces](/concepts/traces.md), open the [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) tab in your experiment. When token usage is correctly set on the root span, the trace summary displays input, output, and total token counts alongside other [Trace Metadata](/concepts/trace-metadata.md). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Searching by Token Usage

Token usage attributes can be used as search filters when querying [Traces](/concepts/traces.md) programmatically. Use the `span.attributes.*` prefix in `mlflow.search_traces()` to filter by token count values: ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

[[mlflow|MLflow]].set_experiment(experiment_id="<experiment-id>")

# Find high-token [[traces|Traces]]
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.gen_ai.usage.input_tokens > 1000"
)
```

## Related Concepts

- [OpenTelemetry Span Attributes for MLflow](/concepts/opentelemetry-mlflow-span-attribute-mapping.md) — Complete guide to setting all span attributes for proper trace rendering.
- [MLflow Span Types](/concepts/mlflow-spans.md) — How [MLflow](/concepts/mlflow.md) categorizes spans and displays them in the UI.
- Trace Level Aggregation — General concept of aggregating span data at the trace level.
- OTel GenAI Semantic Conventions — The underlying OpenTelemetry specification for GenAI operation attributes.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the [MLflow Tracing](/concepts/mlflow-tracing.md) system.

## Sources

- set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md

# Citations

1. [set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md](/references/set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws-8961c630.md)
