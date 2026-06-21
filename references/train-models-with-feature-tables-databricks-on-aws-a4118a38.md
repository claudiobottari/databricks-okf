---
title: Train models with feature tables | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/train-models-with-feature-store
ingestedAt: "2026-06-18T08:10:40.525Z"
---

To train a model using Databricks Feature Store or the legacy Workspace Feature Store, you first create a training dataset that defines the features to use and how to join them. When you then train the model, it retains references to those features.

When you train a model using Feature Engineering in Unity Catalog, you can view the model's lineage in Catalog Explorer. Tables and functions that were used to create the model are automatically tracked and displayed. See [Feature governance and lineage](https://docs.databricks.com/aws/en/machine-learning/feature-store/lineage).

When you use the model for inference, you can choose to have it retrieve feature values from the feature store. You can also serve the model with [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) and it will automatically lookup features [published to online stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store). Feature store models are also compatible with the [MLflow pyfunc interface](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html), so you can use MLflow to perform batch inference with feature tables.

If your model uses environment variables, learn more about how to use them when serving the model online at [Configure access to resources from model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving).

A model can use at most 50 tables and 100 functions for training.

## Create a training dataset[​](#create-a-training-dataset "Direct link to Create a training dataset")

To select specific features from a feature table for model training, you create a training dataset using the `FeatureEngineeringClient.create_training_set` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient.create_training_set` (for Workspace Feature Store) API and an object called a `FeatureLookup`. A `FeatureLookup` specifies each feature to use in the training set, including the name of the feature table, the name(s) of the features, and the key(s) to use when joining the feature table with the DataFrame passed to `create_training_set`. See [Feature Lookup](https://docs.databricks.com/aws/en/machine-learning/feature-store/concepts#feature-lookup) for more information.

Use the `feature_names` parameter when you create a `FeatureLookup`. `feature_names` takes a single feature name, a list of feature names, or None to look up all features (excluding primary keys) in the feature table at the time that the training set is created.

note

The type and order of `lookup_key` columns in the DataFrame must match the type and order of the primary keys (excluding timestamp keys) of the reference feature table.

Timestamp columns should not be used as a `lookup_key`.

important

`DATE` or `TIMESTAMP` columns used as primary keys must be declared as timeseries keys. If a feature table has a `DATE` or `TIMESTAMP` primary key column that is not designated as a timeseries key, calls to `create_feature_spec()`, `create_training_set()`, and `publish_table()` return an error.

To resolve this, use one of the following approaches:

*   **Declare the column as a timeseries column**: If the column represents event times or observation times and you want point-in-time lookup behavior, use the `timeseries_columns` parameter when creating the table. See [Point-in-time feature joins](https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series).
*   **Change the column type to `STRING`**: If the column is used as a plain lookup key for exact-match semantics (not time-based), alter the column type to `STRING` to avoid the restriction.

This article includes code examples for both versions of the syntax.

In this example, the DataFrame returned by `trainingSet.load_df` contains a column for each feature in `feature_lookups`. It preserves all columns of the DataFrame provided to `create_training_set` except those excluded using `exclude_columns`.

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup# The model training uses two features from the 'customer_features' feature table and# a single feature from 'product_features'feature_lookups = [    FeatureLookup(      table_name='ml.recommender_system.customer_features',      feature_names=['total_purchases_30d', 'total_purchases_7d'],      lookup_key='customer_id'    ),    FeatureLookup(      table_name='ml.recommender_system.product_features',      feature_names=['category'],      lookup_key='product_id'    )  ]fe = FeatureEngineeringClient()# Create a training set using training DataFrame and features from Feature Store# The training DataFrame must contain all lookup keys from the set of feature lookups,# in this case 'customer_id' and 'product_id'. It must also contain all labels used# for training, in this case 'rating'.training_set = fe.create_training_set(  df=training_df,  feature_lookups=feature_lookups,  label='rating',  exclude_columns=['customer_id', 'product_id'])training_df = training_set.load_df()

### Create a TrainingSet when lookup keys do not match the primary keys[​](#create-a-trainingset-when-lookup-keys-do-not-match-the-primary-keys "Direct link to Create a TrainingSet when lookup keys do not match the primary keys")

Use the argument `lookup_key` in the `FeatureLookup` for the column name in the training set. `create_training_set` performs an ordered join between the columns from the training set specified in the `lookup_key` argument using the order in which the primary keys were specified when the feature table was created.

In this example, `recommender_system.customer_features` has the following primary keys: `customer_id`, `dt`.

The `recommender_system.product_features` feature table has primary key `product_id`.

If the `training_df` has the following columns:

*   `cid`
*   `transaction_dt`
*   `product_id`
*   `rating`

the following code will create the correct feature lookups for the `TrainingSet`:

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    feature_lookups = [    FeatureLookup(      table_name='ml.recommender_system.customer_features',      feature_names=['total_purchases_30d', 'total_purchases_7d'],      lookup_key=['cid', 'transaction_dt']    ),    FeatureLookup(      table_name='ml.recommender_system.product_features',      feature_names=['category'],      lookup_key='product_id'    )  ]

When `create_training_set` is called, it creates a training dataset by performing a left join, joining the tables `recommender_system.customer_features` and `training_df` using the keys (`customer_id`,`dt`) corresponding to (`cid`,`transaction_dt`), as shown in the following code:

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    customer_features_df = spark.sql("SELECT * FROM ml.recommender_system.customer_features")product_features_df = spark.sql("SELECT * FROM ml.recommender_system.product_features")training_df.join(  customer_features_df,  on=[training_df.cid == customer_features_df.customer_id,      training_df.transaction_dt == customer_features_df.dt],  how="left").join(  product_features_df,  on="product_id",  how="left")

### Create a TrainingSet containing two features with the same name from different feature tables[​](#create-a-trainingset-containing-two-features-with-the-same-name-from-different-feature-tables "Direct link to Create a TrainingSet containing two features with the same name from different feature tables")

Use the optional argument `output_name` in the `FeatureLookup`. The name provided is used in place of the feature name in the DataFrame returned by `TrainingSet.load_df`. For example, with the following code, the DataFrame returned by `training_set.load_df` includes columns `customer_height` and `product_height`.

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    feature_lookups = [    FeatureLookup(      table_name='ml.recommender_system.customer_features',      feature_names=['height'],      lookup_key='customer_id',      output_name='customer_height',    ),    FeatureLookup(      table_name='ml.recommender_system.product_features',      feature_names=['height'],      lookup_key='product_id',      output_name='product_height'    ),  ]fe = FeatureEngineeringClient()with mlflow.start_run():  training_set = fe.create_training_set(    df=df,    feature_lookups=feature_lookups,    label='rating',    exclude_columns=['customer_id']  )  training_df = training_set.load_df()

### Create a TrainingSet using the same feature multiple times[​](#create-a-trainingset-using-the-same-feature-multiple-times "Direct link to Create a TrainingSet using the same feature multiple times")

To create a TrainingSet using the same feature joined by different lookup keys, use multiple FeatureLookups. Use a unique `output_name` for each FeatureLookup output.

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    feature_lookups = [    FeatureLookup(      table_name='ml.taxi_data.zip_features',      feature_names=['temperature'],      lookup_key=['pickup_zip'],      output_name='pickup_temp'    ),    FeatureLookup(      table_name='ml.taxi_data.zip_features',      feature_names=['temperature'],      lookup_key=['dropoff_zip'],      output_name='dropoff_temp'    )  ]

### Create a TrainingSet for unsupervised machine learning models[​](#create-a-trainingset-for-unsupervised-machine-learning-models "Direct link to Create a TrainingSet for unsupervised machine learning models")

Set `label=None` when creating a TrainingSet for unsupervised learning models. For example, the following TrainingSet can be used to cluster different customers into groups based on their interests:

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    feature_lookups = [    FeatureLookup(      table_name='ml.recommender_system.customer_features',      feature_names=['interests'],      lookup_key='customer_id',    ),  ]fe = FeatureEngineeringClient()with mlflow.start_run():  training_set = fe.create_training_set(    df=df,    feature_lookups=feature_lookups,    label=None,    exclude_columns=['customer_id']  )  training_df = training_set.load_df()

### Create a TrainingSet when using a view as a feature table[​](#create-a-trainingset-when-using-a-view-as-a-feature-table "Direct link to Create a TrainingSet when using a view as a feature table")

To use a view as a feature table, you must use `databricks-feature-engineering` version 0.7.0 or above, which is built into Databricks Runtime 16.0 ML.

The view must be a simple SELECT view from the source Delta table. A simple SELECT view is defined as a view created from a single Delta table in Unity Catalog that can be used as a feature table, and whose primary keys are selected without JOIN, GROUP BY, or DISTINCT clauses. Acceptable keywords in the SQL statement are SELECT, FROM, WHERE, ORDER BY, LIMIT, and OFFSET.

In the following example, `ml.recommender_system.customer_table` has primary keys `cid` and `dt`, where `dt` is a time series column. The example assumes that the dataframe `training_df` has columns `cid`, `dt`, and `label`:

Python

    from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookupcustomer_features_df = spark.sql("CREATE OR REPLACE VIEW ml.recommender_system.customer_features AS SELECT cid, dt, pid, rating FROM ml.recommender_system.customer_table WHERE rating > 3")feature_lookups = [    FeatureLookup(      table_name='ml.recommender_system.customer_features',      feature_names=['pid', 'rating'],      lookup_key=['cid'],      timestamp_lookup_key='dt'    ),]fe = FeatureEngineeringClient()training_set = fe.create_training_set(  df=training_df,  feature_lookups=feature_lookups,  label='label')training_df = training_set.load_df()

### Create a training set with default values[​](#create-a-training-set-with-default-values "Direct link to Create a training set with default values")

When creating a training dataset, you can specify default values for features to handle cases where the Feature Store does not have a computed feature value for an ID.

To specify default values, use the `default_values` parameter in the `FeatureLookup`.

The following example demonstrates how to specify default values for a set of features:

Python

    feature_lookups = [    FeatureLookup(        table_name="ml.recommender_system.customer_features",        feature_names=[            "membership_tier",            "age",            "page_views_count_30days",        ],        lookup_key="customer_id",        default_values={          "age": 18,          "membership_tier": "bronze"        },    ),]

If the feature columns are renamed using the `rename_outputs` parameter, `default_values` must use the renamed feature names.

Python

    FeatureLookup(  table_name = 'main.default.table',  feature_names = ['materialized_feature_value'],  lookup_key = 'id',  rename_outputs={"materialized_feature_value": "feature_value"},  default_values={    "feature_value": 0  })

## Train models and perform batch inference with feature tables[​](#train-models-and-perform-batch-inference-with-feature-tables "Direct link to train-models-and-perform-batch-inference-with-feature-tables")

When you train a model using features from Feature Store, the model retains references to the features. When you use the model for inference, you can choose to have it retrieve feature values from Feature Store. You must provide the primary key(s) of the features used in the model. The model retrieves the features it requires from Feature Store in your workspace. It then joins the feature values as needed during scoring.

To support feature lookup at inference time:

*   You must log the model using the `log_model` method of `FeatureEngineeringClient` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient` (for Workspace Feature Store).
*   You must use the DataFrame returned by `TrainingSet.load_df` to train the model. If you modify this DataFrame in any way before using it to train the model, the modifications are not applied when you use the model for inference. This decreases the performance of the model.
*   The model type must have a corresponding `python_flavor` in MLflow. MLflow supports most Python model training frameworks, including:
    *   scikit-learn
    *   keras
    *   PyTorch
    *   SparkML
    *   LightGBM
    *   XGBoost
    *   TensorFlow Keras (using the `python_flavor` `mlflow.keras`)
