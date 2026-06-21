---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7c79517ff50d7bf8d7a1bd6610b5cd386fe64760aee4b316c8d0a0fc875aa3e
  pageDirectory: concepts
  sources:
    - resolve-storage-path-conflicts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - storage-path-conflict
    - SPC
    - storage path conflicts
  citations:
    - file: resolve-storage-path-conflicts-databricks-on-aws.md
title: Storage path conflict
description: A conflict that occurs when an external location overlaps with the default Unity Catalog storage path of any workspace in a Databricks account, interfering with internal processing and data governance.
tags:
  - unity-catalog
  - data-governance
  - storage
timestamp: "2026-06-19T20:14:01.664Z"
---

# Storage Path Conflict

A **storage path conflict** occurs when an [External location](/concepts/external-location.md) in Unity Catalog overlaps with the default Unity Catalog storage path of any workspace in the Databricks account. This overlap interferes with the internal processing of certain Unity Catalog features and, if present, requires updating the external location configuration. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## How the Conflict Happens

The conflict arises when you create or update an external location whose path overlaps with the default Unity Catalog storage path of any workspace in the account. That default path is set using the storage configuration object during classic workspace deployment. For example: ^[resolve-storage-path-conflicts-databricks-on-aws.md]

- Default workspace storage path: `s3://<your-bucket>/<region>/`
- Overlapping external location (conflict): `s3://<your-bucket>/`

Because Unity Catalog validates external locations against every storage configuration registered to the account — not just the workspace where the location was created — a conflict can also occur if multiple workspaces share the same bucket. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

An external location defined on a more specific path **under** a workspace’s default storage path (for example, a path used for the [DBFS root location](/concepts/dbfs-root-location.md)) does **not** cause a conflict, because the DBFS root location is a sibling of the workspace’s internal storage path. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Consequences

A storage path conflict prevents Unity Catalog from using the workspace storage location for internal processing and blocks certain Unity Catalog functionality. The overlap also weakens data governance because internal workspace data could be exposed by the external location. Therefore, external location paths must not overlap with any workspace default Unity Catalog storage path in your account. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Identifying a Conflict

Review your external locations in **Catalog Explorer** in the Databricks UI. Check whether an external location path includes or is broader than any workspace’s default storage path. For example: ^[resolve-storage-path-conflicts-databricks-on-aws.md]

- External location: `s3://<your-bucket>/`
- Workspace default storage path: `s3://<your-bucket>/<region>/`

## Resolution Scenarios

Two common scenarios are described below, along with the recommended actions.

### Scenario A: External Location Updates Without Moving Data

You define an external location at a broad path (e.g., `s3://<customer-bucket>/`) but only access data in a more specific sibling folder, such as legacy Databricks File System data stored at `s3://<customer-bucket>/<region>/<workspace-id>/`.

**Action (Recommended):** Update the existing external location to the more specific path (e.g., from `s3://<your-bucket>/` to `s3://<your-bucket>/<region>/<workspace-id>/`). This resolves the conflict while continuing to allow access to all the data and prevents accidental data leakage of workspace internal data. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

### Scenario B: Managed Tables Stored at the Root Bucket Location

You define an external location at the root of your bucket (e.g., `s3://<your-bucket>/`) and create [Managed Tables](/concepts/managed-tables-in-databricks.md) directly under it, such as `s3://<your-bucket>/__unity_storage/catalogs/<catalog_id>/tables/<table_id>`.

In this case, updating the path alone is not possible — you must move the data.

**Action:** Open a support ticket with Databricks Support. The support team can help you migrate your managed data to a new location and restore your [Metastore](/concepts/metastore.md) to a non-conflicting state. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [External location](/concepts/external-location.md)
- Workspace Storage Configuration
- [DBFS root location](/concepts/dbfs-root-location.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Managed Tables](/concepts/managed-tables-in-databricks.md)
- Default Unity Catalog Storage Path

## Sources

- resolve-storage-path-conflicts-databricks-on-aws.md

# Citations

1. [resolve-storage-path-conflicts-databricks-on-aws.md](/references/resolve-storage-path-conflicts-databricks-on-aws-74a353cf.md)
