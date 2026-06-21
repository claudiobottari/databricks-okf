---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad4c4dd07beefc22e50d8210124b1b92ccf0aad912d30f5b5a9057d7346c3cc6
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-assisted-development-genie-code
    - AD(C
    - ai-assisted-development-with-genie-code
    - ADWGC
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: AI-Assisted Development (Genie Code)
description: An integrated AI assistant for development, debugging, and operations across the ML workflow on Databricks
tags:
  - ai-assistance
  - development
  - mlops
timestamp: "2026-06-19T14:22:22.097Z"
---

# AI-Assisted Development (Genie Code)

**AI-Assisted Development (Genie Code)** refers to Databricks' integrated AI assistant that helps data scientists and developers across the full machine learning lifecycle — from initial exploration and prototyping to production monitoring and debugging. Genie Code is embedded directly within notebooks and the Databricks workspace, providing context-aware assistance informed by enterprise-specific knowledge. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Overview

Genie Code is an AI assistant designed to accelerate data science and machine learning workflows on Databricks. Unlike general-purpose coding assistants, Genie Code draws on specialized knowledge of your enterprise context, including workspace assets, Unity Catalog metadata, and existing models and features. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

The assistant is accessible throughout the Databricks workspace, appearing in notebooks, chat interfaces, and model serving dashboards. This ubiquity allows practitioners to receive AI assistance without leaving their current workflow context. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Use Cases Across the ML Lifecycle

### Discovery and Exploration

Genie Code can be used through Genie chat to discover relevant models, data, and features already present in your workspace and Unity Catalog. This helps practitioners avoid duplicating existing work and find the most appropriate assets for their task. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Prototyping and Pipeline Development

During the development phase, Genie Code assists with prototyping pipelines for featurization, model training and tuning, evaluation, and deployment. This includes generating code for data preparation, feature engineering, and model training within notebooks. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Production Monitoring and Debugging

Genie Code integrates with [Model Serving](/concepts/model-serving.md) to help analyze model serving endpoints. Practitioners can use it to diagnose and investigate issues in production, such as unexpected inference behavior, performance degradation, or data drift. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Accessibility

Genie Code is accessible through the following entry points:

- **Genie chat** – A conversational interface for discovering workspace assets and asking questions about your data and models. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]
- **Notebook integration** – Inline assistance for writing and debugging code within Databricks notebooks. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]
- **Model serving endpoints** – Context-aware analysis of production serving endpoints for troubleshooting and optimization. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Integration with Third-Party Tools

In addition to Genie Code, Databricks supports the use of third-party AI coding assistants for developing and maintaining ML pipelines. This extensibility is enabled through Agent skills for AI coding assistants, which provide standardized interfaces for external tools to interact with Databricks resources. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- Genie chat – The conversational interface for workspace discovery and assistance
- Machine Learning Lifecycle – The end-to-end stages where Genie Code provides support
- [Model Serving](/concepts/model-serving.md) – Production serving endpoints that can be analyzed with Genie Code
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that Genie Code queries for asset discovery
- Agent skills for AI coding assistants – Standardized interfaces for third-party coding tools

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
