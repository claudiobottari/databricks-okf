---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4a5d1ff2a1fd8df62ca3c0f9f6c5f21b2b9b9fe70194c1714591f9225e0d700
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - primary-key-requirements-for-shared-data-assets
    - PKRFSDA
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: Primary Key Requirements for Shared Data Assets
description: Any data asset shared via SAP BDC must have a primary key or identity column defined before sharing
tags:
  - databricks
  - sap
  - data-governance
  - delta-sharing
timestamp: "2026-06-19T19:01:54.636Z"
---

# Primary Key Requirements for Shared Data Assets

**Primary Key Requirements for Shared Data Assets** refers to the mandatory constraint that any data asset shared with an SAP Business Data Cloud (BDC) recipient must have a primary key or identity column defined. This requirement ensures data integrity and enables proper identification of records when sharing data via [OpenSharing](/concepts/opensharing.md).

## Overview

When sharing data assets with SAP BDC recipients, each data asset included in a share object must have a primary key. This requirement applies to all tables that are shared through the [Delta Sharing](/concepts/delta-sharing.md) mechanism to SAP BDC. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Implementation Options

You can satisfy the primary key requirement in two ways:

1. **Add a primary key constraint before sharing**: Define a primary key constraint on the table within Databricks before including it in a share object. This is done using standard [Unity Catalog](/concepts/unity-catalog.md) table constraints.
2. **Define a primary key in the CSN schema**: When sharing to SAP BDC, you can define a primary key within the [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) schema that describes the share for SAP BDC users.

Both approaches achieve the same result: ensuring that the shared data asset has a unique identifier for each record. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Prerequisites

Before sharing data assets with SAP BDC recipients, you must have:

- A connection between your Databricks workspace and the desired SAP BDC account
- A share object with data assets to share with your SAP BDC recipient
- The appropriate permissions (share owner with `USE RECIPIENT` privilege, or `USE RECIPIENT`, `USE SHARE`, and `SET SHARE PERMISSION` privileges)

The primary key requirement must be met for any data asset in the share object. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Sharing Process

To share data assets with an SAP BDC recipient:

1. Navigate to **Catalog** in your Databricks workspace
2. Access the **OpenSharing** interface
3. Select the desired SAP BDC recipient (automatically created after connection establishment)
4. **Grant share** to the recipient
5. Select which shares the SAP BDC recipient should have access to
6. Run a notebook using the [SAP BDC SDK](/concepts/sap-bdc-sdk.md) to describe the share in Core Schema Notation

The CSN description step is necessary so SAP BDC users can read the shared data. The primary key can be defined either before the sharing process or within this CSN schema. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for sharing data assets across platforms
- [OpenSharing](/concepts/opensharing.md) — The Databricks interface for managing data shares
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where primary key constraints are defined
- SAP Business Data Cloud (BDC) — The recipient system consuming the shared data
- [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) — The schema format used to describe data shares to SAP BDC

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
