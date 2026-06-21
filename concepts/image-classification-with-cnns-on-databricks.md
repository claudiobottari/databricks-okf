---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 39f12a4778d4a7bfbc494aaa31290586608e62fd4682b9002a8d22446d0cfc80
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - image-classification-with-cnns-on-databricks
    - ICWCOD
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Image Classification with CNNs on Databricks
description: A tutorial demonstrating how to train a 2-D convolutional neural network for image classification on serverless GPUs using Databricks AI Runtime.
tags:
  - computer-vision
  - image-classification
  - cnn
  - databricks
timestamp: "2026-06-19T17:48:53.322Z"
---

```markdown
# Image Classification with CNNs on Databricks

**Image Classification with CNNs on Databricks** refers to a notebook example provided in the Databricks AI Runtime that demonstrates training a two‑dimensional convolutional neural network (CNN) on serverless GPUs for image classification tasks. The example is designed to help users get started with deep learning for computer vision on the platform. ^[computer-vision-databricks-on-aws.md]

## Overview

The tutorial, titled “Image classification using convolutional neural network”, is part of the AI Runtime’s collection of computer‑vision examples. It provides a simple, end‑to‑end walkthrough of defining and training a 2‑D CNN architecture on serverless GPU infrastructure. The example is intended for single‑node training and is available in Public Preview; multi‑GPU distributed training remains in Beta. ^[computer-vision-databricks-on-aws.md]

## Related Tutorials

Databricks offers additional computer‑vision tutorials that build on similar infrastructure:

| Tutorial | Description |
|---|---|
| Object detection using RetinaNet | Train an object detection model with RetinaNet on serverless GPU. |
| Object detection using YOLO11n | Train a YOLO11n model on the COCO128 dataset using serverless GPU, with MLflow tracking and Model Serving deployment. |

These companion examples illustrate how MLflow experiment tracking and model deployment can be integrated into the training workflow. ^[computer-vision-databricks-on-aws.md]

## Related Concepts

- Convolutional Neural Networks – The core architecture used in the example.
- [[Serverless GPU Compute|Serverless GPU]] – The on‑demand GPU resource that powers the training.
- [[AI Runtime]] – The Databricks environment that bundles the necessary libraries.
- [[MLflow]] – Used in related tutorials for experiment tracking and model registry.
- [[Databricks Model Serving]] – Deployment target shown in the YOLO tutorial.

## Sources

- computer-vision-databricks-on-aws.md
```

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
