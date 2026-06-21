---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e6f6ba241789a48666cef002b7a180a7eb2e019d4800642a45011984ca2202d
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-migration-path
    - UCMP
    - Unity Catalog Migration
    - Unity Catalog migration
  citations:
    - file: hive-metastore-table-access-control-legacy-databricks-on-aws.md
title: Unity Catalog Migration Path
description: The recommended upgrade strategy to replace the legacy Hive metastore table access control with Unity Catalog for simplified, centralized data governance across workspaces.
tags:
  - databricks
  - migration
  - unity-catalog
  - best-practice
timestamp: "2026-06-19T19:04:56.049Z"
---

```markdown
---
title: Unity Catalog Migration Path
summary: The recommended upgrade path from the legacy Hive [[metastore|Metastore]] table access control model to Unity Catalog for centralized data governance across multiple workspaces.
sources:
  - hive-metastore-table-access-control-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:47:26.528Z"
updatedAt: "2026-06-19T10:47:26.528Z"
tags:
  - databricks
  - unity-catalog
  - migration
  - governance
aliases:
  - unity-catalog-migration-path
  - UCMP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Unity Catalog Migration Path

**Unity Catalog Migration Path** refers to the strategy for upgrading from the legacy Hive [[metastore|Metastore]] data governance model to Databricks' Unity Catalog. This migration simplifies security and governance by providing a central place to administer and audit data access across multiple workspaces in an account. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Overview

Databricks recommends that organizations upgrade the tables managed by the Hive [[metastore|Metastore]] to the Unity Catalog [[metastore|Metastore]]. Unity Catalog supersedes the built-in Hive [[metastore|Metastore]] that each workspace deploys as a managed service, offering improved capabilities for managing data access at scale. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Context: The Legacy System

The [[Built-in Hive Metastore|Hive metastore]] is a built-in component that deploys with each Databricks workspace. An instance of the [[metastore|Metastore]] deploys to each cluster and securely accesses metadata from a central per-workspace repository. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

By default, a cluster allows all users to access all data managed by the workspace's built-in Hive [[metastore|Metastore]] unless [[Table Access Control (TACL)|table access control]] is enabled. When table access control is enabled on a cluster, users can programmatically grant and revoke access to Hive [[metastore|Metastore]] objects from Python and SQL. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

Hive [[metastore|Metastore]] [[Table Access Control (TACL)|table access control]] is a legacy data governance model. It is only available to workspaces on the Premium plan or above, and it requires either a Data Science & Engineering cluster with an appropriate configuration or a SQL warehouse. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Benefits of Migration

Unity Catalog simplifies security and governance of data by providing a central place to administer and audit data access across multiple workspaces in an account. Unlike the Hive [[metastore|Metastore]], which is workspace-scoped, Unity Catalog enables cross-workspace data management with unified access controls. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

## Migration Approach

Databricks recommends that organizations upgrade the tables managed by the Hive [[metastore|Metastore]] to the Unity Catalog [[metastore|Metastore]]. ^[hive-metastore-table-access-control-legacy-databricks-on-aws.md]

For detailed guidance on the migration process, including step-by-step instructions and tooling support, see the official documentation on upgrading to Unity Catalog.

## Related Concepts

- [[Unity Catalog]] — The modern data governance solution that provides centralized access control and auditing.
- [[Built-in Hive Metastore|Hive metastore]] — The legacy workspace-managed metadata service being replaced.
- [[Table Access Control (TACL)|Table access control]] — The legacy ACL-based permissions system for Hive [[metastore|Metastore]] objects.
- Data governance — The broader discipline of managing data availability, usability, integrity, and security.
- [[Upgrading Jobs to Unity Catalog|Upgrading to Unity Catalog]] — The official migration documentation with step-by-step procedures.

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md
```

# Citations

1. [hive-metastore-table-access-control-legacy-databricks-on-aws.md](/references/hive-metastore-table-access-control-legacy-databricks-on-aws-d8a45857.md)
