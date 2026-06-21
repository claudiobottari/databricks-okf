---
title: Use the UCX utilities to upgrade your workspace to Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/ucx
ingestedAt: "2026-06-18T08:04:56.319Z"
---

This article introduces [UCX](https://github.com/databrickslabs/ucx), a Databricks Labs project that provides tools to help you upgrade your non-Unity-Catalog workspace to Unity Catalog.

note

UCX, like all projects in the databrickslabs GitHub account, is provided for your exploration only, and is not formally supported by Databricks with service-level agreements (SLAs). It is provided as-is. We make no guarantees of any kind. Do not submit a Databricks support ticket relating to issues that arise from the use of this project. Instead, file a [GitHub issue](https://github.com/databrickslabs/ucx/issues/new/choose). Issues will be reviewed as time permits, but there are no formal SLAs for support.

The UCX project provides the following migration tools and workflows:

1.  [Assessment workflow](#assessment) to help you plan your migration.
2.  [Group migration workflow](#group) to help you upgrade group membership from your workspace to your Databricks account and migrate permissions to the new account-level groups.
3.  [Table migration workflow](#table) to help you upgrade tables that are registered in your workspace's Hive metastore to the Unity Catalog metastore. This workflow also helps you migrate storage locations and the credentials required to access them.

This diagram shows the overall migration flow, identifying migration workflows and utilities by name:

![UCX migration workflows chart](https://docs.databricks.com/aws/en/assets/images/ucx-migration-flow-f9cdadba655682595859fd005b81dee3.png)

note

The code migration workflow that is depicted in the diagram remains under development and is not yet available.

For a demo of upgrading your workspace using UXC, see [Schema Upgrade Using UCX](https://app.getreprise.com/launch/96m2d3n/).

## Before you begin[​](#before-you-begin "Direct link to Before you begin")

Before you can install UCX and run the UCX workflows, your environment must meet the following requirements.

**Packages installed on the computer where you run UCX**:

*   Databricks CLI v0.213 or above. See [Install or update the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install).
    
    You must have a Databricks configuration file with configuration profiles for both the workspace and the Databricks account.
    
*   Python 3.10 or above.
    
*   If you want to run the UCX workflow that identifies storage locations used by Hive tables in your workspace (recommended, but not required), you must have the CLI for your cloud storage provider (Azure CLI or AWS CLI) installed on the computer where you run the UCX workflows.
    

**Network access**:

*   Network access from the computer that runs the UCX installation to the Databricks workspace that you are migrating.
*   Network access to the internet from the computer that runs the UCX installation. This is required for access to pypi.org and github.com.
*   Network access from your Databricks workspace to pypi.org to download the `databricks-sdk` and `pyyaml` packages.

**Databricks roles and permissions**:

*   Databricks account admin and workspace admin roles for the user who runs the UCX installation. You cannot run the installation as a service principal.

**Other Databricks prerequisites**:

*   A Unity Catalog metastore created for every region that hosts a workspace that you want to upgrade, with each of those Databricks workspaces attached to a Unity Catalog metastore.
    
    To learn how to determine whether you already have a Unity Catalog metastore in the relevant workspace regions, how to create a metastore if you don't, and how to attach a Unity Catalog metastore to a workspace, see [Step 1: Confirm that your workspace is enabled for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/setup-uc#confirm-uc) in the Unity Catalog setup article. As an alternative, UCX provides [a utility for assigning Unity Catalog metastores to workspaces](https://databrickslabs.github.io/ucx/docs/reference/commands/#assign-metastore) that you can use after UCX is installed.
    
    Attaching a Unity Catalog metastore to a workspace also enables _identity federation_, in which you centralize user management at the Databricks account level, which is also a prerequisite for using UCX. See [Enable identity federation](https://docs.databricks.com/aws/en/admin/users-groups/best-practices#identity-federation).
    
*   If your workspace uses an external Hive metastore (such as AWS Glue) instead of the default workspace-local Hive metastore, you must perform some prerequisite setup. See [External Hive Metastore Integration](https://databrickslabs.github.io/ucx/docs/reference/external_hms_glue/) in the UCX documentation.
    
*   A Pro or Serverless SQL warehouse running on the workspace where you run UCX workflows, required to render the report generated by the assessment workflow.
    

## Install UCX[​](#install-ucx "Direct link to Install UCX")

To install UCX, use the Databricks CLI:

Bash

    databricks labs install ucx

You are prompted to select the following:

1.  The Databricks configuration profile for the workspace that you want to upgrade. The configuration file must also include a configuration profile for the workspace's parent Databricks account.
    
2.  A name for the inventory database that will be used to store the output of the migration workflows. Typically it's fine to select the default, which is `ucx`.
    
3.  A SQL warehouse to run the installation process on.
    
4.  A list of workspace-local groups you want to migrate to account-level groups. If you leave this as the default (`<ALL>`), any existing account-level group whose name matches a workspace-local group will be treated as the replacement for that workspace-local group and will inherit all of its workspace permissions when you run the [group migration workflow](#group) after installation.
    
    You do have the opportunity to modify the workspace-group-to-account-group mapping after you run the installer and before you run group migration. See [Group Name Conflict Resolution](https://github.comthat/databrickslabs/ucx/blob/main/docs/group_name_conflict.md) in the UCX repo.
    
5.  If you have an external Hive metastore, such as AWS Glue, you have the option to connect to it or not. See [External Hive Metastore Integration](https://github.com/databrickslabs/ucx/blob/main/docs/external_hms_glue.md) in the databrickslabs/ucx repo.
    
6.  Whether to open the generated README notebook.
    

When the installation is done, it deploys a README notebook, dashboards, databases, libraries, jobs, and other assets in your workspace.

For more information, see the [installation instructions in the project readme](https://github.com/databrickslabs/ucx#install-ucx). You can also [install UCX on all of the workspaces in your Databricks account](https://github.com/databrickslabs/ucx#advanced-installing-ucx-on-all-workspaces-within-a-databricks-account).

## Open the README notebook[​](#open-the-readme-notebook "Direct link to Open the README notebook")

Every installation creates a README notebook that provides a detailed description of all workflows and tasks, with quick links to the workflows and dashboards. See [Readme notebook](https://github.com/databrickslabs/ucx/blob/main/README.md#readme-notebook).

## Step 1. Run the assessment workflow[​](#step-1-run-the-assessment-workflow "Direct link to step-1-run-the-assessment-workflow")

The assessment workflow assesses the Unity Catalog compatibility of group identities, storage locations, storage credentials, access controls, and tables in the current workspace and provides the information necessary for planning the migration to Unity Catalog. The tasks in the assessment workflow can be executed in parallel or sequentially, depending on specified dependencies. After the assessment workflow finishes, an assessment dashboard is populated with findings and common recommendations.

The output of each workflow task is stored in Delta tables in the `$inventory_database` schema that you specify during installation. You can use these tables to perform further analysis and decision-making using an [assessment report](https://databrickslabs.github.io/ucx/docs/reference/assessment/). You can run the assessment workflow multiple times to ensure that all incompatible entities are identified and accounted for before you start the migration process.

You can trigger the assessment workflow from the UCX-generated README notebook and the Databricks UI (Workflows > Jobs > \[UCX\] Assessment), or run the following Databricks CLI command:

Bash

    databricks labs ucx ensure-assessment-run

For detailed instructions, see [Assessment workflow](https://databrickslabs.github.io/ucx/docs/reference/workflows/#assessment-workflow).

## Step 2. Run the group migration workflow[​](#step-2-run-the-group-migration-workflow "Direct link to step-2-run-the-group-migration-workflow")

The group migration workflow upgrades workspace-local groups to account-level groups to support Unity Catalog. It ensures that the appropriate account-level groups are available in the workspace and replicates all permissions. It also removes any unnecessary groups and permissions from the workspace. The tasks in the group migration workflow depend on the output of the assessment workflow.

The output of each workflow task is stored in Delta tables in the `$inventory_database` schema that you specify during installation. You can use these tables to perform further analysis and decision-making. You can run the group migration workflow multiple times to ensure that all groups are upgraded successfully and that all necessary permissions are assigned.

For information about running the group migration workflow, see your UCX-generated README notebook and [Group migration workflow](https://databrickslabs.github.io/ucx/docs/reference/workflows/#group-migration-workflow) in the UCX readme.

## Step 3. Run the table migration workflow[​](#step-3-run-the-table-migration-workflow "Direct link to step-3-run-the-table-migration-workflow")

The table migration workflow upgrades tables from the Hive metastore to the Unity Catalog metastore. External tables in the Hive metastore are upgraded as external tables in Unity Catalog, using [SYNC](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-sync). Managed tables in the Hive metastore that are stored in workspace storage (also known as DBFS root) are upgraded as managed tables in Unity Catalog, using [DEEP CLONE](https://docs.databricks.com/aws/en/tables/operations/clone).

Hive managed tables must be in Delta or Parquet format to be upgraded. External Hive tables must be in one of the data formats listed in [Work with external tables](https://docs.databricks.com/aws/en/tables/external).

### Run the preparatory commands[​](#run-the-preparatory-commands "Direct link to Run the preparatory commands")

Table migration includes a number of preparatory tasks that you run before you run the table migration workflow. You perform these tasks using the following Databricks CLI commands:

*   The `create-table-mapping` command, which creates a CSV file that maps a target Unity Catalog catalog, schema, and table to each Hive table that will be upgraded. You should review and update the mapping file before proceeding with the migration workflow.
*   The `create-uber-principal` command, which creates a service principal with read-only access to all storage used by the tables in this workspace. The workflow job compute resource uses this principal to upgrade the tables in the workspace. Deprovision this service principal when you are done with your upgrade.
*   (Optional) The `principal-prefix-access` command, which identifies the storage accounts and storage access credentials used by the Hive tables in the workspace.
*   (Optional) The `migrate-credentials` command, which creates Unity Catalog storage credentials from the storage access credentials identified by `principal-prefix-access`.
*   (Optional) The `migration locations` command, which creates Unity Catalog external locations from the storage locations identified by the assessment workflow, using the storage credentials created by `migrate-credentials`.
*   (Optional) The `create-catalogs-schemas`command, which creates Unity Catalog catalogs and schemas that will hold the upgraded tables.

For details, including additional table migration workflow commands and options, see [Table migration commands](https://databrickslabs.github.io/ucx/docs/reference/commands/#table-migration-commands) in the UCX readme.

### Run the table migration[​](#run-the-table-migration "Direct link to Run the table migration")

Once you've run the preparatory tasks, you can run the table migration workflow from the UCX-generated README notebook or from **Jobs & Pipelines** in the workspace UI.

The output of each workflow task is stored in Delta tables in the `$inventory_database` schema that you specify during installation. You can use these tables to perform further analysis and decision-making. You might need to run the table migration workflow multiple times to ensure that all tables are upgraded successfully.

For complete table migration instructions, see your UCX-generated README notebook and the [Table Migration Workflows](https://databrickslabs.github.io/ucx/docs/reference/workflows/#table-migration-workflows) in the UCX readme.

UCX also includes:

*   Utilities for enabling [Hive metastore federation](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts), the Databricks integration tool that enables Unity Catalog to govern tables registered in a Hive metastore:
    
    *   `enable-hms-federation`
    *   `create-federated-catalog`
    
    Hive metastore federation aids in migration by enabling you to run workloads on both your legacy Hive metastore and its mirror in Unity Catalog, easing the transition to Unity Catalog. For more information about using Hive metastore federation in a migration scenario, see [How do you use Hive metastore federation during migration to Unity Catalog?](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts#migration).
    
*   Debugging tools and other utilities to help you succeed with your migration.
    

For more information, see your UCX-generated README notebook and the [UCX project documentation](https://databrickslabs.github.io/ucx/docs/gettingstarted/).

## Upgrade your UCX installation[​](#upgrade-your-ucx-installation "Direct link to Upgrade your UCX installation")

The UCX project is updated regularly. To upgrade your UCX installation to the latest version:

1.  Verify that UCX is installed.
    
    Bash
    
        databricks labs installedName  Description                            Versionucx   Unity Catalog Migration Toolkit (UCX)  0.20.0
    
2.  Run the upgrade:
    
    Bash
    
        databricks labs upgrade ucx
    

## Get help[​](#get-help "Direct link to Get help")

For help with the UCX CLI, run:

Bash

    databricks labs ucx --help

For help with a specific UCX command, run:

Bash

    databricks labs ucx <command> --help

To troubleshoot issues:

*   Run `--debug` with any command to enable [debug logs](https://databrickslabs.github.io/ucx/docs/reference/troubleshooting/#ucx-command-lines).
*   See the [UCX troubleshooting guide](https://databrickslabs.github.io/ucx/docs/reference/troubleshooting/) for more details.

To file an issue or feature request, file a [GitHub issue](https://github.com/databrickslabs/ucx/issues/new/choose).

## UCX release notes[​](#ucx-release-notes "Direct link to UCX release notes")

See the [changelog](https://github.com/databrickslabs/ucx/blob/main/CHANGELOG.md) in the UCX GitHub repo.
