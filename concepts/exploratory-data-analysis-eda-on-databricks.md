---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22a6c865d56a90f8a774ffb6dbb9ee057237e0d4b6d16f42765dc01630cb886a
  pageDirectory: concepts
  sources:
    - machine-learning-lifecycle-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - exploratory-data-analysis-eda-on-databricks
    - EDA(OD
    - Exploratory Data Analysis
    - exploratory data analysis (EDA)
  citations:
    - file: machine-learning-lifecycle-databricks-on-aws.md
title: Exploratory Data Analysis (EDA) on Databricks
description: The process of summarizing and visualizing datasets to surface distributions, correlations, missing values, and outliers, supported by Databricks tools including notebooks, dashboards, Genie Chat, and Genie Code.
tags:
  - machine-learning
  - data-analysis
  - databricks-tools
timestamp: "2026-06-19T19:20:17.894Z"
---

# Exploratory Data Analysis (EDA) on Databricks

**Exploratory Data Analysis (EDA)** is the process of summarizing and visualizing a dataset to surface distributions, correlations, missing values, and outliers that shape downstream modeling decisions. On Databricks, EDA is an early and critical stage in the [machine learning lifecycle](/concepts/cicd-for-machine-learning.md), typically occurring after scoping the use case but before preparing data and features. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Purpose and Goals

During EDA, practitioners answer questions that inform the rest of the ML lifecycle:

- Which inputs are most predictive of the target, and are any of them unavailable at serving time?
- Are there missing values, outliers, or skewed distributions that require cleaning or transformation?
- Is the dataset large enough, and representative enough, to learn the target pattern?

Early on, practitioners must also decide how to verify they have valid test data that is held back from training. Even during EDA, care must be taken to avoid making modeling decisions based on test data. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Tools and Capabilities

Databricks provides interactive, collaborative, and AI-assisted tools for EDA. Users can explore data using natural language chat, UIs, or code, and collaborate through both real-time co-editing and Git-based code sharing: ^[machine-learning-lifecycle-databricks-on-aws.md]

- **Notebooks**: Provide collaborative spaces for exploration, visualization, and documentation.
- **Dashboards**: Provide SQL and visualization-based exploration.
- **Genie Chat**: Provides a full-page, natural-language interface for asking data questions.
- **[Genie Code](/concepts/genie-code.md)**: Can perform fully automated EDA or act as an interactive assistant.

## EDA in the ML Lifecycle

EDA fits into the broader ML lifecycle between scope definition and data preparation. After exploring and understanding the data, practitioners proceed to prepare data and features, using the insights gained during EDA to guide [feature engineering](/concepts/featureengineeringclient-api.md) decisions. The transformation identified during EDA become inputs to [Data Quality Monitoring](/concepts/data-quality-monitoring.md) and other downstream processes. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Related Concepts

- Machine Learning Lifecycle
- [Data Profiling](/concepts/data-profiling.md)
- [Feature Engineering](/concepts/featureengineeringclient-api.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for discovering and managing data assets explored during EDA

## Sources

- machine-learning-lifecycle-databricks-on-aws.md

# Citations

1. [machine-learning-lifecycle-databricks-on-aws.md](/references/machine-learning-lifecycle-databricks-on-aws-d195211f.md)