*   Custom MLflow pyfunc models

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    # Train modelimport mlflowfrom sklearn import linear_modelfeature_lookups = [    FeatureLookup(      table_name='ml.recommender_system.customer_features',      feature_names=['total_purchases_30d'],      lookup_key='customer_id',    ),    FeatureLookup(      table_name='ml.recommender_system.product_features',      feature_names=['category'],      lookup_key='product_id'    )  ]fe = FeatureEngineeringClient()with mlflow.start_run():  # df has columns ['customer_id', 'product_id', 'rating']  training_set = fe.create_training_set(    df=df,    feature_lookups=feature_lookups,    label='rating',    exclude_columns=['customer_id', 'product_id']  )  training_df = training_set.load_df().toPandas()  # "training_df" columns ['total_purchases_30d', 'category', 'rating']  X_train = training_df.drop(['rating'], axis=1)  y_train = training_df.rating  model = linear_model.LinearRegression().fit(X_train, y_train)  fe.log_model(    model=model,    artifact_path="recommendation_model",    flavor=mlflow.sklearn,    training_set=training_set,    registered_model_name="recommendation_model"  )# Batch inference# If the model at model_uri is packaged with the features, the FeatureStoreClient.score_batch()# call automatically retrieves the required features from Feature Store before scoring the model.# The DataFrame returned by score_batch() augments batch_df with# columns containing the feature values and a column containing model predictions.fe = FeatureEngineeringClient()# batch_df has columns 'customer_id' and 'product_id'predictions = fe.score_batch(    model_uri=model_uri,    df=batch_df)# The 'predictions' DataFrame has these columns:# 'customer_id', 'product_id', 'total_purchases_30d', 'category', 'prediction'

