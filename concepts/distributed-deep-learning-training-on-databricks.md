---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9cbc7da9e1d962b60f3b3f443483481f9078b05b05f1ecf4089e50501fcdbb88
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
    - deep-learning-databricks-on-aws.md
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-deep-learning-training-on-databricks
    - DDLTOD
    - Distributed deep learning training
    - distributed deep learning training
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
    - file: load-data-using-petastorm-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Distributed Deep Learning Training on Databricks
description: Best practices and examples for developing and fine-tuning deep learning models at scale using distributed training on the Databricks platform.
tags:
  - deep-learning
  - distributed-training
  - machine-learning
  - databricks
timestamp: "2026-06-19T14:54:59.965Z"
---

Here is the updated wiki page for "Distributed Deep Learning Training on Databricks", incorporating the new source material.

---

# Distributed Deep Learning Training on Databricks

**Distributed deep learning training on Databricks** refers to the practice of scaling machine learning model training across multiple GPUs and worker nodes using Databricks infrastructure. Databricks provides pre-built deep learning infrastructure with Databricks Runtime for Machine Learning (Databricks Runtime ML), which includes common deep learning libraries like TensorFlow, PyTorch, and Keras, along with built-in, pre-configured GPU support including drivers and supporting libraries.^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

Databricks Runtime ML also includes all capabilities of the Databricks workspace, such as cluster creation and management, library and environment management, code management with Databricks Git folders, automation support including [Lakeflow Jobs](/concepts/lakeflow-jobs.md) and APIs, and integrated [MLflow](/concepts/mlflow.md) for model development tracking and model deployment and serving.^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## When to Use Distributed Training

A [Single Node cluster](/concepts/single-node-clusters-for-pytorch.md) with a GPU driver is typically fastest and most cost-effective for deep learning model development during the early, iterative phases. One node with 4 GPUs is likely to be faster for deep learning training than 4 worker nodes with 1 GPU each, because distributed training incurs network communication overhead.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

A Single Node cluster is a good option during fast, iterative development and for training models on small- to medium-size data. If your dataset is large enough to make training slow on a single machine, consider moving to multi-GPU and even distributed compute.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Distributed Training Frameworks

Databricks Runtime ML includes several tools to facilitate the move from single-node to distributed training:

- **TorchDistributor**: An open-source module in PySpark that facilitates distributed training with PyTorch on Spark clusters, allowing you to launch PyTorch training jobs as Spark jobs. See distributed training with TorchDistributor for details.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **DeepSpeed**: Included for distributed training optimization.
- **Ray**: Available for distributed batch data processing.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

[Optuna](/concepts/optuna.md) provides adaptive hyperparameter tuning for machine learning and can be used to parallelize training across distributed resources.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## GPU Considerations

### A100 GPUs

A100 GPUs are an efficient choice for many deep learning tasks, such as training and tuning large language models, natural language processing, object detection and classification, and recommendation engines. Databricks supports A100 GPUs on all clouds. A100 GPUs usually have limited availability; contact your cloud provider for resource allocation, or consider reserving capacity in advance.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### GPU Scheduling

To maximize GPUs for distributed deep learning training and inference, optimize GPU scheduling. See GPU scheduling for details.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Data Loading for Distributed Deep Learning

Databricks Runtime ML includes [Delta Lake](/concepts/delta-lake.md) to optimize data throughput for deep learning applications. Databricks recommends using Delta Lake tables for data storage, as Delta Lake simplifies ETL and enables efficient data access. Especially for images, Delta Lake helps optimize ingestion for both training and inference.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Shared Storage for Checkpointing

Machine learning applications may need to use shared storage for data loading and model checkpointing. This is particularly important for distributed deep learning. Databricks provides [Unity Catalog](/concepts/unity-catalog.md), a unified governance solution for data and AI assets, which can be used for accessing data on a cluster using both Spark and local file APIs.^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

### Streaming Approaches for Large Datasets

