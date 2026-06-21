---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e53936d34695a88390d1f4daff1f4ade3e01317ed1ae35e5106357c332e511d3
  pageDirectory: concepts
  sources:
    - migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricksmigrationsmigrate_traces_to_uc
  citations:
    - file: migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
title: databricks.migrations.migrate_traces_to_uc
description: A Python SDK module providing the run() function used to perform the migration from a source MLflow experiment to a target Unity Catalog-backed experiment.
tags:
  - mlflow
  - api
  - python
  - migration
timestamp: "2026-06-19T19:33:23.180Z"
---

# databricks.migrations.migrate_traces_to_uc

The **`databricks.migrations.migrate_traces_to_uc`** module provides the `run()` function for migrating [[MLflow Trace|MLflow Traces]] from a source experiment to a destination [Unity Catalog](/concepts/unity-catalog.md)-backed experiment. This migration copies traces, spans, assessments, tags, and metadata into Unity Catalog Delta tables, removing trace storage limits and enabling fine-grained access controls through Unity Catalog governance. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Overview

Storing traces in Unity Catalog makes them queryable from notebooks, SQL, Genie, AI/BI dashboards, and any Spark-based tool. The migration is designed to be idempotent — if interrupted (for example, due to a cluster timeout), it can be safely rerun and will automatically resume from where it left off, skipping already-migrated rows. The source experiment is not modified during the process. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

The migration does **not** copy archived or deleted traces, dataset records, labeling sessions, runs, or non-trace entities. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before running the migration, the following requirements must be met:

- A Unity Catalog-enabled workspace.
- A Databricks cluster running Databricks Runtime 15.3 or above.
- The `databricks-agents` Python package version 1.10.1 or later installed.
- Read access to the source experiment.
- `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md).

^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Migration Workflow

### Step 1: Create a Destination Experiment

A destination experiment is an MLflow experiment bound to a Unity Catalog trace location. The trace location is a three-part path (`catalog.schema.table_prefix`) that maps to four Delta tables:

- `<prefix>_otel_spans`
- `<prefix>_otel_annotations`
- `<prefix>_otel_logs`
- `<prefix>_otel_metrics`

Create the destination using `mlflow.set_experiment()` with a `UnityCatalog` trace location. The resulting experiment ID is used in subsequent steps. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Step 2: Switch Trace Logging

Before running the migration, redirect all trace logging to the destination experiment and stop writes to the source experiment. This ensures no traces are lost during the migration. Replace any existing `mlflow.set_experiment()` calls pointing to the source experiment with ones pointing to the destination experiment, either by name or by ID. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

Trace location can also be configured through environment variables like `MLFLOW_EXPERIMENT_NAME` and `MLFLOW_EXPERIMENT_ID`, which are used by deployed applications, containerized services, model serving endpoint configurations, and IDE or local development setups. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Step 3: Run the Migration

Execute the `run()` function from a Databricks notebook on the cluster:

```python
from databricks.migrations.migrate_traces_to_uc import run

run(
    source_experiment_id="<source_experiment_id>",
    target_experiment_id="<destination_experiment_id>",
)
```

Replace `<source_experiment_id>` with the experiment ID of the existing experiment containing traces to migrate, and `<destination_experiment_id>` with the experiment ID of the Unity Catalog-backed experiment created in Step 1. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Time-Restricted Migration

To migrate only traces created after a specific time, pass the `start_time_ms` parameter with a timestamp in epoch milliseconds. The migration will ingest all traces with a request time at or after the specified timestamp, skipping those already migrated:

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

## Idempotency and Resilience

The migration is fully idempotent. If it is interrupted for any reason, rerunning the same command will safely resume from where it left off, skipping any rows that have already been migrated. The source experiment remains unmodified and can be retained as a backup. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and traces.
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' governance solution for data and AI assets.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The mechanism for capturing and storing trace data.
- [Store traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md) — Configuration for new experiments to write traces directly to Unity Catalog.
- [Delta Tables](/concepts/delta-lake-table.md) — The underlying storage format for Unity Catalog traces.

## Sources

- migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md](/references/migrate-experiment-traces-to-unity-catalog-databricks-on-aws-a625531c.md)
