---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 603728286e52efb1b75bb48874a04b6c855b92a45d63576d651c4c22e9e987f7
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-three-level-namespace
    - UCTN
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Unity Catalog Three-Level Namespace
description: The catalog.schema.table hierarchical naming convention used by Unity Catalog to organize and access data objects.
tags:
  - unity-catalog
  - data-organization
  - naming
timestamp: "2026-06-19T14:31:02.956Z"
---

# Unity Catalog Three-Level Namespace

The **Unity Catalog Three-Level Namespace** is the logical data organization model used by [Unity Catalog](/concepts/unity-catalog.md) to structure and reference data assets. It follows the pattern `catalog.schema.table`, providing a consistent, hierarchical way to organize data across an organization.

## Concept

Each [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) exposes a three-level namespace (`catalog`.`schema`.`table`) by which data can be organized. A [Metastore](/concepts/metastore.md) is the top-level container that registers metadata about securable objects — such as tables, volumes, external locations, and shares — and the permissions that govern access to them. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

Under this namespace:

- A **catalog** is the first level and acts as a grouping container for schemas.
- A **schema** (also called a database) is the second level and contains tables, views, functions, and other objects.
- A **table** is the third level and represents the actual data structure.

All data references in Unity Catalog use this fully qualified three-part path.

## Regional Requirement

Every [Metastore](/concepts/metastore.md) is region-specific: you must have one [Metastore](/concepts/metastore.md) for each region in which your organization operates. Workspaces within that region can be linked to the [Metastore](/concepts/metastore.md), giving users a consistent view of data under the three-level namespace. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Relationship to Workspaces

To work with Unity Catalog, users must be on a workspace that is attached to a [Metastore](/concepts/metastore.md) in their region. When a workspace is linked to a [Metastore](/concepts/metastore.md), all users on that workspace can see and query data using the three-level namespace (subject to permissions). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container that exposes the three-level namespace
- [Managed Storage in Unity Catalog](/concepts/managed-storage-in-unity-catalog.md) — Storage locations that can be configured at the [Metastore](/concepts/metastore.md), catalog, and schema levels
- [Delta Sharing](/concepts/delta-sharing.md) — Mechanism for accessing data across different metastores
- [Catalog](/concepts/unity-catalog.md) — The first level of the namespace hierarchy
- Schema — The second level, also known as a database
- Table — The third and final level, representing actual data structures

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
