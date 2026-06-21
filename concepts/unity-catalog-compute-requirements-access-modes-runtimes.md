---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8255d3058b34a67141a4ba244e381e5798f3375557a3a4b1817a2a5bde549a74
  pageDirectory: concepts
  sources:
    - unity-catalog-requirements-and-limitations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-compute-requirements-access-modes-runtimes
    - UCCR(M&R
  citations:
    - file: unity-catalog-requirements-and-limitations-databricks-on-aws.md
title: Unity Catalog Compute Requirements (Access Modes & Runtimes)
description: Clusters must run Databricks Runtime 11.3 LTS or above and be configured with standard or dedicated access mode to access Unity Catalog data.
tags:
  - unity-catalog
  - compute
  - databricks
timestamp: "2026-06-19T23:15:03.754Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) Compute Requirements (Access Modes & Runtimes)

**Unity Catalog Compute Requirements** define the necessary Databricks Runtime version, Access Modes|access mode configuration, and other compute prerequisites for accessing data governed by [Unity Catalog](/concepts/unity-catalog.md).

## Databricks Runtime Version

[Unity Catalog](/concepts/unity-catalog.md) is supported on clusters that run **Databricks Runtime 11.3 LTS or above**. All SQL warehouse compute versions support [Unity Catalog](/concepts/unity-catalog.md) by default. Clusters running earlier versions of Databricks Runtime do not provide support for all [Unity Catalog](/concepts/unity-catalog.md) GA features and functionality. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Access Modes

To access data in [Unity Catalog](/concepts/unity-catalog.md), clusters must be configured with the correct access mode. [Unity Catalog](/concepts/unity-catalog.md) is secure by default. If a cluster is not configured with **standard** or **dedicated** access mode, the cluster cannot access data in [Unity Catalog](/concepts/unity-catalog.md). For detailed information about access modes, see the page on [Access modes](/concepts/standard-access-mode.md). ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Relationship to File Formats

While not a compute requirement per se, [Unity Catalog](/concepts/unity-catalog.md) supports only specific table formats for managed and external tables. Managed tables must use `delta` or `iceberg` format; external tables can use `delta`, `CSV`, `JSON`, `avro`, `parquet`, `ORC`, or `text`. These formats affect how compute reads and writes data in [Unity Catalog](/concepts/unity-catalog.md). ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Limitations Related to Compute

Some limitations depend on the Databricks Runtime version or access mode:

- **Structured Streaming**: Has additional limitations based on Databricks Runtime and access mode. See Standard compute requirements and limitations and Dedicated compute requirements and limitations. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]
- **R workloads with dynamic views**: On Databricks Runtime 15.3 and below, R workloads do not support dynamic views for row‑level or column‑level security. Use Databricks Runtime 15.4 LTS or above on a compute resource that also supports serverless compute. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]
- **Python UDFs**: Not supported in Databricks Runtime 12.2 LTS and below. Python scalar UDFs are supported in [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) and above. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]
- **Scala UDFs**: Not supported in Databricks Runtime 14.1 and below on compute with [Standard Access Mode](/concepts/standard-access-mode.md). Scalar UDFs are supported in Databricks Runtime 14.2 and above on compute with [Standard Access Mode](/concepts/standard-access-mode.md). ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]
- **Standard Scala thread pools**: Not supported. Use `org.apache.spark.util.ThreadUtils` (except `newForkJoinPool` and `ScheduledExecutorService` thread pools). ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Resource Quotas

[Unity Catalog](/concepts/unity-catalog.md) enforces resource quotas on all securable objects. For the current limits see Resource limits. You can monitor quota usage using the [Unity Catalog Resource Quotas](/concepts/unity-catalog-resource-quotas.md) APIs. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Sources

- unity-catalog-requirements-and-limitations-databricks-on-aws.md

# Citations

1. [unity-catalog-requirements-and-limitations-databricks-on-aws.md](/references/unity-catalog-requirements-and-limitations-databricks-on-aws-0188dbe0.md)
