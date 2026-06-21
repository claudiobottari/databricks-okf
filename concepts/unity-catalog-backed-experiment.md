---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 311e03bd33f89c5461e31f7a4a0a7f010367698e8126e9a73fc87af7109b5bc2
  pageDirectory: concepts
  sources:
    - migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-backed-experiment
    - UCE
  citations:
    - file: migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
title: Unity Catalog-Backed Experiment
description: An MLflow experiment bound to a Unity Catalog trace location, backed by four Delta tables (otel_spans, otel_annotations, otel_logs, otel_metrics) sharing a common table prefix.
tags:
  - mlflow
  - unity-catalog
  - experiment
timestamp: "2026-06-19T19:33:45.121Z"
---

# Unity Catalog-Backed Experiment

A **Unity Catalog-Backed Experiment** is an [MLflow](/concepts/mlflow.md) experiment whose traces are stored in [Unity Catalog](/concepts/unity-catalog.md) Delta tables rather than in the default MLflow experiment trace store. This configuration removes trace storage limits, provides fine-grained access controls through Unity Catalog governance, and makes traces queryable from notebooks, SQL, Genie, AI/BI dashboards, and any Spark-based tool. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Overview

When an experiment is backed by Unity Catalog, its trace location is a three-part path (`catalog.schema.table_prefix`). The table prefix is applied to four Delta tables that store the experiment's data:

- `<prefix>_otel_spans`
- `<prefix>_otel_annotations`
- `<prefix>_otel_logs`
- `<prefix>_otel_metrics`

^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Creating a Unity Catalog-Backed Experiment

To create a Unity Catalog-backed experiment, use `mlflow.set_experiment()` with a `trace_location` parameter set to a `UnityCatalog` object specifying the destination catalog, schema, and table prefix: ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

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
```

## Migration from Existing Experiments

Traces stored in an existing MLflow experiment can be migrated to a Unity Catalog-backed experiment using the `databricks.migrations.migrate_traces_to_uc` module. The migration copies traces, spans, assessments, tags, and metadata from the source experiment to Unity Catalog tables without modifying the source experiment. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

The migration is idempotent — if interrupted (for example, due to a cluster timeout), it can be safely re-run and will resume from where it left off, skipping already-migrated rows. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Limitations of Migration

The migration does not copy archived or deleted traces, dataset records, labeling sessions, runs, or non-trace entities. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Prerequisites for Migration

- A Unity Catalog-enabled workspace
- A Databricks cluster running Databricks Runtime 15.3 or above
- The `databricks-agents` Python package (version 1.10.1 or later)
- Read access to the source experiment
- `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md)

^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Benefits

Storing traces in Unity Catalog provides:
- **Removed trace storage limits** — No capacity constraints on trace storage
- **Fine-grained access controls** — Through Unity Catalog's governance framework
- **Queryability** — Traces can be accessed from notebooks, SQL, Genie, AI/BI dashboards, and any Spark-based tool

^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance and access control layer for Databricks data assets
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure for monitoring and debugging ML applications
- Trace Storage Migration — The process of moving traces between storage backends
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controlling resource allocation for serverless MLflow workloads
- [Delta Tables](/concepts/delta-lake-table.md) — The underlying storage format for Unity Catalog-backed experiments

## Sources

- migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md](/references/migrate-experiment-traces-to-unity-catalog-databricks-on-aws-a625531c.md)
