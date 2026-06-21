---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 573f566c4a66cad504e2d0681148cadc222707a030d8a01a65c40f8f93a7f7b7
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-connection-limits-for-sap-bdc
    - MCLFSB
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Metastore Connection Limits for SAP BDC
description: A limit of five SAP BDC connections per Unity Catalog metastore, enforced as a hard upper bound.
tags:
  - limits
  - metastore
  - sap-bdc
timestamp: "2026-06-19T18:00:07.445Z"
---

# [Metastore](/concepts/metastore.md) Connection Limits for SAP BDC

**Metastore Connection Limits for SAP BDC** refers to the maximum number of SAP Business Data Cloud (BDC) connections that can exist per [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) on Databricks. This limit governs how many independent SAP BDC accounts can be linked to a single [Metastore](/concepts/metastore.md) for [OpenSharing](/concepts/opensharing.md) data exchange.

## Overview

When setting up an SAP BDC connector, each connection corresponds to an individual SAP BDC account and automatically creates both a provider and a recipient object in the [Metastore](/concepts/metastore.md). These connections are managed through the **Data Ingestion** sidebar under the SAP Business Data Cloud tile. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

The connection limit is enforced at the [Metastore](/concepts/metastore.md) level, meaning it applies to all workspaces that share the same Unity Catalog [Metastore](/concepts/metastore.md).

## Limit Details

The hard limit is **five connections per metastore**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

- If a [Metastore](/concepts/metastore.md) already has five SAP BDC connections, creating a sixth will fail.
- Each connection consumes one slot regardless of whether it is actively sharing data.
- Deleting a connection (after unmounting all associated shares) frees a slot.

## Implications

- **Planning**: Organizations that need to connect to more than five SAP BDC accounts from the same [Metastore](/concepts/metastore.md) must either use multiple metastores or consolidate accounts.
- **Cleanup**: Before deleting a connection, you must unmount all catalogs created from shares received through that connection. Otherwise, deletion is blocked. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]
- **Ownership**: Only the connection owner or a [Metastore](/concepts/metastore.md) admin can delete a connection; ownership cannot be transferred to a group or service principal. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) – Process for creating and managing a connection.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) layer where connections reside.
- [OpenSharing](/concepts/opensharing.md) – The Delta Sharing protocol used for SAP BDC data exchange.
- [Delta Sharing](/concepts/delta-sharing.md) – Broader framework for sharing data across platforms.
- Provider Object and Recipient Object – Automatically created per connection.

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
