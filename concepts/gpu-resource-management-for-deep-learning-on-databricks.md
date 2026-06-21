---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 28d547810d6bcf4149c986f0b96726b4f4fd18dd8f24551a5d633145288af422
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-resource-management-for-deep-learning-on-databricks
    - GRMFDLOD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: GPU Resource Management for Deep Learning on Databricks
description: Guidance on selecting GPU instances (including A100 GPUs), GPU scheduling optimization, and using cluster policies to guide resource choices for deep learning workloads on Databricks.
tags:
  - gpu
  - resource-management
  - deep-learning
  - databricks
timestamp: "2026-06-18T10:55:00.556Z"
---

# GPU Resource Management for Deep Learning on Databricks

**GPU resource management for deep learning on Databricks** involves selecting appropriate GPU instance types, configuring clusters for optimal utilization, and implementing scheduling strategies to maximize training and inference performance while controlling costs.

## GPU Instance Selection

### A100 GPUs for Deep Learning

A100 GPUs are an efficient choice for many deep learning tasks, including training and tuning large language models, natural language processing, object detection and classification, and recommendation engines. Databricks supports A100 GPUs on all clouds. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

A100 GPUs usually have limited availability. Contact your cloud provider for resource allocation, or consider reserving capacity in advance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Inference-Optimized GPUs

For inference workloads, consider both CPUs and inference-optimized GPU instances such as Amazon EC2 G4 and G5 instances. The best choice depends on model size, data dimensions, and other variables. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

For the complete list of supported GPU types, see [Supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Cluster Configuration for GPU Workloads

### Single Node Clusters for Development

A [Single Node](/concepts/single-node-ai-runtime.md) (driver only) GPU cluster is typically fastest and most cost-effective for deep learning model development. One node with 4 GPUs is likely to be faster for deep learning training than 4 worker nodes with 1 GPU each, because distributed training incurs network communication overhead. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

A Single Node cluster is a good option during fast, iterative development and for training models on small- to medium-size data. If your dataset is large enough to make training slow on a single machine, consider moving to multi-GPU and even distributed compute. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Cluster Policies

Create cluster policies to guide data scientists to the right choices, such as using a Single Node cluster for development and using an autoscaling cluster for large jobs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Autoscaling for Large Jobs

For production-scale training or inference, use autoscaling clusters that can dynamically adjust the number of GPU nodes based on workload demands. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## GPU Scheduling

To maximize your GPUs for distributed deep learning training and inference, optimize GPU scheduling. See [GPU scheduling](https://docs.databricks.com/aws/en/compute/gpu#gpu-scheduling). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Batch Size Tuning

Batch size tuning helps optimize GPU utilization. If the batch size is too small, the calculations cannot fully use the GPU capabilities. Use cluster metrics to view GPU metrics. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Adjust the batch size in conjunction with the learning rate. A good rule of thumb is: when you increase the batch size by n, increase the learning rate by sqrt(n). When tuning manually, try changing batch size by a factor of 2 or 0.5. Then continue tuning to optimize performance, either manually or by testing a variety of hyperparameters using an automated tool like [Optuna](/concepts/optuna.md). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Environment Management

### Databricks Runtime for Machine Learning

Databricks provides pre-built deep learning infrastructure with [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md), which includes the most common deep learning libraries like TensorFlow, PyTorch, and Keras. It also has built-in, pre-configured GPU support including drivers and supporting libraries. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Databricks Runtime ML also includes all capabilities of the Databricks workspace, such as cluster creation and management, library and environment management, code management with Databricks Git folders, automation support including [Lakeflow Jobs](/concepts/lakeflow-jobs.md) and APIs, and integrated MLflow for model development tracking and model deployment and serving. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Customizing Environments

With Databricks Runtime, you can customize your development environment at multiple levels:

- Use notebook-scoped Python libraries or [notebook-scoped R libraries](/concepts/compute-scoped-vs-notebook-scoped-library-installation.md) to use a specific set or version of libraries without affecting other cluster users.
- Install libraries at the cluster level to standardize versions for a team or a project.
- Set up a Databricks job to ensure that a repeated task runs in a consistent, unchanging environment.

^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Monitoring GPU Performance

### Monitoring GPU Utilization

Use cluster metrics to monitor GPU utilization. This helps identify whether batch sizes are appropriate and whether the GPU is being fully utilized. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Cluster metrics are available in all Databricks runtimes. You can examine network, processor, and memory usage to inspect for bottlenecks. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### TensorBoard

[TensorBoard](/concepts/tensorboard-on-databricks.md) is preinstalled in Databricks Runtime ML. You can use it within a notebook or in a separate tab to monitor training progress. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Moving to Distributed Training

When single-node GPU training becomes a bottleneck, move to distributed training. Databricks Runtime ML includes several tools to facilitate this transition.

### TorchDistributor

[TorchDistributor](/concepts/torchdistributor.md) is an open-source module in PySpark that facilitates distributed training with PyTorch on Spark clusters, allowing you to launch PyTorch training jobs as Spark jobs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Optuna for Hyperparameter Tuning

[Optuna](/concepts/optuna.md) provides adaptive hyperparameter tuning for machine learning, helping you find optimal batch sizes, learning rates, and other hyperparameters that affect GPU utilization. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### DeepSpeed and Ray

Databricks Runtime ML also includes DeepSpeed and Ray to facilitate the move from single-node to distributed training. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices for Inference GPUs

### Separating ETL from Inference

If you expect to access data for inference more than once, consider creating a preprocessing job to ETL the data into a [Delta Lake](/concepts/delta-lake.md) table before running the inference job. This spreads the cost of ingesting and preparing data across multiple reads. Separating preprocessing from inference also allows you to select different hardware for each job to optimize cost and performance — for example, use CPUs for ETL and GPUs for inference. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Scaling Inference

Use Spark Pandas UDFs to scale batch and streaming inference across a cluster. When you log a model from Databricks, MLflow automatically provides inference code to apply the model as a pandas UDF. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- GPU Clusters — Configuration and management of GPU-enabled clusters
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-configured ML environment with GPU support
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU and multi-node training strategies
- Cluster Policies — Governance for GPU cluster configuration
- [Delta Lake](/concepts/delta-lake.md) — Optimized data storage for deep learning pipelines
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking with GPU utilization metrics
- [Model Serving](/concepts/model-serving.md) — Deploying models for online inference
- [Optuna](/concepts/optuna.md) — Hyperparameter optimization for GPU workloads

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
