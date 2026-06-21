---
title: Materialize declarative features | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/materialized-features
ingestedAt: "2026-06-18T08:10:21.237Z"
---

After you have created your declarative feature definitions, which are stored in Unity Catalog, you can produce feature data from your source table using the feature definitions. This process is called materializing your features. Databricks creates and manages Lakeflow Spark Declarative Pipelines to populate tables in Unity Catalog for model training and batch scoring or online serving.

For information about serving declarative features, see [Serve declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/serve-declarative-features).

## Requirements[​](#requirements "Direct link to Requirements")

*   Features must be created with the declarative feature API and stored in Unity Catalog.
*   For version requirements, see [Requirements](https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-apis#requirements).
*   `ColumnSelection` features can be materialized to online stores. See [ColumnSelection materialization](#columnselection-materialization).
*   `RequestSource` features cannot be materialized because they represent data provided at inference time.

## API data structures[​](#api-data-structures "Direct link to API data structures")

### `OfflineStoreConfig`[​](#offlinestoreconfig "Direct link to offlinestoreconfig")

Configuration for the offline store where materialized features will be written. When `materialize_features` is called, the feature store backend creates tables using this prefix. Each pipeline run materializes the latest feature values to the table according to materialization schedule.

Python

    OfflineStoreConfig(    catalog_name: str,        # Catalog name for the offline table where materialized features will be stored    schema_name: str,         # Schema name for the offline table    table_name_prefix: str    # Table name prefix for the offline table. The pipeline may create multiple tables with this prefix, each updated at different cadences)

Python

    from databricks.feature_engineering.entities import OfflineStoreConfigoffline_store = OfflineStoreConfig(    catalog_name="main",    schema_name="feature_store",    table_name_prefix="customer_features")

### `OnlineStoreConfig`[​](#onlinestoreconfig "Direct link to onlinestoreconfig")

Configuration for the online store, which stores features used by model serving. Materialization creates Delta tables with the `catalog.schema.table_name_prefix`, and streams the tables to the Online Feature Store with the same name.

Python

    from databricks.feature_engineering.entities import OnlineStoreConfigonline_store = OnlineStoreConfig(    catalog_name="main",    schema_name="feature_store",    table_name_prefix="customer_features_serving",    online_store_name="customer_features_store")

### `MaterializedFeature`[​](#materializedfeature "Direct link to materializedfeature")

Represents a declarative feature that has been materialized, that is, that has a precomputed representation available in Unity Catalog. There is a distinct materialized feature for the offline table and online table. Typically, users will not instantiate a `MaterializedFeature` directly.

### API function calls[​](#api-function-calls "Direct link to API function calls")

### `materialize_features()`[​](#materialize_features "Direct link to materialize_features")

Materializes a list of declarative features into either an offline Delta table or to an Online Feature Store. Features must be registered in Unity Catalog before calling this function (for example, using `create_feature` or `register_feature`). Locally constructed features that have not been registered will not work.

Python

    FeatureEngineeringClient.materialize_features(    features: List[Feature],                                               # List of declarative features to materialize    offline_config: Optional[OfflineStoreConfig] = None,                   # Offline store config (aggregation features only)    online_config: Optional[OnlineStoreConfig] = None,                     # Online store config    trigger: Union[CronSchedule, TableTrigger],                            # Materialization trigger) -> List[MaterializedFeature]:

The method returns a list of materialized features, which contain metadata about when feature values are updated and the Unity Catalog tables where features are materialized.

If both an `OnlineStoreConfig` and an `OfflineStoreConfig` are provided, then two materialized features are returned per feature provided, one for each type of store.

The `trigger` parameter controls when the materialization pipeline runs:

*   **`CronSchedule`**: Runs on a fixed schedule. Required for aggregation features (`AggregationFunction`).
*   **`TableTrigger`**: Runs when the upstream Delta table receives a commit. Required for `ColumnSelection` features backed by a `DeltaTableSource`.

You cannot mix `ColumnSelection` and aggregation features in a single `materialize_features` call because they require different trigger types. Issue separate calls instead.

#### Materialize to offline store[​](#materialize-to-offline-store "Direct link to Materialize to offline store")

Python

    from databricks.feature_engineering import FeatureEngineeringClientfrom databricks.feature_engineering.entities import (    CronSchedule, MaterializedFeaturePipelineScheduleState, OfflineStoreConfig,)fe = FeatureEngineeringClient()materialized = fe.materialize_features(    features=features,    offline_config=OfflineStoreConfig(        catalog_name="main",        schema_name="feature_store",        table_name_prefix="customer_features"    ),    trigger=CronSchedule(        quartz_cron_expression="0 0 * * * ?",  # Hourly        timezone_id="UTC",        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,    ),)

#### Materialize to online store[​](#materialize-to-online-store "Direct link to Materialize to online store")

note

To materialize aggregation features to an online store, you must also materialize to an offline store. Both `offline_config` and `online_config` are required. The `online_store_name` must reference an existing Online Feature Store. For instructions on creating one, see [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store).

`ColumnSelection` features do not require an `OfflineStoreConfig`. See [ColumnSelection materialization](#columnselection-materialization).

Python

    from databricks.feature_engineering import FeatureEngineeringClientfrom databricks.feature_engineering.entities import (    CronSchedule, MaterializedFeaturePipelineScheduleState,    OfflineStoreConfig, OnlineStoreConfig,)fe = FeatureEngineeringClient()materialized = fe.materialize_features(    features=features,    offline_config=OfflineStoreConfig(        catalog_name="main",        schema_name="feature_store",        table_name_prefix="customer_features"    ),    online_config=OnlineStoreConfig(        catalog_name="main",        schema_name="feature_store",        table_name_prefix="customer_features_serving",        online_store_name="customer_features_store"    ),    trigger=CronSchedule(        quartz_cron_expression="0 0 * * * ?",  # Hourly        timezone_id="UTC",        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,    ),)

### `list_materialized_features()`[​](#list_materialized_features "Direct link to list_materialized_features")

Returns a list of all materialized features in the user's Unity Catalog metastore.

By default, a maximum of 100 features are returned. You can change this limit using the `max_results` parameter.

To filter the returned materialized features by a feature name, use the optional `feature_name` parameter.

Python

    FeatureEngineeringClient.list_materialized_features(    feature_name: Optional[str] = None,     # Optional feature name to filter by    max_results: int = 100,                 # Maximum number of features to be returned) -> List[MaterializedFeature]:

### `delete_materialized_feature()`[​](#-delete_materialized_feature "Direct link to -delete_materialized_feature")

Before deleting a materialized feature, remove or update any models or feature specs that reference the feature.

Deletes a materialized feature. The feature to pass depends on the feature type:

*   **Aggregation features**: Pass the offline materialized feature. If there is an online materialized feature for the same feature, both are deleted.
*   **`ColumnSelection` features**: Pass the online materialized feature. `ColumnSelection` features are materialized only to the online store (see [ColumnSelection materialization](#columnselection-materialization)), so there is no paired offline feature.

As part of materialization, features are grouped together by data source and aggregation window for efficiency. `ColumnSelection` features have no aggregation window, so they are grouped only by data source. The materialization pipeline, offline table, and online table are not deleted until all grouped features have been deleted. When the last materialized feature in a group is deleted, the feature store schedules the associated resources for automatic cleanup by a background process. See [Background resource cleanup](#background-resource-cleanup).

To clean up materialized features, look at the table associated with a materialized feature. Each feature in the table (one per column) must be deleted before compute and Delta table resources are cleaned up.

Use `list_materialized_features()` to get the `materialized_feature` argument.

Python

    FeatureEngineeringClient.delete_materialized_feature(    materialized_feature: MaterializedFeature,  # Required: The materialized feature to delete) -> None

Python

    from databricks.feature_engineering import FeatureEngineeringClientfrom databricks.feature_engineering.entities import ColumnSelectionfe = FeatureEngineeringClient()feature_names = [    "main.feature_store.amount_sum_sliding_7d_1d",    "main.feature_store.amount_sum_sliding_30d_1d",    "main.feature_store.transaction_count_sliding_7d_1d",    "main.feature_store.latest_transaction_amount",    "main.feature_store.latest_user_tier",]for name in feature_names:    feature = fe.get_feature(full_name=name)    for mf in fe.list_materialized_features(feature_name=name):        if isinstance(feature.function, ColumnSelection):            # ColumnSelection features only have online materializations. Delete the online materialized feature directly.            fe.delete_materialized_feature(materialized_feature=mf)        elif not mf.is_online:            # Aggregation features have both offline and online materializations. Delete the offline materialized feature to delete both.            fe.delete_materialized_feature(materialized_feature=mf)        # Online materialized aggregation features cannot be deleted directly. They are deleted via their paired offline materialized features.

## ColumnSelection materialization[​](#-columnselection-materialization "Direct link to -columnselection-materialization")

`ColumnSelection` features select the latest value of a single column per entity key without aggregation. They can only be materialized to online stores. For offline use cases (training and batch inference), `ColumnSelection` features are fetched directly from the source data at query time, so offline materialization is not needed.

### Materialization behavior[​](#materialization-behavior "Direct link to Materialization behavior")

*   The pipeline writes the most recent row per entity key to the online table, with no aggregation window.
*   Online materialization populates the online table with the current latest value per entity key.

### Example[​](#example "Direct link to Example")

Python

    from databricks.feature_engineering import FeatureEngineeringClientfrom databricks.feature_engineering.entities import (    DeltaTableSource, Feature, ColumnSelection, TableTrigger, OnlineStoreConfig,)fe = FeatureEngineeringClient()delta_source = DeltaTableSource(    catalog_name="catalog",    schema_name="schema",    table_name="transactions",)amount_feature = Feature(    source=delta_source,    function=ColumnSelection("amount"),    entity=["user_id"],    timeseries_column="transaction_time",    name="latest_transaction_amount",)# Register before materializingamount_feature = fe.register_feature(    feature=amount_feature,    catalog_name="catalog",    schema_name="schema",)mfs = fe.materialize_features(    features=[amount_feature],    online_config=OnlineStoreConfig(        catalog_name="catalog",        schema_name="feats_online",        table_name_prefix="txn_",        online_store_name="lb_usw2"    ),    trigger=TableTrigger(),)

`ColumnSelection` features use `TableTrigger`, which runs the pipeline whenever the source Delta table receives a new commit. No `offline_config` is needed because `ColumnSelection` features are read directly from the source for offline use cases (training and batch inference).

note

`RequestSource` features cannot be materialized because they represent data provided by the caller at inference time (or extracted from the labeled DataFrame at training time). There is no source table to read from. The values exist only in the request payload or training DataFrame.

## Background resource cleanup[​](#background-resource-cleanup "Direct link to Background resource cleanup")

When you delete a materialized feature, Databricks removes the feature metadata immediately. The associated infrastructure (tables, pipelines, and jobs) is cleaned up asynchronously by a background process.

Because multiple materialized features can share the same tables and pipelines, these shared resources are not removed until every materialized feature that references them has been deleted. When the last materialized feature sharing a set of tables is deleted, the background process automatically deletes the following resources:

*   The offline Delta tables containing the materialized feature data
*   The online tables, if the features were materialized to an online store
*   The materialization pipeline
*   The orchestration job

This background process uses a Databricks-managed system service principal to perform these cleanup actions on your behalf, including deleting tables, pipelines, and jobs in your workspace. No action is required from you. The cleanup is fully managed by the feature store.

note

There might be a short delay between deleting the last materialized feature in a group and the removal of the associated tables and other resources.

## Limitations[​](#limitations "Direct link to Limitations")

*   Batch rolling window features cannot be materialized. Due to their high fidelity of time correctness, rolling window features for offline training or batch inference are generated on the fly for each data point.
*   `ColumnSelection` features can only be materialized to online stores.
*   `RequestSource` features cannot be materialized.
*   Materialized features can only be deleted in the workspace in which they were created.
*   For materialized aggregation features, the online materialized feature cannot be deleted directly. Delete the paired offline materialized feature, and the change propagates to both.
*   For materialized aggregation features created before April 20, 2026, the materialization pipeline continues producing new feature values until all materialized features in the pipeline have been deleted, which triggers resource cleanup. To create an updated pipeline that supports per-feature delete, delete and re-materialize the feature.
*   For materialized `ColumnSelection` features, the materialization pipeline continues producing new feature values until all materialized features in the pipeline have been deleted, which triggers resource cleanup.
