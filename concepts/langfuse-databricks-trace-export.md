---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffcbf4d1f63ac93df58ca4ec8287ba8890ce6d994aef7fd9362653a08604b0fd
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - langfuse-databricks-trace-export
    - LTE
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Langfuse-Databricks Trace Export
description: Configuring Langfuse to route OpenTelemetry trace spans to the Databricks MLflow OTLP endpoint for storage and governance in Unity Catalog.
tags:
  - tracing
  - observability
  - databricks
  - langfuse
timestamp: "2026-06-19T18:47:06.080Z"
---

# Langfuse-Databricks Trace Export

**Langfuse-Databricks Trace Export** is a configuration pattern that allows Langfuse-instrumented applications to send OpenTelemetry-based trace spans to the Databricks [MLflow](/concepts/mlflow.md) OTLP endpoint. This enables Langfuse traces to be stored in [Unity Catalog](/concepts/unity-catalog.md) tables alongside other MLflow traces, consolidating observability data in a single governed location on Databricks. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Overview

By exporting Langfuse traces to Databricks, organizations gain several benefits. Traces from Langfuse-instrumented calls can be queried and compared alongside traces from other frameworks in a single place. Databricks SQL can be used to analyze trace data at scale. All traces inherit [Unity Catalog](/concepts/unity-catalog.md) governance features such as access controls and lineage. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

The core mechanism works by attaching a Databricks [OpenTelemetry Protocol (OTLP)](/concepts/opentelemetry-protocol-otlp-endpoint-in-databricks-mlflow.md) exporter to the Langfuse SDK's internal tracer provider. Langfuse's environment variables are set to dummy values so that no spans are sent to Langfuse's own servers — instead, all spans flow exclusively to the Databricks endpoint. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Prerequisites

- A Databricks workspace with the "OpenTelemetry on Databricks" preview enabled. See Databricks Preview Management. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- A new [MLflow Experiment](/concepts/mlflow-experiment.md) to receive the traces. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Setup Process

### Installing Required Packages

The Langfuse SDK (version 3.14.5 or later), MLflow with Databricks support (version 3.10.0 or later), and OpenTelemetry packages must be installed. In a Databricks notebook, use `%pip install` with the required libraries and restart Python afterward. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
%pip install "langfuse>=3.14.5" "mlflow[databricks]>=3.10.0" opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
%restart_python
```

### Disabling Langfuse Trace Collection

Langfuse requires `LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, and `LANGFUSE_SECRET_KEY` environment variables to initialize its SDK. These should be set to dummy values to prevent traces from being sent to a Langfuse server. Only the OTLP exporter configured in the next step will receive the spans. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
import os
os.environ["LANGFUSE_HOST"] = "localhost"
os.environ["LANGFUSE_PUBLIC_KEY"] = ""
os.environ["LANGFUSE_SECRET_KEY"] = ""
```

An alternative is to set `LANGFUSE_TRACING_ENABLED=False` to disable Langfuse's built-in trace collection. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Configuring the Databricks Connection

When running inside a Databricks notebook, the workspace host URL and API token can be retrieved from the notebook context using `dbutils`. Outside a notebook, these should be set as environment variables manually. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Linking an Experiment to Unity Catalog

A Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) must be defined, then linked to an MLflow experiment using `set_experiment_trace_location`. This tells Databricks where to store incoming traces. The function `mlflow.tracing.enablement.set_experiment_trace_location` accepts a `UCSchemaLocation` and an experiment ID. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
from mlflow.entities import UCSchemaLocation
from mlflow.tracing.enablement import set_experiment_trace_location

trace_location = set_experiment_trace_location(
    location=UCSchemaLocation(catalog_name=CATALOG_NAME, schema_name=SCHEMA_NAME),
    experiment_id=EXPERIMENT_ID,
)
```

### Attaching the Databricks OTLP Exporter

The Langfuse client registers its own TracerProvider as the global OpenTelemetry tracer provider. This provider can be retrieved and a `BatchSpanProcessor` with an OTLPSpanExporter attached, pointing to the Databricks MLflow endpoint. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

The OTLP exporter uses three custom headers: the `X-Databricks-UC-Table-Name` header routes incoming spans to the Unity Catalog table defined by the trace location, while `Authorization` and `content-type` are standard protocol headers. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

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

Because the Langfuse environment variables are set to dummy values, this processor is the only active exporter, so all spans are sent exclusively to Databricks. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Instrumenting Functions

Langfuse's `@observe()` decorator is used to instrument functions. The decorator creates OpenTelemetry spans that the exporter sends to Databricks. Any function — whether it calls an LLM or performs other logic — can be traced. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
from langfuse import observe

@observe()
def my_llm_call(prompt: str) -> str:
    return f"Response to: {prompt}"

@observe()
def my_pipeline(user_input: str) -> str:
    result = my_llm_call(user_input)
    return result

my_pipeline("Hello, world!")
```

## Viewing Traces

Traces appear in the MLflow experiment's **Traces** tab in the Databricks workspace. From there, users can search, filter, and analyze the captured telemetry data. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader framework for capturing and storing traces in MLflow.
- [OpenTelemetry Protocol (OTLP)](/concepts/opentelemetry-protocol-otlp-endpoint-in-databricks-mlflow.md) — The standard protocol used for exporting telemetry data.
- Langfuse Integration with MLflow — Overview of Langfuse compatibility with the MLflow ecosystem.
- [Storing OpenTelemetry Traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md) — The underlying storage mechanism for ingested spans.
- Querying Traces with Databricks SQL — Using SQL to analyze trace data at scale.
- Searching Traces by OTel Span Attributes — Finding specific traces based on span metadata.

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
