---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c1485e5f4ce179b800ba57ed8b397e992ad855129600266c64bcb781f2668d9
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-training
    - DMT
    - Model Training
    - model training
    - model training job
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Databricks Model Training
description: A unified platform for training and deploying ML and AI models through AutoML and Foundation Model Fine-tuning workloads
tags:
  - machine-learning
  - training
  - databricks
timestamp: "2026-06-19T09:54:30.800Z"
---

# Databricks Model Training

**Databricks Model Training** streamlines and unifies the process of training and deploying traditional machine learning models through AutoML and [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) workloads on the Databricks platform. It provides a comprehensive environment for building, training, and deploying machine learning models at scale, built on [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (Databricks Runtime ML). ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Overview

Databricks Model Training automates the creation of compute resources with pre-installed machine learning and deep learning infrastructure, including the most common ML and DL libraries. This unified platform enables data scientists and ML engineers to train models ranging from small traditional ML models to large-scale deep learning models with billions of parameters. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Training Capabilities

### AutoML

AutoML simplifies the process of applying machine learning to datasets by automatically finding the best algorithm and hyperparameter configuration. It offers both a no-code UI and a Python API, making it accessible to users of varying technical backgrounds. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Foundation Model Fine-tuning

[Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) (now a core component of Databricks Model Training) enables customization of large language models (LLMs) using your own data. This process involves fine-tuning pre-trained foundation models, significantly reducing the data, time, and compute resources required compared to training from scratch. Key features include: ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- **Instruction fine-tuning:** Adapt models to new tasks by training on structured prompt-response data.
- **Continued pre-training:** Enhance models with additional text data to add new knowledge or focus on a specific domain.
- **Chat completion:** Train models on chat logs to improve conversational abilities.

### Open Source Library Support

Databricks Model Training supports a wide range of open source machine learning libraries. For training examples and best practices, see machine learning training examples from various open source libraries, including hyperparameter tuning examples using [Optuna](/concepts/optuna.md) and [Hyperopt](/concepts/hyperopt.md). ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Deep Learning

For deep learning workloads, Databricks Model Training provides examples and best practices for [distributed deep learning training](/concepts/distributed-deep-learning-training-on-databricks.md) to develop and fine-tune deep learning models at scale. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Recommendation Models

Databricks supports training [deep-learning-based recommendation models](/concepts/deep-learning-based-recommender-systems.md), which can achieve higher quality results and scale to larger amounts of data compared to traditional recommendation models. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Large-Scale Model Training

For models in the **20B to 120B+ parameter range**, Databricks supports training using [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). FSDP shards model parameters, gradients, and optimizer states across multiple GPUs, significantly reducing the per-GPU memory footprint and enabling training of very large models that would otherwise be impossible. Standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is suitable for models that fit within a single GPU's memory, while FSDP becomes necessary for larger models. For even more advanced memory optimization, practitioners may consider [DeepSpeed](/concepts/deepspeed.md). ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Compute Environment

### Databricks Runtime ML

To create a compute resource for model training, select the **Machine learning** checkbox in the create compute UI. This automatically sets the access mode to **Dedicated** with your account as the dedicated user. The compute resource can be manually assigned to a different user or group in the **Advanced** section. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### GPU Support

Databricks supports A100 GPUs across all clouds for deep learning tasks like LLM training, NLP, object detection, and recommendation engines. For GPU-based compute, select a GPU-enabled instance type in the **Worker type** drop-down menu. See the supported GPU instance types for the complete list. A100 GPUs typically have limited capacity in cloud environments, so contacting your cloud provider for resource allocation or reserving capacity in advance is recommended. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md] ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Photon Support

When using Databricks Runtime 15.2 ML or above, you can enable Photon to improve performance for applications using Spark SQL, Spark DataFrames, feature engineering, and specific ML libraries. Photon is not expected to improve performance on applications using Spark RDDs, Pandas UDFs, and non-JVM languages such as Python. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### AWS Graviton Support

Databricks Runtime 15.4 LTS ML and above support Graviton instance types, which can improve performance for Spark, Photon, feature engineering, and machine learning libraries such as XGBoost and LightGBM. Graviton instances may also provide better price-to-performance value. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Dedicated Access Mode

To access data in [Unity Catalog](/concepts/unity-catalog.md) on a compute resource running Databricks Runtime ML, you must set the access mode to **Dedicated**. This is automatically set when you select the **Machine learning** checkbox. When assigned to a group, the user's permissions automatically down-scope to the group's permissions. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

When using dedicated access mode on Databricks Runtime 15.4 LTS ML and above, the following features are available:
- Fine-grained access control
- Querying tables created using [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md), including streaming tables and materialized views

## Library Management

Databricks Runtime ML includes a variety of popular ML libraries updated with each release. Databricks designates some as **top-tier libraries**, providing faster update cadence, advanced support, testing, and embedded optimizations. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

To install additional libraries:
- For compute-scoped availability, create a compute-scoped library.
- For notebook-specific availability, use [Notebook-scoped Python libraries](/concepts/compute-scoped-vs-notebook-scoped-library-installation.md).
- For custom environments, use init scripts or see the release notes for Databricks Runtime ML.

## Evaluation and Monitoring

### A/B Comparison of Agent Configurations

For GenAI agent evaluation, Databricks Model Training supports [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md). This practice involves evaluating two or more versions of an agent side-by-side against the same evaluation dataset, using consistent [judges](/concepts/llm-judges.md) to quantify the impact of changes before promoting a configuration to production. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Serverless Budget Policy

When running serverless workloads for evaluation (such as scheduled scorers, synthetic evaluation set generation, or agent evaluation), MLflow uses a serverless budget policy. If the workspace's default policy is disabled and no alternative policy is assigned, the 403 PERMISSION_DENIED Serverless Budget Policy Error may occur. Setting a serverless budget policy on the MLflow experiment resolves this issue. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Model Governance

### ABAC Security Policies

Databricks Model Training integrates with [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) through Unity Catalog to provide granular security for trained models. Key policies include:

- [ABAC GRANT Policies](/concepts/abac-grant-policies.md): Dynamically grant privileges to models based on governed tags and conditions on the principal and object. These policies control who can execute models in the [Serving UI](/concepts/serving-ui.md) without requiring manual privilege management. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md): Apply dynamic data masking to columns in training data based on tag conditions, ensuring sensitive data (like PII) is properly protected during model training and inference. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

These policies evaluate at query time against tags on the target objects and can be defined once at a catalog or schema scope to cover many assets automatically, reducing maintenance overhead.

## Related Concepts

- [MLflow](/concepts/mlflow.md) — For experiment tracking and model management
- AutoML — Automated machine learning workflows
- Foundation Model Training — Customization of large language models
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The underlying runtime for ML workloads
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance for ML assets
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Strategies for training large models
- [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) — Fully Sharded Data Parallel for large model training
- [DeepSpeed](/concepts/deepspeed.md) — Advanced memory optimization for training

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
4. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
5. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
6. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
