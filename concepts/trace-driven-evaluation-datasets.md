---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2dfb54f5eed18235fa0cded5a107f1ba7390799a217a0b60463323a665c621ee
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - trace-driven-evaluation-datasets
    - TED
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Trace-Driven Evaluation Datasets
description: Practice of using archived trace data to construct MLflow evaluation datasets for further analysis and monitoring.
tags:
  - evaluation
  - datasets
  - mlflow
timestamp: "2026-06-18T10:48:08.852Z"
---

# Trace-Driven Evaluation Datasets

**Trace-Driven Evaluation Datasets** are evaluation datasets built from archived traces of GenAI applications, enabling continuous evaluation and monitoring based on real production data rather than static, pre-collected examples.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Overview

Trace-driven evaluation datasets are constructed by archiving traces—records of application behavior, including inputs, outputs, and intermediate steps—to a [Unity Catalog](/concepts/unity-catalog.md) Delta table, then using that archived data as the foundation for evaluation datasets. This approach ensures that evaluation reflects actual production usage patterns and edge cases.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Creating Trace-Driven Evaluation Datasets

The process involves two main steps:

1. **Archive traces to a Delta table**: Use the `enable_databricks_trace_archival` function to save traces and their associated assessments from an MLflow experiment to a Unity Catalog Delta table.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

2. **Build evaluation datasets from the archived table**: Once traces are archived, you can use the data in the Delta table to construct evaluation datasets that reflect real production behavior.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Benefits

- **Real-world coverage**: Evaluation datasets are drawn from actual production traces, capturing real user queries and system behavior.^[archive-traces-to-a-delta-table-databricks-on-aws.md]
- **Continuous updates**: As new traces are archived, evaluation datasets can be refreshed to reflect the latest application behavior.^[archive-traces-to-a-delta-table-databricks-on-aws.md]
- **Long-term durability**: Traces are stored in [Delta Tables](/concepts/delta-lake-table.md) within Unity Catalog, providing a durable record for historical analysis.^[archive-traces-to-a-delta-table-databricks-on-aws.md]
- **Advanced analytics**: Archived trace data can be used to build custom dashboards and perform in-depth analytics on application behavior.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Requirements

- You must have the necessary permissions to write to the specified Unity Catalog Delta table.^[archive-traces-to-a-delta-table-databricks-on-aws.md]
- The target table will be created if it does not already exist.^[archive-traces-to-a-delta-table-databricks-on-aws.md]
- If the table already exists, traces are appended to it.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Enabling Trace Archiving

To begin archiving traces for an experiment, use the `enable_databricks_trace_archival` function. You must specify the full name of the target Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md). If you don't provide an `experiment_id`, archiving is enabled for the currently active experiment.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

# Archive traces from a specific experiment to a Unity Catalog Delta table
enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

## Disabling Trace Archiving

Stop archiving traces for an experiment at any time by using the `disable_databricks_trace_archival` function.^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

# Stop archiving traces for the specified experiment
disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The framework for capturing and storing GenAI application traces
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for storing archived trace data in Delta tables
- [Delta Tables](/concepts/delta-lake-table.md) — The storage format for archived trace data
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The broader practice of evaluating generative AI applications
- [Production Monitoring](/concepts/production-monitoring.md) — Continuous monitoring of GenAI applications in production

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
