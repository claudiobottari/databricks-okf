---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 152b0926d99a868e8818ff4052da0c823b31ab6c9783b07158feca8c6f53a299
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connection-identifier-exchange
    - CIE
    - connection-identifier-exchange-protocol
    - CIEP
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Connection Identifier Exchange
description: The handshake process where a Databricks workspace generates a connection identifier, shares it with an SAP BDC admin who produces a connection link, which is then used to finalize the connection on Databricks.
tags:
  - databricks
  - sap
  - authentication
  - workflow
timestamp: "2026-06-19T14:35:08.687Z"
---

# Connection Identifier Exchange

**Connection Identifier Exchange** is a step in the SAP Business Data Cloud (BDC) connector setup process on Databricks. It involves sharing a unique Databricks connection identifier with an SAP BDC admin, who then uses that identifier to generate a connection link on the SAP BDC side. This exchange is required before a secure OpenSharing connection can be established between Databricks and SAP BDC.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Overview

When setting up an SAP BDC connection on Databricks for [OpenSharing](/concepts/opensharing.md), the workspace admin must first generate a connection identifier and send it to an SAP BDC admin. The SAP BDC admin uses this identifier to configure a Databricks connection within SAP BDC and returns a connection link. The workspace admin then uses that link to finalize the connection on Databricks.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Process

### Step 1: Obtain a Connection Identifier

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Click **Connection Identifier**.
4. Share the partner identifier information with your SAP BDC admin.
5. Ask your SAP BDC admin to set up a Databricks connection on SAP BDC using the provided identifier information. See the SAP BDC documentation for details on provisioning the connector.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Step 2: Create the Connection Using the Returned Link

1. After your SAP BDC admin sends you the Databricks connection for your identifier, click **Connect to SAP BDC**.
2. In **Connection link from SAP BDC**, copy the invitation link sent from your SAP BDC admin.
3. Click **Connect**.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## After Connection

Once the connection is established, the SAP BDC account is automatically added as both a share provider and a share recipient. You can access shares granted by the SAP BDC admin on Databricks and also OpenShare Databricks assets to SAP BDC. Click **View provider** to see all data products received from the SAP BDC account, or **View recipient** to see all data assets you have shared with the SAP BDC account.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

After mounting a share received from SAP BDC to a Unity Catalog catalog, SAP semantic metadata (table and column comments, primary keys, foreign keys, and governance tags) syncs automatically into Unity Catalog.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md)
- [OpenSharing](/concepts/opensharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Sharing](/concepts/delta-sharing.md)

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
