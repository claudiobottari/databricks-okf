---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88dc1139d5546a956b4057e4fb95a965c945437a5533387344a90b7a2f8b20e2
  pageDirectory: concepts
  sources:
    - resolve-storage-path-conflicts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-storage-validation
    - UCSV
  citations:
    - file: resolve-storage-path-conflicts-databricks-on-aws.md
title: Unity Catalog storage validation
description: The process by which Unity Catalog validates external locations against every storage configuration registered to the Databricks account, not just the workspace where the location was created.
tags:
  - unity-catalog
  - security
  - storage
timestamp: "2026-06-19T20:14:11.389Z"
---

Here is the wiki page for "Unity Catalog storage validation".

---

## Unity Catalog Storage Validation

**Unity Catalog storage validation** is the process by which [Unity Catalog](/concepts/unity-catalog.md) checks that [external locations](/concepts/external-location.md) do not conflict with the default storage paths of any workspace in a Databricks account. This validation ensures that internal workspace data remains isolated and that Unity Catalog features function correctly. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

### How Validation Works

When an external location is created or updated, Unity Catalog validates it against every storage configuration registered to the Databricks account — not just the configuration for the workspace where the location was created. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

A storage path conflict occurs if an external location path overlaps with the default Unity Catalog storage path of any workspace in the account. The default path is configured using the storage configuration object during workspace deployment. For example:

- **Default workspace storage path:** `s3://<your-bucket>/<region>/`
- **Overlapping external location (conflict):** `s3://<your-bucket>/`

This overlap can prevent Unity Catalog from using the workspace storage location for internal processing and may weaken data governance by exposing internal workspace data through the external location. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

### Resolving Conflicts

If a storage path conflict is identified, the resolution depends on your data layout:

- **Scenario A – No data move needed:** If your external location is defined at a broad path (e.g., `s3://<customer-bucket>/`) but you only access data in a more specific sibling folder (e.g., `s3://<customer-bucket>/<region>/<workspace-id>/`), you can update the external location to the more specific path. This resolves the conflict without moving data. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

- **Scenario B – Data move required:** If you have created [managed tables](/concepts/managed-tables-in-databricks.md) directly under the root bucket location (e.g., `s3://<your-bucket>/__unity_storage/...`), you cannot simply update the path. You must open a support ticket with Databricks Support to migrate the managed data to a new location and restore the [Metastore](/concepts/metastore.md) to a non-conflicting state. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

### Permissible Subpath Overlaps

External locations can be created on more specific paths under a workspace default storage path, as long as they are siblings of the workspace's internal storage path. For example, the [DBFS root](/concepts/dbfs-root-location.md) location is a sibling of the workspace's internal storage path and does not create a conflict. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

### Related Concepts

- [External locations](/concepts/external-location.md)
- Storage configuration
- [Managed tables](/concepts/managed-tables-in-databricks.md)
- [DBFS root](/concepts/dbfs-root-location.md)
- Workspace deployment

### Sources

- resolve-storage-path-conflicts-databricks-on-aws.md

# Citations

1. [resolve-storage-path-conflicts-databricks-on-aws.md](/references/resolve-storage-path-conflicts-databricks-on-aws-74a353cf.md)
