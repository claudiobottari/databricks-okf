---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f11f1896f079404b5ee7608904981d37c43ec53df29f400c15dcd3d0b771ea6
  pageDirectory: concepts
  sources:
    - set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-mlflow-span-attribute-mapping
    - OMSAM
    - OpenTelemetry Span Attributes
    - OpenTelemetry Span Attributes for MLflow
    - OpenTelemetry span attributes
    - Set OpenTelemetry Span Attributes for MLflow
  citations:
    - file: set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
title: OpenTelemetry MLflow Span Attribute Mapping
description: How OpenTelemetry GenAI semantic convention attributes map to MLflow span types and UI rendering in Databricks managed MLflow.
tags:
  - open-telemetry
  - mlflow
  - observability
  - databricks
timestamp: "2026-06-19T23:03:36.918Z"
---

# OpenTelemetry [MLflow](/concepts/mlflow.md) Span Attribute Mapping

The **OpenTelemetry [MLflow](/concepts/mlflow.md) Span Attribute Mapping** defines how custom OpenTelemetry (OTel) span attributes are interpreted by Databricks [MLflow](/concepts/mlflow.md) to correctly render trace data in the [MLflow](/concepts/mlflow.md) UI. When you send [Traces](/concepts/traces.md) from a custom OTel-instrumented application to Databricks [MLflow](/concepts/mlflow.md), you must set specific attributes following the OpenTelemetry GenAI Semantic Conventions for [MLflow](/concepts/mlflow.md) to display span types, inputs, outputs, token usage, session identifiers, and user metadata. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

