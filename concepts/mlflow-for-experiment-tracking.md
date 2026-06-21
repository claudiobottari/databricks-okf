---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 159910423818e09ab6db6a70f981e582ae356ce9da2c6899fb9330b5619d2cac
  pageDirectory: concepts
  sources:
    - compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-for-experiment-tracking
    - MFET
  citations:
    - file: compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md
title: MLflow for experiment tracking
description: Using MLflow to log, track, and compare hyperparameter tuning runs across different model types
tags:
  - mlflow
  - experiment-tracking
  - machine-learning
timestamp: "2026-06-19T14:19:42.824Z"
---

# MLflow for Experiment Tracking

**MLflow for experiment tracking** refers to the use of MLflow's tracking capabilities to log, organize, compare, and manage machine learning experiments. MLflow provides a centralized system for recording parameters, metrics, artifacts, and model versions across training runs, enabling reproducibility and systematic model comparison.

## Overview

MLflow Experiment Tracking is a core component of the MLflow platform that allows data scientists and ML engineers to log and query experiments. Each experiment contains multiple runs, where a run represents a single execution of a training script or notebook. For each run, MLflow can log parameters, metrics, tags, artifacts (such as model files, plots, and data snapshots), and source code information. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Key Concepts

### Experiments and Runs

An **experiment** is the top-level organizational unit in MLflow Tracking. Within an experiment, each **run** captures the results of a single training attempt. Runs are automatically timestamped and can be compared side-by-side in the MLflow UI. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### Logged Components

MLflow Tracking can record the following components for each run:

- **Parameters**: Key-value pairs of input configuration (e.g., learning rate, number of trees, regularization strength)
- **Metrics**: Numeric values that change over time or across runs (e.g., accuracy, loss, F1 score)
- **Artifacts**: Files produced by the run, including model binaries, plots, feature importance charts, and serialized objects
- **Tags**: Key-value metadata for organizing and searching runs
- **Source**: The code version and entry point that produced the run

^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Using MLflow for Hyperparameter Tuning

MLflow integrates naturally with hyperparameter optimization frameworks like [Hyperopt](/concepts/hyperopt.md), [Optuna](/concepts/optuna.md), and [RayTune](/concepts/raytune.md). When performing hyperparameter tuning, each trial is logged as a separate [MLflow Run](/concepts/mlflow-run.md), allowing practitioners to compare results across different hyperparameter configurations. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### Comparing Multiple Model Types

A common workflow involves using MLflow to compare different model architectures or algorithms. For example, when using [Hyperopt](/concepts/hyperopt.md) with `SparkTrials`, practitioners can evaluate multiple model types (e.g., random forest, gradient boosting, linear models) with different hyperparameter sets appropriate for each type. MLflow captures all runs in a single experiment, enabling direct comparison of performance metrics across model families. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

### Best Model Selection

By logging all trials to the same MLflow experiment, practitioners can use the MLflow UI or API to query the best-performing run based on a chosen metric (e.g., validation accuracy or F1 score). The best run's parameters and artifacts can then be promoted to production or used for further refinement. ^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Integration with Databricks

On Databricks, MLflow is pre-installed and configured in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). The platform provides:

- Automatic logging of parameters, metrics, and models when using MLflow APIs
- The MLflow experiment UI accessible from the Databricks workspace
- Integration with [Hyperopt](/concepts/hyperopt.md) and [SparkTrials](/concepts/sparktrials.md) for distributed hyperparameter tuning
- Model registry for managing model lifecycle from experimentation to production

^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Best Practices

- **Use one experiment per project** to keep related runs organized and comparable
- **Log all relevant parameters** before training begins to ensure reproducibility
- **Log metrics at each epoch or iteration** to visualize training dynamics
- **Log artifacts** such as feature importance plots, confusion matrices, and model summaries
- **Use tags** to mark runs with metadata like data version, environment, or experiment purpose
- **Compare runs systematically** using the MLflow UI's parallel coordinates plot or scatter plot views

^[compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) — Hyperparameter optimization framework that integrates with MLflow
- [Optuna](/concepts/optuna.md) — Modern hyperparameter optimization library recommended for single-node tuning
- [RayTune](/concepts/raytune.md) — Distributed hyperparameter tuning framework
- [SparkTrials](/concepts/sparktrials.md) — Hyperopt's distributed trial execution engine for Spark
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Component for managing model versions and lifecycle
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-configured runtime with MLflow and ML libraries
- [Experiment Comparison](/concepts/multi-experiment-run-comparison.md) — Techniques for comparing MLflow runs

## Sources

- compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md

# Citations

1. [compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws.md](/references/compare-model-types-with-hyperopt-and-mlflow-databricks-on-aws-24ee58b3.md)
