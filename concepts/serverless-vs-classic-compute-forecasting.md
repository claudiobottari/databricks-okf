---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f9595ce509e56cb0ae20d0d6e0a6eae45d47108e4c4a52e8a2f7617cb3a15dd
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - serverless-vs-classic-compute-forecasting
    - SVCCF
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Serverless vs Classic Compute Forecasting
description: The distinction between Databricks' serverless forecasting (fully-managed compute) and classic compute forecasting (traditional compute-backed), with differences in setup, scaling, and management overhead.
tags:
  - databricks
  - forecasting
  - architecture
  - comparison
timestamp: "2026-06-19T18:53:15.466Z"
---

# Serverless vs Classic Compute Forecasting

**Serverless vs Classic Compute Forecasting** refers to two distinct execution models for [AutoML forecasting](/concepts/automl-forecast.md) workloads on Databricks. Each approach differs in compute management, scalability, user interaction, and associated features.

## Overview

Databricks Model Training offers two modes for running forecasting experiments on time-series data: a [serverless computing|serverless](/concepts/serverless-compute-tracing-requirements.md) option that uses fully-managed compute resources, and a classic compute option that requires users to manage their own clusters. The choice between them depends on requirements for control, cost, and infrastructure management. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Serverless Forecasting

Serverless forecasting runs AutoML experiments entirely on Databricks-managed compute infrastructure. Users do not need to provision or configure clusters, and all compute resources are fully managed by the platform. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Key Characteristics

- **Fully managed compute**: No cluster setup or management required. ^[forecasting-serverless-with-automl-databricks-on-aws.md]
- **UI-driven workflow**: Users create and run experiments through the Databricks Model Training UI. ^[forecasting-serverless-with-automl-databricks-on-aws.md]
- **Automated pipeline**: The system handles preprocessing, tuning, and training stages automatically. ^[forecasting-serverless-with-automl-databricks-on-aws.md]
- **Unity Catalog integration**: Training data, predictions, and registered models all use [Unity Catalog](/concepts/unity-catalog.md) tables. ^[forecasting-serverless-with-automl-databricks-on-aws.md]
- **Simplified deployment**: Best models can be deployed directly to [Model Serving](/concepts/model-serving.md) endpoints from the UI. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Benefits

- Reduced operational overhead for users who prefer not to manage infrastructure.
- Automatic scaling and resource optimization.
- Streamlined workflow from data selection to model serving.

## Classic Compute Forecasting

Classic compute forecasting requires users to set up and manage their own Databricks clusters for running AutoML experiments. It provides more control over the compute environment and configuration. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Key Characteristics

- **User-managed clusters**: Users must provision and configure compute resources. ^[forecasting-serverless-with-automl-databricks-on-aws.md]
- **Notebook-based workflow**: Typically involves running AutoML through Databricks notebooks. ^[forecasting-serverless-with-automl-databricks-on-aws.md]
- **Manual infrastructure management**: Users control cluster sizes, configurations, and lifecycle. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Benefits

- Greater control over compute resources and environment configuration.
- Allows for custom cluster configurations and libraries.
- May be preferred in environments with strict network policies or compliance requirements.

## Comparison Summary

| Feature | Serverless Forecasting | Classic Compute Forecasting |
|---------|----------------------|---------------------------|
| Compute management | Fully managed by Databricks | User-managed clusters |
| Setup effort | Minimal – no cluster configuration | Requires cluster provisioning |
| Workflow | UI-driven | Notebook-driven |
| Infrastructure control | Limited | Full control |
| Unity Catalog support | Built-in | Supported |
| Model serving deployment | Direct from UI | Manual setup required |

^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Requirements for Serverless Forecasting

Serverless forecasting has the following specific requirements:^[forecasting-serverless-with-automl-databricks-on-aws.md]

- Training data must be saved as a [Unity Catalog table](/concepts/unity-catalog.md) with a time series column of type `timestamp` or `date`.
- If the workspace has serverless egress control enabled, `pypi.org` must be added to the allowed domains list for network policies.

## When to Use Each Approach

- **Choose serverless forecasting** when you want minimal infrastructure management, prefer a UI-driven workflow, and have straightforward forecasting needs that fit within Databricks' managed compute model.
- **Choose classic compute forecasting** when you need fine-grained control over cluster configuration, require custom libraries or environments, or have compliance constraints that require user-managed infrastructure.

## Related Concepts

- AutoML
- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- [Databricks Model Serving](/concepts/databricks-model-serving.md)
- Serverless Compute on Databricks
- [Unity Catalog](/concepts/unity-catalog.md)
- Network Policies for Serverless

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
