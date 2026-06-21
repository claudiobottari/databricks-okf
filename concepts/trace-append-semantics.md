---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38b532d21ed29e0bc841b3b661cd9befdc8573a89dc1b19117b04116c6046aef
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.88
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-append-semantics
    - TAS
    - Tags
    - tags
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Trace Append Semantics
description: The behavior where archived traces are appended to an existing Delta table rather than overwriting or replacing previous entries.
tags:
  - delta-table
  - traces
  - data-ingestion
timestamp: "2026-06-19T14:03:31.524Z"
---

# Trace Append Semantics

**Trace Append Semantics** refers to the behavior of the [Trace Archival](/concepts/trace-archival.md) system when writing traces to an existing [Delta Table](/concepts/delta-lake-table.md) destination. When traces are archived to a Unity Catalog Delta table that already contains data, new trace records are appended rather than overwriting existing data.

## Overview

The trace archival feature in [MLflow](/concepts/mlflow.md) allows users to save traces and their associated assessments to a Unity Catalog Delta table for long-term storage and advanced analysis. This capability supports building custom dashboards, performing in-depth analytics on trace data, and maintaining a durable record of application behavior. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Append Behavior

When the target Delta table already exists, new traces are appended to the existing data. This append-only semantics ensures that previously archived traces are preserved and remain accessible for historical analysis. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

If the target table does not already exist, it is created automatically during the archival process. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Enabling Trace Archival

To archive traces to a Delta table, use the `enable_databricks_trace_archival` function from `mlflow.tracing.archival`. You must specify the full three-level name of the target Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md). If no `experiment_id` is provided, archiving is enabled for the currently active experiment. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

# Archive traces from a specific experiment to a Unity Catalog Delta table
enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

## Disabling Trace Archival

Use the `disable_databricks_trace_archival` function to stop archiving traces for an experiment at any time. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

# Stop archiving traces for the specified experiment
disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

## Permissions

Users must have the necessary permissions to write to the specified Unity Catalog Delta table. The archival process requires write access to create or modify the target Delta table. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Use Cases

Archived traces with append semantics support several downstream workflows:

- **Custom dashboards** — Build visualizations on accumulated trace data
- **In-depth analytics** — Perform historical analysis across all archived traces
- **Durable record keeping** — Maintain a complete, append-only log of application behavior over time
- **Evaluation dataset creation** — Use archived traces as a source for constructing [Evaluation Datasets](/concepts/evaluation-datasets.md) for model assessment

## Related Concepts

- [Trace Archival](/concepts/trace-archival.md) — The broader process of persisting traces to Delta tables
- [Delta Table](/concepts/delta-lake-table.md) — The storage format used for trace archival
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer managing Delta table access
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Workflows that benefit from trace archival
- [Building MLflow evaluation datasets](/concepts/mlflow-evaluation-datasets.md) — Using archived traces to create evaluation data

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
