---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a46cfd06fce34065fa52d211581c24b12c1481a016a28d2d7fefaec03393be8
  pageDirectory: concepts
  sources:
    - object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - purge-phase-after-deletion
    - PPAD
  citations:
    - file: object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Purge Phase After Deletion
description: After the 7-day recovery window ends, Unity Catalog permanently deletes data files within 48 hours, and the object can no longer be recovered.
tags:
  - unity-catalog
  - deletion
  - lifecycle
timestamp: "2026-06-19T19:49:10.042Z"
---

# Purge Phase After Deletion

The **Purge Phase After Deletion** is the second phase in the multi-phase lifecycle of managed data files in [Unity Catalog](/concepts/unity-catalog.md) after a managed table or volume is deleted. It begins when the 7-day [Recovery Window After Deletion](/concepts/recovery-window-and-undrop.md) ends and the object can no longer be recovered.

## Timing

The purge phase lasts for up to 48 hours following the end of the 7-day recovery window. During this period, Unity Catalog permanently deletes the underlying data files from cloud storage. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Behavior

Once the purge phase begins, the deleted object cannot be recovered. The `UNDROP` SQL command no longer works, and Unity Catalog removes the object's metadata from the [Metastore](/concepts/metastore.md). ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Storage Billing

Storage billing behavior differs by storage type during the purge phase:

- **Databricks default storage**: Storage billing stops once the 7-day recovery window passes. Databricks no longer charges for the storage of the deleted data files. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]
- **Customer-provided managed storage**: Your cloud provider continues to bill you for storage. To reduce charges after deletion, check your bucket's object versioning, soft-delete, and lifecycle policies. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Applicable Object Types

The purge phase applies only to managed tables and volumes — objects where [Unity Catalog](/concepts/unity-catalog.md) controls the storage location and data file lifecycle. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

For other securable objects (catalogs, schemas, views, functions, models), deletion removes metadata only, and there are no data files to purge. For [External Tables and Volumes in Unity Catalog|external tables and volumes](/concepts/external-tables-in-unity-catalog.md), data files remain in your cloud storage and are not purged by Unity Catalog. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Recovery Window After Deletion](/concepts/recovery-window-and-undrop.md) — The 7-day period preceding the purge phase during which objects can be recovered
- [Managed vs External Assets in Unity Catalog](/concepts/managed-vs-external-assets-in-unity-catalog.md) — Determines whether data files are subject to the purge phase
- [UNDROP Command](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-undrop-table) — Recovery command available only before the purge phase begins

## Sources

- object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/object-storage-lifecycle-in-unity-catalog-databricks-on-aws-112fa332.md)
