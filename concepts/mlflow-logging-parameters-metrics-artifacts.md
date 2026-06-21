---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 178e084c400b1490a65bda25abd04a908e142a83502741d52ab4c7cdfaaae49e
  pageDirectory: concepts
  sources:
    - mlflow-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-logging-parameters-metrics-artifacts
    - ML(MA
  citations:
    - file: mlflow-api-reference-databricks-on-aws.md
title: MLflow Logging (Parameters, Metrics, Artifacts)
description: The MLflow capability to log parameters, metrics, and artifacts to runs via the REST API
tags:
  - mlflow
  - logging
  - tracking
timestamp: "2026-06-19T19:38:04.364Z"
---

# MLflow Logging (Parameters, Metrics, Artifacts)

**MLflow Logging (Parameters, Metrics, Artifacts)** refers to the core capability provided by the [MLflow REST API](/concepts/mlflow-rest-api.md) for recording metadata and outputs generated during machine learning experiments. This logging functionality enables experiment tracking by persisting key information—hyperparameters, performance scores, and model files—to an [MLflow Experiment](/concepts/mlflow-experiment.md) or a specific [MLflow Run](/concepts/mlflow-run.md).

## Overview

The open-source MLflow REST API allows users to create, list, and get experiments and runs, and to log parameters, metrics, and artifacts. ^[mlflow-api-reference-databricks-on-aws.md] These three logging categories cover the essential information that data scientists and ML engineers need to compare runs, reproduce results, and manage the model lifecycle.

## Parameters

Parameters are key-value pairs that capture input configurations of a run, such as hyperparameters (e.g., learning rate, number of layers, batch size). Logging parameters enables easy comparison across different runs and helps identify which configuration produced the best results. The MLflow REST API provides endpoints to log parameters for a given run. ^[mlflow-api-reference-databricks-on-aws.md]

## Metrics

Metrics are numeric values that quantify the performance of a model, for example, accuracy, loss, F1 score, or RMSE. They are logged during or after training and can be updated over time (e.g., to record each training epoch). The MLflow REST API allows logging of metrics, and the Databricks environment supports tracking them across runs for visual comparison and analysis. ^[mlflow-api-reference-databricks-on-aws.md]

## Artifacts

Artifacts are output files associated with a run, such as trained model files, plots, data files, or any other serializable objects. Logging artifacts allows you to store and retrieve the actual outputs of a run, enabling model deployment and reproducibility. The MLflow REST API provides endpoints for uploading and downloading artifacts to and from a run’s artifact store. ^[mlflow-api-reference-databricks-on-aws.md]

## Managed MLflow on Databricks

[Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) provides a managed version of the MLflow server, which includes experiment tracking and the [MLflow Model Registry](/concepts/mlflow-model-registry.md). This managed service handles the underlying infrastructure for storing parameters, metrics, and artifacts, allowing users to log and query data without managing a separate server. ^[mlflow-api-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – The overall framework for organizing runs and logged data.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – A centralized model store for managing model versions, stages, and deployments.
- [MLflow REST API](/concepts/mlflow-rest-api.md) – The programmatic interface for all logging and management operations.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The pre-configured environment that bundles a managed MLflow server.

## Sources

- mlflow-api-reference-databricks-on-aws.md

# Citations

1. [mlflow-api-reference-databricks-on-aws.md](/references/mlflow-api-reference-databricks-on-aws-472f1a07.md)
