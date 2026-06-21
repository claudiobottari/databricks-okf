---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3684c6c7185ca7243666d804d5de3c08cea06de260041173b4439dd17058e67
  pageDirectory: concepts
  sources:
    - unity-catalog-securable-objects-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-object-hierarchy
    - UCOH
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
title: Unity Catalog Object Hierarchy
description: The hierarchical structure of securable objects in Unity Catalog, with the metastore at the top and a three-level namespace (catalog.schema.table) for data assets.
tags:
  - architecture
  - unity-catalog
  - access-control
timestamp: "2026-06-19T23:15:24.833Z"
---

## [Unity Catalog](/concepts/unity-catalog.md) Object Hierarchy

**Unity Catalog Object Hierarchy** describes the nested structure of all securable objects in [Unity Catalog](/concepts/unity-catalog.md), the data governance solution on Databricks. Privileges can be granted on securable objects down the hierarchy, and the hierarchy determines how access control propagates from parent to child objects. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### Overview

The [Metastore](/concepts/metastore.md) is the top-level securable object in [Unity Catalog](/concepts/unity-catalog.md). It contains all other objects registered in a single cloud region. Within the [Metastore](/concepts/metastore.md), data assets are organized in a **three-level namespace** (`catalog.schema.table`), while non‑data securable objects — such as storage credentials, connections, and sharing entities — exist directly under the [Metastore](/concepts/metastore.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### The [Three-Level Namespace](/concepts/three-level-namespace.md)

The [Three-Level Namespace](/concepts/three-level-namespace.md) is the foundational structure for data assets in [Unity Catalog](/concepts/unity-catalog.md):

1. **Catalog** — The highest layer for data assets. Catalogs are container objects that hold schemas. They are typically used to organize data by organizational unit or lifecycle stage (e.g., dev, prod).
2. **Schema** (also called a database) — The second layer, contained within a catalog. Schemas organize assets into finer categories such as projects or teams. They are also container objects.
3. **Asset type** — The third level names the specific object, such as a Table, View, Volume, or Function.

This [Three-Level Namespace](/concepts/three-level-namespace.md) is universally used when referencing data: `catalog.schema.table`. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### Data Asset Hierarchy

Data assets live under a schema within a catalog. The hierarchy is:

- [Catalog](/concepts/unity-catalog.md) → Schema → Table (structured data, either managed, external, or foreign)
- Catalog → Schema → View (including [Materialized View](/concepts/materialized-views-in-databricks.md) and Metric View)
- Catalog → Schema → Volume (unstructured data in cloud storage, managed or external)
- Catalog → Schema → Function (including User-Defined Functions (UDFs), Stored Procedures, and Model | registered MLflow models)

Each of these object types has its own specific privileges (e.g., `SELECT` on tables, `READ VOLUME` on volumes, `CREATE MODEL` on schemas for models). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

#### Models as Functions

A Model is a versioned [MLflow](/concepts/mlflow.md) model stored as a function object. It supports additional privileges such as `APPLY TAG` and `CREATE MODEL VERSION`. Creating a model requires the `CREATE MODEL` privilege on the schema (not `CREATE FUNCTION`). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### Non-Data Securable Objects

These objects exist directly under the [Metastore](/concepts/metastore.md) and are not part of the [Three-Level Namespace](/concepts/three-level-namespace.md). They are grouped into two broad categories:

**Access management to cloud storage and external services:**

- [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) — Stores authentication information (e.g., IAM role on AWS) for accessing cloud storage paths.
- [External location](/concepts/external-location.md) — Pairs a storage credential with a specific cloud storage path.
- [External Metadata](/concepts/external-metadata-api.md) — Defines custom [Data Lineage](/concepts/data-lineage.md) relationships for external systems.
- Service Credential — Stores authentication for external cloud services (e.g., database endpoints).
- Connection — Stores endpoint and credentials for external systems (used for query federation, catalog federation, JDBC, etc.).

**Data and AI asset sharing across metastores or organizations:**

- Share — A logical grouping of data assets (tables, views, volumes) intended to be shared with recipients.
- Provider — Represents an external organization that has shared data with your organization.
- [Recipient](/concepts/data-recipient.md) — Represents an external organization that receives shared data.
- [Clean Room](/concepts/databricks-clean-rooms.md) — A secure environment for collaborating on shared data without exposing underlying data.

All these objects require specific creation privileges on the [Metastore](/concepts/metastore.md) (e.g., `CREATE STORAGE CREDENTIAL`, `CREATE SHARE`, `CREATE CLEAN ROOM`). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

### Sources

- unity-catalog-securable-objects-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
