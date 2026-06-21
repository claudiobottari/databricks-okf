---
title: Use XGBoost on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost
ingestedAt: "2026-06-18T08:13:44.582Z"
---

This article provides examples of training machine learning models using XGBoost in Databricks. Databricks Runtime for Machine Learning includes XGBoost libraries for both Python and Scala. You can train XGBoost models on an individual machine or in a distributed fashion.

## Train XGBoost models on a single node[​](#train-xgboost-models-on-a-single-node "Direct link to Train XGBoost models on a single node")

You can train models using the Python `xgboost` package. This package supports only single node workloads. To train a PySpark ML pipeline and take advantage of distributed training, see [Distributed training of XGBoost models](#xgboost-pyspark).

#### XGBoost Python notebook

## Distributed training of XGBoost models[​](#distributed-training-of-xgboost-models "Direct link to distributed-training-of-xgboost-models")

For distributed training of XGBoost models, Databricks includes PySpark estimators based on the `xgboost` package. In Databricks Runtime 16.4 LTS ML and below, Databricks also includes the Scala package `xgboost-4j`. For details and example notebooks, see the following:

*   [Distributed training of XGBoost models using `xgboost.spark`](https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost-spark) (Databricks Runtime 12.0 ML and above)
*   [Distributed training of XGBoost models using `sparkdl.xgboost`](https://docs.databricks.com/aws/en/machine-learning/train-model/sparkdl-xgboost) (deprecated starting with Databricks Runtime 12.0 ML)
*   [Distributed training of XGBoost models using Scala](https://docs.databricks.com/aws/en/machine-learning/train-model/xgboost-scala)

## Install XGBoost on Databricks[​](#install-xgboost-on-databricks "Direct link to install-xgboost-on-databricks")

If you need to install XGBoost on Databricks Runtime or use a different version than the one pre-installed with Databricks Runtime ML, follow these instructions.

### Install XGBoost on Databricks Runtime ML[​](#install-xgboost-on-databricks-runtime-ml "Direct link to install-xgboost-on-databricks-runtime-ml")

XGBoost is included in Databricks Runtime ML. You can use these libraries in Databricks Runtime ML without installing any packages.

For the version of XGBoost installed in the Databricks Runtime ML version you are using, see the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/). To install other Python versions in Databricks Runtime ML, install XGBoost as a [Databricks PyPI library](https://docs.databricks.com/aws/en/libraries/). Specify it as the following and replace `<xgboost version>` with the desired version.

Python

    xgboost==<xgboost version>

### Install XGBoost on Databricks Runtime[​](#install-xgboost-on-databricks-runtime "Direct link to install-xgboost-on-databricks-runtime")

*   **Python package**: Execute the following command in a notebook cell:
    

To install a specific version, replace `<xgboost version>` with the desired version:

Python

      %pip install xgboost==<xgboost version>

*   **Scala/Java packages**: Install as a [Databricks library](https://docs.databricks.com/aws/en/libraries/) with the Spark Package name `xgboost-linux64`.
