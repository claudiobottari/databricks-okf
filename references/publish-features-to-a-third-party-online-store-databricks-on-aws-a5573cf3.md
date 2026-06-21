---
title: Publish features to a third-party online store | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/publish-features
ingestedAt: "2026-06-18T08:10:29.989Z"
---

Publish feature tables to a third-party online store to make features available for low-latency, real-time serving. You can publish batch or streaming features, a selected subset of features, or to a specific database.

Databricks Feature Store supports these online stores:

note

The DynamoDB online store uses a different schema than the offline store. Specifically, in the online store, primary keys are stored as a combined key in the column `_feature_store_internal__primary_keys`.

To ensure that Feature Store can access the DynamoDB online store, you must create the table in the online store by using `publish_table()`. Do not manually create a table inside DynamoDB. `publish_table()` does that for you automatically.

## Publish batch-computed features to an online store[​](#publish-batch-computed-features-to-an-online-store "Direct link to Publish batch-computed features to an online store")

You can create and schedule a Databricks job to regularly publish updated features. This job can also include the code to calculate the updated features, or you can create and run separate jobs to calculate and publish feature updates.

For SQL stores, the following code assumes that an online database named “recommender\_system” already exists in the online store and matches the name of the offline store. If there is no table named “customer\_features” in the database, this code creates one. It also assumes that features are computed each day and stored as a partitioned column `_dt`.

The following code assumes that you have [created secrets](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication#provide-online-store-credentials-using-databricks-secrets) to access this online store.

If you are using DynamoDB, Databricks recommends that you provide authentication with write permission through [an instance profile attached to a Databricks cluster](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication#auth-instance-profile).

*   DynamoDB
*   SQL stores

DynamoDB support is available in all versions of Feature Engineering in Unity Catalog client, and Feature Store client v0.3.8 and above.

Python

    import datetimefrom databricks.feature_engineering.online_store_spec import AmazonDynamoDBSpec# or databricks.feature_store.online_store_spec for Workspace Feature Store# do not pass `write_secret_prefix` if you intend to use the instance profile attached to the cluster.online_store = AmazonDynamoDBSpec(  region='<region>',  read_secret_prefix='<read-scope>/<prefix>',  write_secret_prefix='<write-scope>/<prefix>')fe.publish_table( # or fs.publish_table for Workspace Feature Store  name='ml.recommender_system.customer_features',  online_store=online_store,  filter_condition=f"_dt = '{str(datetime.date.today())}'",  mode='merge')

## Publish streaming features to an online store[​](#publish-streaming-features-to-an-online-store "Direct link to Publish streaming features to an online store")

To continuously stream features to the online store, set `streaming=True`.

Python

    fe.publish_table( # or fs.publish_table for Workspace Feature Store  name='ml.recommender_system.customer_features',  online_store=online_store,  streaming=True)

## Publish selected features to an online store[​](#publish-selected-features-to-an-online-store "Direct link to Publish selected features to an online store")

To publish only selected features to the online store, use the `features` argument to specify the feature name(s) to publish. Primary keys and timestamp keys are always published. If you do not specify the `features` argument or if the value is None, all features from the offline feature table are published.

note

The entire offline table must be a valid feature table even if you are publishing only a subset of features to an online store. If the offline table contains unsupported [data types](https://docs.databricks.com/aws/en/machine-learning/feature-store/#supported-data-types), you cannot publish a subset of features from that table to an online store.

Python

    fe.publish_table( # or fs.publish_table for Workspace Feature Store  name='ml.recommender_system.customer_features',  online_store=online_store,  features=["total_purchases_30d"])

## Publish a feature table to a specific database[​](#publish-a-feature-table-to-a-specific-database "Direct link to Publish a feature table to a specific database")

In the [online store spec](https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api), specify the database name (`database_name`) and the table name (`table_name`). If you do not specify these parameters, the offline database name and feature table name are used. `database_name` must already exist in the online store.

Python

    online_store = AmazonRdsMySqlSpec(  hostname='<hostname>',  port='<port>',  database_name='<database-name>',  table_name='<table-name>',  read_secret_prefix='<read-scope>/<prefix>',  write_secret_prefix='<write-scope>/<prefix>')

## Overwrite an existing online feature table or specific rows[​](#overwrite-an-existing-online-feature-table-or-specific-rows "Direct link to Overwrite an existing online feature table or specific rows")

Use `mode='overwrite'` in the `publish_table` call. The online table is completely overwritten by the data in the offline table.

note

Amazon DynamoDB does not support overwrite mode.

Python

    fs.publish_table(  name='recommender_system.customer_features',  online_store=online_store,  mode='overwrite')

To overwrite only certain rows, use the `filter_condition` argument:

Python

    fs.publish_table(  name='recommender_system.customer_features',  online_store=online_store,  filter_condition=f"_dt = '{str(datetime.date.today())}'",  mode='merge')

## Delete a published table from an online store[​](#delete-a-published-table-from-an-online-store "Direct link to Delete a published table from an online store")

With Feature Store client v0.12.0 and above, you can use `drop_online_table` to delete a published table from an online store. When you delete a published table with `drop_online_table`, the table is deleted from your online store provider and the online store metadata is removed from Databricks.

Python

    fe.drop_online_table( # or fs.drop_online_table for Workspace Feature Store  name='recommender_system.customer_features',  online_store = online_store)

note

*   `drop_online_table` deletes the published table from the online store. It does not delete the feature table in Databricks.
*   Before you delete a published table, you should ensure that the table is not used for Model Serving feature lookup and has no other downstream dependencies. The delete is irreversible and might cause dependencies to fail.
*   To check for any dependencies, consider rotating the keys for the published table you plan to delete for a day before you execute `drop_online_table`.
