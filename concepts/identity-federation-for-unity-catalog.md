---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c303cd4473b5f37fb4b36ee28eaf1f1245fbb1b6f8d08cf5ba80c4e482bcacb6
  pageDirectory: concepts
  sources:
    - use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - identity-federation-for-unity-catalog
    - IFFUC
    - Identity Federation
  citations:
    - file: use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
title: Identity Federation for Unity Catalog
description: The centralization of user management at the Databricks account level, required as a prerequisite for using UCX and enabling Unity Catalog adoption.
tags:
  - databricks
  - unity-catalog
  - identity
  - authentication
timestamp: "2026-06-19T23:23:08.101Z"
---

# Identity Federation for [Unity Catalog](/concepts/unity-catalog.md)

**Identity Federation for Unity Catalog** refers to the process of centralizing user management at the Databricks account level, enabling a unified identity system across workspaces that are attached to [Unity Catalog](/concepts/unity-catalog.md). This is a prerequisite for using the UCX ([Unity Catalog](/concepts/unity-catalog.md) migration) tools to upgrade workspaces from legacy Hive metastores to [Unity Catalog](/concepts/unity-catalog.md).

## Overview

Identity federation is established when a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) is attached to a Databricks workspace. This attachment centralizes user management at the Databricks account level, allowing workspace-level groups and users to be managed consistently across multiple workspaces. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Prerequisites for UCX

To use UCX for upgrading a workspace to [Unity Catalog](/concepts/unity-catalog.md), identity federation must be enabled. This is one of the prerequisites listed in the UCX setup documentation. Specifically, a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) must be created for every region that hosts a workspace to be upgraded, and each of those Databricks workspaces must be attached to a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

Enabling identity federation is part of the broader Unity Catalog setup process. For guidance on how to determine whether identity federation is already in place, how to create a [Metastore](/concepts/metastore.md), and how to attach a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) to a workspace, see Step 1: Confirm that your workspace is enabled for Unity Catalog in the [Unity Catalog](/concepts/unity-catalog.md) setup article. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Relationship to Group Migration

The group migration workflow within UCX upgrades workspace-local groups to account-level groups, which is a direct benefit of identity federation. After migration, account-level groups can be used to manage permissions across all workspaces within a Databricks account, rather than maintaining separate group definitions for each workspace. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution that enables centralized metadata management.
- UCX – The migration toolkit that requires identity federation as a prerequisite.
- Group migration workflow – The UCX workflow that upgrades workspace-local groups to account-level groups.
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) – An alternative integration approach that can be used alongside identity federation during migration.
- [Identity Federation](/concepts/identity-federation-for-unity-catalog.md) – The broader concept of centralizing user and group management across a Databricks account.

## Sources

- use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md](/references/use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws-0023b143.md)
