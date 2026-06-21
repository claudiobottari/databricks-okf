---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dcd0575ecf2d6cbbae8e08026f90ebf1755737cbd71be909a6d65c24dd877d75
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-level-connection-limit
    - MCL
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
      start: 52
      end: 54
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
      start: 20
      end: 23
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
      start: 27
      end: 31
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
      start: 26
      end: 30
title: Metastore-Level Connection Limit
description: A single Unity Catalog metastore can have at most five SAP BDC connections.
tags:
  - databricks
  - sap-bdc
  - limits
  - unity-catalog
timestamp: "2026-06-18T11:20:55.274Z"
---

# Metastore-Level Connection Limit

The **Metastore-Level Connection Limit** refers to a constraint in [Delta Sharing](/concepts/delta-sharing.md) that restricts the number of SAP Business Data Cloud (BDC) connections that can be established per [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). This limit ensures operational stability and prevents resource exhaustion within the sharing infrastructure.

## Overview

The connection limit is a boundary set at the [Metastore](/concepts/metastore.md) level, not at the workspace or account level. Each Unity Catalog [Metastore](/concepts/metastore.md) can support a maximum of **five** active [SAP BDC connections](/concepts/sap-bdc-connection.md) at any given time. This limit applies regardless of the number of workspaces or users within the organization that might need to establish connections to SAP BDC systems. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md:52-54]

## Connection Lifecycle

When a connection is created, two objects are automatically provisioned:

- A **Provider** object, which represents the SAP BDC account as a data source
- A **Recipient** object, which represents the Databricks workspace as a data consumer

These objects persist for the duration of the connection and are cleaned up when the connection is deleted. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md:20-23]

## Impact on Sharing

The connection limit directly affects the following [OpenSharing](/concepts/opensharing.md) capabilities:

- **Receiving shares**: SAP BDC admins can share data products with the Databricks workspace through the connection
- **Sending shares**: Databricks users can share data assets to SAP BDC accounts through the same connection
- **Semantic metadata**: After a share is mounted, SAP semantic metadata including table and column comments, primary keys, foreign keys, and [governance tags](/concepts/governed-tags.md) syncs automatically into Unity Catalog

## Configuration and Management

### Creating a Connection

To establish a connection, the following prerequisites must be met:

- The user must be a [workspace admin](/concepts/workspace-admin-unity-catalog.md)
- The user must have `CREATE PROVIDER` and `CREATE RECIPIENT` privileges
- The workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled
- [OpenSharing](/concepts/opensharing.md) must be enabled on the [Metastore](/concepts/metastore.md)

The connection process follows a two-step protocol:

1. The Databricks user generates a connection identifier from the **Data Ingestion** page
2. The SAP BDC admin uses this identifier to create a connection link on their end
3. The Databricks user completes the connection by providing the link received from the SAP admin

### Connection Ownership

Upon creation, the user becomes the **connection owner** and retains ownership throughout the connection's lifecycle. Ownership can only be transferred to another individual user—not to a group or service principal. The new owner must be a [Metastore](/concepts/metastore.md) admin. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md:27-31]

### Deleting a Connection

Before a connection can be deleted, all associated shares must be unmounted from the catalog. The catalog owner must perform the unmount operation. If mounted catalogs still exist, the connection cannot be removed. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md:26-30]

The deletion process:

1. Unmount all shares from the catalog
2. From the **Data Ingestion** page, locate the connection
3. Select **Delete connection**

After deletion, the Databricks workspace loses access to all data products previously shared by the SAP BDC admin, and the SAP BDC recipient loses access to all shares.

## Best Practices

Given the five-connection limit, consider the following:

- **Consolidate connections**: Where possible, use a single connection to manage multiple data flows rather than creating separate connections for each data product
- **Monitor connection count**: Regularly audit the number of active connections to ensure the limit is not approached unexpectedly
- **Plan for growth**: If more than five connections are needed, consider requesting a limit increase or restructuring the sharing architecture to reduce connection requirements

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying technology for sharing data between Databricks and SAP BDC
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that enforces the connection limit
- [OpenSharing](/concepts/opensharing.md) — The sharing protocol that enables connection establishment
- [SAP BDC connections](/concepts/sap-bdc-connection.md) — Individual connection instances that count toward the limit
- Connection identifier — The partner identifier used in the two-step connection protocol

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md:52-54](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
2. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md:20-23](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
3. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md:27-31](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
4. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md:26-30](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
