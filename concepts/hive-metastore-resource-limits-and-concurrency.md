---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 77b7b44bec2045fcde1f23921fc13c7a4b6d0b293057fcc1858b8766a20269e6
  pageDirectory: concepts
  sources:
    - work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-resource-limits-and-concurrency
    - Concurrency and Hive Metastore Resource Limits
    - HMRLAC
  citations:
    - file: work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
title: Hive Metastore Resource Limits and Concurrency
description: The Databricks-hosted legacy Hive metastore has resource limits on concurrent connections and connections per hour; exceeding these can cause metastore connection errors, and mitigation includes migration to Unity Catalog and smoothing workload concurrency.
tags:
  - databricks
  - hive-metastore
  - performance
  - reliability
timestamp: "2026-06-19T23:26:41.021Z"
---

# Hive [Metastore](/concepts/metastore.md) Resource Limits and Concurrency

The **Hive [Metastore](/concepts/metastore.md) Resource Limits and Concurrency** topic describes the connection and throughput constraints that apply to the Databricks-hosted legacy Hive [Metastore](/concepts/metastore.md), and the strategies available to avoid hitting those limits.

## Overview

The Databricks-hosted legacy Hive [Metastore](/concepts/metastore.md) has resource limits to ensure reliability. These limits include constraints on concurrent (active) connections and connections per hour. If workloads exceed these limits, clusters and jobs might encounter [Metastore](/concepts/metastore.md) connection errors or fail to start. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Types of Limits

The Hive [Metastore](/concepts/metastore.md) enforces two primary categories of resource limits:

- **Concurrent (active) connections**: The maximum number of simultaneous connections the [Metastore](/concepts/metastore.md) can handle at any given time.
- **Connections per hour**: A throughput cap on the total number of connections established within a rolling one-hour window.

When either limit is breached, workloads may experience [Metastore](/concepts/metastore.md) connection errors or cluster startup failures. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Avoiding Resource Limit Breaches

To avoid reaching these limits, Databricks recommends two approaches:

### 1. Migrate to [Unity Catalog](/concepts/unity-catalog.md)

The most effective approach is to upgrade tables from the Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md) and disable direct access to the Hive [Metastore](/concepts/metastore.md). [Unity Catalog](/concepts/unity-catalog.md) does not use the legacy Hive [Metastore](/concepts/metastore.md), so Hive metastore-specific database connection limits no longer apply. See [Upgrade a Databricks workspace to Unity Catalog](/concepts/migrating-existing-workspaces-to-unity-catalog.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

### 2. Optimize Workload Orchestration

If migration is not yet complete, optimize workload orchestration to smooth peak concurrency. Recommended practices include:

- Avoid synchronized job and cluster launches.
- Limit burst fan-out patterns.
- Minimize transient Hive [Metastore](/concepts/metastore.md) activity spikes that increase the likelihood of connection-limit breaches.

These optimizations reduce the probability of hitting connection limits during peak usage. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Disabling Hive [Metastore](/concepts/metastore.md) Access

After migrating tables to [Unity Catalog](/concepts/unity-catalog.md), Databricks recommends explicitly disabling direct access to the Hive [Metastore](/concepts/metastore.md). By default, Databricks compute clusters continue to connect to the Hive [Metastore](/concepts/metastore.md) even after migration, unless you explicitly disable Hive [Metastore](/concepts/metastore.md) access. Disabling access can be done across the entire workspace or individually per compute cluster. See [Disable access to the Hive metastore used by your Databricks workspace](/concepts/disabling-direct-access-to-the-legacy-hive-metastore.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The account-level governance solution that replaces the legacy Hive [Metastore](/concepts/metastore.md).
- [Hive metastore](/concepts/built-in-hive-metastore.md) — The legacy per-workspace metadata store.
- [hive_metastore catalog](/concepts/hive-metastore-federation.md) — The [Three-Level Namespace](/concepts/three-level-namespace.md) representation of the legacy Hive [Metastore](/concepts/metastore.md) in Unity Catalog-enabled workspaces.
- [Legacy table access control](/concepts/table-access-control-tacl.md) — Access controls that continue to be enforced for `hive_metastore` data on [Standard Access Mode](/concepts/standard-access-mode.md) clusters.
- [Cluster-Scoped Data Access Permissions](/concepts/cluster-scoped-data-access-permissions.md) — How data access credentials interact with Hive [Metastore](/concepts/metastore.md) data when used alongside [Unity Catalog](/concepts/unity-catalog.md).

## Sources

- work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md

# Citations

1. [work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md](/references/work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws-c5d018d3.md)
