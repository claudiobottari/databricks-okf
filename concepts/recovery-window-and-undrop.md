---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd34516ec6a8953fc7c1ee62d0c2da6e01b1500c71f62a3db5989aefff55389a
  pageDirectory: concepts
  sources:
    - object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recovery-window-and-undrop
    - UNDROP and Recovery Window
    - RWAU
    - Recovery Window After Deletion
    - Recovery window
  citations:
    - file: object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Recovery Window and UNDROP
description: A 7-day soft-delete window following deletion of a managed table or volume during which the object can be recovered using the UNDROP SQL command.
tags:
  - unity-catalog
  - recovery
  - deletion
timestamp: "2026-06-19T19:49:02.971Z"
---

# Recovery Window and UNDROP

**Recovery Window and UNDROP** refers to the time-limited, best-effort mechanism in Unity Catalog that allows users to recover dropped managed objects — such as tables, materialized views, and streaming tables — by using the `UNDROP` SQL command. This feature provides a safety net against accidental deletion by retaining soft-deleted data for a fixed period before permanent removal.

## Recovery Window Overview

After a managed table or volume is deleted, Unity Catalog does not immediately erase the underlying data files from cloud storage. Instead, the data enters a **recovery window** that lasts for 7 days from the time of deletion. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

During this 7-day window:

- Users can recover the dropped object using the `UNDROP` SQL command.
- Unity Catalog retains the dropped object's metadata.
- Storage billing continues for the retained data.

This recovery window applies to managed tables, materialized views, and streaming tables. It does not apply to external tables or volumes, which are not managed by Unity Catalog. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## UNDROP Command

The `UNDROP` SQL command is used to recover a dropped object during the recovery window. The command restores the object and its metadata from the soft-deleted state. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

Relevant documentation for the command includes:
- UNDROP — The SQL language reference for the recovery command.
- DROP TABLE — The command used to delete a table.
- DROP VOLUME — The command used to delete a volume.
- DROP CATALOG — The command used to delete a catalog.
- DROP SCHEMA — The command used to delete a schema.

## Purge Phase

When the 7-day recovery window expires, the object can no longer be recovered. Unity Catalog then enters a **purge phase**, during which it permanently deletes the underlying data files within 48 hours. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

After purge:
- Storage billing from Databricks for the deleted object stops.
- For customer-provided managed storage, your cloud provider may continue to bill you depending on your bucket's versioning, soft-delete, and lifecycle policies.
- The object and its data are irrecoverable.

## Limitations and Best Practices

Recovery is **time-limited and best-effort**. Databricks recommends deleting an object only after confirming the data is no longer needed. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

To prevent accidental recursive deletion of non-empty objects, use the `RESTRICT` option (the default) on `DROP CATALOG` and `DROP SCHEMA`. This option prevents dropping a parent object if it still contains child objects. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Storage Billing During Recovery

During the 7-day recovery window, Databricks continues to bill for storage on **Databricks default storage**. For customer-provided managed storage, your cloud provider bills you directly during and after the recovery window. After the purge phase, Databricks storage billing stops. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Applicability by Object Type

| Object Type | Recovery Window Applies? | Notes |
|---|---|---|
| Managed tables | Yes | 7-day window, recoverable via `UNDROP` |
| Materialized views | Yes | 7-day window, recoverable via `UNDROP` |
| Streaming tables | Yes | 7-day window, recoverable via `UNDROP` |
| Managed volumes | Recoverability not specified via `UNDROP` | Data files retained during recovery window |
| External tables | No | Metadata removed; data files remain in cloud storage |
| External volumes | No | Metadata removed; data files remain in cloud storage |
| Foreign and federated catalogs | No | Metadata only; source system data unaffected |

^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Managed vs External Assets in Unity Catalog](/concepts/managed-vs-external-assets-in-unity-catalog.md) — The distinction that determines whether data files are managed by Unity Catalog or by the user.
- Default Storage in Databricks — Object storage provisioned by Databricks.
- [Customer-Provided Managed Storage](/concepts/databricks-default-storage-vs-customer-provisioned-managed-storage.md) — Cloud storage configured by the user for managed assets.
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — The full hierarchy of objects that can be secured and recovered.
- Data Lifecycle Management — Broader policies for data retention and deletion.

## Sources

- object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/object-storage-lifecycle-in-unity-catalog-databricks-on-aws-112fa332.md)
