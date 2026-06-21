---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66572f6dbd46f6cd37ef0d8e881f91bf27027cbb794f170db95fea7b7af91c96
  pageDirectory: concepts
  sources:
    - mlflow-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-rest-api-20
    - DMRA2
    - Databricks REST API
  citations:
    - file: mlflow-api-reference-databricks-on-aws.md
title: Databricks MLflow REST API 2.0
description: Databricks' managed version of the MLflow API, documented separately from the open-source reference
tags:
  - databricks
  - mlflow
  - api
timestamp: "2026-06-19T19:38:04.127Z"
---

# Databricks MLflow REST API 2.0

The **Databricks MLflow REST API 2.0** is a managed implementation of the [MLflow](/concepts/mlflow.md) REST API provided by Databricks. It allows users to create, list, and get experiments and runs, and to log parameters, metrics, and artifacts programmatically. This API is part of the Databricks Runtime for Machine Learning, which provides a managed version of the MLflow server, including experiment tracking and the [Model Registry](/concepts/mlflow-model-registry.md). ^[mlflow-api-reference-databricks-on-aws.md]

## Overview

The Databricks MLflow REST API 2.0 is distinct from the open-source [MLflow REST API](/concepts/mlflow-rest-api.md). While both APIs share core functionality for experiment tracking and model management, the Databricks version is integrated with the Databricks platform's authentication, access control, and workspace management features. It operates through the Databricks workspace API endpoint, typically at `https://<workspace-url>/api/2.0/experiments/`. ^[mlflow-api-reference-databricks-on-aws.md]

## API Reference Documentation

Databricks provides a dedicated API reference for the MLflow REST API 2.0 at the following location:

- **Databricks MLflow REST API 2.0 reference:** `https://docs.databricks.com/api/workspace/experiments`

This reference covers all available endpoints, request formats, and response schemas for working with experiments, runs, metrics, parameters, and artifacts through the Databricks platform. ^[mlflow-api-reference-databricks-on-aws.md]

## Key Capabilities

The API supports the following core operations:

- **Experiments:** Create, list, get, and search experiments.
- **Runs:** Create, list, get, update, and search runs within experiments.
- **Logging:** Log parameters, metrics, and tags to runs. Log artifacts (files) to run storage.
- **Model Registry:** Register models, create model versions, transition stages, and manage model metadata.

## Relationship to Open-Source MLflow REST API

There are two REST API reference guides available for MLflow on Databricks:

1. **Databricks MLflow REST API 2.0 reference** — The Databricks-specific implementation that integrates with platform features such as workspace authentication, [Unity Catalog](/concepts/unity-catalog.md), and Databricks Access Control.
2. **Open Source MLflow REST API reference** (at `https://mlflow.org/docs/latest/rest-api.html`) — The community standard API specification that is compatible with any MLflow server.

While both APIs share a similar design, the Databricks version may include additional endpoints or modified behaviors to support platform-specific features. Users should consult the Databricks API reference when working within a Databricks environment. ^[mlflow-api-reference-databricks-on-aws.md]

## Authentication

The Databricks MLflow REST API 2.0 uses Databricks Authentication mechanisms, typically requiring a Databricks personal access token or service principal token. API calls must be authenticated against the workspace endpoint. The token is passed as a Bearer token in the `Authorization` header of HTTP requests.

## Related Concepts

- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) — The core functionality exposed by the API
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Managed through the API
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) — The broader API framework that includes MLflow endpoints
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The environment that provides the managed MLflow server
- Databricks Access Control — Auth and permissions for API access

## Sources

- mlflow-api-reference-databricks-on-aws.md

# Citations

1. [mlflow-api-reference-databricks-on-aws.md](/references/mlflow-api-reference-databricks-on-aws-472f1a07.md)
