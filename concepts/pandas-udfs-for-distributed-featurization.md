---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee1cca51c857178624cba1f664435e77cca753b1ab28d08e41d99c8d23213235
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-udfs-for-distributed-featurization
    - PUFDF
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Pandas UDFs for Distributed Featurization
description: Using pandas UDFs (and Scalar Iterator pandas UDFs) on Databricks to apply pre-trained deep learning models across a cluster for scalable, distributed feature computation.
tags:
  - databricks
  - pandas-udfs
  - distributed-computing
  - feature-engineering
timestamp: "2026-06-19T18:49:08.832Z"
---

# Pandas UDFs for Distributed Featurization

**Pandas UDFs for Distributed Featurization** refers to the use of pandas user-defined functions (UDFs) in Apache Spark to compute feature vectors from pre-trained deep learning models at scale across a Databricks cluster. This technique enables efficient transfer learning by distributing the computation of feature representations across multiple nodes. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Overview

Featurization is a powerful method for [Transfer Learning](/concepts/transfer-learning.md), where knowledge from one problem domain is reused in a related domain. By computing features using a pre-trained deep learning model, you transfer knowledge about good features from the original domain to a new task. ^[featurization-for-transfer-learning-databricks-on-aws.md]

Databricks supports featurization at scale by distributing the computation across a cluster. You can perform featurization with deep learning libraries included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), such as TensorFlow and PyTorch. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Workflow

To compute features for transfer learning using pandas UDFs, follow this general workflow:

1. **Start with a pre-trained deep learning model** — for example, an image classification model from `tensorflow.keras.applications`. ^[featurization-for-transfer-learning-databricks-on-aws.md]
2. **Truncate the last layer(s)** of the model so that the modified model produces a tensor of features as output, rather than a prediction. ^[featurization-for-transfer-learning-databricks-on-aws.md]
3. **Apply the model to a new dataset** from a different problem domain, computing features for each input record. ^[featurization-for-transfer-learning-databricks-on-aws.md]
4. **Use the computed features** to train a new downstream model, such as logistic regression. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Advantages of pandas UDFs

pandas UDFs, and their newer variant [Scalar Iterator pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md), offer several advantages for featurization:

- **Flexible APIs** — pandas UDFs can work with any deep learning library, not just a single framework. ^[featurization-for-transfer-learning-databricks-on-aws.md]
- **High performance** — They are optimized for distributed execution across Spark clusters. ^[featurization-for-transfer-learning-databricks-on-aws.md]
- **Scalability** — The computation is distributed across the cluster, enabling processing of large datasets that would be impractical on a single machine. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Implementation Details

When implementing featurization with pandas UDFs:

- The pre-trained model is loaded and modified once per executor, typically within a UDF initialization step.
- Each executor processes batches of input data, applying the model to generate feature vectors.
- The resulting feature vectors can be stored as new columns in a [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) for downstream training.

## Related Concepts

- [Transfer Learning](/concepts/transfer-learning.md) — The broader technique of reusing knowledge from one problem domain in a related domain
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The ML-optimized runtime that supports deep learning libraries like TensorFlow and PyTorch
- [Scalar Iterator pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) — The newer variant of pandas UDFs with improved performance characteristics
- [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) — The distributed data structure used to store and process feature vectors
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The broader discipline of creating features for machine learning models

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
