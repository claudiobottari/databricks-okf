---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4454238171a806e4a9df7d1a2d5c9e034c72bc661d17fc2c433fb3b0c6d88bbf
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-for-computer-vision-models
    - MIFCVM
  citations:
    - file: computer-vision-databricks-on-aws.md
title: MLflow Integration for Computer Vision Models
description: AI Runtime computer vision workflows integrate MLflow for experiment tracking and Databricks Model Serving for deployment of trained models.
tags:
  - databricks
  - mlflow
  - model-serving
timestamp: "2026-06-18T11:05:14.662Z"
---

# MLflow Integration for Computer Vision Models

**MLflow Integration for Computer Vision Models** refers to the framework and tooling that enables data scientists and ML engineers to track, manage, and deploy computer vision models using [MLflow](/concepts/mlflow.md) on Databricks. This integration covers both single-node and distributed training workflows for tasks such as image classification and object detection, running on AI Runtime with GPU acceleration.^[computer-vision-databricks-on-aws.md]

## Overview

Computer vision models—including convolutional neural networks (CNNs) for image classification and architectures like RetinaNet or YOLO for object detection—can be trained and tracked using MLflow on Databricks. The platform provides serverless GPU compute for single-node tasks (in Public Preview) and distributed training APIs for multi-GPU workloads (in Beta).^[computer-vision-databricks-on-aws.md]

All training runs are automatically tracked by [MLflow](/concepts/mlflow.md), which logs parameters, metrics, and model artifacts. This tracking enables experiment comparison and model registry management for deployment.^[computer-vision-databricks-on-aws.md]

## Supported Computer Vision Tasks

The following tutorials demonstrate MLflow integration for common computer vision workflows:

| Tutorial | Description |
|----------|-------------|
| [Image classification using convolutional neural network](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-cnn-mnist) | Train a 2-D convolution neural network on serverless GPUs for image classification, with MLflow tracking for accuracy and loss metrics. |
| [Object detection using RetinaNet](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-retinanet-image-detection-model-training) | Train an object detection model using RetinaNet on serverless GPU, logging bounding box predictions and confidence scores via MLflow. |
| [Object detection using YOLO11n](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/tutorials/sgc-yolo11n-detect-coco128) | Train a YOLO11n model on the COCO128 dataset using serverless GPU, with MLflow tracking and [Model Serving](/concepts/model-serving.md) deployment. |

^[computer-vision-databricks-on-aws.md]

## MLflow Tracking Capabilities

During computer vision model training, MLflow automatically captures:

- **Parameters**: Hyperparameters such as learning rate, batch size, number of epochs, and architecture-specific settings (e.g., anchor sizes in RetinaNet, backbone selection)
- **Metrics**: Training and validation metrics including loss, accuracy (for classification), mean average precision (mAP) for object detection, and Intersection over Union (IoU)
- **Model artifacts**: The trained model serialization (e.g., PyTorch or TensorFlow model files) along with any necessary preprocessing pipelines
- **Datasets**: Information about training and validation dataset splits, including references to source data in [Unity Catalog](/concepts/unity-catalog.md)

These logged artifacts enable experiment comparison across runs and direct promotion to [Model Registry](/concepts/mlflow-model-registry.md) for downstream deployment.^[computer-vision-databricks-on-aws.md]

## Model Serving Deployment

Models trained with MLflow on Databricks can be deployed to [Model Serving](/concepts/model-serving.md) endpoints. The YOLO11n tutorial specifically demonstrates this end-to-end workflow: train on serverless GPU using the COCO128 dataset, track with MLflow, then deploy the model to a serving endpoint for real-time inference.^[computer-vision-databricks-on-aws.md]

## AI Runtime Considerations

- **Single-node GPU training**: In Public Preview. Suitable for models that fit on one GPU. MLflow tracking works identically to standard MLflow on Databricks.
- **Distributed multi-GPU training**: In Beta. For large-scale computer vision training (e.g., multi-GPU RetinaNet), use the distributed training API. MLflow merges metrics from all workers into a single run.
- **GPU availability**: Serverless GPU compute is used in all tutorials. Refer to GPU compute guidelines for quota and region availability.

^[computer-vision-databricks-on-aws.md]

## Getting Started

To begin using MLflow for computer vision models:

1. Open a notebook in a Databricks workspace with GPU compute.
2. Select one of the tutorials from the table above.
3. Follow the notebook steps: data loading, model definition, [MLflow Autologging](/concepts/mlflow-autologging.md) or manual logging, training, evaluation, and registry.

All tutorials are self-contained and assume basic familiarity with MLflow and the chosen computer vision framework (PyTorch or TensorFlow).^[computer-vision-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – The open-source platform for ML lifecycle management
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Logging and querying experiments
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Central model catalog for deployment
- [Model Serving](/concepts/model-serving.md) – Deploying models to production endpoints
- [AI Runtime](/concepts/ai-runtime.md) – Optimized runtime for ML workloads on Databricks
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance for training datasets
- GPU Compute – Accelerated hardware for model training
- [Computer Vision](/concepts/computer-vision-on-databricks.md) – Broader field covering image classification and object detection

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
