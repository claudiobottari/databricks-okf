---
title: Feature tables in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc
ingestedAt: "2026-06-18T08:10:45.992Z"
---

In Unity Catalog, any Delta table with a primary key constraint can serve as a feature table. Create feature tables using Databricks SQL, the Python client, or Lakeflow Spark Declarative Pipelines, then update, browse, and govern them using Unity Catalog.

This page applies only to workspaces that are enabled for Unity Catalog. If your workspace is not enabled for Unity Catalog, see [Work with feature tables in Workspace Feature Store (legacy)](https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/feature-tables).

For details about the commands and parameters used in the examples on this page, see the [Feature Engineering Python API reference](https://api-docs.databricks.com/python/feature-engineering/latest/index.html).

## Requirements[​](#requirements "Direct link to Requirements")

Feature Engineering in Unity Catalog requires Databricks Runtime 13.2 or above. In addition, the Unity Catalog metastore must have [Privilege Model Version 1.0](https://docs.databricks.com/aws/en/archive/unity-catalog/upgrade-privilege-model).

## Install Feature Engineering in Unity Catalog Python client[​](#install-feature-engineering-in-unity-catalog-python-client "Direct link to install-feature-engineering-in-unity-catalog-python-client")

Feature Engineering in Unity Catalog has a Python client `FeatureEngineeringClient`. The class is available on PyPI with the `databricks-feature-engineering` package and is pre-installed in Databricks Runtime 13.3 LTS ML and above. If you use a non-ML Databricks Runtime, you must install the client manually. Use the [compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix) to find the correct version for your Databricks Runtime version.

Python

    %pip install databricks-feature-engineeringdbutils.library.restartPython()

## Create a catalog and a schema for feature tables in Unity Catalog[​](#create-a-catalog-and-a-schema-for-feature-tables-in-unity-catalog "Direct link to create-a-catalog-and-a-schema-for-feature-tables-in-unity-catalog")

You must create a new [catalog](https://docs.databricks.com/aws/en/catalogs/) or use an existing catalog for feature tables.

To create a new catalog, you must have the `CREATE CATALOG` privilege on the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore).

SQL

    CREATE CATALOG IF NOT EXISTS <catalog-name>

To use an existing catalog, you must have the `USE CATALOG` privilege on the catalog.

SQL

    USE CATALOG <catalog-name>

Feature tables in Unity Catalog must be stored in a [schema](https://docs.databricks.com/aws/en/schemas/). To create a new schema in the catalog, you must have the `CREATE SCHEMA` privilege on the catalog.

SQL

    CREATE SCHEMA IF NOT EXISTS <schema-name>

## Create a feature table in Unity Catalog[​](#create-a-feature-table-in-unity-catalog "Direct link to create-a-feature-table-in-unity-catalog")

note

You can use an existing Delta table in Unity Catalog that includes a primary key constraint as a feature table. If the table does not have a primary key defined, you must update the table using `ALTER TABLE` DDL statements to add the constraint. See [Use an existing Delta table in Unity Catalog as a feature table](#use-existing-uc-table).

However, adding a primary key to a streaming table or materialized view that was published to Unity Catalog by Lakeflow Spark Declarative Pipelines requires modifying the schema of the streaming table or materialized view definition to include the primary key and then refreshing the streaming table or materialized view. See [Use a streaming table or materialized view created by Lakeflow Spark Declarative Pipelines as a feature table](#use-existing-delta-live-table).

Feature tables in Unity Catalog are [Delta tables](https://docs.databricks.com/aws/en/delta/). Feature tables must have a primary key. Feature tables, like other data assets in Unity Catalog, are accessed using a three-level namespace: `<catalog-name>.<schema-name>.<table-name>`.

You can use Databricks SQL, the Python `FeatureEngineeringClient`, or Lakeflow Spark Declarative Pipelines to create feature tables in Unity Catalog.

*   Databricks SQL
*   Python

You can use any Delta table with a [primary key constraint](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-alter-table-add-constraint) as a feature table. The following code shows how to create a table with a primary key:

SQL

    CREATE TABLE ml.recommender_system.customer_features (  customer_id int NOT NULL,  feat1 long,  feat2 varchar(100),  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id));

To create a [time series feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series), add a time column as a primary key column and specify the [`TIMESERIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-constraint) keyword. The `TIMESERIES` keyword requires Databricks Runtime 13.3 LTS or above.

SQL

    CREATE TABLE ml.recommender_system.customer_features (  customer_id int NOT NULL,  ts timestamp NOT NULL,  feat1 long,  feat2 varchar(100),  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id, ts TIMESERIES));

After the table is created, you can write data to it like other Delta tables, and it can be used as a feature table.

### Create a feature table in Unity Catalog with Lakeflow Spark Declarative Pipelines[​](#create-a-feature-table-in-unity-catalog-with-lakeflow-spark-declarative-pipelines "Direct link to create-a-feature-table-in-unity-catalog-with-lakeflow-spark-declarative-pipelines")

note

Lakeflow Spark Declarative Pipelines support for table constraints is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). The following code examples must be run using the Lakeflow Spark Declarative Pipelines [preview channel](https://docs.databricks.com/aws/en/release-notes/dlt/#runtime-channels).

Any table published from Lakeflow Spark Declarative Pipelines that includes a [primary key constraint](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-alter-table-add-constraint) can be used as a feature table. To create a table in a pipeline with a primary key, you can use either Databricks SQL or the [Lakeflow Spark Declarative Pipelines Python programming interface](https://docs.databricks.com/aws/en/ldp/developer/python-ref).

To create a table in a pipeline with a primary key, use the following syntax:

*   Databricks SQL
*   Python

SQL

    CREATE MATERIALIZED VIEW customer_features (  customer_id int NOT NULL,  feat1 long,  feat2 varchar(100),  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)) AS SELECT * FROM ...;

To create a [time series feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series), add a time column as a primary key column and specify the [`TIMESERIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-constraint) keyword.

*   Databricks SQL
*   Python

SQL

    CREATE MATERIALIZED VIEW customer_features (  customer_id int NOT NULL,  ts timestamp NOT NULL,  feat1 long,  feat2 varchar(100),  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id, ts TIMESERIES)) AS SELECT * FROM ...;

After the table is created, you can write data to it like other Lakeflow Spark Declarative Pipelines datasets, and it can be used as a feature table.

## Use an existing Delta table in Unity Catalog as a feature table[​](#use-an-existing-delta-table-in-unity-catalog-as-a-feature-table "Direct link to use-an-existing-delta-table-in-unity-catalog-as-a-feature-table")

Any Delta table in Unity Catalog with a primary key can be a feature table in Unity Catalog, and you can use the Features UI and API with the table.

note

*   Only the table owner can declare primary key constraints. The owner's name is displayed on the table detail page of Catalog Explorer.
*   Verify the data type in the Delta table is supported by Feature Engineering in Unity Catalog. See [Supported data types](https://docs.databricks.com/aws/en/machine-learning/feature-store/#supported-data-types).
*   The [`TIMESERIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-constraint) keyword requires Databricks Runtime 13.3 LTS or above.

If an existing Delta table does not have a [primary key constraint](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-alter-table-add-constraint), you can create one as follows:

1.  Set primary key columns to `NOT NULL`. For each primary key column, run:
    
    SQL
    
        ALTER TABLE <full_table_name> ALTER COLUMN <pk_col_name> SET NOT NULL
    
2.  Alter the table to add the primary key constraint:
    
    SQL
    
        ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1, pk_col2, ...)
    
    `pk_name` is the name of the primary key constraint. By convention, you can use the table name (without schema and catalog) with a `_pk` suffix. For example, a table with the name `"ml.recommender_system.customer_features"` would have `customer_features_pk` as the name of its primary key constraint.
    
    To make the table a [time series feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series), specify the [`TIMESERIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-constraint) keyword on one of the primary key columns, as follows:
    
    SQL
    
        ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1 TIMESERIES, pk_col2, ...)
    
    After you add the primary key constraint on the table, the table appears in the Features UI and you can use it as a feature table.
    

## Use a streaming table or materialized view created by Lakeflow Spark Declarative Pipelines as a feature table[​](#use-a-streaming-table-or-materialized-view-created-by-lakeflow-spark-declarative-pipelines-as-a-feature-table "Direct link to use-a-streaming-table-or-materialized-view-created-by-lakeflow-spark-declarative-pipelines-as-a-feature-table")

Any streaming table or materialized view in Unity Catalog with a primary key can be a feature table in Unity Catalog, and you can use the Features UI and API with the table.

note

*   Lakeflow Spark Declarative Pipelines support for table constraints is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). The following code examples must be run using the Lakeflow Spark Declarative Pipelines [preview channel](https://docs.databricks.com/aws/en/release-notes/dlt/#runtime-channels).
*   Only the table owner can declare primary key constraints. The owner's name is displayed on the table detail page of Catalog Explorer.
*   Verify that Feature Engineering in Unity Catalog supports the data type in the Delta table. See [Supported data types](https://docs.databricks.com/aws/en/machine-learning/feature-store/#supported-data-types).

To set primary keys for an existing streaming table or materialized view, update the schema of the streaming table or materialized view in the notebook that manages the object. Then, [refresh the table](https://docs.databricks.com/aws/en/ldp/updates#refresh-selection) to update the Unity Catalog object.

The following is the syntax to add a primary key to a materialized view:

*   Databricks SQL
*   Python

SQL

    CREATE OR REFRESH MATERIALIZED VIEW existing_live_table(  id int NOT NULL PRIMARY KEY,  ...) AS SELECT ...

## Use an existing view in Unity Catalog as a feature table[​](#use-an-existing-view-in-unity-catalog-as-a-feature-table "Direct link to use-an-existing-view-in-unity-catalog-as-a-feature-table")

To use a view as a feature table, you must use `databricks-feature-engineering` version 0.7.0 or above, which is built into Databricks Runtime 16.0 ML.

A simple SELECT view in Unity Catalog can be a feature table in Unity Catalog, and you can use the Features API with the table.

note

*   A simple SELECT view is defined as a view created from a single Delta table in Unity Catalog that can be used as a feature table, and whose primary keys are selected without JOIN, GROUP BY, or DISTINCT clauses. Acceptable keywords in the SQL statement are SELECT, FROM, WHERE, ORDER BY, LIMIT, and OFFSET.
*   See [Supported data types](https://docs.databricks.com/aws/en/machine-learning/feature-store/#supported-data-types) for supported data types.
*   Feature tables backed by views do not appear in the Features UI.
*   If columns are renamed in the source Delta table, the columns in the SELECT statement for the view definition must be renamed to match.

Here is an example of a simple SELECT view that can be used as a feature table:

SQL

    CREATE OR REPLACE VIEW ml.recommender_system.content_recommendation_subset ASSELECT    user_id,    content_id,    user_age,    user_gender,    content_genre,    content_release_year,    user_content_watch_duration,    user_content_like_dislike_ratioFROM    ml.recommender_system.content_recommendations_featuresWHERE    user_age BETWEEN 18 AND 35    AND content_genre IN ('Drama', 'Comedy', 'Action')    AND content_release_year >= 2010    AND user_content_watch_duration > 60;

Feature tables based on views can be used for offline model training and evaluation. They cannot be published to online stores. Features from these tables and models based on these features cannot be served.

## Update a feature table in Unity Catalog[​](#update-a-feature-table-in-unity-catalog "Direct link to update-a-feature-table-in-unity-catalog")

You can update a feature table in Unity Catalog by adding new features or by modifying specific rows based on the primary key.

The following feature table metadata should not be updated:

*   Primary key.
*   Partition key.
*   Name or data type of an existing feature.

Altering them will cause downstream pipelines that use features for training and serving models to break.

### Add new features to an existing feature table in Unity Catalog[​](#add-new-features-to-an-existing-feature-table-in-unity-catalog "Direct link to add-new-features-to-an-existing-feature-table-in-unity-catalog")

You can add new features to an existing feature table in one of two ways:

*   Update the existing feature computation function and run `write_table` with the returned DataFrame. This updates the feature table schema and merges new feature values based on the primary key.
*   Create a new feature computation function to calculate the new feature values. The DataFrame returned by this new computation function must contain the feature tables' primary and partition keys (if defined). Run `write_table` with the DataFrame to write the new features to the existing feature table using the same primary key.

### Update only specific rows in a feature table[​](#update-only-specific-rows-in-a-feature-table "Direct link to Update only specific rows in a feature table")

Use `mode = "merge"` in `write_table`. Rows whose primary key does not exist in the DataFrame sent in the `write_table` call remain unchanged.

Python

    from databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()fe.write_table(  name='ml.recommender_system.customer_features',  df = customer_features_df,  mode = 'merge')

### Schedule a job to update a feature table[​](#schedule-a-job-to-update-a-feature-table "Direct link to Schedule a job to update a feature table")

To ensure that features in feature tables always have the most recent values, Databricks recommends that you create a job that runs a notebook to update your feature table on a regular basis, such as every day. If you already have a non-scheduled job created, you can convert it to a scheduled job to ensure the feature values are always up-to-date. See [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/).

Code to update a feature table uses `mode='merge'`, as shown in the following example.

Python

    from databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()customer_features_df = compute_customer_features(data)fe.write_table(  df=customer_features_df,  name='ml.recommender_system.customer_features',  mode='merge')

### Store past values of daily features[​](#store-past-values-of-daily-features "Direct link to Store past values of daily features")

Define a feature table with a composite primary key. Include the date in the primary key. For example, for a feature table `customer_features`, you might use a composite primary key (`date`, `customer_id`) and partition key `date` for efficient reads.

Databricks recommends that you enable [liquid clustering](https://docs.databricks.com/aws/en/tables/clustering) on the table for efficient reads. If you do not use liquid clustering, set the date column as a partition key for better read performance.

*   Databricks SQL
*   Python

SQL

    CREATE TABLE ml.recommender_system.customer_features (  customer_id int NOT NULL,  `date` date NOT NULL,  feat1 long,  feat2 varchar(100),  CONSTRAINT customer_features_pk PRIMARY KEY (`date`, customer_id))-- If you are not using liquid clustering, uncomment the following line.-- PARTITIONED BY (`date`)COMMENT "Customer features";

You can then create code to read from the feature table filtering `date` to the time period of interest.

You can also create a [time series feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series) which enables point-in-time lookups when you use `create_training_set` or `score_batch`. See [Create a feature table in Unity Catalog](#create-feature-table).

To keep the feature table up to date, set up a regularly scheduled job to write features or stream new feature values into the feature table.

### Create a streaming feature computation pipeline to update features[​](#create-a-streaming-feature-computation-pipeline-to-update-features "Direct link to Create a streaming feature computation pipeline to update features")

To create a streaming feature computation pipeline, pass a streaming `DataFrame` as an argument to `write_table`. This method returns a `StreamingQuery` object.

Python

    def compute_additional_customer_features(data):  ''' Returns Streaming DataFrame  '''  passfrom databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()customer_transactions = spark.readStream.table("prod.events.customer_transactions")stream_df = compute_additional_customer_features(customer_transactions)fe.write_table(  df=stream_df,  name='ml.recommender_system.customer_features',  mode='merge')

## Read from a feature table in Unity Catalog[​](#read-from-a-feature-table-in-unity-catalog "Direct link to read-from-a-feature-table-in-unity-catalog")

Use `read_table` to read feature values.

Python

    from databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()customer_features_df = fe.read_table(  name='ml.recommender_system.customer_features',)

## Search and browse feature tables in Unity Catalog[​](#search-and-browse-feature-tables-in-unity-catalog "Direct link to search-and-browse-feature-tables-in-unity-catalog")

Use the Features UI to search for or browse feature tables in Unity Catalog.

1.  Click ![Feature Store Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAABRElEQVRIDWNUsHT6zzAAgGkA7ARbOWox3UKehRybVkztYzA31Ceo9cnzFwzpZfUM1+7ewVBL0ziWkZRg6K4rxbAUJMBIy+x0/9hesKWKVs5gGpmgqY+RLUJnExXH1IhTdIup6mN8cYpuMVE+jsguQteHlQ+KUy1VFaxy6IJU9TG64fj4WH0sIiDIMLe3lUFPUx2fXoZL128yJBdXM7z58B6vOmySWH1MjKUgw0AOA6klB2D1McynJp7BDG8/fsBqrjC/AMOZ7WsJhgpWzUBBrBbDFOOyFCSPTw6m/+T5izAmBo3XYgzVJArgyw1Y45hE88lSPmAWUzWo8cUperBQ1WJ8cYpuMd6gBmUZXACfHC49yOJYfQwqkUB5GZRPCQGQWnIAVh+DikFiDIQVmeRYTNMWCD4HYfUxPg3Ukhu1mFohSdAcAKHrUqbEeRf4AAAAAElFTkSuQmCC) **Features** in the sidebar to display the Features UI.
    
2.  Select catalog with the catalog selector to view all of the available feature tables in that catalog. In the search box, enter all or part of the name of a feature table, a feature, or a comment. You can also enter all or part of the [key or value of a tag](#feature-table-tags). Search text is case-insensitive.
    
    ![Feature search example](https://docs.databricks.com/aws/en/assets/images/feature-search-example-uc-16dbd302e1a2dbbe8880e4a56cf27f98.png)
    

Use `get_table` to get feature table metadata.

Python

    from databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()ft = fe.get_table(name="ml.recommender_system.user_feature_table")print(ft.features)

You can use tags, which are simple key-value pairs, to categorize and manage your feature tables and features.

For feature tables, you can create, edit, and delete tags using Catalog Explorer, SQL statements in a notebook or SQL query editor, or the Feature Engineering Python API.

For features, you can create, edit, and delete tags using Catalog Explorer or SQL statements in a notebook or SQL query editor.

See [Apply tags to Unity Catalog securable objects](https://docs.databricks.com/aws/en/database-objects/tags) and [Feature Engineering Python API](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

The following example shows how to use the Feature Engineering Python API to create, update, and delete feature table tags.

Python

    from databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()# Create feature table with tagscustomer_feature_table = fe.create_table(  # ...  tags={"tag_key_1": "tag_value_1", "tag_key_2": "tag_value_2", ...},  # ...)# Upsert a tagfe.set_feature_table_tag(name="customer_feature_table", key="tag_key_1", value="new_key_value")# Delete a tagfe.delete_feature_table_tag(name="customer_feature_table", key="tag_key_2")

## Delete a feature table in Unity Catalog[​](#delete-a-feature-table-in-unity-catalog "Direct link to delete-a-feature-table-in-unity-catalog")

You can delete a feature table in Unity Catalog by directly deleting the Delta table in Unity Catalog using Catalog Explorer or using the [Feature Engineering Python API](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

note

*   Deleting a feature table can lead to unexpected failures in upstream producers and downstream consumers (models, endpoints, and scheduled jobs). You must delete published online stores with your cloud provider.
*   When you delete a feature table in Unity Catalog, the underlying Delta table is also dropped.
*   `drop_table` is not supported in Databricks Runtime 13.1 ML or below. Use SQL command to delete the table.

You can use Databricks SQL or `FeatureEngineeringClient.drop_table` to delete a feature table in Unity Catalog:

*   Databricks SQL
*   Python

SQL

    DROP TABLE ml.recommender_system.customer_features;

A feature table in Unity Catalog is accessible to all workspaces assigned to the table's Unity Catalog metastore.

To share a feature table with workspaces that are not assigned to the same Unity Catalog metastore, use [OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/).

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**Error message: `Feature tables must have a primary key`**

The feature table must have a primary key constraint. See [Use an existing Delta table in Unity Catalog as a feature table](#use-existing-uc-table).

## Example notebooks[​](#example-notebooks "Direct link to Example notebooks")

The basic notebook shows how to create a feature table, use it to train a model, and run batch scoring using automatic feature lookup. It also shows the Feature Engineering UI, which you can use to search for features and understand how features are created and used.

#### Basic Feature Engineering in Unity Catalog example notebook

The taxi example notebook illustrates the process of creating features, updating them, and using them for model training and batch inference.

#### Feature Engineering in Unity Catalog taxi example notebook
