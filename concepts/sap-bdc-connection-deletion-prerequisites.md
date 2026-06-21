---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfe976f72423b04ac5baa3b87022943d910658001da2655fa2545dac4392ec2f
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection-deletion-prerequisites
    - SBCDP
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection Deletion Prerequisites
description: Before deleting an SAP BDC connection, all mounted shares received from SAP BDC must be unmounted from Unity Catalog catalogs, or deletion is blocked.
tags:
  - databricks
  - sap-bdc
  - lifecycle
timestamp: "2026-06-19T09:35:12.868Z"
---

# SAP BDC Connection Deletion Prerequisites

**SAP BDC Connection Deletion Prerequisites** are the mandatory steps that must be completed before an [SAP Business Data Cloud (BDC) connection](/concepts/sap-business-data-cloud-bdc-connector.md) can be deleted from a Databricks workspace. These prerequisites ensure that shared data assets are properly cleaned up and that the deletion process does not leave orphaned shares or disrupt ongoing data access.

## Overview

Before deleting an SAP BDC connection, you must first clean up all shared assets that were received from the SAP BDC account. This ensures a clean disconnection and prevents data integrity issues. The connection owner is responsible for initiating the deletion process. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Step 1: Clean Up Shared Assets

The first prerequisite is to unmount any shares received from SAP BDC from Unity Catalog catalogs. The owner of the catalog must perform this unmounting operation. See Unmount a share for detailed instructions. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

If mounted catalogs still exist in the workspace, the connection cannot be deleted. All received shares must be fully unmounted before proceeding to the deletion step. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Step 2: Delete the SAP BDC Connection

After all shared assets are unmounted, the connection owner can proceed with the deletion. To delete a connection:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Find the connection you want to update and click the kebab menu icon.
4. Select **Delete connection**.
^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Consequences of Deletion

After the connection is deleted, the following occurs:

- The Databricks workspace loses access to all data products shared by the SAP BDC admin.
- The SAP BDC recipient loses access to shares previously granted.
- All associated provider and recipient objects are removed.
^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Prerequisites

You must be the owner of the connection to delete it. Connection ownership cannot be transferred to a group or service principal; it must be an individual user. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP BDC Connection](/concepts/sap-bdc-connection.md) — The connection object that facilitates data sharing
- Unmount a share — The process of removing mounted shared assets from catalogs
- [SAP BDC provider](/concepts/sap-bdc-provider-object.md) — The provider object created when establishing a connection
- [SAP BDC Recipient](/concepts/sap-bdc-recipient.md) — The recipient object created when establishing a connection

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
