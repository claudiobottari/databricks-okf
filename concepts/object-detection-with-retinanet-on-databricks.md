---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ddbcd2576311a908a3b828f2d0f39b1fd13bf74eb6fedfd1400d2fc1bfcf1b4
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - object-detection-with-retinanet-on-databricks
    - ODWROD
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Object detection with RetinaNet on Databricks
description: A tutorial notebook demonstrating how to train an object detection model using RetinaNet on serverless GPU with Databricks AI Runtime.
tags:
  - computer-vision
  - object-detection
  - retinanet
timestamp: "2026-06-19T14:20:39.303Z"
---

# Object Detection with RetinaNet on Databricks

**Object Detection with RetinaNet on Databricks** refers to the workflow for training a RetinaNet object detection model using GPU-accelerated compute on the Databricks platform, leveraging the AI Runtime environment. A tutorial notebook demonstrates end-to-end training of a RetinaNet model on serverless GPUs.^[computer-vision-databricks-on-aws.md]

## Overview

RetinaNet is a one-stage object detection model known for its use of focal loss to address class imbalance during training. On Databricks, you can train such models using the [AI Runtime](/concepts/ai-runtime.md) environment, which simplifies dependency management and provides optimized GPU compute. The tutorial notebook titled "Object detection using RetinaNet" walks through the full training pipeline.^[computer-vision-databricks-on-aws.md]

## AI Runtime and GPU Support

- **AI Runtime for single-node tasks** is in **Public Preview**.^[computer-vision-databricks-on-aws.md]
- **Distributed training APIs for multi-GPU workloads** remain in **Beta**.^[computer-vision-databricks-on-aws.md]

The RetinaNet tutorial is designed to run on serverless GPU resources, which are available through AI Runtime. This allows you to train models without managing cluster infrastructure or provisioning hardware in advance.^[computer-vision-databricks-on-aws.md]

## Prerequisites

To train RetinaNet on Databricks, you need:

- A Databricks workspace with access to [AI Runtime](/concepts/ai-runtime.md)
- A serverless GPU compute resource attached to your notebook
- The AI Runtime environment selected in the compute configuration

## Related Tutorials

Databricks offers several computer vision example notebooks using AI Runtime, including:

- Image classification using convolutional neural networks
- Object detection using RetinaNet (this page)
- Object detection using YOLO11n on the COCO128 dataset

Each tutorial integrates with [MLflow](/concepts/mlflow.md) for experiment tracking and can optionally deploy the trained model to [Model Serving](/concepts/model-serving.md).^[computer-vision-databricks-on-aws.md]

## Usage

To train RetinaNet on Databricks, open the provided notebook in a workspace attached to an AI Runtime cluster with serverless GPU support. The notebook covers data loading, model definition, training, and evaluation. Follow the instructions within the notebook to adjust hyperparameters and dataset paths. The notebook demonstrates how to leverage serverless GPU compute for the entire training workflow.^[computer-vision-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Object Detection
- RetinaNet
- [MLflow](/concepts/mlflow.md)
- [Model Serving](/concepts/model-serving.md)
- GPU Training on Databricks
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
