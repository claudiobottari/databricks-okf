---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3922e8f0532c2dd1705a3ba1b808b3ad3eb304a6ee971082cc4991e5c898bda
  pageDirectory: concepts
  sources:
    - create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-opensharing
    - Data shares (OpenSharing)
    - Dynamic Views in OpenSharing
  citations:
    - file: create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md
title: Databricks OpenSharing
description: A Databricks feature that enables organizations to share data across platforms using Delta Sharing protocols
tags:
  - data-sharing
  - databricks
  - open-sharing
timestamp: "2026-06-18T14:52:27.948Z"
---

# Databricks OpenSharing

**Databricks OpenSharing** is a feature that enables sharing data assets from a Databricks Unity Catalog [Metastore](/concepts/metastore.md) with external systems, such as SAP Business Data Cloud (BDC). It is built on the [Delta Sharing](/concepts/delta-sharing.md) protocol and allows Databricks to act as both a provider and recipient of shares.

## Overview

OpenSharing must be enabled on the [Metastore](/concepts/metastore.md) before any sharing can occur. Once enabled, administrators can grant users and service principals the ability to create and manage shares and recipients. In the context of the [SAP BDC Connector](/concepts/sap-bdc-connector.md), establishing an OpenSharing connection automatically creates a **provider object** and a **recipient object** on Databricks, enabling bidirectional data exchange. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Enabling OpenSharing

To use OpenSharing, a workspace admin must first enable it on the [Metastore](/concepts/metastore.md) and then grant the `CREATE PROVIDER` and `CREATE RECIPIENT` privileges to appropriate users. This setup is a prerequisite for creating connections to external partners such as SAP BDC. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Sharing Data with External Systems

After OpenSharing is enabled and a connection is established (e.g., to SAP BDC), Databricks can **openshare** assets—such as tables, views, and notebooks—to the external recipient. The shared assets can then be mounted as catalogs in Unity Catalog for consumption. ^[create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [SAP Business Data Cloud connector](/concepts/sap-business-data-cloud-bdc-connector.md)
- [Provider and Recipient objects](/concepts/sap-bdc-provider-and-recipient-objects.md)
- [OpenSharing setup for providers](/concepts/opensharing-provider-object.md)

## Sources

- create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md

# Citations

1. [create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws.md](/references/create-and-manage-the-sap-business-data-cloud-bdc-connector-databricks-on-aws-007033cf.md)
