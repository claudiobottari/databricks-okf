---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c1159677a3b3b4834ba896e0f7354dd85587246b9e29f5390bc8e1f20bbf31e
  pageDirectory: concepts
  sources:
    - archive-traces-to-a-delta-table-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - trace-based-evaluation-datasets
    - TED
  citations:
    - file: archive-traces-to-a-delta-table-databricks-on-aws.md
title: Trace-based Evaluation Datasets
description: Using archived traces to build evaluation datasets for MLflow evaluation, enabling reuse of production trace data for model assessment.
tags:
  - mlflow
  - evaluation
  - datasets
timestamp: "2026-06-19T22:08:00.106Z"
---

# Trace-based Evaluation Datasets

**Trace-based evaluation datasets** are datasets derived from [archived traces](/concepts/trace-archival.md) stored in a [Unity Catalog](/concepts/unity-catalog.md) [Delta Table](/concepts/delta-lake-table.md). They enable in-depth analytics, custom dashboards, and durable record‑keeping of an application’s behavior for the purpose of evaluating and monitoring [GenAI applications|GenAI apps](/concepts/genai-application-evaluation-lifecycle.md) in production. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Creating a Trace-based Evaluation Dataset

To build a trace‑based evaluation dataset, you first archive traces and their associated assessments to a Unity Catalog Delta table using the `enable_databricks_trace_archival` function. Once traces are archived, you can use the table as the foundation for constructing evaluation datasets. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

The basic workflow is:

1. **Enable trace archiving** – Call `enable_databricks_trace_archival` with the full name of the target Delta table (including [Catalog and Schema](/concepts/catalog-and-schema.md)) and an optional `experiment_id`. If no `experiment_id` is given, the currently active experiment is used. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]
2. **Build evaluation datasets** – Follow the guide on [Building MLflow evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) to create datasets from the archived traces. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

You can stop archiving at any time with `disable_databricks_trace_archival`. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Requirements

You must have the necessary permissions to write to the specified Unity Catalog Delta table. If the table does not exist, it is created automatically; if it already exists, new traces are appended. ^[archive-traces-to-a-delta-table-databricks-on-aws.md]

## Use Cases

- Performing advanced analytics on trace data (e.g., custom dashboards).
- Maintaining a durable record of application behavior for compliance or audit.
- Using the archived traces as a labeled dataset for offline evaluation of model or agent performance.

## Related Concepts

- [Trace Archival](/concepts/trace-archival.md) – The mechanism for saving traces to a Delta table.
- [Delta Table](/concepts/delta-lake-table.md) – The storage format used for archived traces.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages the target table.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The dataset built from archived traces for model evaluation.
- [Production Monitoring](/concepts/production-monitoring.md) – The broader workflow that trace‑based evaluation datasets support.

## Sources

- archive-traces-to-a-delta-table-databricks-on-aws.md

# Citations

1. [archive-traces-to-a-delta-table-databricks-on-aws.md](/references/archive-traces-to-a-delta-table-databricks-on-aws-85660ef9.md)
