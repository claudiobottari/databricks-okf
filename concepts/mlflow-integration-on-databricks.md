---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 961b5ab7601127664af0995344aee56923c2299785ae2b8c04ab263986348c63
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-on-databricks
    - MIOD
  citations:
    - file: computer-vision-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Integration on Databricks
description: Databricks AI Runtime integrates MLflow for tracking model training experiments, as demonstrated in computer vision tutorials.
tags:
  - mlflow
  - experiment-tracking
  - databricks
  - mllifecycle
timestamp: "2026-06-19T17:49:09.177Z"
---

Here is the wiki page for "MLflow Integration on Databricks", written based solely on the provided source material.

---

## MLflow Integration on Databricks

**MLflow Integration on Databricks** refers to the deep, native embedding of [MLflow](/concepts/mlflow.md) tracking and model management capabilities within the Databricks platform. This integration allows users to log, register, deploy, and monitor machine learning models directly from Databricks notebooks, jobs, and serverless compute environments. The integration is a core component of the [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md), which includes pre-built MLflow libraries. ^[computer-vision-databricks-on-aws.md, configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Key Features

- **Automatic Tracking:** MLflow automatically logs parameters, metrics, and artifacts for runs executed within Databricks, including those on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) and [8xH100](/concepts/8xh100-single-node-configuration.md) nodes. ^[computer-vision-databricks-on-aws.md]
- **Model Registry:** Models can be registered and versioned in the [MLflow Model Registry](/concepts/mlflow-model-registry.md), enabling a central catalog for model governance.
- **Model Serving:** Registered models can be directly deployed to [Model Serving](/concepts/model-serving.md) endpoints for real-time inference.
- **Tutorial Support:** Databricks provides tutorial notebooks that demonstrate MLflow tracking during model training, such as for Object Detection using YOLO11n or RetinaNet.^[computer-vision-databricks-on-aws.md]
- **Serverless Budget Policy Control:** For serverless workloads, MLflow experiments can be configured with a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) via the UI or the `mlflow.set_experiment_tag()` API to control spending.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Serverless Workloads and Budget Policies

When MLflow runs serverless workloads—such as scheduled scorers for [Production Monitoring](/concepts/production-monitoring.md), synthetic evaluation set generation, or [Agent Evaluation](/concepts/mlflow-agent-evaluation.md)—it uses the workspace's default serverless budget policy by default. If the default policy is disabled and no alternative is set, a 403 PERMISSION_DENIED Serverless Budget Policy Error|403 PERMISSION_DENIED Serverless Budget Policy Error|403 PERMISSION_DENIED error occurs. To resolve this, users set a specific budget policy on the experiment using the `mlflow.workload_creation_policy_id` tag. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

The API to set this tag is:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent serverless workloads created from the experiment use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Tutorial Notebooks

Databricks provides example notebooks that showcase MLflow integration for various computer vision tasks:

- **YOLO11n Object Detection:** This notebook trains a YOLO11n model on the COCO128 dataset using serverless GPU, with MLflow tracking and Model Serving deployment.^[computer-vision-databricks-on-aws.md]
- **RetinaNet Object Detection:** This notebook demonstrates training an object detection model using RetinaNet on serverless GPU, with MLflow integration for experiment tracking.^[computer-vision-databricks-on-aws.md]
- **CNN Image Classification:** This notebook provides a simple example of training a 2-D convolutional neural network on serverless GPUs for image classification, with MLflow logging.^[computer-vision-databricks-on-aws.md]

### Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The Databricks runtime optimized for single-node and multi-GPU ML workloads.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Central repository for managing model versions and lifecycle stages.
- [Model Serving](/concepts/model-serving.md) – Deployment infrastructure for serving MLflow models as REST endpoints.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On-demand GPU infrastructure that supports MLflow-tracked training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Distributed training strategy that integrates with MLflow for logging.
- [Data Profiling](/concepts/data-profiling.md) – MLflow can integrate with profile metrics for monitoring model input drift.

### Sources

- computer-vision-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
