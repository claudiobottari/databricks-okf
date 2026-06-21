---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6eed28845ccdb978fde494aec89b8765e7d302fe3d7ee6291fd65659a309216
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-profile
    - Inference profiles
    - inference profiles
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
    - file: data-profiling-databricks-on-aws.md
title: Inference Profile
description: A data profile type for monitoring ML model predictions, requiring problem type (classification/regression), prediction column, and model ID column.
tags:
  - machine-learning
  - model-monitoring
  - data-profiling
timestamp: "2026-06-19T17:56:06.463Z"
---

# Inference Profile

An **Inference Profile** is a type of data profile in [Unity Catalog](/concepts/unity-catalog.md) that analyzes and monitors the quality of machine learning inference data over time. It is designed to track model predictions, compare them against ground truth labels, and detect [anomalies](/concepts/anomaly-detection.md) in model behavior, such as data drift or performance degradation. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md, data-profiling-databricks-on-aws.md]

## Overview

Inference profiles extend the capabilities of [Time Series Profile](/concepts/time-series-profile.md) by adding model-specific metrics. They are particularly useful for [Production Monitoring](/concepts/production-monitoring.md) of ML models, allowing data scientists and engineers to track prediction quality, monitor for concept drift, and validate model performance against ground truth data. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md, data-profiling-databricks-on-aws.md]

You can use inference profiles to answer questions such as: How are ML model inputs and predictions shifting over time? How is model performance trending over time? Is model version A performing better than model version B? ^[data-profiling-databricks-on-aws.md]

## Creating an Inference Profile

Inference profiles can be created through the Databricks UI or via the API. When first created, the profile analyzes only data from the 30 days prior to its creation. After creation, all new data is processed incrementally. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md, data-profiling-databricks-on-aws.md]

### Prerequisites

- [Unity Catalog](/concepts/unity-catalog.md) must be enabled for your workspace and you must have access to Databricks SQL. ^[data-profiling-databricks-on-aws.md]
- [Anomaly Detection](/concepts/anomaly-detection.md) must be enabled for the schema containing the table you want to profile. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- You must have the following privileges: `USE CATALOG` on the catalog, `USE SCHEMA` on the schema, `SELECT` on the table, and `MANAGE` on the catalog, schema, or table. ^[data-profiling-databricks-on-aws.md]
- It is a best practice to enable change data feed (CDF) on your table. When CDF is enabled, only newly appended data is processed rather than re-processing the entire table every refresh, making execution more efficient and reducing costs as you scale profiling across many tables. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Required Parameters

- **Metric granularities**: Determines how to partition the data in windows across time. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Timestamp column**: The column containing timestamps, which must be of type `TIMESTAMP` or convertible using `to_timestamp`. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Problem type**: Either classification or regression. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Prediction column**: The column containing the model's predicted values. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Model ID column**: The column containing the ID of the model used for prediction. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Label column** (optional): The column containing the ground truth for model predictions. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Advanced Options

When configuring an inference profile, you can specify additional settings:

- **Schedule**: Set the profile to run on a scheduled basis or refresh manually. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Notifications**: Configure up to 5 email addresses per notification event type. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Metrics tables schema name**: The Unity Catalog schema where metric tables are stored (defaults to the same schema as the profiled table). ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Assets directory**: The absolute path to store profiling assets (defaults to `/Users/{user_name}/databricks_lakehouse_monitoring/{table_name}`). For profiles intended to be shared within an organization, you can use a path in the `/Shared/` directory. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Unity Catalog baseline table name**: A table or view containing baseline data for comparison. A good choice for a baseline is the data that was used to train or validate the model being profiled. The baseline table should contain the same feature columns as the primary table and the same `model_id_col` specified for the primary table. Ideally, the test or validation set used to evaluate the model should be used to ensure comparable model quality metrics. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md, data-profiling-databricks-on-aws.md]
- **Metric slicing expressions**: Define subsets of the table to profile in addition to the whole table. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Custom metrics**: Define additional metrics through SQL code. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## How Inference Profiles Work

To profile the performance of a machine learning model, you attach the profile to an inference table that holds the model's inputs and corresponding predictions. Inference profiles compute metrics for the entire table, for time windows and data subsets (or "slices") specified during profile creation, and for each model ID. ^[data-profiling-databricks-on-aws.md]

### Metric Tables and Dashboard

Profiling creates two metric tables and a dashboard:

- **Profile metric table**: Contains summary statistics for the profiled data. ^[data-profiling-databricks-on-aws.md]
- **Drift metrics table**: Contains statistics related to the data's drift over time. If a baseline table is provided, drift is also profiled relative to the baseline values. ^[data-profiling-databricks-on-aws.md]

The metric tables are Delta tables stored in a Unity Catalog schema that you specify. You can view these tables using the Databricks UI, query them using Databricks SQL, and create dashboards and alerts based on them. For each profile, Databricks automatically creates a fully customizable dashboard to help visualize and present profile results. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [Time Series Profile](/concepts/time-series-profile.md)
- [Snapshot Profile](/concepts/snapshot-profile.md)
- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- [Inference Tables](/concepts/inference-tables.md)

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md
- data-profiling-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
2. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
