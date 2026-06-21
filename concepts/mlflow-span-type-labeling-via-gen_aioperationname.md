---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3add941905ba38e09d95cab77f7de7140ff3da1c47f6b75dee650a02a4003f8b
  pageDirectory: concepts
  sources:
    - set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-span-type-labeling-via-gen_aioperationname
    - MSTLVG
  citations:
    - file: set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
title: MLflow Span Type Labeling via gen_ai.operation.name
description: Setting the gen_ai.operation.name attribute on spans to classify operations (chat, etc.) so MLflow renders the correct span type instead of UNKNOWN.
tags:
  - open-telemetry
  - mlflow
  - tracing
  - span-types
timestamp: "2026-06-19T23:03:31.504Z"
---

# [MLflow](/concepts/mlflow.md) Span Type Labeling via gen_ai.operation.name

**MLflow Span Type Labeling via gen_ai.operation.name** is the mechanism by which custom OpenTelemetry-instrumented applications assign a semantic type label to each span in a trace, enabling [MLflow](/concepts/mlflow.md) to correctly render the span in the trace UI. The `gen_ai.operation.name` attribute follows the [OpenTelemetry GenAI Semantic Convention](https://opentelemetry.io/docs/specs/semconv/gen-ai/) and is the primary way to distinguish different kinds of operations—such as chat completions, embeddings, or tool calls—within a single trace. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Purpose

When you send [Traces](/concepts/traces.md) from a custom OpenTelemetry-instrumented application to Databricks [MLflow](/concepts/mlflow.md), each span must have a type label so [MLflow](/concepts/mlflow.md) can identify what kind of operation it represents. Without this label, the span displays as `UNKNOWN` in the [MLflow](/concepts/mlflow.md) UI. Setting `gen_ai.operation.name` on a span causes [MLflow](/concepts/mlflow.md) to map it to the corresponding [MLflow Span Types|MLflow span type](/concepts/mlflow-spans.md) and display the appropriate icon and label in the trace viewer. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## How to Set the Attribute

Set the attribute by calling `span.set_attribute("gen_ai.operation.name", "<value>")` on any span you want to label. The value must be one of the recognized operation names defined by the OpenTelemetry GenAI semantic convention. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
span.set_attribute("gen_ai.operation.name", "chat")
```

## Recognized Values

The following table lists the recognized values for `gen_ai.operation.name` and their corresponding [MLflow](/concepts/mlflow.md) span types. Set the attribute to one of these values to get the correct rendering in the [MLflow](/concepts/mlflow.md) UI.

| `gen_ai.operation.name` value | [MLflow](/concepts/mlflow.md) span type | Description |
|---|---|---|
| `chat` | Chat | A chat completion operation (e.g., a call to an LLM chat endpoint) |
| `embedding` | Embedding | An embedding generation operation |
| `tool` | Tool | A tool or function call operation |

*Note: The exact set of recognized values may expand as the OpenTelemetry GenAI semantic convention evolves. Consult the [OpenTelemetry GenAI Semantic Convention documentation](https://opentelemetry.io/docs/specs/semconv/gen-ai/) for the most up-to-date list.* ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Relationship to Other Span Attributes

The `gen_ai.operation.name` attribute is one of several OpenTelemetry GenAI attributes that [MLflow](/concepts/mlflow.md) reads from spans. It works alongside:

- `gen_ai.input.messages` and `gen_ai.output.messages` — for displaying request and response content
- `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` — for displaying token counts
- `gen_ai.request.model` — for identifying the model used

For the full set of supported attributes, see [Set OpenTelemetry Span Attributes for MLflow](/concepts/opentelemetry-mlflow-span-attribute-mapping.md). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Root Span vs. Child Spans

The `gen_ai.operation.name` attribute can be set on any span in the trace. However, [MLflow](/concepts/mlflow.md) reads certain attributes—such as token usage and session/user identifiers—specifically from the **root span** to populate the trace-level summary in the UI. Setting `gen_ai.operation.name` on the root span is recommended to ensure the trace itself has a meaningful type label. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Searching by Operation Name

After ingesting OTel [Traces](/concepts/traces.md) into [Unity Catalog](/concepts/unity-catalog.md), you can search for [Traces](/concepts/traces.md) by operation name using the `span.attributes.*` prefix in `mlflow.search_traces()`: ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

[[mlflow|MLflow]].set_experiment(experiment_id="<experiment-id>")

# Find [[traces|Traces]] by operation type
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.gen_ai.operation.name = 'chat'"
)
```

## Pre-built Integrations

If you use a pre-built integration such as Langfuse, that integration sets `gen_ai.operation.name` automatically. This page is intended for applications with custom OTel instrumentation that need to set the attribute manually. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Limitations

Custom OTel span attributes set with `span.set_attribute()` are not surfaced as [MLflow Trace Tags](/concepts/mlflow-trace-tags.md). Attributes you set outside the recognized OTel-to-MLflow mappings do not appear in the **Tags** column, the unified trace view, the `_traces_unified` [Unity Catalog](/concepts/unity-catalog.md) table, or the `tags` field returned by `mlflow.search_traces()`. They are preserved on the underlying span and remain visible in the **Attributes** tab of the [[mlflow-trace|MLflow Trace]] UI. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry Tracing — The framework for generating and collecting trace data
- [MLflow Span Types](/concepts/mlflow-spans.md) — The span type taxonomy used by [MLflow](/concepts/mlflow.md)
- [Set OpenTelemetry Span Attributes for MLflow](/concepts/opentelemetry-mlflow-span-attribute-mapping.md) — Complete guide to all supported OTel attributes
- mlflow.search_traces() API|Search Traces Programmatically — Querying [Traces](/concepts/traces.md) via the [MLflow](/concepts/mlflow.md) SDK
- [Unity Catalog](/concepts/unity-catalog.md) — The storage layer for ingested trace data
- Langfuse Integration — A pre-built integration that sets span attributes automatically

## Sources

- set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md

# Citations

1. [set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md](/references/set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws-8961c630.md)
