---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1436b433a7d722330577f23c83a2c340b3f55a8e32c8891b0ff6140a3964f7d0
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-for-xgboost-spark-models
    - MIFXSM
  citations:
    - file: distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md
title: MLflow Integration for XGBoost Spark Models
description: Limitations of MLflow autologging with distributed XGBoost and recommended use of mlflow.spark.log_model for model logging
tags:
  - mlflow
  - xgboost
  - spark
  - logging
timestamp: "2026-06-18T15:33:03.434Z"
---

# MLflow Integration for XGBoost Spark Models

**MLflow Integration for XGBoost Spark Models** refers to the recommended approach for logging, tracking, and managing XGBoost models trained using the `xgboost.spark` module within the MLflow ecosystem. While `xgboost.spark` estimators (`SparkXGBRegressor`, `SparkXGBClassifier`, `SparkXGBRanker`) can be incorporated directly into SparkML Pipelines, their integration with MLflow has specific requirements that differ from standard XGBoost models. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Using MLflow with `xgboost.spark`

The standard `mlflow.xgboost.autolog()` function **cannot** be used with distributed XGBoost training via the `xgboost.spark` module. Instead, you must explicitly log the trained Spark model using `mlflow.spark.log_model()`. This method accepts the fitted `xgboost.spark` model object and an artifact path, enabling MLflow to serialize and store the model in the format compatible with [Spark ML Pipelines](/concepts/mllib-pipelines-api.md). ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

```python
import mlflow
from xgboost.spark import SparkXGBClassifier

# Train the model
classifier = SparkXGBClassifier(num_workers=sc.defaultParallelism)
model = classifier.fit(train_df)

# Log the model with MLflow
with mlflow.start_run():
    mlflow.spark.log_model(spark_xgb_model=model, artifact_path="xgboost-spark-model")
```

This approach works for both single‑node (`num_workers=1`) and multi‑node distributed training. The logged model can later be loaded for batch inference or deployed as a MLflow Model serving endpoint. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Important Considerations

- Because `mlflow.xgboost.autolog` is not compatible, you must manually log parameters, metrics, and artifacts if you wish to capture them. Consider using `mlflow.log_param()` and `mlflow.log_metric()` alongside `mlflow.spark.log_model()`. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- When the `xgboost.spark` model is part of a larger `pyspark.ml.PipelineModel`, the entire pipeline can be logged using `mlflow.spark.log_model()` with the pipeline object, which preserves all stages including the XGBoost stage. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]
- The `xgboost.spark` module is available in Databricks Runtime 12.0 ML and above. For the deprecated `sparkdl.xgboost` module, a migration guide is provided in the source documentation. ^[distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – Log parameters, metrics, and artifacts
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) – Integrating estimators with pipeline stages
- XGBoost Parameters – Configuring XGBoost for Spark
- [Distributed Training of XGBoost Models](/concepts/distributed-training-with-xgboostspark.md) – Multi‑worker setup
- [GPU Training with xgboost.spark](/concepts/gpu-training-with-xgboostspark.md) – Enabling GPU acceleration

## Sources

- distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-xgboostspark-databricks-on-aws-49a22c88.md)
