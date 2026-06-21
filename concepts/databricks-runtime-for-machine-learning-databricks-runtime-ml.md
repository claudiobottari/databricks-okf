---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b20901302ab891692d65cbbe4e5135628d86144352bb4d0cab14759da3040b4
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-for-machine-learning-databricks-runtime-ml
    - DRFML(RM
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Databricks Runtime for Machine Learning (Databricks Runtime ML)
description: A pre-configured Databricks runtime environment that automates compute resource creation with built-in machine learning and deep learning libraries and tools.
tags:
  - databricks
  - machine-learning
  - runtime
timestamp: "2026-06-18T11:41:50.312Z"
---

# Databricks Runtime for Machine Learning (Databricks Runtime ML)

**Databricks Runtime for Machine Learning (Databricks Runtime ML)** automates the creation of a compute resource with pre-built machine learning and deep learning infrastructure, including the most common ML and DL libraries. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Libraries Included in Databricks Runtime ML

Databricks Runtime ML includes a variety of popular ML libraries. The libraries are updated with each release to include new features and fixes. A subset of the supported libraries are designated as **top-tier libraries** — Databricks provides a faster update cadence for these, updating to the latest package releases with each runtime release (barring dependency conflicts), along with advanced support, testing, and embedded optimizations. Top-tier libraries are added or removed only with major releases. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- For a full list of top‑tier and other provided libraries, see the release notes for Databricks Runtime ML.
- For information about library update cadence and deprecation, see the Databricks Runtime ML maintenance policy.

You can install additional libraries to create a custom environment for your notebook or compute resource. To make a library available for all notebooks running on a compute resource, [create a compute‑scoped library](https://docs.databricks.com/aws/en/libraries/cluster-libraries#install-libraries) or use an [init script](https://docs.databricks.com/aws/en/init-scripts/cluster-scoped). To install a library for only a specific notebook session, use notebook‑scoped Python libraries. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Create a Compute Resource with Databricks Runtime for ML

To create a compute resource that uses Databricks Runtime for ML, select the **Machine learning** checkbox in the create‑compute UI. This automatically sets the access mode to **Dedicated** with your account as the dedicated user. You can manually assign the compute resource to a different user or group in the **Advanced** section. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

For GPU‑based compute, select a GPU‑enabled instance type in the **Worker type** drop‑down menu. The complete list of supported GPU types is available in the documentation on supported instance types. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Photon and Databricks Runtime ML

When you create a compute resource that runs Databricks Runtime **15.2 ML** or above, you can choose to enable Photon. Photon improves performance for applications using Spark SQL, Spark DataFrames, feature engineering, GraphFrames, and `xgboost4j`. It is not expected to improve performance for applications using Spark RDDs, Pandas UDFs, or non‑JVM languages such as Python — therefore Python packages such as XGBoost, PyTorch, and TensorFlow will not see an improvement with Photon. Spark RDD APIs and [Spark MLlib](/concepts/apache-spark-mllib.md) have limited compatibility with Photon; processing large datasets with Spark RDD or MLlib may cause Spark memory issues. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Databricks Runtime ML on AWS Graviton Instances

Databricks Runtime **15.4 LTS ML** and above support Graviton instance types. Using Graviton instance types can improve performance for Spark, Photon, feature engineering, ML libraries such as XGBoost and LightGBM, and Spark MLlib algorithms for gradient boosting. Graviton instances may also provide a better price‑to‑performance ratio than other AWS EC2 instance types. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Compute Access Mode for Databricks Runtime ML

To access data in [Unity Catalog](/concepts/unity-catalog.md) on a compute resource running Databricks Runtime ML, you must set the access mode to **Dedicated**. The access mode is automatically set when you select the **Machine learning** checkbox. In Dedicated mode, the resource can be assigned to a single user or a group. When assigned to a group, the user’s permissions automatically down‑scope to the group’s permissions, allowing secure sharing of the resource with other group members. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

When using Dedicated access mode, the following features are only available on Databricks Runtime 15.4 LTS ML and above:

- Fine‑grained access control.
- Querying tables created using Lakeflow Spark Declarative Pipelines, including streaming tables and materialized views.

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Train Models

Databricks Model Training streamlines and unifies the process of training and deploying traditional ML models through AutoML and Foundation Model Fine‑tuning workloads. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### AutoML

AutoML simplifies applying machine learning to your datasets by automatically finding the best algorithm and hyperparameter configuration. It offers a no‑code UI and a Python API. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Foundation Model Fine‑tuning

[Foundation Model Fine‑tuning](/concepts/foundation-model-fine-tuning-databricks.md) (part of Databricks Model Training) lets you customize large language models (LLMs) using your own data. It significantly reduces the data, time, and compute resources required compared to training from scratch. Key features include:

- **Instruction fine‑tuning:** Adapt models to new tasks using structured prompt‑response data.
- **Continued pre‑training:** Enhance the model with additional text data to add new knowledge or focus on a specific domain.
- **Chat completion:** Train on chat logs to improve conversational abilities.

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Open Source Library Examples

See machine learning training examples from a wide variety of open source ML libraries, including hyperparameter tuning examples using Optuna and Hyperopt. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Deep Learning

Find examples and best practices for distributed deep learning training to develop and fine‑tune deep learning models on Databricks. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Recommenders

Learn how to train deep‑learning‑based recommendation models on Databricks. Compared to traditional recommendation models, deep learning models can achieve higher quality results and scale to larger amounts of data. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- Databricks Runtime
- Photon
- [Unity Catalog](/concepts/unity-catalog.md)
- [Dedicated access mode](/concepts/dedicated-access-mode-for-ml-compute.md)
- [Spark MLlib](/concepts/apache-spark-mllib.md)
- AutoML
- [Foundation Model Fine‑tuning](/concepts/foundation-model-fine-tuning-databricks.md)
- Deep learning
- Recommender models
- Machine learning training examples

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
