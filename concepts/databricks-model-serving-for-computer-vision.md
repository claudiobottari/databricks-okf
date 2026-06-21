---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0efb3bcbc60cb7ebcc21615a3a27829b4c986cd78df01b36735c4218bc287bb
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving-for-computer-vision
    - DMSFCV
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Databricks Model Serving for computer vision
description: Databricks supports deploying trained computer vision models (e.g., YOLO11n) to production using Model Serving after training on AI Runtime.
tags:
  - databricks
  - model-serving
  - mlops
timestamp: "2026-06-19T14:20:55.646Z"
---

# Databricks Model Serving for Computer Vision

**Databricks Model Serving for computer vision** refers to the deployment of trained computer vision models — such as image classifiers and object detectors — as production endpoints on the Databricks platform. Model Serving integrates with [MLflow](/concepts/mlflow.md) and [AI Runtime](/concepts/ai-runtime.md) to allow seamless transition from training to inference.

## Overview

Databricks provides [Model Serving](/concepts/model-serving.md) capabilities that allow users to deploy machine learning models as REST API endpoints. For computer vision workloads, these endpoints can serve models trained on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) using [AI Runtime](/concepts/ai-runtime.md). The platform supports both single-node and multi-GPU distributed training, and models can be registered and deployed using MLflow’s model registry and deployment APIs.^[computer-vision-databricks-on-aws.md]

## Supported Computer Vision Tasks

Databricks provides example notebooks that demonstrate end-to-end workflows for training and deploying computer vision models. The following tutorials are available:

- **Image Classification using Convolutional Neural Networks** – Trains a 2D CNN on serverless GPUs for image classification.^[computer-vision-databricks-on-aws.md]
- **Object Detection using RetinaNet** – Demonstrates training an object detection model on serverless GPU.^[computer-vision-databricks-on-aws.md]
- **Object Detection using YOLO11n** – Trains a YOLO11n model on the COCO128 dataset, with MLflow tracking and Model Serving deployment.^[computer-vision-databricks-on-aws.md]

## Model Training with AI Runtime

All tutorials use **AI Runtime**, Databricks’ environment optimized for deep learning. Single-node tasks are in **Public Preview**, while the distributed training API for multi-GPU workloads remains in **Beta**.^[computer-vision-databricks-on-aws.md]

Training is performed on serverless GPUs, which provide on-demand acceleration without the need to manage clusters. Models are logged with MLflow to track parameters, metrics, and artifacts.^[computer-vision-databricks-on-aws.md]

## Model Serving Deployment

While training notebooks for image classification (CNN) and object detection (RetinaNet) focus on the training phase, the YOLO11n tutorial explicitly includes **Model Serving deployment**. After training, the model is registered in MLflow and deployed as a serving endpoint, enabling real-time inference requests.^[computer-vision-databricks-on-aws.md]

To serve a computer vision model, the typical workflow is:

1. Train the model using a supported framework (e.g., PyTorch, TensorFlow) on serverless GPU.
2. Log the model to MLflow with the proper signature and environment.
3. Deploy the model using Databricks Model Serving, either via the UI or API.

The serving endpoint accepts input images (e.g., base64-encoded or as raw bytes) and returns predictions such as class labels or bounding boxes.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The environment used for training computer vision models.
- [MLflow](/concepts/mlflow.md) – Used for experiment tracking and model deployment.
- [Model Serving](/concepts/model-serving.md) – The infrastructure for deploying models as scalable endpoints.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On-demand GPU resources for training and inference.
- [GPU Computer Vision](/concepts/ai-runtime-for-computer-vision.md) – General guidance on using GPUs for vision workloads.
- RetinaNet – A popular one-stage object detection model.
- YOLO11n – A lightweight real-time object detection model.

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
