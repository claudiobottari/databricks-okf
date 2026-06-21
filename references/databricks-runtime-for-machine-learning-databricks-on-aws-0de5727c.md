---
title: Databricks Runtime for Machine Learning | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml
ingestedAt: "2026-06-18T08:09:59.688Z"
---

This page describes the Databricks Runtime for Machine Learning and provides guidance for how to create a classic compute resource that uses it.

## What is Databricks Runtime for Machine Learning?[​](#what-is-databricks-runtime-for-machine-learning "Direct link to what-is-databricks-runtime-for-machine-learning")

Databricks Runtime for Machine Learning (Databricks Runtime ML) automates the creation of a compute resource with pre-built machine learning and deep learning infrastructure including the most common ML and DL libraries.

## Libraries included in Databricks Runtime ML[​](#libraries-included-in-databricks-runtime-ml "Direct link to Libraries included in Databricks Runtime ML")

Databricks Runtime ML includes a variety of popular ML libraries. The libraries are updated with each release to include new features and fixes.

Databricks has designated a subset of the supported libraries as top-tier libraries. For these libraries, Databricks provides a faster update cadence, updating to the latest package releases with each runtime release (barring dependency conflicts). Databricks also provides advanced support, testing, and embedded optimizations for top-tier libraries. Top-tier libraries are added or removed only with major releases.

*   For a full list of top-tier and other provided libraries, see the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/) for Databricks Runtime ML.
*   For information about how often libraries are updated and when libraries are deprecated, see [Databricks Runtime ML maintenance policy](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml-maintenance).

You can install additional libraries to create a custom environment for your notebook or compute resource.

*   To make a library available for all notebooks running on a compute resource, [create a compute-scoped library](https://docs.databricks.com/aws/en/libraries/cluster-libraries#install-libraries). You can also use an [init script](https://docs.databricks.com/aws/en/init-scripts/cluster-scoped) to install libraries during compute creation.
*   To install a library that is available only to a specific notebook session, use [Notebook-scoped Python libraries](https://docs.databricks.com/aws/en/libraries/notebooks-python-libraries).

## Create a compute resource with Databricks Runtime for ML[​](#create-a-compute-resource-with-databricks-runtime-for-ml "Direct link to create-a-compute-resource-with-databricks-runtime-for-ml")

To create a compute resource that uses Databricks Runtime for ML, select the **Machine learning** checkbox in the create compute UI. This automatically sets the access mode to **Dedicated** with your account as the dedicated user. You can manually assign the compute resource to a different user or group in the **Advanced** section of the create compute UI.

For GPU-based compute, select a GPU-enabled instance type in the **Worker type** drop-down menu. For the complete list of supported GPU types, see [Supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list).

### Photon and Databricks Runtime ML[​](#photon-and-databricks-runtime-ml "Direct link to Photon and Databricks Runtime ML")

When you create a compute resource that runs Databricks Runtime 15.2 ML or above, you can choose to enable [Photon](https://docs.databricks.com/aws/en/compute/photon). Photon improves performance for applications using Spark SQL, Spark DataFrames, feature engineering, GraphFrames, and xgboost4j. It is not expected to improve performance on applications using Spark RDDs, Pandas UDFs, and non-JVM languages such as Python. Thus, Python packages such as XGBoost, PyTorch, and TensorFlow will not see an improvement with Photon.

Spark RDD APIs and [Spark MLlib](https://docs.databricks.com/aws/en/machine-learning/train-model/mllib) have limited compatibility with Photon. When processing large datasets using Spark RDD or Spark MLlib, you may experience Spark memory issues. See [Spark memory issues](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/spark-memory-issues).

### Databricks Runtime ML on AWS Graviton instances[​](#databricks-runtime-ml-on-aws-graviton-instances "Direct link to databricks-runtime-ml-on-aws-graviton-instances")

Databricks Runtime 15.4 LTS ML and above support [Graviton instance types](https://docs.databricks.com/aws/en/compute/configure#graviton). Using Graviton instance types can improve performance for Spark, Photon, feature engineering, machine learning libraries such as XGBoost and LightGBM, and Spark MLlib algorithms for gradient boosting. Graviton instances may also provide better price-to-performance value than other AWS EC2 instance types.

## Compute access mode for Databricks Runtime ML[​](#compute-access-mode-for-databricks-runtime-ml "Direct link to compute-access-mode-for-databricks-runtime-ml")

To access data in Unity Catalog on a compute resource running Databricks Runtime ML, you must set the access mode to [Dedicated](https://docs.databricks.com/aws/en/compute/dedicated-overview). The access mode is automatically set in the create compute UI when you select the **Machine learning** checkbox.

When a compute resource has **Dedicated** access mode, the resource can be assigned to a single user or a group. When assigned to a group, the user's permissions automatically down-scope to the group's permissions, allowing the user to securely share the resource with other members of the group.

When using dedicated access mode, the following features are only available on Databricks Runtime 15.4 LTS ML and above:

*   [Fine-grained access control](https://docs.databricks.com/aws/en/compute/single-user-fgac).
*   [Querying tables that were created using Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/compute/single-user-fgac), including [streaming tables](https://docs.databricks.com/aws/en/ldp/concepts/streaming-tables) and [materialized views](https://docs.databricks.com/aws/en/ldp/concepts/materialized-views).

## Train models[​](#train-models "Direct link to Train models")

The following resources show you how to train machine learning and AI models.

Databricks Model Training streamlines and unifies the process of training and deploying traditional ML models through AutoML and Foundation Model Fine-tuning workloads.

### AutoML[​](#automl "Direct link to AutoML")

[AutoML](https://docs.databricks.com/aws/en/machine-learning/automl/) simplifies the process of applying machine learning to your datasets by automatically finding the best algorithm and hyperparameter configuration. AutoML offers a no-code UI as well as a Python API.

### Foundation Model Fine-tuning[​](#foundation-model-fine-tuning "Direct link to Foundation Model Fine-tuning")

[Foundation Model Fine-tuning](https://docs.databricks.com/aws/en/large-language-models/foundation-model-training/) (now part of Databricks Model Training) on Databricks lets you customize large language models (LLMs) using your own data. This process involves fine-tuning the training of a pre-existing foundation model, significantly reducing the data, time, and compute resources required compared to training a model from scratch. Key features include:

*   **Instruction fine-tuning:** Adapt your model to new tasks by training on structured prompt-response data.
*   **Continued pre-training:** Enhance your model with additional text data to add new knowledge or focus on a specific domain.
*   **Chat completion:** Train your model on chat logs to improve conversational abilities.

### Open source library examples[​](#open-source-library-examples "Direct link to Open source library examples")

See [machine learning training examples](https://docs.databricks.com/aws/en/machine-learning/train-model/training-examples) from a wide variety of open source machine learning libraries, including hyperparameter tuning examples using Optuna and Hyperopt.

### Deep learning[​](#deep-learning "Direct link to Deep learning")

See examples and best practices for [distributed deep learning training](https://docs.databricks.com/aws/en/machine-learning/train-model/deep-learning) to develop and fine-tune deep learning models on Databricks.

### Recommenders[​](#recommenders "Direct link to Recommenders")

Learn how to train [deep-learning-based recommendation models](https://docs.databricks.com/aws/en/machine-learning/train-recommender-models) on Databricks. Compared to traditional recommendation models, deep learning models can achieve higher quality results and scale to larger amounts of data.
