---
title: Declarative features | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-apis
ingestedAt: "2026-06-18T08:10:11.424Z"
---

The Declarative Feature Engineering APIs enable you to define and compute features from data sources. Features can be defined using a variety of sources (Delta table and request-time data) and computations (time-windowed aggregations, simple column selections, and more). This guide covers the following workflows:

*   **Feature development** workflow
    *   Use `create_feature` to define Unity Catalog feature objects that can be used in model training and serving workflows.
    *   Alternatively, construct `Feature` objects locally and use `register_feature` to persist them to Unity Catalog later. Locally constructed features can be used with `create_training_set` before registration.
*   **Model training** workflow
    *   Use `create_training_set` to calculate point-in-time aggregated features for machine learning. For detailed documentation on training with declarative features, see [Train models with declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-with-declarative-features).
*   **Feature materialization and serving** workflow
    *   After defining a feature with `create_feature` or retrieving it using `get_feature`, you can use `materialize_features` to materialize the feature or set of features to an offline store for efficient reuse, or to an online store for online serving.
    *   Use `create_training_set` with the materialized view to prepare an offline batch training dataset.

For API details, see [Declarative features API reference](https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-api-reference).

## Requirements[​](#requirements "Direct link to Requirements")

*   A [classic compute](https://docs.databricks.com/aws/en/compute/use-compute) cluster running Databricks Runtime 17.0 ML or above.
    
*   You must install the custom Python package. Run the following lines of code each time you run a notebook:
    
    Python
    
        %pip install databricks-feature-engineering>=0.15.0dbutils.library.restartPython()
    

## Quickstart example[​](#-quickstart-example "Direct link to -quickstart-example")

For a runnable quickstart notebook, see [Example notebook](#example).

Python

    from databricks.feature_engineering import FeatureEngineeringClientfrom databricks.feature_engineering.entities import (    CronSchedule, DeltaTableSource, Feature, AggregationFunction,    MaterializedFeaturePipelineScheduleState,    Sum, Avg, ColumnSelection, TableTrigger,    TumblingWindow, SlidingWindow,    OfflineStoreConfig, OnlineStoreConfig,)from datetime import timedeltaCATALOG_NAME = "main"SCHEMA_NAME = "feature_store"TABLE_NAME = "transactions"# 1. Create data sourcesource = DeltaTableSource(    catalog_name=CATALOG_NAME,    schema_name=SCHEMA_NAME,    table_name=TABLE_NAME,)# 2. Define features locally (no catalog/schema needed yet)avg_feature = Feature(    source=source,    entity=["user_id"],    timeseries_column="transaction_time",    function=AggregationFunction(Avg(input="amount"), TumblingWindow(window_duration=timedelta(days=30))),    name="avg_transaction_30d",)sum_feature = Feature(    source=source,    entity=["user_id"],    timeseries_column="transaction_time",    function=AggregationFunction(Sum(input="amount"), SlidingWindow(window_duration=timedelta(days=7), slide_duration=timedelta(days=1))),    # name auto-generated: "amount_sum_sliding_7d_1d")fe = FeatureEngineeringClient()# 3. Explore features with compute_featuresfeature_df = fe.compute_features(features=[avg_feature, sum_feature])feature_df.display()# 4. Create training set using local features# `labeled_df` should have columns "user_id", "transaction_time", and "target".training_set = fe.create_training_set(    df=labeled_df,    features=[avg_feature, sum_feature],    label="target",)training_set.load_df().display()# 5. Register features in Unity Catalogavg_feature = fe.register_feature(    feature=avg_feature,    catalog_name=CATALOG_NAME,    schema_name=SCHEMA_NAME,)sum_feature = fe.register_feature(    feature=sum_feature,    catalog_name=CATALOG_NAME,    schema_name=SCHEMA_NAME,)# 6. Or use create_feature for a one-step define-and-register workflowlatest_amount = fe.create_feature(    source=source,    function=ColumnSelection("amount"),    entity=["user_id"],    timeseries_column="transaction_time",    catalog_name=CATALOG_NAME,    schema_name=SCHEMA_NAME,    name="latest_amount",)# 7. Train modelwith mlflow.start_run():    training_df = training_set.load_df()    # training code    fe.log_model(        model=model,        artifact_path="recommendation_model",        flavor=mlflow.sklearn,        training_set=training_set,        registered_model_name=f"{CATALOG_NAME}.{SCHEMA_NAME}.recommendation_model",    )# 8. (Optional) Materialize features for serving# Features must be registered in UC before calling materialize_featuresonline_config = OnlineStoreConfig(    catalog_name=CATALOG_NAME,    schema_name=SCHEMA_NAME,    table_name_prefix="customer_features_serving",    online_store_name="customer_features_store",)# Aggregation features use CronSchedule and support both offline and online configsfe.materialize_features(    features=[avg_feature, sum_feature],    offline_config=OfflineStoreConfig(        catalog_name=CATALOG_NAME,        schema_name=SCHEMA_NAME,        table_name_prefix="customer_features",    ),    online_config=online_config,    trigger=CronSchedule(        quartz_cron_expression="0 0 * * * ?",  # Hourly        timezone_id="UTC",        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,    ),)# ColumnSelection features use TableTrigger and only support online configfe.materialize_features(    features=[latest_amount],    online_config=online_config,    trigger=TableTrigger(),)

### Example notebook[​](#-example-notebook "Direct link to -example-notebook")

#### Declarative features quickstart notebook

## Model training and inference[​](#model-training-and-inference "Direct link to Model training and inference")

To train models and run batch inference with declarative features, including `log_model()`, `score_batch()`, and `create_training_set()`, see [Train models with declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-with-declarative-features).

## Feature materialization[​](#feature-materialization "Direct link to Feature materialization")

After you define features, you can materialize them to offline or online stores for efficient reuse in training and serving workflows. After materializing features, you can serve models using CPU model serving. For details, see [Materialize declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/materialized-features).

## Best practices[​](#best-practices "Direct link to Best practices")

### Feature naming[​](#feature-naming "Direct link to Feature naming")

*   Use descriptive names for business-critical features.
*   Follow consistent naming conventions across teams.
*   Use [auto-generated names](https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-api-reference#auto-generated-names) as you begin developing features.

### Time windows[​](#time-windows "Direct link to Time windows")

*   Align window boundaries with business cycles (daily, weekly).
*   Shorter windows capture recent trends but can be noisy. Longer windows produce more stable feature distributions but might miss recent behavioral shifts. Choose based on how quickly the underlying signal changes for your use case. For example, a 7-day window smooths out daily fluctuations and produces consistent model inputs, while a 1-hour window reacts quickly to behavioral changes but might introduce variance that degrades model performance. If your model's accuracy degrades when the distribution shifts, use a longer window to stabilize inputs.
*   Tumbling and sliding windows are more scalable than rolling (continuous) windows. Start with sliding windows for most use cases.

### Performance[​](#performance "Direct link to Performance")

*   Materialize features from the same data source in a single `materialize_features` call to minimize data scans.
*   Use the same granularity (for example, all 1-hour or all 1-day slide durations) for features on the same data source to enable better grouping during materialization.

### Entity columns vs. filter conditions[​](#entity-columns-vs-filter-conditions "Direct link to Entity columns vs. filter conditions")

Use this decision guide when working with features from the same source table:

**Use `entity` (on `create_feature`) when you need different aggregation levels:**

*   **Customer-level features** (one row per customer): `entity=["customer_id"]`
*   **Customer-merchant features** (multiple rows per customer): `entity=["customer_id", "merchant_id"]`
*   **Different aggregation levels can share the same `DeltaTableSource`**: specify different `entity` values on each feature definition

**Use `filter_condition` (on `DeltaTableSource`) when you need to filter rows at the same aggregation level:**

*   **High-value transactions only**: `filter_condition="amount > 100"` (still aggregated per customer)
*   **Completed orders only**: `filter_condition="status = 'completed'"` (still aggregated per customer)

**Rule of thumb:** If your change would result in a different number of rows per entity value, use different `entity` values on your feature definitions. If you're just filtering which rows contribute to the same aggregation, use `filter_condition` on the source.

## Common patterns[​](#common-patterns "Direct link to Common patterns")

### Customer analytics[​](#customer-analytics "Direct link to Customer analytics")

Python

    from databricks.feature_engineering.entities import AggregationFunction, Sum, Count, RollingWindowfe = FeatureEngineeringClient()features = [    # Recency: Number of transactions in the last day    fe.create_feature(catalog_name="main", schema_name="ecommerce", source=transactions,            entity=["user_id"], timeseries_column="transaction_time",            function=AggregationFunction(Count(input="transaction_id"), RollingWindow(window_duration=timedelta(days=1)))),    # Frequency: transaction count over the last 90 days    fe.create_feature(catalog_name="main", schema_name="ecommerce", source=transactions,            entity=["user_id"], timeseries_column="transaction_time",            function=AggregationFunction(Count(input="transaction_id"), RollingWindow(window_duration=timedelta(days=90)))),    # Monetary: total spend in the last month    fe.create_feature(catalog_name="main", schema_name="ecommerce", source=transactions,            entity=["user_id"], timeseries_column="transaction_time",            function=AggregationFunction(Sum(input="amount"), RollingWindow(window_duration=timedelta(days=30)))),]

### Trend analysis[​](#trend-analysis "Direct link to Trend analysis")

Python

    # Compare recent vs. historical behaviorfe = FeatureEngineeringClient()recent_avg = fe.create_feature(    catalog_name="main", schema_name="ecommerce",    source=transactions, entity=["user_id"], timeseries_column="transaction_time",    function=AggregationFunction(Avg(input="amount"), RollingWindow(window_duration=timedelta(days=7))),)historical_avg = fe.create_feature(    catalog_name="main", schema_name="ecommerce",    source=transactions, entity=["user_id"], timeseries_column="transaction_time",    function=AggregationFunction(Avg(input="amount"), RollingWindow(window_duration=timedelta(days=7), delay=timedelta(days=7))),)

### Seasonal patterns[​](#seasonal-patterns "Direct link to Seasonal patterns")

Python

    # Same day of week, 4 weeks agofe = FeatureEngineeringClient()weekly_pattern = fe.create_feature(    catalog_name="main", schema_name="ecommerce",    source=transactions, entity=["user_id"], timeseries_column="transaction_time",    function=AggregationFunction(Avg(input="amount"), RollingWindow(window_duration=timedelta(days=1), delay=timedelta(weeks=4))),)

## Limitations[​](#limitations "Direct link to Limitations")

*   Names of entity and timeseries columns must match between the training (labeled) dataset and the feature definitions when used in the `create_training_set` API.
*   The column name used as the `label` column in the training dataset should not exist in the source tables used for defining `Feature`s.
*   A limited list of functions (UDAFs) is supported in the `create_feature` API. See [Supported functions](https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-api-reference#supported-functions).
*   Entity columns cannot be of type `DATE` or `TIMESTAMP`.
*   `RequestSource` supports only scalar data types defined in `ScalarDataType` (`INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, `SHORT`). Complex types such as arrays, maps, and structs are not supported.
*   `RequestSource` does not support aggregation functions or time windows. Only `ColumnSelection` functions can be used.
*   The set of entity column names, timeseries column names, and request feature column names must be globally unique across all sources in a training set or serving endpoint.

For materialization-specific limitations, see [Limitations](https://docs.databricks.com/aws/en/machine-learning/feature-store/materialized-features#limitations).
