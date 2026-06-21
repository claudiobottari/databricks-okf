---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3ac7216af8680f3d74a9bff98655df4e10c297570079fc4eed409eaee87c53a
  pageDirectory: concepts
  sources:
    - view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-limitations-and-scaling
    - Scaling and MLflow Tracing Limitations
    - MTLAS
    - mTLS
  citations:
    - file: view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
title: MLflow Tracing Limitations and Scaling
description: The trace list returns at most 1,000 traces; experiments not in Unity Catalog are capped at 100,000 traces; migrating to Unity Catalog removes both limits and enables full time-range search across all traces.
tags:
  - mlflow
  - tracing
  - unity-catalog
  - scaling
timestamp: "2026-06-19T23:25:27.027Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Limitations and Scaling

**MLflow Tracing Limitations and Scaling** describes the known capacity constraints and behavioral boundaries of the [MLflow Tracing](/concepts/mlflow-tracing.md) system on Databricks. Understanding these limits is essential for planning observability at scale and avoiding gaps in trace visibility.

## Trace List Capacity

The trace list view in the [MLflow](/concepts/mlflow.md) UI returns at most **1,000 traces** per query. Filters and trace ID searches apply only to this returned set, not to the full experiment. As a result, older [Traces](/concepts/traces.md) in experiments that contain more than 1,000 [Traces](/concepts/traces.md) may not appear in the list unless the time range is narrowed to include them. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Experiment Trace Limit

Experiments that are **not** in [Unity Catalog](/concepts/unity-catalog.md) are capped at **100,000 traces**. Once this limit is reached, no additional [Traces](/concepts/traces.md) can be logged to the experiment. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Scaling Recommendations

To remove both the 1,000‑trace list limit and the 100,000‑trace experiment cap, and to enable searching across all [Traces](/concepts/traces.md) in a time range, migrate your [Traces](/concepts/traces.md) to [Traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md). [Unity Catalog](/concepts/unity-catalog.md) does not impose the same per‑experiment trace cap and allows the trace list to return results from the full experiment history rather than a fixed‑size window. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Storage and Serving

[Traces](/concepts/traces.md) are stored and served by the managed [MLflow Tracking](/concepts/mlflow-tracking.md) service in your Databricks workspace when `MLFLOW_TRACKING_URI` is set to `databricks`. This production‑ready backend requires no additional hosting. See Trace agents deployed on Databricks for more information. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the tracing system.
- View traces in the Databricks MLflow UI — How to navigate and filter [Traces](/concepts/traces.md).
- [Traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md) — The recommended destination for scaling beyond capacity limits.
- Trace agents deployed on Databricks — Production deployment for the tracing infrastructure.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for runs and [Traces](/concepts/traces.md).

## Sources

- view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md

# Citations

1. [view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md](/references/view-traces-in-the-databricks-mlflow-ui-databricks-on-aws-d0ec6f89.md)
