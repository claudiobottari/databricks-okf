---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a2f13dc056d8b95fe154b5f3d81ab04cd7eeeaabff6efec95f7df2fa44a14ed
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disable_databricks_trace_archival-api
    - disable_databricks_trace_archival API
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: disable_databricks_trace_archival API
description: An MLflow API function used to stop archiving traces for a specific experiment.
tags:
  - mlflow
  - api
  - python
timestamp: "2026-06-19T22:08:00.440Z"
---

# disable_databricks_trace_archival API

The **`disable_databricks_trace_archival` API** is a function in the `mlflow.tracing.archival` module that stops the archiving of traces and their associated assessments to a Unity Catalog Delta table. It reverses the effect of the enable_databricks_trace_archival|enable_databricks_trace_archival function. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Overview

Trace archiving saves MLflow traces to a Delta table for long-term storage, custom dashboards, in-depth analytics, and durable record-keeping. The `disable_databricks_trace_archival` function stops this archival process for a specified experiment. If you don't provide an `experiment_id`, the function disables archiving for the currently active experiment. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Syntax

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `experiment_id` | string | No | The ID of the experiment for which to stop trace archiving. If omitted, archiving is disabled for the currently active experiment. |

^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Usage Notes

- You can stop archiving traces for an experiment at any time by calling this function. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]
- The function can be called from both the MLflow API and the Databricks UI. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]
- Disabling archival does not remove previously archived traces from the Delta table; they remain appended. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related Concepts

- enable_databricks_trace_archival|enable_databricks_trace_archival function — The counterpart function that starts trace archiving.
- [Trace Archiving](/concepts/trace-archival.md) — The overall process of saving traces to Delta tables.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system underlying the archival feature.
- [Production Monitoring](/concepts/production-monitoring.md) — A use case that benefits from trace archiving.
- [Delta Table](/concepts/delta-lake-table.md) — The storage format used for archived traces.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
