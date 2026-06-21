---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0e83a23de7a7d78e968d3075f2a6794566c70d63562cb368ee148d81436ba27
  pageDirectory: concepts
  sources:
    - set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-level-inputoutput-rendering-in-mlflow
    - TIRIM
  citations:
    - file: set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
title: Trace-level Input/Output Rendering in MLflow
description: Using gen_ai.input.messages and gen_ai.output.messages attributes with JSON-serialized message arrays for rich UI rendering with role-labeled bubbles.
tags:
  - open-telemetry
  - mlflow
  - tracing
  - ui-rendering
timestamp: "2026-06-19T23:03:45.052Z"
---

# Trace-level Input/Output Rendering in [MLflow](/concepts/mlflow.md)

**Trace-level Input/Output Rendering in MLflow** refers to how the [MLflow](/concepts/mlflow.md) UI displays the request and response payloads of a trace, showing the inputs sent to and outputs received from a model or agent. This rendering is controlled by specific [OpenTelemetry (OTel)](/concepts/opentelemetry-compatibility.md) span attributes set during instrumentation.

## Overview

When [Traces](/concepts/traces.md) are ingested into Databricks [MLflow](/concepts/mlflow.md), the UI renders input/output data at both the trace level and the individual span level. The trace-level request and response previews are populated by setting the `gen_ai.input.messages` and `gen_ai.output.messages` attributes on the **root span** of the trace. These attributes can be plain strings or JSON-serialized arrays of message objects with `role` and `content` fields. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

Using JSON message arrays enables richer rendering in the [MLflow](/concepts/mlflow.md) UI, including labeled "User" and "Assistant" bubbles that improve readability of conversational [Traces](/concepts/traces.md). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Setting Input and Output Attributes

The attributes `gen_ai.input.messages` and `gen_ai.output.messages` should be set on each span that should display inputs and outputs. For trace-level rendering, they must be set on the **root span** specifically. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### Plain String Example

```python
span.set_attribute("gen_ai.input.messages", "What is the weather today?")
```

This displays the string as-is in the UI. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### JSON Message Array Example

```python
import json

span.set_attribute("gen_ai.input.messages", json.dumps([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the weather today?"}
]))

span.set_attribute("gen_ai.output.messages", json.dumps([
    {"role": "assistant", "content": "It is sunny and 72°F in San Francisco."}
]))
```

This renders with role labels in the [MLflow](/concepts/mlflow.md) UI, with "User" and "Assistant" bubbles for each message. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## How Rendering Works in the UI

When a correctly instrumented trace is viewed in the [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) tab:

- The root span shows the **input messages** and **output messages** in the trace summary
- Each individual span displays its own input/output data in the span detail panel
- The trace-level preview provides a quick overview of the entire interaction without needing to expand individual spans

This rendering is controlled by the `gen_ai.operation.name` attribute, which determines the [MLflow span type](/concepts/mlflow-spans.md) displayed in the UI. For chat-oriented [Traces](/concepts/traces.md), setting `gen_ai.operation.name` to `"chat"` provides appropriate rendering. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Requirements

To use trace-level input/output rendering, you must:

1. Have a Databricks workspace with the OTel tracing preview enabled
2. Configure the OTLP exporter to send [Traces](/concepts/traces.md) to your workspace (see [Log traces to Unity Catalog tables](/concepts/model-traces-in-unity-catalog.md))
3. Have an application instrumented with the OpenTelemetry SDK

If you use a pre-built integration such as Langfuse, that integration sets these attributes automatically. The custom instrumentation path is only needed for applications with custom OTel instrumentation. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry GenAI Semantic Conventions – The standard attributes used for trace instrumentation
- MLflow span types – The type labels that determine UI rendering behavior
- Setting OpenTelemetry span attributes for MLflow – Full guide on all OTel attributes supported in [MLflow](/concepts/mlflow.md)
- [Token usage display in MLflow traces](/concepts/token-usage-in-mlflow-traces.md) – Display of input/output token counts alongside messages
- [Session and User Association in MLflow Traces](/concepts/session-and-user-association-in-mlflow-traces.md) – Associating [Traces](/concepts/traces.md) with specific sessions and users

## Sources

- set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md

# Citations

1. [set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md](/references/set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws-8961c630.md)
