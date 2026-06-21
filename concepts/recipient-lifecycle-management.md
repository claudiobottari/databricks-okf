---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c610d8d4c9f63ae859257bebc952055565f5abeb7a0bf4b5f5839b7c21e969a
  pageDirectory: concepts
  sources:
    - manage-data-recipients-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-lifecycle-management
    - RLM
    - Recipient Object Management
    - Recipient management
  citations:
    - file: manage-data-recipients-for-opensharing-databricks-on-aws.md
title: Recipient Lifecycle Management
description: Administration of OpenSharing recipients including viewing recipient lists (SHOW RECIPIENTS), viewing details (DESCRIBE RECIPIENT), viewing granted shares (SHOW GRANTS TO RECIPIENT), updating properties/owner/name/comments (ALTER RECIPIENT), and deleting recipients (DROP RECIPIENT), which invalidates tokens and revokes data access.
tags:
  - delta-sharing
  - administration
  - databricks
  - opensharing
timestamp: "2026-06-19T19:23:53.219Z"
---

# Recipient Lifecycle Management

**Recipient Lifecycle Management** refers to the set of operations that data providers perform on recipient objects in Databricks OpenSharing. A *recipient* is the named object that represents the identity of a user or group with whom you share data. Providers can view, update, manage properties on, restrict access for, and delete recipients. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

Recipients can be created for [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) using bearer tokens, or [Open ID Connect (OIDC) federation](/concepts/opensharing-with-oidc-federation.md). After a recipient is created and [OpenSharing shares](/concepts/opensharing-share.md) are created, providers grant the recipient access to shares using the `GRANT ON SHARE` SQL command, Catalog Explorer, or the Unity Catalog CLI. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

**Permissions required**: To grant share access, a user must be a [Metastore](/concepts/metastore.md) admin or have delegated permissions or ownership on both the share and the recipient objects (`USE SHARE` + `SET SHARE PERMISSION` or share owner) AND (`USE RECIPIENT` or recipient owner). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## View Recipients

To view a list of recipients, use Catalog Explorer, the Unity Catalog CLI, or the `SHOW RECIPIENTS` SQL command in a Databricks notebook or the Databricks SQL query editor. A user must have the `USE RECIPIENT` privilege to view all recipients in the [Metastore](/concepts/metastore.md); other users see only the recipients they own. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

* **Catalog Explorer**: Navigate to **Catalog** > gear icon > **OpenSharing** > **Shared by me** > **Recipients**. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## View Recipient Details

Viewing details about a recipient requires being a [Metastore](/concepts/metastore.md) admin, having the `USE RECIPIENT` privilege, or being the recipient object owner. Details include: ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

- Creator, creation timestamp, comments, and authentication type (`DATABRICKS`, `TOKEN`, `OAUTH_CLIENT_CREDENTIALS`, or `OIDC_FEDERATION`). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]
- For token-authenticated recipients: token lifetime, activation link, activation status (whether the credential has been downloaded), and IP access lists (if assigned). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]
- For OIDC-federated recipients: recipient endpoint, MTLS endpoint, federation policies, and IP access lists (if assigned). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]
- For Databricks-to-Databricks recipients: the cloud, region, and [Metastore](/concepts/metastore.md) ID of the recipient's Unity Catalog [Metastore](/concepts/metastore.md), as well as activation status. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]
- Recipient properties, including custom properties. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

Use the `DESCRIBE RECIPIENT` SQL command, Catalog Explorer, or the CLI to view these details. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## View Shares Granted to a Recipient

To see which shares a recipient has been granted access to, use Catalog Explorer, the CLI, or the `SHOW GRANTS TO RECIPIENT` SQL command. The same permission requirements as viewing details apply ([Metastore](/concepts/metastore.md) admin, `USE RECIPIENT`, or owner). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

* **Catalog Explorer**: From the recipient details page, go to the **Shares** tab. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Update a Recipient

Updatable properties include recipient name, owner, comment, and custom properties. The `ALTER RECIPIENT` SQL command, Catalog Explorer, or the CLI can be used. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

**Permissions required**:
- To update the **owner**: must be a [Metastore](/concepts/metastore.md) admin or current owner. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]
- To update the **name**: must have `CREATE RECIPIENT` privilege *and* be the owner. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]
- To update **comment** or **custom properties**: must be the owner. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

In Catalog Explorer, on the recipient details page, use the kebab menu to rename, edit comments, or modify custom properties. For token-authenticated recipients, you can also rotate or update the bearer token under **Token Management**. For OIDC-federated recipients, you can add federation policies. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Manage Recipient Properties

Recipient objects include predefined properties (starting with `databricks.`) and custom properties. Predefined properties are: ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

- `databricks.accountId` – the Databricks account of the recipient (Databricks-to-Databricks only).
- `databricks.metastoreId` – the Unity Catalog [Metastore](/concepts/metastore.md) of the recipient (Databricks-to-Databricks only).
- `databricks.name` – the name of the recipient.

Custom properties can be used to refine data sharing, such as sharing different table partitions with different recipients or filtering rows/columns via dynamic views. For example, a custom property `'country' = 'us'` can control partition filtering. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

**Requirements**: Must use a SQL warehouse or compute running Databricks Runtime 12.2 or above. Permission required: [Metastore](/concepts/metastore.md) admin or user with `CREATE RECIPIENT` privilege. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

To add or update properties in Catalog Explorer, go to the recipient details page, click the pencil icon next to **Recipient properties**, add a key-value pair, and save. Predefined properties (`databricks.metastoreID`, `databricks.name`) are displayed and editable similarly. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

To view properties, follow the same steps as viewing recipient details. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Restrict Recipient Access Using Access Lists

For Databricks-to-Open sharing recipients, you can limit recipient access to a restricted set of IP addresses. See [Restrict OpenSharing recipient access using IP access lists](/concepts/opensharing-ip-access-list.md). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Delete a Recipient

Deleting a recipient requires being the recipient object owner. Use the `DROP RECIPIENT` SQL command, Catalog Explorer, or the CLI. When a recipient is deleted, the users represented by that recipient can no longer access the shared data, and any tokens used in Databricks-to-Open sharing are invalidated. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

* **Catalog Explorer**: From the **Recipients** tab, select the recipient, click the kebab menu, choose **Delete**, and confirm. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol used on Databricks.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI tool for managing Unity Catalog objects.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) governing data access.
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) – Sharing between two Databricks workspaces.
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) – Sharing with non-Databricks users via bearer tokens.
- [OIDC federation](/concepts/oidc-federation-policy.md) – Authentication method for OpenSharing recipients.
- Bearer tokens – Token-based authentication for recipients.
- IP access lists – Mechanism to restrict recipient access by IP.
- Dynamic views – Views that filter rows/columns based on recipient properties.

## Sources

- manage-data-recipients-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-data-recipients-for-opensharing-databricks-on-aws.md](/references/manage-data-recipients-for-opensharing-databricks-on-aws-073afd50.md)
