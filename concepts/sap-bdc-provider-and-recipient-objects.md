---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b06bd755bcb33a00ffdbee02d9b31e23d254ffd9c6ea7daa81a522605a8cf91c
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-provider-and-recipient-objects
    - Recipient Objects and SAP BDC Provider
    - SBPARO
    - Provider and Recipient Objects
    - Provider and Recipient objects
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Provider and Recipient Objects
description: Two automatically created Unity Catalog objects (provider and recipient) that represent the SAP BDC account for sharing and receiving data.
tags:
  - databricks
  - unity-catalog
  - delta-sharing
timestamp: "2026-06-19T09:34:45.176Z"
---

# SAP BDC Provider and Recipient Objects

**SAP BDC Provider and Recipient Objects** are automatically created Databricks objects that represent the two-way data sharing relationship between a Databricks workspace and an SAP Business Data Cloud (BDC) account. These objects are generated when an SAP BDC connection is established and enable bidirectional data exchange through OpenSharing.

## Overview

When a user creates an SAP BDC connection on Databricks, two objects are automatically created that correspond to the SAP BDC account: a **provider object** and a **recipient object**. These objects facilitate the sharing of data products between Databricks and SAP BDC. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Provider Object

The provider object represents the SAP BDC account as a data provider to Databricks. Through this object, Databricks can access data products that an SAP BDC admin has shared with the workspace. After a connection is established, users can click **View provider** to see all data products received from the SAP BDC account. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Recipient Object

The recipient object represents the SAP BDC account as a data recipient from Databricks. Through this object, Databricks can share data assets with the SAP BDC account using OpenSharing. Users can click **View recipient** to see all data assets that have been shared with the SAP BDC account. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Automatic Creation

Both objects are created automatically when the SAP BDC connection is established. The user who creates the connection becomes its owner. After the connection is established, the SAP BDC account is automatically added as both a share provider and a share recipient. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Accessing Shared Data

After mounting a share received from SAP BDC to a Unity Catalog catalog, SAP semantic metadata — including table and column comments, primary keys, foreign keys, and governance tags — syncs automatically into Unity Catalog. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Deletion Impact

When an SAP BDC connection is deleted, both the provider and recipient objects are removed. This means the Databricks workspace loses access to all data products shared by the SAP BDC admin, and the SAP BDC recipient loses access to shares from Databricks. Before deleting a connection, all shares received from SAP BDC must be unmounted from catalogs. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) — The connection that enables data sharing between Databricks and SAP BDC
- [OpenSharing](/concepts/opensharing.md) — The Delta Sharing protocol used for bidirectional data exchange
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where shared data is mounted and managed
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying technology for sharing data across platforms
- SAP BDC Semantic Metadata — Metadata that syncs automatically when shares are mounted

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
