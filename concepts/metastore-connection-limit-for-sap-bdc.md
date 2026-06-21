---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 342d5c1b80a5c15c2ad16f01aea3aa2f139417744b60824e4cb364b3add42bb6
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-connection-limit-for-sap-bdc
    - MCLFSB
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Metastore Connection Limit for SAP BDC
description: A maximum of five SAP BDC connections can exist per Unity Catalog metastore.
tags:
  - databricks
  - limitations
  - administration
timestamp: "2026-06-19T09:35:04.316Z"
---

# [Metastore](/concepts/metastore.md) Connection Limit for SAP BDC

**Metastore Connection Limit for SAP BDC** refers to the restriction that a single [Metastore](/concepts/metastore.md) configured for [OpenSharing](/concepts/opensharing.md) in Databricks can have a maximum of five [SAP BDC connections](/concepts/sap-business-data-cloud-bdc-connector.md).

## Overview

When setting up connections between Databricks and SAP Business Data Cloud (BDC) for data sharing, the Databricks [Metastore](/concepts/metastore.md) enforces a hard limit of five SAP BDC connections. This means that an organization cannot establish more than five distinct SAP BDC account connections within the same [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Connection Limit Details

The limit of five connections applies across the entire [Metastore](/concepts/metastore.md). Each SAP BDC connection represents a pairing between a Databricks workspace and an SAP BDC account. When a user creates an SAP BDC connection, two objects are automatically created: a provider object and a recipient object, both of which correspond to the SAP BDC account. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

If you need to connect to more than five SAP BDC accounts, you would need to use a different [Metastore](/concepts/metastore.md) or work with your account team to understand alternative architectural options.

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) — The connection object used to share data between Databricks and SAP BDC
- [Metastore](/concepts/metastore.md) — The Unity Catalog [Metastore](/concepts/metastore.md) that contains the connection limit
- [OpenSharing](/concepts/opensharing.md) — The Delta Sharing protocol used for SAP BDC data exchange
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that manages metastores and connections
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol underlying OpenSharing

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
