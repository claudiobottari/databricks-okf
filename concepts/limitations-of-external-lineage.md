---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40b4aef3e0fe94b1f9a3e43c0e6b169d1c20651ab03c4e5fa6fe19c43ac7dc66
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-external-lineage
    - LOEL
  citations:
    - file: external-lineage-databricks-on-aws.md
title: Limitations of External Lineage
description: "Constraints on external lineage in Unity Catalog including: lineage not recorded in system.access lineage tables, and resource limits of 10,000 external metadata objects and 100,000 lineage relationships per metastore."
tags:
  - limitations
  - lineage
  - unity-catalog
  - scale
timestamp: "2026-06-18T12:17:52.177Z"
---

# Limitations of External Lineage

External lineage in [Unity Catalog](/concepts/unity-catalog.md) allows you to augment automatically captured runtime lineage with metadata from workloads that run outside Databricks, such as first-mile ETL or last-mile BI. However, the feature has the following limitations: ^[external-lineage-databricks-on-aws.md]

- External lineage is not recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`). This means that queries written against those system tables will not reflect externally added lineage relationships. ^[external-lineage-databricks-on-aws.md]
- You can create up to 10,000 external metadata objects and 100,000 external lineage relationships per [Metastore](/concepts/metastore.md). These limits are part of the broader Databricks resource limits and are enforced to prevent [Metastore](/concepts/metastore.md) bloat and performance degradation. ^[external-lineage-databricks-on-aws.md]

Because external lineage is not stored in system tables, it is visible only through the lineage graph in Catalog Explorer or through the External Lineage API. Administrators planning to rely on external lineage for compliance or governance audits should account for this gap when designing their data lineage workflows. ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — The automatically captured lineage that external lineage supplements
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages external metadata objects
- Lakeflow Connect — An alternative method for automatically recording source lineage for managed ingestion pipelines
- Resource limits — The full set of Databricks resource quotas that includes the external lineage object limits

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
