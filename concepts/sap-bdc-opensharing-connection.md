---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb75af34cdb726aaaf2f6622dda2dfde2d749be0bbb43f140190c48e2d579b0e
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-opensharing-connection
    - SBOC
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC OpenSharing Connection
description: A bidirectional Delta Sharing connection between Databricks and SAP Business Data Cloud that enables data exchange via the OpenSharing protocol.
tags:
  - databricks
  - sap-bdc
  - delta-sharing
timestamp: "2026-06-19T09:34:41.283Z"
---

# SAP BDC OpenSharing Connection

An **SAP BDC OpenSharing Connection** is a Databricks connection object that enables bidirectional data sharing between a Databricks workspace and an SAP Business Data Cloud (BDC) account using the [Delta Sharing](/concepts/delta-sharing.md) protocol with [OpenSharing](/concepts/opensharing.md) enabled. The connection is required for both receiving data products from and sharing Databricks assets to an SAP BDC account.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Requirements

To create an SAP BDC connection, you must be a workspace admin. You also need the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges in [Unity Catalog](/concepts/unity-catalog.md). Your Databricks workspace must be enabled for Unity Catalog, and OpenSharing must be enabled on the [Metastore](/concepts/metastore.md) with users granted permission to create and manage shares and recipients.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Creating an SAP BDC Connection

Creating a connection requires coordination with an SAP BDC admin. The user who creates the connection becomes its owner. Upon successful creation, two objects are automatically created in Databricks corresponding to the SAP BDC account: a provider object and a recipient object.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 1: Obtain a Connection Identifier

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Click **Connection Identifier**.
4. Share the partner identifier information with your SAP BDC admin.
5. Ask your SAP BDC admin to set up a Databricks connection on SAP BDC using the provided identifier.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 2: Complete the Connection on Databricks

1. After your SAP BDC admin sends you the Databricks connection invitation link, click **Connect to SAP BDC**.
2. In **Connection link from SAP BDC**, paste the invitation link.
3. Click **Connect**.
4. Once the connection is established, the SAP BDC account is automatically added as both a share provider and a recipient.
5. Click **View provider** to see all data products received from SAP BDC, or **View recipient** to see all data assets shared with SAP BDC.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

After mounting a share received from SAP BDC to a Unity Catalog catalog, SAP semantic metadata (table and column comments, primary keys, foreign keys, and governance tags) syncs automatically into Unity Catalog. See [SAP BDC semantic metadata](/concepts/sap-bdc-semantic-metadata-sync.md).^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Updating the Connection Owner

You must be the connection owner or a [Metastore](/concepts/metastore.md) admin to update the owner. The owner must be an individual user — connection ownership cannot be transferred to a group or service principal. To change the owner:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Find the connection, click the kebab menu (⋮), and select **Edit owner**.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Deleting a Connection

Deleting a connection removes access to all data products shared by the SAP BDC admin and revokes the SAP BDC recipient's access to Databricks shares. You must be the owner of the connection.

### Step 1: Clean Up Shared Assets

Unmount any shares received from SAP BDC from their mounted catalogs. The owner of each catalog must perform this action. If mounted catalogs still exist, you cannot delete the connection.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 2: Delete the Connection

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Find the connection, click the kebab menu, and select **Delete connection**.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Limitations

- There is a limit of **five connections per metastore**.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol underlying OpenSharing
- [OpenSharing](/concepts/opensharing.md) — Feature enabling cross-platform sharing in Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer required for SAP BDC connections
- SAP Business Data Cloud — SAP’s business data platform
- [SAP BDC semantic metadata](/concepts/sap-bdc-semantic-metadata-sync.md) — Automatic metadata sync after mounting shares
- Provider object and Recipient object — Objects created automatically with a connection
- Data Ingestion — The UI entry point for managing SAP BDC connections

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
