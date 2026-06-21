---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07cab37809847d2c85d2e44f2a737de07a77387417b039597444526d09d9fa5e
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-share-to-sap-bdc
    - GSTSB
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: Grant Share to SAP BDC
description: The workflow of granting an SAP BDC recipient access to selected shares through the Databricks OpenSharing interface.
tags:
  - delta-sharing
  - permissions
  - sap-bdc
timestamp: "2026-06-19T10:46:29.196Z"
---

# Grant Share to SAP BDC

**Grant Share to SAP BDC** refers to the process of sharing data assets from a Databricks workspace with an SAP Business Data Cloud (BDC) recipient using [Delta Sharing](/concepts/delta-sharing.md) and OpenSharing.

## Overview

Sharing data assets with SAP BDC recipients allows organizations to make their Databricks data available for consumption within SAP BDC environments. The process involves connecting a share object to an SAP BDC recipient, enabling SAP users to access the shared data through SAP's connector infrastructure. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Requirements

Before granting share to SAP BDC, the following prerequisites must be met:

- A connection must exist between the Databricks workspace and the desired SAP BDC account. This is established using the [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md). ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]
- A share object with data assets must exist in the workspace. See Create shares for OpenSharing. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]
- Any data asset shared must have a primary key or identity column. This can be added before sharing the table or defined in the Core Schema Notation (CSN) schema when sharing to SAP BDC. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]
- The user must meet one of the following privilege requirements:
  - Be the share owner with the `USE RECIPIENT` privilege
  - Have the `USE RECIPIENT`, `USE SHARE`, and `SET SHARE PERMISSION` privileges ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Procedure

### Step 1: Navigate to OpenSharing

In the Databricks workspace, click **Catalog**. At the top of the Catalog pane, click the gear icon and select **OpenSharing**. Alternatively, in the upper-right corner, click **Share > OpenSharing**. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

### Step 2: Select the SAP BDC Recipient

On the **Shared by me** tab, click **Recipients**. Select the desired SAP BDC recipient. This recipient is automatically created after the connection with SAP BDC is established. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

### Step 3: Grant Share

Click **Grant share** in the upper-right corner. Select which shares the SAP BDC recipient should have access to, then click **Grant**. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

### Step 4: Publish the Data Share

Run a notebook that uses the SAP BDC SDK to describe the share in Core Schema Notation so SAP BDC users can read it. For more information, see Basic editing in Databricks notebooks. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for data sharing across platforms
- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) — The connection mechanism between Databricks and SAP BDC
- [OpenSharing](/concepts/opensharing.md) — Databricks' implementation of Delta Sharing for external recipients
- Create shares for OpenSharing — Prerequisite step for creating share objects
- [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) — The schema description format used by SAP BDC

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
