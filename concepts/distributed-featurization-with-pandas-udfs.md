---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a52e7d204d26a54a4ed2705584b8eae6d650dd3cd653fa48493d1700f60029e3
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-featurization-with-pandas-udfs
    - DFWPU
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Distributed Featurization with Pandas UDFs
description: A pattern for scaling featurization computations across a Spark cluster by using pandas UDFs (including Scalar Iterator pandas UDFs) to apply pre-trained deep learning models to large datasets in a distributed manner.
tags:
  - databricks
  - spark
  - pandas
  - distributed-computing
timestamp: "2026-06-19T10:31:50.962Z"
---

```markdown
---
title: Distributed Featurization with Pandas UDFs
summary: Using pandas UDFs on Apache Spark to distribute featurization computations across a cluster for scalable inference with deep learning models.
sources:
  - featurization-for-transfer-learning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:19:58.047Z"
updatedAt: "2026-06-18T12:19:58.047Z"
tags:
  - distributed-computing
  - spark
  - pandas-udf
  - deep-learning
aliases:
  - distributed-featurization-with-pandas-udfs
  - DFWPU
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Distributed Featurization with Pandas UDFs

**Distributed Featurization with Pandas UDFs** is a technique for computing feature vectors at scale using pre-trained deep learning models. By combining pandas UDFs (and their [[Scalar Iterator pandas UDFs]] variant) with distributed computing, you can apply a deep learning model to large datasets across a cluster, extracting meaningful features for downstream tasks such as [[transfer learning]] or model training.

## Overview

Databricks supports featurization with deep learning models, distributing the computation across a cluster. Pre-trained deep learning models — including those from TensorFlow and PyTorch — can be used to compute features for use in other downstream models. ^[featurization-for-transfer-learning-databricks-on-aws.md]

Featurization is itself a simple and powerful method for transfer learning: computing features using a pre-trained deep learning model transfers knowledge about good features from the original problem domain to a related domain. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## How It Works

The general workflow for distributed featurization with pandas UDFs is:

1. Start with a pre-trained deep learning model (e.g., an image classification model from `tensorflow.keras.applications`).
2. Truncate the last layer(s) of the model so that the output is a tensor of features rather than a prediction.
3. Use a pandas UDF to apply this modified model to a distributed Spark DataFrame containing the input data (e.g., image paths or raw pixels).
4. The resulting feature columns can then be used to train a simpler model, such as a logistic regression classifier.

Databricks Runtime ML includes the necessary deep learning libraries (TensorFlow, PyTorch) and Spark integration to run these UDFs across cluster nodes. ^[featurization-for-transfer-learning-databricks-on-aws.md]

### Why Pandas UDFs?

Pandas UDFs and their newer variant Scalar Iterator pandas UDFs offer flexible APIs, support any deep learning library, and give high performance. They allow you to load a model once per batch of rows and apply it efficiently, making them well suited for distributed featurization workloads. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Workflow Steps

The following steps outline the typical approach for distributed featurization using pandas UDFs:

1. **Load a pre-trained model** — Obtain a deep learning model that outputs feature embeddings (after removing the classification head).
2. **Define a pandas UDF** — Write a Python function that takes a pandas Series or DataFrame of inputs (e.g., image arrays or file paths), preprocesses them, runs inference through the truncated model, and returns a pandas Series or DataFrame of feature vectors.
3. **Apply the UDF to a Spark DataFrame** — Use `df.withColumn("features", feature_udf("input_column"))` to distribute the featurization across the cluster.
4. **Train a downstream model** — Use the generated features as input to a logistic regression or other classifier.

Databricks provides example notebooks that demonstrate this pattern, including featurization and transfer learning with TensorFlow. ^[featurization-for-transfer-learning-databricks-on-aws.md]

> **Note**: The final training step is not shown in the example notebook referenced in the source material, but it follows standard model training practices. See Train AI and ML models for examples.

## Example: Featurization and Transfer Learning with TensorFlow

The source material includes a notebook titled **Featurization and transfer learning with TensorFlow**. This notebook demonstrates how to:

- Load a pre-trained TensorFlow Keras model (e.g., ResNet50 or MobileNet).
- Remove the final classification layers to obtain a feature extractor.
- Use a pandas UDF to featurize a Spark DataFrame containing images.
- Collect the resulting feature DataFrame for use in a subsequent model.

The notebook is designed to run on [[Databricks Runtime ML]], which provides the required deep learning libraries and Spark pandas UDF support. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Related Concepts

- pandas UDFs — User-defined functions that operate on pandas DataFrames and are distributed by Spark
- [[Scalar Iterator pandas UDFs]] — An optimized variant of pandas UDFs for batch processing
- [[transfer learning]] — Reusing knowledge from one domain in a related domain
- deep learning — Neural network models that can be used as feature extractors
- [[Databricks Runtime ML]] — The ML-optimized runtime that bundles TensorFlow, PyTorch, and Spark
- TensorFlow / PyTorch — Deep learning frameworks supported for featurization
- [[FeatureEngineeringClient API|feature engineering]] — The broader practice of creating input features for machine learning

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md
```

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
