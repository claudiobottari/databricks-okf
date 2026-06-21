---
title: Create and manage the SAP Business Data Cloud (BDC) connector | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/create-connection
ingestedAt: "2026-06-18T08:05:41.392Z"
---

This page explains how to set up an SAP Business Data Cloud (BDC) connection on Databricks for OpenSharing. This connection is necessary for sharing with and receiving shares from an SAP BDC account.

## Requirements[​](#requirements "Direct link to Requirements")

*   You must be be a workspace admin.
*   You must have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges.
*   Your Databricks workspace is enabled for Unity Catalog. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).
*   You have enabled OpenSharing on your metastore and granted users to create and manage shares and recipients. See [Set up OpenSharing for your account (for providers)](https://docs.databricks.com/aws/en/delta-sharing/set-up).

## Create an SAP BDC connection on Databricks[​](#create-an-sap-bdc-connection-on-databricks "Direct link to create-an-sap-bdc-connection-on-databricks")

You must create an SAP BDC connection before granting data access to, or receiving data from, an SAP BDC account. The user who creates the SAP BDC connection becomes its owner. Upon creation, two objects are automatically created and corresponds to the SAP BDC account:

*   Provider object
*   Recipient object

To create a connection, you must first send a Databricks connection identifier to an SAP BDC admin. The SAP BDC admin then uses the connection identifier to generate a connection link on SAP BDC. With the connection link, you finish creating the SAP BDC connection on Databricks.

### Step 1: Obtain a connection identifier for an SAP BDC admin[​](#step-1-obtain-a-connection-identifier-for-an-sap-bdc-admin "Direct link to step-1-obtain-a-connection-identifier-for-an-sap-bdc-admin")

1.  From the Databricks sidebar, click **Data Ingestion**.
2.  Select the SAP Business Data Cloud tile.
3.  Click **Connection Identifier**.
4.  Share the partner identifier information with your SAP BDC admin.
5.  Ask your SAP BDC admin to set up a Databricks connection on SAP BDC using the provided identifier information. See [the SAP BDC documentation](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provision-sap-business-data-cloud-connector-for-supported-external-systems).

### Step 2: Create an SAP BDC connection[​](#step-2-create-an-sap-bdc-connection "Direct link to step-2-create-an-sap-bdc-connection")

1.  After your SAP BDC admin sends you the Databricks connection for your identifier, click **Connect to SAP BDC**.
2.  In **Connection link from SAP BDC**, copy the invitation link sent from your SAP BDC admin.
3.  Click **Connect**.
4.  After the connection is established, the SAP BDC account is automatically added as a share provider and recipient. You can access shares granted by an SAP BDC admin on Databricks and openshare Databricks assets to SAP BDC.
5.  Click **View provider** to see all data products received from the SAP BDC account. Or click **View recipient** to see all data assets you have shared with the SAP BDC account.

After you mount a share received from SAP BDC to a Unity Catalog catalog, SAP semantic metadata (table and column comments, primary keys, foreign keys, and governance tags) syncs automatically into Unity Catalog. For details, see [SAP BDC semantic metadata](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/semantic-metadata).

## Update connection owner[​](#update-connection-owner "Direct link to update-connection-owner")

You must be the connection owner or a metastore admin to update the owner of a connection.

note

The owner of the connection must be an individual user. You cannot transfer connection ownership to a group or a service principal.

To change the owner of a connection, do the following:

1.  From the Databricks sidebar, click **Data Ingestion**.
2.  Select the SAP Business Data Cloud tile.
3.  Find the connection you want to update and click ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==).
4.  Select **Edit owner**.

## Delete a connection[​](#delete-a-connection "Direct link to delete-a-connection")

After the connection is deleted, the Databricks workspace loses access to all data products shared by the SAP BDC admin and the SAP BDC recipient loses access to shares.

You must be the owner of the connection.

### Step 1: Clean up shared assets[​](#step-1-clean-up-shared-assets "Direct link to Step 1: Clean up shared assets")

Unmount any shares received from SAP BDC from catalogs. The owner of the catalog must do this. See [Unmount a share](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#unmount-share).

If mounted catalogs still exist, you cannot delete the connection.

### Step 2: Delete the SAP BDC connection[​](#step-2-delete-the-sap-bdc-connection "Direct link to Step 2: Delete the SAP BDC connection")

After unmounting all shared assets, do the following to delete an SAP BDC connection:

1.  From the Databricks sidebar, click **Data Ingestion**.
2.  Select the SAP Business Data Cloud tile.
3.  Find the connection you want to update and click ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==).
4.  Select **Delete connection**.

## Limitations[​](#limitations "Direct link to Limitations")

*   There is a limit of five connections per metastore.

## Next steps[​](#next-steps "Direct link to Next steps")

*   To read SAP BDC data in Databricks, create a catalog from the SAP BDC provider share. See [Create a catalog from a share](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#create-catalog)
*   [Grant SAP Business Data Cloud (BDC) recipients access to OpenSharing data shares](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/share-to-sap)
*   [SAP BDC semantic metadata](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/semantic-metadata)
*   [Usage data shared with SAP](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/#shared-data)
