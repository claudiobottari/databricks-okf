---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b1f7746ff25190876ec65b19fabaed7d4d5fcfe0c2f8ec11c0f47759c8e82a1
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-connection-limits
    - MCL
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Metastore Connection Limits
description: A limitation restricting the number of SAP BDC connections to five per metastore in Databricks
tags:
  - limitations
  - databricks
  - governance
timestamp: "2026-06-18T14:52:50.803Z"
---

## [Metastore](/concepts/metastore.md) Connection Limits

**Metastore Connection Limits** refer to the maximum number of allowed connections from a [Delta Sharing](/concepts/delta-sharing.md) [Metastore](/concepts/metastore.md) to SAP Business Data Cloud (BDC) for OpenSharing. This limit is an operational constraint that administrators must consider when planning multi-account or multi-connector integrations.

### Limit Specification

There is a limit of **five SAP BDC connections per metastore**. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

This means that a single [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) can have at most five active connections to SAP BDC accounts. The limit is enforced at the [Metastore](/concepts/metastore.md) level; additional connections beyond five cannot be created.

### Implications

- When the limit is reached, no new SAP BDC connections can be established until an existing one is deleted.
- The limit applies regardless of the connection owner or the number of workspaces attached to the [Metastore](/concepts/metastore.md). ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Scope

The limit is specific to connections created for the SAP BDC connector on Databricks for OpenSharing. It does not affect other types of connections or shares. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

### Related Concepts

- [Metastore](/concepts/metastore.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [SAP Business Data Cloud (BDC) Connector](/concepts/sap-business-data-cloud-bdc-connector.md)
- [OpenSharing](/concepts/opensharing.md)

### Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
