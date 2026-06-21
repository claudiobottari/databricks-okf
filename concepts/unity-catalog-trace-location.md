---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c17752c2d48a45e57821da6494b52396322092741c7870cbe422baf915c26dda
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
    - migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
  confidence: 0.97
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-trace-location
    - UCTL
    - Unity Catalog External Locations
  citations:
    - file: migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Unity Catalog Trace Location
description: Mechanism to link an MLflow experiment to a Unity Catalog catalog and schema using set_experiment_trace_location(), which determines where ingested OTLP spans are stored as tables.
tags:
  - unity-catalog
  - mlflow
  - databricks
  - governance
timestamp: "2026-06-18T12:16:21.284Z"
---

# Unity Catalog Trace Location

A **Unity Catalog Trace Location** is a configuration that binds an MLflow experiment to a set of Delta tables in Unity Catalog where OpenTelemetry traces, spans, annotations, logs, and metrics are stored. By using a trace location, you remove the trace storage limits of workspace-level experiments and enable Unity Catalog governance, fine-grained access controls, and the ability to query traces via Databricks SQL, notebooks, Genie, AI/BI dashboards, and any Spark-based tool.^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Structure

A trace location is defined as a three‑part Unity Catalog path: `catalog.schema.table_prefix`. When an experiment is linked to a trace location, MLflow automatically creates four Delta tables under that prefix:^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

| Table name (derived from prefix) | Contents |
|--------------------------------|----------|
| `<table_prefix>_otel_spans`    | OpenTelemetry span data |
| `<table_prefix>_otel_annotations` | Annotations (assessments, tags) |
| `<table_prefix>_otel_logs`     | Log records |
| `<table_prefix>_otel_metrics`  | Metric data |

The exact table names are accessible via the trace location object’s `full_otel_spans_table_name` property, which can be used as the value of the `X-Databricks-UC-Table-Name` header when sending traces via the OTLP exporter.^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Creating a Trace Location

You can create a trace location at experiment creation time using Mlflow’s `set_experiment` with a `trace_location` parameter, or after experiment creation using `set_experiment_trace_location`.

### Using `set_experiment`

This approach is used when creating a new destination experiment for trace migration. The `UnityCatalog` class accepts `catalog_name`, `schema_name`, and `table_prefix`:^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities.trace_location import UnityCatalog

experiment = mlflow.set_experiment(
    experiment_name="/Workspace/Users/<user>/<experiment_name>",
    trace_location=UnityCatalog(
        catalog_name="<destination_catalog>",
        schema_name="<destination_schema>",
        table_prefix="<table_prefix>",
    ),
)
print(f"Destination experiment ID: {experiment.experiment_id}")
```

### Using `set_experiment_trace_location`

This API links an existing experiment to a Unity Catalog location. It accepts a `UCSchemaLocation` (which requires `catalog_name` and `schema_name`) and an `experiment_id`:^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities import UCSchemaLocation
from mlflow.tracing.enablement import set_experiment_trace_location

trace_location = set_experiment_trace_location(
    location=UCSchemaLocation(catalog_name=CATALOG_NAME, schema_name=SCHEMA_NAME),
    experiment_id=EXPERIMENT_ID,
)
```

The returned `trace_location` object provides the `full_otel_spans_table_name` property for use in OTLP exporters.^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Benefits

- **No trace storage limits** — traces are stored in Unity Catalog Delta tables instead of the workspace metadata store.^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]
- **Unity Catalog governance** — apply access controls, lineage, and other governance features to all trace data.^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- **Query at scale** — trace data can be queried with Databricks SQL, Genie, AI/BI dashboards, notebooks, and Spark.^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]
- **Consolidation** — traces from multiple frameworks (Langfuse, custom OTel instrumentations, etc.) can be stored together in the same experiment.^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Usage in External Frameworks

When sending traces from an external framework (e.g., Langfuse) to Databricks, you configure an OTLP exporter to point to the Databricks endpoint and include the `X-Databricks-UC-Table-Name` header set to the trace location’s full OTEL spans table name. This routes the spans directly to the correct Unity Catalog tables.^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Migration of Existing Traces

If you have existing traces in a workspace-level experiment, you can migrate them to a new Unity Catalog trace location. The migration copies traces, spans, assessments, tags, and metadata (excluding archived/deleted traces, dataset records, labeling sessions, and runs) leaving the source experiment unchanged.^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

- A Unity Catalog‑enabled workspace.^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]
- The `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md).^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]
- For migration, a cluster running Databricks Runtime 15.3 or above and the `databricks-agents` package (version 1.10.1 or later).^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md) — The parent entity that a trace location is bound to.
- OpenTelemetry Tracing — The standard for trace data stored in Unity Catalog tables.
- [MLflow Tracing API](/concepts/mlflow-tracing.md) — The API for logging and querying traces.
- Export Langfuse Traces — How to configure Langfuse to send traces to a Unity Catalog trace location.
- Migrate Experiment Traces to Unity Catalog — Process for moving existing traces to a trace location.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer providing storage and access control for traces.
- [Delta Tables](/concepts/delta-lake-table.md) — The underlying storage format for trace data.
- [Governed Tags](/concepts/governed-tags.md) — Tags that can be applied to trace‑related securable objects.

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
- migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md](/references/migrate-experiment-traces-to-unity-catalog-databricks-on-aws-a625531c.md)
2. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
