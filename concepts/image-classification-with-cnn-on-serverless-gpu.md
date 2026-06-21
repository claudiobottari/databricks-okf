---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1524098362d2c92a24ff501809384cd0804f20a2b57eb2cb35e34b11c100f7d
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - image-classification-with-cnn-on-serverless-gpu
    - ICWCOSG
  citations:
    - file: computer-vision-databricks-on-aws.md
title: Image Classification with CNN on Serverless GPU
description: Training a 2-D convolutional neural network for image classification using serverless GPUs in Databricks.
tags:
  - computer-vision
  - deep-learning
  - image-classification
timestamp: "2026-06-18T14:41:06.840Z"
---

# Image Classification with CNN on Serverless GPU

**Image Classification with CNN on Serverless GPU** refers to a notebook tutorial provided by Databricks AI Runtime that demonstrates how to train a 2‑D convolutional neural network (CNN) for image classification using serverless GPU infrastructure. The tutorial is designed as a simple, introductory example for practitioners who want to leverage GPU acceleration without managing dedicated GPU clusters.

## Overview

Databricks AI Runtime for single‑node tasks (in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types)) includes a notebook that walks through training a CNN for image classification on serverless GPUs. The tutorial focuses on a basic 2‑D convolution architecture, making it suitable for users who are new to deep learning on Databricks or who want a quick start with serverless GPU compute for vision tasks. ^[computer-vision-databricks-on-aws.md]

## Tutorial Content

The notebook provides a step‑by‑step example of how to train a 2‑D convolutional neural network entirely on serverless GPUs. It covers data loading, model definition, training loops, and evaluation — all within the AI Runtime environment. The tutorial is purpose‑built for serverless GPU, meaning no manual cluster setup or GPU instance management is required. ^[computer-vision-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The Databricks environment that hosts this tutorial and optimizes single‑node GPU workloads.
- [Serverless GPU](/concepts/serverless-gpu-compute.md) – The on‑demand GPU infrastructure used by the notebook, eliminating the need to manage clusters.
- Convolutional Neural Network – The model architecture applied in the tutorial.
- Image Classification – The task demonstrated by the tutorial.
- [Computer vision on Databricks](/concepts/computer-vision-on-databricks.md) – The broader notebook collection that includes object detection tutorials such as RetinaNet and YOLO11n.

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
