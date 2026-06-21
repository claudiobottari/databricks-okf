---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1a7fe4f7d32f32caf3384bebef7f43a0fee0f4c3951eaf5c4253e7469e2e740
  pageDirectory: concepts
  sources:
    - work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cluster-scoped-data-access-permissions
    - CDAP
    - Cluster Permissions
    - Cluster-level permissions
  citations:
    - file: work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
title: Cluster-Scoped Data Access Permissions
description: When using the Hive metastore alongside Unity Catalog, cluster-scoped credentials are used for Hive metastore data access but not for Unity Catalog data, and are also used for paths outside Unity Catalog.
tags:
  - databricks
  - unity-catalog
  - clusters
  - security
timestamp: "2026-06-19T23:26:39.503Z"
---

# Cluster-Scoped Data Access Permissions

**Cluster-scoped data access permissions** refer to the authorization model that governs how compute clusters access data when a Databricks workspace operates with both [Unity Catalog](/concepts/unity-catalog.md) and the legacy Hive [Metastore](/concepts/metastore.md). Under this model, the data access credentials assigned to a cluster are used to access Hive [Metastore](/concepts/metastore.md) data but are not used for data registered in [Unity Catalog](/concepts/unity-catalog.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Overview

When a workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md) while retaining access to the legacy per-workspace Hive [Metastore](/concepts/metastore.md), two distinct access control mechanisms apply simultaneously. The cluster-scoped credentials control access to data in the `hive_metastore` catalog, while [Unity Catalog](/concepts/unity-catalog.md) manages access to its own catalogs through its own security model. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

This dual system creates important implications for data access:

- **Hive [Metastore](/concepts/metastore.md) data**: Accessed using the credentials configured on the compute cluster.
- **Unity Catalog data**: Accessed through [Unity Catalog](/concepts/unity-catalog.md)'s built-in access controls, which do not rely on cluster-scoped credentials.
- **External paths**: If users access paths that are outside [Unity Catalog](/concepts/unity-catalog.md) (such as a path not registered as a table or [External location](/concepts/external-location.md)), the access credentials assigned to the cluster are used. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Key Differences from [Unity Catalog](/concepts/unity-catalog.md) Access

Cluster-scoped permissions differ from [Unity Catalog](/concepts/unity-catalog.md)'s access model in several important ways:

| Aspect | Cluster-Scoped (Hive [Metastore](/concepts/metastore.md)) | [Unity Catalog](/concepts/unity-catalog.md) |
|--------|---------------------------------|---------------|
| Scope | Workspace-level | Account-level |
| Groups | Workspace-local groups | Account groups |
| `USE CATALOG`/`USE SCHEMA` | Not required for root catalog access | Required for all operations |
| View ownership | Owner must own all referenced tables/views | Owner only needs `SELECT` privilege |
| `ANY FILE` / `ANONYMOUS FUNCTION` | Supported | Not supported |
| `DENY` | Supported | Not supported (implicit deny) |
| `READ_METADATA` | Supported | Managed differently |

^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Implications for Data Joins

When joining data from the Hive [Metastore](/concepts/metastore.md) with data from [Unity Catalog](/concepts/unity-catalog.md), cluster-scoped permissions govern the Hive [Metastore](/concepts/metastore.md) side of the join. Such joins can only be performed on the workspace where the Hive [Metastore](/concepts/metastore.md) data resides — running them in another workspace results in an error. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Best Practices

### Migration

Because cluster-scoped access for the Hive [Metastore](/concepts/metastore.md) represents a legacy workflow, Databricks recommends migrating to full [Unity Catalog](/concepts/unity-catalog.md) usage. Two migration paths are available:

1. **Direct upgrade**: Upgrade all tables registered in the Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md).
2. **Gradual federation**: Use [Hive Metastore Federation](/concepts/hive-metastore-federation.md) to create a foreign catalog in [Unity Catalog](/concepts/unity-catalog.md) that mirrors the Hive [Metastore](/concepts/metastore.md).

After migration, disable direct access to the Hive [Metastore](/concepts/metastore.md) at the workspace or cluster level. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

### Resource Limits

The Databricks-hosted legacy Hive [Metastore](/concepts/metastore.md) has resource limits, including limits on concurrent connections and connections per hour. Workloads that exceed these limits may encounter [Metastore](/concepts/metastore.md) connection errors or fail to start. To avoid these limits:

- **Migrate to Unity Catalog**: [Unity Catalog](/concepts/unity-catalog.md) does not use the legacy Hive [Metastore](/concepts/metastore.md), so these limits no longer apply.
- **Optimize workload orchestration**: Avoid synchronized job launches, limit burst fan-out, and minimize transient Hive [Metastore](/concepts/metastore.md) activity spikes. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The account-level governance solution that supersedes cluster-scoped permissions
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — The legacy per-workspace metadata store
- [Legacy Table Access Control](/concepts/table-access-control-tacl.md) — The access control system applicable to Hive [Metastore](/concepts/metastore.md) data
- Default Catalog — The default catalog configuration for workspaces with both metastores
- [Disable Hive Metastore Access](/concepts/disable-legacy-hive-metastore-access.md) — How to disable direct Hive [Metastore](/concepts/metastore.md) access after migration

## Sources

- work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md

# Citations

1. [work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md](/references/work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws-c5d018d3.md)
