---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00cdc85ed9ae43c77c0086e233b7498b25da857e0cc2349ce738169ac259f282
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-truncation-for-feature-extraction
    - MTFFE
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Model Truncation for Feature Extraction
description: The technique of removing the final classification layers of a pre-trained deep learning model so that it outputs feature tensors instead of predictions, enabling use as a feature extractor.
tags:
  - deep-learning
  - model-architecture
  - transfer-learning
timestamp: "2026-06-19T18:49:02.343Z"
---

# Model Truncation for Feature Extraction

**Model Truncation for Feature Extraction** is a technique used in [Transfer Learning](/concepts/transfer-learning.md) where the final layers of a pre-trained deep learning model are removed (truncated) so that the model outputs a tensor of features rather than a final prediction. This modified model can then be applied to new datasets to compute feature representations for downstream tasks.

## Overview

Pre-trained deep learning models, such as image classification models from `tensorflow.keras.applications`, are typically designed to produce predictions for specific tasks. By truncating the last layer(s) of these models, the output becomes a feature vector that captures learned representations from the original domain. ^[featurization-for-transfer-learning-databricks-on-aws.md]

This approach is closely related to [Transfer Learning](/concepts/transfer-learning.md), a technique that allows knowledge from one problem domain to be reused in a related domain. Feature extraction through model truncation is itself a simple and powerful method for transfer learning: computing features using a pre-trained model transfers knowledge about good feature representations from the original domain to a new problem. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Workflow

The typical workflow for model truncation in feature extraction involves the following steps:

1. **Start with a pre-trained deep learning model** — for example, an image classification model from `tensorflow.keras.applications`.
2. **Truncate the last layer(s) of the model** — the modified model produces a tensor of features as output, rather than a prediction.
3. **Apply the truncated model to a new dataset** — compute features for data from a different problem domain.
4. **Use the extracted features to train a new model** — the features serve as input to a downstream model such as logistic regression.

^[featurization-for-transfer-learning-databricks-on-aws.md]

## Implementation on Databricks

Databricks supports featurization with deep learning models at scale, distributing the computation across a cluster. You can perform featurization with deep learning libraries included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), including TensorFlow and PyTorch. ^[featurization-for-transfer-learning-databricks-on-aws.md]

### Using pandas UDFs

A common approach for implementing model truncation for feature extraction on Databricks is to use pandas UDFs (User-Defined Functions). pandas UDFs, and their newer variant [Scalar Iterator pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md), offer flexible APIs, support any deep learning library, and give high performance for distributed feature computation. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Related Concepts

- [Transfer Learning](/concepts/transfer-learning.md) — The broader technique of reusing knowledge from one domain in a related domain
- Featurization — The process of computing feature representations from data
- Pre-trained Models — Models trained on large datasets that can be adapted for new tasks
- TensorFlow — A deep learning framework commonly used for model truncation
- PyTorch — An alternative deep learning framework for feature extraction
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The Databricks environment that includes deep learning libraries

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
