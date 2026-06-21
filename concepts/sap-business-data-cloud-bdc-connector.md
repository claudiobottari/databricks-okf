---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0759613890ae51b55e2f38aa9cff204d76ae1ef039da6b11c7112dcc98dfd61e
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-business-data-cloud-bdc-connector
    - SBDC(C
    - SAP Business Data Cloud (BDC) Connection
    - SAP Business Data Cloud (BDC) connection
    - SAP Business Data Cloud Connector
    - SAP Business Data Cloud connector
    - Create and manage the SAP Business Data Cloud (BDC) connector
    - SAP Business Data Cloud (BDC) integration
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: SAP Business Data Cloud (BDC) Connector
description: A Databricks connector that establishes a connection between a Databricks workspace and an SAP BDC account for data sharing
tags:
  - databricks
  - sap
  - delta-sharing
  - connector
timestamp: "2026-06-19T19:01:47.432Z"
---

# SAP Business Data Cloud (BDC) Connector

The **SAP Business Data Cloud (BDC) Connector** is a Databricks feature that enables sharing data assets with SAP Business Data Cloud recipients using OpenSharing. It allows organizations to securely share Databricks tables and other data assets with SAP BDC, enabling integration between the Databricks Lakehouse Platform and SAP's data cloud ecosystem. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Requirements

Before sharing data with an SAP BDC recipient, the following prerequisites must be met:

- A connection must exist between your Databricks workspace and the desired SAP BDC account. See [Create and manage the SAP Business Data Cloud (BDC) connector](/concepts/sap-business-data-cloud-bdc-connector.md).
- You must have a share object with data assets to share with your SAP BDC recipient. See Create shares for OpenSharing.
- Any data asset you share must have a primary key or identity column. You can add a primary key constraint before sharing the table or define a primary key in the Core Schema Notation (CSN) schema when sharing to SAP BDC.
- You must meet one of the following privilege requirements:
  - You are the share owner and have the `USE RECIPIENT` privilege.
  - You have the `USE RECIPIENT`, `USE SHARE`, and `SET SHARE PERMISSION` privileges.

^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Granting Access to SAP BDC Recipients

To share data assets with an SAP BDC recipient, follow these steps:

1. In your Databricks workspace, open **Catalog**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**. Alternatively, in the upper-right corner, click **Share > OpenSharing**.
3. On the **Shared by me** tab, click **Recipients**.
4. Select the desired SAP BDC recipient. This recipient is automatically created after the connection with SAP BDC is established.
5. Click **Grant share** in the upper-right corner.
6. Select which shares the SAP BDC recipient should have access to.
7. Click **Grant**.
8. Run the notebook that uses the SAP BDC SDK to describe the share in Core Schema Notation (CSN) so SAP BDC users can read it.

^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## SAP BDC SDK

The SAP Business Data Cloud integration requires the use of the [SAP BDC SDK](https://pypi.org/project/sap-bdc-connect-sdk/) (a Python package available on PyPI). After granting share access, you run a notebook that uses this SDK to describe the shared data in Core Schema Notation format, which enables SAP BDC users to read and consume the shared data assets. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The sharing framework used to distribute data assets to external recipients
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for secure data sharing across platforms
- [Create and manage the SAP Business Data Cloud (BDC) connector](/concepts/sap-business-data-cloud-bdc-connector.md) — Establishing the initial connection between Databricks and SAP BDC
- Create shares for OpenSharing — Creating share objects with data assets for distribution
- SAP BDC documentation — External SAP documentation for administering the connector

## Additional Resources

- [Usage data shared with SAP](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/#shared-data)
- [SAP BDC documentation](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provision-sap-business-data-cloud-connector-for-supported-external-systems)

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
