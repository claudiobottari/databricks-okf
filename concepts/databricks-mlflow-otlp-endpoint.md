---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 498f5e18a6609349147fd566625b23c320cfa2afd6bb3fc67d39f2273e5497e2
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-otlp-endpoint
    - DMOE
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Databricks MLflow OTLP Endpoint
description: A Databricks REST API endpoint at /api/2.0/otel/v1/traces that ingests OpenTelemetry Protocol (OTLP) spans and routes them to a specified Unity Catalog table via the X-Databricks-UC-Table-Name header.
tags:
  - databricks
  - otel
  - api
timestamp: "2026-06-19T10:27:47.183Z"
---

# Databricks MLflow OTLP Endpoint

The **Databricks MLflow OTLP Endpoint** is an OpenTelemetry Protocol (OTLP) endpoint provided by Databricks that enables ingestion of OpenTelemetry trace spans from external frameworks — such as Langfuse — directly into Databricks MLflow. This endpoint allows traces to be stored in [Unity Catalog](/concepts/unity-catalog.md) tables alongside native MLflow traces, providing a unified observability platform for AI applications. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Overview

The OTLP endpoint acts as a bridge between the OpenTelemetry ecosystem and Databricks. By sending spans to `{DATABRICKS_HOST}/api/2.0/otel/v1/traces`, users can consolidate traces from various instrumentation sources into a single location. This approach eliminates the need to maintain separate tracing backends for different frameworks. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Benefits

Consolidating traces through the Databricks MLflow OTLP endpoint provides several advantages:

- **Unified observability**: Query and compare traces from Langfuse and other frameworks in a single place. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- **Scalable analysis**: Use Databricks SQL to analyze trace data at scale. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- **Unified governance**: Apply [Unity Catalog](/concepts/unity-catalog.md) governance controls — such as access policies and lineage — to all traces. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Requirements

To use the OTLP endpoint, the following prerequisites must be met:

- A Databricks workspace with the "OpenTelemetry on Databricks" preview enabled (see Manage Databricks previews). ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- A new [MLflow Experiment](/concepts/mlflow-experiment.md). ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## How It Works

### 1. Configure the OTLP Exporter

The OTLP exporter is configured using the OpenTelemetry SDK. It sends spans to the Databricks endpoint with the following components: ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

| Component | Description |
|-----------|-------------|
| `endpoint` | `{DATABRICKS_HOST}/api/2.0/otel/v1/traces` |
| `content-type` | `application/x-protobuf` |
| `Authorization` | Bearer token for Databricks authentication |
| `X-Databricks-UC-Table-Name` | Header that routes spans to the correct Unity Catalog table |

### 2. Set the Trace Location

Before sending spans, the trace location must be configured using `set_experiment_trace_location()`. This tells Databricks where to store incoming traces by linking an MLflow experiment to a Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md): ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities import UCSchemaLocation
from mlflow.tracing.enablement import set_experiment_trace_location

trace_location = set_experiment_trace_location(
    location=UCSchemaLocation(catalog_name=CATALOG_NAME, schema_name=SCHEMA_NAME),
    experiment_id=EXPERIMENT_ID,
)
```

### 3. Attach the Exporter to a Tracer Provider

The exporter is attached as a BatchSpanProcessor to an OpenTelemetry TracerProvider. This ensures that spans created by the instrumented framework are forwarded to Databricks alongside any existing processing pipeline. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

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

## Integration with Langfuse

When integrating with Langfuse:

1. Langfuse registers its own TracerProvider as the global OpenTelemetry TracerProvider. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
2. The Databricks OTLP exporter is attached to this provider as an additional span processor. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
3. Langfuse's environment variables (`LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`) are set to dummy values to prevent traces from being sent to an external Langfuse server. Alternatively, `LANGFUSE_TRACING_ENABLED=False` can be used to disable Langfuse's own trace collection. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

This configuration ensures that all OpenTelemetry spans created by Langfuse's `@observe()` decorator are sent exclusively to Databricks. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Viewing Traces

After spans are ingested, they can be viewed by opening the linked MLflow experiment and clicking the **Traces** tab. Users can then: ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

- Search and filter traces in the MLflow UI.
- Query trace data directly using SQL through a Databricks SQL warehouse.
- Search for ingested traces by [OpenTelemetry span attributes](/concepts/opentelemetry-mlflow-span-attribute-mapping.md).

## Related Concepts

- OpenTelemetry Tracing — The open standard for observability data
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Trace management within MLflow
- [Trace Storage in Unity Catalog](/concepts/mlflow-trace-storage-in-unity-catalog.md) — Storing and managing traces in Unity Catalog tables
- Langfuse Integration — Using Langfuse with Databricks
- OTLP Protocol — The OpenTelemetry Protocol for exporting telemetry data
- Span Processors — Components that handle span export in the OpenTelemetry SDK

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
