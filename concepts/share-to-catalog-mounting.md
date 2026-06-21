---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 133803883b01ba507c8cf6451a32fb4dc7a6d1a74fe6e04190348b9893c88e94
  pageDirectory: concepts
  sources:
    - read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-to-catalog-mounting
    - Mount a share to a catalog
  citations:
    - file: read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
title: Share-to-Catalog Mounting
description: The process of creating a new catalog from a share or mounting a share to an existing OpenSharing catalog, which makes shared data assets accessible in a recipient's Unity Catalog workspace.
tags:
  - unity-catalog
  - data-sharing
  - configuration
timestamp: "2026-06-19T20:09:34.815Z"
---

# Share-to-Catalog Mounting

**Share-to-Catalog Mounting** is the process of making data shared through the Databricks-to-Databricks OpenSharing protocol accessible to users in a recipient's Unity Catalog workspace. Mounting creates a catalog—or adds a share to an existing catalog—that users can query like any other read-only data asset in Databricks.

## Overview

When a data provider shares data using the Databricks-to-Databricks protocol, the recipient does not directly access the provider's storage. Instead, a user on the recipient team finds the *share*—the container for the tables, views, volumes, and notebooks that have been shared—and uses that share to create a *catalog*, the top-level container for all data in Unity Catalog. The catalog then makes the data available for read access. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

Updates the provider makes to the shared tables, views, volumes, and partitions are reflected in the recipient's workspace in near real time. Column changes (adding, renaming, deleting) and new shares or updates to shares may be cached for up to one minute before appearing in Catalog Explorer. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Permissions Required

The privileges needed depend on the mounting operation:

- **To create a new catalog from a share:** You must be a [Metastore](/concepts/metastore.md) admin, a user who has both the `CREATE CATALOG` and `USE PROVIDER` privileges for your Unity Catalog [Metastore](/concepts/metastore.md), or a user who has both the `CREATE CATALOG` privilege and ownership of the provider object. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- **To mount a share to an existing catalog:** You must have the `USE PROVIDER` privilege or ownership of the provider object, and you must either own the existing shared catalog or have both `MANAGE` and `USE CATALOG` privileges on it. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

To list and view details about all providers and provider shares, you must have the `USE PROVIDER` privilege. Other users have access only to the providers and shares that they own. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Mounting Methods

You can mount a share using Catalog Explorer, SQL commands, or the Databricks CLI. The three main approaches are:

### Create a New Catalog

When mounting to a new catalog, you specify a name for the catalog. The catalog name cannot be the same as any provider catalog that contains a table referenced by a shared view, to avoid namespace conflicts. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Mount to an Existing Catalog

Alternatively, you can add the share to an existing catalog that already has the OpenSharing type. This approach is available through Catalog Explorer. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon to open Catalog Explorer.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared with me** tab, find and select the provider.
4. Find the desired share and click **Mount to catalog** on the share row.
5. Choose **Create a new catalog** or **Mount to existing catalog**.
6. Enter a name for the new catalog or select an existing catalog.
7. Click **Create** or **Mount**.

^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Catalog Properties and Limitations

The catalog created from a share has a type of **OpenSharing**, visible on the catalog details page in Catalog Explorer or via the `DESCRIBE CATALOG` SQL command. All shared catalogs appear under **Catalog > Shared** in the Catalog Explorer left pane. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

Key properties:

- The 3-level namespace structure is `catalog.schema.table` or `catalog.schema.volume`, matching standard Unity Catalog conventions. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- Table and volume data under a shared catalog is **read-only**. Supported operations include `DESCRIBE`, `SHOW`, `SELECT` for tables, and `DESCRIBE VOLUME`, `LIST`, `SELECT * FROM`, and `COPY INTO` for volumes. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- Notebooks in a shared catalog can be previewed and cloned by any user with `USE CATALOG` on the catalog. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- Models in a shared catalog can be loaded for inference by users with `EXECUTE` privilege on the model plus `USE SCHEMA` and `USE CATALOG` on the schema and catalog. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]
- OpenSharing catalogs can be managed with standard SQL commands: `SHOW CATALOGS`, `DESCRIBE CATALOG`, `ALTER CATALOG`, and `DROP CATALOG`. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Managing Permissions After Mounting

By default, the catalog creator is the owner of all data objects under an OpenSharing catalog and can manage permissions for any of them. Privileges are inherited downward. For example, granting `SELECT` on the catalog grants `SELECT` on all schemas and tables unless revoked. You cannot grant privileges that give write or update access. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

The catalog owner can delegate ownership of data objects to other users or groups, granting them the ability to manage object permissions and life cycles. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Unmounting

To remove a share from a catalog, use Catalog Explorer:

1. Open the **OpenSharing** interface from Catalog Explorer.
2. On the **Shared with me** tab, select the provider.
3. Click the kebab menu on the share row and select **Unmount share**.
4. Confirm by clicking **Unmount**.

You need `USE CATALOG` and `MANAGE` privileges on the shared catalog to perform this operation. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [Databricks-to-Databricks OpenSharing](/concepts/databricks-to-databricks-sharing.md) — The sharing protocol that uses Unity Catalog for secure connections
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that manages shared catalogs
- [OpenSharing Catalog](/concepts/opensharing-catalog.md) — The catalog type created when mounting a share
- [Unity Catalog Privilege Model](/concepts/privileges-and-ownership.md) — The access control system governing shared data
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — An alternative sharing protocol using bearer tokens
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Applying row filters and column masks on shared data

## Sources

- read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md](/references/read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws-21150d4f.md)
