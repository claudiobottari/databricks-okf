---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 11615c952a82e2243d4b374dec1d177a09acb2f45a73b13418bd459144e06a4d
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - regional-metastore-requirement
    - RMR
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Regional Metastore Requirement
description: Each AWS region in which an organization operates requires its own Unity Catalog metastore; workspaces can only link to a metastore in the same region.
tags:
  - unity-catalog
  - aws
  - deployment
timestamp: "2026-06-19T14:31:16.673Z"
---

# Regional [Metastore](/concepts/metastore.md) Requirement

**Regional [Metastore](/concepts/metastore.md) Requirement** refers to the architectural constraint in [Unity Catalog](/concepts/unity-catalog.md) that each Databricks region must have its own dedicated [Metastore](/concepts/metastore.md). A [Metastore](/concepts/metastore.md) is the top-level container for metadata in Unity Catalog, registering information about securable objects (such as tables, volumes, external locations, and shares) and the permissions that govern access to them. Each [Metastore](/concepts/metastore.md) exposes a three-level namespace (`catalog.schema.table`) by which data can be organized. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Why the Requirement Exists

Unity Catalog metastores are regional resources. To work with Unity Catalog, users must be on a workspace that is attached to a [Metastore](/concepts/metastore.md) in the same region. Consequently, you must create one [Metastore](/concepts/metastore.md) for each region in which your organization operates. This ensures that data governance policies and metadata are co-located with compute resources for performance and compliance. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## How It Works

When you create a [Metastore](/concepts/metastore.md), you specify the region where it should be deployed. That region must match the region of the workspaces that will access the data. The [Metastore](/concepts/metastore.md) may optionally use an S3 bucket in the same region for metastore-level storage of [managed tables](/concepts/managed-tables-in-databricks.md) and managed volumes. If you have more than one [Metastore](/concepts/metastore.md), Databricks recommends using a dedicated S3 bucket for each one, also located in the same region. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

Once a regional [Metastore](/concepts/metastore.md) is created, you can link it to any number of workspaces within that region. Each linked workspace shares the same view of the data in the [Metastore](/concepts/metastore.md), and data access control can be managed across those workspaces. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Cross-Region Data Access

Data in one region’s [Metastore](/concepts/metastore.md) can be accessed from workspaces in another region by using [OpenSharing](/concepts/opensharing.md) (the Databricks implementation of Delta Sharing). This provides a mechanism for cross-region data sharing while maintaining the per-metastore governance model. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution that uses metastores.
- [Metastore](/concepts/metastore.md) – The top-level metadata container.
- [Managed storage location](/concepts/managed-storage-location.md) – Cloud storage configured for managed tables and volumes at the [Metastore](/concepts/metastore.md), catalog, or schema level.
- Enable a workspace for Unity Catalog – The process of attaching a workspace to a [Metastore](/concepts/metastore.md).
- [OpenSharing](/concepts/opensharing.md) – Delta Sharing implementation for cross-metastore access.
- [Create a Unity Catalog metastore](/concepts/unity-catalog-metastore.md) – Step-by-step guide for setting up a regional [Metastore](/concepts/metastore.md).

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
