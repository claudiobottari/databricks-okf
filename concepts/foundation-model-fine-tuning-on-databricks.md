---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 659df4af62cce628241c1290032dc41069a7bc844b75ed4e0331c202de87e78a
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-fine-tuning-on-databricks
    - FMFOD
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: Foundation Model Fine-tuning on Databricks
description: A feature within Databricks Model Training that lets users customize large language models using their own data via instruction fine-tuning, continued pre-training, and chat completion.
tags:
  - databricks
  - llm
  - fine-tuning
  - machine-learning
timestamp: "2026-06-19T18:15:27.412Z"
---



# Foundation Model Fine-tuning on Databricks

**Foundation Model Fine-tuning on Databricks** (now part of Databricks Model Training) lets you customize large language models (LLMs) using your own data. This process involves fine-tuning a pre-existing foundation model, significantly reducing the data, time, and compute resources required compared to training a model from scratch. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Key Capabilities

### Instruction Fine-Tuning

Adapt your model to new tasks by training on structured prompt-response data. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Continued Pre-Training

Enhance your model with additional text data to add new knowledge or focus on a specific domain. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Chat Completion

Train your model on chat logs to improve conversational abilities. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Infrastructure and Compute

### Databricks Runtime for Machine Learning

Foundation model fine-tuning runs on [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (Databricks Runtime ML), which automates the creation of a compute resource with pre-built machine learning and deep learning infrastructure, including the most common ML and DL libraries updated with each release. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### GPU Compute

For GPU-based compute, select a GPU-enabled instance type in the **Worker type** drop-down menu when creating compute resources. For the complete list of supported GPU types, see the supported instance type documentation. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Photon Support

When you create a compute resource running Databricks Runtime 15.2 ML or above, you can choose to enable Photon. Photon improves performance for applications using Spark SQL, Spark DataFrames, feature engineering, GraphFrames, and xgboost4j. It is not expected to improve performance on Python packages such as PyTorch and TensorFlow, which are commonly used in fine-tuning workflows. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Access Mode Requirements

To access data in [Unity Catalog](/concepts/unity-catalog.md) on a compute resource running Databricks Runtime ML, you must set the access mode to **Dedicated**. The access mode is automatically set when you select the **Machine learning** checkbox during compute creation. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

When using dedicated access mode, fine-grained access control and querying tables created using Lakeflow Spark Declarative Pipelines (including streaming tables and materialized views) are only available on Databricks Runtime 15.4 LTS ML and above. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Features

### AutoML

AutoML simplifies the process of applying machine learning to your datasets by automatically finding the best algorithm and hyperparameter configuration. AutoML offers a no-code UI as well as a Python API, and is part of Databricks Model Training alongside Foundation Model Fine-tuning. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Deep Learning Training

See examples and best practices for [distributed deep learning training](/concepts/distributed-deep-learning-training-on-databricks.md) to develop and fine-tune deep learning models on Databricks beyond LLMs. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### LLMOps Integration

In LLMOps workflows, fine-tuning is a distinct step that can be implemented as a Databricks Job. Validating a fine-tuned model before deployment is often a manual process. Foundation Model Fine-tuning lets you use your own data to customize an existing LLM to optimize its performance for your specific application. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- AutoML
- [Unity Catalog](/concepts/unity-catalog.md)
- [Deep Learning Training](/concepts/deep-learning-on-databricks.md)
- Photon
- LLMOps Workflows

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md
- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
2. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
