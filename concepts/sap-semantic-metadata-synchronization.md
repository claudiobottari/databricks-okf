---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e8130bdc3d2d9607bb7c7a43192bb6a5688524ff06cefb354794c520b64584ae
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-semantic-metadata-synchronization
    - SSMS
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: SAP Semantic Metadata Synchronization
description: When an SAP BDC share is mounted to a Unity Catalog catalog, SAP semantic metadata (table/column comments, primary keys, foreign keys, governance tags) syncs automatically into Unity Catalog.
tags:
  - databricks
  - metadata
  - unity-catalog
timestamp: "2026-06-19T09:34:59.348Z"
---

# SAP Semantic Metadata Synchronization

**SAP Semantic Metadata Synchronization** refers to the automatic propagation of SAP Business Data Cloud (BDC) semantic metadata into [Unity Catalog](/concepts/unity-catalog.md) when a share received from SAP BDC is mounted to a Unity Catalog catalog. After mounting the share, Unity Catalog automatically imports table and column comments, primary keys, foreign keys, and governance tags from the SAP BDC source. This synchronization ensures that Databricks users see the same business context that exists in the SAP system without manual re-creation. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

The synchronization occurs as a consequence of the [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) setup. Once an SAP BDC connection is established and a share is mounted to a catalog, the semantic metadata flows automatically into Unity Catalog. For more detailed information on the types of metadata synchronized and the sync behavior, see the SAP BDC semantic metadata documentation referenced in the connector guide. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md) – The connection object required to set up OpenSharing between SAP BDC and Databricks.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where the synchronized metadata is stored.
- [Delta Sharing / OpenSharing](/concepts/delta-sharing-open-sharing.md) – The protocol used to exchange data and metadata between SAP BDC and Databricks.
- [Governed Tags](/concepts/governed-tags.md) – Tags that are part of the synchronized governance metadata.

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
