---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6156ef17f7fa76ba1bd2c5ffe3f1d40fe0b3b6ccbe010c54b05234c639bc51d1
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-assisted-development-with-genie-code
    - ADWGC
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: AI-Assisted Development with Genie Code
description: An AI assistant integrated across Databricks notebooks and workspace that helps with development, debugging, and operations using enterprise-context knowledge at every step of the ML workflow.
tags:
  - ai-assistant
  - genie-code
  - development
timestamp: "2026-06-19T17:49:48.662Z"
---

# AI-Assisted Development with Genie Code

**AI-Assisted Development with Genie Code** refers to the use of Databricks' Genie Code, an AI assistant integrated across notebooks and the workspace, to support data science and machine learning workflows. Genie Code helps with development, debugging, and ongoing operations, drawing on specialized knowledge of the user's enterprise context. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Overview

Genie Code is part of the broader Genie AI assistant on Databricks. It is designed to be used at every step of the data science workflow, from initial discovery to production monitoring. Users can interact with Genie Code through a chat interface and within notebooks to accelerate common tasks. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Capabilities and Use Cases

Genie Code can be applied to several key stages of the [ML Lifecycle](/concepts/ml-lifecycle.md):

1. **Discovery** – Use Genie chat to discover relevant models, data, and features stored in the workspace and [Unity Catalog](/concepts/unity-catalog.md). ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]
2. **Prototyping** – Use Genie Code within notebooks to prototype pipelines for [feature engineering](/concepts/featureengineeringclient-api.md), model training, hyperparameter tuning, evaluation, and deployment. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]
3. **Production monitoring** – Analyze [Model Serving](/concepts/model-serving.md) endpoints with Genie Code to diagnose and investigate issues in production. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

In addition to Genie Code, users can also integrate third-party AI coding assistants into their Databricks workflows using the Agent skills for AI coding assistants feature. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Usage in the ML Lifecycle

Genie Code supports each stage of the end-to-end ML lifecycle, including:
- **Scope the use case** – Genie can help clarify prediction targets and success metrics.
- **EDA** – Assist with exploratory data analysis.
- **Data preparation and features** – Guide creation and management of features in a [Feature Store](/concepts/feature-store.md).
- **Training and experiment tracking** – Help set up training runs and log experiments in [MLflow](/concepts/mlflow.md).
- **Evaluation** – Support model quality assessment.
- **Registration and staging** – Facilitate model registration and testing.
- **Deployment** – Assist with setting up batch or real-time serving.
- **Monitoring and retraining** – Provide diagnostics for production endpoints.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- Genie chat – The conversational interface for discovering assets.
- [Unity Catalog](/concepts/unity-catalog.md) – Unified governance for data and ML assets.
- [Model Serving](/concepts/model-serving.md) – Real-time and batch inference endpoints that can be analyzed with Genie Code.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry used in conjunction with Genie Code.
- Agent skills for AI coding assistants – Extensibility mechanism for third-party AI coding tools.
- [ML Lifecycle](/concepts/ml-lifecycle.md) – The end-to-end process Genie Code supports.
- [Feature engineering](/concepts/featureengineeringclient-api.md) – Pipeline prototyping assisted by Genie Code.

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
