---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0db554a251cd1980b85f3055f4010dd3da6d52ada4666e5bffe6fa3f4a1a4a16
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-access-control
    - FTAC
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Feature Table Access Control
description: A mechanism within the Databricks Workspace Feature Store for restricting which users or groups can view, modify, or use feature tables.
tags:
  - feature-store
  - security
  - governance
timestamp: "2026-06-19T10:26:44.214Z"
---

# Feature Table Access Control

**Feature Table Access Control** refers to the ability to manage permissions on feature tables within the Databricks Workspace Feature Store (legacy). This control allows administrators to restrict which users, groups, or service principals can read, write, or manage feature tables. Access to feature tables is configured through the same Unity Catalog or workspace-level permissions used for other securable objects. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Overview

The Workspace Feature Store provides dedicated access control mechanisms for feature tables. While the Feature Store UI allows users to search for feature tables, track lineage, add tags, and monitor freshness, controlling access is handled through separate permission settings. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## How to Configure

For complete instructions on setting up access control for feature tables, see the dedicated documentation:

- **Access control (legacy)** – The primary reference for configuring permissions on feature tables. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store (legacy)](/concepts/databricks-workspace-feature-store-legacy.md) – The platform that stores and manages feature tables.
- [Unity Catalog Permissions](/concepts/unity-catalog-permissions-model.md) – Governing access to tables and other securable objects.
- [Workspace-level access control](/concepts/workspace-level-restrictions.md) – Broader permission model for Databricks workspaces.
- Feature Lineage and Freshness – Monitoring feature provenance and timeliness.
- [Feature Table Tags](/concepts/feature-table-tagging.md) – Key-value metadata for organizing and discovering feature tables.

## Limitations

The source material does not provide specific details about the permission model, ACL types, or the exact steps for granting or revoking access. Users should consult the linked *Access control (legacy)* documentation for authoritative instructions. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
