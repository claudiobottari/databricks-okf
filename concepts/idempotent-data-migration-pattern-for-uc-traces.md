---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5e235f7327fa50fc5382d5c434efc2490851b74fa935520f365f827b3885035
  pageDirectory: concepts
  sources:
    - migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-data-migration-pattern-for-uc-traces
    - IDMPFUT
  citations:
    - file: migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
title: Idempotent Data Migration Pattern for UC Traces
description: "Design pattern for migrating trace data between UC table formats where the migration is idempotent: already-migrated rows are skipped on rerun, making it resilient to partial failures like cluster timeouts"
tags:
  - migration
  - reliability
  - data-engineering
timestamp: "2026-06-19T19:32:53.376Z"
---

# Idempotent Data Migration Pattern for UC Traces

The **Idempotent Data Migration Pattern for UC Traces** is a migration strategy used to move [MLflow](/concepts/mlflow.md) trace data from the older schema-linked Unity Catalog format (`catalog.schema`) to the newer table-prefix format (`catalog.schema.table_prefix`). The pattern ensures that the migration can be safely retried without causing duplicate or corrupted data, making it resilient to partial failures such as cluster timeouts. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Background

During the Beta release of Unity Catalog trace storage, MLflow experiments used a **schema-linked** format where the trace destination was a two-part path (`catalog.schema`). Trace data was stored in fixed-name tables such as `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`, with tags, assessments, and metadata stored as log events in the logs table. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

The Public Preview release introduced a **table-prefix** format where the trace destination uses a three-part path (`catalog.schema.table_prefix`). This format provides faster time-range queries, richer attribute types, a dedicated annotations table, and support for multiple trace destinations per schema. Databricks recommends this format for all new and existing UC trace workloads. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Idempotency Behavior

The migration is designed to be **idempotent** — if it fails partway through (for example, due to a cluster timeout), you can safely rerun it. Already-migrated rows are skipped automatically, preventing duplicate entries in the destination tables. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Migration Process

### Prerequisites

- A Unity Catalog-enabled workspace
- A Databricks cluster running Databricks Runtime 15.3 or above
- The `databricks-agents` Python package (version 1.10.0 or later)
- Appropriate permissions: `USE_CATALOG` and `USE_SCHEMA` on the source [Catalog and Schema](/concepts/catalog-and-schema.md); `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` on the destination [Catalog and Schema](/concepts/catalog-and-schema.md) ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Step 1: Create a Destination Experiment

Create an experiment linked to a Unity Catalog table-prefix location using `mlflow.set_experiment()` with a `trace_location` parameter of type `UnityCatalog`. This is where migrated traces will be stored. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

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
print(f"Experiment ID: {experiment.experiment_id}")
```

### Step 2: Switch Trace Logging

Update notebooks, jobs, or deployed models to log traces to the new experiment. All writes to the source experiment should be stopped before running the migration — any traces written to the source tables during migration might not be copied. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Step 3: Run the Migration

Execute the migration using the `V1ToV2SqlMigration` class from the `databricks.migrations` module: ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

```python
from databricks.migrations.v1_to_v2 import V1ToV2SqlMigration

migration = V1ToV2SqlMigration(
    v1_source_schema="<source_catalog>.<source_schema>",
    v2_destination_prefix="<destination_catalog>.<destination_schema>.<table_prefix>",
)
migration.run()
```

The migration copies spans and annotations (tags, assessments, metadata) using Spark SQL. The source tables are not modified by the migration and can be retained as a backup. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Identifying Experiments Using the Older Format

Experiments that use the schema-linked format can be identified by checking if the Unity Catalog schema contains tables named `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure for MLflow experiments
- [Unity Catalog Trace Location](/concepts/unity-catalog-trace-location.md) — Configuration for storing traces in Unity Catalog
- [Idempotent Operations](/concepts/idempotent-trace-migration.md) — The general concept of operations that can be safely retried
- Data Migration Patterns — Broader strategies for moving data between systems
- Spark SQL — The engine used for copying migration data

## Sources

- migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md

# Citations

1. [migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md](/references/migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws-4136e9d1.md)
