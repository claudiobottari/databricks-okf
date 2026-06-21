---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c44407edb5011fdcb31e30b0f9727f4547f3f24e48b62f5825e19c701b9daf9
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-ai-assisted-development
    - GC(D
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: Genie Code (AI-Assisted Development)
description: An AI assistant integrated across notebooks and workspace on Databricks, used for development, debugging, and ongoing operations with specialized knowledge of enterprise context.
tags:
  - ai-assistant
  - development
  - databricks
timestamp: "2026-06-18T11:06:01.273Z"
---

# Genie Code (AI-Assisted Development)

**Genie Code** is an AI assistant integrated across Databricks notebooks and the workspace that supports development, debugging, and ongoing operations for data science and machine learning workflows. It draws on specialized knowledge of your enterprise context to provide contextual assistance throughout the ML lifecycle.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Overview

Genie Code is part of Databricks' AI-assisted development and operations capabilities. It can be used at every step of the data science and machine learning workflow, from initial discovery through production monitoring.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Key Capabilities

### Discovery and Exploration

Use Genie chat to discover relevant models, data, and features in your workspace and [Unity Catalog](/concepts/unity-catalog.md). This helps data scientists quickly find existing assets before starting new work.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Prototyping and Development

Use Genie Code to prototype pipelines for featurization, model training and tuning, evaluation, and deployment. It assists with writing and debugging code directly in notebooks.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Production Monitoring

Analyze [model serving endpoints](/concepts/model-serving-endpoint.md) with Genie Code to diagnose and investigate issues in production deployments. This enables ongoing operations support for deployed models.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Integration with the ML Lifecycle

Genie Code supports the full [ML Lifecycle](/concepts/ml-lifecycle.md) across all key stages:

- **Scope the use case** — Define prediction targets, success metrics, and production requirements.
- **Run exploratory data analysis (EDA)** — Understand data distributions, predictive signals, and data quality issues.
- **Prepare data and features** — Build pipelines for feature engineering, managed within a [Feature Store](/concepts/feature-store.md).
- **Train models and track experiments** — Log experiment metadata for analysis and deployment.
- **Evaluate model quality** — Assess against held-out data and stakeholder criteria.
- **Register, stage, and test models** — Prepare models before promoting to production.
- **Deploy to production** — Set up real-time endpoints or batch inference jobs.
- **Monitor and retrain** — Adapt models to changing data or user behavior.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Third-Party AI Coding Tools

In addition to Genie Code, you can also use third-party coding tools to develop and maintain ML pipelines on Databricks. See Agent skills for AI coding assistants for more information.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- Genie chat — The conversational interface for discovering assets in your workspace
- [ML Lifecycle](/concepts/ml-lifecycle.md) — The end-to-end journey from raw data to production model
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for data and ML assets
- [Model serving endpoints](/concepts/model-serving-endpoint.md) — Production infrastructure for real-time and batch inference
- [Feature Store](/concepts/feature-store.md) — Managed repository for machine learning features
- Agent skills for AI coding assistants — Third-party AI coding tool integration

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
