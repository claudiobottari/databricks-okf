---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffec058cf333f10aeb2d81e39e60d55d01e17cd4b9752b5d09bd897fb04642d6
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
    - computer-vision-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - gpu-accelerated-computer-vision-on-databricks
    - GCVOD
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
    - file: computer-vision-databricks-on-aws.md
title: GPU-Accelerated Computer Vision on Databricks
description: Using GPU-optimized AI Runtime on Databricks for computer vision tasks including object detection and image classification.
tags:
  - databricks
  - computer-vision
  - gpu
timestamp: "2026-06-19T13:58:16.344Z"
---

# GPU-Accelerated Computer Vision on Databricks

**GPU-Accelerated Computer Vision on Databricks** refers to the use of [AI Runtime](/concepts/ai-runtime.md) with serverless GPUs to train and fine-tune computer vision models such as image classifiers, object detectors, and other deep learning vision models. Databricks provides pre-built example notebooks that walk through the entire workflow — from data loading to model training, tracking with [MLflow](/concepts/mlflow.md), and deployment via [Model Serving](/concepts/model-serving.md).

## Overview

AI Runtime for single-node tasks is in Public Preview, while the distributed training API for multi-GPU workloads remains in Beta.^[ai-runtime-example-notebooks-databricks-on-aws.md] The runtime includes optimized libraries and environments for running GPU-intensive workloads without managing cluster infrastructure. Computer vision notebooks are designed to run on serverless GPU compute and demonstrate end-to-end training processes.^[computer-vision-databricks-on-aws.md]

## Example Notebooks

The following tutorials are provided as part of the AI Runtime example notebooks for computer vision:

| Tutorial | Description |
|----------|-------------|
| **Image classification using convolutional neural network** | Trains a 2-D convolutional neural network on serverless GPUs for image classification using the MNIST dataset.^[computer-vision-databricks-on-aws.md] |
| **Object detection using RetinaNet** | Trains an object detection model with RetinaNet on serverless GPU.^[computer-vision-databricks-on-aws.md] |
| **Object detection using YOLO11n** | Trains a YOLO11n object detection model on the COCO128 dataset using serverless GPU, with MLflow tracking and Model Serving deployment.^[computer-vision-databricks-on-aws.md] |

Each notebook is self-contained and can be run directly on a Databricks workspace with serverless GPU enabled. The examples cover both classic architectures (CNN, RetinaNet) and modern lightweight detectors (YOLO11n).

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The pre-configured runtime environment for GPU workloads.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU resources used by these notebooks.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Used to log parameters, metrics, and models during training.
- [Model Serving](/concepts/model-serving.md) — Deployment target for trained computer vision models.
- Object Detection on Databricks — Broader topic covering detection workflows.
- Image Classification on Databricks — Classification approaches using distributed GPU.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md
- computer-vision-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
2. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