### Use custom feature values when scoring a model packaged with feature metadata[​](#use-custom-feature-values-when-scoring-a-model-packaged-with-feature-metadata "Direct link to Use custom feature values when scoring a model packaged with feature metadata")

By default, a model packaged with feature metadata looks up features from feature tables at inference. To use custom feature values for scoring, include them in the DataFrame passed to `FeatureEngineeringClient.score_batch` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient.score_batch` (for Workspace Feature Store).

For example, suppose you package a model with these two features:

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    feature_lookups = [    FeatureLookup(      table_name='ml.recommender_system.customer_features',      feature_names=['account_creation_date', 'num_lifetime_purchases'],      lookup_key='customer_id',    ),  ]

At inference, you can provide custom values for the feature `account_creation_date` by calling `score_batch` on a DataFrame that includes a column named `account_creation_date`. In this case the API looks up only the `num_lifetime_purchases` feature from Feature Store and uses the provided custom `account_creation_date` column values for model scoring.

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    # batch_df has columns ['customer_id', 'account_creation_date']predictions = fe.score_batch(  model_uri='models:/ban_prediction_model/1',  df=batch_df)

### Train and score a model using a combination of Feature Store features and data residing outside Feature Store[​](#train-and-score-a-model-using-a-combination-of-feature-store-features-and-data-residing-outside-feature-store "Direct link to Train and score a model using a combination of Feature Store features and data residing outside Feature Store")

You can train a model using a combination of Feature Store features and data from outside Feature Store. When you package the model with feature metadata, the model retrieves feature values from Feature Store for inference.

To train a model, include the extra data as columns in the DataFrame passed to `FeatureEngineeringClient.create_training_set` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient.create_training_set` (for Workspace Feature Store). This example uses the feature `total_purchases_30d` from Feature Store and the external column `browser`.

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    feature_lookups = [    FeatureLookup(      table_name='ml.recommender_system.customer_features',      feature_names=['total_purchases_30d'],      lookup_key='customer_id',    ),  ]fe = FeatureEngineeringClient()# df has columns ['customer_id', 'browser', 'rating']training_set = fe.create_training_set(  df=df,  feature_lookups=feature_lookups,  label='rating',  exclude_columns=['customer_id']  # 'browser' is not excluded)

