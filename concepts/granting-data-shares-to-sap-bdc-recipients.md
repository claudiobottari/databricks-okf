---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b21e06314d164054a5d90103dd8fe357cadbd1491a682de52d207c86f9f18d3
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - granting-data-shares-to-sap-bdc-recipients
    - GDSTSBR
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: Granting Data Shares to SAP BDC Recipients
description: The step-by-step process of granting an SAP BDC recipient access to specific OpenSharing shares in Databricks
tags:
  - databricks
  - sap
  - delta-sharing
  - sharing
timestamp: "2026-06-19T19:01:38.523Z"
---

# Granting Data Shares to SAP BDC Recipients

This page describes how to grant access to an [OpenSharing](/concepts/opensharing.md) data share for a recipient that represents an SAP Business Data Cloud (BDC) account. After the share is granted, you run a notebook that publishes the share’s schema in [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) so that SAP BDC users can discover and consume the data. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Requirements

Before granting a share, ensure the following prerequisites are met:

- A connection exists between your Databricks workspace and the SAP BDC account. See [Create and manage the SAP Business Data Cloud (BDC) connector](/concepts/sap-business-data-cloud-bdc-connector.md). ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]
- You have a share object that contains the data assets you want to share. See Create shares for OpenSharing. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]
- Every data asset in the share must have a primary key or identity column. You can enforce a primary key constraint on the table before sharing, or define the primary key in the CSN schema when publishing the share to SAP BDC. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]
- You must have one of the following privilege sets:
  - You are the share owner **and** have the `USE RECIPIENT` privilege.
  - You have the `USE RECIPIENT`, `USE SHARE`, and `SET SHARE PERMISSION` privileges. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Procedure

1. In your Databricks workspace, click the **Catalog** icon in the sidebar.
2. At the top of the Catalog pane, click the gear icon and select **OpenSharing**. Alternatively, in the upper-right corner of the Catalog pane, click **Share > OpenSharing**.
3. On the **Shared by me** tab, click **Recipients**.
4. Select the SAP BDC recipient. This recipient is automatically created when the connection with SAP BDC was established.
5. Click **Grant share** in the upper-right corner.
6. Select which shares the SAP BDC recipient should have access to.
7. Click **Grant**.
8. Run a notebook that uses the [SAP BDC SDK](/concepts/sap-bdc-sdk.md) to describe the share in Core Schema Notation so that SAP BDC users can read it. See Basic editing in Databricks notebooks for notebook instructions.

The notebook for publishing the share to SAP BDC is provided in the Databricks documentation as a downloadable example. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Post‑Grant Steps

After the share is granted, the SAP BDC account can access the shared data through its standard consumption tools. If you need to revoke access later, you can modify the grant settings from the same recipient view.

## Related Concepts

- SAP Business Data Cloud (BDC) – The recipient system that consumes the share.
- [OpenSharing](/concepts/opensharing.md) – The Delta Sharing framework used for cross‑platform data exchange.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol for sharing data outside Databricks.
- [Recipient (Delta Sharing)](/concepts/recipient-delta-sharing.md) – A logical entity that receives access to a share.
- [Share (Delta Sharing)](/concepts/delta-sharing.md) – A container for data assets that are shared with one or more recipients.
- [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) – The metadata language used to describe the schema to SAP BDC.
- [Primary Key Constraint](/concepts/primary-key-constraint-for-feature-tables.md) – Required for each table in the share to enable SAP BDC consumption.

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
