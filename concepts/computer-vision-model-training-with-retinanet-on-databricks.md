---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe1ec89d0d6d7179b9bb0d26309268edbb375a45c2c733f8ce1289034c7307d5
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - computer-vision-model-training-with-retinanet-on-databricks
    - CVMTWROD
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Computer Vision Model Training with RetinaNet on Databricks
description: A tutorial demonstrating how to train a RetinaNet object detection model on serverless GPUs using Databricks AI Runtime.
tags:
  - computer-vision
  - object-detection
  - retinanet
  - databricks
timestamp: "2026-06-19T17:48:46.642Z"
---

# Computer Vision Model Training with RetinaNet on Databricks

**Computer Vision Model Training with RetinaNet on Databricks** refers to a notebook-based tutorial provided in the Databricks AI Runtime that demonstrates how to train an object detection model using the RetinaNet architecture on serverless GPU infrastructure. The tutorial is part of a collection of computer vision examples that leverage the [AI Runtime](/concepts/ai-runtime.md) for both single-node and multi-GPU workloads. ^[computer-vision-databricks-on-aws.md]

## Overview

The RetinaNet object detection tutorial is one of several computer vision example notebooks available on Databricks. It is designed to run on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) using the AI Runtime, which supports single-node tasks in Public Preview and distributed multi-GPU training in Beta. The tutorial covers the complete workflow for training a RetinaNet model, from data loading to model evaluation. ^[computer-vision-databricks-on-aws.md]

## RetinaNet Object Detection Tutorial

The tutorial titled *Object detection using RetinaNet* demonstrates how to train an object detection model with RetinaNet. It uses a serverless GPU environment provided by the AI Runtime. The notebook is accessible from the Databricks documentation and is intended for users who want to apply state-of-the-art computer vision techniques to their own datasets. ^[computer-vision-databricks-on-aws.md]

No further technical details about the model architecture, hyperparameters, or dataset are provided in the source material beyond the existence of the tutorial link.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The runtime environment used to execute the RetinaNet notebook.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The GPU infrastructure provisioned on demand for training workloads.
- Object Detection – The computer vision task addressed by RetinaNet.
- Image Classification using Convolutional Neural Network – Another computer vision example in the same collection.
- [Object Detection using YOLO11n](/concepts/object-detection-with-yolo11n-on-databricks.md) – An alternative object detection example provided in the AI Runtime.
- [MLflow](/concepts/mlflow.md) – Used for tracking experiments and model serving in companion notebooks.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Supported in Beta via the AI Runtime’s distributed training API.

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
