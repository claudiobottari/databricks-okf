---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d9528847531e8f346dd4f0bd15d48fef1d5e06bb09d24f7f9792e8f07b0b9ed
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection-on-databricks
    - SBCOD
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection on Databricks
description: A configuration enabling bidirectional data sharing between SAP Business Data Cloud and Databricks via OpenSharing
tags:
  - data-sharing
  - databricks
  - sap
  - connector
timestamp: "2026-06-18T14:52:37.179Z"
---

# SAP BDC Connection on Databricks

The **SAP BDC Connection on Databricks** is a [Delta Sharing](/concepts/delta-sharing.md)-based integration that enables secure data exchange between SAP Business Data Cloud (BDC) and Databricks. This connection uses OpenSharing to establish a bi-directional link, allowing organizations to share data products and receive data assets between the two platforms.

## Overview

SAP BDC connections on Databricks enable organizations to exchange data using the OpenSharing protocol. When a connection is established, two objects are automatically created in the Databricks [Metastore](/concepts/metastore.md): a Provider object and a [Recipient](/concepts/data-recipient.md) object. These represent the SAP BDC account and allow data sharing in both directions. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Requirements

To create an SAP BDC connection, the following prerequisites must be met:

- The user must be a workspace admin
- The user must have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges
- The Databricks workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled
- [OpenSharing](/concepts/opensharing.md) must be enabled on the [Metastore](/concepts/metastore.md), with users granted permission to create and manage shares and recipients

^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Creating a Connection

Creating an SAP BDC connection is a two-step process that requires coordination between a Databricks admin and an SAP BDC admin.

### Step 1: Obtain a Connection Identifier

The Databricks admin generates a connection identifier from the **Data Ingestion** page in the Databricks sidebar. This identifier is shared with the SAP BDC admin, who uses it to set up a Databricks connection on SAP BDC. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 2: Complete the Connection

After the SAP BDC admin provides a connection link, the Databricks admin completes the connection by:

1. Selecting **Connect to SAP BDC** from the SAP Business Data Cloud tile
2. Pasting the invitation link from the SAP BDC admin
3. Clicking **Connect**

Once established, the SAP BDC account is automatically added as both a share provider and recipient. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Post-Connection Features

After a connection is established and a share is mounted to a Unity Catalog catalog, SAP semantic metadata automatically synchronizes into [Unity Catalog](/concepts/unity-catalog.md). This includes:

- Table and column comments
- Primary keys and foreign keys
- Governance tags

^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Managing Connections

### Updating Ownership

Connection ownership can be transferred to another user, but cannot be assigned to a group or service principal. The current owner or a [Metastore](/concepts/metastore.md) admin can perform this operation by editing the owner from the connection's kebab menu. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Deleting a Connection

Deleting a connection requires two steps. First, all mounted shares must be unmounted from catalogs. The catalog owner must perform this unmounting. If mounted catalogs still exist, the connection cannot be deleted. After unmounting, the connection can be removed from the SAP BDC tile's kebab menu. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

When a connection is deleted, the Databricks workspace loses access to all shared data products from the SAP BDC account, and the SAP BDC recipient loses access to shares from Databricks. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Limitations

- There is a limit of five connections per [Metastore](/concepts/metastore.md)

^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The sharing protocol underlying SAP BDC connections
- [OpenSharing](/concepts/opensharing.md) — The sharing model that enables bi-directional data exchange
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that manages shared assets
- SAP BDC Semantic Metadata — Automatic metadata synchronization from SAP
- [Provider and Recipient Objects](/concepts/sap-bdc-provider-and-recipient-objects.md) — The two automatically created objects in a connection

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
