---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 450ad1949d751f43412920012bc1c4a4d86bf9c13c2505fe6acdbc3e3e350253
  pageDirectory: concepts
  sources:
    - deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-learning-best-practices-on-databricks
    - DLBPOD
    - Model training best practices on Databricks
    - Partitioning best practices on Databricks
    - Deep learning best practices
  citations:
    - file: deep-learning-databricks-on-aws.md
title: Deep learning best practices on Databricks
description: General guidelines and optimization strategies for developing and fine-tuning deep learning models on the Databricks platform.
tags:
  - deep-learning
  - best-practices
  - optimization
timestamp: "2026-06-18T11:46:41.961Z"
---

# Deep learning best practices on Databricks

This page covers best practices for developing, training, and optimizing deep learning models on Databricks, including guidance on cluster configuration, distributed training, experiment tracking, and resource management.

## Cluster Configuration

### Use Databricks Runtime ML

Databricks Runtime ML includes pre-installed deep learning frameworks such as PyTorch and TensorFlow, along with GPU drivers, CUDA libraries, and optimization tools. Using Databricks Runtime ML eliminates the need to manually install and configure these dependencies, reducing setup time and ensuring compatibility. ^[deep-learning-databricks-on-aws.md]

### Select Appropriate GPU Instances

Choose GPU instance types based on your model size and training requirements:

- **Single GPU training**: Suitable for small to medium models or fine-tuning tasks.
- **Multi-GPU single node**: Use for larger models that fit within a single node's memory.
- **Multi-node distributed training**: Required for very large models or when training speed is critical.

For serverless GPU workloads, see [AI Runtime](/concepts/ai-runtime.md) for single and multi-node deep learning support. ^[deep-learning-databricks-on-aws.md]

### Configure Autoscaling Carefully

For deep learning workloads, consider disabling autoscaling or setting narrow scaling limits. Adding or removing nodes during training can cause job interruptions and reduce throughput. Instead, right-size your cluster upfront based on the expected workload. ^[deep-learning-databricks-on-aws.md]

## Distributed Training

### When to Use Distributed Training

Deep learning models are data and computation-intensive, making distributed training important for reducing training time and handling large datasets. Consider distributed training when:

- Your model does not fit on a single GPU.
- Training time with a single GPU is unacceptably long.
- You need to process large datasets efficiently.

### Available Distributed Training Frameworks

Databricks supports multiple distributed training approaches: ^[deep-learning-databricks-on-aws.md]

| Framework | Use Case |
|-----------|----------|
| [TorchDistributor](/concepts/torchdistributor.md) | PyTorch native distributed training on Databricks |
| Ray | Distributed computing with support for deep learning |
| [DeepSpeed](/concepts/deepspeed.md) | Memory optimization and distributed training for large models |

### Best Practices for Distributed Training

- **Use data parallelism** when the model fits on a single GPU but training is slow. Distribute batches across GPUs and synchronize gradients.
- **Use model parallelism** when the model is too large for a single GPU. Split the model layers across multiple GPUs.
- **Monitor GPU utilization** to ensure all GPUs are being used efficiently. Low utilization may indicate bottlenecks in data loading or communication.
- **Optimize data loading** with parallel data pipelines to prevent GPUs from waiting on data. ^[deep-learning-databricks-on-aws.md]

## Experiment Tracking with MLflow

### Track All Training Runs

Tracking remains a cornerstone of the MLflow ecosystem and is especially vital for the iterative nature of deep learning. Use [MLflow Tracking](/concepts/mlflow-tracking.md) to log: ^[deep-learning-databricks-on-aws.md]

- Hyperparameters (learning rate, batch size, optimizer settings)
- Metrics (loss, accuracy, validation scores)
- Model checkpoints
- Training artifacts (plots, confusion matrices)
- Source code and environment details

### Log Models for Reproducibility

Use MLflow to log trained models with their dependencies. This enables:

- Reproducing results by loading the exact model and environment
- Comparing different model versions
- Deploying models to production with confidence

### Compare Runs Systematically

Use the MLflow UI to compare runs side-by-side. Sort and filter runs by metrics to identify the best-performing configurations. This is particularly important for deep learning, where small hyperparameter changes can significantly impact results. ^[deep-learning-databricks-on-aws.md]

## Framework-Specific Best Practices

### PyTorch

PyTorch is included in Databricks Runtime ML and provides GPU-accelerated tensor computation. Best practices include: ^[deep-learning-databricks-on-aws.md]

- Use `torch.utils.data.DataLoader` with multiple workers for efficient data loading.
- Enable cuDNN autotuner with `torch.backends.cudnn.benchmark = True` for fixed input sizes.
- Use mixed precision training with `torch.cuda.amp` to reduce memory usage and speed up training.
- For end-to-end workflows, see the [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md) tutorial notebook.

### TensorFlow

Databricks Runtime ML includes TensorFlow and TensorBoard without requiring additional package installation. Best practices include: ^[deep-learning-databricks-on-aws.md]

- Use `tf.data` for efficient input pipelines.
- Leverage TensorBoard for visualization of training curves, graph structures, and embeddings.
- Use `tf.distribute.MirroredStrategy` for single-node multi-GPU training.
- Use `tf.distribute.MultiWorkerMirroredStrategy` for multi-node distributed training.

## Resource Management

### Monitor GPU Memory

GPU memory is often the limiting factor in deep learning. Monitor memory usage and adjust batch sizes accordingly. Techniques to reduce memory usage include: ^[deep-learning-databricks-on-aws.md]

- Gradient accumulation
- Mixed precision training
- Gradient checkpointing
- Model parallelism

### Use Spot Instances for Cost Savings

For non-critical training jobs or hyperparameter tuning, consider using spot instances to reduce costs. Be aware that spot instances can be preempted, so implement checkpointing to save progress regularly. ^[deep-learning-databricks-on-aws.md]

### Set Up Budget Policies

For serverless GPU workloads, configure [serverless budget policies](/concepts/serverless-budget-policy.md) to control spending and prevent runaway costs. This is especially important for large-scale training runs. ^[deep-learning-databricks-on-aws.md]

## Workflow Optimization

### Use Notebooks for Exploration, Scripts for Production

- Use Databricks notebooks for exploratory work, prototyping, and visualization.
- Convert successful experiments to Python scripts for production training jobs.
- Use [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) to schedule and automate training runs.

### Implement Checkpointing

Save model checkpoints at regular intervals during training. This allows you to: ^[deep-learning-databricks-on-aws.md]

- Resume training from the last checkpoint if a job fails.
- Evaluate intermediate model states.
- Select the best model based on validation metrics across all checkpoints.

### Version Control Everything

Store training code, configuration files, and environment specifications in version control. Use MLflow to log the exact code version and dependencies for each run, ensuring full reproducibility. ^[deep-learning-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — Serverless GPU compute for deep learning
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) — Multi-node and multi-GPU training approaches
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking and model management
- [PyTorch on Databricks](/concepts/pytorch-on-databricks.md) — PyTorch-specific guidance
- [TensorFlow on Databricks](/concepts/tensorflow-on-databricks.md) — TensorFlow-specific guidance
- [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md) — End-to-end tutorial notebook
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Cost control for GPU workloads
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — Automated job scheduling

## Sources

- deep-learning-databricks-on-aws.md

# Citations

1. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
