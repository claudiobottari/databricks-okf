---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe4b6396eaa5fafcfbc6e553a4482277d88167570600ea670601a72b85be2eb7
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connection-identifier-exchange-protocol
    - CIEP
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Connection Identifier Exchange Protocol
description: A two-phase handshake where a Databricks-generated connection identifier is provided to an SAP BDC admin, who returns a connection link to finalize the connection.
tags:
  - databricks
  - sap-bdc
  - workflow
timestamp: "2026-06-19T09:35:00.611Z"
---

# Connection Identifier Exchange Protocol

The **Connection Identifier Exchange Protocol** is the process by which a Databricks workspace and an SAP Business Data Cloud (BDC) account establish a secure connection for sharing data. It involves exchanging connection identifiers between the two systems to generate an invitation link that completes the connection on the Databricks side. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Overview

Before granting data access to or receiving data from an SAP BDC account, a Databricks workspace admin must create an SAP BDC connection. The creation process requires a two-step exchange: first, the Databricks admin generates a connection identifier and shares it with an SAP BDC admin; second, the SAP BDC admin uses that identifier to produce a connection link, which the Databricks admin then uses to finalize the connection. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

Upon successful creation, two objects are automatically generated in Databricks: a **Provider object** and a **Recipient object**. The Provider object represents the SAP BDC account as a data provider that can share data products to Databricks. The Recipient object represents the Databricks workspace as a data recipient for sharing Databricks assets back to SAP BDC. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Protocol Flow

### Step 1: Obtain a Connection Identifier

To initiate the protocol, a Databricks workspace admin performs the following: ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the SAP Business Data Cloud tile.
3. Click **Connection Identifier**.
4. Share the partner identifier information with the SAP BDC admin.
5. The SAP BDC admin uses the identifier to set up a Databricks connection on the SAP BDC side. See the SAP BDC documentation on provisioning a connector for supported external systems.

### Step 2: Create the Connection

After the SAP BDC admin generates an invitation link from the connection identifier, the Databricks admin completes the connection: ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

1. Click **Connect to SAP BDC**.
2. In **Connection link from SAP BDC**, paste the invitation link sent by the SAP BDC admin.
3. Click **Connect**.
4. After the connection is established, the SAP BDC account is automatically added as a share provider and recipient.

## Post-Connection Behavior

Once the connection is established: ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

- The Databricks workspace gains access to all data products shared by the SAP BDC admin.
- Databricks can OpenShare assets back to the SAP BDC account.
- SAP semantic metadata (table and column comments, primary keys, foreign keys, and governance tags) syncs automatically into Unity Catalog when a share received from SAP BDC is mounted to a Unity Catalog catalog.

## Requirements

To participate in the protocol, the following prerequisites must be met: ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

- The user must be a workspace admin.
- The user must have `CREATE PROVIDER` and `CREATE RECIPIENT` privileges.
- The Databricks workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md).
- OpenSharing must be enabled on the [Metastore](/concepts/metastore.md), with users granted permission to create and manage shares and recipients.

## Limitations

- There is a limit of five connections per [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Connection Lifecycle

### Ownership Transfer

The connection owner must be an individual user. Ownership cannot be transferred to a group or service principal. To update the owner, the current owner or a [Metastore](/concepts/metastore.md) admin uses the **Edit owner** option from the connection's kebab menu. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Deletion

To delete an SAP BDC connection, the owner must first unmount all shares received from SAP BDC from any catalogs. If mounted catalogs still exist, the connection cannot be deleted. After unmounting, the owner uses the **Delete connection** option from the connection's kebab menu. Once deleted, the Databricks workspace loses access to all data products shared by the SAP BDC admin, and the SAP BDC recipient loses access to shares. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) — The full configuration for establishing and managing BDC connections on Databricks.
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol used for data sharing between systems.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer required for OpenSharing.
- [OpenSharing](/concepts/opensharing.md) — The Databricks feature that enables sharing data across platforms.

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
