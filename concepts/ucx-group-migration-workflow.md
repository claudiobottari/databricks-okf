---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc43d8507e92566ddc36c81c71a86893099675a7e913e3c79869bdfb7547315c
  pageDirectory: concepts
  sources:
    - use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ucx-group-migration-workflow
    - UGMW
    - Group Migration Workflow
    - Group migration workflow
    - Group migration
  citations:
    - file: use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
title: UCX Group Migration Workflow
description: A UCX workflow that upgrades workspace-local groups to account-level groups to support Unity Catalog, replicating permissions and removing unnecessary groups.
tags:
  - databricks
  - unity-catalog
  - migration
  - identity
timestamp: "2026-06-19T23:22:40.957Z"
---

# UCX Group Migration Workflow

The **UCX Group Migration Workflow** is a component of the [UCX (Unity Catalog Migration Toolkit)](/concepts/ucx-unity-catalog-migration-toolkit.md) that upgrades workspace-local groups to account-level groups to support [Unity Catalog](/concepts/unity-catalog.md). It ensures that appropriate account-level groups are available in the workspace, replicates all permissions from workspace-local groups to their account-level counterparts, and removes any unnecessary groups and permissions from the workspace. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Overview

The group migration workflow is the second step in the UCX migration process, following the [UCX Assessment Workflow](/concepts/ucx-assessment-workflow.md). The tasks in the group migration workflow depend on the output of the assessment workflow, which first assesses the [Unity Catalog](/concepts/unity-catalog.md) compatibility of group identities, storage locations, storage credentials, access controls, and tables in the current workspace. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before running the group migration workflow, the following conditions must be met:

- The assessment workflow must have been run successfully, as the group migration workflow depends on its output. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]
- Identity federation must be enabled, which centralizes user management at the Databricks account level. This is enabled when a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) is attached to the workspace. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]
- During UCX installation, you must specify which workspace-local groups to migrate to account-level groups. If you select the default (`<ALL>`), any existing account-level group whose name matches a workspace-local group will be treated as the replacement for that workspace-local group and will inherit all of its workspace permissions when you run the group migration workflow. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Group Name Conflict Resolution

You have the opportunity to modify the workspace-group-to-account-group mapping after running the UCX installer and before running the group migration workflow. This is handled through the Group Name Conflict Resolution mechanism documented in the UCX repository. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Output

The output of each workflow task is stored in Delta tables in the `$inventory_database` schema that you specify during UCX installation. You can use these tables to perform further analysis and decision-making. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Running the Workflow Multiple Times

You can run the group migration workflow multiple times to ensure that all groups are upgraded successfully and that all necessary permissions are assigned. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## How to Run

For information about running the group migration workflow, see your UCX-generated README notebook and the [Group migration workflow](https://databrickslabs.github.io/ucx/docs/reference/workflows/#group-migration-workflow) documentation in the UCX readme. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [UCX (Unity Catalog Migration Toolkit)](/concepts/ucx-unity-catalog-migration-toolkit.md) — The overall migration toolkit that includes this workflow
- [UCX Assessment Workflow](/concepts/ucx-assessment-workflow.md) — The prerequisite workflow that assesses compatibility
- [UCX Table Migration Workflow](/concepts/ucx-table-migration-workflow.md) — The subsequent workflow for migrating tables
- [Unity Catalog](/concepts/unity-catalog.md) — The target data governance solution
- Group Name Conflict Resolution — Mechanism for handling group name conflicts during migration
- [Identity Federation](/concepts/identity-federation-for-unity-catalog.md) — Centralized user management at the account level

## Sources

- use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md](/references/use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws-0023b143.md)
