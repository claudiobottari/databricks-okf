---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e15d240421c3608fbe66cd9e0e798d76c5cf882157d88fee35594891b601990
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - core-schema-notation-csn-for-sap-bdc
    - CSN(FSB
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: Core Schema Notation (CSN) for SAP BDC
description: A schema notation used to describe data shares to SAP BDC so that SAP BDC users can read and interpret the shared data
tags:
  - sap
  - schema
  - data-sharing
  - interoperability
timestamp: "2026-06-19T19:01:47.782Z"
---

## Core Schema Notation (CSN) for SAP BDC

**Core Schema Notation (CSN)** is a schema description format used when sharing data from Databricks to an SAP Business Data Cloud (BDC) recipient via OpenSharing. When a share is granted to an SAP BDC recipient, a notebook using the SAP BDC SDK describes the share in CSN so that SAP BDC users can read the structure of the data assets. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

CSN is referenced in the context of defining a primary key for a shared table: any data asset shared with SAP BDC must have a primary key or identity column, and this can be defined in the CSN schema when sharing to SAP BDC. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

No further technical details about CSN itself (such as syntax, structure, or version) are provided in the source material.

## Related Concepts

- SAP Business Data Cloud (BDC) – The recipient system that consumes the CSN-described share.
- [OpenSharing](/concepts/opensharing.md) – The data sharing framework used to share data with SAP BDC.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol for OpenSharing.
- [SAP BDC SDK](/concepts/sap-bdc-sdk.md) – The Python library used to produce the CSN description.

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
