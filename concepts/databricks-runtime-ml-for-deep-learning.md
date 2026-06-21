---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5b6e693c34adc667865fb6d3265504a5185aa51975ca5ca94b36375d9b77b65
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-for-deep-learning
    - DRMFDL
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Databricks Runtime ML for Deep Learning
description: Databricks Runtime ML includes deep learning libraries such as TensorFlow and PyTorch, and supports featurization at scale by distributing computation across clusters.
tags:
  - databricks
  - machine-learning
  - deep-learning
timestamp: "2026-06-19T18:49:07.543Z"
---

# Databricks Runtime ML for Deep Learning

**Databricks Runtime ML** is a pre-configured machine learning environment on the Databricks platform that includes deep learning libraries and tools for building, training, and deploying deep learning models. It provides an optimized runtime for deep learning workloads, including support for distributed training and inference at scale. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Included Deep Learning Libraries

Databricks Runtime ML includes popular deep learning frameworks such as **TensorFlow** and **PyTorch**, enabling users to work with these libraries directly on their clusters without additional installation or configuration. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Featurization and Transfer Learning

Databricks Runtime ML supports **featurization** with deep learning models at scale. Pre-trained deep learning models can be used to compute feature representations for new datasets, distributing the computation across a cluster using pandas UDFs (user-defined functions). ^[featurization-for-transfer-learning-databricks-on-aws.md]

This process is closely related to [Transfer Learning](/concepts/transfer-learning.md), where knowledge from one problem domain is reused in a related domain. A common workflow is:

1. Start with a pre-trained deep learning model (e.g., an image classifier from `tensorflow.keras.applications`).
2. Truncate the last layer(s) so the model outputs feature tensors instead of predictions.
3. Apply the modified model to a new dataset to compute features.
4. Use those features to train a downstream model (e.g., logistic regression). ^[featurization-for-transfer-learning-databricks-on-aws.md]

Featurization is itself a simple but powerful method for transfer learning, because the pre-trained model transfers knowledge about good features from its original domain. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Performance and Scalability

For featurization workflows, Databricks recommends using **pandas UDFs** or their newer variant **Scalar Iterator pandas UDFs**. These APIs offer flexible interfaces, work with any deep learning library, and provide high performance when applied to large distributed datasets. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Related Concepts

- pandas UDFs – Distributed computation via user-defined functions
- [Transfer Learning](/concepts/transfer-learning.md) – Reusing knowledge between domains
- TensorFlow – Deep learning framework included in Databricks Runtime ML
- PyTorch – Deep learning framework included in Databricks Runtime ML
- Featurization – Computing features using pre-trained models
- Databricks Machine Learning – Broader ML platform
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Scaling deep learning across clusters

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
