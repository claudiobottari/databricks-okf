---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4ab684500888d435fa08aaf50699608ccd03c2b981b0fca53e6f2461d04ce38
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-protocol-otlp-endpoint-in-databricks-mlflow
    - OP(EIDM
    - OpenTelemetry Protocol (OTLP)
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: OpenTelemetry Protocol (OTLP) Endpoint in Databricks MLflow
description: Databricks exposes an OTLP-compatible API at /api/2.0/otel/v1/traces that accepts OpenTelemetry spans and stores them in Unity Catalog tables.
tags:
  - opentelemetry
  - mlflow
  - databricks
  - api
timestamp: "2026-06-18T12:16:22.880Z"
---

# OpenTelemetry Protocol (OTLP) Endpoint in Databricks MLflow

The **OpenTelemetry Protocol (OTLP) Endpoint** in Databricks MLflow is an HTTP API that accepts OpenTelemetry trace spans and stores them in [Unity Catalog](/concepts/unity-catalog.md) tables. This endpoint enables any OpenTelemetry-compatible instrumented application, framework, or observability tool to send traces directly into Databricks without using the MLflow client library. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Endpoint Details

The OTLP endpoint accepts spans encoded with the OpenTelemetry Protocol (OTLP) over HTTP using protobuf serialization. Traces are stored in a Unity Catalog table that is linked to an [MLflow Experiment](/concepts/mlflow-experiment.md) via the `set_experiment_trace_location` API. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

| Property | Value |
|----------|-------|
| **URL** | `https://<workspace-host>/api/2.0/otel/v1/traces` |
| **Content-Type** | `application/x-protobuf` |
| **Authentication** | Bearer token (Databricks personal access token or OAuth token) |

### Required Headers

The following HTTP headers are mandatory: ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

| Header | Description |
|--------|-------------|
| `Authorization: Bearer <token>` | A valid Databricks API token with access to the target workspace. |
| `X-Databricks-UC-Table-Name` | The full name of the Unity Catalog table where spans should be stored (e.g., `catalog.schema.traces`). This table is created automatically when a trace location is set on an experiment. |

## How It Works

1. **Link an experiment to a Unity Catalog location** – Use `mlflow.tracing.enablement.set_experiment_trace_location()` to associate an experiment with a Unity Catalog schema. This returns a location object containing the fully qualified OTel spans table name. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

2. **Configure an OTLP exporter** – Create an `OTLPSpanExporter` pointing to the Databricks endpoint and include the authentication header and the `X-Databricks-UC-Table-Name` header. Exporters can be attached to any OpenTelemetry `TracerProvider`. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

3. **Send spans** – When spans are exported (e.g., via a `BatchSpanProcessor`), they are sent to the Databricks endpoint and persisted in the specified Unity Catalog table. Spans are then visible in the MLflow experiment’s **Traces** tab and queryable via Databricks SQL. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Requirements

- A Databricks workspace with the "OpenTelemetry on Databricks" preview enabled. See Manage Databricks Previews. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- A Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) where the traces table will reside.
- An MLflow experiment created in that workspace.
- Appropriate permissions to create experiments and write to Unity Catalog tables.

## Configuration Example

The following example demonstrates configuring an OTLP exporter to send spans from a Python application to the Databricks MLflow endpoint. This pattern is used when integrating with third-party instrumentation frameworks such as Langfuse. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities import UCSchemaLocation
from mlflow.tracing.enablement import set_experiment_trace_location
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Step 1: Link an experiment to a Unity Catalog schema
trace_location = set_experiment_trace_location(
    location=UCSchemaLocation(catalog_name="my_catalog", schema_name="my_schema"),
    experiment_id="123456789",
)

# Step 2: Create the exporter with the Databricks endpoint
databricks_exporter = OTLPSpanExporter(
    endpoint="https://<workspace-host>/api/2.0/otel/v1/traces",
    headers={
        "Authorization": "Bearer <token>",
        "X-Databricks-UC-Table-Name": trace_location.full_otel_spans_table_name,
    },
)

# Step 3: Attach the exporter to the global TracerProvider (or a custom provider)
from opentelemetry import trace as otel_trace
provider = otel_trace.get_tracer_provider()
provider.add_span_processor(BatchSpanProcessor(databricks_exporter))
```

## Benefits

- **Centralized observability** – Traces from multiple frameworks (Langfuse, OpenInference, custom instrumentation) are stored in one location alongside MLflow native traces. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- **Unity Catalog governance** – Apply access controls, lineage, and auditing to trace data using standard [Unity Catalog](/concepts/unity-catalog.md) features. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- **SQL-based analysis** – Query trace data at scale using Databricks SQL via a SQL warehouse. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The broader tracing subsystem in MLflow
- OpenTelemetry – The open standard for observability data
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit for runs and traces
- Langfuse Integration – Example of sending traces via OTLP endpoint
- Querying OTel Traces with SQL – Analyzing stored traces
- [Unity Catalog Governance for MLflow](/concepts/unity-catalog-governance-for-ml.md) – Applying governance to trace tables

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
