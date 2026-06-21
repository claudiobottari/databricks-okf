---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66979b4e863a16791169d462fa3e06bae7c04e4f10972f87a9e43c48851c7407
  pageDirectory: concepts
  sources:
    - managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-storage-location
    - MSL
    - Specify a Managed Storage Location
    - Managed storage
    - managed storage
  citations:
    - file: managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
title: Managed storage location
description: The storage location within a user's cloud account that Unity Catalog controls for organizing, optimizing, and deleting data files of managed assets
tags:
  - unity-catalog
  - storage
  - databricks
timestamp: "2026-06-19T19:29:23.138Z"
---

# Managed Storage Location

A **managed storage location** is the cloud storage path (and associated IAM role) that [Unity Catalog](/concepts/unity-catalog.md) uses to physically store the underlying data files for [Managed Tables](/concepts/managed-tables-in-databricks.md) and Managed Volumes. It is configurable at the [Metastore](/concepts/metastore.md), catalog, and schema levels, with each level overriding the one above. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Purpose

The managed storage location determines where in your cloud account Unity Catalog places the data files for managed assets. When you create a managed table or managed volume, Unity Catalog automatically stores its data in the managed storage location defined on the containing schema, catalog, or [Metastore](/concepts/metastore.md). When you drop a managed asset, Unity Catalog deletes the underlying data files from this location. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

This is distinct from External Assets, where you specify the storage location and control the file lifecycle yourself. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Configuration Scope

Managed storage can be configured at three hierarchical levels:

1. **Metastore level**: The root storage location for the entire [Metastore](/concepts/metastore.md).
2. **Catalog level**: Overrides the [Metastore](/concepts/metastore.md) storage for all schemas and tables within that catalog.
3. **Schema level**: Overrides both [Metastore](/concepts/metastore.md) and catalog storage for all tables and volumes in that schema.

If no managed storage is configured at any level, managed tables and managed volumes cannot be created. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Data Ownership

When you register a managed asset, you retain full ownership of your data. The data files always remain in your cloud account. Unity Catalog determines where within your account they are stored, but does not transfer them to Databricks or own them. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Managed Tables](/concepts/managed-tables-in-databricks.md) — Tables whose data files are stored in the managed storage location
- Managed Volumes — Volumes whose data files are stored in the managed storage location
- External Assets — Assets where you control the file storage lifecycle
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container that the managed storage location serves
- [Catalog](/concepts/unity-catalog.md) — Can override the [Metastore](/concepts/metastore.md)'s managed storage location
- Schema — Can override higher-level managed storage locations
- [Securable objects in Unity Catalog](/concepts/securable-objects-in-unity-catalog.md) — All objects governed by Unity Catalog

## Sources

- managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md

# Citations

1. [managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md](/references/managed-versus-external-assets-in-unity-catalog-databricks-on-aws-581e1fb1.md)
