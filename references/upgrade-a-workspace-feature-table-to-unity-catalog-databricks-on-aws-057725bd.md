---
title: Upgrade a workspace feature table to Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/upgrade-feature-table-to-uc
ingestedAt: "2026-06-18T08:10:50.276Z"
---

Upgrade an existing workspace feature table to Unity Catalog by first upgrading the underlying Delta table, then migrating the feature table metadata using `upgrade_workspace_table`.

First, you must upgrade the underlying workspace Delta table. Follow these instructions: [Upgrade tables and views to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate).

After the underlying table and data are available in Unity Catalog, use `upgrade_workspace_table` to upgrade the workspace feature table metadata to Unity Catalog, as illustrated in the following code. Databricks recommends always using the latest version of `databricks-feature-engineering` for this operation, regardless of the Databricks Runtime version you are using.

Python

    %pip install databricks-feature-engineering --upgradedbutils.library.restartPython()from databricks.feature_engineering import UpgradeClientupgrade_client = UpgradeClient()upgrade_client.upgrade_workspace_table(  source_workspace_table='recommender_system.customer_features',  target_uc_table='ml.recommender_system.customer_features')

The following metadata is upgraded to Unity Catalog:

*   Primary keys
*   Time series columns
*   Table and column comments (descriptions)
*   Table and column tags
*   Notebook and job lineage

If the target table has existing table or column comments that are different from the source table, the upgrade method skips upgrading comments and logs a warning. If you are using version 0.1.2 or below of `databricks-feature-engineering`, an error is thrown and the upgrade does not run. For all other metadata, a mismatch between the target table and source table causes an error and prevents the upgrade. To bypass the error and overwrite any existing metadata on the target Unity Catalog table, pass `overwrite = True` to the API:

Python

    upgrade_client.upgrade_workspace_table(  source_workspace_table='recommender_system.customer_features',  target_uc_table='ml.recommender_system.customer_features',  overwrite=True)

note

*   Before calling this API, you must first upgrade the underlying workspace Delta table to Unity Catalog.
*   Upgrading tags and time series columns is not supported in Databricks Runtime 13.2 ML and below.
*   Remember to notify producers and consumers of the upgraded feature table to start using the new table name in Unity Catalog. If the target table in Unity Catalog was upgraded using `CREATE TABLE AS SELECT` or a similar way that cloned the source table, updates to the source table are not automatically synchronized in the target table.
