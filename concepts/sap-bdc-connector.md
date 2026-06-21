---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05e71aa78ac8c6f68c107d9fd9bab32a9e1df80a97a76ba218df3b1ecf41eb16
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connector
    - SBC
    - Create and manage the SAP BDC connector
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: SAP BDC Connector
description: The connection infrastructure between a Databricks workspace and an SAP Business Data Cloud account required before sharing data.
tags:
  - delta-sharing
  - sap-bdc
  - connector
timestamp: "2026-06-19T10:45:48.375Z"
---

Here is the wiki page for "SAP BDC Connector", written solely based on the provided source material.

---

## SAP BDC Connector

The **SAP BDC Connector** is a connection between a Databricks workspace and a SAP Business Data Cloud (BDC) account. It enables the sharing of data assets from Databricks to SAP BDC recipients using the [OpenSharing](/concepts/opensharing.md) protocol.

### Overview

The SAP BDC Connector is the underlying mechanism that establishes a link between your Databricks workspace and your SAP BDC environment. Once a connection is established, a corresponding recipient is automatically created in the Databricks OpenSharing interface, which can then be granted access to specific shares. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

### Requirements

Before data can be shared, a connection must exist between the Databricks workspace and the desired SAP BDC account. The process for establishing this connection is documented separately, and must be completed before proceeding with data sharing. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

### Sharing Data

Data is shared by granting a specific SAP BDC recipient access to one or more share objects. The recipient is created automatically upon the establishment of the SAP BDC Connector. To manage shares and recipients, navigate to the **OpenSharing** section in the Databricks **Catalog**. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

#### Prerequisites for Data Sharing

- A share object with data assets must exist. See Create shares for OpenSharing.
- Any data asset being shared must have a primary key or identity column. This can be added as a constraint before sharing, or defined in the CSN schema during the sharing process. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]
- The user must have the required privileges:
    - As the share owner, the `USE RECIPIENT` privilege.
    - Alternatively, have the `USE RECIPIENT`, `USE SHARE`, and `SET SHARE PERMISSION` privileges. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

#### Process

1.  In your Databricks workspace, navigate to the **OpenSharing** section (via the **Catalog** gear icon or **Share** menu).
2.  Select the **Shared by me** tab and click **Recipients**.
3.  Select the desired SAP BDC recipient (created automatically after establishing the connection).
4.  Click **Grant share**.
5.  Select the shares the recipient should have access to.
6.  Click **Grant**.

After granting access, a notebook using the [SAP BDC SDK](https://pypi.org/project/sap-bdc-connect-sdk/) must be run to describe the share in Core Schema Notation (CSN), making it readable by SAP BDC users. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

### Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The protocol used for sharing data between Databricks and external recipients, including SAP BDC.
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying data sharing framework for OpenSharing.
- SAP Business Data Cloud — The destination system for the shared data.
- [Create and manage the SAP Business Data Cloud (BDC) connector](/concepts/sap-business-data-cloud-bdc-connector.md) — The prerequisite setup task for the connector.
- Usage data shared with SAP — Data that is shared with SAP as part of the connection.

### Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
