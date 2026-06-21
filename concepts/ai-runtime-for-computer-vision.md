---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a5fcb3e6a88b66cb681d0584c129da11704ce37ea70d179ec103518a73770267
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-for-computer-vision
    - ARFCV
    - GPU Computer Vision
  citations:
    - file: computer-vision-databricks-on-aws.md
title: AI Runtime for Computer Vision
description: Databricks AI Runtime provides a managed environment with pre-configured libraries and serverless GPUs for training and fine-tuning computer vision models on AWS.
tags:
  - databricks
  - computer-vision
  - machine-learning
timestamp: "2026-06-18T11:04:54.398Z"
---

# AI Runtime for Computer Vision

**AI Runtime for Computer Vision** refers to the set of capabilities within [AI Runtime](/concepts/ai-runtime.md) that enable training, fine-tuning, and deploying computer vision models on Databricks, leveraging serverless GPUs and single-node or multi-GPU distributed training infrastructure.

## Overview

AI Runtime provides a managed environment for computer vision workloads, supporting both single-node tasks and distributed training across multiple GPUs. The single-node capabilities are in **Public Preview**, while the distributed training API for multi-GPU workloads remains in **Beta**. ^[computer-vision-databricks-on-aws.md]

## Supported Computer Vision Tasks

AI Runtime includes example notebooks demonstrating common computer vision tasks, each optimized for serverless GPU execution:

### Image Classification with Convolutional Neural Networks

A simple notebook example demonstrating how to train a 2-D convolutional neural network (CNN) on serverless GPUs for image classification tasks. This is suitable for beginners learning computer vision on Databricks or for rapid prototyping of classification models. ^[computer-vision-databricks-on-aws.md]

### Object Detection with RetinaNet

A notebook that demonstrates how to train an object detection model using RetinaNet on serverless GPU infrastructure. RetinaNet is a one-stage object detection model known for its focal loss mechanism that addresses class imbalance. ^[computer-vision-databricks-on-aws.md]

### Object Detection with YOLO11n

A notebook that demonstrates how to train a YOLO11n object detection model on the COCO128 dataset using serverless GPU. This example includes [MLflow Tracking](/concepts/mlflow-tracking.md) integration for experiment management and [Model Serving](/concepts/model-serving.md) deployment for serving the trained model in production. ^[computer-vision-databricks-on-aws.md]

## Infrastructure and Performance

AI Runtime for computer vision leverages serverless GPUs, eliminating the need to manually provision and manage GPU clusters. The single-node training mode is optimized for smaller datasets and rapid iteration, while the multi-GPU distributed training API (in Beta) supports larger models and datasets that benefit from parallel processing. ^[computer-vision-databricks-on-aws.md]

## Integration with MLflow

All computer vision examples in AI Runtime are designed to work with [MLflow Tracking](/concepts/mlflow-tracking.md) for experiment logging, including metrics, parameters, and model artifacts. This integration enables reproducible experiments and seamless model deployment through [Model Serving](/concepts/model-serving.md). ^[computer-vision-databricks-on-aws.md]

## Getting Started

To get started with computer vision on AI Runtime: ^[computer-vision-databricks-on-aws.md]

- Use the provided example notebooks as templates for your own models
- Choose between single-node (Public Preview) or distributed training (Beta) based on dataset size and model complexity
- Leverage MLflow for experiment tracking and model registry
- Deploy trained models using Databricks Model Serving for real-time inference

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The underlying runtime environment for machine learning workloads
- GPU Clusters — Infrastructure for training deep learning models
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment logging and management
- [Model Serving](/concepts/model-serving.md) — Production deployment of trained models
- Image Classification — Core computer vision task
- Object Detection — Identifying and localizing objects in images

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
