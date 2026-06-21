---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed7d85b4f7e43821ddb437a6dcfd16bcb6f81f7ab2bab3e970c41687e0cf7525
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - object-detection-with-yolo11n-on-databricks
    - ODWYOD
    - Object Detection with YOLO on Databricks
    - Object Detection Models
    - Object Detection using YOLO11n
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Object detection with YOLO11n on Databricks
description: A tutorial notebook demonstrating how to train a YOLO11n object detection model on the COCO128 dataset using serverless GPU, with MLflow tracking and Model Serving deployment.
tags:
  - computer-vision
  - object-detection
  - yolo
timestamp: "2026-06-19T14:21:21.234Z"
---

```markdown
---
title: Object Detection with YOLO11n on Databricks
summary: A tutorial notebook demonstrating training a YOLO11n model on the COCO128 dataset with MLflow tracking and Model Serving deployment.
sources:
  - computer-vision-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:05:19.272Z"
updatedAt: "2026-06-19T09:20:47.829Z"
tags:
  - computer-vision
  - object-detection
  - yolo
  - mlflow
aliases:
  - object-detection-with-yolo11n-on-databricks
  - ODWYOD
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Object Detection with YOLO11n on Databricks

**Object Detection with YOLO11n on Databricks** refers to the workflow for training a YOLO11n object detection model using serverless GPU infrastructure on Databricks, with built-in [[MLflow]] tracking and [[Model Serving]] deployment. This approach enables practitioners to train and deploy lightweight object detection models without managing GPU clusters manually.

## Overview

YOLO11n is a lightweight variant of the YOLO (You Only Look Once) family of real-time object detection models. When combined with Databricks' AI Runtime, the training pipeline benefits from serverless GPU compute that eliminates the need for manual cluster management. The workflow is demonstrated in an official Databricks tutorial notebook that uses the COCO128 dataset as the training source. ^[computer-vision-databricks-on-aws.md]

## Key Components

### Model: YOLO11n

YOLO11n is designed for efficient object detection, balancing accuracy with computational efficiency. As a lightweight model, it is well-suited for scenarios where inference speed or resource constraints are important considerations.

### Dataset: COCO128

The COCO128 dataset is a subset of the [[COCO128 dataset|COCO dataset]], a standard benchmark commonly used for object detection tasks. It provides a manageable dataset size for demonstration and experimentation purposes while maintaining representative object detection challenges.

### Compute: Serverless GPU

Serverless GPU on Databricks provides on-demand GPU compute resources without requiring users to provision or manage GPU clusters. This simplifies infrastructure management and allows practitioners to focus on model development.

### Tracking: MLflow

[[MLflow]] is used throughout the training process to log parameters, metrics, and artifacts. This provides experiment reproducibility and enables comparison across different training runs.

### Deployment: Model Serving

After training, the model can be deployed via Databricks [[Model Serving]] for real-time inference, enabling integration with production applications.

## Related Notebooks

The YOLO11n tutorial is part of a broader set of computer vision examples in Databricks AI Runtime. Other tutorials in this collection include: ^[computer-vision-databricks-on-aws.md]

- Image classification using convolutional neural networks (CNNs)
- Object detection using RetinaNet

These notebooks demonstrate various approaches to computer vision tasks, each leveraging serverless GPU infrastructure on Databricks.

## Public Preview

AI Runtime for single-node tasks is in **Public Preview**. The distributed training API for multi-GPU workloads remains in **Beta**. ^[computer-vision-databricks-on-aws.md]

## Related Concepts

- Object detection — the computer vision task addressed by YOLO11n
- YOLO — the family of real-time object detection models
- [[MLflow]] — experiment tracking and model registry
- [[Model Serving]] — deployment of trained models for inference
- [[COCO128 dataset|COCO dataset]] — standard benchmark for object detection
- [[Serverless GPU Compute|Serverless GPU]] — on-demand GPU compute in Databricks
- [[Computer Vision on Databricks]] — broader set of examples and tutorials
- [[A100 GPU Support on Databricks]] — GPU infrastructure options for deep learning workloads

## Sources

- computer-vision-databricks-on-aws.md
```

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
