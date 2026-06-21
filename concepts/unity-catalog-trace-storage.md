---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16a30e7f154d4f2239419b513b39ab49b5edc36dff4907d8f923e6d59abf837a
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
    - store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-trace-storage
    - UCTS
    - unity-catalog-trace-storage-for-opentelemetry
    - UCTSFO
  citations:
    - file: store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Unity Catalog Trace Storage
description: Storing OpenTelemetry trace spans in Unity Catalog tables alongside MLflow traces, enabling SQL querying, access controls, lineage, and centralized governance.
tags:
  - tracing
  - unity-catalog
  - databricks
  - governance
timestamp: "2026-06-19T18:46:39.246Z"
---

# Unity Catalog Trace Storage

**Unity Catalog Trace Storage** is a Databricks capability that stores [OpenTelemetry (OTel)](/wiki/OpenTelemetry) traces in [Unity Catalog](/wiki/Unity-Catalog) tables rather than in the default MLflow control-plane experiment storage. This enables SQL querying, Unity Catalog governance, long-term retention, and consolidated trace analysis across multiple frameworks.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Benefits

Storing traces in Unity Catalog provides several advantages over experiment-only storage:

- **Access control** is managed through Unity Catalog schema and table permissions rather than experiment-level ACLs. Any user with access to the underlying Unity Catalog tables can view traces, regardless of which experiment they belong to.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **Trace IDs use URI format** instead of the `tr-<UUID>` format, improving compatibility with external systems.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **Large volumes of traces** can be stored in Delta tables for long-term retention and batch analysis.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **SQL querying** is supported directly via a Databricks SQL warehouse, enabling custom analytics and reporting.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **OTel format** ensures compatibility with other OpenTelemetry clients and tools.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **Consolidation** of traces from multiple sources — including third-party frameworks like Langfuse — into a single location for unified querying, governance, and analysis.^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Prerequisites

- A Unity Catalog-enabled workspace.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- The "OpenTelemetry on Databricks" preview enabled (along with "Variant Shredding for Optimized Read Performance on Semi-Structured Data"). See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- Permissions to create catalogs and schemas in Unity Catalog.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- A [Databricks SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/) with `CAN USE` permissions.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- Workspace in a [supported region](https://docs.databricks.com/aws/en/resources/feature-region-support).^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- MLflow Python library version 3.11 or later (`pip install mlflow[databricks]>=3.11.0`).^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Setup

To enable Unity Catalog trace storage, create an [MLflow Experiment](/concepts/mlflow-experiment.md) bound to a Unity Catalog trace location. This binds the experiment to a set of OTel tables that will hold the trace data.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Creating an experiment with a trace location

Use `mlflow.set_experiment()` with a `trace_location` parameter of type `UnityCatalog`:

```python
import mlflow
from mlflow.entities.trace_location import UnityCatalog

mlflow.set_tracking_uri("databricks")
os.environ["MLFLOW_TRACING_SQL_WAREHOUSE_ID"] = "<SQL_WAREHOUSE_ID>"

experiment = mlflow.set_experiment(
    experiment_name="/Users/user@company.com/traces",
    trace_location=UnityCatalog(
        catalog_name="main",
        schema_name="mlflow_traces",
        table_prefix="my_otel",  # defaults to experiment ID if omitted
    ),
)
```

^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

Alternatively, use `mlflow.create_experiment()` with the same `trace_location`; then call `mlflow.set_experiment()` to make it active. Once an experiment is bound to a Unity Catalog trace location, it cannot be reassigned to a different location. Multiple experiments can share the same trace location.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Tables created

After setup, four new Unity Catalog tables appear in the specified schema:^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

- `<table_prefix>_otel_annotations`
- `<table_prefix>_otel_logs`
- `<table_prefix>_otel_metrics`
- `<table_prefix>_otel_spans`

### Granting permissions

To read or write traces to the OTel tables, a user or service principal needs these [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md):^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

- `USE_CATALOG` on the catalog
- `USE_SCHEMA` on the schema
- `MODIFY` and `SELECT` on each of the `<table_prefix>_<type>` tables

> **Note:** `ALL_PRIVILEGES` is not sufficient — `MODIFY` and `SELECT` must be granted explicitly.

## Logging traces

Traces can be written to Unity Catalog tables from multiple sources:

### MLflow SDK

Use the `@mlflow.trace` decorator or [MLflow Tracing](/concepts/mlflow-tracing.md) APIs after setting the active experiment with its trace location. MLflow automatically routes traces to the bound Unity Catalog tables.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

```python
@mlflow.trace
def test(x):
    return x + 1

test(100)
```

### Model Serving endpoint

If your serving endpoint is linked to an experiment with a Unity Catalog trace location, the endpoint's traces are written to those tables.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Third-party OTel clients (including Langfuse)

You can configure any OpenTelemetry exporter to send spans to the Databricks OTLP endpoint. For example, Langfuse traces can be forwarded by attaching a `BatchSpanProcessor` with an `OTLPSpanExporter` pointing to `DATABRICKS_HOST/api/2.0/otel/v1/traces` and including the `X-Databricks-UC-Table-Name` header set to the trace location's full OTel spans table name.^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

The consolidated storage allows querying Langfuse-instrumented calls together with traces from other frameworks in a single place, applying Unity Catalog governance to all of them.^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Viewing traces in the UI

1. In your workspace, go to **Experiments**.
2. Find the experiment where traces are logged.
3. Click the **Traces** tab.
4. If traces are stored in Unity Catalog, select a SQL warehouse from the drop-down menu (Databricks retrieves traces using that warehouse).^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Production monitoring

[Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) works with traces stored in Unity Catalog, but requires configuring a SQL warehouse ID for the experiment. Use `mlflow.tracing.set_databricks_monitoring_sql_warehouse_id()` or set the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable before starting monitoring. Without this, monitoring jobs fail with a missing tag error.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

Required workspace-level permissions for monitoring:
- `CAN USE` on the SQL warehouse
- `CAN EDIT` on the MLflow experiment
- Permission on the monitoring job (automatically granted when the first scorer is registered)

The monitoring job runs under the identity of the user who first registered a scorer.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Limitations

- **Ingestion limits**: 200 traces per second per workspace and 100 MB per second per table. Contact your account team for higher limits.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **Reassignment**: An experiment can only be bound to a Unity Catalog trace location at creation time.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **Not supported with** [Knowledge Assistant](/concepts/agent-bricks-knowledge-assistant-incompatibility.md) or Supervisor Agent.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **Deleting individual traces** is not supported via the MLflow UI or API; you must delete rows directly from the underlying Unity Catalog tables using SQL.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- **MLflow MCP server** does not support interacting with traces stored in Unity Catalog.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- Traces cannot yet be written to a [Default Storage](/concepts/workspace-default-storage-path.md) catalog.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- Traces cannot yet be written to storage protected by Private Link.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]
- Enabling tracing on a serving endpoint may reduce throughput.^[store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- OpenTelemetry on Databricks
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- Langfuse Integration
- Databricks SQL Warehouses
- [Unity Catalog governance](/concepts/unity-catalog-governance.md)
- Databricks SQL Warehouse

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
- store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

# Citations

1. [store-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md](/references/store-opentelemetry-traces-in-unity-catalog-databricks-on-aws-758230eb.md)
2. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
