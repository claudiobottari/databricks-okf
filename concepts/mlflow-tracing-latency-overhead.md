---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8bb8e08b2a7bb402b828a4c7007b67f917aa0ac09c6c6eda325df04671841e5
  pageDirectory: concepts
  sources:
    - tracing-faq-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-latency-overhead
    - MTLO
  citations:
    - file: tracing-faq-databricks-on-aws.md
title: MLflow Tracing Latency Overhead
description: Traces are written asynchronously but still add minimal latency proportional to trace size; testing is recommended before production deployment.
tags:
  - mlflow
  - tracing
  - performance
  - databricks
timestamp: "2026-06-19T23:11:16.842Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Latency Overhead

**MLflow Tracing Latency Overhead** refers to the additional time incurred when [MLflow Tracing](/concepts/mlflow-tracing.md) instruments code to capture and record trace data (spans). Databricks recommends understanding this overhead before deploying tracing to production workloads. ^[tracing-faq-databricks-on-aws.md]

## How [MLflow](/concepts/mlflow.md) Minimizes Overhead

[Traces](/concepts/traces.md) are written **asynchronously** to minimize the performance impact on the application. This means that the collection and export of trace data happen in the background, allowing the main execution path to continue without blocking. ^[tracing-faq-databricks-on-aws.md]

## Observed Latency Impact

Despite asynchronous writing, tracing still adds a small amount of latency – especially when the trace size is large. The exact overhead depends on factors such as the number and size of spans, the complexity of the traced function, and the backend destination. [MLflow](/concepts/mlflow.md) provides rough estimates for latency impact by trace size in its documentation (see the table in the source). ^[tracing-faq-databricks-on-aws.md]

## Recommendation

[MLflow](/concepts/mlflow.md) recommends that you test your application with tracing enabled to understand the latency impact before deploying to production. This is particularly important for latency-sensitive applications where even minimal overhead may affect user experience. ^[tracing-faq-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overall tracing framework for instrumenting applications.
- [Production Monitoring](/concepts/production-monitoring.md) – Using [Traces](/concepts/traces.md) to monitor deployed models, which may involve additional latency considerations.
- [Databricks MLflow](/concepts/databricks-managed-mlflow.md) – The managed [MLflow](/concepts/mlflow.md) environment on Databricks.
- Rate limits and quotas for MLflow Tracing – Service constraints that interact with tracing volume and performance.

## Sources

- tracing-faq-databricks-on-aws.md

# Citations

1. [tracing-faq-databricks-on-aws.md](/references/tracing-faq-databricks-on-aws-83ee1878.md)
