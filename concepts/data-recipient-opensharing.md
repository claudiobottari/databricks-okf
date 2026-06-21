---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b73a6bf752907a75ffa7f0b67cd0f7a11bbcff93c560495483f59beab74ebe5b
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-recipient-opensharing
    - DR(
    - Create a Recipient (OpenSharing)
    - Manage Recipients (OpenSharing)
    - Recipient (OpenSharing)
    - recipient (OpenSharing)
    - Create data recipients for OpenSharing
    - Manage Data Recipients for OpenSharing
    - Manage data recipients for OpenSharing
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: Data Recipient (OpenSharing)
description: A named object in OpenSharing that represents the identity of a user or group of users who consume shared data, identified by a sharing identifier for Databricks-to-Databricks mode.
tags:
  - delta-sharing
  - data-sharing
  - databricks
timestamp: "2026-06-18T11:23:12.050Z"
---

# Data Recipient (OpenSharing)

A **Data Recipient** is the named object in [OpenSharing](/concepts/opensharing.md) that represents the identity of a user or group of users who consume shared data. The way you create a recipient depends on whether the recipient has access to a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

- **Recipients with access to a Unity Catalog‑enabled Databricks workspace:** You create a recipient object with a secure connection managed by Databricks. This sharing mode is called *Databricks-to-Databricks sharing*, and is documented on this page. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **Recipients without access to a Unity Catalog‑enabled Databricks workspace:** You must use *open sharing* with a secure connection managed by token-based authentication (either bearer tokens or OAuth federation). See [OIDC Federation for OpenSharing Recipients](/concepts/oidc-federation-for-opensharing.md) and Create Recipient with Bearer Token for instructions. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Requirements

To create a recipient you need:

- The `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the data you want to share is registered. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- The recipient must be created from a Databricks workspace that has that [Metastore](/concepts/metastore.md) attached. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- If you use a Databricks notebook, your compute must use Databricks Runtime 11.3 LTS or above and either standard or dedicated access mode (formerly shared and single user). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

For permissions required to view, update, delete, grant share access, or manage properties, see [Manage Data Recipients for OpenSharing](/concepts/data-recipient-opensharing.md). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Create a recipient for Databricks-to-Databricks sharing

A recipient object with authentication type `DATABRICKS` represents a data recipient on a particular Unity Catalog [Metastore](/concepts/metastore.md). The [Metastore](/concepts/metastore.md) is identified by a *sharing identifier* in the format `<cloud>:<region>:<uuid>`. Data shared with this recipient can be accessed only on that [Metastore](/concepts/metastore.md). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Step 1: Request the recipient’s sharing identifier

Ask the intended recipient to send you the sharing identifier for the Unity Catalog [Metastore](/concepts/metastore.md) attached to the workspaces they will use to access the shared data. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The recipient can find this identifier using:

- **Catalog Explorer:** Click the gear icon and select **OpenSharing**. On the **Shared with me** tab, click the organization name in the upper right and choose **Copy sharing identifier**. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **SQL:** Run `SELECT CURRENT_METASTORE()` in a Databricks notebook or SQL query on Unity Catalog‑capable compute. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **Databricks Unity Catalog CLI:** Use the CLI to retrieve the [Metastore](/concepts/metastore.md) information. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The complete sharing identifier looks like `aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016`. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Step 2: Create the recipient

You can create the recipient using Catalog Explorer, SQL, or the Databricks CLI. All methods require the `CREATE RECIPIENT` privilege or [Metastore](/concepts/metastore.md) admin role. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

#### Using Catalog Explorer

1. In your workspace, click **Catalog**, then click the gear icon and select **OpenSharing** (or click **Share > OpenSharing** in the upper-right corner).
2. On the **Shared by me** tab, click **New recipient**.
3. Enter a **Recipient name**.
4. For **Recipient type**, select **Databricks**.
5. Enter the recipient’s **Sharing identifier** (the full `<cloud>:<region>:<uuid>` string).
6. (Optional) Add a comment.
7. Click **Create**.
8. (Optional) On the recipient’s **Overview** tab, click the edit icon next to **Recipient properties** to add custom key‑value properties.

#### Using SQL

```sql
CREATE RECIPIENT recipient_name
  USING ID '<sharing_identifier>';
```

Replace `<sharing_identifier>` with the full string (e.g., `aws:us-west-2:19a84bee...`). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

#### Using the CLI

```bash
databricks recipients create <recipient_name> \
  --authentication-type DATABRICKS \
  --sharing-identity '<sharing_identifier>'
```

The created recipient will have `authentication_type` set to `DATABRICKS`. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Next steps

- Grant Access to OpenSharing Shares – Grant the recipient access to one or more shares.
- [Manage Data Recipients for OpenSharing](/concepts/data-recipient-opensharing.md) – View, update, delete, manage properties, or restrict IP access for an existing recipient.
- [Create Shares for OpenSharing](/concepts/delta-sharing-open-sharing.md) – Create the shares you want to grant the recipient access to.

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
