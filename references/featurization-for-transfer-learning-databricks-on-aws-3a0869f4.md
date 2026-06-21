---
title: Featurization for transfer learning | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/preprocess-data/transfer-learning-tensorflow
ingestedAt: "2026-06-18T08:12:57.515Z"
---

This article provides an example of doing featurization for transfer learning using pandas UDFs.

## Featurization for transfer learning in DL models[​](#featurization-for-transfer-learning-in-dl-models "Direct link to Featurization for transfer learning in DL models")

Databricks supports featurization with deep learning models. Pre-trained deep learning models can be used to compute features for use in other downstream models. Databricks supports featurization at scale, distributing the computation across a cluster. You can perform featurization with deep learning libraries included in [Databricks Runtime ML](https://docs.databricks.com/aws/en/machine-learning/), including TensorFlow and PyTorch.

Databricks also supports [transfer learning](https://en.wikipedia.org/wiki/Transfer_learning), a technique closely related to featurization. Transfer learning allows you to reuse knowledge from one problem domain in a related domain. Featurization is itself a simple and powerful method for transfer learning: computing features using a pre-trained deep learning model transfers knowledge about good features from the original domain.

## Steps to compute features for transfer learning[​](#steps-to-compute-features-for-transfer-learning "Direct link to Steps to compute features for transfer learning")

This article demonstrates how to compute features for transfer learning using a pre-trained TensorFlow model, using the following workflow:

1.  Start with a pre-trained deep learning model, in this case an image classification model from `tensorflow.keras.applications`.
2.  Truncate the last layer(s) of the model. The modified model produces a tensor of features as output, rather than a prediction.
3.  Apply that model to a new image dataset from a different problem domain, computing features for the images.
4.  Use these features to train a new model. The following notebook omits this final step. For examples of training a simple model such as logistic regression, see [Train AI and ML models](https://docs.databricks.com/aws/en/machine-learning/train-model/).

## Example: Use pandas UDFs for featurization[​](#example-use-pandas-udfs-for-featurization "Direct link to Example: Use pandas UDFs for featurization")

The following notebook uses [pandas UDFs](https://docs.databricks.com/aws/en/udf/pandas) to perform the featurization step. pandas UDFs, and their newer variant [Scalar Iterator pandas UDFs](https://docs.databricks.com/aws/en/udf/pandas#scalar-iterator-udfs), offer flexible APIs, support any deep learning library, and give high performance.

#### Featurization and transfer learning with TensorFlow
