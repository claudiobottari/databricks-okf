---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1b861f6d29079b26aa7e383c67d89568b188c2f3a7dd4b4d79acc4f0b5109dd
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-xgboost-training-on-databricks-with-scala
    - DXTODWS
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: Distributed XGBoost Training on Databricks with Scala
description: Using Scala API on Databricks to perform distributed training of XGBoost models
tags:
  - machine-learning
  - xgboost
  - scala
  - databricks
  - distributed-training
timestamp: "2026-06-19T10:17:29.189Z"
---

---
title: Distributed XGBoost Training on Databricks with Scala
summary: How to use XGBoost with [Apache Spark MLlib](/concepts/apache-spark-mllib.md) on Databricks to build distributed classification and regression models using Scala.
sources:
  - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:13:46.408Z"
updatedAt: "2026-06-18T08:13:46.408Z"
tags:
  - xgboost
  - scala
  - databricks
  - distributed-training
  - mllib
aliases:
  - distributed-xgboost-training-on-databricks-with-scala
  - DXTODWS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Distributed XGBoost Training on Databricks with Scala

**Distributed XGBoost Training on Databricks with Scala** refers to the use of [XGBoost](/concepts/xgboostspark-module.md) together with [Apache Spark MLlib](/concepts/apache-spark-mllib.md) on the Databricks platform to perform large-scale gradient boosting at scale, using the Scala programming language. This approach enables XGBoox models to be trained on large datasets that do not fit into a single machine's memory, and embeds those models directly into [ML Pipelines](/concepts/mllib-pipelines-api.md) for end-to-end workflow management. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Overview

XGBoost is a popular, high-performance gradient-boosting library for classification, regression, and ranking. On Databricks, users can train XGBoost models in a distributed fashion by integrating them with MLlib, the machine learning library built on top of Spark. The platform provides example notebooks that demonstrate two key patterns: embedding an XGBoost model into an MLlib ML Pipeline, and using MLlib cross-validation to tune hyperparameters. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Available Example Notebooks

Databricks provides two example notebooks that show how to use XGBoost with MLlib in Scala:

- **XGBoost classification with ML Pipeline notebook** — Demonstrates how to wrap an XGBoost model inside an [MLlib ML Pipeline](/concepts/mllib-pipelines-api.md) for structured classification workflows. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
- **XGBoost regression with cross-validation notebook** — Shows how to use MLlib cross-validation to tune an [XGBoost](/concepts/xgboostspark-module.md) model for regression tasks. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

Both notebooks are available from the [model training examples](/concepts/databricks-runtime-ml-model-training-examples.md) section of the Databricks documentation. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) — The underlying gradient-boosting library.
- MLlib — Spark's distributed machine learning library.
- ML Pipeline — A Spark abstraction for chaining multiple transformation and [model training](/concepts/databricks-model-training.md) stages.
- Scala on Databricks — General guidance for using the Scala API on the platform.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Broad topic of scaling ML workloads across multiple nodes.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — Cross-validation as a tuning strategy.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
