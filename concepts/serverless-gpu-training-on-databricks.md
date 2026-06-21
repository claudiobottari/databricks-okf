---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73b01e789e9693b7aee10a0f23dbccf5271378f0bce3ca5b65e473e323fbda47
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-training-on-databricks
    - SGTOD
    - Serverless GPU Distributed Training on Databricks
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Serverless GPU Training on Databricks
description: AI Runtime supports serverless GPU compute for single-node computer vision tasks (Public Preview), with a separate Beta API for distributed multi-GPU training.
tags:
  - databricks
  - gpu
  - serverless
timestamp: "2026-06-18T11:05:00.982Z"
---

# Serverless GPU Training on Databricks

**Serverless GPU training** on Databricks enables users to train machine learning models — particularly computer vision models — using GPU resources without provisioning or managing GPU clusters. The training runs on AI Runtime, which provides pre-configured environments optimized for GPU workloads.^[computer-vision-databricks-on-aws.md]

## Availability

AI Runtime for single‑node GPU tasks is in **Public Preview**. The distributed training API for multi‑GPU workloads remains in **Beta**. This means that most users can run single‑node GPU training in preview, while multi‑node distributed training is available as a beta feature.^[computer-vision-databricks-on-aws.md]

## Example Notebooks

Databricks provides tutorial notebooks that demonstrate common computer vision tasks using serverless GPUs. These examples cover image classification, object detection, and include integration with [MLflow Tracking](/concepts/mlflow-tracking.md) and [Model Serving](/concepts/model-serving.md) for experiment tracking and deployment.

| Tutorial | Description |
|----------|-------------|
| [Image classification using convolutional neural network](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-cnn-mnist) | Train a 2‑D convolution neural network on serverless GPUs for image classification. |
| [Object detection using RetinaNet](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-retinanet-image-detection-model-training) | Train an object detection model using RetinaNet on serverless GPU. |
| [Object detection using YOLO11n](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-yolo11n-detect-coco128) | Train a YOLO11n object detection model on the COCO128 dataset using serverless GPU, with MLflow tracking and Model Serving deployment. |

^[computer-vision-databricks-on-aws.md]

## Benefits

Serverless GPU training abstracts away cluster management, allowing data scientists and ML engineers to focus on model development rather than infrastructure. The AI Runtime includes common deep learning libraries and is configured to leverage GPU acceleration out of the box. Because the compute is serverless, users only pay for the GPU time consumed during training, and idle capacity is automatically reclaimed.

*Note: The specific billing model and resource limits are governed by your Databricks workspace configuration and are not detailed in the source document.*

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The Databricks runtime that provides GPU‑optimized environments.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Used in the YOLO11n example to log training metrics.
- [Model Serving](/concepts/model-serving.md) — For deploying trained models to production endpoints.
- GPU Compute — General concept of GPU‑accelerated compute on Databricks.

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
