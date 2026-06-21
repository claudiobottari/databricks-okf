---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1cd051519897862664adb99e98c3dd6a14d05fbb586d0a60b0e0b6d4ccc2603
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - primary-key-constraints-for-feature-tables
    - PKCFFT
    - Primary Key Constraints
    - Primary key constraints
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Primary Key Constraints for Feature Tables
description: Feature tables require a primary key constraint defined via NOT NULL columns and ALTER TABLE ADD CONSTRAINT DDL; only the table owner can declare it.
tags:
  - delta-tables
  - sql
  - constraints
  - feature-store
timestamp: "2026-06-18T12:19:29.973Z"
---

# Primary Key Constraints for Feature Tables

In [Unity Catalog](/concepts/unity-catalog.md), any [Delta table](/concepts/delta-lake-table.md) that has a primary key constraint can serve as a feature table. The primary key is a required component of a feature table — it uniquely identifies each row and enables feature lookups during training and serving. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

Feature Engineering in Unity Catalog requires Databricks Runtime 13.2 or above, and the Unity Catalog [Metastore](/concepts/metastore.md) must use Privilege Model Version 1.0. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Creating a Feature Table with a Primary Key

You can create a feature table with a primary key using Databricks SQL, the [Feature Engineering Python client](/concepts/featureengineeringclient-python-client.md) (`FeatureEngineeringClient`), or [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md).

### Using Databricks SQL

Define the table with `NOT NULL` columns for the primary key and a `CONSTRAINT` clause. The following example creates a feature table with a single primary key column:

```sql
CREATE TABLE ml.recommender_system.customer_features (
  customer_id int NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)
);
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Using the Python Client

The `FeatureEngineeringClient` can create a table, but the example in the source focuses on registering an existing table. The underlying Delta table must already have a primary key constraint. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Using Lakeflow Spark Declarative Pipelines (Preview)

Streaming tables and materialized views published from Lakeflow Spark Declarative Pipelines can serve as feature tables if they include a primary key constraint. Define the constraint in the `CREATE MATERIALIZED VIEW` or `CREATE STREAMING TABLE` statement. This feature is in Public Preview and requires the pipeline’s preview channel. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
CREATE MATERIALIZED VIEW customer_features (
  customer_id int NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)
) AS SELECT * FROM ...;
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Time Series Feature Tables

To create a [Time series feature table](/concepts/time-series-feature-table.md), add a timestamp column as a primary key column and specify the `TIMESERIES` keyword on that column. This requires Databricks Runtime 13.3 LTS or above.

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

## Using an Existing Delta Table as a Feature Table

Any existing [Delta table](/concepts/delta-lake-table.md) in Unity Catalog that already has a primary key constraint can be used as a feature table immediately. If the table does not have a primary key, you must add one:

1. Set each primary key column to `NOT NULL`:
   ```sql
   ALTER TABLE <full_table_name> ALTER COLUMN <pk_col_name> SET NOT NULL
   ```
2. Add the primary key constraint:
   ```sql
   ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1, pk_col2, ...)
   ```

The constraint name conventionally uses the table name with a `_pk` suffix (e.g., `customer_features_pk`). After adding the constraint, the table appears in the Features UI and can be used as a feature table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Only the table owner can declare primary key constraints. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using a Streaming Table or Materialized View from Lakeflow Spark Declarative Pipelines

To use an existing streaming table or materialized view as a feature table, update its schema in the managing notebook to include the primary key constraint, then MUST_REFRESH_SAME_TABLE|refresh the table. The syntax for a materialized view is:

```sql
CREATE OR REFRESH MATERIALIZED VIEW existing_live_table(
  id int NOT NULL PRIMARY KEY,
  ...
) AS SELECT ...
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using a View as a Feature Table

A simple SELECT view (created from a single Delta table without `JOIN`, `GROUP BY`, or `DISTINCT`) can act as a feature table when using `databricks-feature-engineering` version 0.7.0 or above (built into Databricks Runtime 16.0 ML). The view must select the primary key columns from the underlying table. Feature tables backed by views do not appear in the Features UI and cannot be published to online stores. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Updating Feature Tables

When updating a feature table, the following metadata must not be changed:
- Primary key
- Partition key
- Name or data type of an existing feature

Altering these will break downstream pipelines that use the features for training and serving. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

You can add new features or update specific rows based on the primary key using `write_table` with `mode = 'merge'`. Rows whose primary key does not exist in the new data remain unchanged. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Deleting a Feature Table

When a feature table is deleted (via `DROP TABLE` or `drop_table`), the underlying Delta table is also dropped. Deleting a feature table can cause failures in upstream producers and downstream consumers. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta tables](/concepts/delta-lake-table.md)
- [Time series feature table](/concepts/time-series-feature-table.md)
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- [Primary key constraint](/concepts/primary-key-constraint-for-feature-tables.md)
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)
- Catalog and Schema for Feature Tables

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
