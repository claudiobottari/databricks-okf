---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3f2e59857656b1865ebb8c9ebebd69f01fa98e39a0ba636dedc3f31a5158b99
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-semantic-metadata-synchronization
    - SBSMS
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP BDC Semantic Metadata Synchronization
description: When an SAP BDC share is mounted to a Unity Catalog catalog, SAP semantic metadata—including table/column comments, primary keys, foreign keys, and governance tags—automatically syncs into Unity Catalog.
tags:
  - metadata
  - unity-catalog
  - sap-bdc
  - governance
timestamp: "2026-06-18T11:20:34.536Z"
---

---
title: SAP BDC Semantic Metadata Synchronization
summary: The automatic synchronization of SAP semantic metadata (table and column comments, primary keys, foreign keys, and governance tags) into Unity Catalog when an SAP BDC share is mounted to a catalog.
sources:
  - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - sap
  - unity-catalog
  - metadata
  - delta-sharing
aliases:
  - sap-bdc-semantic-metadata-synchronization
  - SBDCSMS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# SAP BDC Semantic Metadata Synchronization

**SAP BDC Semantic Metadata Synchronization** refers to the automatic propagation of SAP-defined metadata into [Unity Catalog](/concepts/unity-catalog.md) after an SAP Business Data Cloud (BDC) share is mounted to a Unity Catalog catalog. This synchronization ensures that business context carried in SAP assets—such as descriptions, relationships, and governance classifications—is available directly within Databricks without manual replication.

## How Synchronization Works

After you establish an [SAP BDC Connection](/concepts/sap-bdc-connection.md) and mount a share received from SAP BDC to a Unity Catalog catalog, the SAP semantic metadata is synced automatically into Unity Catalog. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Synchronized Metadata Elements

The following SAP semantic metadata components are synchronized:

- **Table and column comments** – Business descriptions that document the meaning of tables and their columns.
- **Primary keys** – Identifies the columns that uniquely identify rows in each SAP table.
- **Foreign keys** – Defines the relationships between tables as modeled in SAP.
- **Governance tags** – SAP-defined classification and sensitivity labels that can drive ABAC policies in Unity Catalog.

## Prerequisites

To enable semantic metadata synchronization, you must:

- Complete the SAP BDC connection setup as described in [Create and manage the SAP BDC connector](/concepts/sap-bdc-connector.md).
- Mount a share received from the SAP BDC provider to a Unity Catalog catalog. See [Mount a share to a catalog](/concepts/share-to-catalog-mounting.md).

## Related Concepts

- SAP Business Data Cloud (BDC) – The source system providing the semantic metadata.
- [SAP BDC Connector](/concepts/sap-bdc-connector.md) – The Databricks connection object used to establish OpenSharing with SAP BDC.
- [Unity Catalog](/concepts/unity-catalog.md) – The Databricks governance layer that receives the synchronized metadata.
- [OpenSharing](/concepts/opensharing.md) – The protocol enabling cross-platform data sharing with SAP BDC.
- [Governed Tags](/concepts/governed-tags.md) – Tags that can be synchronized from SAP and used for attribute-based access control.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying sharing protocol used for data and metadata exchange.

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
