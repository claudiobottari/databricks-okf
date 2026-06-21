---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 90165b448528265bc946fa2546a863f05b20b985f160197dc706e19fad874578
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection-databricks
    - SBC(
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection (Databricks)
description: A bidirectional connection between Databricks and SAP Business Data Cloud that enables Delta Sharing via the OpenSharing protocol, with automatic creation of provider and recipient objects.
tags:
  - databricks
  - sap
  - delta-sharing
  - connection-management
timestamp: "2026-06-19T14:34:37.019Z"
---

## SAP BDC Connection (Databricks)

The **SAP BDC Connection (Databricks)** is a Databricks entity that enables secure data sharing between a Databricks workspace and an SAP Business Data Cloud (BDC) account using the OpenSharing protocol. This connection is required to both grant SAP BDC access to Databricks data and to receive data products from SAP BDC. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Requirements

To create an SAP BDC connection you must be a workspace admin, have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges, have a workspace enabled for [Unity Catalog](/concepts/unity-catalog.md), and have OpenSharing enabled on the [Metastore](/concepts/metastore.md) with users granted permissions to create and manage shares and recipients. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Creating an SAP BDC Connection

The creation process involves a two‑step exchange between a Databricks workspace admin and an SAP BDC admin. The user who creates the connection becomes its owner. Upon creation, two objects are automatically created: a **Provider** object (representing the SAP BDC account as a data provider) and a **Recipient** object (representing the SAP BDC account as a data recipient). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

#### Step 1: Obtain a connection identifier

1. In the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Click **Connection Identifier**.
4. Share the displayed partner identifier information with your SAP BDC admin.
5. Ask the SAP BDC admin to set up a Databricks connection on SAP BDC using that identifier, following the SAP BDC documentation. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

#### Step 2: Create the connection

1. After the SAP BDC admin sends back a Databricks connection invitation link, click **Connect to SAP BDC**.
2. Paste the invitation link into the **Connection link from SAP BDC** field.
3. Click **Connect**.
4. Once the connection is established, the SAP BDC account is automatically added as both a share provider and a recipient. You can then access shares granted by SAP BDC and OpenShare Databricks assets to SAP BDC.
5. Click **View provider** to see all received data products, or **View recipient** to see all shared data assets. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

After mounting a share received from SAP BDC to a Unity Catalog catalog, SAP semantic metadata (table/column comments, primary keys, foreign keys, and governance tags) syncs automatically into Unity Catalog. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Updating the Connection Owner

You must be the current connection owner or a [Metastore](/concepts/metastore.md) admin to change ownership. The new owner must be an individual user; ownership cannot be transferred to a group or service principal. To update:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Locate the connection, click the kebab menu, and select **Edit owner**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Deleting a Connection

Deleting the connection removes the Databricks workspace’s access to all data products shared by the SAP BDC admin and revokes the SAP BDC recipient’s access to Databricks shares. You must be the connection owner.

#### Step 1: Clean up shared assets

First, unmount any shares received from SAP BDC from their Unity Catalog catalogs. The catalog owner must perform this step. The connection cannot be deleted if any mounted catalogs still exist. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

#### Step 2: Delete the SAP BDC connection

After unmounting all shared assets:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Locate the connection, click the kebab menu, and select **Delete connection**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Limitations

- A [Metastore](/concepts/metastore.md) can have a maximum of five SAP BDC connections. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [OpenSharing](/concepts/opensharing.md)
- SAP Business Data Cloud
- Data Ingestion

### Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
