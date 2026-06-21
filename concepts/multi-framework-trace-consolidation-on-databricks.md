---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac78d732a81a2a8eef494363b1a5ae82fb72751bb7ff9c6e3659e6864a812044
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-framework-trace-consolidation-on-databricks
    - MTCOD
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Multi-Framework Trace Consolidation on Databricks
description: Architectural benefit of routing traces from Langfuse and other frameworks into a single Unity Catalog-backed storage, enabling unified querying, comparison, and governance.
tags:
  - databricks
  - observability
  - governance
  - mlflow
timestamp: "2026-06-18T12:16:52.748Z"
---

# Multi-Framework Trace Consolidation on Databricks

**Multi-Framework Trace Consolidation** refers to the practice of sending OpenTelemetry (OTel) trace spans from multiple instrumentation frameworks — such as Langfuse, OpenTelemetry-native SDKs, or other OTLP-compatible tools — to a single Databricks endpoint, where they are stored in [Unity Catalog](/concepts/unity-catalog.md) tables alongside native [MLflow](/concepts/mlflow.md) traces. This approach unifies observability data across different agent and LLM pipelines, enabling centralized querying, comparison, and governance. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Benefits

Consolidating traces on Databricks provides three main advantages: ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

- **Unified view** – Query and compare Langfuse-instrumented calls together with traces from other frameworks in a single place, without switching tools.
- **Scalable analytics** – Use Databricks SQL to analyze trace data at scale across all consolidated sources.
- **Unified governance** – Apply [Unity Catalog](/concepts/unity-catalog.md) access controls, lineage, and data classification to all traces, regardless of which framework generated them.

## How It Works

The consolidation uses the OpenTelemetry Protocol (OTLP). Each framework sends its trace spans to a Databricks OTLP endpoint (`/api/2.0/otel/v1/traces`). A custom HTTP header (`X-Databricks-UC-Table-Name`) routes the spans to a specific Unity Catalog table that is linked to an [MLflow Experiment](/concepts/mlflow-experiment.md) via the `set_experiment_trace_location` API. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

The following diagram (conceptual) illustrates the flow:

```
Langfuse SDK ──OTLP──┐
Other OTel SDKs ─────┤──> Databricks OTLP Endpoint ──> Unity Catalog Table
```

## Requirements

To use this consolidation, you need: ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

- A Databricks workspace with the **"OpenTelemetry on Databricks"** preview enabled (see [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews)).
- A new [MLflow Experiment](/concepts/mlflow-experiment.md).
- A Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) where trace tables will be created.

## Configuration Steps (Langfuse Example)

The following steps demonstrate the pattern using Langfuse as the source framework. The same approach applies to any OTLP-compatible tracer.

### 1. Install packages

```python
%pip install "langfuse>=3.14.5" "mlflow[databricks]>=3.10.0" opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
%restart_python
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### 2. Disable Langfuse server collection

Set dummy environment variables so Langfuse does not send traces to its own cloud. Only the OTLP exporter will receive the spans.

```python
import os
os.environ["LANGFUSE_HOST"] = "localhost"
os.environ["LANGFUSE_PUBLIC_KEY"] = ""
os.environ["LANGFUSE_SECRET_KEY"] = ""
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### 3. Configure Databricks connection

Retrieve the workspace host URL and API token (in a Databricks notebook, from `dbutils`).

```python
context = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
DATABRICKS_HOST = context.apiUrl().get().rstrip("/")
DATABRICKS_TOKEN = context.apiToken().get()
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### 4. Link an experiment to Unity Catalog

Use `set_experiment_trace_location` to define where traces will be stored.

```python
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
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### 5. Add the Databricks OTLP exporter

Attach an `OTLPSpanExporter` as a batch processor to the global TracerProvider that Langfuse registers.

```python
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

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### 6. Instrument and run traced code

Use Langfuse’s `@observe()` decorator to automatically generate OpenTelemetry spans that flow to Databricks.

```python
from langfuse import observe

@observe()
def my_llm_call(prompt: str) -> str:
    return f"Response to: {prompt}"

@observe()
def my_pipeline(user_input: str) -> str:
    return my_llm_call(user_input)

my_pipeline("Hello, world!")
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Viewing and Querying Traces

Once traces are ingested, they appear in the **Traces** tab of the associated MLflow experiment in the Databricks workspace UI. You can:

- Search and filter traces by OpenTelemetry span attributes. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- Query the stored trace data directly using Databricks SQL through a SQL warehouse. The data resides in a Unity Catalog table named according to the trace location. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Extending to Other Frameworks

The same OTLP-based pattern works for any framework that can export OpenTelemetry spans. Instead of initializing a Langfuse client, you configure the framework’s OpenTelemetry SDK to use the Databricks exporter with the correct endpoint and `X-Databricks-UC-Table-Name` header. This allows you to consolidate traces from OpenAI Agents SDK, LlamaIndex, custom Python code, and more — all alongside Langfuse and native MLflow traces.

## Related Concepts

- OpenTelemetry – The open standard for observability that underpins the consolidation.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The container that groups related traces and runs.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where trace tables are stored.
- OTLP – The protocol used to send span data to the Databricks endpoint.
- Databricks SQL – Used for querying consolidated trace data.
- [Trace Storage in Unity Catalog](/concepts/mlflow-trace-storage-in-unity-catalog.md) – Details on how trace tables are organized.
- Searching Traces by OTel Span Attributes – How to filter consolidated traces.

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