For very large datasets that do not fit in memory, use streaming approaches:^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- PyTorch IterableDataset for custom streaming logic.
- [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming for datasets hosted on the Hub or in volumes.
- Ray Data for distributed batch data processing.

### Mosaic Streaming (Recommended Replacement)

The `petastorm` package, previously used for converting Spark DataFrames to TensorFlow or PyTorch formats, is deprecated. [Mosaic Streaming](/concepts/mosaic-streaming.md) is the recommended replacement for loading large datasets from cloud storage.^[load-data-using-petastorm-databricks-on-aws.md]

## Petastorm (Legacy Approach)

Petastorm is an open-source data access library that enables single-node or distributed training and evaluation of deep learning models directly from datasets in Apache Parquet format and datasets already loaded as Apache Spark DataFrames. It supports TensorFlow, PyTorch, and PySpark.^[load-data-using-petastorm-databricks-on-aws.md]

### Spark Converter API

The Petastorm Spark converter API simplifies data conversion from Spark to TensorFlow or PyTorch. The recommended workflow is:^[load-data-using-petastorm-databricks-on-aws.md]

1. Use Apache Spark to load and optionally preprocess data.
2. Use the Petastorm `spark_dataset_converter` method to convert data from a Spark DataFrame to a TensorFlow Dataset or a PyTorch DataLoader.
3. Feed data into a deep learning framework for training or inference.

The Petastorm Spark converter caches the input Spark DataFrame in Parquet format in a user-specified cache directory location. The cache directory must be a DBFS path starting with `file:///dbfs/`, for example, `file:///dbfs/tmp/foo/`.^[load-data-using-petastorm-databricks-on-aws.md]

## Performance Optimization

### Early Stopping

Early stopping monitors the value of a metric calculated on the validation set and stops training when the metric stops improving. Each deep learning library provides a native API for early stopping; for example, TensorFlow/Keras provides the EarlyStopping callback, and PyTorch Lightning provides its own implementation.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Batch Size Tuning

Batch size tuning helps optimize GPU utilization. If the batch size is too small, the calculations cannot fully use the GPU capabilities. Adjust the batch size in conjunction with the learning rate. A good rule of thumb is: when you increase the batch size by n, increase the learning rate by sqrt(n). When tuning manually, try changing batch size by a factor of 2 or 0.5.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Transfer Learning

With transfer learning, you start with a previously trained model and modify it as needed for your application. Transfer learning can significantly reduce the time required to train and tune a new model. See [Featurization for Transfer Learning](/concepts/featurization-for-transfer-learning.md) for more information.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Training Very Large Models (20B to 120B+ Parameters)

For models with 20 billion to over 120 billion parameters, standard data parallelism is often insufficient because even a single copy of the model parameters, gradients, and optimizer states exceeds the memory capacity of a single GPU. The primary recommended approach for this scale is [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), which shards model parameters, gradients, and optimizer states across multiple GPUs to significantly reduce the per-GPU memory footprint.^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

For models that require even more advanced memory optimization features, practitioners may consider alternatives like [DeepSpeed](/concepts/deepspeed.md), which provides additional strategies beyond what FSDP offers out-of-the-box. The choice between DDP, FSDP, and DeepSpeed depends on the model size and memory requirements.^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Monitoring Training

[TensorBoard](/concepts/tensorboard-on-databricks.md) is preinstalled in Databricks Runtime ML. You can use it within a notebook or in a separate tab to monitor the training process.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Cluster metrics are available in all Databricks runtimes. You can examine network, processor, and memory usage to inspect for bottlenecks.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Environment Management

With Databricks Runtime, you can customize the development environment at the notebook, cluster, and job levels:^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- Use notebook-scoped Python libraries or [notebook-scoped R libraries](/concepts/compute-scoped-vs-notebook-scoped-library-installation.md) to use a specific set or version of libraries without affecting other cluster users.
- Install libraries at the cluster level to standardize versions for a team or a project.
- Set up a Databricks job to ensure that a repeated task runs in a consistent, unchanging environment.

You can create cluster policies to guide data scientists to the right choices, such as using a Single Node cluster for development and an autoscaling cluster for large jobs.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Inference After Distributed Training

Once a model is trained, Databricks provides multiple serving options. Use [MLflow](/concepts/mlflow.md) to simplify deployment and model serving. MLflow can log any deep learning model, including custom preprocessing and postprocessing logic. Models in [Unity Catalog](/concepts/unity-catalog.md) or the [Workspace Model Registry](/concepts/workspace-model-registry.md) can be deployed for batch, streaming, or online inference.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Online Serving

The best option for low-latency serving is online serving behind a REST API. Databricks [Model Serving](/concepts/model-serving.md) provides a unified interface to deploy, govern, and query AI models. It supports custom models packaged in MLflow format, foundation models, and external models hosted outside Databricks.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Batch Inference

Spark Pandas UDFs are recommended for scaling batch and streaming inference across a cluster. When you log a model from Databricks, MLflow automatically provides inference code to apply the model as a pandas UDF.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

If you expect to access data for inference more than once, consider creating a preprocessing job to ETL the data into a [Delta Lake Table](/concepts/delta-lake-table.md) before running the inference job. This spreads the cost across multiple reads and allows selecting different hardware for each job.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The pre-configured runtime for deep learning workloads
- Single Node Cluster — Recommended starting point for deep learning development
- [Delta Lake](/concepts/delta-lake.md) — Storage layer for optimizing data throughput
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking and model management
- [TorchDistributor](/concepts/torchdistributor.md) — PySpark module for distributed PyTorch training
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Strategy for training very large models (20B+ parameters)
- [DeepSpeed](/concepts/deepspeed.md) — Alternative framework for advanced memory optimization
- [Optuna](/concepts/optuna.md) — Hyperparameter optimization framework
- [TensorBoard](/concepts/tensorboard-on-databricks.md) — Training visualization tool
- [Mosaic Streaming](/concepts/mosaic-streaming.md) — Recommended data loading approach for large datasets
- [Model Serving](/concepts/model-serving.md) — Online and batch inference deployment

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
- load-data-using-petastorm-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
3. [load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md](/references/load-data-for-machine-learning-and-deep-learning-databricks-on-aws-dfd2be96.md)
4. [load-data-using-petastorm-databricks-on-aws.md](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
5. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
