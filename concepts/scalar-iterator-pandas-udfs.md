---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41830947223b7ecc174be4834e82f31cc096d1d4c2ead38336601f712116ce6b
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - scalar-iterator-pandas-udfs
    - SIPU
    - Pandas UDFs
    - Scalar Iterator UDFs|scalar iterator variant
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Scalar Iterator pandas UDFs
description: A newer variant of pandas UDFs that offers flexible APIs, support for any deep learning library, and high performance for featurization tasks in distributed Spark environments.
tags:
  - pandas
  - spark
  - udf
  - performance
timestamp: "2026-06-19T10:32:10.664Z"
---

Based on the provided source material, here is the wiki page for "Scalar Iterator pandas UDFs".

---

**Scalar Iterator pandas UDFs** are a variant of pandas user-defined functions (UDFs) in Apache Spark that offer flexible APIs, support any deep learning library, and give high performance. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Overview

Scalar Iterator pandas UDFs are part of the pandas UDFs framework. They are designed to process data in batches, as opposed to the standard row-at-a-time processing of regular UDFs. This batching allows for significant performance improvements, especially when used with deep learning models that are optimized for batch processing. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Key Features

- **Flexible API**: They provide a flexible interface for implementing custom logic. ^[featurization-for-transfer-learning-databricks-on-aws.md]
- **Library Support**: They work with any deep learning library, including TensorFlow and PyTorch. ^[featurization-for-transfer-learning-databricks-on-aws.md]
- **High Performance**: The batching capability leads to high performance by allowing the deep learning model to process multiple inputs simultaneously. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Use Cases

Scalar Iterator pandas UDFs are particularly useful for featurization for [Transfer Learning](/concepts/transfer-learning.md) in deep learning models. A common workflow involves:

1.  **Starting with a pre-trained model**: For example, an image classification model from `tensorflow.keras.applications`. ^[featurization-for-transfer-learning-databricks-on-aws.md]
2.  **Modifying the model**: The last layer(s) of the model are truncated to produce a tensor of features as output rather than a prediction. ^[featurization-for-transfer-learning-databricks-on-aws.md]
3.  **Applying the model at scale**: The modified model is applied to a new dataset, computing features for the data. ^[featurization-for-transfer-learning-databricks-on-aws.md]
4.  **Using the features**: These computed features can be used to train a new downstream model. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Related Concepts

- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md)
- Featurization
- [Transfer Learning](/concepts/transfer-learning.md)
- TensorFlow
- PyTorch

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
