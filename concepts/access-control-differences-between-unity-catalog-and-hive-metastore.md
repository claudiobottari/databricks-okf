---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ba82dbafdd26fdc182825a7b1cc5f768b3931bb217bb1bb241e08b5fa910f54
  pageDirectory: concepts
  sources:
    - work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-control-differences-between-unity-catalog-and-hive-metastore
    - Hive Metastore and Access Control Differences Between Unity Catalog
    - ACDBUCAHM
  citations:
    - file: work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
title: Access Control Differences Between Unity Catalog and Hive Metastore
description: Unity Catalog and the legacy Hive metastore have differing access control models, including metastore scope (account-level vs workspace-level), permission requirements (USE CATALOG/USE SCHEMA), view ownership rules, and support for DENY, ANY FILE, ANONYMOUS FUNCTION, and READ_METADATA.
tags:
  - databricks
  - unity-catalog
  - access-control
  - security
timestamp: "2026-06-19T23:26:33.894Z"
---

# Access Control Differences Between [Unity Catalog](/concepts/unity-catalog.md) and Hive [Metastore](/concepts/metastore.md)

**Access Control Differences Between [Unity Catalog](/concepts/unity-catalog.md) and Hive Metastore** refers to the distinct security models and permission frameworks that govern data access when using [Unity Catalog](/concepts/unity-catalog.md) alongside a legacy [Hive Metastore](/concepts/built-in-hive-metastore.md) on Databricks. While both systems provide data governance, [Unity Catalog](/concepts/unity-catalog.md) introduces a fundamentally different approach to access control that differs from the legacy workspace-level Hive [Metastore](/concepts/metastore.md) in several key areas.

## Overview

When a Databricks workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md), the legacy per-workspace Hive [Metastore](/concepts/metastore.md) continues to exist as a top-level catalog called `hive_metastore` in the [Three-Level Namespace](/concepts/three-level-namespace.md). Databricks continues to enforce any previously configured [legacy table access control](/concepts/table-access-control-tacl.md) for data in the `hive_metastore` catalog when clusters run in [Standard Access Mode](/concepts/standard-access-mode.md). However, the [Unity Catalog](/concepts/unity-catalog.md) access model differs from these legacy controls, requiring users to understand the differences when managing permissions across both systems. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Key Differences in Access Control

### [Metastore](/concepts/metastore.md) Scope and Governance

- **Metastore scope**: The [Unity Catalog](/concepts/unity-catalog.md) is an account-level object, while the Hive [Metastore](/concepts/metastore.md) is a workspace-level object. Permissions defined within the `hive_metastore` catalog always refer to the local users and groups in the workspace. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]
- **Group sources**: Access control policies in [Unity Catalog](/concepts/unity-catalog.md) are applied to account groups, whereas access control policies for the Hive [Metastore](/concepts/metastore.md) are applied to workspace-local groups. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

### Required Permissions on Catalogs and Schemas

In [Unity Catalog](/concepts/unity-catalog.md), `USE CATALOG` and `USE SCHEMA` permissions are required on the [Catalog and Schema](/concepts/catalog-and-schema.md) for all operations on objects inside the catalog or schema. Regardless of a principal's privileges on a table, the principal must also have the `USE CATALOG` privilege on its parent catalog to access the schema and the `USE SCHEMA` privilege to access objects within the schema. With workspace-level table access controls, granting `USAGE` on the root catalog automatically grants `USAGE` on all databases, but `USAGE` on the root catalog is not required. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

### View Ownership Requirements

In [Unity Catalog](/concepts/unity-catalog.md), the owner of a view does not need to be an owner of the view's referenced tables and views. Having the `SELECT` privilege is sufficient, along with `USE SCHEMA` on the views' parent schema and `USE CATALOG` on the parent catalog. With workspace-level table access controls, a view's owner needs to be an owner of all referenced tables and views. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

### Unsupported Securables

- **No support for `ANY FILE` or `ANONYMOUS FUNCTION`**: In [Unity Catalog](/concepts/unity-catalog.md), there is no concept of an `ANY FILE` or `ANONYMOUS FUNCTION` securable that might allow an unprivileged user to run privileged code. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]
- **No support for `DENY`**: The [Unity Catalog](/concepts/unity-catalog.md) privilege model is built on the principle of least privilege. Privileges that are not granted are implicitly denied. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]
- **No `READ_METADATA` privilege**: [Unity Catalog](/concepts/unity-catalog.md) manages access to view metadata in a different way from the legacy Hive [Metastore](/concepts/metastore.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

### Cross-Workspace Join Limitations

A join with data in the legacy Hive [Metastore](/concepts/metastore.md) will only work on the workspace where that data resides. Trying to run such a join in another workspace results in an error. Databricks recommends upgrading legacy tables and views to [Unity Catalog](/concepts/unity-catalog.md). ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog privileges reference](/concepts/unity-catalog-privileges-and-ownership.md)
- [Legacy table access control](/concepts/table-access-control-tacl.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md)
- [Upgrade a workspace to Unity Catalog](/concepts/workspace-catalog-unity-catalog.md)
- [Three-Level Namespace](/concepts/three-level-namespace.md)

## Sources

- work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md

# Citations

1. [work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md](/references/work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws-c5d018d3.md)
