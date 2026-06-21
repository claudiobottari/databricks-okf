---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9782c55e43faad8cef3c3a55fb55a248c53277428b430b127a71df11e33cd4f6
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperparameter-tuning-for-model-selection
    - HTFMS
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: Hyperparameter tuning for model selection
description: The technique of using hyperparameter optimization frameworks like Hyperopt to compare different model types (e.g., different algorithm families) by tuning each with its own appropriate hyperparameter space to find the best overall model.
tags:
  - machine-learning
  - model-selection
  - hyperparameter-tuning
timestamp: "2026-06-19T09:19:23.603Z"
---

# Hyperparameter tuning for model selection

**Hyperparameter tuning for model selection** refers to the process of tuning hyperparameters across multiple model types and comparing their performance to identify the best overall model. This approach systematically explores different hyperparameter configurations appropriate for each model type, rather than tuning a single model in isolation.

## Overview

The goal of hyperparameter tuning for model selection is to find not just the best hyperparameters for a given model, but also the best model type for the problem. This involves evaluating multiple model architectures or algorithms, each with its own set of hyperparameters, on the same task. By comparing the optimized performance of each model type, practitioners can make an informed selection. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Approach with Hyperopt and SparkTrials

A typical method for hyperparameter tuning for model selection uses [Hyperopt](/concepts/hyperopt.md) with [SparkTrials](/concepts/sparktrials.md) to distribute the search across a Spark cluster. The workflow involves:

1. Defining multiple model types (e.g., three different algorithms from scikit-learn).
2. Specifying a distinct hyperparameter search space for each model type, appropriate to its characteristics.
3. Running a distributed hyperparameter optimization using `SparkTrials` to efficiently evaluate many combinations.
4. Tracking results with [MLflow](/concepts/mlflow.md) to compare model types and hyperparameter configurations.

This approach is demonstrated in the Databricks notebook *Compare models using scikit-learn, Hyperopt, and MLflow*, which tunes three model types and evaluates their performance with different hyperparameters to arrive at a best model overall. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Deprecation and alternatives

The open-source version of Hyperopt is no longer being maintained, and Hyperopt is not included in Databricks Runtime for Machine Learning after version 16.4 LTS ML. Databricks recommends using [Optuna](/concepts/optuna.md) for single-node optimization or [RayTune](/concepts/raytune.md) for distributed hyperparameter tuning (similar to the deprecated Hyperopt with `SparkTrials` experience). ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Related concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- [Model selection](/concepts/custom-judge-model-selection.md)
- [Optuna](/concepts/optuna.md)
- [RayTune](/concepts/raytune.md)
- [SparkTrials](/concepts/sparktrials.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
