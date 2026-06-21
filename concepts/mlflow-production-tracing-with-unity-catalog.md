---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32897cd78acfbb88862e43a5628c6ddc462cd2c5acd51cce392170f7c0de2e70
  pageDirectory: concepts
  sources:
    - tracing-faq-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-production-tracing-with-unity-catalog
    - MPTWUC
  citations:
    - file: tracing-faq-databricks-on-aws.md
title: MLflow Production Tracing with Unity Catalog
description: For large-scale trace analysis in production, use production monitoring to log traces to Delta tables in Unity Catalog, removing the 1,000-trace and 100,000-trace limits.
tags:
  - mlflow
  - tracing
  - production
  - unity-catalog
  - databricks
timestamp: "2026-06-19T23:11:41.256Z"
---

# [MLflow](/concepts/mlflow.md) Production Tracing with [Unity Catalog](/concepts/unity-catalog.md)

**MLflow Production Tracing with Unity Catalog** refers to the practice of logging and storing [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) in Delta tables within [Unity Catalog](/concepts/unity-catalog.md) for production AI workloads. This approach overcomes the scalability limitations of workspace-level tracing and enables large-scale trace analysis for deployed models and agents.

## Overview

When [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) are stored in workspace-level experiments, they are subject to limitations: the trace list returns only the most recent 1,000 [Traces](/concepts/traces.md) by default, and experiments not in [Unity Catalog](/concepts/unity-catalog.md) are capped at 100,000 [Traces](/concepts/traces.md) total. These constraints make workspace-level tracing unsuitable for [Production Monitoring](/concepts/production-monitoring.md) at scale. ^[tracing-faq-databricks-on-aws.md]

Production tracing with [Unity Catalog](/concepts/unity-catalog.md) addresses these limitations by writing [Traces](/concepts/traces.md) directly to [Delta Tables](/concepts/delta-lake-table.md) in [Unity Catalog](/concepts/unity-catalog.md), enabling unlimited trace storage and full searchability across all [Traces](/concepts/traces.md) in a time range. ^[tracing-faq-databricks-on-aws.md]

## Benefits

### Scalable Trace Search

Workspace-level trace searches are limited to the 1,000 most recent [Traces](/concepts/traces.md). Even when searching by trace ID, older [Traces](/concepts/traces.md) outside this window do not appear in results. Production tracing with [Unity Catalog](/concepts/unity-catalog.md) removes this restriction, allowing searches across all [Traces](/concepts/traces.md) in any time range. ^[tracing-faq-databricks-on-aws.md]

### No Trace Count Limits

Experiments not in [Unity Catalog](/concepts/unity-catalog.md) have a hard cap of 100,000 [Traces](/concepts/traces.md) total. By migrating [Traces](/concepts/traces.md) to [Unity Catalog](/concepts/unity-catalog.md), users eliminate this limit entirely. ^[tracing-faq-databricks-on-aws.md]

## Implementation

To implement production tracing with [Unity Catalog](/concepts/unity-catalog.md), use [Production Monitoring](/concepts/production-monitoring.md) on Databricks to log [Traces](/concepts/traces.md) to Delta tables in [Unity Catalog](/concepts/unity-catalog.md). This approach is recommended for large-scale trace analysis in production environments. ^[tracing-faq-databricks-on-aws.md]

For users with existing workspace-level [Traces](/concepts/traces.md), Databricks provides guidance on migrating [Traces](/concepts/traces.md) to [Unity Catalog](/concepts/unity-catalog.md). See the documentation on migrating traces to Unity Catalog for step-by-step instructions. ^[tracing-faq-databricks-on-aws.md]

## API Usage

For production trace analysis at scale, the `mlflow.search_traces()` API provides convenient defaults for querying [Traces](/concepts/traces.md). For use cases requiring pagination, `MlflowClient.search_traces()` is available. However, for large-scale production analysis, querying the Delta tables in [Unity Catalog](/concepts/unity-catalog.md) directly is generally the most performant approach. ^[tracing-faq-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) — The recommended workflow for logging [Traces](/concepts/traces.md) to Delta tables
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and storage layer for production [Traces](/concepts/traces.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying tracing framework
- Migrating Traces to Unity Catalog — Process for moving existing [Traces](/concepts/traces.md) from workspace-level experiments
- [Trace Search and Discovery](/concepts/mlflow-trace-search-and-filtering.md) — Querying and finding [Traces](/concepts/traces.md) at scale
- [Delta Tables](/concepts/delta-lake-table.md) — The storage format for production [Traces](/concepts/traces.md)

## Sources

- tracing-faq-databricks-on-aws.md

# Citations

1. [tracing-faq-databricks-on-aws.md](/references/tracing-faq-databricks-on-aws-83ee1878.md)
