---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bfdbe26154ccce7b500c7d27b69691093eede26075a8471505640e250a700de
  pageDirectory: concepts
  sources:
    - featurization-for-transfer-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - transfer-learning
  citations:
    - file: featurization-for-transfer-learning-databricks-on-aws.md
title: Transfer Learning
description: A machine learning technique that reuses knowledge from a pre-trained model on one problem domain to improve learning in a related domain, with featurization being one simple and powerful method for achieving it.
tags:
  - machine-learning
  - deep-learning
timestamp: "2026-06-19T10:31:46.927Z"
---

---
title: Transfer Learning
summary: A machine learning technique that reuses knowledge from one problem domain in a related domain, commonly implemented via featurization with pre-trained deep learning models.
sources:
  - featurization-for-transfer-learning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:20:03.236Z"
updatedAt: "2026-06-18T12:20:03.236Z"
tags:
  - machine-learning
  - deep-learning
  - knowledge-transfer
aliases:
  - transfer-learning
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Transfer Learning

**Transfer learning** is a machine learning technique that reuses knowledge gained from solving one problem domain and applies it to a different, related domain. ^[featurization-for-transfer-learning-databricks-on-aws.md] It is closely related to featurization, and featurization itself is a simple and powerful method for transfer learning: computing features using a pre-trained deep learning model transfers knowledge about good representations from the original domain to the target domain. ^[featurization-for-transfer-learning-databricks-on-aws.md]

## Featurization for Transfer Learning

Databricks supports featurization with deep learning models, distributing the computation across a cluster for scalability. ^[featurization-for-transfer-learning-databricks-on-aws.md] You can perform featurization using the deep learning libraries included in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), such as TensorFlow and PyTorch. ^[featurization-for-transfer-learning-databricks-on-aws.md]

The typical workflow to compute features for transfer learning is: ^[featurization-for-transfer-learning-databricks-on-aws.md]

1. **Start with a pre-trained model** – obtain a model from `tensorflow.keras.applications`, PyTorch Hub, or another source.
2. **Truncate the last layer(s)** – remove the model’s prediction head so the output becomes a feature tensor rather than a class label.
3. **Apply the truncated model to a new dataset** – compute feature vectors for the target data.
4. **Train a new model** using the computed features (for example, a logistic regression classifier).

## Example: Using Pandas UDFs

Databricks recommends using [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) (and their newer [Scalar Iterator UDFs|scalar iterator variant](/concepts/scalar-iterator-pandas-udfs.md)) to perform the featurization step, as they offer flexible APIs, support any deep learning library, and give high performance. ^[featurization-for-transfer-learning-databricks-on-aws.md] The following notebook illustrates the process using a pre-trained TensorFlow image classifier:

```python
# (Conceptual example – see the full notebook in the documentation)
from tensorflow.keras.applications import ResNet50
base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Define a pandas UDF that applies the model to image content
# and returns feature vectors for downstream training.
```

The complete notebook is linked in the Databricks documentation.

## Related Concepts

- Featurization – The process of extracting meaningful features using pre-trained models.
- Deep Learning – The class of models most commonly used for transfer learning.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime that includes pre-installed deep learning frameworks.
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) – A Spark API for vectorized operations that can distribute model inference.
- Image Classification – A common source domain for transfer learning.

## Sources

- featurization-for-transfer-learning-databricks-on-aws.md

# Citations

1. [featurization-for-transfer-learning-databricks-on-aws.md](/references/featurization-for-transfer-learning-databricks-on-aws-3a0869f4.md)
