---
title: Train Spark ML models on Databricks Connect with pyspark.ml.connect | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/distributed-ml-for-spark-connect
ingestedAt: "2026-06-18T08:13:22.749Z"
---

This article provides an example that demonstrates how to use the `pyspark.ml.connect` module to perform distributed training to train Spark ML models and run model inference.

## What is `pyspark.ml.connect`?[​](#what-is-pysparkmlconnect "Direct link to what-is-pysparkmlconnect")

Spark 3.5 introduces `pyspark.ml.connect` which is designed for supporting Spark connect mode and Databricks Connect. Learn more about [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

The `pyspark.ml.connect` module consists of common learning algorithms and utilities, including classification, feature transformers, ML pipelines, and cross validation. This module provides similar interfaces to the legacy [`pyspark.ml` module](https://spark.apache.org/docs/latest/ml-guide.html), but the `pyspark.ml.connect` module currently only contains a subset of the algorithms in `pyspark.ml`. The supported algorithms are listed below:

*   Classification algorithm: `pyspark.ml.connect.classification.LogisticRegression`
*   Feature transformers: `pyspark.ml.connect.feature.MaxAbsScaler` and `pyspark.ml.connect.feature.StandardScaler`
*   Evaluator: `pyspark.ml.connect.RegressionEvaluator`, `pyspark.ml.connect.BinaryClassificationEvaluator` and `MulticlassClassificationEvaluator`
*   Pipeline: `pyspark.ml.connect.pipeline.Pipeline`
*   Model tuning: `pyspark.ml.connect.tuning.CrossValidator`

## Requirements[​](#requirements "Direct link to Requirements")

On Databricks Runtime 17.0 and above, Spark ML on Spark connect is enabled by default on compute resources with **Standard** access mode with some limitations. See [Limitations for Databricks Runtime 17.0 on Standard compute](#limitations). Use Spark ML on Standard compute if you need Spark-level distribution for data that doesn’t fit in memory on a single node or if you need to do distributed hyperparameter tuning.

For Databricks Runtime 14.0 ML and above (including Databricks Runtime 17.0 on compute resources using **Dedicated** access mode), there are additional requirements to use Spark ML:

*   Set up Databricks Connect on your clusters. See [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).
*   Databricks Runtime 14.0 ML or higher installed.
*   Compute resource with **Dedicated** access mode.

## Example notebook[​](#example-notebook "Direct link to Example notebook")

The following notebook demonstrates how to use Distributed ML on Databricks Connect:

#### Distributed ML on Databricks Connect

For reference information about APIs in `pyspark.ml.connect`, Databricks recommends the [Apache Spark API reference](https://spark.apache.org/docs/latest/api/python/index.html)

## Limitations for Databricks Runtime 17.0 on Standard compute[​](#limitations-for-databricks-runtime-170-on-standard-compute "Direct link to limitations-for-databricks-runtime-170-on-standard-compute")

*   **Python only**: Spark ML on Standard compute supports only Python. R and Scala are not supported.
*   **Library support**: Only the `pyspark.ml` package is supported. The `pyspark.mllib` package is not supported.
*   **Model size constraints**: The maximum model size is 1 GB, so training extremely large models may not be feasible. Tree model training will stop early if the model size is about to exceed 1GB.
*   **Memory constraints**: While data can be distributed across the cluster, the trained model itself is cached on the driver node, which is shared among other users. The maximum model cache size per session is 10 GB, and the maximum in-memory model cache size per session is 25% of the Spark driver JVM memory.
*   **Session timeouts**: The cached model on Standard compute automatically times out after 15 minutes of inactivity. To prevent losing your model, save it to disk within 15 minutes after training is completed, or keep the session active with frequent usage.
*   **Resource contention**: In Standard compute environments, resources are shared across users and jobs within the workspace. Running multiple large jobs concurrently may lead to slower performance or competition for executor slots.
*   **No GPU support**: Standard compute environments do not support GPU acceleration. For GPU-accelerated machine learning workloads, dedicated GPU clusters are recommended.
*   **Limited SparkML models**: The following SparkML models are not supported:
    *   `DistributedLDAModel`
    *   `FPGrowthModel`
