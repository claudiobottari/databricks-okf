---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 141f4b48ca5ee0974c6a259bdc6797aa266637d9d55ecf600f18c848c483ac1c
  pageDirectory: concepts
  sources:
    - migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-storage-in-unity-catalog
    - MTSIUC
    - MLflow Traces in Unity Catalog
    - Trace Storage in Unity Catalog
    - MLflow trace-to-Unity Catalog binding
  citations:
    - file: migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
title: MLflow Trace Storage in Unity Catalog
description: Mechanism for storing MLflow AI/agent traces in Unity Catalog tables, supporting structured querying, annotations, and multiple trace destinations per schema
tags:
  - mlflow
  - unity-catalog
  - tracing
  - genai
timestamp: "2026-06-19T19:32:42.666Z"
---

# MLflow Trace Storage in Unity Catalog

**MLflow Trace Storage in Unity Catalog** refers to the mechanism by which [MLflow] experiment traces – spans and annotations (tags, assessments, metadata) – are persisted in [Unity Catalog] tables. Two table formats exist: a Beta-era “schema-linked” format and the current “table-prefix” format introduced with Public Preview.

## Formats

### Schema-linked (Beta)

Experiments configured during the Beta release store traces in a fixed set of tables whose names are not configurable. The trace destination is a two‑part path (`catalog.schema`), and data resides in tables named `mlflow_experiment_trace_otel_spans` (spans) and `mlflow_experiment_trace_otel_logs` (logs). Tags, assessments, and metadata are all stored as log events in the logs table. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Table-prefix (Public Preview / latest)

The table‑prefix format uses a three‑part destination path (`catalog.schema.table_prefix`). Trace data is stored in prefix‑namespaced tables, for example `<table_prefix>_otel_spans`. A dedicated annotations table is created separately from the logs table. This format provides several advantages:
- Faster time‑range queries due to an improved table structure.
- Support for richer attribute types.
- A dedicated table for annotations, separate from log events.
- Ability to store traces for multiple experiments or destinations within a single schema (by using different table prefixes).  
^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

Databricks recommends the table‑prefix format for all new and existing Unity Catalog trace workloads. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Identifying the Used Format

To determine which format an experiment uses, inspect its Unity Catalog schema. If the schema contains tables named `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`, the experiment is using the older schema‑linked format and is eligible for migration. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Migration to the Table‑Prefix Format

A migration utility, `V1ToV2SqlMigration`, copies spans and annotations from schema‑linked tables to table‑prefix tables using Spark SQL. The migration is idempotent: if it fails partway through (e.g., due to a cluster timeout), it can be safely rerun, and already‑migrated rows are skipped. The source tables are not modified by the migration and can be retained as a backup. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Prerequisites

- A Unity Catalog‑enabled workspace.
- A cluster running Databricks Runtime **15.3 or above**.
- The `databricks-agents` Python package installed (`pip install "databricks-agents>=1.10.0"`).
- Permissions: `USE_CATALOG` and `USE_SCHEMA` on the source [Catalog and Schema](/concepts/catalog-and-schema.md); `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` on the destination [Catalog and Schema](/concepts/catalog-and-schema.md).  
^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Migration Steps

1. **Create a destination experiment** that uses a table‑prefix trace location. Save its experiment ID to configure future tracing.  
   ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

2. **Switch trace logging** to the new experiment. Stop all writes to the source experiment before running the migration to ensure consistency. Verifying that no notebooks, jobs, or deployed models are actively logging traces to the source experiment is recommended. (A dry run can be performed by skipping this step.)  
   ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

3. **Run the migration** in a Databricks notebook:  
   ```python
   from databricks.migrations.v1_to_v2 import V1ToV2SqlMigration
   migration = V1ToV2SqlMigration(
       v1_source_schema="<source_catalog>.<source_schema>",
       v2_destination_prefix="<destination_catalog>.<destination_schema>.<table_prefix>",
   )
   migration.run()
   ```
   Placeholders should match the source schema and the destination prefix configured in Step 1.  
   ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

After migration, traces are available in the new destination experiment. The source tables remain untouched and can serve as a backup. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit that owns trace destinations.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer used for trace storage.
- [GenAI Tracing](/concepts/mlflow-genai-tracing.md) – The broader MLflow capability for tracing generative AI applications.
- OpenTelemetry – The underlying tracing standard used in MLflow span tables.

## Sources

- migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md

# Citations

1. [migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md](/references/migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws-4136e9d1.md)
