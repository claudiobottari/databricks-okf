---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: da416e6c92a804706559ef3f2d8ae1ce5de99388edd8b176a663433121c15bbe
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-recipient
    - SBR
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: SAP BDC Recipient
description: A Delta Sharing recipient automatically created when a Databricks-to-SAP BDC connection is established, used to grant data share access.
tags:
  - delta-sharing
  - sap-bdc
  - recipient-management
timestamp: "2026-06-19T10:45:47.537Z"
---

# SAP BDC Recipient

An **SAP BDC Recipient** is a Databricks [OpenSharing](/concepts/opensharing.md) recipient automatically created after a connection is established between a Databricks workspace and an SAP Business Data Cloud (BDC) account. This recipient enables sharing data assets from Databricks to SAP BDC users via OpenSharing. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Requirements

Before granting access to an SAP BDC recipient, ensure the following prerequisites are met:

- A connection exists between your Databricks workspace and the desired SAP BDC account. See [SAP BDC Connector](/concepts/sap-bdc-connector.md).
- You have a share object with data assets to share with the SAP BDC recipient. See Create shares for OpenSharing.
- Every data asset shared must have a primary key or identity column. You can add a primary key constraint before sharing the table, or define a primary key in the CSN schema when sharing to SAP BDC.
- You meet one of the following privilege requirements:
  - You are the share owner and have the `USE RECIPIENT` privilege.
  - You have the `USE RECIPIENT`, `USE SHARE`, and `SET SHARE PERMISSION` privileges.

^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Granting Shares to an SAP BDC Recipient

To grant access to data shares using an SAP BDC recipient:

1. In your Databricks workspace, click **Catalog**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**. Alternatively, in the upper-right corner, click **Share > OpenSharing**.
3. On the **Shared by me** tab, click **Recipients**.
4. Select the desired SAP BDC recipient. This recipient is automatically created after the connection with SAP BDC is established.
5. Click **Grant share** in the upper-right corner.
6. Select which shares the SAP BDC recipient should have access to.
7. Click **Grant**.
8. Run a notebook that uses the [SAP BDC SDK](/concepts/sap-bdc-sdk.md) to describe the share in Core Schema Notation (CSN) so that SAP BDC users can read it.

^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Additional Resources

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for OpenSharing.
- SAP BDC Documentation (External) — Official SAP documentation on provisioning the BDC connector.
- Usage data shared with SAP — Information about what telemetry Databricks shares with SAP when using the BDC connector.

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
