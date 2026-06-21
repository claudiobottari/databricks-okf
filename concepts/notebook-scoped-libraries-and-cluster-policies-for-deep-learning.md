---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c11cc360fa95b7f13770ecf4691bfa3bb034d95402991bc60f9832392b3ccba
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - notebook-scoped-libraries-and-cluster-policies-for-deep-learning
    - Cluster Policies for Deep Learning and Notebook-Scoped Libraries
    - NLACPFDL
    - Cluster Policies for Deep Learning
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Notebook-Scoped Libraries and Cluster Policies for Deep Learning
description: Customizing deep learning environments at notebook, cluster, and job levels using notebook-scoped libraries, cluster-level libraries, and cluster policies to enforce consistent configurations
tags:
  - databricks
  - environment-management
  - libraries
  - cluster-policies
timestamp: "2026-06-18T14:33:43.166Z"
---

# Notebook-Scoped Libraries and Cluster Policies for Deep Learning

**Notebook-scoped libraries** and **cluster policies** are two complementary mechanisms in Databricks that help manage the development environment for deep learning workloads. Notebook-scoped libraries allow individual users to install specific Python or R libraries at the notebook level without affecting other cluster users, while cluster policies provide administrative guardrails that guide users toward appropriate compute configurations for their tasks.

## Notebook-Scoped Libraries

Databricks supports **notebook-scoped Python libraries** and **notebook-scoped R libraries**, which let you use a specific set or version of libraries within a single notebook session. These libraries are installed only for the duration of the notebook's attached cluster session and do not persist to other notebooks or users sharing the same cluster. This is particularly useful during deep learning development, where different model architectures or preprocessing pipelines may require conflicting library versions. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Benefits for Deep Learning

Deep learning frameworks such as TensorFlow, PyTorch, and Keras are pre-installed in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). However, during iterative development, you may need to test experimental branches, custom layers, or bleeding-edge releases of these libraries. Notebook-scoped libraries allow you to do so without requiring cluster-wide changes or altering the environment for other team members. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Comparison with Other Environment Scopes

| Scope | Persistence | Use Case |
|-------|-------------|----------|
| Notebook-scoped libraries | Current session only | Individual experimentation |
| Cluster-level libraries | While cluster runs | Team/project standardization |
| Job-level libraries | Each job run | Consistent, repeatable production runs |

For team standardization, you can install libraries at the cluster level. For production workflows that must run in an unchanging environment, you can configure a Databricks job. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Cluster Policies for Deep Learning

**Cluster policies** are administrative rules that guide data scientists toward appropriate compute configurations. For deep learning workflows, policies can enforce choices such as using a [Single Node cluster](/concepts/single-node-clusters-for-pytorch.md) for development and an autoscaling cluster for large jobs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Single Node Clusters for Development

A **Single Node** cluster (driver only) with GPUs is often the fastest and most cost-effective option for deep learning model development. One node with 4 GPUs can train models faster than 4 worker nodes with 1 GPU each, because distributed training incurs network communication overhead. Single Node clusters are a good choice during fast, iterative development and for training models on small- to medium-sized data. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Scaling to Distributed Training

When datasets grow large enough that training becomes slow on a single machine, you should consider moving to multi-GPU and distributed compute. Databricks Runtime ML includes tools for distributed training such as [TorchDistributor](/concepts/torchdistributor.md), [DeepSpeed](/concepts/deepspeed.md), and Ray. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### GPU Selection

For many deep learning tasks — such as training and tuning large language models, natural language processing, object detection, and recommendation engines — A100 GPUs are an efficient choice. Databricks supports A100 GPUs on all clouds. Because A100 GPUs usually have limited availability, it is advisable to contact your cloud provider for resource allocation or consider reserving capacity in advance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Optimizing GPU Utilization

To maximize GPU performance, you should also consider GPU scheduling and batch size tuning. Cluster policies can enforce GPU scheduling configurations to prevent resource contention on multi-GPU clusters. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices

- **Use notebook-scoped libraries during development** to avoid version conflicts and experiment with different library versions without disrupting team members.
- **Use cluster-level libraries** when you need to standardize library versions across a team or project.
- **Apply cluster policies** to guide users toward appropriate hardware choices — for example, Single Node GPU clusters for development and autoscaling clusters for production training jobs.
- **Monitor training** using [TensorBoard](/concepts/tensorboard-on-databricks.md), which is pre-installed in Databricks Runtime ML, and review cluster metrics to identify bottlenecks in network, processor, memory, or GPU utilization.
- **Consider data loading strategies** using [Delta Lake](/concepts/delta-lake.md) tables for efficient I/O, and use streaming approaches like PyTorch IterableDataset, [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming, or Ray Data for datasets that do not fit in memory. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The pre-configured environment with deep learning frameworks
- [Delta Lake](/concepts/delta-lake.md) — Optimized data storage for deep learning data pipelines
- Single Node Cluster — Recommended configuration for development workloads
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling deep learning across multiple GPUs and nodes
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking and model management

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
