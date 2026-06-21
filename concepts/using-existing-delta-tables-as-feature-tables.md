---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f493b666450959192b6e66d51b437762fcbacf36b222a2b9f4945e428d9f855
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - using-existing-delta-tables-as-feature-tables
    - UEDTAFT
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Using existing Delta tables as feature tables
description: Process of converting an existing Delta table in Unity Catalog into a feature table by adding NOT NULL constraints and a primary key constraint via ALTER TABLE DDL statements.
tags:
  - unity-catalog
  - delta-tables
  - feature-engineering
timestamp: "2026-06-19T10:30:35.928Z"
---

# Using Existing Delta Tables as Feature Tables

In Unity Catalog, any Delta table with a primary key constraint can serve as a feature table. This means you can leverage your existing data infrastructure for machine learning features without needing to create separate storage or migrate data. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Overview

Feature tables in Unity Catalog are standard [Delta tables](/concepts/delta-lake-table.md) that have a primary key constraint defined. They are accessed using the three-level namespace `<catalog-name>.<schema-name>.<table-name>`. Once a primary key is established, the table becomes available in the Features UI and can be used with the Features API for model training and inference. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

To use an existing Delta table as a feature table, the following conditions must be met:

- The table must have a primary key constraint defined. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- The data types in the Delta table must be supported by Feature Engineering in Unity Catalog. See [Supported data types for Feature Engineering](/concepts/supported-data-types-for-feature-stores.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- Feature Engineering in Unity Catalog requires Databricks Runtime 13.2 or above. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- The Unity Catalog [Metastore](/concepts/metastore.md) must have Privilege Model Version 1.0. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Adding a Primary Key to an Existing Delta Table

If your Delta table does not already have a primary key constraint, you can add one using SQL DDL statements. Only the table owner can declare primary key constraints. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

1. **Set primary key columns to `NOT NULL`:**

```sql
ALTER TABLE <full_table_name> ALTER COLUMN <pk_col_name> SET NOT NULL
```

2. **Add the primary key constraint:**

```sql
ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1, pk_col2, ...)
```

By convention, `pk_name` should use the table name (without schema and catalog) with a `_pk` suffix. For example, a table named `ml.recommender_system.customer_features` would have `customer_features_pk` as the primary key constraint name. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

3. **For time series feature tables**, specify the `TIMESERIES` keyword on one of the primary key columns. This requires Databricks Runtime 13.3 LTS or above:

```sql
ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1 TIMESERIES, pk_col2, ...)
```

After adding the primary key constraint, the table appears in the Features UI and can be used as a feature table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using Streaming Tables and Materialized Views as Feature Tables

Any streaming table or materialized view published from [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) that includes a primary key constraint can also serve as a feature table. To add a primary key to an existing streaming table or materialized view, update the schema in the notebook that manages the object and then refresh the table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Note: Lakeflow Spark Declarative Pipelines support for table constraints is in Public Preview and requires using the preview channel. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

The following syntax adds a primary key to a materialized view:

```sql
CREATE OR REFRESH MATERIALIZED VIEW existing_live_table(
  id int NOT NULL PRIMARY KEY,
  ...
) AS SELECT ...
```

## Using Views as Feature Tables

Simple SELECT [Views in Unity Catalog](/concepts/views-in-unity-catalog.md) can also serve as feature tables, requiring `databricks-feature-engineering` version 0.7.0 or above (built into Databricks Runtime 16.0 ML). A simple SELECT view is defined as a view created from a single Delta table with primary keys selected without JOIN, GROUP BY, or DISTINCT clauses. Acceptable SQL keywords are SELECT, FROM, WHERE, ORDER BY, LIMIT, and OFFSET. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
CREATE OR REPLACE VIEW ml.recommender_system.content_recommendation_subset AS
SELECT
    user_id,
    content_id,
    user_age,
    ...
FROM
    ml.recommender_system.content_recommendations_features
WHERE
    user_age BETWEEN 18 AND 35
```

Feature tables backed by views can be used for offline model training and evaluation but cannot be published to online stores or served through model serving endpoints. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Benefits

- **No data migration**: Use existing Delta tables directly without copying or transforming data. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- **Unified governance**: Feature tables benefit from Unity Catalog's governance capabilities, including [Unity Catalog](/concepts/unity-catalog.md) access controls and search. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- **Cross-workspace access**: Feature tables in Unity Catalog are accessible to all workspaces assigned to the table's Unity Catalog [Metastore](/concepts/metastore.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- **Delta Sharing support**: To share feature tables with workspaces not assigned to the same [Metastore](/concepts/metastore.md), use [Delta Sharing](/concepts/delta-sharing.md) (OpenSharing). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- Primary Key Constraints in Delta Tables
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md)
- [Feature Store Overview](/concepts/feature-store.md)
- Delta Tables in Unity Catalog
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
