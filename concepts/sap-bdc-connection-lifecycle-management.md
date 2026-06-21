---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 829d121c9a69d3d665418f42b98deba0217557214b89a135507c38c12a833c53
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection-lifecycle-management
    - SBCLM
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection Lifecycle Management
description: The process of creating, transferring ownership, and deleting SAP BDC connections on Databricks, including prerequisite cleanup steps for deletion.
tags:
  - administration
  - connection-lifecycle
  - sap-bdc
timestamp: "2026-06-19T18:00:05.222Z"
---

# SAP BDC Connection Lifecycle Management

**SAP BDC Connection Lifecycle Management** refers to the complete process of creating, maintaining, updating ownership, and deleting connections between a Databricks workspace and an SAP Business Data Cloud (BDC) account for OpenSharing. A connection is required to share data with and receive shares from an SAP BDC account. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Overview

The connection lifecycle involves several distinct stages: creation through a two-step process involving both a Databricks workspace admin and an SAP BDC admin, ongoing ownership management, and eventual deletion with prerequisite cleanup steps. Upon creation, two objects are automatically generated: a provider object and a recipient object, corresponding to the SAP BDC account. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Requirements

Before creating or managing an SAP BDC connection, the following prerequisites must be met:

- You must be a workspace admin.
- You must have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges.
- Your Databricks workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md).
- [OpenSharing](/concepts/opensharing.md) must be enabled on your [Metastore](/concepts/metastore.md), with users granted permissions to create and manage shares and recipients. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Creating a Connection

The creation process is a two-step workflow that requires coordination between a Databricks workspace admin and an SAP BDC admin. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 1: Obtain a Connection Identifier

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Click **Connection Identifier**.
4. Share the partner identifier information with your SAP BDC admin.
5. Ask your SAP BDC admin to set up a Databricks connection on SAP BDC using the provided identifier information (refer to the SAP BDC documentation for provisioning the connector). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 2: Create the Connection

1. After your SAP BDC admin returns the Databricks connection for your identifier, click **Connect to SAP BDC**.
2. In **Connection link from SAP BDC**, paste the invitation link sent by your SAP BDC admin.
3. Click **Connect**.
4. Once the connection is established, the SAP BDC account is automatically added as both a share provider and a share recipient.
5. Click **View provider** to see all data products received from the SAP BDC account, or **View recipient** to see all data assets shared with the SAP BDC account. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

After a share received from SAP BDC is mounted to a Unity Catalog catalog, SAP semantic metadata — including table and column comments, primary keys, foreign keys, and governance tags — syncs automatically into Unity Catalog. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Managing Connection Ownership

The connection owner is the user who created the connection. Ownership can be transferred, but only to another individual user — not to a group or a service principal. To update the owner, you must be the current connection owner or a [Metastore](/concepts/metastore.md) admin. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

To change the owner:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Find the connection and click the kebab menu (three vertical dots).
4. Select **Edit owner**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Deleting a Connection

Deleting a connection causes the Databricks workspace to lose access to all data products shared by the SAP BDC admin, and the SAP BDC recipient loses access to shares. You must be the owner of the connection to delete it. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 1: Clean Up Shared Assets

Before deletion, unmount any shares received from SAP BDC from catalogs. The catalog owner must perform this step. If mounted catalogs still exist, the connection cannot be deleted. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 2: Delete the Connection

After unmounting all shared assets:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Find the connection and click the kebab menu.
4. Select **Delete connection**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Limitations

- There is a limit of **five connections per metastore**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md)
- [OpenSharing](/concepts/opensharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- SAP BDC Semantic Metadata

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
