---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b8f6a3b15b90050bfdd712eb55aef4de959b60f19d8dbe6141bdf48711c8211
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - computer-vision-model-training-with-yolo-on-databricks
    - CVMTWYOD
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Computer Vision Model Training with YOLO on Databricks
description: A tutorial demonstrating how to train a YOLO11n object detection model on COCO128 using Databricks AI Runtime, with MLflow tracking and Model Serving deployment.
tags:
  - computer-vision
  - object-detection
  - yolo
  - databricks
timestamp: "2026-06-19T17:48:51.913Z"
---

# Computer Vision Model Training with YOLO on Databricks

**Computer Vision Model Training with YOLO on Databricks** refers to the process of training YOLO (You Only Look Once) object‑detection models using the Databricks AI Runtime, typically on serverless GPU infrastructure. Databricks provides a dedicated tutorial notebook that demonstrates how to train a YOLO11n model on the COCO128 dataset, with integrated [MLflow](/concepts/mlflow.md) tracking and deployment to [Model Serving](/concepts/model-serving.md). ^[computer-vision-databricks-on-aws.md]

## Overview

Databricks AI Runtime includes example notebooks for several computer vision tasks. One of the featured tutorials covers **Object detection using YOLO11n**. This notebook walks through training a YOLO11n object detection model on the COCO128 dataset using serverless GPU compute. The workflow incorporates [MLflow Tracking](/concepts/mlflow-tracking.md) for experiment logging and ends with deploying the trained model to Databricks [Model Serving](/concepts/model-serving.md) for inference. ^[computer-vision-databricks-on-aws.md]

AI Runtime for single‑node tasks is in **Public Preview**, while the distributed training API for multi‑GPU workloads remains in **Beta**. ^[computer-vision-databricks-on-aws.md]

## The YOLO11n Tutorial

The YOLO11n example is one of three computer vision tutorials provided:

| Tutorial | Description |
|----------|-------------|
| Image classification using convolutional neural network (CNN) | Train a 2‑D CNN on serverless GPUs for image classification. |
| Object detection using RetinaNet | Train an object detection model with RetinaNet on serverless GPU. |
| **Object detection using YOLO11n** | Train a YOLO11n model on COCO128 using serverless GPU, with MLflow tracking and Model Serving deployment. |

^[computer-vision-databricks-on-aws.md]

## Key Features

- **Serverless GPU:** The training job runs on serverless GPU compute, eliminating the need to manage clusters manually.
- **MLflow Tracking:** Experiment metrics, parameters, and artifacts are automatically logged, enabling reproducibility and comparison.
- **Model Serving Deployment:** After training, the model can be directly deployed to a Databricks Model Serving endpoint for real‑time inference.

## Related Concepts

- [AI Runtime (Preview)](/concepts/ai-runtime.md) – The runtime environment that provides pre‑configured libraries for machine learning tasks.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On‑demand GPU resources used for training.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Logging and managing ML experiments.
- [Model Serving](/concepts/model-serving.md) – Deploying models as REST endpoints.
- YOLO Object Detection – The family of real‑time object detection models.
- COCO Dataset – Common benchmark dataset for object detection.

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
