---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 882574c0788b5b416d4a7665e8a6065172d6c38f1f39956bbcdf0ae275d52ab0
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - opensharing-for-sap-bdc
    - OFSB
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: OpenSharing for SAP BDC
description: The Delta Sharing-based framework used to enable bidirectional data sharing between Databricks and SAP Business Data Cloud, requiring the metastore to have OpenSharing enabled.
tags:
  - delta-sharing
  - opensharing
  - sap-bdc
timestamp: "2026-06-19T18:00:20.506Z"
---

Here is the wiki page for "OpenSharing for SAP BDC".

## OpenSharing for SAP BDC

**OpenSharing for SAP BDC** refers to the integration between Databricks and SAP Business Data Cloud (BDC) that uses the [Delta Sharing](/concepts/delta-sharing.md) protocol to enable secure, bidirectional data sharing. This connection allows Databricks workspaces to both receive data products from an SAP BDC account and share Databricks data assets back to SAP BDC. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Overview

The integration is managed through a dedicated SAP BDC connection created within the Databricks workspace. The connection requires that the workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md) and that OpenSharing is enabled on the [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Creating an SAP BDC Connection

An SAP BDC connection must be established before any data sharing can occur. The creation process involves a two-step exchange between a Databricks workspace admin and an SAP BDC admin. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

1.  **Obtain and share a connection identifier.** From the Databricks sidebar, navigate to **Data Ingestion** and select the SAP Business Data Cloud tile. Click **Connection Identifier** and share the identifier with your SAP BDC admin, who will then set up a corresponding connection on the SAP BDC side. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]
2.  **Complete the connection.** After the SAP BDC admin generates and sends the invitation link back to the Databricks admin, click **Connect to SAP BDC**. Paste the invitation link into the **Connection link from SAP BDC** field and click **Connect**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

Once the connection is established, two objects are automatically created: a **Provider** object, which allows the workspace to view and mount shares from SAP BDC, and a **Recipient** object, which enables the workspace to grant SAP BDC access to Databricks shares. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Sharing Data with SAP BDC

After the connection is created, a Databricks workspace admin can grant an SAP BDC recipient access to OpenSharing data shares. The process involves the following steps: ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

1.  **Create or identify a share** containing the data assets to be shared.
2.  **Grant access** to the SAP BDC recipient. The admin selects the desired share, grants access to the SAP BDC recipient, and specifies which tables or partitions to include.

The SAP BDC admin can then accept the share on the SAP BDC side. For detailed instructions, see the documentation on Grant SAP BDC recipients access to OpenSharing data shares. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

#### Shared Data Categories

The following categories of usage data are shared with SAP BDC for each connection:

- **Usage by workspace:** Metrics for open model inference, MLflow runs, and model serving endpoint requests.
- **Compute and cost:** Timespan for cluster/serverless compute usage data.
- **Data Engineering:** Databricks SQL usage.
- **Identity:** User and service principal information.
- **Delta Sharing:** Outbound data transfer metrics.

### Receiving Data from SAP BDC

After the SAP BDC admin shares a data product, the Databricks admin can view all available data products by clicking **View provider** from the connection page. To make the data available for querying, the admin creates a catalog in Unity Catalog from the SAP BDC provider share. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

When a share from SAP BDC is mounted to a Unity Catalog catalog, SAP semantic metadata is automatically synced. This metadata includes table and column comments, primary keys, foreign keys, and governance tags. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Managing Connections

You must be the connection owner or a [Metastore](/concepts/metastore.md) admin to manage an SAP BDC connection.

- **Update connection owner:** From the **Data Ingestion** page, find the connection, click the kebab menu (⋮), and select **Edit owner**. Ownership must be transferred to an individual user; groups and service principals are not supported. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]
- **Delete a connection:** This is a two-step process. First, unmount any shares received from SAP BDC from their catalogs. Then, from the **Data Ingestion** page, find the connection, click the kebab menu (⋮), and select **Delete connection**. Deleting the connection removes access to all data products shared by SAP BDC and revokes SAP BDC's access to Databricks shares. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Limitations

- There is a limit of five SAP BDC connections per [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Requirements

- Workspace admin privileges.
- `CREATE PROVIDER` and `CREATE RECIPIENT` privileges.
- A workspace enabled for [Unity Catalog](/concepts/unity-catalog.md).
- OpenSharing enabled on the [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol underlying the SAP BDC integration.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer required for OpenSharing.
- SAP BDC Semantic Metadata – Automatically synced metadata from SAP data products.
- Create a Catalog from a Share – How to mount received shares for querying.
- Set up OpenSharing for your account – Prerequisite for enabling the integration.

### Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
