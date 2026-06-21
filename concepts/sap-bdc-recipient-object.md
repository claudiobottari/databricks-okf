---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b84371c17eb42e9f788b0372fd1236f23f700284bb999db50b475df8980943b5
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-recipient-object
    - SBRO
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Recipient Object
description: An object automatically created upon SAP BDC connection establishment that represents the SAP BDC account as a data recipient within Unity Catalog.
tags:
  - delta-sharing
  - recipient
  - sap-bdc
timestamp: "2026-06-19T17:59:54.544Z"
---

# SAP BDC Recipient Object

The **SAP BDC Recipient Object** is a Databricks object that is automatically created when an [SAP Business Data Cloud (BDC) connection](/concepts/sap-business-data-cloud-bdc-connector.md) is established. It represents the SAP BDC account as a recipient of data shares from the Databricks workspace, enabling cross-platform data sharing through [OpenSharing](/concepts/opensharing.md).

## Overview

When a Databricks workspace admin creates an SAP BDC connection, the system automatically generates two objects that correspond to the SAP BDC account: a Provider object and a Recipient object. The Recipient object represents the SAP BDC account as the consumer of data assets shared from Databricks.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

Through the Recipient object, you can view all data assets that you have shared with the SAP BDC account. This is accessed via the "View recipient" option after establishing the connection.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Lifecycle

The Recipient object is created automatically during Step 2 of the connection creation process, after the SAP BDC admin sends back the connection link. It exists as long as the SAP BDC connection exists.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

When a connection is deleted, the Databricks workspace loses access to all data products shared by the SAP BDC admin, and the SAP BDC recipient loses access to shares from Databricks. The deletion process requires first unmounting any shares received from SAP BDC from Unity Catalog catalogs.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Accessing the Recipient View

After the connection is established:

1. From the Databricks sidebar, click **Data Ingestion**.
2. Select the **SAP Business Data Cloud** tile.
3. Locate the established connection.
4. Click **View recipient** to see all data assets shared with the SAP BDC account.

^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP BDC Connection](/concepts/sap-bdc-connection.md) — The parent connection object that triggers creation of the Recipient object
- [SAP BDC Provider Object](/concepts/sap-bdc-provider-object.md) — The companion object representing the SAP BDC account as a data provider
- [OpenSharing](/concepts/opensharing.md) — The sharing protocol enabling cross-platform data exchange
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages data sharing
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for sharing data across platforms
- SAP Business Data Cloud (BDC) — The SAP platform that acts as the data sharing partner

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
