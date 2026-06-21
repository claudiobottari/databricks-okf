---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 231e87fac76df794d44363fccce6b1502b2427361e5f830fac651b12b81a7057
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - primary-key-requirement-for-shared-data
    - PKRFSD
    - primary-key-requirements-for-shared-data-assets
    - PKRFSDA
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: Primary Key Requirement for Shared Data
description: Requirement that any data asset shared with SAP BDC must have a primary key or identity column, which can be added before sharing or defined in the CSN schema.
tags:
  - data-governance
  - delta-sharing
  - constraints
timestamp: "2026-06-19T10:46:12.240Z"
---

# Primary Key Requirement for Shared Data

**Primary Key Requirement for Shared Data** is a foundational constraint in [Delta Sharing](/concepts/delta-sharing.md) and [OpenSharing](/concepts/opensharing.md): any data asset shared with an SAP Business Data Cloud (BDC) recipient must have a primary key (or an identity column) defined on it. This requirement ensures that the recipient can unambiguously reference, join, and update records.

## Why a primary key is required

OpenSharing delivers data to SAP BDC, which expects every shared table to have a **primary key** or **identity column**. Without this key, the recipient cannot determine which rows are unique, and operations such as incremental refresh, deduplication, or record-level updates become unreliable. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## How to satisfy the requirement

The primary key can be provided in one of two ways:

- **Before sharing**: add a primary key constraint to the table in your Databricks Catalog.
- **At share time**: define a primary key in the [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) schema that describes the share to SAP BDC.

Both approaches produce the same end result: the recipient sees a table with a declared primary key. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Step 1 – Granting access to the share

In your Databricks workspace, open the **Catalog** pane, click the gear icon, and select **OpenSharing**. On the **Shared by me** tab, click **Recipients**, then select the SAP BDC recipient. Click **Grant share** in the upper right, choose the shares the recipient should access, and click **Grant**. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

After granting, run the notebook that uses the SAP BDC Connect SDK to describe the share in CSN. The SDK allows SAP BDC to read the schema and understand which column is the primary key. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Related concepts

- [Primary key constraint](/concepts/primary-key-constraint-for-feature-tables.md) – the SQL mechanism that enforces uniqueness
- [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) – the schema language used by SAP BDC
- Delta Sharing with SAP BDC – end-to-end data sharing workflow
- [Create and manage the SAP BDC connector](/concepts/sap-bdc-connector.md) – the connection that makes sharing possible

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
