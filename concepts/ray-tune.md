---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5dd5847dbe59ebaee5b4c97f278377b825d149aea8412fd819fd93fdded689e1
  pageDirectory: concepts
  sources:
    - hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-tune
  citations:
    - file: hyperparameter-tuning-databricks-on-aws.md
title: Ray Tune
description: A distributed hyperparameter tuning library that uses Ray as a backend for parallel compute, available in Databricks Runtime ML.
tags:
  - machine-learning
  - distributed-computing
  - hyperparameter-tuning
timestamp: "2026-06-19T19:08:29.256Z"
---

# Ray Tune

**Ray Tune** is a hyperparameter tuning library that is part of the Ray ecosystem (an open-source framework for parallel and distributed computing). It automates the search for optimal hyperparameters and uses Ray as a distributed backend to scale across multiple machines or GPUs, reducing the time needed for model selection. ^[hyperparameter-tuning-databricks-on-aws.md]

## Integration with Databricks

Databricks Runtime ML includes Ray, making Ray Tune available directly on Databricks clusters. The platform recommends Ray Tune as a replacement for the deprecated [Hyperopt](/concepts/hyperopt.md) library for distributed hyperparameter tuning workflows. Users can refer to the Ray on Databricks documentation and the official Ray Tune tutorials for examples of running distributed tuning jobs. ^[hyperparameter-tuning-databricks-on-aws.md]

## Related Concepts

- [Optuna](/concepts/optuna.md) – A lightweight hyperparameter tuning library, recommended for single-node optimization.
- [Hyperopt](/concepts/hyperopt.md) – A deprecated library; Ray Tune is the recommended alternative for distributed tuning.
- Ray – The underlying distributed computing framework that provides the backend for Ray Tune.
- [MLflow](/concepts/mlflow.md) – For tracking hyperparameters and metrics across tuning trials.
- [Distributed Hyperparameter Tuning](/concepts/raytune-for-distributed-hyperparameter-tuning-on-databricks.md) – The general practice of scaling hyperparameter search.

## Sources

- hyperparameter-tuning-databricks-on-aws.md

# Citations

1. [hyperparameter-tuning-databricks-on-aws.md](/references/hyperparameter-tuning-databricks-on-aws-6d74646d.md)
