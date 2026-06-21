---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf1b662758e432af39cdfee8b46304cbbc859b7a50d6e8d248a6683cb6817cbb
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-recipient-privilege-and-command
    - Command and CREATE RECIPIENT Privilege
    - CRPAC
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: CREATE RECIPIENT Privilege and Command
description: A privilege required to create recipients in Unity Catalog, and the SQL command used to create recipient objects for Delta Sharing
tags:
  - privileges
  - sql-command
  - unity-catalog
  - permissions
timestamp: "2026-06-18T14:54:31.024Z"
---

# CREATE RECIPIENT Privilege and Command

**CREATE RECIPIENT** is a privilege and SQL command in [Unity Catalog](/concepts/unity-catalog.md) that enables users to create recipient objects for [OpenSharing](/concepts/opensharing.md) ([Delta Sharing](/concepts/delta-sharing.md)). The command establishes the named entity that represents a data consumer, allowing the provider to share data from a Unity Catalog [Metastore](/concepts/metastore.md) with external recipients.

## Overview

A recipient is the named object that represents the identity of a user or group of users who consume shared data. The `CREATE RECIPIENT` privilege is required at the Unity Catalog [Metastore](/concepts/metastore.md) level where the data to be shared is registered.^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Privilege Requirements

To create a recipient, you must have the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the data you want to share is registered. Additionally:

- You must create the recipient using a Databricks workspace that has that Unity Catalog [Metastore](/concepts/metastore.md) attached.
- If using a Databricks notebook to create the recipient, your compute must use Databricks Runtime 11.3 LTS or above and either standard or dedicated access mode (formerly shared and single user access modes).^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Creating Recipients for Databricks-to-Databricks Sharing

When a data recipient has access to a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace, you can create a recipient object with an authentication type of `DATABRICKS`. This creates a secure connection managed by Databricks for the sharing relationship.

### Requesting the Recipient's Sharing Identifier

Before creating a recipient for Databricks-to-Databricks sharing, you need to obtain the recipient's **sharing identifier**. This is a string consisting of the [Metastore](/concepts/metastore.md)'s cloud, region, and UUID in the format `<cloud>:<region>:<uuid>`.

The recipient can find their sharing identifier using:
- **Catalog Explorer**: In their Databricks workspace, navigate to Catalog, then click the gear icon and select **OpenSharing**. On the **Shared with me** tab, click their organization name and select **Copy sharing identifier**.
- **SQL**: Use the `CURRENT_METASTORE` function in a Databrick notebook or SQL query.
- **CLI**: The Databricks Unity Catalog CLI can retrieve the identifier.^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Creating the Recipient with SQL

Use the `CREATE RECIPIENT` SQL command in a Databricks notebook or the Databricks SQL query editor:

```sql
CREATE RECIPIENT [IF NOT EXISTS] recipient_name
  USING ID '<sharing_identifier>'
  COMMENT 'optional_description';
```

The sharing identifier must be in the format `<cloud>:<region>:<uuid>`. For example: `aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016`.^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Creating the Recipient via Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. At the top, click the gear icon and select **OpenSharing** (or click **Share > OpenSharing** in the upper-right corner).
3. On the **Shared by me** tab, click **New recipient**.
4. Enter the **Recipient name**.
5. For **Recipient type**, select **Databricks**.
6. Enter the recipient's **Sharing identifier** (the full string in `<cloud>:<region>:<uuid>` format).
7. (Optional) Enter a comment.
8. Click **Create**.
9. (Optional) Create custom **Recipient properties** by clicking the edit icon on the **Overview** tab.^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Alternative: Creating Recipients for Open Sharing

If the data recipient does not have access to a Unity Catalog-enabled Databricks workspace, you must use **open sharing** with token-based authentication (bearer tokens or OAuth federation). For these cases, see:
- [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](/concepts/oidc-federation-for-opensharing.md)
- Create a recipient object for non-Databricks users using bearer tokens^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Related Commands and Operations

After creating a recipient, you can perform additional operations:
- **GRANT**: Grant the recipient access to one or more shares.
- **ALTER**: Update recipient properties or modify the recipient object.
- **DROP**: Delete a recipient.
- **SHOW**: View existing recipients.
- **DESCRIBE**: Get details about a specific recipient.^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

For managing existing recipients, see [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md).

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [OpenSharing](/concepts/opensharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Data sharing](/concepts/delta-sharing.md)
- [Sharing Identifier](/concepts/sharing-identifier.md)
- [Recipient Properties](/concepts/recipient-properties.md)

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
