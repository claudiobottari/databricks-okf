---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0f131015758fe0b837825f7f37529916d24a6d6c2df6400af525d9d021f0330a
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
    - mlflow-api-reference-databricks-on-aws.md
    - train-ai-and-ml-models-databricks-on-aws.md
    - what-are-hugging-face-transformers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-for-machine-learning
    - DRFML
    - AI Runtime for Machine Learning
    - Databricks AI Runtime for Machine Learning
    - databricks-runtime-for-machine-learning-databricks-runtime-ml
    - DRFML(RM
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: train-ai-and-ml-models-databricks-on-aws.md
    - file: pytorch-databricks-on-aws.md
    - file: what-are-hugging-face-transformers-databricks-on-aws.md
    - file: model-training-examples-databricks-on-aws.md
    - file: mlflow-api-reference-databricks-on-aws.md
title: Databricks Runtime for Machine Learning
description: A pre-built runtime environment for deep learning that includes TensorFlow, PyTorch, Keras, pre-configured GPU support, and integrated MLflow tracking.
tags:
  - deep-learning
  - databricks
  - runtime
  - machine-learning
timestamp: "2026-06-19T22:13:45.902Z"
---

---

title: Databricks Runtime for Machine Learning
summary: A pre-configured deep learning infrastructure that includes TensorFlow, PyTorch, Keras, GPU drivers, MLflow, and all Databricks workspace capabilities.
sources:
  - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  - databricks-runtime-for-machine-learning-databricks-on-aws.md
  - mlflow-api-reference-databricks-on-aws.md
  - train-ai-and-ml-models-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:53:14.382Z"
updatedAt: "2026-06-19T17:41:19.741Z"
tags:
  - deep-learning
  - infrastructure
  - databricks
aliases:
  - databricks-runtime-for-machine-learning
  - DRFML
confidence: 0.9
provenanceState: merged
inferredParagraphs: 2
---

# Databricks Runtime for Machine Learning

**Databricks Runtime for Machine Learning** (Databricks Runtime ML) is a specialized runtime that automates the creation of compute resources with pre-built machine learning and deep learning infrastructure. It provides a comprehensive, ready-to-use environment that includes the most common ML and deep learning libraries, built-in GPU support, and full integration with Databricks workspace capabilities. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md] ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md] ^[train-ai-and-ml-models-databricks-on-aws.md]

## Key features

### Pre-installed libraries

Databricks Runtime ML bundles popular machine learning and deep learning libraries out of the box. The libraries are updated with each release, and a subset of top-tier libraries receive a faster update cadence and advanced support. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md] Included libraries:

- **PyTorch** — GPU-accelerated tensor computation and deep learning networks. PyTorch is included in Databricks Runtime ML; for standard Databricks Runtime, it must be installed separately. ^[pytorch-databricks-on-aws.md]
- **TensorFlow** and **Keras** — for building and training neural networks. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Hugging Face Transformers** — included from Databricks Runtime 10.4 LTS ML onward; also includes `datasets`, `accelerate`, and `evaluate` from Databricks Runtime 13.0 ML and above. ^[what-are-hugging-face-transformers-databricks-on-aws.md]
- **XGBoost** — gradient boosting framework for both Python and Scala; supports single-node and distributed training. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md] ^[model-training-examples-databricks-on-aws.md]
- **MLflow** — the runtime provides a managed version of the MLflow server, including experiment tracking and the [Model Registry](/concepts/mlflow-model-registry.md). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md] ^[mlflow-api-reference-databricks-on-aws.md]
- Additional libraries: [Optuna](/concepts/optuna.md) for hyperparameter tuning, [DeepSpeed](/concepts/deepspeed.md), Ray, and [TorchDistributor](/concepts/torchdistributor.md) for distributed training. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

You can install additional libraries at the notebook, cluster, or job level to create a custom environment. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### GPU support

Databricks Runtime ML includes built-in, pre-configured GPU support with drivers and supporting libraries. It supports GPU instance types including A100 GPUs for large-scale deep learning tasks such as training large language models, natural language processing, object detection and classification, and recommendation engines. A100 GPUs typically have limited availability and may require reservation in advance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Compute versatility

The runtime supports both CPU and GPU-based instance types, including AWS Graviton for improved price-to-performance (available from Databricks Runtime 15.4 LTS ML). It integrates with Photon to accelerate Spark SQL, DataFrames, and feature engineering tasks (available from Databricks Runtime 15.2 ML). Photon is not expected to improve performance on Python packages such as XGBoost, PyTorch, and TensorFlow, or Spark RDDs and Pandas UDFs. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Access control

To access data in [Unity Catalog](/concepts/unity-catalog.md) on a compute resource running Databricks Runtime ML, you must set the access mode to **Dedicated**. When a compute resource has Dedicated access mode, it can be assigned to a single user or a group. When assigned to a group, the user's permissions automatically down-scope to the group's permissions. Fine-grained access control and querying tables created using Lakeflow Spark Declarative Pipelines are only available on Databricks Runtime 15.4 LTS ML and above. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Additional workspace capabilities

Databricks Runtime ML includes all capabilities of the Databricks workspace, such as:
- Cluster creation and management with cluster policies to guide data scientists toward appropriate configurations.
- Library and environment management at the notebook, cluster, and job levels.
- Code management with Databricks Git folders.
- Automation support including [Lakeflow Jobs](/concepts/lakeflow-jobs.md) and APIs.
- Integrated [MLflow Tracking](/concepts/mlflow-tracking.md) and [Databricks Autologging](/concepts/databricks-autologging.md) for model development tracking and deployment. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Use cases and best practices

