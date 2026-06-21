---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75d02c7f4449e815213c122c169c81b67133cfb9b40dc4d72afedab5abd4ea32
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-production-monitoring-for-long-term-trace-storage
    - MPMFLTS
  citations:
    - file: trace-agents-deployed-outside-of-databricks-databricks-on-aws.md
title: MLflow Production Monitoring for Long-term Trace Storage
description: Beta feature for storing GenAI agent traces in Delta tables via Production Monitoring, offering durable storage, no trace size limits, automated quality assessment, and ~15-minute sync intervals.
tags:
  - mlflow
  - production-monitoring
  - delta-tables
  - trace-storage
timestamp: "2026-06-19T23:08:03.314Z"
---

# [MLflow Production Monitoring](/concepts/mlflow-production-monitoring.md) for Long-term Trace Storage

**MLflow [Production Monitoring](/concepts/production-monitoring.md) for Long-term Trace Storage** is a beta feature that allows you to persist [MLflow Tracing](/concepts/mlflow-tracing.md) data from production [GenAI Agents](/concepts/genai-agent-observability.md) into [Delta Tables](/concepts/delta-lake-table.md), enabling durable storage, scalable size handling, and automated quality evaluation. After [Traces](/concepts/traces.md) are logged to an [MLflow Experiment](/concepts/mlflow-experiment.md), you can enable [Production Monitoring](/concepts/production-monitoring.md) to store them long-term, beyond the default lifecycle of [MLflow Experiment](/concepts/mlflow-experiment.md) artifacts. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Benefits

[Production Monitoring](/concepts/production-monitoring.md) provides several advantages over storing [Traces](/concepts/traces.md) solely in the [MLflow](/concepts/mlflow.md) artifact store:

- **Durable storage**: [Traces](/concepts/traces.md) are written to Delta tables, offering long-term retention independent of the [MLflow Experiment](/concepts/mlflow-experiment.md) artifact lifecycle. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]
- **No trace size limits**: Unlike alternative storage methods, [Production Monitoring](/concepts/production-monitoring.md) handles [Traces](/concepts/traces.md) of any size, making it suitable for high‑volume or large‑payload production deployments. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]
- **Automated quality assessment**: You can run [MLflow Scorers](/concepts/mlflow-scorers.md) on the stored production [Traces](/concepts/traces.md) to continuously monitor application quality and detect regressions. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]
- **Fast sync**: [Traces](/concepts/traces.md) are synced to Delta tables approximately every 15 minutes, providing near‑real‑time visibility into your production system. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Prerequisites

This feature is available for agents deployed outside of Databricks (for example, in Docker or Kubernetes containers) after you have configured tracing to log [Traces](/concepts/traces.md) to a Databricks [MLflow Experiment](/concepts/mlflow-experiment.md). The standard prerequisites for [MLflow Tracing with External Deployments](/concepts/mlflow-production-tracing-for-external-deployments.md) apply, including setting `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `MLFLOW_TRACKING_URI=databricks`, and `MLFLOW_EXPERIMENT_NAME`. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Next Steps

After enabling [Production Monitoring](/concepts/production-monitoring.md) for trace storage, you can view [Traces](/concepts/traces.md) in the Databricks MLflow UI, add context such as user or session IDs and custom tags, and use the stored Delta tables for further analysis or reporting. ^[trace-agents-deployed-outside-of-databricks-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) – The broader framework for evaluating and monitoring production GenAI applications.
- [Delta Tables](/concepts/delta-lake-table.md) – The storage format used for long‑term trace persistence.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit to which [Traces](/concepts/traces.md) are initially logged.
- [MLflow Scorers](/concepts/mlflow-scorers.md) – Tools that can automatically evaluate trace quality.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The observability system that captures execution details from GenAI agents.

## Sources

- trace-agents-deployed-outside-of-databricks-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-outside-of-databricks-databricks-on-aws.md](/references/trace-agents-deployed-outside-of-databricks-databricks-on-aws-afaae7ad.md)
