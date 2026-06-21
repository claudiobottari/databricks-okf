---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e63bba6e6d1437ad6d301b22a695447a79b9f6634db29bcdba4592f40dbed742
  pageDirectory: concepts
  sources:
    - migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-unity-catalog-trace-migration
    - PFUCTM
  citations:
    - file: migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md
title: Prerequisites for Unity Catalog Trace Migration
description: The required environment setup including a Unity Catalog-enabled workspace, Databricks Runtime 15.3+, the databricks-agents package (>=1.10.1), and specific read/write permissions on source and destination.
tags:
  - mlflow
  - unity-catalog
  - setup
  - permissions
timestamp: "2026-06-19T19:33:16.513Z"
---

# Prerequisites for Unity Catalog Trace Migration

Before migrating traces from an [MLflow Experiment](/concepts/mlflow-experiment.md) to [Unity Catalog](/concepts/unity-catalog.md) Delta tables, you must satisfy several infrastructure, software, and permission requirements. These prerequisites ensure that the migration tool can read the source experiment and write to the target Unity Catalog location.

## Requirements

### Unity Catalog–enabled workspace

The workspace must have Unity Catalog enabled. Storing traces in Unity Catalog removes trace storage limits, provides fine-grained access controls through Unity Catalog governance, and makes traces queryable from notebooks, SQL, Genie, AI/BI dashboards, and any Spark-based tool. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### Databricks Runtime version

The migration must be run from a Databricks cluster running Databricks Runtime 15.3 or above. Earlier runtimes may lack the required libraries or SQL features needed to interact with Unity Catalog tables and the MLflow trace migration API. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

### `databricks-agents` Python package

The `databricks-agents` package (version 1.10.1 or later) must be installed on the cluster. It contains the `migrate_traces_to_uc` module used in the migration. Install it with: ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

```bash
pip install "databricks-agents>=1.10.1"
```

### Required permissions

The user or service principal running the migration must have:

- **Read access** to the source experiment (the MLflow experiment containing the traces to be migrated).
- **`USE_CATALOG`**, **`USE_SCHEMA`**, and **`MODIFY`** permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md) where the Unity Catalog–backed experiment will be created.

These permissions are necessary for the migration tool to read traces from the source and write them to the four Delta tables that back the destination experiment. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Additional considerations

While not a prerequisite of the migration itself, you must also create a destination experiment bound to a Unity Catalog trace location before running the migration (see [Step 1](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/migrate-traces-to-uc#step-1-create-a-destination-experiment) in the full guide). The migration copies traces, spans, assessments, tags, and metadata from the source experiment to the destination; archived or deleted traces, dataset records, labeling sessions, runs, and non-trace entities are not copied. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

The migration is idempotent — if interrupted, it can be safely rerun, and already-migrated rows are skipped. ^[migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Experiment](/concepts/mlflow-experiment.md)
- Trace migration to Unity Catalog
- Databricks Runtime
- databricks-agents package
- [Store traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md)
- [Delta tables for traces](/concepts/delta-lake-table.md)

## Sources

- migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-experiment-traces-to-unity-catalog-databricks-on-aws.md](/references/migrate-experiment-traces-to-unity-catalog-databricks-on-aws-a625531c.md)
