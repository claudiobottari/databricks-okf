---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e608b004514185f2d1059487d9b3bdd5fb607dea6d5288253f9519e46b500bb7
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-provider-and-recipient-objects
    - Recipient Objects and Automatic Provider
    - APARO
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Automatic Provider and Recipient Objects
description: Two objects automatically created when an SAP BDC connection is established, enabling bidirectional sharing
tags:
  - data-sharing
  - sap
  - databricks
timestamp: "2026-06-18T14:52:53.379Z"
---

# Automatic Provider and Recipient Objects

**Automatic Provider and Recipient Objects** refers to a behavior of the [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) on Databricks, where establishing a connection to an SAP BDC account automatically creates two managed objects in Unity Catalog: a **provider** object (for receiving shares) and a **recipient** object (for sending shares).^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Overview

When a user creates an [SAP BDC Connection](/concepts/sap-bdc-connection.md) on Databricks, the system automatically creates two corresponding objects that represent the SAP BDC account in Databricks' [OpenSharing](/concepts/opensharing.md) framework:^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

- **Provider object** — Represents the SAP BDC account as a share provider, allowing the Databricks workspace to view and mount data products (shares) that the SAP BDC admin has granted access to.
- **Recipient object** — Represents the SAP BDC account as a share recipient, enabling the Databricks workspace to share (OpenShare) Databricks assets with the SAP BDC account.

These objects are created automatically upon successful connection establishment and are managed by the connection's owner.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Lifecycle

### Creation

Both objects are created automatically when the connection setup is completed. After the SAP BDC admin sends the invitation link and the Databricks user clicks **Connect**, the connection is established, and the provider and recipient objects are created in the background.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Usage

Users can navigate to these objects from the connection administrative interface:^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

- Clicking **View provider** shows all data products (shares) received from the SAP BDC account, which can be mounted to [Unity Catalog](/concepts/unity-catalog.md) catalogs.
- Clicking **View recipient** shows all data assets that have been shared with the SAP BDC account.

### Deletion

When a connection is deleted, the Databricks workspace loses access to all data products shared by the SAP BDC admin, and the SAP BDC recipient loses access to shares. Before deleting a connection, users must first unmount any shares received from SAP BDC from catalogs. If mounted catalogs still exist, the connection cannot be deleted.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Permissions

The user who creates the SAP BDC connection becomes the owner of both the connection and the automatically created provider and recipient objects. The owner must be an individual user — connection ownership cannot be transferred to a group or service principal.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

To create the connection, the user must be a workspace admin and have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for secure data sharing between Databricks and external systems
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that manages providers and recipients
- [OpenSharing](/concepts/opensharing.md) — The Databricks feature that enables creating and managing shares and recipients
- SAP Business Data Cloud (BDC) — The SAP data platform that can share data with Databricks
- [SAP BDC semantic metadata](/concepts/sap-bdc-semantic-metadata-sync.md) — Metadata (table comments, primary keys, foreign keys, governance tags) that syncs automatically when a share is mounted

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
