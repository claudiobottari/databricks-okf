---
title: Distributed training | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/
ingestedAt: "2026-06-18T08:13:19.509Z"
---

When possible, Databricks recommends that you train neural networks on a single machine; distributed code for training and inference is more complex than single-machine code and slower due to communication overhead. However, you should consider distributed training and inference if your model or your data are too large to fit in memory on a single machine. For these workloads, Databricks Runtime ML includes the TorchDistributor, DeepSpeed distributor and Ray packages.

Databricks also offers distributed training for Spark ML models with the `pyspark.ml.connect` module.

## DeepSpeed distributor[​](#deepspeed-distributor "Direct link to DeepSpeed distributor")

The DeepSpeed distributor is built on top of [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor) and is a recommended solution for customers with models that require higher compute power, but are limited by memory constraints. DeepSpeed is an open-source library developed by Microsoft and offers optimized memory usage, reduced communication overhead, and advanced pipeline parallelism. Learn more about [Distributed training with DeepSpeed distributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/deepspeed)

## TorchDistributor[​](#torchdistributor "Direct link to torchdistributor")

[TorchDistributor](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.torch.distributor.TorchDistributor.html) is an open-source module in PySpark that helps users do distributed training with PyTorch on their Spark clusters, so it lets you launch PyTorch training jobs as Spark jobs. Under-the-hood, it initializes the environment and the communication channels between the workers and utilizes the CLI command `torch.distributed.run` to run distributed training across the worker nodes. Learn more about [Distributed training with TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor).

## Ray[​](#ray "Direct link to Ray")

[Ray](https://docs.ray.io/en/latest/ray-overview/index.html) is an open-source framework that specializes in parallel compute processing for scaling ML workflows and AI applications. See [What is Ray on Databricks?](https://docs.databricks.com/aws/en/machine-learning/ray/).

## Spark ML[​](#spark-ml "Direct link to Spark ML")

Use the `pyspark.ml.connect` module to perform distributed training to train Spark ML models and run model inference. In Databricks Runtime 17.0 and above, Spark ML is enabled by default in Standard compute resources, allowing you to use Spark’s distributed machine learning capabilities without managing a full cluster. See [Train Spark ML models on Databricks Connect with `pyspark.ml.connect`](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/distributed-ml-for-spark-connect).
