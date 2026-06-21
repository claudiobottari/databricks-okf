---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e6b44fd53b1c88c43754d0c1ff1e6b4974321ee9bc998b7c019d42f40bf945d
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-ds-agent
    - GC(A
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Genie Code (DS Agent)
description: An AI-assisted agent on Databricks that performs automated EDA, feature discovery, code generation, AutoML, and model serving diagnostics using natural language.
tags:
  - ai-assistance
  - automl
  - data-science
timestamp: "2026-06-19T18:11:20.211Z"
---

# Genie Code (DS Agent)

**Genie Code** (also referred to as the **DS Agent**) is an AI-powered assistant within Databricks that accelerates the full data science and machine learning (DS/ML) lifecycle. It integrates natural language understanding with automated code generation and workflow orchestration, enabling data scientists to perform exploratory data analysis (EDA), feature engineering, model training, deployment, and production monitoring through conversational interactions. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Capabilities

### Exploratory Data Analysis
Genie Code can perform fully automated exploratory data analysis (EDA) or act as an interactive assistant, allowing users to explore data using natural language chat, UI interactions, or code. It supports real-time co-editing and Git-based code sharing for collaborative data exploration. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Feature Preparation and Serving
Genie Code accelerates data discovery and preparation by browsing [Unity Catalog](/concepts/unity-catalog.md) to discover relevant tables, suggesting feature transformations, and generating code for data ingestion and feature pipeline creation. This reduces the time needed to move from raw data to ML‑ready features. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Automated Model Training (AutoML)
Genie Code provides intelligent AutoML capabilities. It takes natural language requests and automatically builds full multi-notebook workflows for featurization, training, hyperparameter tuning, evaluation, and model registration. This enables rapid prototyping and iteration on model development. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Model Deployment and Monitoring
For deployment, Genie Code can generate code to deploy models to both [batch inference](/concepts/batch-inference-on-databricks.md) and real-time serving endpoints. Additionally, it can diagnose issues and analyze performance for model serving endpoints, helping maintain production reliability. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Integration with the Databricks Platform
Genie Code is deeply integrated with other Databricks capabilities. It leverages [Unity Catalog](/concepts/unity-catalog.md) for governed data discovery, works with [Feature Store](/concepts/feature-store.md) for feature management, and interacts with [Databricks-Managed MLflow](/concepts/databricks-managed-mlflow.md) for experiment tracking and model registry. Its outputs are standard Databricks notebooks that can be versioned, shared, and scheduled. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Use Cases
- **Rapid prototyping**: Data scientists can describe a desired analysis or model in natural language, and Genie Code generates the corresponding notebooks.
- **Collaborative EDA**: Teams can jointly explore datasets using a conversational agent that produces reproducible code.
- **Operational efficiency**: By automating repetitive coding tasks (feature pipelines, deployment scripts), Genie Code frees data scientists to focus on higher‑value work.

## Related Concepts
- [Exploratory Data Analysis](/concepts/exploratory-data-analysis-eda-on-databricks.md)
- AutoML
- [Unity Catalog](/concepts/unity-catalog.md)
- [Feature Store](/concepts/feature-store.md)
- [Model Serving](/concepts/model-serving.md)
- [MLflow](/concepts/mlflow.md)
- Batch Inference
- Real-time Serving

## Sources
- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
