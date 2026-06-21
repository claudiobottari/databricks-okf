---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2002654f9b718150bdad5ca0620e162073b6ce5eecf5a42a2d3a99b54c70c5e9
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-and-recipient-auto-creation
    - Recipient Auto-Creation and Provider
    - PARA
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Provider and Recipient Auto-Creation
description: When an SAP BDC connection is created on Databricks, two objects (a Provider and a Recipient) are automatically generated to represent the SAP BDC account for bidirectional sharing.
tags:
  - data-sharing
  - databricks
  - sap-bdc
  - automation
timestamp: "2026-06-18T11:20:36.708Z"
---

# Provider and Recipient Auto-Creation

**Provider and Recipient Auto-Creation** refers to the automatic creation of provider and recipient objects in [Unity Catalog](/concepts/unity-catalog.md) when establishing a connection with SAP Business Data Cloud (BDC) for OpenSharing. When a user creates an SAP BDC connection on Databricks, the system automatically creates two corresponding objects that represent the SAP BDC account: a provider object for receiving shares and a recipient object for sending shares. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## How It Works

When you create an SAP BDC connection, the Databricks system automatically generates:

1. **Provider object** — Represents the SAP BDC account as a data provider. This object allows you to access and mount data products (shares) that the SAP BDC admin has granted to your Databricks workspace.
2. **Recipient object** — Represents the SAP BDC account as a data recipient. This object enables you to share Databricks data assets with the SAP BDC account. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

After the connection is established, you can click **View provider** in the Databricks UI to see all data products received from the SAP BDC account, or **View recipient** to see all data assets you have shared with the SAP BDC account. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Relationship to Connection Creation

The provider and recipient objects are created as part of the two-step connection establishment process:

1. **Obtain a connection identifier**: The Databricks workspace generates a partner identifier that you share with an SAP BDC admin. The SAP BDC admin uses this identifier to set up a Databricks connection on SAP BDC and sends back a connection link.
2. **Establish the connection**: You paste the connection link from the SAP BDC admin into the Databricks UI and click **Connect**. Once the connection is established, the SAP BDC account is automatically added as both a share provider and a share recipient. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Impact of Connection Deletion

When you delete an SAP BDC connection, the associated provider and recipient objects are also removed. This means:

- The Databricks workspace loses access to all data products shared by the SAP BDC admin.
- The SAP BDC recipient loses access to any shares you had granted. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

Before deleting a connection, you must first clean up any mounted shares. You must unmount any shares received from SAP BDC from their associated [Unity Catalog](/concepts/unity-catalog.md) catalogs. The owner of the catalog must perform this step. If mounted catalogs still exist, you cannot delete the connection. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Requirements

To create a connection (which triggers provider and recipient auto-creation), you must:
- Be a workspace admin.
- Have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges.
- Have your Databricks workspace enabled for [Unity Catalog](/concepts/unity-catalog.md).
- Have enabled [OpenSharing](/concepts/opensharing.md) on your [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Limitations

- There is a limit of five connections per [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- SAP Business Data Cloud (BDC) — The SAP platform that connects with Databricks via OpenSharing
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that manages shares, providers, and recipients
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol used for data sharing with SAP BDC
- [OpenSharing](/concepts/opensharing.md) — The Databricks feature that enables sharing with non-Databricks platforms
- Mount a share — The process of attaching received shares to Unity Catalog catalogs

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
