---
title: Distributed training with TensorFlow 2 | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/machine-learning/train-model/spark-tf-distributor
ingestedAt: "2026-06-18T08:03:09.487Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Documentation archive](https://docs.databricks.com/aws/en/archive/)
*   Distributed training with TensorFlow 2

Last updated on **Sep 26, 2024**

The [spark-tensorflow-distributor](https://github.com/tensorflow/ecosystem/tree/master/spark/spark-tensorflow-distributor) is an open-source native package in TensorFlow that helps users do distributed training with TensorFlow on their Spark clusters. It is built on top of `tensorflow.distribute.Strategy`, which is one of the major features in TensorFlow 2. For detailed API documentation, see [docstrings](https://github.com/tensorflow/ecosystem/blob/master/spark/spark-tensorflow-distributor/spark_tensorflow_distributor/mirrored_strategy_runner.py#L40). For general documentation about distributed TensorFlow, see [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training).

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Distributed Training with TensorFlow 2