### Training deep learning models

Databricks recommends using Databricks Runtime ML together with MLflow tracking and autologging for all model training. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

**Start with a Single Node cluster** — A [Single Node](/concepts/single-node-ai-runtime.md) (driver-only) GPU cluster is typically fastest and most cost-effective for iterative deep learning development. One node with 4 GPUs is often faster than 4 worker nodes with 1 GPU each because distributed training incurs network communication overhead. Use a single node for small- to medium-size data; for larger datasets move to multi-GPU or distributed compute. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

**Use [TensorBoard](/concepts/tensorboard-on-databricks.md) and cluster metrics** to monitor the training process. TensorBoard is pre-installed in Databricks Runtime ML. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

**Apply performance optimization techniques**:
- **Early stopping** — monitor a validation metric and stop when it stops improving. Native APIs are available in TensorFlow/Keras and PyTorch Lightning.
- **Batch size tuning** — adjust batch size alongside the learning rate to optimize GPU utilization. When increasing batch size by n, increase learning rate by sqrt(n).
- **Transfer learning** — start from a previously trained model to reduce training and tuning time. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

**Move to distributed training** — Databricks Runtime ML includes [TorchDistributor](/concepts/torchdistributor.md), [DeepSpeed](/concepts/deepspeed.md), and Ray to facilitate scaling from single-node to distributed training. TorchDistributor is an open-source PySpark module that launches PyTorch training jobs as Spark jobs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

For hyperparameter tuning, [Optuna](/concepts/optuna.md) provides adaptive tuning; it is included and can parallelize training. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Classic machine learning

Databricks Runtime ML supports traditional ML workflows through AutoML and open-source libraries. [AutoML](https://docs.databricks.com/aws/en/machine-learning/automl/) simplifies the process of applying machine learning by automatically finding the best algorithm and hyperparameter configuration, offering both a no-code UI and a Python API. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Inference

**Online serving** — Use [Model Serving](/concepts/model-serving.md) to deploy custom models (packaged in MLflow format) behind a REST API, including PyTorch, Hugging Face, and other frameworks. [Foundation Model APIs](/concepts/foundation-model-apis.md) provide pay-per-token access to state-of-the-art open models, and [External Models](/concepts/external-models.md) such as OpenAI GPT-4 and Anthropic Claude can be centrally governed. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

**Batch and streaming inference** — Use Spark Pandas UDFs to scale inference across a cluster. When a model is logged from Databricks, MLflow automatically generates inference code to apply the model as a pandas UDF. Separate preprocessing ETL into [Delta Lake](/concepts/delta-lake.md) tables to reduce costs and optimize hardware selection. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Data loading

Databricks recommends using [Delta Lake](/concepts/delta-lake.md) tables for data storage, especially for image datasets, as it simplifies ETL and optimizes data throughput. For very large datasets that do not fit in memory, streaming approaches such as PyTorch IterableDataset, [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming, or Ray Data are available. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Comparison with AI Runtime

[AI Runtime](/concepts/ai-runtime.md) is a serverless GPU compute environment (Preview) optimized for custom single-node and multi-node deep learning workloads, offering instant availability without managing underlying cluster infrastructure. Databricks Runtime ML is a classic compute runtime with pre-built infrastructure, suitable for users who want a comprehensive, ready-to-use environment for both classic ML and deep learning. ^[train-ai-and-ml-models-databricks-on-aws.md]

## Related concepts

- [AI Runtime](/concepts/ai-runtime.md) — Serverless GPU compute for deep learning workloads.
- [MLflow](/concepts/mlflow.md) — Tracking, autologging, and model registry integrated into Databricks Runtime ML.
- [Unity Catalog](/concepts/unity-catalog.md) — Secure data access requires Dedicated access mode.
- Photon — Accelerated query engine for Spark SQL, available in Databricks Runtime 15.2 ML and above.
- [Optuna](/concepts/optuna.md) — Hyperparameter tuning library included in Databricks Runtime ML.
- [TorchDistributor](/concepts/torchdistributor.md) — PySpark module for distributed PyTorch training.
- [DeepSpeed](/concepts/deepspeed.md) — Distributed training library included in Databricks Runtime ML.
- Ray — Platform for distributed computing, included in Databricks Runtime ML.
- Hugging Face Transformers — Pre-installed from Databricks Runtime 10.4 LTS ML.
- [Model Serving](/concepts/model-serving.md) — Online inference deployment for custom models.
- AutoML — Automated model training available on Databricks Runtime ML.

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- train-ai-and-ml-models-databricks-on-aws.md
- what-are-hugging-face-transformers-databricks-on-aws.md
- pytorch-databricks-on-aws.md
- model-training-examples-databricks-on-aws.md
- mlflow-api-reference-databricks-on-aws.md
- machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
3. [train-ai-and-ml-models-databricks-on-aws.md](/references/train-ai-and-ml-models-databricks-on-aws-b6078c61.md)
4. [pytorch-databricks-on-aws.md](/references/pytorch-databricks-on-aws-b092c491.md)
5. [what-are-hugging-face-transformers-databricks-on-aws.md](/references/what-are-hugging-face-transformers-databricks-on-aws-8bbaced1.md)
6. [model-training-examples-databricks-on-aws.md](/references/model-training-examples-databricks-on-aws-47a05943.md)
7. [mlflow-api-reference-databricks-on-aws.md](/references/mlflow-api-reference-databricks-on-aws-472f1a07.md)
