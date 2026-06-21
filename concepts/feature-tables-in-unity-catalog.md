---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60f711b7bd3933c2fb5552e62884eae283159805f387bea6d422328a4df2d849
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-tables-in-unity-catalog
    - FTIUC
    - Feature Store in Unity Catalog
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Feature Tables in Unity Catalog
description: Any Delta table with a primary key constraint in Unity Catalog can serve as a feature table for machine learning, accessible via a three-level namespace.
tags:
  - feature-store
  - unity-catalog
  - machine-learning
timestamp: "2026-06-19T18:48:51.967Z"
---

# Feature Tables in Unity Catalog

**Feature tables** in Unity Catalog are Delta tables with a primary key constraint that serve as the foundation for machine learning feature storage and management. Any Delta table in Unity Catalog that has a primary key defined can function as a feature table, enabling organizations to store, discover, and govern features alongside other data assets using Unity Catalog's unified governance model. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Overview

Feature tables in Unity Catalog are accessed using the three-level namespace: `<catalog-name>.<schema-name>.<table-name>`. They are Delta tables that must have a primary key constraint. Feature tables can be created using Databricks SQL, the Python `FeatureEngineeringClient`, or [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Feature tables in Unity Catalog are accessible to all workspaces assigned to the table's Unity Catalog [Metastore](/concepts/metastore.md). To share feature tables with workspaces not assigned to the same [Metastore](/concepts/metastore.md), use [Delta Sharing](/concepts/delta-sharing.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

Feature Engineering in Unity Catalog requires Databricks Runtime 13.2 or above. The Unity Catalog [Metastore](/concepts/metastore.md) must have Privilege Model Version 1.0. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

The Python client `FeatureEngineeringClient` is available on PyPI with the `databricks-feature-engineering` package and is pre-installed in Databricks Runtime 13.3 LTS ML and above. For non-ML Databricks Runtimes, manual installation is required. Use the compatibility matrix to find the correct version for your runtime. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Creating Feature Tables

### Using Databricks SQL

You can create a feature table by defining a Delta table with a primary key constraint:

```sql
CREATE TABLE ml.recommender_system.customer_features (
  customer_id int NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)
);
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Time Series Feature Tables

To create a [Time series feature table](/concepts/time-series-feature-table.md), add a time column as a primary key column and specify the `TIMESERIES` keyword. This requires Databricks Runtime 13.3 LTS or above:

```sql
CREATE TABLE ml.recommender_system.customer_features (
  customer_id int NOT NULL,
  ts timestamp NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id, ts TIMESERIES)
);
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Using Lakeflow Spark Declarative Pipelines

Any table published from Lakeflow Spark Declarative Pipelines that includes a primary key constraint can be used as a feature table. Lakeflow Spark Declarative Pipelines support for table constraints is in Public Preview and requires the preview channel. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
CREATE MATERIALIZED VIEW customer_features (
  customer_id int NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)
) AS SELECT * FROM ...;
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using Existing Tables as Feature Tables

### Existing Delta Tables

Any Delta table in Unity Catalog with a primary key can serve as a feature table. If an existing table does not have a primary key constraint, you can add one:

1. Set primary key columns to `NOT NULL`:
   ```sql
   ALTER TABLE <full_table_name> ALTER COLUMN <pk_col_name> SET NOT NULL
   ```

2. Add the primary key constraint:
   ```sql
   ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1, pk_col2, ...)
   ```

Only the table owner can declare primary key constraints. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

For time series feature tables, include the `TIMESERIES` keyword on the relevant primary key column:

```sql
ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1 TIMESERIES, pk_col2, ...)
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Existing Views

A simple SELECT view in Unity Catalog can be used as a feature table with `databricks-feature-engineering` version 0.7.0 or above (built into Databricks Runtime 16.0 ML). A simple SELECT view is defined as a view created from a single Delta table without JOIN, GROUP BY, or DISTINCT clauses. Acceptable keywords are SELECT, FROM, WHERE, ORDER BY, LIMIT, and OFFSET. Feature tables backed by views do not appear in the Features UI and cannot be published to online stores. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Existing Streaming Tables or Materialized Views (Lakeflow Spark Declarative Pipelines)

To use an existing streaming table or materialized view created by Lakeflow Spark Declarative Pipelines as a feature table, update the schema definition in the notebook that manages the object to include the primary key, then refresh the table. Only the table owner can declare primary key constraints. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Updating Feature Tables

### Adding New Features

You can add new features to an existing feature table by updating the feature computation function and running `write_table` with the returned DataFrame, or by creating a new feature computation function that calculates new feature values and writing them using the same primary key. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Updating Specific Rows

Use `mode = "merge"` in `write_table` to update only specific rows. Rows whose primary key does not exist in the DataFrame remain unchanged:

```python
from databricks.feature_engineering import FeatureEngineeringClient
fe = FeatureEngineeringClient()
fe.write_table(
  name='ml.recommender_system.customer_features',
  df = customer_features_df,
  mode = 'merge'
)
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Scheduled Updates

Databricks recommends creating a scheduled job that runs a notebook to update feature tables regularly (for example, daily) to ensure feature values are always current. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Streaming Updates

To create a streaming feature computation pipeline, pass a streaming DataFrame as an argument to `write_table`. This method returns a `StreamingQuery` object. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Storing Past Values

Define a feature table with a composite primary key that includes a date column. Databricks recommends enabling [Liquid Clustering](/concepts/liquid-clustering.md) on the table for efficient reads. If not using liquid clustering, set the date column as a partition key. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Reading from Feature Tables

Use `read_table` to read feature values:

```python
from databricks.feature_engineering import FeatureEngineeringClient
fe = FeatureEngineeringClient()
customer_features_df = fe.read_table(
  name='ml.recommender_system.customer_features',
)
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Searching and Browsing

Use the Features UI in the sidebar to search for or browse feature tables. You can search by feature table name, feature name, comment, or tag key/value. Search text is case-insensitive. Use `get_table` to retrieve feature table metadata programmatically. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Tags

Tags (key-value pairs) can be used to categorize and manage feature tables and features. For feature tables, tags can be created, edited, and deleted using Catalog Explorer, SQL statements, or the Feature Engineering Python API. For features, tags can be managed using Catalog Explorer or SQL statements. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Deleting Feature Tables

You can delete a feature table by dropping the underlying Delta table using Catalog Explorer, SQL, or the Feature Engineering Python API. Deleting a feature table can cause unexpected failures in upstream producers and downstream consumers (models, endpoints, and scheduled jobs). Published online stores must be deleted separately with your cloud provider. `drop_table` is not supported in Databricks Runtime 13.1 ML or below. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
DROP TABLE ml.recommender_system.customer_features;
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Metadata Restrictions

The following feature table metadata should not be updated after creation:
- Primary key
- Partition key
- Name or data type of an existing feature

Altering these will cause downstream pipelines that use features for training and serving models to break. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Troubleshooting

**Error message: `Feature tables must have a primary key`**

The feature table must have a primary key constraint. If the table does not have one, use `ALTER TABLE` DDL statements to add the constraint. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The broader framework for managing ML features
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables with point-in-time lookup capabilities
- [Online Feature Stores](/concepts/online-feature-store.md) — Publishing features for real-time serving
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for feature tables
- [Delta Sharing](/concepts/delta-sharing.md) — Sharing feature tables across metastores
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — Creating feature tables through pipelines
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended for efficient reads on feature tables with past values

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
