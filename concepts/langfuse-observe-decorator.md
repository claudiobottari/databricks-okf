---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf388dd5e17fc1a3e865aaefe735b6f8645b88b458f9c0e71dddccb6fa92189f
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - langfuse-observe-decorator
    - L@D
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Langfuse @observe() Decorator
description: Langfuse's function decorator that automatically creates OpenTelemetry trace spans for instrumented functions, which can be exported to any OTel-compatible backend.
tags:
  - tracing
  - langfuse
  - opentelemetry
  - instrumentation
timestamp: "2026-06-19T18:46:34.697Z"
---

# Langfuse `@observe()` Decorator

The **Langfuse `@observe()` decorator** is a Python decorator provided by the Langfuse SDK that instruments functions to generate OpenTelemetry (OTEL) trace spans. When configured with the appropriate environment variables, these spans can be redirected to any OTLP‑compatible backend—such as the Databricks MLflow OTLP endpoint—instead of being sent to the Langfuse server. This enables consolidated trace analysis alongside traces from other frameworks, and allows applying Unity Catalog governance to all traces. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Overview

The `@observe()` decorator wraps any function—typically an LLM call or a multi‑step pipeline—and automatically creates an OTEL span each time the function is invoked. By default, Langfuse requires the `LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, and `LANGFUSE_SECRET_KEY` environment variables to initialize its SDK. Setting these variables to dummy values disables the built‑in Langfuse server exporter, so only the custom OTLP exporter (attached to Langfuse’s internal `TracerProvider`) receives the spans. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Usage

### Basic Example

The decorator is applied directly to the function definition: ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
from langfuse import observe

@observe()
def my_llm_call(prompt: str) -> str:
    # Replace with your LLM logic (OpenAI, Anthropic, etc.)
    return f"Response to: {prompt}"

@observe()
def my_pipeline(user_input: str) -> str:
    result = my_llm_call(user_input)
    return result

my_pipeline("Hello, world!")
```

### Chaining Decorators

You can stack `@observe()` on multiple functions within a single pipeline. Each function call produces its own span, and the parent–child relationship between spans is preserved based on the call stack. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Configuration for Databricks Export

To send Langfuse traces to Databricks MLflow instead of the Langfuse server, follow these steps:

1. **Install packages** – Ensure `langfuse>=3.14.5`, `mlflow[databricks]>=3.10.0`, and the required OpenTelemetry packages (`opentelemetry-api`, `opentelemetry-sdk`, `opentelemetry-exporter-otlp-proto-http`) are installed. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
2. **Disable Langfuse server collection** – Set `LANGFUSE_HOST` to `"localhost"` and leave `LANGFUSE_PUBLIC_KEY` and `LANGFUSE_SECRET_KEY` empty. Alternatively, set `LANGFUSE_TRACING_ENABLED=False`. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
3. **Configure Databricks connection** – Retrieve the workspace host URL and an API token. In a Databricks notebook, use `dbutils.notebook.entry_point.getDbutils().notebook().getContext()`. Outside a notebook, set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables manually. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
4. **Link an experiment to Unity Catalog** – Use `mlflow.tracing.enablement.set_experiment_trace_location()` to define the Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) where traces will be stored. This returns a location object that contains the full OTEL spans table name. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
5. **Add the Databricks OTLP exporter** – Get the global `TracerProvider` (the one registered by Langfuse), create an `OTLPSpanExporter` pointing to the Databricks OTLP endpoint, and attach it as a `BatchSpanProcessor`. The exporter’s headers must include the `X-Databricks-UC-Table-Name` header set to the full table name from the trace location. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

After configuration, any function decorated with `@observe()` generates spans that are sent exclusively to Databricks, because Langfuse’s built‑in exporter is disabled. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Complete Setup Code

```python
# Step 2: Disable Langfuse trace collection
import os
os.environ["LANGFUSE_HOST"] = "localhost"
os.environ["LANGFUSE_PUBLIC_KEY"] = ""
os.environ["LANGFUSE_SECRET_KEY"] = ""

# Step 3: Configure Databricks connection (inside a notebook)
context = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
DATABRICKS_HOST = context.apiUrl().get().rstrip("/")
DATABRICKS_TOKEN = context.apiToken().get()

# Step 4: Link an experiment to Unity Catalog
import mlflow
from mlflow.entities import UCSchemaLocation
from mlflow.tracing.enablement import set_experiment_trace_location

CATALOG_NAME = "<UC_CATALOG_NAME>"
SCHEMA_NAME = "<UC_SCHEMA_NAME>"
EXPERIMENT_ID = "<EXPERIMENT_ID>"

trace_location = set_experiment_trace_location(
    location=UCSchemaLocation(catalog_name=CATALOG_NAME, schema_name=SCHEMA_NAME),
    experiment_id=EXPERIMENT_ID,
)

# Step 5: Add the Databricks OTLP exporter
from langfuse import get_client
from opentelemetry import trace as otel_trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

langfuse = get_client()
provider = otel_trace.get_tracer_provider()

databricks_exporter = OTLPSpanExporter(
    endpoint=f"{DATABRICKS_HOST}/api/2.0/otel/v1/traces",
    headers={
        "content-type": "application/x-protobuf",
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        "X-Databricks-UC-Table-Name": trace_location.full_otel_spans_table_name,
    },
)
provider.add_span_processor(BatchSpanProcessor(databricks_exporter))
```

## Viewing Traces

Once traces are ingested, open the MLflow experiment in your Databricks workspace and click the **Traces** tab. Traces from `@observe()`-decorated functions appear there and can be searched or filtered using OpenTelemetry span attributes. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry on Databricks – The preview feature that enables OTLP ingestion into MLflow
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The broader tracing infrastructure for GenAI workflows
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where trace data is stored
- Langfuse – The open-source observability platform for LLM applications
- OTLPSpanExporter – The OpenTelemetry exporter used to forward spans to Databricks
- MLflow set_experiment_trace_location API|set_experiment_trace_location() – The MLflow API to link an experiment to a Unity Catalog location

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
