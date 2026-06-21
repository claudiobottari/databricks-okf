---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a00f80b2983fc7b3b7518b803ebb864305a450841d4af21b8b1035eca0c5231
  pageDirectory: concepts
  sources:
    - migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-trace-location-configuration
    - METLC
  citations:
    - file: migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
title: MLflow Experiment Trace Location Configuration
description: The API and configuration pattern for setting a Unity Catalog trace location when creating or configuring an MLflow experiment, including catalog_name, schema_name, and table_prefix parameters
tags:
  - mlflow
  - configuration
  - tracing
timestamp: "2026-06-19T19:32:44.255Z"
---

## MLflow Experiment Trace Location Configuration

**MLflow Experiment Trace Location Configuration** determines how trace data (spans and annotations) is stored and organized in [Unity Catalog](/concepts/unity-catalog.md) when using MLflow's trace logging capabilities. An experiment's trace location can be configured to use either a schema-linked format (two-part path) or a table-prefix format (three-part path), with the table-prefix format being the recommended approach for all new and existing workloads. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Trace Location Formats

Experiments that store traces in Unity Catalog use one of two formats:

- **Schema-linked** (Beta release): The trace destination is a two-part path (`catalog.schema`). Trace data is stored in fixed-name tables like `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`. Tags, assessments, and metadata are stored as log events in the logs table. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]
- **Table-prefix** (Public Preview and later): The trace destination is a three-part path (`catalog.schema.table_prefix`). Trace data is stored in prefix-namespaced tables like `<table_prefix>_otel_spans`, and annotations have a dedicated table. This format provides faster time-range queries, richer attribute types, a dedicated annotations table, and support for multiple trace destinations per schema. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Configuring Trace Location

To create an experiment with a table-prefix trace location, use `mlflow.set_experiment()` with the `trace_location` parameter set to a `UnityCatalog` object specifying the catalog, schema, and table prefix:

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

The experiment ID is used to configure notebooks, jobs, or deployed models to log traces to the new destination. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Migrating from Schema-Linked to Table-Prefix Format

Databricks recommends migrating existing schema-linked experiments to the table-prefix format. The migration copies spans and annotations (tags, assessments, metadata) using Spark SQL and is performed with the `V1ToV2SqlMigration` utility from the `databricks-agents` Python package. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

#### Prerequisites

- A Unity Catalog-enabled workspace.
- A Databricks cluster running Databricks Runtime 15.3 or above.
- The `databricks-agents` package (version 1.10.0 or later): `pip install "databricks-agents>=1.10.0"`
- Permissions: `USE_CATALOG` and `USE_SCHEMA` on the source [Catalog and Schema](/concepts/catalog-and-schema.md); `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` on the destination [Catalog and Schema](/concepts/catalog-and-schema.md). ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

#### Migration Steps

1. **Create a destination experiment** with a table-prefix trace location as shown above.
2. **Stop all writes to the source experiment** before running the migration. Update notebooks, jobs, or deployed models to log traces to the new destination experiment. Any traces written to the source tables during migration might not be copied.
3. **Run the migration** in a Databricks notebook:

```python
from databricks.migrations.v1_to_v2 import V1ToV2SqlMigration

migration = V1ToV2SqlMigration(
    v1_source_schema="<source_catalog>.<source_schema>",
    v2_destination_prefix="<destination_catalog>.<destination_schema>.<table_prefix>",
)
migration.run()
```

The migration is idempotent — if it fails partway through (e.g., due to a cluster timeout), it can be safely rerun. Already-migrated rows are skipped automatically. Source tables are not modified and can be retained as a backup. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Identifying Experiments Using the Older Format

If your Unity Catalog schema contains tables named `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`, the experiment uses the older schema-linked format and is eligible for migration. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- TraceLocation
- Span
- Annotation

### Sources

- migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md

# Citations

1. [migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md](/references/migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws-4136e9d1.md)
