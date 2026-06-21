---
title: Work with feature tables in Workspace Feature Store (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/feature-tables
ingestedAt: "2026-06-18T08:10:55.722Z"
---

This page describes how to create and work with feature tables in the Workspace Feature Store.

note

If your workspace is enabled for Unity Catalog, any table managed by Unity Catalog that has a primary key is automatically a feature table that you can use for model training and inference. All Unity Catalog capabilities, such as security, lineage, tagging, and cross-workspace access, are automatically available to the feature table. For information about working with feature tables in a Unity Catalog\-enabled workspace, see [Feature tables in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc).

For information about tracking feature lineage and freshness, see [Explore features and lineage (legacy)](https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/ui).

note

Database and feature table names can contain only alphanumeric characters and underscores (\_).

## Create a database for feature tables[​](#create-a-database-for-feature-tables "Direct link to Create a database for feature tables")

Before creating any feature tables, you must create a [database](https://docs.databricks.com/aws/en/schemas/) to store them.

    %sql CREATE DATABASE IF NOT EXISTS <database-name>

Feature tables are stored as [Delta tables](https://docs.databricks.com/aws/en/delta/). When you create a feature table with `create_table` (Feature Store client v0.3.6 and above) or `create_feature_table` (v0.3.5 and below), you must specify the database name. For example, this argument creates a Delta table named `customer_features` in the database `recommender_system`.

`name='recommender_system.customer_features'`

When you publish a feature table to an online store, the default table and database name are the ones specified when you created the table; you can specify different names using the `publish_table` method.

The Databricks Feature Store UI shows the name of the table and database in the online store, along with other metadata.

## Create a feature table in Databricks Feature Store[​](#create-a-feature-table-in-databricks-feature-store "Direct link to create-a-feature-table-in-databricks-feature-store")

The basic steps to creating a feature table are:

1.  Write the Python functions to compute the features. The output of each function should be an Apache Spark DataFrame with a unique primary key. The primary key can consist of one or more columns.
2.  Create a feature table by instantiating a `FeatureStoreClient` and using `create_table` (v0.3.6 and above) or `create_feature_table` (v0.3.5 and below).
3.  Populate the feature table using `write_table`.

For details about the commands and parameters used in the following examples, see the [Feature Store Python API reference](https://api-docs.databricks.com/python/feature-store/latest/index.html).

*   V0.3.6 and above
*   V0.3.5 and below

Python

    from databricks.feature_store import feature_tabledef compute_customer_features(data):  ''' Feature computation code returns a DataFrame with 'customer_id' as primary key'''  pass# create feature table keyed by customer_id# take schema from DataFrame output by compute_customer_featuresfrom databricks.feature_store import FeatureStoreClientcustomer_features_df = compute_customer_features(df)fs = FeatureStoreClient()customer_feature_table = fs.create_table(  name='recommender_system.customer_features',  primary_keys='customer_id',  schema=customer_features_df.schema,  description='Customer features')# An alternative is to use `create_table` and specify the `df` argument.# This code automatically saves the features to the underlying Delta table.# customer_feature_table = fs.create_table(#  ...#  df=customer_features_df,#  ...# )# To use a composite key, pass all keys in the create_table call# customer_feature_table = fs.create_table(#   ...#   primary_keys=['customer_id', 'date'],#   ...# )# Use write_table to write data to the feature table# Overwrite mode does a full refresh of the feature tablefs.write_table(  name='recommender_system.customer_features',  df = customer_features_df,  mode = 'overwrite')

## Register an existing Delta table as a feature table[​](#register-an-existing-delta-table-as-a-feature-table "Direct link to register-an-existing-delta-table-as-a-feature-table")

With v0.3.8 and above, you can register an existing [Delta table](https://docs.databricks.com/aws/en/delta/) as a feature table. The Delta table must exist in the metastore.

Python

    fs.register_table(  delta_table='recommender.customer_features',  primary_keys='customer_id',  description='Customer features')

## Control access to feature tables[​](#control-access-to-feature-tables "Direct link to Control access to feature tables")

See [Access control (legacy)](https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/access-control).

## Update a feature table[​](#update-a-feature-table "Direct link to Update a feature table")

You can update a feature table by adding new features or by modifying specific rows based on the primary key.

The following feature table metadata cannot be updated:

*   Primary key
*   Partition key
*   Name or type of an existing feature

### Add new features to an existing feature table[​](#add-new-features-to-an-existing-feature-table "Direct link to Add new features to an existing feature table")

You can add new features to an existing feature table in one of two ways:

*   Update the existing feature computation function and run `write_table` with the returned DataFrame. This updates the feature table schema and merges new feature values based on the primary key.
*   Create a new feature computation function to calculate the new feature values. The DataFrame returned by this new computation function must contain the feature tables's primary keys and partition keys (if defined). Run `write_table` with the DataFrame to write the new features to the existing feature table, using the same primary key.

### Update only specific rows in a feature table[​](#update-only-specific-rows-in-a-feature-table "Direct link to Update only specific rows in a feature table")

Use `mode = "merge"` in `write_table`. Rows whose primary key does not exist in the DataFrame sent in the `write_table` call remain unchanged.

Python

    fs.write_table(  name='recommender.customer_features',  df = customer_features_df,  mode = 'merge')

### Schedule a job to update a feature table[​](#schedule-a-job-to-update-a-feature-table "Direct link to Schedule a job to update a feature table")

To ensure that features in feature tables always have the most recent values, Databricks recommends that you create a job that runs a notebook to update your feature table on a regular basis, such as every day. If you already have a non-scheduled job created, you can convert it to a scheduled job to make sure the feature values are always up-to-date. See [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/).

Code to update a feature table uses `mode='merge'`, as shown in the following example.

Python

    fs = FeatureStoreClient()customer_features_df = compute_customer_features(data)fs.write_table(  df=customer_features_df,  name='recommender_system.customer_features',  mode='merge')

### Store past values of daily features[​](#store-past-values-of-daily-features "Direct link to Store past values of daily features")

Define a feature table with a composite primary key. Include the date in the primary key. For example, for a feature table `store_purchases`, you might use a composite primary key (`date`, `user_id`) and partition key `date` for efficient reads.

Python

    fs.create_table(  name='recommender_system.customer_features',  primary_keys=['date', 'customer_id'],  partition_columns=['date'],  schema=customer_features_df.schema,  description='Customer features')

You can then create code to read from the feature table filtering `date` to the time period of interest.

You can also create a [time series feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series) by specifying the `date` column as a timestamp key using the `timestamp_keys` argument.

Python

    fs.create_table(  name='recommender_system.customer_features',  primary_keys=['date', 'customer_id'],  timestamp_keys=['date'],  schema=customer_features_df.schema,  description='Customer time series features')

This enables point-in-time lookups when you use `create_training_set` or `score_batch`. The system performs an as-of timestamp join, using the `timestamp_lookup_key` you specify.

To keep the feature table up to date, set up a regularly scheduled job to write features, or stream new feature values into the feature table.

### Create a streaming feature computation pipeline to update features[​](#create-a-streaming-feature-computation-pipeline-to-update-features "Direct link to Create a streaming feature computation pipeline to update features")

To create a streaming feature computation pipeline, pass a streaming `DataFrame` as an argument to `write_table`. This method returns a `StreamingQuery` object.

Python

    def compute_additional_customer_features(data):  ''' Returns Streaming DataFrame  '''  pass  # not showncustomer_transactions = spark.readStream.load("dbfs:/events/customer_transactions")stream_df = compute_additional_customer_features(customer_transactions)fs.write_table(  df=stream_df,  name='recommender_system.customer_features',  mode='merge')

## Read from a feature table[​](#read-from-a-feature-table "Direct link to Read from a feature table")

Use `read_table` to read feature values.

Python

    fs = feature_store.FeatureStoreClient()customer_features_df = fs.read_table(  name='recommender.customer_features',)

## Search and browse feature tables[​](#search-and-browse-feature-tables "Direct link to Search and browse feature tables")

Use the Feature Store UI to search for or browse feature tables.

1.  In the sidebar, under **AI/ML**, click **Features** to display the Feature Store UI.
    
2.  In the search box, enter all or part of the name of a feature table, a feature, or a data source used for feature computation. You can also enter all or part of the [key or value of a tag](#work-with-feature-table-tags). Search text is case-insensitive.
    
    ![Feature search example](https://docs.databricks.com/aws/en/assets/images/feature-search-example-9b520100ccba30d2b3a935273adf8521.png)
    

The API to get feature table metadata depends on the Databricks runtime version you are using. With v0.3.6 and above, use `get_table`. With v0.3.5 and below, use `get_feature_table`.

Python

    # this example works with v0.3.6 and above# for v0.3.5, use `get_feature_table`from databricks.feature_store import FeatureStoreClientfs = FeatureStoreClient()fs.get_table("feature_store_example.user_feature_table")

Tags are key-value pairs that you can create and use to [search for feature tables](#search-and-browse-feature-tables). You can create, edit, and delete tags using the Feature Store UI or the [Feature Store Python API](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

### Work with feature table tags in the UI[​](#work-with-feature-table-tags-in-the-ui "Direct link to Work with feature table tags in the UI")

Use the Feature Store UI to search for or browse feature tables. To access the UI, in the sidebar, under **AI/ML**, click **Features**.

#### Add a tag using the Feature Store UI[​](#add-a-tag-using-the-feature-store-ui "Direct link to Add a tag using the Feature Store UI")

1.  Click ![Tag icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAAZCAYAAAB5CNMWAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAS6ADAAQAAAABAAAAGQAAAADG2PsQAAAEHUlEQVRYCe1XWShtbRh+HCc3IpJChnJhvEGGpAxFkQwZM9y5wQU3UhQZilyZpchQhDKXkAxX7ogypIxJIfOcsM5639qrvU/svdfy+x21v9prfcPzvt/6nu+dtpEgNhiaXgz80gtlADEDBrJkGIKBLANZMhiQAf0tA/spaHV1Nbq6urTqGBgYgJeXl1bMdy7+b2SFh4fDyclJOmt5eTl8fHwQExMjzdnb20v9f7Fj9F2lg6urKzIzM1FSUvIuL1TRGBkZvbtGk7rWVYL64lR4be93A3xTUxOqqqq0yX3J2vPzM+rr60FW6ObmhqSkJIyNjWnsdXx8jLKyMgQFBbFl1tbWYnh4GNHR0bi/v2fs09MTyO1DQkJYT0ZGBpaXlzX0KBl86Ibd3d04OjpCc3OzEr2KZOiC+vr6EBcXh/j4eMzNzaGwsBCWlpYIDg7G4+MjcnNzsb6+jsTERFhZWWFiYgIXFxdM1OvrK+9bWlrKJBOWZAcHB5GWlobZ2Vl8ytXJDf9ujY2NgouLC//EDxd2d3f/hnx6TPorKio09LS3twuiJUlzl5eX/A2VlZU8NzQ0xOORkREJc3p6KgQGBvL89fW18Pb2xv2CggIJc3JyIrS0tAgiydKcks67bqhuFpubm0hJSeFbUZ//in5WVhZiY2MhHg5bW1vY3t7mbcj1qG1sbPBbPSlYW1trJAmKcxQPx8fH0dHRgb29PRAmJycHHh4eLK/0oZMsUvzy8gLxxpTuobfc/Pw8xxlyOSKNYg01lXsRaeR6xsbGGjqJDPVWV1cHX19f1NTUIDIyEqGhoejt7VWHKOrrJMvR0RE9PT2IiIhQtIG+QldXV8jOzmYraG1txcLCApaWluDg4AATExNW4+7ujvPzcxBWva2trakP4ezszOQQ+UQYESy6PMc3DaDMgVayvL29MTMzA09PT5lq5cPJ7ailp6cjLCwMtra2HLQPDw8lZX5+ftynAH57e8sWR+42OTkpYW5ubjA1NYWDgwPY2dlxohBjIa+r3FgCy+x8mA1TU1P5NmTqUwwXAz7LUpVvamrKrt/Q0KChz9/fn7OhGKwxPT0trZGbkSVSIyssLi6GmZkZioqKYGNjg9HRUV4LCAjgt+KHkqzwX8i8lw3FMkAQrZmzGa23tbUJYjAX8vLypC0p24lJRxBLG6Gzs1PY398XxEAuZUMCrqyssBzpoB9ly/7+fkmH0s63VfAf3a54EI5L5ubmUqxSYXd2dtiiqNhUhQbCU112dnaGxcVFFZTfDw8PoELXwsJCY17p4J8jS9tB7u7uuDglTHJyMrsaFa5UpObn57OLapP/7NqPIosOS/8q6C/R6uoqB3mysKioKCQkJHyWC53yP44snSf6QoDW0uEL9/2Rqg1kybg2A1kGsmQwIAP6B1GoWkBNFigmAAAAAElFTkSuQmCC) if it is not already open. The tags table appears.
    
    ![tag table](https://docs.databricks.com/aws/en/assets/images/tags-open-2b92892f2d6833c4fac51ed029b0ae39.png)
    
2.  Click in the **Name** and **Value** fields and enter the key and value for your tag.
    
3.  Click **Add**.
    

#### Edit or delete a tag using the Feature Store UI[​](#edit-or-delete-a-tag-using-the-feature-store-ui "Direct link to Edit or delete a tag using the Feature Store UI")

To edit or delete an existing tag, use the icons in the **Actions** column.

![tag actions](https://docs.databricks.com/aws/en/assets/images/tag-edit-or-delete-2a374d59a14e35d810bf70d2e1369a79.png)

### Work with feature table tags using the Feature Store Python API[​](#work-with-feature-table-tags-using-the-feature-store-python-api "Direct link to work-with-feature-table-tags-using-the-feature-store-python-api")

On clusters running v0.4.1 and above, you can create, edit, and delete tags using the [Feature Store Python API](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

#### Requirements[​](#requirements "Direct link to Requirements")

Feature Store client v0.4.1 and above

#### Create feature table with tag using the Feature Store Python API[​](#create-feature-table-with-tag-using-the-feature-store-python-api "Direct link to Create feature table with tag using the Feature Store Python API")

Python

    from databricks.feature_store import FeatureStoreClientfs = FeatureStoreClient()customer_feature_table = fs.create_table(  ...  tags={"tag_key_1": "tag_value_1", "tag_key_2": "tag_value_2", ...},  ...)

#### Add, update, and delete tags using the Feature Store Python API[​](#add-update-and-delete-tags-using-the-feature-store-python-api "Direct link to Add, update, and delete tags using the Feature Store Python API")

Python

    from databricks.feature_store import FeatureStoreClientfs = FeatureStoreClient()# Upsert a tagfs.set_feature_table_tag(table_name="my_table", key="quality", value="gold")# Delete a tagfs.delete_feature_table_tag(table_name="my_table", key="quality")

## Update data sources for a feature table[​](#update-data-sources-for-a-feature-table "Direct link to update-data-sources-for-a-feature-table")

Feature store automatically tracks the data sources used to compute features. You can also manually update the data sources by using the [Feature Store Python API](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

### Requirements[​](#requirements-1 "Direct link to Requirements")

Feature Store client v0.5.0 and above

### Add data sources using the Feature Store Python API[​](#add-data-sources-using-the-feature-store-python-api "Direct link to Add data sources using the Feature Store Python API")

Below are some example commands. For details, see [the API documentation](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

Python

    from databricks.feature_store import FeatureStoreClientfs = FeatureStoreClient()# Use `source_type="table"` to add a table in the metastore as data source.fs.add_data_sources(feature_table_name="clicks", data_sources="user_info.clicks", source_type="table")# Use `source_type="path"` to add a data source in path format.fs.add_data_sources(feature_table_name="user_metrics", data_sources="dbfs:/FileStore/user_metrics.json", source_type="path")# Use `source_type="custom"` if the source is not a table or a path.fs.add_data_sources(feature_table_name="user_metrics", data_sources="user_metrics.txt", source_type="custom")

### Delete data sources using the Feature Store Python API[​](#delete-data-sources-using-the-feature-store-python-api "Direct link to Delete data sources using the Feature Store Python API")

For details, see [the API documentation](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

note

The following command deletes data sources of all types (“table”, “path”, and “custom”) that match the source names.

Python

    from databricks.feature_store import FeatureStoreClientfs = FeatureStoreClient()fs.delete_data_sources(feature_table_name="clicks", sources_names="user_info.clicks")

## Delete a feature table[​](#delete-a-feature-table "Direct link to Delete a feature table")

You can delete a feature table using the Feature Store UI or the [Feature Store Python API](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api).

note

*   Deleting a feature table can lead to unexpected failures in upstream producers and downstream consumers (models, endpoints, and scheduled jobs). You must delete published online stores with your cloud provider.
*   When you delete a feature table using the API, the underlying Delta table is also dropped. When you delete a feature table from the UI, you must drop the underlying Delta table separately.

### Delete a feature table using the UI[​](#delete-a-feature-table-using-the-ui "Direct link to Delete a feature table using the UI")

1.  On the feature table page, click ![Button Down](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAYCAYAAAD6S912AAAAAXNSR0IArs4c6QAAAKhJREFUOBHtlUsKAyEMQGPpRj2irr2Trj2JNxJRlw6RKVRocGiz6GICQdT4zIeoqLUOYJDWGuSc4cnAmgil1BwfXEDkSCmBFSiE4AWil6we3kDMwO9CFiXGCFrrj+qco2/G1qPUe49tuagxhrSfbUzBXuvv0B0Mz2x72Vo7w0spQQiBDvXcEdPNrdl1A7Io1xGr5Q1c8/HN7L9zOMbgfWB773y/XikFUA+Iv6YwxAsTlgAAAABJRU5ErkJggg==) at the right of the feature table name and select **Delete**. If you do not have CAN MANAGE permission for the feature table, you will not see this option.
    
    ![Select delete from drop-down menu](https://docs.databricks.com/aws/en/assets/images/feature-store-deletion-3dfd2bf01ad3eff459dddc0be1710f22.png)
    
2.  In the Delete Feature Table dialog, click **Delete** to confirm.
    
3.  If you also want to [drop the underlying Delta table](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-drop-table), run the following command in a notebook.
    
    SQL
    
        %sql DROP TABLE IF EXISTS <feature-table-name>;
    

### Delete a feature table using the Feature Store Python API[​](#delete-a-feature-table-using-the-feature-store-python-api "Direct link to Delete a feature table using the Feature Store Python API")

With Feature Store client v0.4.1 and above, you can use `drop_table` to delete a feature table. When you delete a table with `drop_table`, the underlying Delta table is also dropped.

Python

    fs.drop_table(  name='recommender_system.customer_features')
