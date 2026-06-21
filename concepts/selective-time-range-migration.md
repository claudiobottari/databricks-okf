---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 218c43eb35cbba6b353c0ad49415adf1aa6ec2eb6a318fb35cf5bc67b5b114d8
  pageDirectory: concepts
  sources:
    - migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - selective-time-range-migration
    - STM
    - LSTM
  citations:
    - file: migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
title: Selective Time-Range Migration
description: The ability to migrate only traces created after a specific timestamp using the start_time_ms parameter in epoch milliseconds, with automatic deduplication of already-migrated traces.
tags:
  - mlflow
  - migration
  - filtering
timestamp: "2026-06-19T19:33:23.062Z"
---

# Selective Time-Range Migration

**Selective Time-Range Migration** is a feature of the migration utility that copies MLflow experiment traces to Unity Catalog Delta tables. It allows you to migrate only traces whose request time falls within a specified time window, rather than migrating the entire historical dataset.

## Overview

The selective time-range migration is implemented via the `start_time_ms` parameter of the `run()` function in the `databricks.migrations.migrate_traces_to_uc` module. When provided, the migration ingests all traces with a request time at or after the given timestamp (expressed in epoch milliseconds). Traces with a request time before that timestamp are skipped. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

This parameter is optional. If omitted, the migration copies all traces from the source experiment to the destination Unity Catalog–backed experiment.

## Usage

The migration is called from a Databricks notebook running on a cluster with Databricks Runtime 15.3 or above and the `databricks-agents` Python package (version ≥ 1.10.1). The following example shows how to migrate only traces from the last seven days:

```python
import time
from databricks.migrations.migrate_traces_to_uc import run

one_week_ago_ms = int((time.time() - 7 * 24 * 60 * 60) * 1000)

run(
    source_experiment_id="<source_experiment_id>",
    target_experiment_id="<destination_experiment_id>",
    start_time_ms=one_week_ago_ms,
)
```

^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Behavior

- **Inclusion criterion**: A trace is included if its request time is **at or after** the specified timestamp. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]
- **Idempotent and resumable**: The migration is idempotent. If interrupted, it can be safely re-run. Already‑migrated rows are skipped, and the migration resumes from where it left off. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]
- **Source unchanged**: The source experiment is not modified by the migration, regardless of the time range selected. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]
- **What is copied**: The migration copies traces, spans, assessments, tags, and metadata. Archived or deleted traces, dataset records, labeling sessions, runs, and non-trace entities are not copied. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Use Cases

- **Incremental migration**: Migrate only recent traces while keeping older traces in the source experiment for reference.
- **Testing and validation**: Validate the migration process on a subset of traces before running a full migration.
- **Time‑bounded compliance**: Migrate only traces within a specific date range to meet data retention or governance policies.

## Prerequisites

Before running a selective migration, you must have:

- A Unity Catalog–enabled workspace.
- A destination experiment bound to a Unity Catalog trace location (created in Step 1 of the full migration workflow).
- Read access to the source experiment and `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md).

## Related Concepts

- Migration of Traces to Unity Catalog – The full migration workflow, including creation of the destination experiment and switching trace logging.
- Idempotent Migration – The property that allows safe re‑runs of the migration.
- [Trace Storage in Unity Catalog](/concepts/mlflow-trace-storage-in-unity-catalog.md) – How traces are stored in Delta tables and the benefits of Unity Catalog governance.
- start_time_ms parameter – The epoch‑milliseconds timestamp that defines the selective time range.
- Epoch Milliseconds – Common time representation used for the `start_time_ms` parameter.

## Sources

- migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md](/references/migrate-experiment-traces-to-unity-catalog-databricks-on-aws-a625531c.md)
