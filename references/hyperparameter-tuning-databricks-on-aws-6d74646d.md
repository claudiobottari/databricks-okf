---
title: Hyperparameter tuning | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/
ingestedAt: "2026-06-18T08:09:41.976Z"
---

Python libraries like Optuna, Ray Tune, and Hyperopt simplify and automate hyperparameter tuning to efficiently find an optimal set of hyperparameters for machine learning models. These libraries scale across multiple computes to quickly find hyperparameters with minimal manual orchestration and configuration requirements.

## Optuna[​](#optuna "Direct link to optuna")

[Optuna](https://github.com/optuna/optuna) is a light-weight framework that makes it easy to define a dynamic search space for hyperparameter tuning and model selection. Optuna includes some of the latest optimization and machine learning algorithms.

Optuna can be easily parallelized with Joblib to scale workloads, and integrated with MLflow to track hyperparameters and metrics across trials.

To get started with Optuna, see [Hyperparameter tuning with Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna).

## Ray Tune[​](#ray-tune "Direct link to ray-tune")

Databricks Runtime ML includes Ray, an open-source framework used for parallel compute processing. Ray Tune is a hyperparameter tuning library that comes with Ray and uses Ray as a backend for distributed computing.

For details on how to run Ray on Databricks, see [What is Ray on Databricks?](https://docs.databricks.com/aws/en/machine-learning/ray/). For examples of Ray Tune, see [Ray Tune documentation](https://docs.ray.io/en/latest/tune/tutorials/tune-distributed.html).

## Hyperopt[​](#hyperopt "Direct link to hyperopt")

note

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained.

Hyperopt is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Databricks recommends using either [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna) for single-node optimization or [RayTune](https://docs.ray.io/en/latest/tune/index.html) for a similar experience to the deprecated Hyperopt distributed hyperparameter tuning functionality. Learn more about using [RayTune](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow) on Databricks.

[Hyperopt](https://github.com/hyperopt/hyperopt) is a Python library used for distributed hyperparameter tuning and model selection. Hyperopt works with both distributed ML algorithms such as Apache Spark MLlib and Horovod, as well as with single-machine ML models such as scikit-learn and TensorFlow.

To get started using Hyperopt, see [Use distributed training algorithms with Hyperopt](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-distributed-ml).

## MLlib automated MLflow tracking[​](#mllib-automated-mlflow-tracking "Direct link to MLlib automated MLflow tracking")

note

MLlib automated MLflow tracking is deprecated and disabled by default on clusters that run Databricks Runtime 10.4 LTS ML and above.

Instead, use [MLflow PySpark ML autologging](https://www.mlflow.org/docs/latest/python_api/mlflow.pyspark.ml.html#mlflow.pyspark.ml.autolog) by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with [Databricks Autologging](https://docs.databricks.com/aws/en/mlflow/databricks-autologging).

With MLlib automated MLflow tracking, when you run tuning code that uses CrossValidator or TrainValidationSplit, hyperparameters and evaluation metrics are automatically logged in MLflow.
