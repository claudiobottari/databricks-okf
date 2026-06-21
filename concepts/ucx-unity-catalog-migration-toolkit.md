---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d74534325936303451edbdfd2c8f87685a89a9b72fa3c994f37b2c9a1e5926b9
  pageDirectory: concepts
  sources:
    - use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ucx-unity-catalog-migration-toolkit
    - U(CMT
    - UCX|UCX (Unity Catalog Migration Toolkit)
    - Unity Catalog Migration Toolkit (UCX)
    - UCX Migration Tool
  citations:
    - file: use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
title: UCX (Unity Catalog Migration Toolkit)
description: A Databricks Labs open-source project providing tools and workflows to upgrade non-Unity-Catalog workspaces to Unity Catalog on Databricks.
tags:
  - databricks
  - unity-catalog
  - migration
  - open-source
timestamp: "2026-06-19T23:22:34.108Z"
---

---
title: UCX ([Unity Catalog](/concepts/unity-catalog.md) Migration Toolkit)
summary: A Databricks Labs tool that provides workflows to upgrade a workspace from a Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md), including assessment, group migration, and table migration.
sources:
  - use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
kind: tool
createdAt: "2026-06-20T10:00:00Z"
updatedAt: "2026-06-20T10:00:00Z"
tags:
  - databricks
  - unity-catalog
  - migration
  - hive-metastore
aliases:
  - ucx
  - unity-catalog-migration-toolkit
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# UCX ([Unity Catalog](/concepts/unity-catalog.md) Migration Toolkit)

**UCX** ([Unity Catalog](/concepts/unity-catalog.md) Migration Toolkit) is a Databricks Labs project that provides utilities and automated workflows to help upgrade a workspace from a Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md). It includes an assessment workflow, a group migration workflow, and a table migration workflow. UCX is provided as‑is with no formal Databricks support; issues should be filed on its [GitHub repository](https://github.com/databrickslabs/ucx). ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Before you begin

Before installing UCX, the environment must meet the following prerequisites:

- **Databricks CLI** v0.213 or above with configuration profiles for both the workspace and the Databricks account.
- **Python** 3.10 or above on the machine running UCX.
- **Cloud CLI** (AWS CLI or Azure CLI) if using the optional storage location identification workflow.
- **Network access** from the installation machine to the workspace, to the internet (pypi.org, github.com), and from the workspace to pypi.org for `databricks-sdk` and `pyyaml`.
- **Roles:** Databricks account admin and workspace admin roles (service principals cannot install).
- **Unity Catalog metastore** in every region hosting a workspace to be upgraded, with each workspace attached to a [Metastore](/concepts/metastore.md). Attaching a [Metastore](/concepts/metastore.md) also enables identity federation (centralized user management at account level).
- If using an external Hive [Metastore](/concepts/metastore.md) (e.g., AWS Glue), additional setup is required.
- A **Pro or Serverless SQL warehouse** on the workspace to render the assessment report.

^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Installation

Install UCX using the Databricks CLI:

```bash
databricks labs install ucx
```

During installation you are prompted to:
1. Select the Databricks configuration profile for the workspace.
2. Choose an inventory database name (default: `ucx`).
3. Select a SQL warehouse for installation.
4. Choose workspace-local groups to migrate to account-level groups. Default `<ALL>` treats matching account-level groups as replacements.
5. Optionally connect to an external Hive [Metastore](/concepts/metastore.md).
6. Choose whether to open the generated README notebook.

The installation deploys a README notebook, dashboards, databases, libraries, jobs, and other assets. UCX can also be installed on all workspaces in an account. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Step 1: Assessment workflow

The assessment workflow evaluates the [Unity Catalog](/concepts/unity-catalog.md) compatibility of group identities, storage locations, storage credentials, access controls, and tables. It populates an assessment dashboard with findings and recommendations. Output is stored in Delta tables in the inventory database. The workflow can be triggered from the README notebook, the Databricks UI (Jobs > [UCX] Assessment), or via CLI:

```bash
databricks labs ucx ensure-assessment-run
```

Run the workflow multiple times until all incompatibilities are resolved. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Step 2: Group migration workflow

The group migration workflow upgrades workspace-local groups to account-level groups, replicates permissions, and removes unnecessary groups. It depends on the assessment output. Run from the README notebook or CLI. Output is stored in Delta tables; run multiple times to ensure success. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Step 3: Table migration workflow

The table migration workflow upgrades tables from the Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md). External Hive tables become [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) using `SYNC`; managed tables stored in DBFS root become managed tables using `DEEP CLONE`. Hive managed tables must be Delta or Parquet; external tables must be in supported formats.

### Preparatory commands (run before the workflow)

- `create-table-mapping` – creates a CSV mapping each Hive table to a target [Unity Catalog](/concepts/unity-catalog.md) catalog, schema, and table. Review and edit before proceeding.
- `create-uber-principal` – creates a read-only service principal for the workflow compute; deprovision when done.
- `principal-prefix-access`, `migrate-credentials`, `migration-locations`, `create-catalogs-schemas` – optional commands for credentials and locations.

### Running table migration

Trigger the workflow from the README notebook or the jobs UI. Output is stored in Delta tables. Run multiple times if needed. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Additional utilities

UCX also provides commands for enabling [Hive Metastore Federation](/concepts/hive-metastore-federation.md) (`enable-hms-federation`, `create-federated-catalog`) to ease the transition by allowing workloads on both the legacy Hive [Metastore](/concepts/metastore.md) and the mirrored [Unity Catalog](/concepts/unity-catalog.md). Debugging tools and other utilities are available. ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Upgrading UCX

To upgrade an existing installation to the latest version:

```bash
databricks labs upgrade ucx
```

## Getting help

- `databricks labs ucx --help` for CLI help.
- `databricks labs ucx <command> --help` for specific command help.
- Append `--debug` to any command for debug logs.
- See the [UCX troubleshooting guide](https://databrickslabs.github.io/ucx/docs/reference/troubleshooting/).
- File issues on the [GitHub repository](https://github.com/databrickslabs/ucx/issues/new/choose).

^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Release notes

See the [changelog](https://github.com/databrickslabs/ucx/blob/main/CHANGELOG.md). ^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- Databricks Labs
- Databricks CLI
- Assessment dashboard
- [Group migration](/concepts/ucx-group-migration-workflow.md)
- [Table migration](/concepts/ucx-table-migration-workflow.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md)
- External Hive metastore

## Sources

- use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md](/references/use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws-0023b143.md)
