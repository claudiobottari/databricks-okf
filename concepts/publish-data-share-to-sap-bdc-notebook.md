---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0640349d186ba6759c6f56396e388639ca43ea52a3b0d9a72cb2e879ebf32ee
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - publish-data-share-to-sap-bdc-notebook
    - PDSTSBN
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: Publish Data Share to SAP BDC Notebook
description: A Databricks notebook that uses the SAP BDC SDK to describe a share in Core Schema Notation (CSN) for consumption by SAP BDC users
tags:
  - databricks
  - sap
  - notebook
  - delta-sharing
timestamp: "2026-06-19T19:01:47.463Z"
---

# Publish Data Share to SAP BDC Notebook

The **Publish Data Share to SAP BDC Notebook** is a Databricks notebook that completes the process of sharing data assets with an SAP Business Data Cloud (BDC) recipient. Its purpose is to describe the share in [Core Schema Notation](/concepts/core-schema-notation-csn.md) (CSN) so that SAP BDC users can discover and read the shared data. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Role in the Sharing Workflow

The notebook is the final step after a share has been granted to an SAP BDC recipient. The preceding steps are:

1. Establish a connection between the Databricks workspace and the SAP BDC account (see [Create and manage the SAP BDC connector](/concepts/sap-bdc-connector.md)).
2. Create a share object with data assets that include a primary key or identity column (see Create shares for OpenSharing).
3. Grant the SAP BDC recipient access to the desired shares using the **Catalog** UI. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

After granting access, you run the **Publish Data Share to SAP BDC Notebook**. This notebook uses the [SAP BDC SDK](https://pypi.org/project/sap-bdc-connect-sdk/) to describe the share in Core Schema Notation, which is the metadata format that SAP BDC understands. Once published, SAP BDC users can read the shared data. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Prerequisites

Before running the notebook, the following must be in place:

- A connection exists between the Databricks workspace and the desired SAP BDC account.
- A share object has been created with data assets; each asset must have a primary key or identity column (either defined as a table constraint or specified in the CSN schema).
- The user performing the grant must be the share owner with the `USE RECIPIENT` privilege, or have the `USE RECIPIENT`, `USE SHARE`, and `SET SHARE PERMISSION` privileges.
- The share has been granted to the SAP BDC recipient. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The framework for sharing data outside of Databricks.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol used by OpenSharing.
- SAP Business Data Cloud (BDC) – The target system for the shared data.
- [Core Schema Notation](/concepts/core-schema-notation-csn.md) – The metadata format used to describe the share to SAP BDC.
- [SAP BDC SDK](/concepts/sap-bdc-sdk.md) – The Python library used in the notebook.
- [Data Shares for OpenSharing](/concepts/delta-sharing-open-sharing.md) – How to create and manage shares.

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
