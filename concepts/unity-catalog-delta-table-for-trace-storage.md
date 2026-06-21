---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17ca6cd4393a4b20d492540e3455bae6aba6f19b339b9e4b1c22a901e97d55aa
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-delta-table-for-trace-storage
    - UCDTFTS
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Unity Catalog Delta Table for Trace Storage
description: The requirement and mechanism for storing archived traces in a Unity Catalog-managed Delta table, which is auto-created if it doesn't exist.
tags:
  - unity-catalog
  - delta-table
  - traces
  - databricks
timestamp: "2026-06-19T14:03:27.611Z"
---

## Unity Catalog Delta Table for Trace Storage

**Unity Catalog Delta Table for Trace Storage** refers to the practice of persisting [MLflow](/concepts/mlflow.md) traces and their associated assessments into a [Unity Catalog](/concepts/unity-catalog.md) managed [Delta table](/concepts/delta-lake-table.md). This enables long-term retention, custom dashboarding, and advanced analytics on trace data beyond the default short-term storage.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Overview

Trace archiving is useful for building custom dashboards, performing in-depth analytics on trace data, and maintaining a durable record of application behavior. Traces are stored in a Delta table that can be queried via SQL, Python, or BI tools.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Enabling Trace Archiving

Trace archiving is controlled per experiment. To begin archiving, use the `mlflow.tracing.archival.enable_databricks_trace_archival` function. You must provide the full three-level name of the target Delta table (catalog, schema, table name). If no `experiment_id` is given, archiving is enabled for the currently active experiment.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

Archiving can also be enabled through the Databricks UI under the experiment’s settings.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Disabling Trace Archiving

To stop archiving, call `disable_databricks_trace_archival` with the same `experiment_id`.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

### Permissions and Table Behavior

You must have the necessary permissions to write to the specified Unity Catalog Delta table. If the target table does not exist, it is created automatically. If the table already exists, new trace data is appended to it.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Next Steps

Once traces are archived, you can:
- Monitor GenAI apps in production
- Use the archived traces to [Building MLflow evaluation datasets](/concepts/evaluation-datasets.md)

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta table](/concepts/delta-lake-table.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)

### Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
