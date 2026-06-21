---
title: Use distributed training algorithms with Hyperopt | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-distributed-ml
ingestedAt: "2026-06-18T08:09:47.512Z"
---

note

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained.

Hyperopt is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Databricks recommends using either [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna) for single-node optimization or [RayTune](https://docs.ray.io/en/latest/tune/index.html) for a similar experience to the deprecated Hyperopt distributed hyperparameter tuning functionality. Learn more about using [RayTune](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow) on Databricks.

In addition to single-machine training algorithms such as those from scikit-learn, you can use Hyperopt with distributed training algorithms. In this scenario, Hyperopt generates trials with different hyperparameter settings on the driver node. Each trial is executed from the driver node, giving it access to the full cluster resources. This setup works with any distributed machine learning algorithms or libraries, including Apache Spark MLlib and HorovodRunner.

When you use Hyperopt with distributed training algorithms, do not pass a `trials` argument to `fmin()`, and specifically, do not use the `SparkTrials` class. `SparkTrials` is designed to distribute trials for algorithms that are not themselves distributed. With distributed training algorithms, use the default `Trials` class, which runs on the cluster driver. Hyperopt evaluates each trial on the driver node so that the ML algorithm itself can initiate distributed training.

note

Databricks does not support automatic logging to MLflow with the `Trials` class. When using distributed training algorithms, you must manually call MLflow to log trials for Hyperopt.

## Notebook example: Use Hyperopt with MLlib algorithms[​](#notebook-example-use-hyperopt-with-mllib-algorithms "Direct link to Notebook example: Use Hyperopt with MLlib algorithms")

The example notebook shows how to use Hyperopt to tune MLlib's distributed training algorithms.

#### Hyperopt and MLlib distributed training notebook

## Notebook example: Use Hyperopt with HorovodRunner[​](#notebook-example-use-hyperopt-with-horovodrunner "Direct link to Notebook example: Use Hyperopt with HorovodRunner")

HorovodRunner is a general API used to run distributed deep learning workloads on Databricks. HorovodRunner integrates [Horovod](https://github.com/horovod/horovod) with Spark's [barrier mode](https://issues.apache.org/jira/browse/SPARK-24374) to provide higher stability for long-running deep learning training jobs on Spark.

The example notebook shows how to use Hyperopt to tune distributed training for deep learning based on HorovodRunner.

#### Hyperopt and HorovodRunner distributed training notebook
