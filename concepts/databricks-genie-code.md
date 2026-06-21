---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 801b2a16c351639b6a019b924c20e0a2814555bdb70a4b9ccf4a297db702c27a
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-genie-code
    - DGC
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Databricks Genie Code
description: An AI assistant within Databricks that performs automated exploratory data analysis, natural language AutoML, code generation for data preparation and feature pipelines, and diagnosis of model serving endpoints.
tags:
  - ai-assistant
  - automl
  - databricks
  - code-generation
timestamp: "2026-06-19T09:50:04.966Z"
---

# Databricks Genie Code

**Databricks Genie Code** is an AI-powered assistant integrated into the Databricks platform that accelerates data science and machine learning workflows by interpreting natural language requests and generating executable code. It is accessible from notebooks and can function as either a fully automated agent or an interactive, collaborative assistant. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Capabilities

### Exploratory Data Analysis (EDA)
Genie Code can perform fully automated exploratory data analysis or act as an interactive assistant that responds to natural-language questions about the data. This allows data scientists to quickly understand dataset characteristics, distributions, and correlations without writing manual analysis code. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Data Discovery and Feature Preparation
The tool integrates with [Unity Catalog](/concepts/unity-catalog.md) to browse available tables and discover relevant data sources. It can suggest feature transformations and generate code for data ingestion and feature pipelines, streamlining the preparation stage of ML workflows. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Intelligent AutoML
Genie Code provides intelligent AutoML capabilities: given a natural-language description of the desired machine learning task, it can build complete multi-notebook workflows that include featurization, model training, hyperparameter tuning, evaluation, and deployment code. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Model Deployment and Endpoint Diagnostics
For model serving, Genie Code can generate the code needed to deploy models to production endpoints. It can also diagnose issues and performance problems for existing [Model Serving](/concepts/model-serving.md) endpoints, helping operators troubleshoot latency, errors, or other runtime concerns. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## How It Works
Genie Code operates within Databricks notebooks, interpreting user prompts in natural language and producing Scala, Python, or SQL code as output. It leverages metadata from Unity Catalog to understand the data landscape and can chain multiple notebook cells into an automated pipeline. The assistant is designed to be used throughout the DS/ML lifecycle — from initial exploration through feature engineering, training, and production monitoring.

## Related Concepts
- [Unity Catalog](/concepts/unity-catalog.md) – governed data catalog used by Genie Code for table discovery and lineage.
- [Managed MLflow](/concepts/databricks-managed-mlflow.md) – tracking and registry integrated with Genie Code workflows.
- AutoML – automated machine learning approach that Genie Code implements.
- [Model Serving](/concepts/model-serving.md) – endpoint deployment and diagnostics supported by Genie Code.
- Notebooks – the primary interface for interacting with Genie Code.

## Sources
- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
