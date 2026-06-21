---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de5a80410f3c7f857caa7fc95275ec10fed1f76cde8e3fd1e9457a195fdb37cb
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connection-ownership-and-deletion-prerequisites
    - Deletion Prerequisites and Connection Ownership
    - COADP
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Connection Ownership and Deletion Prerequisites
description: Connection ownership is restricted to individual users (not groups or service principals), and deleting a connection requires first unmounting all shared catalogs and being the connection owner.
tags:
  - databricks
  - sap-bdc
  - administration
  - security
timestamp: "2026-06-18T11:20:47.735Z"
---

# Connection Ownership and Deletion Prerequisites

**Connection Ownership and Deletion Prerequisites** describes the permissions, preparatory steps, and constraints required to change the owner of an SAP Business Data Cloud (BDC) connection or to delete it entirely. These rules ensure that shared data assets are properly unmounted before the connection is removed and that only authorized users can transfer or revoke the connection.

## Overview

An SAP BDC connection on Databricks represents a bilateral sharing relationship between a Databricks [Metastore](/concepts/metastore.md) and an SAP BDC account. Creating a connection automatically generates a **provider** object (for receiving shares) and a **recipient** object (for sending shares). The user who creates the connection becomes its owner. Ownership controls who can modify or delete the connection.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Ownership Requirements

- The current connection owner or a [Metastore](/concepts/metastore.md) admin can transfer ownership.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]
- The new owner **must be an individual user**. Connection ownership cannot be transferred to a group or a service principal.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

To update the owner via the UI:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Locate the connection and click the kebab menu (⋮).
4. Select **Edit owner**.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Deletion Prerequisites

Before you can delete an SAP BDC connection, the following must be true:

- **You are the owner of the connection.** Only the owner can delete it.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]
- **All shares received from SAP BDC must be unmounted** from Unity Catalog catalogs. The catalog owner must perform the unmount operation. If any mounted catalogs still exist, the connection cannot be deleted.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Step-by-Step Deletion

1. **Clean up shared assets**: Unmount every share received from SAP BDC from its associated catalog. See Unmount a share for the procedure.
2. **Delete the connection**: After unmounting, go to **Data Ingestion** > **SAP Business Data Cloud** > locate the connection > kebab menu > **Delete connection**.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Consequences of Deletion

- The Databricks workspace loses access to all data products shared by the SAP BDC admin.
- The SAP BDC recipient loses access to shares that were sent from Databricks.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Limitations

- There is a limit of **five connections per metastore**.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- SAP Business Data Cloud (BDC) — The external system that shares data with Databricks
- [OpenSharing](/concepts/opensharing.md) — The Delta Sharing protocol used for bidirectional sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that hosts mounted shares
- Mount a share — The operation that must be reversed before deletion
- Delta Sharing provider and recipient — The objects created automatically with the connection

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
