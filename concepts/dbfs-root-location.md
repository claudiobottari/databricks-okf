---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3402b20a1c3360b25f548915efcc31e8d5b2aae3b8adb3703df2904dfaa557e5
  pageDirectory: concepts
  sources:
    - resolve-storage-path-conflicts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbfs-root-location
    - DRL
    - DBFS root
    - DBFS root volume
  citations:
    - file: resolve-storage-path-conflicts-databricks-on-aws.md
title: DBFS root location
description: A sibling path under a workspace's default storage path that does not create a conflict when used as an external location, as it is not the same as the internal storage path.
tags:
  - unity-catalog
  - dbfs
  - storage
timestamp: "2026-06-19T20:14:00.478Z"
---

# DBFS Root Location

**DBFS root location** is the default storage location for the Databricks File System (DBFS) in a Databricks workspace. It is configured during workspace deployment and serves as the top-level storage path for workspace data, including notebooks, libraries, and temporary files.

## Overview

The DBFS root location is a sibling of the workspace's internal Unity Catalog storage path within the same cloud storage bucket. For example, if a workspace's default Unity Catalog storage path is `s3://<your-bucket>/<region>/`, the DBFS root location would be at a parallel path under the same bucket. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Relationship to External Locations

When configuring [External Locations](/concepts/external-location.md) in Unity Catalog, you can create external locations on paths that are more specific than the DBFS root location. This is permitted because the DBFS root location is a sibling of the workspace's internal storage path and does not create a conflict with Unity Catalog's internal processing. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Storage Path Conflicts

A [Storage path conflict](/concepts/storage-path-conflict.md) occurs when an external location overlaps with the default Unity Catalog storage path of any workspace in your Databricks account. However, creating an external location on paths under the DBFS root location does not cause such conflicts, as the DBFS root location is separate from the workspace's internal storage path. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Related Concepts

- Databricks File System (DBFS)
- [External Locations](/concepts/external-location.md)
- [Storage path conflict](/concepts/storage-path-conflict.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Workspace Storage Configuration

## Sources

- resolve-storage-path-conflicts-databricks-on-aws.md

# Citations

1. [resolve-storage-path-conflicts-databricks-on-aws.md](/references/resolve-storage-path-conflicts-databricks-on-aws-74a353cf.md)
