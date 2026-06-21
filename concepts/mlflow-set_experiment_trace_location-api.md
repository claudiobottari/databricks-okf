---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af3b7d62df3c1dc9926b1494893405d6d0e891cd3ee71ede9cd274edbf1c545f
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-set_experiment_trace_location-api
    - MSA
    - set_experiment_trace_location
    - set_experiment_trace_location()
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: MLflow set_experiment_trace_location API
description: An MLflow API that links a Unity Catalog schema location to an MLflow experiment, defining where incoming OTLP spans will be stored as trace tables.
tags:
  - mlflow
  - databricks
  - api
timestamp: "2026-06-19T10:27:50.417Z"
---

# MLflow `set_experiment_trace_location` API

The **`set_experiment_trace_location`** API configures a [MLflow Experiment](/concepts/mlflow-experiment.md) to store OpenTelemetry traces in a specific [Unity Catalog](/concepts/unity-catalog.md) schema. It is used when ingesting traces from external systems (e.g., Langfuse) so that all spans are persisted to a Unity Catalog table, enabling governance, SQL querying, and unified trace visibility. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## API Signature

```python
from mlflow.tracing.enablement import set_experiment_trace_location
```

The function takes two arguments: a `location` object that defines the Unity Catalog schema, and an `experiment_id` identifying the target MLflow experiment. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `location` | `mlflow.entities.UCSchemaLocation` | Specifies the Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) where trace data will be stored. |
| `experiment_id` | `str` | The ID of the MLflow experiment to associate with this trace location. |

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Return Value

The function returns a trace location object that contains a `full_otel_spans_table_name` attribute. This attribute gives the fully qualified name of the Unity Catalog table (e.g., `catalog.schema.spans`) where OpenTelemetry spans will be written. The table name is used as the value of the `X-Databricks-UC-Table-Name` header when configuring an OTLP exporter. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Usage Example

The following example links an experiment to a Unity Catalog schema and retrieves the table name for later use in an OTLP exporter:

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

# trace_location.full_otel_spans_table_name contains the full table path
# e.g., "catalog.schema.spans"
```

^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Related Concepts

- OTLP Span Exporter – How to configure the exporter that sends spans to Databricks using the table name from `set_experiment_trace_location`.
- [Unity Catalog tables for traces](/concepts/unity-catalog-delta-tables-for-trace-storage.md) – The underlying storage for ingested OpenTelemetry data.
- Langfuse integration – An end-to-end example that uses this API to redirect Langfuse traces to Databricks.
- [MLflow experiment trace storage](/concepts/mlflow-experiment-as-trace-storage-backend.md) – General documentation on storing traces in Unity Catalog.

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
