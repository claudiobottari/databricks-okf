---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba60f49d3a42375d34042fea39d1648a4901d8b3a1557bbad2e99f650241b8be
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-provider-object
    - SBPO
    - Provider objects
    - SAP BDC provider
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Provider Object
description: An object automatically created upon SAP BDC connection establishment that represents the SAP BDC account as a data provider within Unity Catalog.
tags:
  - delta-sharing
  - provider
  - sap-bdc
timestamp: "2026-06-19T17:59:44.764Z"
---

# SAP BDC Provider Object

The **SAP BDC Provider Object** is a [Delta Sharing](/concepts/delta-sharing.md) provider object that is automatically created in [Unity Catalog](/concepts/unity-catalog.md) when a [SAP Business Data Cloud (BDC) Connection](/concepts/sap-business-data-cloud-bdc-connector.md) is established on Databricks. It represents the SAP BDC account from the Databricks perspective, enabling bidirectional data sharing through the OpenSharing protocol.

## Overview

When a Databricks workspace admin creates an [SAP BDC Connection](/concepts/sap-bdc-connection.md), the system automatically generates two Unity Catalog objects that correspond to the SAP BDC account: a provider object and a recipient object. The provider object allows Databricks to receive data products shared by the SAP BDC admin. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

The owner of the connection becomes the owner of both the provider and recipient objects. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Provider Object Functionality

Once the provider object exists, users can access shares granted by an SAP BDC admin directly from Databricks. After mounting a share received from SAP BDC to a [Unity Catalog](/concepts/unity-catalog.md) catalog, SAP semantic metadata—including table and column comments, primary keys, foreign keys, and governance tags—syncs automatically into Unity Catalog. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Viewing the Provider Object

After establishing the connection, users can view the provider object to see all data products received from the SAP BDC account. From the Databricks sidebar, navigate to **Data Ingestion**, select the SAP Business Data Cloud tile, and click **View provider**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP BDC Recipient Object](/concepts/sap-bdc-recipient-object.md) – The companion object for sharing Databricks assets to SAP BDC
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol for data sharing
- [OpenSharing](/concepts/opensharing.md) – The sharing mode used for SAP BDC connections
- [SAP BDC Connection](/concepts/sap-bdc-connection.md) – The connection that creates the provider and recipient objects
- SAP BDC Semantic Metadata – Metadata that syncs automatically when mounting shares

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
