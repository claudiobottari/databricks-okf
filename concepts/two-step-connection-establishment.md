---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8bc93315497feab109e13d167d3c23ce4dd092428dcece8966a83986fc08f854
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - two-step-connection-establishment
    - TCE
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Two-Step Connection Establishment
description: "Creating a Databricks–SAP BDC connection requires a two-party workflow: the Databricks admin shares a connection identifier with the SAP BDC admin, who generates a connection link that the Databricks admin uses to finalize the connection."
tags:
  - data-sharing
  - databricks
  - sap-bdc
  - workflow
timestamp: "2026-06-18T11:20:40.216Z"
---

# Two-Step Connection Establishment

**Two-step connection establishment** is the required process for creating an SAP Business Data Cloud (BDC) connection on Databricks. The connection is necessary for sharing data with and receiving shares from an SAP BDC account. The connection is created in two phases: the Databricks workspace sends a connection identifier to the SAP BDC admin, and the SAP BDC admin returns a connection link that finalises the connection. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Prerequisites

Before you can follow the two-step process, you must be a workspace admin, have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges, have a Unity Catalog-enabled workspace, and have enabled OpenSharing on the [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Step 1: Obtain a Connection Identifier

The Databricks workspace generates a connection identifier and shares it with the SAP BDC admin. From the Databricks sidebar, navigate to **Data Ingestion**, select the **SAP Business Data Cloud** tile, and click **Connection Identifier**. Provide the resulting partner identifier information to your SAP BDC admin and ask them to set up a Databricks connection on SAP BDC using that identifier. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Step 2: Create the SAP BDC Connection

After the SAP BDC admin sends back the Databricks connection link for your identifier, go to **Data Ingestion** > **SAP Business Data Cloud** and click **Connect to SAP BDC**. Paste the invitation link into **Connection link from SAP BDC** and click **Connect**. The connection is then established. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Automatic Object Creation

Upon successful two-step establishment, two objects are automatically created to correspond to the SAP BDC account:

- **Provider object** – allows you to view shares received from SAP BDC.
- **Recipient object** – allows you to share Databricks assets with SAP BDC.

After mounting a received share to a Unity Catalog catalog, SAP semantic metadata (table and column comments, primary keys, foreign keys, and governance tags) syncs automatically. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connection](/concepts/sap-business-data-cloud-bdc-connector.md)
- [OpenSharing](/concepts/opensharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Data Ingestion in Databricks
- SAP BDC Semantic Metadata

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
