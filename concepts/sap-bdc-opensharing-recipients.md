---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d99cbb475f83767bddc0920441cbe8724de550ae1f862d9f4ce9b7992ca09671
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - sap-bdc-opensharing-recipients
    - SBOR
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: SAP BDC OpenSharing Recipients
description: Recipient entities automatically created in Databricks when an SAP BDC connection is established, used to manage share access
tags:
  - databricks
  - sap
  - delta-sharing
  - recipients
timestamp: "2026-06-19T19:01:55.384Z"
---

# SAP BDC OpenSharing Recipients

**SAP BDC OpenSharing Recipients** are entities within [Databricks Delta Sharing](/concepts/opensharing-databricks-delta-sharing.md) that represent connections to SAP Business Data Cloud (BDC) accounts. These recipients are automatically created when a connection between a Databricks workspace and an SAP BDC account is established, enabling data sharing from Databricks to SAP BDC. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Overview

An SAP BDC OpenSharing recipient serves as the target for sharing data assets from Databricks to SAP BDC. Once the SAP BDC connector is set up and a connection exists between the Databricks workspace and the SAP BDC account, the recipient is automatically created and appears in the OpenSharing interface. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Granting Share Access

To share data with an SAP BDC recipient, you must grant the recipient access to specific share objects that contain the data assets to be shared. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

### Requirements

Before granting access, you must have: ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

- A connection between your Databricks workspace and the desired SAP BDC account (see [SAP BDC Connector](/concepts/sap-bdc-connector.md)).
- A share object with data assets to share.
- Appropriate privileges: either the share owner with `USE RECIPIENT` privilege, or `USE RECIPIENT`, `USE SHARE`, and `SET SHARE PERMISSION` privileges.

### Data Asset Requirements

Any data asset shared with an SAP BDC recipient must have a primary key or identity column. This constraint can be satisfied by either: ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

- Adding a primary key constraint to the table before sharing.
- Defining a primary key in the Core Schema Notation (CSN) schema when sharing to SAP BDC.

### Granting Process

To grant access to an SAP BDC recipient: ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

1. Open **Catalog** in your Databricks workspace.
2. Click the gear icon and select **OpenSharing**, or click **Share > OpenSharing** in the upper-right corner.
3. On the **Shared by me** tab, click **Recipients**.
4. Select the desired SAP BDC recipient.
5. Click **Grant share** in the upper-right corner.
6. Select which shares the SAP BDC recipient should have access to.
7. Click **Grant**.

## Publishing Data to SAP BDC

After granting access, you must run a notebook that uses the [SAP BDC SDK](/concepts/sap-bdc-sdk.md) to describe the share in Core Schema Notation (CSN). This step is required so that SAP BDC users can read the shared data. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

The SAP BDC SDK is available as the `sap-bdc-connect-sdk` PyPI package. The notebook publishes the data share to SAP BDC in the CSN format. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for data sharing across platforms.
- [OpenSharing](/concepts/opensharing.md) — The Databricks interface for managing data shares and recipients.
- SAP Business Data Cloud (BDC) — The SAP platform for business data integration.
- [SAP BDC Connector](/concepts/sap-bdc-connector.md) — The mechanism for establishing connections between Databricks and SAP BDC.
- Share Objects — Collections of data assets shared with recipients.
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) — Required for data assets shared with SAP BDC.
- [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) — The schema format used to describe shared data to SAP BDC.

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
