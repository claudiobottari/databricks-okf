---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b7e5ad4c418007a35e467a3d868c35b740f654565231662fb7516b4b18ba387
  pageDirectory: concepts
  sources:
    - unity-catalog-requirements-and-limitations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-resource-quotas
    - UCRQ
    - Unity Catalog Resource Quotas APIs
    - Resource Quotas
  citations:
    - file: unity-catalog-requirements-and-limitations-databricks-on-aws.md
title: Unity Catalog Resource Quotas
description: Unity Catalog enforces resource quotas on all securable objects; users can monitor usage via dedicated APIs and contact the Databricks account team if they expect to exceed limits.
tags:
  - unity-catalog
  - quotas
  - governance
timestamp: "2026-06-19T23:15:12.479Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) Resource Quotas

**Unity Catalog Resource Quotas** are predefined limits on the number of securable objects that can be created in a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). These quotas ensure that system resources are used fairly and prevent accidental over‑provisioning. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Quotas on Securable Objects

[Unity Catalog](/concepts/unity-catalog.md) enforces resource quotas on all securable objects, including catalogs, schemas, tables, views, functions, and other metadata constructs. The exact numerical limits are maintained in the Databricks documentation and are not configurable by users. If you expect to exceed these resource limits, contact your Databricks account team. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

The current quotas are listed on the Resource limits page. Databricks regularly updates this list as platform capabilities evolve. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Monitoring Quota Usage

You can monitor your current quota usage using the [Unity Catalog](/concepts/unity-catalog.md) resource quotas APIs. These APIs allow you to inspect how many objects of each type have been created and how close you are to the quota limits. For API details, see [Monitor your usage of [Unity Catalog](/concepts/unity-catalog.md) resource quotas](https://docs.databricks.com/aws/en/resources/manage-resource-quotas). ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The catalog system that enforces these quotas.
- Securable objects – The entities (catalogs, schemas, tables, etc.) to which quotas apply.
- Resource limits – The page listing all current quota values.
- Unity Catalog requirements and limitations – The broader page that includes quota information.

## Sources

- unity-catalog-requirements-and-limitations-databricks-on-aws.md

# Citations

1. [unity-catalog-requirements-and-limitations-databricks-on-aws.md](/references/unity-catalog-requirements-and-limitations-databricks-on-aws-0188dbe0.md)
