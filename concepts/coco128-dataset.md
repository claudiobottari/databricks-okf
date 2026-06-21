---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: edb41379f85019b5475aa6a046664f1a5359e287ae23a56fce35fa935af85e51
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.6
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - coco128-dataset
    - COCO Dataset
    - COCO dataset
  citations:
    - file: computer-vision-databricks-on-aws.md
title: COCO128 dataset
description: COCO128 is a subset of the COCO dataset used for training object detection models such as YOLO11n on Databricks serverless GPUs.
tags:
  - dataset
  - computer-vision
  - object-detection
timestamp: "2026-06-19T14:21:02.185Z"
---

# COCO128 dataset

The **COCO128 dataset** is an object detection dataset used in Databricks example notebooks for training YOLO11n models. It serves as a demonstration dataset for computer vision workflows on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md).

## Usage in Databricks

Within the Databricks platform, the COCO128 dataset is referenced in a tutorial notebook that shows how to train a YOLO11n object detection model. The training uses serverless GPU compute and integrates [MLflow Tracking](/concepts/mlflow-tracking.md) for experiment logging and [Model Serving](/concepts/model-serving.md) for deployment. ^[computer-vision-databricks-on-aws.md]

## Related Concepts

- Object detection
- YOLO11n
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [MLflow](/concepts/mlflow.md)
- [Model Serving](/concepts/model-serving.md)
- [AI Runtime (Preview)](/concepts/ai-runtime.md)

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
