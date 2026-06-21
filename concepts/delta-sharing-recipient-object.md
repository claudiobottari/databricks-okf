---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1cf88533f086b45acf15491ebaa8e2d87df12291380c4513f8452380c51bb25b
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-sharing-recipient-object
    - DSRO
    - Delta Sharing Recipient
    - Delta Sharing Recipient Setup
    - Delta Sharing Recipients
    - Delta Sharing recipient
    - Data Sharing Recipients
    - Delta Sharing Data Recipient
    - Delta Sharing providers and recipients
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: Delta Sharing Recipient Object
description: A named object in Unity Catalog that represents the identity of a user or group who consumes shared data, with authentication types depending on the recipient's environment.
tags:
  - delta-sharing
  - unity-catalog
  - data-sharing
timestamp: "2026-06-19T09:36:38.894Z"
---

# Delta Sharing Recipient Object

A **Delta Sharing Recipient Object** is the named object in a Delta Sharing provider’s [Metastore](/concepts/metastore.md) that represents the identity of a user or group of users who consume shared data. The recipient object enables the provider to manage access to shares and control how data is delivered to consumers. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Types of Recipients

The way a recipient is created and authenticated depends on whether the consumer has access to a Unity Catalog-enabled Databricks workspace:

* **Databricks-to-Databricks sharing** – The consumer has a Databricks workspace with Unity Catalog. The recipient object uses `DATABRICKS` authentication, and the secure connection is managed by Databricks. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
* **Databricks-to-Open sharing** – The consumer does not have access to a Unity Catalog-enabled Databricks workspace. The recipient uses token-based authentication (bearer tokens or OAuth federation). Procedures for these are documented in separate pages. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

This page focuses on creating recipients for **Databricks-to-Databricks sharing**.

## Requirements

To create a recipient, the following prerequisites must be met:

- The user must have the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the data to be shared is registered. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- The recipient must be created using a Databricks workspace that has that [Metastore](/concepts/metastore.md) attached. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- If using a notebook, the compute must use Databricks Runtime 11.3 LTS or above and either standard or dedicated access mode. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Creating a Recipient for Databricks-to-Databricks Sharing

### Step 1: Obtain the Consumer’s Sharing Identifier

The sharing identifier is a string that uniquely identifies the consumer’s Unity Catalog [Metastore](/concepts/metastore.md). It has the format `<cloud>:<region>:<uuid>` (for example, `aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016`). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The consumer can obtain this identifier using:

- **Catalog Explorer** – The sharing identifier is available under the OpenSharing settings (gear icon > OpenSharing > “Copy sharing identifier”). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **SQL** – The `CURRENT_METASTORE` function returns the identifier. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **CLI** – The Databricks Unity Catalog CLI can retrieve the [Metastore](/concepts/metastore.md) details. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The provider asks the consumer to supply this string.

### Step 2: Create the Recipient Object

The recipient can be created using **Catalog Explorer**, **SQL**, or the **CLI**. The permissions required are the same as the requirements above.

**Using Catalog Explorer:**

1. In the workspace, click **Catalog**.
2. Click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, click **New recipient**.
4. Enter a **Recipient name**.
5. For **Recipient type**, select **Databricks**.
6. Enter the consumer’s **Sharing identifier** in the format `<cloud>:<region>:<uuid>`.
7. (Optional) Add a comment.
8. Click **Create**. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

**Using SQL:**

```sql
CREATE RECIPIENT recipient_name
  USING ID '<sharing_identifier>';
```

**Using CLI:**

```bash
databricks recipients create --name recipient_name --sharing-identifier '<sharing_identifier>'
```

The created recipient object will have `authentication_type = DATABRICKS`.

### Optional: Manage Recipient Properties

After creation, you can add custom **Recipient properties** (key-value pairs) that can be used for filtering or routing. In Catalog Explorer, go to the recipient **Overview** tab and click the edit icon next to **Recipient properties**. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Next Steps

After the recipient is created, the provider can:

- **Grant access to shares** – Use the `GRANT` syntax to associate the recipient with one or more Delta Sharing shares. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **Manage the recipient** – View, update, delete, manage properties, or restrict access using IP lists. See [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) for details. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **Create shares** – Set up the shares that will be granted to the recipient. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Open Sharing vs Databricks-to-Databricks sharing](/concepts/databricks-to-open-sharing-vs-databricks-to-databricks-sharing.md)
- [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md)

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
