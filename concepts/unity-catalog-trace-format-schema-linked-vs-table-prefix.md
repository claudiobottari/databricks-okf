---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73c98b7390d8789ec50abf3d3e23b2738e2abf6de3ea042cc169df69012ce797
  pageDirectory: concepts
  sources:
    - migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-trace-format-schema-linked-vs-table-prefix
    - UCTF(VT
  citations:
    - file: migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
title: Unity Catalog Trace Format (Schema-linked vs Table-prefix)
description: "Two formats for storing MLflow traces in Unity Catalog: the older Beta schema-linked format (catalog.schema) and the newer Public Preview table-prefix format (catalog.schema.table_prefix)"
tags:
  - mlflow
  - unity-catalog
  - tracing
timestamp: "2026-06-19T19:33:04.509Z"
---

# Unity Catalog Trace Format (Schema-linked vs Table-prefix)

**Unity Catalog Trace Format (Schema-linked vs Table-prefix)** describes the two distinct storage formats available for storing [MLflow](/concepts/mlflow.md) traces in [Unity Catalog](/concepts/unity-catalog.md). Understanding the differences between these formats is essential for managing trace data, particularly when migrating from the legacy Beta release format to the current Public Preview format.

## Overview

When [MLflow experiments](/concepts/mlflow-experiment.md) store traces in [Unity Catalog](/concepts/unity-catalog.md), they use one of two formats: **schema-linked** or **table-prefix**. The schema-linked format was used during the Beta release, while the table-prefix format was introduced with the Public Preview release and is the recommended format for all new and existing Unity Catalog trace workloads. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Schema-linked Format (Beta)

The schema-linked format uses a two-part path (`catalog.schema`) as the trace destination. In this format: ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

- Trace data is stored in fixed-name tables, specifically `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]
- Tags, assessments, and metadata are stored as log events within the logs table. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

If a [Unity Catalog](/concepts/unity-catalog.md) schema contains tables named `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`, the experiment uses the older schema-linked format. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Table-prefix Format (Public Preview and Later)

The table-prefix format uses a three-part path (`catalog.schema.table_prefix`) as the trace destination. In this format: ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

- Trace data is stored in prefix-namespaced tables such as `<table_prefix>_otel_spans`. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]
- Annotations (tags, [Assessments](/concepts/assessments.md), and metadata) have a dedicated table rather than being embedded in the logs table. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Benefits of Table-prefix Format

Databricks recommends the table-prefix format for all new and existing Unity Catalog trace workloads because it provides: ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

- Faster time-range queries
- Richer attribute types
- A dedicated annotations table
- Support for multiple trace destinations per schema

## Migration

Users who configured an [MLflow Experiment](/concepts/mlflow-experiment.md) to store traces in Unity Catalog during the Beta release using the schema-linked format can migrate to the table-prefix format. The migration copies spans and annotations using Spark SQL. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

### Prerequisites for Migration

- A Unity Catalog-enabled workspace
- A Databricks cluster running Databricks Runtime 15.3 or above
- The `databricks-agents` Python package (version 1.10.0 or above)
- Appropriate permissions: `USE_CATALOG` and `USE_SCHEMA` on the source [Catalog and Schema](/concepts/catalog-and-schema.md), and `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` on the destination [Catalog and Schema](/concepts/catalog-and-schema.md)

### Migration Process

The migration involves:

1. Creating a destination experiment linked to a Unity Catalog table-prefix location
2. Switching trace logging to the new experiment and stopping writes to the source experiment
3. Running the migration using the `V1ToV2SqlMigration` class from `databricks.migrations.v1_to_v2` ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

The migration is idempotent — if it fails partway through, it can be safely rerun, and already-migrated rows are skipped automatically. Source tables are not modified by the migration and can be retained as a backup. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- Trace Location
- Data Migration

# Citations

1. [migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md](/references/migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws-4136e9d1.md)
