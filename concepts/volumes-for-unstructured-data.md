---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18b49c528590ed85898257fba7c68e09c72f458a44981098f68d04598570c147
  pageDirectory: concepts
  sources:
    - unity-catalog-securable-objects-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - volumes-for-unstructured-data
    - VFUD
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
title: Volumes for Unstructured Data
description: Volumes are securable objects in Unity Catalog for unstructured data in cloud storage, supporting file-level read/write access without SQL query operations, available as managed or external volumes.
tags:
  - unity-catalog
  - unstructured-data
  - storage
timestamp: "2026-06-19T23:15:35.657Z"
---

# Volumes for Unstructured Data

**Volumes** are a securable object in [Unity Catalog](/concepts/unity-catalog.md) that represent collections of unstructured data stored in cloud object storage. Unlike tables and [views](/concepts/shared-views-in-databricks-to-databricks-sharing.md), which store structured data and support SQL query operations, volumes provide file-level read and write access to unstructured data such as images, audio files, documents, and other binary or text files. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Overview

Volumes exist within a schema in the [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md). They are part of the [Three-Level Namespace](/concepts/three-level-namespace.md) (`catalog.schema.volume`) and are governed by [Unity Catalog](/concepts/unity-catalog.md)'s access control system. Volumes do not support SQL query operations — they are designed specifically for file-level access to unstructured data in cloud storage. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Types of Volumes

There are two types of volumes in Databricks:

- **Managed volumes**: The storage location path is determined by [Unity Catalog](/concepts/unity-catalog.md). The data itself lives in your cloud account, but [Unity Catalog](/concepts/unity-catalog.md) manages the storage location. Databricks recommends using managed volumes to have [Unity Catalog](/concepts/unity-catalog.md) automatically govern all data access. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

- **External volumes**: You specify the storage location path. External volumes are useful when you require external system access outside of Databricks, but be aware that external systems can bypass [Unity Catalog governance](/concepts/unity-catalog-governance.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Access Control

Access to volumes is controlled through [Unity Catalog](/concepts/unity-catalog.md) privileges. The relevant privileges include:

- `READ VOLUME`: Allows reading files from the volume.
- `WRITE VOLUME`: Allows writing files to the volume.

Databricks recommends managing cloud storage access through volumes and the `READ VOLUME` and `WRITE VOLUME` privileges rather than granting `READ FILES` and `WRITE FILES` directly on [external locations](/concepts/external-location.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Relationship to Other Securable Objects

Volumes are one of several asset types that can exist within a schema, alongside tables, [views](/concepts/shared-views-in-databricks-to-databricks-sharing.md), and [functions](/concepts/ai-functions.md). They are also related to [external locations](/concepts/external-location.md), which pair a [storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) with a cloud storage path. While external locations provide direct file access, volumes offer a more governed approach to unstructured data management within [Unity Catalog](/concepts/unity-catalog.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Use Cases

Volumes are appropriate for any scenario involving unstructured data that needs to be governed by [Unity Catalog](/concepts/unity-catalog.md), including:

- Storing training data for machine learning models
- Managing document repositories
- Hosting media files for applications
- Providing shared file storage for collaborative data science work

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that manages volumes.
- [External locations](/concepts/external-location.md) — Lower-level objects for cloud storage access.
- Storage credentials — Authentication information for cloud storage access.
- [Managed tables](/concepts/managed-tables-in-databricks.md) — Structured data with Unity Catalog-managed storage.
- Schema — The container object that holds volumes.

## Sources

- unity-catalog-securable-objects-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
