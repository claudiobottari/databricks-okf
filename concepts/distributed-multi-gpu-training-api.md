---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f7013f681500ee3d79269b4872d3bbbdcb029e3a9bfd0011df006c054fcc0e8
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-multi-gpu-training-api
    - DMTA
    - distributed-multi-gpu-training-on-databricks
    - DMTOD
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Distributed Multi-GPU Training API
description: A Databricks API (currently in Beta) for orchestrating training workloads across multiple GPUs, enabling larger-scale model training.
tags:
  - distributed-training
  - gpu
  - beta
timestamp: "2026-06-19T09:21:09.550Z"
---

# Distributed Multi-GPU Training API

The **Distributed Multi-GPU Training API** is a feature of Databricks AI Runtime that enables training deep learning models across multiple GPUs in a distributed manner. This API is designed to handle multi-GPU workloads and is currently in **Beta** status.^[computer-vision-databricks-on-aws.md]

## Overview

The Distributed Multi-GPU Training API allows practitioners to scale model training beyond single-GPU limitations by coordinating computation across multiple GPU resources. This is particularly important for large models or datasets that cannot be processed efficiently on a single GPU.^[computer-vision-databricks-on-aws.md]

While single-node tasks in AI Runtime are in **Public Preview**, the distributed training API for multi-GPU workloads remains in **Beta** as of the latest documentation.^[computer-vision-databricks-on-aws.md]

## Use Cases

The Distributed Multi-GPU Training API supports various deep learning workloads, including:

- Computer vision tasks such as image classification, object detection, and segmentation
- Training large convolutional neural networks (CNNs)
- Scaling object detection models like RetinaNet and YOLO11n
- Any workload that benefits from parallelized GPU computation

## Status and Release Notes

| Status | Scope |
|--------|-------|
| Public Preview | AI Runtime for single-node tasks |
| Beta | Distributed multi-GPU training API |

^[computer-vision-databricks-on-aws.md]

## Related Tutorials

The following tutorials demonstrate computer vision applications that can be adapted for distributed multi-GPU training:

- **Image classification using convolutional neural network** – Training a 2-D convolutional neural network on serverless GPUs for image classification, scalable to multi-GPU configurations.^[computer-vision-databricks-on-aws.md]
- **Object detection using RetinaNet** – Training an object detection model using RetinaNet, suitable for distributed training across multiple GPUs.^[computer-vision-databricks-on-aws.md]
- **Object detection using YOLO11n** – Training a YOLO11n object detection model on the COCO128 dataset, with MLflow tracking and Model Serving deployment.^[computer-vision-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The Databricks runtime environment that includes the distributed training API
- GPU Scheduling – Optimizing GPU utilization for distributed training workloads
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment tracking for distributed training runs
- [Model Serving](/concepts/model-serving.md) – Deploying trained models for inference
- [Computer vision on Databricks](/concepts/computer-vision-on-databricks.md) – Broader ecosystem for vision model development

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
