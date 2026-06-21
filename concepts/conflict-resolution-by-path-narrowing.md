---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 98c5ba81e41805d6bb2381ac9fd8b35c09b552dd6205ff54116e0eebc55e151f
  pageDirectory: concepts
  sources:
    - resolve-storage-path-conflicts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conflict-resolution-by-path-narrowing
    - CRBPN
  citations:
    - file: resolve-storage-path-conflicts-databricks-on-aws.md
title: Conflict resolution by path narrowing
description: Resolution strategy for storage path conflicts where the external location path is updated to a more specific path (e.g., s3://bucket/region/workspace-id) without moving data, resolving the overlap while retaining data access.
tags:
  - unity-catalog
  - troubleshooting
  - storage
timestamp: "2026-06-19T20:14:09.490Z"
---

# Conflict Resolution by Path Narrowing

**Conflict resolution by path narrowing** is a method for resolving [storage path conflicts](/concepts/storage-path-conflict.md) in [Unity Catalog](/concepts/unity-catalog.md) by updating an external location’s path from a broad, overlapping scope to a more specific, non‑overlapping sub‑path. This approach avoids moving existing data and is the recommended action for the most common conflict scenario. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Background: Storage Path Conflicts

A storage path conflict occurs when an external location path overlaps with the default Unity Catalog storage path of any workspace in a Databricks account. Overlap interferes with internal Unity Catalog processing and can weaken data governance by exposing internal workspace data through the external location. For example:

- **Default workspace storage path:** `s3://<your-bucket>/<region>/`
- **Broad external location (conflict):** `s3://<your-bucket>/`

Because Unity Catalog validates external locations against every storage configuration in the account, such overlaps are blocked. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Scenario A: Path Narrowing (Without Moving Data)

When an external location is defined at a broad path (e.g., `s3://<customer-bucket>/`) but the actual data resides in a more specific sibling folder (e.g., `s3://<customer-bucket>/<region>/<workspace-id>/`), administrators can resolve the conflict by **narrowing** the external location path to that specific sub‑path.

**Action:** Update the existing external location from the broad path to the more specific sibling path. For example, change `s3://<your-bucket>/` to `s3://<your-bucket>/<region>/<workspace-id>/`. This resolves the overlap with the workspace’s default storage path while continuing to grant access to the targeted data. It also prevents accidental leakage of workspace internal data. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

This method is the recommended course of action when the data is not stored directly under the overlapping root bucket path.

## Scenario B: When Narrowing Is Not Possible

Path narrowing is not viable when managed tables are stored directly under the root bucket location (e.g., `s3://<your-bucket>/`). In that case, moving the data is required. Administrators should open a support ticket with Databricks Support to migrate managed data to a new location and restore the [Metastore](/concepts/metastore.md) to a non‑conflicting state. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Related Concepts

- [External location](/concepts/external-location.md) – The Unity Catalog object that defines access to cloud storage.
- Default Unity Catalog Storage Path – The storage path assigned to a workspace during deployment.
- [Storage path conflict](/concepts/storage-path-conflict.md) – The general problem of overlapping storage paths.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution for Databricks.
- [DBFS root location](/concepts/dbfs-root-location.md) – A sibling path under the bucket that does not cause conflicts.
- [Managed Tables](/concepts/managed-tables-in-databricks.md) – Tables whose data is managed by Unity Catalog.

## Sources

- resolve-storage-path-conflicts-databricks-on-aws.md

# Citations

1. [resolve-storage-path-conflicts-databricks-on-aws.md](/references/resolve-storage-path-conflicts-databricks-on-aws-74a353cf.md)
