---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84ac36ef30622e5a239232ead77f613abf5060ddb122f5ce2cc3958005218410
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-connection-limitations
    - SBCL
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Connection Limitations
description: A hard limit of five SAP BDC connections per Databricks metastore, enforced at the metastore level.
tags:
  - databricks
  - sap
  - limits
  - architecture
timestamp: "2026-06-19T14:35:57.063Z"
---

# SAP BDC Connection Limitations

**SAP BDC Connection Limitations** refers to the known constraints and operational prerequisites that apply when creating and managing an SAP Business Data Cloud (BDC) connection on Databricks for OpenSharing. These limitations affect how many connections can exist per environment, who can own or delete them, and what dependencies must be in place before a connection can be created or removed.

## Explicit Quota

The most direct limitation is a hard quota: **a [Metastore](/concepts/metastore.md) can have at most five SAP BDC connections**. This limit applies per [Metastore](/concepts/metastore.md), meaning any Unity Catalog [Metastore](/concepts/metastore.md) can only support five distinct SAP BDC accounts. If additional connections are needed, one must delete an existing connection before creating a new one.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Ownership Constraints

Connection ownership is restricted to individual users. Ownership **cannot** be transferred to a group or a service principal. This means that if the connection owner leaves the organization, a [Metastore](/concepts/metastore.md) admin must manually transfer ownership to another individual user. Only the owner (or a [Metastore](/concepts/metastore.md) admin) can update the owner of a connection.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Deletion Dependencies

A connection cannot be deleted while shares received from SAP BDC are still mounted to Unity Catalog catalogs. Before deletion, the owner of the catalog must unmount all such shares. If mounted catalogs still exist, the delete operation fails. This ensures that no dangling data references are left behind.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Creation Workflow Constraints

Creating a connection is a two-step process that requires coordination with an SAP BDC admin. The Databricks user must first obtain a connection identifier and share it with the SAP BDC admin, who then generates an invitation link. The Databricks user completes the connection using that link. No direct self-service creation is possible without this out-of-band exchange.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Prerequisite Requirements

Although not limitations of the connection itself, the following prerequisites must be met before an SAP BDC connection can be established:

- The user creating the connection must be a **workspace admin**.
- The workspace must have the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges granted to the user.
- The Databricks workspace must be **enabled for Unity Catalog**.
- **OpenSharing** must be enabled on the [Metastore](/concepts/metastore.md), and users must be granted permissions to create and manage shares and recipients.

Failure to satisfy any of these prerequisites prevents connection creation.^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer required for SAP BDC connections.
- [Delta Sharing](/concepts/delta-sharing.md) – The protocol underlying OpenSharing.
- SAP Business Data Cloud – The source system for shares.
- [Metastore](/concepts/metastore.md) – The catalog-level container that enforces the five-connection quota.
- [OpenSharing](/concepts/opensharing.md) – The feature that must be enabled to use the SAP BDC connector.
- [SAP BDC semantic metadata](/concepts/sap-bdc-semantic-metadata-sync.md) – Metadata that syncs automatically when shares are mounted.
- Data Ingestion – The UI workflow for creating connections.

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
