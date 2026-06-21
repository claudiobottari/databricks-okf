---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7babb3756197cadde00beef5a6ca79088d0f8c2b4e9e983b29ae22d4c98c2322
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-tables-and-materialized-views-as-feature-tables
    - Materialized Views as Feature Tables and Streaming Tables
    - STAMVAFT
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Streaming Tables and Materialized Views as Feature Tables
description: Streaming tables and materialized views created by Lakeflow Spark Declarative Pipelines with primary key constraints can be used as feature tables.
tags:
  - dlt
  - lakeflow
  - streaming
  - feature-store
  - materialized-views
timestamp: "2026-06-18T12:20:02.446Z"
---

# Streaming Tables and Materialized Views as Feature Tables

**Streaming tables and materialized views** created by [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) can serve as [Feature Tables](/concepts/feature-tables.md) in [Unity Catalog](/concepts/unity-catalog.md) when they include a [primary key constraint](/concepts/primary-key-constraints-as-feature-tables.md). This enables real-time and incremental feature computation pipelines that are automatically governed by Unity Catalog's data management capabilities. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

- Lakeflow Spark Declarative Pipelines support for table constraints is in **Public Preview**. Code examples must be run using the Lakeflow Spark Declarative Pipelines [preview channel](https://docs.databricks.com/aws/en/release-notes/dlt/#runtime-channels). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- Only the table owner can declare primary key constraints. The owner's name is displayed on the table detail page of Catalog Explorer. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- Verify that Feature Engineering in Unity Catalog supports the data type in the Delta table. See [Supported Data Types for Feature Engineering](/concepts/supported-data-types-for-feature-stores.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Creating a Feature Table with a Primary Key

To create a streaming table or materialized view that functions as a feature table, define the primary key constraint directly in the table definition using either Databricks SQL or the Lakeflow Spark Declarative Pipelines Python programming interface. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Using Databricks SQL

```sql
CREATE MATERIALIZED VIEW customer_features (
  customer_id int NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)
) AS SELECT * FROM ...;
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Time Series Feature Tables

To create a [Time series feature table](/concepts/time-series-feature-table.md), add a time column as a primary key column and specify the `TIMESERIES` keyword. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
CREATE MATERIALIZED VIEW customer_features (
  customer_id int NOT NULL,
  ts timestamp NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id, ts TIMESERIES)
) AS SELECT * FROM ...;
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

After the table is created, you can write data to it like other Lakeflow Spark Declarative Pipelines datasets, and it can be used as a feature table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using an Existing Streaming Table or Materialized View as a Feature Table

Any existing streaming table or materialized view in Unity Catalog with a primary key can be used as a feature table. If the table does not already have a primary key, you must modify the schema of the streaming table or materialized view in the notebook that manages the object, then MUST_REFRESH_SAME_TABLE|refresh the table to update the Unity Catalog object. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Adding a Primary Key to an Existing Materialized View

Use the following syntax to add a primary key to an existing materialized view:

```sql
CREATE OR REFRESH MATERIALIZED VIEW existing_live_table(
  id int NOT NULL PRIMARY KEY,
  ...
) AS SELECT ...
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Benefits of Streaming Tables and Materialized Views as Feature Tables

- **Incremental computation**: Streaming tables process data as it arrives, keeping features up to date without full recomputation.
- **Unified governance**: All feature tables are managed under Unity Catalog's governance model, including [Governed Tags](/concepts/governed-tags.md), ABAC policies, and [audit logging](/concepts/abac-policy-audit-logging.md).
- **Declarative pipelines**: Lakeflow Spark Declarative Pipelines handle orchestration, dependency management, and incremental processing automatically.
- **Time series support**: Enable point-in-time lookups for historical feature values when using `create_training_set` or `score_batch`. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Limitations

- Lakeflow Spark Declarative Pipelines support for table constraints is in Public Preview and requires the preview channel.
- Feature tables backed by streaming tables or materialized views cannot be published to online stores.
- Only simple SELECT views (without JOIN, GROUP BY, or DISTINCT) can be used as feature tables — this restriction does not apply to streaming tables or materialized views created by Lakeflow Spark Declarative Pipelines. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Scheduling Updates

To ensure feature tables always have the most recent values, Databricks recommends creating a [scheduled job](/concepts/scheduled-jobs-with-ai-runtime.md) that runs a notebook to update your feature table on a regular basis. For streaming tables, the incremental processing handles continuous updates automatically. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — General overview of feature tables, including creating, updating, and managing them
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) — SQL syntax for defining primary keys on Delta tables
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables that support point-in-time lookups
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — The pipeline framework for creating and managing streaming tables and materialized views
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — Python API for interacting with feature tables
- Delta Tables in Unity Catalog — The underlying storage format for feature tables

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
