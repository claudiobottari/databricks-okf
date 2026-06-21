---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 741d790af90bf5f17902c6eae979bb715325720bbf2a5a00fb2d6796de830118
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection
    - SBC
    - SAP BDC connections
    - Connections pane
    - sap-bdc-connection-databricks
    - SBC(
    - sap-bdc-connection-on-databricks
    - SBCOD
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection
description: A named connection object that links a Databricks workspace to an SAP Business Data Cloud account for OpenSharing, enabling bidirectional data sharing.
tags:
  - delta-sharing
  - sap-bdc
  - connection
timestamp: "2026-06-19T17:59:41.905Z"
---

## SAP BDC Connection

An **SAP BDC Connection** is a Databricks integration that enables bidirectional data sharing with an SAP Business Data Cloud (BDC) account via the [Delta Sharing](/concepts/delta-sharing.md) OpenSharing protocol. The connection allows a Databricks workspace to both receive data products (shares) from SAP BDC and share Databricks assets back to SAP BDC. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Requirements

To create an SAP BDC Connection, you must be a workspace admin and have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges. Your Databricks workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md), and OpenSharing must be enabled on the [Metastore](/concepts/metastore.md) with appropriate user permissions for creating and managing shares and recipients. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Creating an SAP BDC Connection

The creation process involves two steps that require coordination between a Databricks user and an SAP BDC admin.

**Step 1 – Obtain a connection identifier:**  
From the Databricks sidebar, navigate to **Data Ingestion** and select the SAP Business Data Cloud tile. Click **Connection Identifier** and share the generated partner identifier with your SAP BDC admin. The SAP BDC admin uses this identifier to set up a Databricks connection on the SAP BDC side (see the [SAP BDC documentation](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provision-sap-business-data-cloud-connector-for-supported-external-systems)). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

**Step 2 – Complete the connection on Databricks:**  
After the SAP BDC admin sends you the connection invitation link, return to the **Data Ingestion** page and click **Connect to SAP BDC**. Paste the invitation link into the **Connection link from SAP BDC** field and click **Connect**. Once established, the SAP BDC account is automatically registered as both a provider and a recipient in Databricks. You can then view received data products under **View provider** or shared assets under **View recipient**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

When a share received from SAP BDC is mounted to a Unity Catalog catalog, SAP semantic metadata — including table and column comments, primary keys, foreign keys, and governance tags — syncs automatically into Unity Catalog. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Updating Connection Owner

Only the current connection owner or a [Metastore](/concepts/metastore.md) admin can change the owner. The owner must be an individual user; ownership cannot be transferred to a group or service principal. To update the owner, go to **Data Ingestion** > **SAP Business Data Cloud** tile, locate the connection, click the kebab menu, and select **Edit owner**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Deleting a Connection

Deleting a connection removes access to all data products shared by the SAP BDC admin and revokes the SAP BDC recipient’s access to Databricks shares.

**Step 1 – Clean up shared assets:**  
Unmount any shares received from SAP BDC from their Unity Catalog catalogs. The catalog owner must perform this step. The connection cannot be deleted if mounted catalogs still exist. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

**Step 2 – Delete the connection:**  
After unmounting, go to **Data Ingestion** > **SAP Business Data Cloud** tile, find the connection, click the kebab menu, and select **Delete connection**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Limitations

A single [Metastore](/concepts/metastore.md) can have at most **five** SAP BDC connections. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for data sharing across platforms.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks governance layer for managing data assets.
- [OpenSharing](/concepts/opensharing.md) – Enables creation and management of shares and recipients.
- SAP BDC Semantic Metadata – Automatic sync of SAP metadata into Unity Catalog.
- Catalog from Share – How to read shared data by creating a catalog.

### Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
