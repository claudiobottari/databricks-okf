---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b54aab4e02d986b29d929d68a6e21d5e66ce4e1047c23333e2f9c10f31876c19
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - primary-key-constraint-for-feature-tables
    - PKCFFT
    - Add a Primary Key Constraint
    - Primary Key Constraint
    - Primary key constraint
    - add a primary key constraint on the table
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Primary Key Constraint for Feature Tables
description: Feature tables require a primary key constraint, which can be defined at table creation or added to existing Delta tables via ALTER TABLE DDL statements.
tags:
  - feature-store
  - unity-catalog
  - data-governance
timestamp: "2026-06-19T18:48:44.129Z"
---

# Primary Key Constraint for Feature Tables

In [Unity Catalog](/concepts/unity-catalog.md), any Delta table with a **primary key constraint** can serve as a feature table. This constraint is a foundational requirement that enables the Feature Engineering system to uniquely identify rows, perform merges, and support time series lookups. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

To use primary key constraints on feature tables, Feature Engineering in Unity Catalog requires Databricks Runtime 13.2 or above, and the Unity Catalog [Metastore](/concepts/metastore.md) must have Privilege Model Version 1.0. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Creating a Feature Table with a Primary Key

Feature tables can be created using Databricks SQL, the Python `FeatureEngineeringClient`, or Lakeflow Spark Declarative Pipelines. Primary key columns must be declared `NOT NULL`. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

**Databricks SQL example:**

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

To create a time series feature table, include a timestamp column as part of the primary key and specify the `TIMESERIES` keyword on that column. The `TIMESERIES` keyword requires Databricks Runtime 13.3 LTS or above. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

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

### Lakeflow Spark Declarative Pipelines

Tables published from Lakeflow Spark Declarative Pipelines that include a primary key constraint can also be used as feature tables. This feature is in Public Preview; code examples must run using the Lakeflow Spark Declarative Pipelines preview channel. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

**Example using Databricks SQL in a pipeline:**

```sql
CREATE MATERIALIZED VIEW customer_features (
  customer_id int NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)
) AS SELECT * FROM ...;
```
^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Time series tables can be created in a pipeline by adding a timestamp column with the `TIMESERIES` keyword on the constraint. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using an Existing Delta Table as a Feature Table

Any Delta table in Unity Catalog can become a feature table if it has a primary key constraint. If the table does not already have one, you must:

1. Set the primary key columns to `NOT NOT NULL` using `ALTER TABLE ... ALTER COLUMN ... SET NOT NULL`.
2. Add the primary key constraint using `ALTER TABLE ... ADD CONSTRAINT ... PRIMARY KEY(...)`.

Only the table owner can declare primary key constraints. The owner’s name is displayed on the table detail page of Catalog Explorer. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

**Example:**

```sql
ALTER TABLE ml.recommender_system.customer_features
  ADD CONSTRAINT customer_features_pk PRIMARY KEY(customer_id);
```
^[feature-tables-in-unity-catalog-databricks-on-aws.md]

To make the table a time series feature table, specify the `TIMESERIES` keyword on one of the primary key columns in the `ADD CONSTRAINT` statement. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using a Streaming Table or Materialized View as a Feature Table

Streaming tables and materialized views created by Lakeflow Spark Declarative Pipelines can be used as feature tables after a primary key is added. To add the constraint, update the schema in the notebook that manages the object, then refresh the table to update the Unity Catalog object. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

**Example for a materialized view:**

```sql
CREATE OR REFRESH MATERIALIZED VIEW existing_live_table(
  id int NOT NULL PRIMARY KEY,
  ...
) AS SELECT ...;
```
^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using a View as a Feature Table

A simple SELECT view in Unity Catalog can serve as a feature table when using `databricks-feature-engineering` version 0.7.0 or above. The view must be created from a single Delta table that can be used as a feature table, and its primary keys must be selected without `JOIN`, `GROUP BY`, or `DISTINCT` clauses. Only `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`, and `OFFSET` are allowed. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Limitations:
- Feature tables backed by views do not appear in the Features UI.
- They can be used for offline model training and evaluation, but cannot be published to online stores, and features from these tables and models based on them cannot be served. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Updating a Feature Table

The primary key of a feature table should **not** be updated after creation. Altering the primary key, partition key, or the name/data type of an existing feature will cause downstream pipelines that use features for training and serving to break. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

New features can be added by running `write_table` with a DataFrame that includes the primary key (and partition keys if defined). To update specific rows, use `mode = "merge"` in `write_table`; rows whose primary key does not exist in the incoming DataFrame remain unchanged. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Reading from a Feature Table

Use `read_table` of the `FeatureEngineeringClient` to read feature values. The Feature Engineering UI allows searching and browsing feature tables by catalog, name, feature, comment, or tags. `get_table` returns metadata including the list of features. Tags can be applied to feature tables and features for categorization. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Troubleshooting

**Error message: `Feature tables must have a primary key`** — The feature table must have a primary key constraint defined. If it does not, add one as described under [#Using an existing Delta table as a feature table](/concepts/using-existing-delta-tables-as-feature-tables.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — Overview of feature table creation, management, and usage.
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables with point-in-time lookup capabilities.
- [Delta Tables](/concepts/delta-lake-table.md) — The underlying storage format for feature tables.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing feature tables.
- [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) — Programmatic access to feature table operations.

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
