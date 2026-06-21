---
title: "horovod.spark: distributed deep learning with Horovod | Databricks on AWS"
source: https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-spark
ingestedAt: "2026-06-18T08:03:02.151Z"
---

important

Horovod and HorovodRunner are now deprecated. Releases after 15.4 LTS ML will not have this package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/#torch-distributor) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow.

Learn how to use the `horovod.spark` package to perform distributed training of machine learning models.

## `horovod.spark` on Databricks[​](#horovodspark-on-databricks "Direct link to horovodspark-on-databricks")

Databricks supports the `horovod.spark` package, which provides an estimator API that you can use in ML pipelines with Keras and PyTorch. For details, see [Horovod on Spark](https://github.com/horovod/horovod/blob/master/docs/spark.rst), which includes a section on [Horovod on Databricks](https://github.com/horovod/horovod/blob/master/docs/spark.rst#horovod-on-databricks).

note

*   Databricks installs the `horovod` package with dependencies. If you upgrade or downgrade these dependencies, there might be compatibility issues.
*   When using `horovod.spark` with custom callbacks in Keras, you must save models in the TensorFlow SavedModel format.
    *   With TensorFlow 2.x, use the `.tf` suffix in the file name.
    *   With TensorFlow 1.x, set the option `save_weights_only=True`.

## Requirements[​](#requirements "Direct link to Requirements")

Databricks Runtime ML 7.4 or above.

note

`horovod.spark` does not support pyarrow versions 11.0 and above (see relevant [GitHub Issue](https://github.com/horovod/horovod/issues/3829)). Databricks Runtime 15.0 ML includes pyarrow version 14.0.1. To use `horovod.spark` with Databricks Runtime 15.0 ML or above, you must manually install pyarrow, specifying a version below 11.0.

## Example: Distributed training function[​](#example-distributed-training-function "Direct link to Example: Distributed training function")

Here is a basic example to run a distributed training function using `horovod.spark`:

Python

    def train():  import horovod.tensorflow as hvd  hvd.init()import horovod.sparkhorovod.spark.run(train, num_proc=2)

## Example notebooks: Horovod Spark estimators using Keras and PyTorch[​](#example-notebooks-horovod-spark-estimators-using-keras-and-pytorch "Direct link to Example notebooks: Horovod Spark estimators using Keras and PyTorch")

The following notebooks demonstrate how to use the Horovod Spark Estimator API with Keras and PyTorch.

#### Horovod Spark Estimator Keras notebook

#### Horovod Spark Estimator PyTorch notebook
