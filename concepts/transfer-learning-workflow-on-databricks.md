---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3915783afc23f7c348e550a6f28f7f1fc8dd276af6686c5d803520b1b26964b1
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - transfer-learning-workflow-on-databricks
    - TLWOD
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Transfer Learning Workflow on Databricks
description: "A four-step workflow: start with a pre-trained model, truncate its last layers, apply the modified model to a new dataset to compute features, then train a downstream model using those features."
tags:
  - transfer-learning
  - workflow
  - databricks
  - machine-learning-pipeline
timestamp: "2026-06-19T18:49:09.658Z"
---

# Transfer Learning Workflow on Databricks

**Transfer Learning Workflow on Databricks** refers to the process of reusing a pre-trained deep learning model to compute features for a new task by distributing the featurization step across a cluster. Databricks supports this workflow at scale using pandas UDFs and deep learning libraries included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), such as TensorFlow and PyTorch. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Overview

[Transfer Learning](/concepts/transfer-learning.md) is a technique that reuses knowledge from one problem domain in a related domain. Featurization is a simple and powerful method for transfer learning: computing features using a pre-trained deep learning model transfers knowledge about good features from the original domain. Databricks enables featurization at scale by distributing the computation across a cluster. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Steps to Compute Features for Transfer Learning

The workflow consists of four steps:

1. **Start with a pre-trained deep learning model** – for example, an image classification model from `tensorflow.keras.applications`. ^[featurization-for-transfer-learning-databricks-on-aws.md]
2. **Truncate the last layer(s)** of the model. The modified model produces a tensor of features as output, rather than a prediction. ^[featurization-for-transfer-learning-databricks-on-aws.md]
3. **Apply the model to a new image dataset** from a different problem domain, computing features for the images. This step is performed at scale using pandas UDFs. ^[featurization-for-transfer-learning-databricks-on-aws.md]
4. **Use these features to train a new model** – for example, a logistic regression. (The example notebook in the Databricks documentation omits this final step.) ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Example: Use pandas UDFs for Featurization

The recommended approach to perform the featurization step is using pandas UDFs or their newer variant [Scalar Iterator pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md). These offer flexible APIs, support any deep learning library, and give high performance. The official Databricks notebook demonstrates featurization with a pre-trained TensorFlow model using pandas UDFs. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Related Concepts

- Featurization
- [Transfer Learning](/concepts/transfer-learning.md)
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md)
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)
- TensorFlow
- PyTorch
- [Scalar Iterator pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md)

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
