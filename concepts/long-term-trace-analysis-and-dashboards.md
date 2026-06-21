---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e85835a3671a35e95e3eca62db54e3a2298aae3a55bf71461284f6da4fc07f44
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - long-term-trace-analysis-and-dashboards
    - Dashboards and Long-Term Trace Analysis
    - LTAAD
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Long-Term Trace Analysis and Dashboards
description: Archiving traces to Delta tables enables building custom dashboards, performing in-depth analytics on trace data, and maintaining a durable record of application behavior beyond ephemeral tracking.
tags:
  - analytics
  - monitoring
  - observability
timestamp: "2026-06-19T09:02:50.246Z"
---

# Long-Term Trace Analysis and Dashboards

**Long-Term Trace Analysis and Dashboards** refers to the practice of saving GenAI agent traces to persistent storage for ongoing analysis, audit compliance, and custom visualization. By archiving traces to a [Unity Catalog](/concepts/unity-catalog.md) Delta table, teams can build custom dashboards, perform in-depth analytics on historical trace data, and maintain a durable record of their application's behavior over time. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Overview

Traces capture the full execution path of a GenAI agent call, including model inputs and outputs, tool invocations, intermediate reasoning steps, and their results. While [Production Monitoring](/concepts/production-monitoring.md) provides real-time visibility into agent behavior, long-term archiving enables retrospective analysis — such as identifying performance trends, debugging regressions, or auditing past behavior for compliance purposes. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

Archiving traces is particularly valuable for:
- **Building custom dashboards** that track agent quality metrics over weeks or months.
- **Performing in-depth analytics** on historical trace data to identify patterns or anomalies.
- **Maintaining a durable record** of application behavior for compliance or audit requirements. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Trace Archiving to Delta Tables

Traces and their associated assessments can be saved to a [Unity Catalog](/concepts/unity-catalog.md) Delta table for long-term storage. The target table is created if it does not already exist; if the table already exists, traces are appended to it. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Prerequisites

Users must have the necessary permissions to write to the specified Unity Catalog Delta table. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

### Enabling Trace Archiving

To begin archiving traces for an experiment, use the `enable_databricks_trace_archival` function. You must specify the full name of the target Delta table, including [Catalog and Schema](/concepts/catalog-and-schema.md). If you do not provide an `experiment_id`, archiving is enabled for the currently active experiment. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import enable_databricks_trace_archival

# Archive traces from a specific experiment to a Unity Catalog Delta table
enable_databricks_trace_archival(
    delta_table_fullname="my_catalog.my_schema.archived_traces",
    experiment_id="YOUR_EXPERIMENT_ID",
)
```

### Disabling Trace Archiving

Stop archiving traces for an experiment at any time by using the `disable_databricks_trace_archival` function. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

```python
from mlflow.tracing.archival import disable_databricks_trace_archival

# Stop archiving traces for the specified experiment
disable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")
```

## Building Dashboards from Archived Traces

Once traces are stored in a Delta table, you can query them using standard SQL or Spark APIs. This enables:

- **Custom dashboards** in Databricks SQL or visualization tools that plot judge score distributions, latency trends, or error rates over time.
- **Cross-session analysis** comparing agent behavior across configurations, model versions, or time periods.
- **Drill-down investigations** filtering archived traces by user, session, or outcome to understand specific incidents or patterns.

The structured format of the Delta table — containing both the raw trace data and any associated assessments — makes it straightforward to aggregate and analyze at scale.

## Building Evaluation Datasets from Archived Traces

Archived traces can also serve as a source for building [MLflow Evaluation Datasets](/concepts/evaluation-datasets.md). By selecting specific traces or time ranges from the Delta table, teams can create representative test sets for offline evaluation of new agent configurations. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Real-time monitoring of agent behavior before archiving.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for runs and archived traces.
- [Delta Tables](/concepts/delta-lake-table.md) — The storage format for archived trace data.
- GenAI Agent — The application whose traces are being archived.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
