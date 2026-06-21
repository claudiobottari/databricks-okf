---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1e699372c54c1b91df70c2932ce1911493450d4b49606b668d53ed532d35eb6
  pageDirectory: concepts
  sources:
    - migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - v1tov2sqlmigration
  citations:
    - file: migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
title: V1ToV2SqlMigration
description: A Databricks migration utility class that copies trace spans and annotations from schema-linked UC trace tables to table-prefix format using Spark SQL; idempotent and safe to rerun
tags:
  - migration
  - mlflow
  - unity-catalog
timestamp: "2026-06-19T19:32:31.248Z"
---

# V1ToV2SqlMigration

`V1ToV2SqlMigration` is a Python class provided by the `databricks.migrations.v1_to_v2` module (part of the `databricks-agents` package) that copies trace data (spans and annotations) from the older schema-linked Unity Catalog table format to the newer table-prefix format. It is used to migrate [[MLflow Trace|MLflow Traces]] stored in a Beta‑era Unity Catalog configuration to the Public Preview format recommended by Databricks. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Overview

During the Beta release of Unity Catalog trace storage, an experiment’s trace destination was a two‑part path (`catalog.schema`). Trace data lived in fixed‑name tables such as `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`. With the Public Preview, the format changed to a three‑part path (`catalog.schema.table_prefix`) where tables are namespaced with a prefix and annotations have a dedicated table. The `V1ToV2SqlMigration` class automates the copy of spans and annotations from the old tables to the new prefix‑namespaced tables using Spark SQL. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Requirements

Before using the migration, the following prerequisites must be met:

- A Unity Catalog‑enabled workspace.
- A Databricks cluster running Databricks Runtime 15.3 or above.
- The `databricks-agents` Python package (version 1.10.0 or later). Install with `pip install "databricks-agents>=1.10.0"`.
- Permissions: `USE_CATALOG` and `USE_SCHEMA` on the **source** [Catalog and Schema](/concepts/catalog-and-schema.md); `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` on the **destination** [Catalog and Schema](/concepts/catalog-and-schema.md).
- A destination experiment must already be created and linked to a Unity Catalog table‑prefix location (the format introduced in Public Preview). ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Usage

Instantiate the `V1ToV2SqlMigration` with the source schema and the destination prefix, then call `.run()`.

```python
from databricks.migrations.v1_to_v2 import V1ToV2SqlMigration

migration = V1ToV2SqlMigration(
    v1_source_schema="<source_catalog>.<source_schema>",
    v2_destination_prefix="<destination_catalog>.<destination_schema>.<table_prefix>",
)
migration.run()
```

The placeholders must match the source experiment’s old Unity Catalog schema and the destination experiment’s newly configured catalog, schema, and table prefix. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Parameters

- `v1_source_schema` (str) – The Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) where the old‑format trace tables reside, in the form `catalog.schema`. This is the two‑part path of the Beta‑era trace location. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]
- `v2_destination_prefix` (str) – The Unity Catalog catalog, schema, and table prefix for the new‑format destination, in the form `catalog.schema.table_prefix`. This must match the location configured in the destination experiment created in Step 1 of the migration process. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Behavior

The migration copies spans and annotations (tags, assessments, metadata) using Spark SQL. It is **idempotent**: if the migration fails partway through (for example, due to a cluster timeout), it can be safely rerun. Already‑migrated rows are skipped automatically. The source tables are **not modified** by the migration and can be retained as a backup. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Important Considerations

All writes to the source experiment should be stopped before running the migration. Any traces written to the source tables during migration might not be copied. If a dry run is desired, the migration can be performed without switching production workloads first. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Related Concepts

- [MLflow Traces in Unity Catalog](/concepts/mlflow-trace-storage-in-unity-catalog.md) – Overview of trace storage in Unity Catalog.
- Beta to Public Preview Migration – The broader context of format changes.
- Schema-linked Format – The old two‑part trace destination format.
- [Table-prefix Format](/concepts/table-prefix-format-benefits.md) – The new three‑part trace destination format.
- [Unity Catalog](/concepts/unity-catalog.md) – The underlying cataloging system.
- databricks-agents – The package containing the migration tool.

## Sources

- migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md

# Citations

1. [migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md](/references/migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws-4136e9d1.md)
