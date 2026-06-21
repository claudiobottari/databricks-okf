---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d554a6328a53207cdc0fc08dd74d681fe549ba94badd3d1ee2445c243b311a0f
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - genie-code-ai-assistant-for-data-science
    - GC(AFDS
    - Genie Code for data science
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Genie Code (AI Assistant for Data Science)
description: An AI assistant integrated across Databricks notebooks and workspace for development, debugging, and operations, drawing on specialized enterprise knowledge.
tags:
  - ai-assistant
  - development
  - productivity
timestamp: "2026-06-18T14:41:55.216Z"
---

# Genie Code (AI Assistant for Data Science)

**Genie Code** is an AI assistant integrated across Databricks Notebooks and the Databricks workspace. It is designed to support data scientists throughout the Machine Learning Lifecycle, from exploratory data analysis (EDA) through model deployment and production monitoring. Genie Code draws on specialized knowledge of the user’s enterprise context, including data assets in [Unity Catalog](/concepts/unity-catalog.md), to provide contextual assistance. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md, databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Capabilities

### Exploratory Data Analysis (EDA)

Genie Code can perform fully automated EDA or act as an interactive assistant. It helps data scientists explore data using natural language chat, UIs, or code, enabling rapid understanding of data distributions, predictive signals, and quality issues before modeling. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Data Discovery and Feature Preparation

By browsing Unity Catalog, Genie Code accelerates data discovery, suggests relevant feature transformations, and generates code for ingestion and feature pipelines. This bridges data engineering and ML by unifying governance under Unity Catalog while streamlining the creation of features managed in a [Feature Store](/concepts/feature-store.md). ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Intelligent AutoML

Genie Code provides an intelligent AutoML capability that takes natural language requests and builds full multi-notebook workflows. These workflows cover featurization, model training, hyperparameter tuning, evaluation, and deployment, automating the repetitive aspects of model development. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Code Generation for Deployments

Genie Code can generate code for [Model Serving](/concepts/model-serving.md) deployment, whether for batch inference or real-time endpoints. It also helps diagnose issues and analyze performance of model serving endpoints, assisting in production operations. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Full Workflow Integration

Genie Code supports every stage of the ML workflow:

- Start with Genie Chat to discover relevant models, data, and features in the workspace and Unity Catalog.
- Use Genie Code to prototype pipelines for featurization, training, tuning, evaluation, and deployment.
- Analyze production model serving endpoints with Genie Code to diagnose and investigate issues. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Integration with the Databricks Platform

Genie Code is embedded across notebooks and the workspace, integrating with [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md), [Unity Catalog](/concepts/unity-catalog.md), and [Model Serving](/concepts/model-serving.md). It can be used alongside third-party AI coding tools for ML pipeline development, while Databricks provides agent skills for those tools. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md, databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- Genie Chat — Natural language chat assistant for discovery of data, models, and features.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for data and ML assets, which Genie Code queries for context.
- [Feature Store](/concepts/feature-store.md) — Governed repository for ML features that Genie Code helps prepare.
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry integrated with Genie Code workflows.
- [Model Serving](/concepts/model-serving.md) — Deployment targets that Genie Code can configure and diagnose.
- Automated Machine Learning (AutoML) — Umbrella concept for automated model development.
- Exploratory Data Analysis (EDA) — Initial investigation step that Genie Code can automate.

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
2. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
