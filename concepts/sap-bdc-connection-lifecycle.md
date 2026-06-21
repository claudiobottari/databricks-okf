---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 568ee5cc873f08f4f7cf31067cb50ef03b62116d999458fa65ce8834e4a09cd9
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection-lifecycle
    - SBCL
    - sap-bdc-connection-lifecycle-management
    - SBCLM
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection Lifecycle
description: The process of creating, updating ownership, and deleting an SAP BDC connection on Databricks including prerequisites and cleanup steps
tags:
  - data-sharing
  - sap
  - lifecycle
  - operations
timestamp: "2026-06-18T14:52:41.704Z"
---

# SAP BDC Connection Lifecycle

**SAP BDC Connection Lifecycle** refers to the sequence of steps for creating, managing, and removing a connection between Databricks and an SAP Business Data Cloud (BDC) account using OpenSharing. This connection enables bidirectional data sharing — both receiving data products from SAP BDC and sharing Databricks assets with SAP BDC. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Creation

Creating an SAP BDC connection is a two‑step process that requires coordination between a Databricks workspace admin and an SAP BDC admin.

1. **Obtain a connection identifier.** In the Databricks UI, navigate to **Data Ingestion**, select the **SAP Business Data Cloud** tile, and click **Connection Identifier**. Share the generated partner identifier information with the SAP BDC admin, who then uses it to set up a Databricks connection on the SAP BDC side (see [SAP BDC documentation](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provision-sap-business-data-cloud-connector-for-supported-external-systems)). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

2. **Connect using the invitation link.** Once the SAP BDC admin provides the connection link, return to the Databricks UI, click **Connect to SAP BDC**, paste the link into **Connection link from SAP BDC**, and click **Connect**. After the connection is established, the SAP BDC account is automatically added as both a share provider and a recipient. You can then view received data products via **View provider** or shared assets via **View recipient**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

Upon creation, two objects are automatically created corresponding to the SAP BDC account: a **Provider object** and a **Recipient object**. The user who creates the connection becomes its owner. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Owner Management

To update the connection owner, you must be the current connection owner or a [Metastore](/concepts/metastore.md) admin. The owner must be an individual user — ownership cannot be transferred to a group or service principal. To change ownership, go to **Data Ingestion** > **SAP Business Data Cloud** tile, find the connection, click the kebab menu, and select **Edit owner**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Deletion

Deleting an SAP BDC connection requires the connection owner and consists of two steps:

1. **Clean up shared assets.** Unmount any shares received from SAP BDC from Unity Catalog catalogs. The catalog owner must perform this step. If mounted catalogs still exist, deletion will fail. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

2. **Delete the connection.** After unmounting all shares, go to **Data Ingestion** > **SAP Business Data Cloud** tile, find the connection, click the kebab menu, and select **Delete connection**. Deletion removes access to all data products shared by the SAP BDC admin and revokes the SAP BDC recipient’s access to Databricks shares. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Automatic Metadata Sync

After you mount a share received from SAP BDC to a Unity Catalog catalog, SAP semantic metadata — including table and column comments, primary keys, foreign keys, and governance tags — synes automatically into Unity Catalog. For details, see the documentation on [SAP BDC semantic metadata](/concepts/sap-bdc-semantic-metadata-sync.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Limitations

There is a limit of **five connections per metastore**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that hosts the connection and managed shares.
- [OpenSharing](/concepts/opensharing.md) — The underlying Delta Sharing capability enabling cross‑platform data exchange.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol used for sharing data with SAP BDC.
- SAP Business Data Cloud (BDC) — The external system that provides data products.
- [SAP BDC semantic metadata](/concepts/sap-bdc-semantic-metadata-sync.md) — Automatic synchronization of table and column metadata.

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
