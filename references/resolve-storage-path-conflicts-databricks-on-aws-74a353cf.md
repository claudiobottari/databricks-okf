---
title: Resolve storage path conflicts | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/storage-conflicts
ingestedAt: "2026-06-18T08:04:54.765Z"
---

A storage path conflict occurs when an external location overlaps with the default Unity Catalog storage path of any workspace in your Databricks account. This overlap interferes with the internal processing of certain Unity Catalog features. If your account has a storage path conflict, you must update your external location configuration.

Unity Catalog validates external locations against every storage configuration registered to your Databricks account, not just in the workspace where the location was created. As a result, a conflict can arise if multiple workspaces in the same account share the same bucket.

## How the conflict happens[​](#how-the-conflict-happens "Direct link to How the conflict happens")

A conflict occurs when you create or update an external location that overlaps with the default Unity Catalog storage path of any workspace in your account. This default path is configured using the storage configuration object during classic workspace deployment. See [Create a storage configuration](https://docs.databricks.com/aws/en/admin/workspace/create-uc-workspace#storage). For example:

*   **Default workspace storage path used to create workspace:** `s3://<your-bucket>/<region>/`
*   **Overlapping external location (conflict):** `s3://<your-bucket>/`

This overlap prevents Unity Catalog from using the workspace storage location for internal processing, and it blocks certain Unity Catalog functionality. Having an overlap also weakens data governance because internal workspace data could be exposed by the external location. Consequently, external location paths must not overlap with any workspace default Unity Catalog storage path in your account.

You can, however, create an external location on more specific paths under a workspace default storage path, like the [DBFS root location](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/external-locations-dbfs-root). This is because the DBFS root location is a sibling of the workspace's internal storage path and does not create a conflict.

## Identify your scenario[​](#identify-your-scenario "Direct link to Identify your scenario")

Review your external locations in **Catalog Explorer** in the Databricks UI to see if your external location path includes or is broader than your workspace's default storage path.  
Example:

*   **External location:** `s3://<your-bucket>/`
*   **Workspace default storage path:** `s3://<your-bucket>/<region>/`

Consider the following scenarios to help you determine how to proceed.

### Scenario A: External location updates without moving data[​](#scenario-a-external-location-updates-without-moving-data "Direct link to Scenario A: External location updates without moving data")

You define an external location at a broad path (such as `s3://<customer-bucket>/`) but access data in a more specific sibling folder, such as legacy Databricks File System data stored at `s3://<customer-bucket>/<region>/<workspace-id>/`.

**Action:** (Recommended) Update your existing external location to the more specific path. This change resolves the conflict while continuing to allow access to all the data. For example, you would update the path from `s3://<your-bucket>/` to `s3://<your-bucket>/<region>/<workspace-id>/`. This also prevents accidental data leakage of workspace internal data.

### Scenario B: Managed tables stored at the root bucket location[​](#scenario-b-managed-tables-stored-at-the-root-bucket-location "Direct link to Scenario B: Managed tables stored at the root bucket location")

You define an external location at the root of your bucket (for example, `s3://<your-bucket>/`) and create managed tables directly under it, such as `s3://<your-bucket>/__unity_storage/catalogs/<catalog_id>/tables/<table_id>`.

In this case, updating the path is not possible and you must move the data.

**Action:** Open a support ticket with Databricks Support. The support team can help you migrate your managed data to a new location and restore your metastore to a non-conflicting state.
