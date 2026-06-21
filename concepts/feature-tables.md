---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 624f59c2f958d5524b8714b273433ae28e62844477edffb421240e7e26824b44
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-tables
    - Feature Table Tags
    - Feature Flag
    - Feature Table Management
    - Tags on Feature Tables
    - shared tables
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
title: Feature Tables
description: Organized collections of features backed by Delta tables with primary keys, tracked with metadata about data sources, notebooks, and jobs that created them.
tags:
  - feature-engineering
  - databricks
  - data-management
timestamp: "2026-06-19T14:49:17.177Z"
---

# Feature Tables

**Feature Tables** are the core organizational unit of the [Databricks Feature Store](/concepts/databricks-feature-store.md). They group related features into a single table that can be reused across multiple machine learning models, ensuring consistency between training and inference. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Definition and Characteristics

Every feature table must have a **primary key** and is backed by a [Delta table](/concepts/delta-lake-table.md) plus additional metadata. The metadata tracks the data sources from which the table was generated and the notebooks or jobs that created or wrote to the table. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

Features within a table are typically computed and updated using a common computation function. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Unity Catalog vs. Workspace Feature Store

The way feature tables are managed depends on whether the workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md):

- **Unity Catalog workspaces** (Databricks Runtime 13.3 LTS and above): Any Delta table in Unity Catalog that includes a primary key constraint can be used as a feature table. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- **Workspace Feature Store (legacy)**: Workspaces not enabled for Unity Catalog that were created before August 19, 2024 may use the legacy Workspace Feature Store. Feature tables stored there are called *Workspace feature tables*. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Time Series Feature Tables

A *time series feature table* includes a timestamp column that enables point-in-time lookups. This ensures that each row in a training dataset reflects the latest known feature values as of that row’s timestamp. Time series tables are recommended when feature values change over time (e.g., event-based or time-aggregated data). ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

To create a time series feature table, you specify time-related columns within the primary keys using the `timeseries_columns` argument (Unity Catalog) or the `timestamp_keys` argument (Workspace Feature Store). The system then performs an as-of-timestamp join when you build a training set or perform batch scoring. If you do **not** use these arguments and simply designate a timestamp column as a primary key, the Feature Store will match only rows with an exact time match rather than all rows prior to the timestamp. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Usage in the ML Workflow

Feature tables are consumed through several APIs:

- **[FeatureLookup](/concepts/featurelookup.md)**: Specifies which features (columns) to select from a feature table and which lookup key to use to join the table to label data when creating a training dataset. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- **[Training Set](/concepts/training-set-feature-store.md)**: A list of `FeatureLookup` objects combined with a raw training DataFrame and a label column. Model training uses this training set as input. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- **[FeatureSpec](/concepts/featurespec.md)**: A Unity Catalog entity that packages `FeatureLookup`s from feature tables and [FeatureFunction](/concepts/featurefunction.md)s into a reusable unit for serving. FeatureSpecs always reference offline feature tables but require the tables to be published to an [Online Feature Store](/concepts/online-feature-store.md) for real-time serving. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- **Publishing to an online store**: Feature tables can be published to the Databricks Online Feature Store (powered by Lakebase) for low-latency access during real-time inference. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md)
- [Delta table](/concepts/delta-lake-table.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Primary Key
- [FeatureLookup](/concepts/featurelookup.md)
- [FeatureSpec](/concepts/featurespec.md)
- [Online Feature Store](/concepts/online-feature-store.md)
- [Time Series Feature Tables (Point-in-Time Lookups)](/concepts/time-series-feature-table-point-in-time-lookup.md)
- [Workspace Feature Store (legacy)](/concepts/databricks-workspace-feature-store-legacy.md)
- [Model Packaging](/concepts/model-packaging.md)

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
