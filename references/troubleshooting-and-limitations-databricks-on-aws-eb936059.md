---
title: Troubleshooting and limitations | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/troubleshooting-and-limitations
ingestedAt: "2026-06-18T08:10:44.110Z"
---

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### "Database recommender\_system does not exist in the Hive metastore."[​](#database-recommender_system-does-not-exist-in-the-hive-metastore "Direct link to \"Database recommender_system does not exist in the Hive metastore.\"")

A feature table is stored as a Delta table. The database is specified by the table name prefix, so a feature table _recommender\_system.customer\_features_ will be stored in the _recommender\_system_ database.

To create the database, run:

    %sql CREATE DATABASE IF NOT EXISTS recommender_system;

### "ModuleNotFoundError: No module named 'databricks.feature\_engineering'" or "ModuleNotFoundError: No module named 'databricks.feature\_store'"[​](#modulenotfounderror-no-module-named-databricksfeature_engineering-or-modulenotfounderror-no-module-named-databricksfeature_store "Direct link to \"ModuleNotFoundError: No module named 'databricks.feature_engineering'\" or \"ModuleNotFoundError: No module named 'databricks.feature_store'\"")

This error occurs when databricks-feature-engineering is not installed on the Databricks Runtime you are using.

databricks-feature-engineering [is available on PyPI](https://pypi.org/project/databricks-feature-engineering/), and can be installed with:

    %pip install databricks-feature-engineering

### "ModuleNotFoundError: No module named 'databricks.feature\_store'"[​](#modulenotfounderror-no-module-named-databricksfeature_store "Direct link to \"ModuleNotFoundError: No module named 'databricks.feature_store'\"")

This error occurs when databricks-feature-store is not installed on the Databricks Runtime you are using.

note

For Databricks Runtime 14.3 and above, install databricks-feature-engineering instead via `%pip install databricks-feature-engineering`

databricks-feature-store [is available on PyPI](https://pypi.org/project/databricks-feature-store/), and can be installed with:

    %pip install databricks-feature-store

### "Invalid input. Data is not compatible with model signature. Cannot convert non-finite values...'"[​](#invalid-input-data-is-not-compatible-with-model-signature-cannot-convert-non-finite-values "Direct link to \"Invalid input. Data is not compatible with model signature. Cannot convert non-finite values...'\"")

This error can occur when using a Feature Store-packaged model in Model Serving. When providing custom feature values in an input to the endpoint, you must provide a value for the feature for each row in the input, or for no rows. You cannot provide custom values for a feature for only some rows.

### "No suitable online store found for feature tables"[​](#no-suitable-online-store-found-for-feature-tables "Direct link to \"No suitable online store found for feature tables\"")

This error occurs when creating or rebuilding a serving endpoint for a [model with automatic feature lookup](https://docs.databricks.com/aws/en/machine-learning/feature-store/automatic-feature-lookup) or [feature serving](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving). The error message shows up in the failed serving endpoint's Events Log. It indicates a disconnect between your offline feature table and the Online Feature Store.

#### Cause 1: Table not published[​](#cause-1-table-not-published "Direct link to Cause 1: Table not published")

Offline feature tables need to be available in an online store for lookup. The most common cause of the error is that the required feature table (listed in the error message) has not yet been published to the Online Feature Store.

**Resolution**: Follow the [Online Feature Store instructions](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store#publish-a-feature-table) to publish the table(s) mentioned in the error.

#### Cause 2: Source table recreated (ID mismatch)[​](#cause-2-source-table-recreated-id-mismatch "Direct link to Cause 2: Source table recreated (ID mismatch)")

In this case, an offline feature table was published to an online store, and subsequently the offline feature table was dropped then recreated. The online table tracks its source via `source_table_id`, which points to the offline table's `table_id`. Even if the re-created offline feature table has the same name, it has a new `table_id`, so the online table's `source_table_id` still points at the old (dropped) offline table.

**Diagnosis**: You can verify if this is the problem using the following steps:

1.  Get the offline Feature Table ID:
    *   Navigate to [Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/).
    *   Locate your Feature Table.
    *   Open the **Details** tab and find the `table_id`.
2.  Get the Online Table Source ID:
    *   Locate the corresponding Online Table in Catalog Explorer.
    *   Open the **Details** tab.
    *   Look under **Properties** to find the `source_table_id`.

If the IDs don't match, the link is broken. This means the offline source table was recreated. There are two options for resolving this issue.

**Resolution Option 1: Restore the previous offline table**:

*   Use [ALTER TABLE RENAME TO](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-alter-table) command to change the name of the current table.
*   Use [UNDROP TABLE WITH ID](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-undrop-table) command to restore the previous table using the `source_table_id` recorded in the Online Table property.
*   Update or recreate the serving endpoint to connect with the new online tables.

**Resolution Option 2: Keep the current offline table and publish it to a new online store**:

*   Follow instructions to [publish the feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store#publish-a-feature-table).
*   Update or recreate the serving endpoint to connect with the new online tables.
*   _Optional_: Clean up the old online table to avoid confusion.

## Limitations[​](#limitations "Direct link to Limitations")

*   A FeatureSpec can contain a maximum of 1000 features. Using a large number of features in a single FeatureSpec can increase feature serving latency.
    
*   A maximum of 50 tables can be used to train a model.
    
*   A maximum of 100 on-demand features can be used in a model.
    
*   Databricks Runtime ML clusters are not supported when using Lakeflow Spark Declarative Pipelines as feature tables. Instead, use a standard access mode compute resource and manually install the client using `pip install databricks-feature-engineering`. You must also install any other required ML libraries.
    
    Python
    
        %pip install databricks-feature-engineering
    
*   Databricks legacy Workspace Feature Store does not support deleting individual features from a feature table.