At inference, the DataFrame used in `FeatureStoreClient.score_batch` must include the `browser` column.

*   Feature Engineering in Unity Catalog
*   Workspace Feature Store

Python

    # At inference, 'browser' must be provided# batch_df has columns ['customer_id', 'browser']predictions = fe.score_batch(  model_uri=model_uri,  df=batch_df)

### Load models and perform batch inference using MLflow[​](#load-models-and-perform-batch-inference-using-mlflow "Direct link to Load models and perform batch inference using MLflow")

After a model has been logged using the `log_model` method of `FeatureEngineeringClient` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient` (for Workspace Feature Store), MLflow can be used at inference. `mlflow.pyfunc.predict` retrieves feature values from Feature Store and also joins any values provided at inference time. You must provide the primary key(s) of the features used in the model.

note

Batch inference with MLflow requires MLflow version 2.11 and above. Models that use [time series feature tables](https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series) are not supported. To do batch inference with time series feature tables, use `score_batch`. See [Train models and perform batch inference with feature tables](#batch-inference).

Python

    # Train modelimport mlflowfrom sklearn import linear_modelfeature_lookups = [  FeatureLookup(    table_name='ml.recommender_system.customer_features',    feature_names=['total_purchases_30d'],    lookup_key='customer_id',  ),  FeatureLookup(    table_name='ml.recommender_system.product_features',    feature_names=['category'],    lookup_key='product_id'  )]fe = FeatureEngineeringClient()with mlflow.start_run():  # df has columns ['customer_id', 'product_id', 'rating']  training_set = fe.create_training_set(    df=df,    feature_lookups=feature_lookups,    label='rating',    exclude_columns=['customer_id', 'product_id']  )  training_df = training_set.load_df().toPandas()  # "training_df" columns ['total_purchases_30d', 'category', 'rating']  X_train = training_df.drop(['rating'], axis=1)  y_train = training_df.rating  model = linear_model.LinearRegression().fit(X_train, y_train)  fe.log_model(    model=model,    artifact_path="recommendation_model",    flavor=mlflow.sklearn,    training_set=training_set,    registered_model_name="recommendation_model",    #refers to the default value of "result_type" if not provided at inference    params={"result_type":"double"},  )# Batch inference with MLflow# NOTE: the result_type parameter can only be used if a default value# is provided in log_model. This is automatically done for all models# logged using Databricks Runtime for ML 15.0 or above.# For earlier Databricks Runtime versions, use set_result as shown below.# batch_df has columns 'customer_id' and 'product_id'model = mlflow.pyfunc.load_model(model_version_uri)# If result_type parameter is provided in log_modelpredictions = model.predict(df, {"result_type":"double"})# If result_type parameter is NOT provided in log_modelmodel._model_impl.set_result_type("double")predictions = model.predict(df)

### Handle missing feature values[​](#handle-missing-feature-values "Direct link to Handle missing feature values")

When a non-existent lookup key is passed to the model for prediction, the feature value fetched by `FeatureLookup` can be either `None` or `NaN`, depending on the environment. Your model implementation should be able to handle both values.

*   For offline applications using `fe.score_batch`, the returned value for a missing feature is `NaN`.
*   For online applications using [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/), the returned value might be either `None` or `NaN`:
    *   If none of the provided lookup keys exist, the value is `None`.
    *   If only a subset of the lookup keys do not exist, the value is `NaN`.

To handle missing feature values when using on-demand features, see [How to handle missing feature values](https://docs.databricks.com/aws/en/machine-learning/feature-store/on-demand-features#how-to-handle-missing-feature-values).

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**Error message: `Could not find lookup key columns ... required by FeatureLookups.`**

or

**Error message: `Unable to join feature table '...' because timestamp lookup key '...' not found in DataFrame.`**

The `create_training_set` call failed because a primary key or timestamp key is missing in the training DataFrame. The training DataFrame must contain all lookup keys and timestamp lookup keys from the set of feature lookups.

## Example notebooks[​](#example-notebooks "Direct link to Example notebooks")

The basic notebook shows how to create a feature table, use it to train a model, and run batch scoring using automatic feature lookup. It also shows the Feature Engineering UI, which you can use to search for features and understand how features are created and used.

#### Basic Feature Engineering in Unity Catalog example notebook

The taxi example notebook illustrates the process of creating features, updating them, and using them for model training and batch inference.

#### Feature Engineering in Unity Catalog taxi example notebook
