---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ed21c931bbb2c9d4ed392160f93793fbff6b20465105b80670be100183a285b
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - securable-objects-in-unity-catalog
    - SOIUC
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
title: Securable objects in Unity Catalog
description: Objects in the Unity Catalog hierarchy (catalog, schema, table, etc.) that can have attributes and have policies attached to them for access control.
tags:
  - unity-catalog
  - data-governance
  - architecture
timestamp: "2026-06-19T14:04:38.295Z"
---

# Securable objects in Unity Catalog

**Securable objects** are the fundamental entities in [Unity Catalog](/concepts/unity-catalog.md) that can have permissions granted on them. They form the hierarchical structure through which data access is managed and controlled within the Databricks platform.

## Overview

In Unity Catalog, securable objects are organized in a hierarchy that mirrors the logical organization of data assets. Each securable object can have [privileges](/concepts/privileges-and-ownership.md) granted to principals (users, service principals, or groups), enabling fine-grained access control across the data estate. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Hierarchy of Securable Objects

The Unity Catalog hierarchy consists of the following securable objects, from broadest to most granular:

- **Catalog** — The top-level container that organizes schemas and other objects.
- **Schema** — A logical grouping of tables, views, and other data objects within a catalog.
- **Table** — A structured collection of data rows and columns.
- **Materialized View** — A pre-computed view that stores query results for faster access.
- **Streaming Table** — A table that continuously ingests and processes streaming data.
- **Model** — A machine learning model registered in Unity Catalog.

^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Attribute-Based Access Control (ABAC) and Securable Objects

Securable objects can have [Governed Tags](/concepts/governed-tags.md) applied to them, which serve as attributes for [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md). These attributes are used in policy conditions to determine which data a policy should protect. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### Policy Attachment

Policies are attached at specific levels in the Unity Catalog hierarchy — such as a catalog, schema, or table. When a securable object has the attributes targeted by a policy, that policy takes effect automatically. This means a single policy can enforce consistent access rules across an entire catalog or schema without needing to be applied to each individual object. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### Supported Policy Types on Securable Objects

ABAC supports the following policy types that operate on securable objects:

- **Row filter policies** — Applied to tables, materialized views, and streaming tables to restrict which rows are visible to users.
- **Column mask policies** — Applied to tables, materialized views, and streaming tables to obfuscate or transform column values.
- **GRANT policies (Beta)** — Currently scoped to `EXECUTE` on models, enabling dynamic privilege grants based on attributes.

^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Dynamic Evaluation

Access control on securable objects is evaluated dynamically. When a user queries a securable object, Unity Catalog checks all applicable policies and privileges at runtime, ensuring that access decisions reflect the current state of attributes, policies, and grants. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that manages securable objects.
- Privileges in Unity Catalog — The permissions that can be granted on securable objects.
- [Governed Tags](/concepts/governed-tags.md) — Attributes that can be applied to securable objects for ABAC.
- [Row Filters](/concepts/row-filter-policies.md) — Row-level security policies on tables and views.
- Column Masks — Column-level security policies for data obfuscation.
- [Grant Policies](/concepts/grant-policies-beta.md) — Dynamic privilege grants based on attributes (Beta).

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
