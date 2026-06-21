---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b9b93a5f20005d0c836df51030ed33ddc5a8de21d12a80b94b418ee4e67b967
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection-deletion-workflow
    - SBCDW
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection Deletion Workflow
description: A two-step process requiring first unmounting all shares from Unity Catalog catalogs, then deleting the connection; after deletion, both Databricks loses access to SAP data products and SAP loses access to shared assets.
tags:
  - databricks
  - sap
  - lifecycle
  - cleanup
timestamp: "2026-06-19T14:35:06.843Z"
---

# SAP BDC Connection Deletion Workflow

The **SAP BDC Connection Deletion Workflow** describes the process for removing an [SAP BDC connection](/concepts/sap-business-data-cloud-bdc-connector.md) from a Databricks workspace. Deleting a connection revokes all data sharing between the workspace and the corresponding SAP BDC account, including access to shared data products and shares. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Prerequisites

- You must be the **owner** of the connection. Connection ownership cannot be transferred to a group or service principal. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]
- Any shares received from SAP BDC and mounted as Unity Catalog catalogs must be unmounted **before** deleting the connection. The owner of those catalogs is responsible for unmounting them. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Step 1: Clean Up Shared Assets

If any shares from the SAP BDC account are currently mounted as catalogs in Unity Catalog, the deletion will fail. To prevent this, unmount all such shares:

1. The catalog owner must navigate to the mounted share and unmount it. See Unmount a share for detailed instructions. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]
2. Verify that no catalogs originating from the SAP BDC connection remain mounted before proceeding.

## Step 2: Delete the SAP BDC Connection

Once all mounted shares are cleaned up, delete the connection through the Databricks UI:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Locate the connection you want to delete and click the kebab menu (three-dot icon).
4. Select **Delete connection**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Consequences of Deletion

After the connection is deleted:

- The Databricks workspace **loses access** to all data products the SAP BDC admin had shared through that connection.
- The SAP BDC recipient (the SAP BDC account) **loses access** to all shares that the Databricks workspace had granted. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

These effects are permanent; a new connection must be created and configured again to restore sharing.

## Limitations

- There is a limit of five connections per [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). Deleting a connection frees one slot in that limit. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) – Setup and management of the connection
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that manages catalogs, shares, and connections
- [OpenSharing](/concepts/opensharing.md) – The sharing framework used for SAP BDC integration
- Unmount a share – How to remove a mounted share from a catalog
- Data Ingestion – The Databricks UI entry point for connection management

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
