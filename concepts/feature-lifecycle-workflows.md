---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cabeebe21a536d432a9297dba314bcd6e78991fcb38a7961226ca5f94174307f
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-lifecycle-workflows
    - FLW
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Feature Lifecycle Workflows
description: The end-to-end pipeline covering feature development (create/register), model training (create_training_set), and materialization/serving in Databricks.
tags:
  - feature-engineering
  - ml-pipeline
  - databricks
  - workflow
timestamp: "2026-06-19T14:57:42.684Z"
---

# Feature Lifecycle Workflows

**Feature Lifecycle Workflows** refers to the end-to-end processes for defining, registering, training with, materializing, and serving machine learning features using the Databricks Declarative Feature Engineering APIs. These workflows enable data scientists and ML engineers to manage features as first-class entities within Unity Catalog.

## Overview

The Declarative Feature Engineering APIs provide a structured approach to managing the complete lifecycle of ML features. Features can be defined from various data sources, persisted to Unity Catalog, used in model training, materialized for efficient serving, and deployed to online stores for real-time inference. ^[declarative-features-databricks-on-aws.md]

## Feature Development Workflow

The feature development phase involves defining feature objects and optionally persisting them to Unity Catalog:

- **`create_feature`**: Defines a feature and immediately registers it in Unity Catalog. This is the recommended one-step approach for production workflows. ^[declarative-features-databricks-on-aws.md]
- **Local construction with `register_feature`**: Alternatively, you can construct `Feature` objects locally and persist them to Unity Catalog later using `register_feature`. Locally constructed features can also be used directly with `create_training_set` before registration. ^[declarative-features-databricks-on-aws.md]

Features can be defined using multiple source types, including [Delta Table Sources](/concepts/deltatablesource.md) and Request-Time Data, with computations ranging from time-windowed aggregations to simple column selections. ^[declarative-features-databricks-on-aws.md]

## Model Training Workflow

The training workflow uses `create_training_set` to perform point-in-time correct feature computation for machine learning. This function:

- Takes a labeled DataFrame and a set of feature definitions
- Computes features at the correct point in time for each training row
- Returns a training set that can be loaded as a DataFrame for model training ^[declarative-features-databricks-on-aws.md]

After training, `log_model` captures the feature metadata alongside the model for consistent inference. ^[declarative-features-databricks-on-aws.md]

## Feature Materialization and Serving Workflow

After defining features, you can materialize them for efficient reuse in training and serving:

### Materialization Options

- **Offline store**: Materialize features for batch training and offline inference workloads
- **Online store**: Materialize features for real-time serving, supporting CPU model serving ^[declarative-features-databricks-on-aws.md]

### Materialization Triggers

- **`CronSchedule`**: Schedule regular materialization with quartz cron expressions (e.g., hourly updates)
- **`TableTrigger`**: Trigger materialization based on source table changes (supported for `ColumnSelection` features) ^[declarative-features-databricks-on-aws.md]

Materialized features can be used with `create_training_set` to prepare offline batch training datasets, or served through online endpoints for low-latency inference. ^[declarative-features-databricks-on-aws.md]

## Best Practices

### Feature Naming
- Use descriptive names for business-critical features
- Follow consistent naming conventions across teams
- Leverage auto-generated names during feature development ^[declarative-features-databricks-on-aws.md]

### Time Windows
- Align window boundaries with business cycles (daily, weekly)
- Shorter windows capture recent trends but can be noisy; longer windows produce more stable distributions
- Tumbling and sliding windows are more scalable than rolling windows; start with sliding windows for most use cases ^[declarative-features-databricks-on-aws.md]

### Performance
- Materialize features from the same data source in a single `materialize_features` call to minimize data scans
- Use the same granularity (e.g., all 1-hour or all 1-day slide durations) for features on the same data source to enable better grouping during materialization ^[declarative-features-databricks-on-aws.md]

### Entity Columns vs. Filter Conditions
- Use `entity` when different aggregation levels are needed (e.g., customer-level vs. customer-merchant features)
- Use `filter_condition` on data sources when filtering rows at the same aggregation level (e.g., high-value transactions only) ^[declarative-features-databricks-on-aws.md]

## Common Patterns

### Customer Analytics (RFM Analysis)
Create recency, frequency, and monetary features using time-windowed aggregations on transaction data with rolling windows. ^[declarative-features-databricks-on-aws.md]

### Trend Analysis
Compare recent vs. historical behavior by creating features with different window durations and delays (e.g., 7-day average vs. 7-day average from 7 days ago). ^[declarative-features-databricks-on-aws.md]

### Seasonal Patterns
Capture seasonal behavior using features with delays aligned to business cycles (e.g., same day of week, 4 weeks ago). ^[declarative-features-databricks-on-aws.md]

## Limitations

- Entity and timeseries column names must match between training datasets and feature definitions when using `create_training_set`
- Label columns in training datasets should not exist in source tables used for feature definitions
- Only a limited set of UDAF functions is supported in the `create_feature` API
- Entity columns cannot be of type `DATE` or `TIMESTAMP`
- `RequestSource` supports only scalar data types; complex types are not supported
- `RequestSource` does not support aggregation functions or time windows - only `ColumnSelection` functions ^[declarative-features-databricks-on-aws.md]

## Requirements

- Classic compute cluster running Databricks Runtime 17.0 ML or above
- Installation of the `databricks-feature-engineering>=0.15.0` Python package ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Feature Store](/concepts/feature-store.md)
- [Point-in-time correctness](/concepts/point-in-time-correctness.md)
- [Online Feature Serving](/concepts/online-feature-serving.md)
- MLflow Model Serving

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
