---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b7e2eede2e0e3093cef552c9286910225c9cfbfdcfcb121286dbe7eab19f094
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakeflow-spark-declarative-pipelines-for-feature-tables
    - LSDPFFT
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Lakeflow Spark Declarative Pipelines for Feature Tables
description: Streaming tables and materialized views created by Lakeflow Spark Declarative Pipelines can include primary key constraints and be used as feature tables in Unity Catalog.
tags:
  - lakeflow
  - pipelines
  - feature-store
timestamp: "2026-06-19T18:49:51.661Z"
---

# Lakeflow Spark Declarative Pipelines for feature tables

**Lakeflow Spark Declarative Pipelines for feature tables** refers to using Databricks’ declarative pipeline framework (formerly Delta Live Tables) to define, publish, and maintain feature tables in Unity Catalog. Any table published from a pipeline that includes a [primary key constraint](/concepts/primary-key-constraints-as-feature-tables.md) can serve as a feature table, enabling automatic feature engineering workflows alongside the pipeline’s streaming or batch data processing.

## Overview

In Unity Catalog, any [Delta table](/concepts/delta-lake-table.md) with a primary key constraint can be used as a feature table. Lakeflow Spark Declarative Pipelines provide a declarative syntax—either Databricks SQL or the [Lakeflow Spark Declarative Pipelines Python programming interface](/concepts/lakeflow-spark-declarative-pipelines.md)—to create materialized views or streaming tables that include the required primary key. Once published, the table becomes available in the Features UI and can be used for model training, batch scoring, and online serving. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

- Lakeflow Spark Declarative Pipelines support for table constraints is in Public Preview. The code examples must be run using the Lakeflow Spark Declarative Pipelines preview channel. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- Feature Engineering in Unity Catalog requires Databricks Runtime 13.2 or above and Privilege Model Version 1.0. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- Only the table owner can declare primary key constraints. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- The data types in the table must be supported by Feature Engineering in Unity Catalog (see Supported data types). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Creating feature tables with Lakeflow Spark Declarative Pipelines

Any table published from a pipeline that includes a primary key constraint can be used as a feature table. The syntax for creating such a table uses `CREATE MATERIALIZED VIEW` (or `CREATE STREAMING TABLE`) with an inline column definition that includes `NOT NULL` and a `CONSTRAINT` clause.

### Using Databricks SQL

The following SQL statement creates a materialized view with a primary key, which can then be registered as a feature table: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
CREATE MATERIALIZED VIEW customer_features (
  customer_id int NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)
) AS SELECT * FROM ...;
```

After the table is created, it can be written to like other Lakeflow Spark Declarative Pipelines datasets and used as a feature table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Using the Python programming interface

The Lakeflow Spark Declarative Pipelines Python API also supports defining primary keys in table declarations. The syntax follows the same logical structure but uses the Python decorator or function-based approach to define the materialized view with column constraints. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Time series feature tables

To create a [Time series feature table](/concepts/time-series-feature-table.md), add a timestamp column as part of the primary key and specify the `TIMESERIES` keyword on that column. This enables point-in-time lookups when using `create_training_set` or `score_batch`. The `TIMESERIES` keyword requires Databricks Runtime 13.3 LTS or above. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### SQL example

```sql
CREATE MATERIALIZED VIEW customer_features (
  customer_id int NOT NULL,
  ts timestamp NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id, ts TIMESERIES)
) AS SELECT * FROM ...;
```

### Python example

The Python API also supports the `TIMESERIES` keyword in the primary key constraint definition. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using an existing streaming table or materialized view as a feature table

Any streaming table or materialized view already published by Lakeflow Spark Declarative Pipelines can become a feature table if it has a primary key constraint. If the table does not yet have one, you must update the schema in the notebook that manages the object and then MUST_REFRESH_SAME_TABLE|refresh the table to update the Unity Catalog object. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

The following SQL syntax adds a primary key to an existing materialized view: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
CREATE OR REFRESH MATERIALIZED VIEW existing_live_table (
  id int NOT NULL PRIMARY KEY,
  ...
) AS SELECT ...;
```

After the refresh, the table appears in the Features UI and can be used as a feature table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Troubleshooting

**Error message: `Feature tables must have a primary key`** – The feature table must have a primary key constraint. If the table does not have one, add it using `ALTER TABLE` or recreate the object with a primary key as shown above. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md)
- [Primary key constraints](/concepts/primary-key-constraints-for-feature-tables.md)
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta tables](/concepts/delta-lake-table.md)
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md)

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
