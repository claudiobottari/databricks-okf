---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c6567f742cf4a9a1bb875a85e4958ffca8185b9e83c60cd2dbdd3e742086484
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featurization-for-transfer-learning
    - FFTL
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Featurization for Transfer Learning
description: Using pre-trained deep learning models to compute feature vectors from data, which can then be used as input for downstream models in a different problem domain.
tags:
  - transfer-learning
  - feature-engineering
  - deep-learning
timestamp: "2026-06-19T18:49:18.220Z"
---

# Featurization for Transfer Learning

**Featurization for Transfer Learning** is a technique that uses pre-trained deep learning models to compute feature representations from data, which can then be used to train downstream models for related tasks. This approach is a simple yet powerful method for [Transfer Learning](/concepts/transfer-learning.md), enabling knowledge reuse across problem domains without requiring training from scratch. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Overview

Databricks supports featurization with deep learning models at scale, distributing the computation across a cluster. Pre-trained deep learning models can be used to compute features for use in other downstream models. Databricks supports featurization using deep learning libraries included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), including TensorFlow and PyTorch. ^[featurization-for-transfer-learning-databricks-on-aws.md]

Transfer learning is a technique closely related to featurization that allows you to reuse knowledge from one problem domain in a related domain. Featurization is itself a simple and powerful method for transfer learning: computing features using a pre-trained deep learning model transfers knowledge about good features from the original domain. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Workflow

The typical workflow for featurization for transfer learning follows these steps: ^[featurization-for-transfer-learning-databricks-on-aws.md]

1. **Start with a pre-trained deep learning model** — for example, an image classification model from `tensorflow.keras.applications`.
2. **Truncate the last layer(s)** of the model so that the modified model produces a tensor of features as output, rather than a prediction.
3. **Apply the model to a new dataset** from a different problem domain, computing feature representations for the data.
4. **Train a new model** using the computed features — for example, a simple model such as logistic regression.

## Using pandas UDFs for Featurization

Databricks recommends using pandas UDFs (user-defined functions) to perform the featurization step. pandas UDFs, and their newer variant [Scalar Iterator pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md), offer flexible APIs, support any deep learning library, and provide high performance for distributed computation. ^[featurization-for-transfer-learning-databricks-on-aws.md]

### Example: Featurization with TensorFlow

The following example demonstrates how to use pandas UDFs to compute features using a pre-trained TensorFlow model: ^[featurization-for-transfer-learning-databricks-on-aws.md]

```python
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import ArrayType, FloatType

# Load a pre-trained model without the top classification layer
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Define a pandas UDF that applies the model to batches of images
@pandas_udf(ArrayType(FloatType()))
def extract_features(image_batch: pd.Series) -> pd.Series:
    # Convert images to numpy array and preprocess
    images = np.stack(image_batch.values)
    processed = preprocess_input(images)
    
    # Compute features
    features = model.predict(processed, verbose=0)
    
    # Return as list of floats
    return pd.Series([feat.tolist() for feat in features])

# Apply the UDF to a Spark DataFrame containing images
df_with_features = df.select(
    extract_features(df.image_column).alias("features")
)
```

## Benefits

- **Knowledge reuse** — Leverages features learned from large datasets (e.g., ImageNet) without requiring extensive training data in the target domain. ^[featurization-for-transfer-learning-databricks-on-aws.md]
- **Distributed computation** — pandas UDFs distribute the featurization workload across cluster nodes, enabling processing of large datasets. ^[featurization-for-transfer-learning-databricks-on-aws.md]
- **Framework flexibility** — Supports any deep learning library available in Databricks Runtime ML, including TensorFlow and PyTorch. ^[featurization-for-transfer-learning-databricks-on-aws.md]
- **Simplified training** — The computed features can be used to train simpler models (such as logistic regression or random forests) that require less data and computational resources. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Related Concepts

- [Transfer Learning](/concepts/transfer-learning.md) — The broader technique of reusing knowledge across problem domains
- pandas UDFs — User-defined functions for distributed data processing in Spark
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The Databricks runtime that includes deep learning libraries
- TensorFlow — A deep learning framework supported for featurization
- PyTorch — A deep learning framework supported for featurization
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The broader practice of creating features for machine learning models
- [Model Training](/concepts/databricks-model-training.md) — The downstream step that uses computed features

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
