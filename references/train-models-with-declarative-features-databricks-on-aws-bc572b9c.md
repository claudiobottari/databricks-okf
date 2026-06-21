---
title: Train models with declarative features | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/train-with-declarative-features
ingestedAt: "2026-06-18T08:10:42.187Z"
---

Declarative features let you train models with point-in-time correct feature computation and automatic feature lookup at inference. For information about defining declarative features, see [Declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-apis).

## Requirements[​](#requirements "Direct link to Requirements")

*   Features must be created with the declarative feature API. See [Declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-apis).

## API methods[​](#api-methods "Direct link to API methods")

### `create_training_set()`[​](#create_training_set "Direct link to create_training_set")

After you [create declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/declarative-apis), the next step is to create training data for your model. To do this, pass a labeled dataset to `create_training_set`, which automatically ensures point-in-time accurate computation of each feature value.

For example:

Python

    FeatureEngineeringClient.create_training_set(    df: DataFrame,                                # DataFrame with training data    features: Optional[List[Feature]],            # List of Feature objects    label: Union[str, List[str], None],           # Label column name(s)    exclude_columns: Optional[List[str]] = None,  # Optional: columns to exclude) -> TrainingSet

Call `TrainingSet.load_df` to join original training data with point-in-time dynamically computed features.

The `df` argument must meet the following requirements:

*   Must contain all entity columns referenced by feature definitions.
*   Must contain the timeseries column referenced by feature definitions.
*   Must contain all columns declared in any `RequestSource` schema. Types are validated against the declared schema. Mismatches raise an error (no implicit casting).
*   Should contain label column(s).
*   The set of entity column names, timeseries column names, and request feature column names must be globally unique across all sources.

**Point-in-time correctness:** For aggregation and `ColumnSelection` features backed by a table source, features are computed using only source data available before each row's timestamp, to prevent future data leakage into model training. For `RequestSource` features, the value is taken directly from the labeled DataFrame row.

### `log_model()`[​](#log_model "Direct link to log_model")

Use MLflow to log a model with feature metadata for lineage tracking and automatic feature lookup during inference:

Python

    FeatureEngineeringClient.log_model(    model,                                    # Trained model object    artifact_path: str,                       # Path to store model artifact    flavor: ModuleType,                       # MLflow flavor module (e.g., mlflow.sklearn)    training_set: TrainingSet,                # TrainingSet used for training    registered_model_name: Optional[str],     # Optional: register model in Unity Catalog)

The `flavor` parameter specifies the [MLflow model flavor](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) module to use, such as `mlflow.sklearn` or `mlflow.xgboost`.

Models logged with a `TrainingSet` automatically track lineage to the features used in training. When the training set includes `RequestSource` features, the `RequestSource` columns are added to the MLflow model signature as required inputs. This ensures the serving endpoint's API schema reflects the fields callers must provide at inference time. For details, see [Train models with feature tables](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-models-with-feature-store).

### `score_batch()`[​](#score_batch "Direct link to score_batch")

Perform batch inference with automatic feature lookup:

Python

    FeatureEngineeringClient.score_batch(    model_uri: str,                           # URI of logged model    df: DataFrame,                            # DataFrame with entity keys and timestamps) -> DataFrame

`score_batch` uses the feature metadata stored with the model to automatically compute point-in-time correct features for inference, ensuring consistency with training. For details, see [Train models with feature tables](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-models-with-feature-store).

## Example workflow[​](#example-workflow "Direct link to Example workflow")

Python

    import mlflowfrom databricks.feature_engineering import FeatureEngineeringClientfrom sklearn.ensemble import RandomForestClassifierfe = FeatureEngineeringClient()# Assume features are registered in UC# labeled_df should have columns "user_id", "transaction_time", and "is_fraud"# 1. Create training set using declarative featurestraining_set = fe.create_training_set(    df=labeled_df,    features=features,    label="is_fraud",)# 2. Load training data with computed featurestraining_df = training_set.load_df()X = training_df.drop("is_fraud").toPandas()y = training_df.select("is_fraud").toPandas().values.ravel()# 3. Train modelmodel = RandomForestClassifier().fit(X, y)# 4. Log model with feature metadatawith mlflow.start_run():    fe.log_model(        model=model,        artifact_path="fraud_model",        flavor=mlflow.sklearn,        training_set=training_set,        registered_model_name="main.ecommerce.fraud_model",    )# 5. Batch scoring with automatic feature lookup# inference_df must contain the same entity and timeseries columns# used during training. Features are automatically computed.predictions = fe.score_batch(    model_uri="models:/main.ecommerce.fraud_model/1",    df=inference_df,)predictions.display()

## Training with RequestSource features[​](#training-with-requestsource-features "Direct link to Training with RequestSource features")

When your model requires data that is provided at inference time (such as transaction details from an API call), use `RequestSource` features alongside table-backed features. During training, `RequestSource` columns are extracted from the labeled DataFrame.

Python

    from databricks.feature_engineering import FeatureEngineeringClientfrom databricks.feature_engineering.entities import (    DeltaTableSource, Feature, FieldDefinition, RequestSource,    ScalarDataType, ColumnSelection,)fe = FeatureEngineeringClient()# RequestSource provides transaction data at inference timerequest_source = RequestSource(    schema=[        FieldDefinition(name="transaction_amount", data_type=ScalarDataType.DOUBLE),        FieldDefinition(name="vendor_id", data_type=ScalarDataType.STRING),        FieldDefinition(name="transaction_id", data_type=ScalarDataType.STRING),        FieldDefinition(name="transaction_time", data_type=ScalarDataType.DATE),    ])delta_source = DeltaTableSource(    catalog_name="catalog",    schema_name="schema",    table_name="vendor_data",)# A column selection feature from the request source (pass-through)latest_transaction_amount = Feature(    source=request_source,    function=ColumnSelection("transaction_amount"),    name="latest_transaction_amount",)# A lookup feature from a delta tablevendor_category = Feature(    source=delta_source,    function=ColumnSelection("vendor_category"),    entity=["vendor_id"],    timeseries_column="transaction_time",    name="vendor_category",)# labels_df must contain: transaction_id, transaction_time, vendor_id,# transaction_amount, and the label column.ts = fe.create_training_set(    df=labels_df,    features=[latest_transaction_amount, vendor_category],    label="is_fraud",    exclude_columns=["card_id"],)import mlflowfrom sklearn.ensemble import RandomForestClassifierwith mlflow.start_run():    training_df = ts.load_df().toPandas()    X = training_df.drop(columns=["is_fraud"])    y = training_df["is_fraud"]    model = RandomForestClassifier().fit(X, y)    # log_model() adds RequestSource columns to the MLflow model signature    fe.log_model(        model=model,        artifact_path="fraud_model",        flavor=mlflow.sklearn,        training_set=ts,        registered_model_name="catalog.schema.fraud_model",    )

### What reaches the raw model at serving time[​](#what-reaches-the-raw-model-at-serving-time "Direct link to What reaches the raw model at serving time")

The Feature Store model wrapper filters columns before passing them to the raw model:
