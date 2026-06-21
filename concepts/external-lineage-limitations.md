---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb476c96016e3243a77ad3952b89e119dfc592b162832e6bf04f7c90fa61bec3
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage-limitations
    - ELL
    - external-lineage-limitations-and-quotas
    - Quotas and External Lineage Limitations
    - ELLAQ
  citations:
    - file: external-lineage-databricks-on-aws.md
title: External Lineage Limitations
description: Constraints on external lineage including non-recording in system lineage tables, and resource limits of 10,000 external metadata objects and 100,000 relationships per metastore.
tags:
  - limitations
  - unity-catalog
  - data-governance
timestamp: "2026-06-19T10:28:50.542Z"
---

```yaml
---
title: External Lineage Limitations
summary: Limitations of external lineage in Unity Catalog, including exclusion from system tables and [Metastore](/concepts/metastore.md) resource quotas.
sources:
  - external-lineage-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:04:29.448Z"
tags:
  - databricks
  - unity-catalog
  - lineage
  - limitations
aliases:
  - external-lineage-limitations
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# External Lineage Limitations

**External lineage** allows you to augment the data lineage that Unity Catalog automatically captures from Databricks workloads by adding metadata about data sources and sinks that live outside of Databricks (for example, Salesforce, MySQL, Tableau, or Power BI). While this feature provides an end-to-end view of data movement, it is subject to several limitations. ^[external-lineage-databricks-on-aws.md]

## System Table Exclusion

External lineage relationships are **not recorded** in the following lineage system tables:

- `system.access.table_lineage`
- `system.access.column_lineage`

This means that queries and audits relying on these system tables will not reflect lineage data that was added manually through the Catalog Explorer UI, the External Metadata or External Lineage APIs, or the Databricks SDK for Python. To view external lineage, you must use the lineage graph in Catalog Explorer. ^[external-lineage-databricks-on-aws.md]

## [Metastore](/concepts/metastore.md) Resource Limits

The number of external metadata objects and external lineage relationships you can create is capped per [Metastore](/concepts/metastore.md):

| Resource | Limit |
|----------|-------|
| External metadata objects | 10,000 |
| External lineage relationships | 100,000 |

These limits are part of Databricks' broader resource quotas. If you need to track lineage for a very large number of external systems or fine-grained relationships, you must work within these boundaries or consider alternative approaches (such as capturing lineage automatically through Lakeflow Connect where applicable). ^[external-lineage-databricks-on-aws.md]

## Additional Considerations

- External lineage is purely metadata that you define; it does **not** enforce any data movement or access control. It is used solely for visibility in the lineage graph. ^[external-lineage-databricks-on-aws.md]
- When creating external lineage manually, you must have the appropriate privileges: `CREATE EXTERNAL METADATA` on the [Metastore](/concepts/metastore.md), `MODIFY` on the external metadata object, and read or write privileges on the linked Unity Catalog objects. ^[external-lineage-databricks-on-aws.md]
- Automatic external lineage recording is available only through Lakeflow Connect managed ingestion pipelines; other external systems require manual entry. ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Data Lineage](/concepts/unity-catalog-data-lineage.md)
- [System tables (access lineage)](/concepts/system-tables-for-audit-logs.md)
- [External Metadata API](/concepts/external-metadata-api.md)
- [External Lineage API](/concepts/external-lineage-api.md)
- Resource limits
- [Lakeflow Connect Source Lineage](/concepts/lakeflow-connect-source-lineage.md)

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
