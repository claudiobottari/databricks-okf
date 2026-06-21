---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f0766acfce36cff1eb21460328e51176f45cc2af4de977aac95e80ce9f14897a
  pageDirectory: concepts
  sources:
    - use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ucx-assessment-workflow
    - UAW
  citations:
    - file: use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md
title: UCX Assessment Workflow
description: The first UCX migration workflow that assesses Unity Catalog compatibility of groups, storage, access controls, and tables, producing an assessment dashboard and Delta tables for migration planning.
tags:
  - databricks
  - unity-catalog
  - migration
  - assessment
timestamp: "2026-06-19T23:22:31.343Z"
---

# UCX Assessment Workflow

The **UCX Assessment Workflow** is the first major workflow in the [Unity Catalog](/concepts/unity-catalog.md) Migration Toolkit (UCX), designed to assess the [Unity Catalog](/concepts/unity-catalog.md) compatibility of a workspace's existing assets and provide the information needed for planning a migration to [Unity Catalog](/concepts/unity-catalog.md).^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Purpose

The assessment workflow evaluates the [Unity Catalog](/concepts/unity-catalog.md) compatibility of group identities, storage locations, storage credentials, access controls, and tables in the current workspace. It surfaces findings and common recommendations to help users understand what must be addressed before Group Migration Workflow|group migration or [Table Migration Workflow|table migration](/concepts/ucx-table-migration-workflow.md) can proceed.^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Execution

The tasks within the assessment workflow can be executed in parallel or sequentially, depending on specified dependencies. After the workflow finishes, an assessment dashboard is populated with the discovered findings and common recommendations.^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

### How to Run

You can trigger the assessment workflow from:

- The UCX-generated README notebook
- The Databricks UI (Workflows > Jobs > \[UCX\] Assessment)
- The Databricks CLI command:

```bash
databricks labs ucx ensure-assessment-run
```

^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

For detailed instructions, see the [Assessment workflow reference](https://databrickslabs.github.io/ucx/docs/reference/workflows/#assessment-workflow) in the UCX documentation.^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

### Rerunning the Workflow

You can run the assessment workflow multiple times to ensure that all incompatible entities are identified and accounted for before starting the migration process.^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Output

The output of each workflow task is stored in [Delta tables](/concepts/delta-lake-table.md) within the `$inventory_database` schema specified during UCX Installation|UCX installation. These tables can be used for further analysis and decision-making, including generating an [assessment report](/concepts/assessments.md) from the collected data.^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Relationship to Other Workflows

The assessment workflow is a prerequisite for subsequent UCX workflows. Both the Group Migration Workflow and the Table Migration Workflow depend on the output of the assessment workflow.^[use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Migration Toolkit (UCX)](/concepts/ucx-unity-catalog-migration-toolkit.md) — The overarching project that includes the assessment workflow.
- Group Migration Workflow — The workflow that upgrades workspace-local groups to account-level groups, depending on assessment output.
- Table Migration Workflow — The workflow that upgrades Hive [Metastore](/concepts/metastore.md) tables to [Unity Catalog](/concepts/unity-catalog.md), depending on assessment output.
- Assessment Dashboard — The dashboard populated with findings after the assessment workflow completes.

## Sources

- use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws.md](/references/use-the-ucx-utilities-to-upgrade-your-workspace-to-unity-catalog-databricks-on-aws-0023b143.md)
