---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8cfa9f00b9272e5239231f0cd43ea372cc258984e8ab3ca15ddcfb0592b8626a
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-trained-model-truncation-for-feature-extraction
    - PMTFFE
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Pre-trained Model Truncation for Feature Extraction
description: The technique of removing the final classification layers from a pre-trained deep learning model so that the model outputs feature tensors instead of predictions, which can then be used as inputs to new models.
tags:
  - deep-learning
  - feature-engineering
  - model-adaptation
timestamp: "2026-06-19T10:31:55.573Z"
---

# Pre-trained Model Truncation for Feature Extraction

**Pre-trained Model Truncation for Feature Extraction** is a technique used in featurization and [Transfer Learning](/concepts/transfer-learning.md) where the last layer(s) of a pre-trained deep learning model are removed (truncated), causing the model to output intermediate feature representations instead of predictions. These features can then be used as input for other downstream models or tasks.

## Overview

Featurization with deep learning models allows practitioners to reuse knowledge captured by a model trained on one domain to compute useful features for a different, related domain. Databricks supports featurization at scale by distributing the computation across a cluster using libraries such as TensorFlow and PyTorch, both included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). Truncating the final layers of a pre-trained model is a straightforward and powerful method for transfer learning: the pre-trained model already encodes good feature representations, and truncation exposes those features without the model’s original classification or regression head. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## How It Works

1. **Start with a pre-trained deep learning model** — for example, an image classification model from `tensorflow.keras.applications`.
2. **Truncate the last layer(s)** — the modified model no longer produces a class prediction; instead it returns a tensor of features as output.
3. **Apply the truncated model to a new dataset** from a different problem domain, computing features for each input.
4. **Use the computed features to train a new, simpler model** (e.g., logistic regression). The source notes that this final training step is omitted from the provided notebook example. ^[featurization-for-transfer-learning-databricks-on-aws.md]

The truncated model acts as a fixed feature extractor: the pre-trained weights remain frozen, and only the new downstream model is trained on the extracted features.

## Implementation with Pandas UDFs

Databricks recommends using pandas UDFs (or the newer [Scalar Iterator pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md)) to apply the truncated model across large datasets in a distributed manner. Pandas UDFs provide a flexible API that works with any deep learning library and deliver high performance on Spark clusters. The documented notebook example demonstrates this featurization workflow on an image dataset using TensorFlow, but the same pattern can be adapted for other frameworks and data types. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Benefits

- **Reusability**: A single pre-trained model can generate features for many different downstream tasks without retraining.
- **Transfer learning**: Knowledge from the original training domain is effectively transferred to a new domain with minimal additional compute.
- **Scale**: Pandas UDFs allow the feature extraction to be parallelized across a cluster, handling datasets that would be too large for a single machine.
- **Flexibility**: The approach works with any deep learning library supported by Databricks Runtime ML, including TensorFlow and PyTorch.

## Related Concepts

- [Transfer Learning](/concepts/transfer-learning.md) — The broader technique of reusing a model trained on one task for a related task.
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) — The distributed execution mechanism used in the Databricks example.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The preconfigured runtime that includes deep learning frameworks and GPU support.
- Featurization — The general process of transforming raw data into numerical features for machine learning.

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
