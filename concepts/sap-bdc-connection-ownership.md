---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a151af1385e39842d99cad95a1c83266e742d148bec94a74baebd0fdc06aed1a
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection-ownership
    - SBCO
    - Connection Ownership
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection Ownership
description: The ownership model for SAP BDC connections, where the creator becomes owner, ownership can only be transferred to individual users (not groups or service principals), and the owner is required to delete connections.
tags:
  - databricks
  - sap
  - access-control
  - governance
timestamp: "2026-06-19T14:35:10.796Z"
---

Here is the wiki page for "SAP BDC Connection Ownership".

---

## SAP BDC Connection Ownership

**SAP BDC Connection Ownership** refers to the user who owns an [SAP Business Data Cloud (BDC) connection](/concepts/sap-business-data-cloud-bdc-connector.md) on Databricks and has the authority to manage its lifecycle, including updating its metadata and deleting the connection. The connection owner is the user who created the connection. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### The Owner Role

The owner of an SAP BDC connection must be an individual user. A connection's ownership cannot be transferred to a group or a service principal. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Updating the Owner

To change the owner of an SAP BDC connection, the current connection owner or a [metastore admin](/concepts/metastore-admin-role.md) must use the Data Ingestion UI. The steps are:^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

1.  Navigate to **Data Ingestion** in the Databricks sidebar and select the **SAP Business Data Cloud** tile.
2.  Find the connection to update, click the kebab menu (the **...** icon), and select **Edit owner**.

### Deleting a Connection

Only the connection owner can delete an SAP BDC connection. Before the connection can be deleted, all shares received from the SAP BDC account must be unmounted from Unity Catalog catalogs. The owner of the catalog must perform this unmounting. If mounted catalogs still exist, the deletion will fail. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

The deletion process is:^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

1.  **Step 1: Clean up shared assets.** Unmount any shares received from SAP BDC from catalogs.
2.  **Step 2: Delete the SAP BDC connection.** From the **Data Ingestion** UI, select the SAP BDC tile, find the connection, and select **Delete connection**.

### Impact of Deletion

When a connection is deleted, the following occurs:^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

- The Databricks workspace loses access to all data products shared by the SAP BDC admin.
- The SAP BDC recipient loses access to all shares from Databricks.

### Related Concepts

- [SAP Business Data Cloud (BDC) connection](/concepts/sap-business-data-cloud-bdc-connector.md)
- [Metastore admin](/concepts/metastore-admin-role.md)
- Data Ingestion (UI)
- [Unity Catalog](/concepts/unity-catalog.md)
- [OpenSharing](/concepts/opensharing.md)

### Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
