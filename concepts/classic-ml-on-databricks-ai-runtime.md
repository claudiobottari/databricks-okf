---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1e406786b80aeb01b12afbab5c289994ce9eb7c56ace3e6dbdb0b20d229a95a
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - classic-ml-on-databricks-ai-runtime
    - CMODAR
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Classic ML on Databricks AI Runtime
description: Support for traditional machine learning tasks like XGBoost training and time series forecasting within the AI Runtime environment.
tags:
  - machine-learning
  - xgboost
  - time-series
timestamp: "2026-06-18T10:44:36.268Z"
---

# Classic ML on Databricks AI Runtime

**Classic ML on Databricks AI Runtime** refers to traditional machine learning tasks—such as tree-based models and time series forecasting—that are supported on AI Runtime alongside deep learning workloads. These tasks run on GPU-accelerated clusters and can benefit from the same distributed training infrastructure.

## Status

- **Public Preview**: Single-node classic ML tasks are in Public Preview. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Beta**: Distributed training for multi-GPU workloads remains in Beta. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example tasks

Classic ML examples on AI Runtime include:

- **XGBoost model training** – gradient-boosted decision trees for classification and regression.
- **Time series forecasting** – traditional forecasting methods using libraries such as Prophet, ARIMA, or gradient-boosted models.

These examples are available in the AI Runtime example notebooks gallery under the [AI Runtime example notebooks](/concepts/ai-runtime-example-notebooks.md) section. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related concepts

- [AI Runtime](/concepts/ai-runtime.md) – the GPU-optimized runtime for ML workloads
- [XGBoost](/concepts/xgboostspark-module.md) – popular gradient boosting library
- Time series forecasting – traditional ML approach for sequential data
- [AI Runtime example notebooks](/concepts/ai-runtime-example-notebooks.md) – full list of notebook examples
- [AI Runtime CLI (air)](/concepts/ai-runtime-cli-air.md) – CLI for submitting and managing AI Runtime workloads

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
