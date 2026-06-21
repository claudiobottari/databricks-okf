---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 616b1bdd9308c047907690f0b525ba5f5d5ea85ca03ad70789eaf3ab52ade203
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - image-classification-with-cnn-on-databricks
    - ICWCOD
    - Image Classification on Databricks
    - image-classification-with-cnn-on-serverless-gpu
    - ICWCOSG
    - image-classification-with-cnns-on-databricks
  citations:
    - file: computer-vision-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Image classification with CNN on Databricks
description: A tutorial notebook demonstrating how to train a 2-D convolutional neural network for image classification on serverless GPUs using Databricks AI Runtime.
tags:
  - computer-vision
  - image-classification
  - cnn
timestamp: "2026-06-19T14:20:43.129Z"
---

# Image Classification with CNN on Databricks

**Image Classification with CNN on Databricks** refers to the practice of training a 2‑D convolutional neural network (CNN) for image classification tasks using Databricks’ AI Runtime and serverless GPU infrastructure. This approach provides a scalable, GPU‑accelerated training environment directly within the Databricks platform.

## Overview

Databricks offers a notebook‑based tutorial that demonstrates how to train a 2‑D convolution neural network on serverless GPUs for image classification. The tutorial is part of the AI Runtime example notebooks and provides a complete end‑to‑end workflow from data loading to model training. ^[computer-vision-databricks-on-aws.md]

## Tutorial: Image Classification Using Convolutional Neural Network

The primary tutorial is titled **Image classification using convolutional neural network**. It is designed to run on a single node using AI Runtime, which is optimized for single‑node deep learning workloads. The notebook uses serverless GPU compute, eliminating the need to manually manage GPU clusters. ^[computer-vision-databricks-on-aws.md]

### Key Features

- **Serverless GPU Training**: The tutorial runs on Databricks’ serverless GPU infrastructure, provisioning on‑demand GPU resources without requiring cluster management. ^[computer-vision-databricks-on-aws.md]
- **2‑D Convolutional Neural Network**: It implements a standard CNN architecture suitable for image classification, demonstrating the core training loop. ^[computer-vision-databricks-on-aws.md]
- **Single‑Node Execution**: The notebook is designed for single‑node tasks using AI Runtime (in Public Preview). ^[computer-vision-databricks-on-aws.md]

## Related Computer Vision Tutorials

Databricks provides additional computer vision tutorials that complement the CNN image classification example: ^[computer-vision-databricks-on-aws.md]

| Tutorial | Description |
|----------|-------------|
| Image classification using convolutional neural network | Simple example of training a 2‑D CNN on serverless GPUs |
| Object detection using RetinaNet | Training an object detection model using RetinaNet on serverless GPU |
| Object detection using YOLO11n | Training a YOLO11n object detection model on the COCO128 dataset, includes MLflow tracking and Model Serving deployment |

## Infrastructure Considerations

### AI Runtime

AI Runtime for single‑node tasks is in **Public Preview**. The distributed training API for multi‑GPU workloads remains in **Beta**. For the CNN image classification tutorial, the single‑node AI Runtime is the intended environment. ^[computer-vision-databricks-on-aws.md]

### GPU Support

Databricks supports [A100 GPUs](/concepts/a100-gpu-support-on-databricks.md) across all cloud providers for deep learning tasks such as training and tuning large language models, natural language processing, object detection, and classification. For image classification workloads, GPU instances provide the necessary computational power for training CNN models efficiently. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- Convolutional Neural Networks (CNNs)
- [AI Runtime](/concepts/ai-runtime.md)
- [Serverless GPU Computing](/concepts/serverless-gpu-compute.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [Object detection with RetinaNet on Databricks](/concepts/object-detection-with-retinanet-on-databricks.md)
- Object Detection with YOLO on Databricks

## Sources

- computer-vision-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