If you use a pre-built integration such as Langfuse, the integration sets these attributes automatically. This page is intended for applications with custom OTel instrumentation. The attribute mapping described here applies to **Databricks managed MLflow**; for open source (OSS) [MLflow](/concepts/mlflow.md), the attribute mapping differs (see the [OSS [MLflow](/concepts/mlflow.md) documentation](https://[MLflow](/concepts/mlflow.md).org/docs/latest/genai/tracing/opentelemetry/attribute-mapping/)). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Requirements

Before applying the attribute mapping, ensure you have:

- A Databricks workspace with the OTel tracing preview enabled.
- The OTLP Exporter configured to send [Traces](/concepts/traces.md) to your workspace (see [Log [Traces](/concepts/traces.md) to [Unity Catalog](/concepts/unity-catalog.md) tables](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog#log-traces-to-the-unity-catalog-tables)).
- An application instrumented with the OpenTelemetry SDK.

^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Attribute Mappings

### Span Type

Each span needs a type label that [MLflow](/concepts/mlflow.md) uses to identify the kind of operation. Set `gen_ai.operation.name` to one of the recognized values (e.g., `"chat"`, `"completion"`, `"embedding"`, `"agent"`, `"tool"`, `"retriever"`, or `"rerank"`). [MLflow](/concepts/mlflow.md) reads this attribute and displays the corresponding [MLflow Span Types|MLflow span type](/concepts/mlflow-spans.md) (e.g., `chat`) in the trace UI instead of `UNKNOWN`. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
span.set_attribute("gen_ai.operation.name", "chat")
```

### Inputs and Outputs

Set `gen_ai.input.messages` and `gen_ai.output.messages` on any span that should display request and response content. Setting these on the **root span** populates the trace-level request and response previews in the [MLflow](/concepts/mlflow.md) UI. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

Values can be **plain strings** or **JSON-serialized strings**. Using a JSON array of message objects with `role` and `content` fields enables richer rendering (e.g., labeled "User" and "Assistant" bubbles). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
import json

# Plain string
span.set_attribute("gen_ai.input.messages", "What is the weather today?")

# JSON message array
span.set_attribute("gen_ai.input.messages", json.dumps([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the weather today?"}
]))
span.set_attribute("gen_ai.output.messages", json.dumps([
    {"role": "assistant", "content": "It is sunny and 72°F in San Francisco."}
]))
```

### Token Usage

To display token counts in the UI trace summary, set `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` on the **root span**. [MLflow](/concepts/mlflow.md) reads these values from the root span because it aggregates counts at the trace level. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
root.set_attribute("gen_ai.usage.input_tokens", 150)
root.set_attribute("gen_ai.usage.output_tokens", 42)
```

### Session and User

To associate [Traces](/concepts/traces.md) with a specific MLflow Sessions|session or user, set `session.id` and `user.id` on any span. [MLflow](/concepts/mlflow.md) reads these attributes from the **root span** and displays them as trace-level metadata. Setting `session.id` enables the session tab in the [MLflow](/concepts/mlflow.md) UI. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
span.set_attribute("session.id", "conversation-123")
span.set_attribute("user.id", "user-456")
```

## Full Example: Instrument a Python Agent

The following example combines all four attribute categories in a simple agent with an LLM child span. It assumes the OTLP exporter is already configured. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

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
            llm.set_attribute("gen_ai.usage.input_tokens", 150)
            llm.set_attribute("gen_ai.usage.output_tokens", 42)

        # Root span – [[mlflow|MLflow]] reads inputs, outputs, tokens, and session/user
        root.set_attribute("gen_ai.operation.name", "chat")
        root.set_attribute("session.id", "conversation-123")
        root.set_attribute("user.id", "user-456")
        root.set_attribute("gen_ai.input.messages", json.dumps([
            {"role": "user", "content": query}
        ]))
        root.set_attribute("gen_ai.output.messages", json.dumps([
            {"role": "assistant", "content": response}
        ]))
        root.set_attribute("gen_ai.usage.input_tokens", 150)
        root.set_attribute("gen_ai.usage.output_tokens", 42)
        return response
```

## Verification in the [MLflow](/concepts/mlflow.md) UI

After running the instrumented code, open the [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) tab in your experiment. A correctly instrumented trace shows: ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

- **Span types**: Each span displays its type label (e.g., `chat`) instead of `UNKNOWN`.
- **Request and response**: The root span shows input and output messages.
- **Token usage**: The trace summary displays input, output, and total token counts.
- **Session and user**: The trace appears in the session tab under the specified session identifier; the user ID is visible in the [Trace Metadata](/concepts/trace-metadata.md).

## Searching for [Traces](/concepts/traces.md) by OTel Span Attributes

After ingesting OTel [Traces](/concepts/traces.md) into [Unity Catalog](/concepts/unity-catalog.md), use the `span.attributes.*` prefix in `mlflow.search_traces()` to filter by the OTel attribute values. The attribute name after the prefix is the same OTel attribute name used with `span.set_attribute()`. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].set_experiment(experiment_id="<experiment-id>")

# Find [[traces|Traces]] by session
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.session.id = 'conversation-123'"
)
# Find [[traces|Traces]] by user
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.user.id = 'user-456'"
)
# Find [[traces|Traces]] by model
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.gen_ai.request.model LIKE '%gpt%'"
)
# Find [[traces|Traces]] by operation type
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.gen_ai.operation.name = 'chat'"
)
# Find high-token [[traces|Traces]]
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.gen_ai.usage.input_tokens > 1000"
)
```

For the full `filter_string` syntax, see mlflow.search_traces() API|Search Traces Programmatically. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Limitations

Custom OTel span attributes set with `span.set_attribute()` outside the recognized OTel-to-MLflow mappings on this page are **not surfaced as [[mlflow-trace|MLflow Trace]] tags**. They do not appear in: ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

- The **Tags** column or the unified trace view in the [MLflow](/concepts/mlflow.md) UI.
- The `_traces_unified` [Unity Catalog](/concepts/unity-catalog.md) table.
- The `tags` field returned by `mlflow.search_traces()`.

These attributes are preserved on the underlying span. They remain visible in the **Attributes** tab of the [[mlflow-trace|MLflow Trace]] UI and are queryable through the `<prefix>_otel_spans.attributes` field of the OTel spans table. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

To attach searchable tags that appear in the unified trace view, use the MLflow Tag APIs instead. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- OpenTelemetry GenAI Semantic Conventions
- [MLflow Span Types](/concepts/mlflow-spans.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- OTLP Exporter
- Langfuse
- mlflow.search_traces() API|Search Traces Programmatically
- Attach Custom Tags and Metadata

## Sources

- set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md

# Citations

1. [set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md](/references/set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws-8961c630.md)
