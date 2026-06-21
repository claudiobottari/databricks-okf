---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f462dd1d0244257837fbca79d93c3ff043cef7caa0f72a2e3a5798829c1f7d21
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - time-series-feature-tables
    - TSFT
    - Time Series Features
    - time series data
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
    - file: automl-feature-store-integration-databricks-on-aws.md
title: Time Series Feature Tables
description: Feature tables that include timestamp dimensions requiring timestamp lookup keys for point-in-time correct feature lookups in AutoML
tags:
  - feature-store
  - time-series
  - automl
timestamp: "2026-06-19T22:11:31.415Z"
---

---
title: Time Series Feature Tables
summary: Feature tables that include a timestamp column designated with the TIMESERIES keyword in the primary key, enabling temporal lookups for model training and inference.
sources:
  - automl-feature-store-integration-databricks-on-aws.md
  - feature-tables-in-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:37:30.808Z"
updatedAt: "2026-06-19T18:14:03.053Z"
tags:
  - feature-store
  - time-series
  - point-in-time
aliases:
  - time-series-feature-tables
  - TSFT
confidence: 0.96
provenanceState: merged
inferredParagraphs: 1
---

# Time Series Feature Tables

A **time series feature table** is a [Feature Table](/concepts/feature-table.md) in [Databricks Feature Store](/concepts/databricks-feature-store.md) that includes a timestamp column as part of its primary key, designated using the `TIMESERIES` keyword. This designation enables temporal lookups when the table is used for training or inference with AutoML or the Feature Engineering client. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Creating a Time Series Feature Table

Time series feature tables can be created in Unity Catalog using Databricks SQL or Lakeflow Spark Declarative Pipelines. The timestamp column must be declared as `NOT NULL` and the primary key constraint must include the `TIMESERIES` keyword on that column. The `TIMESERIES` keyword is available in Databricks Runtime 13.3 LTS or above. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Using Databricks SQL

```sql
CREATE TABLE ml.recommender_system.customer_features (
  customer_id int NOT NULL,
  ts timestamp NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id, ts TIMESERIES)
);
```

### Using Lakeflow Spark Declarative Pipelines (Preview)

The same syntax applies when defining a materialized view in a pipeline:

```sql
CREATE MATERIALIZED VIEW customer_features (
  customer_id int NOT NULL,
  ts timestamp NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id, ts TIMESERIES))
AS SELECT * FROM ...;
```

## Using an Existing Delta Table as a Time Series Feature Table

Any Delta table in Unity Catalog can be made into a time series feature table by adding a primary key constraint with the `TIMESERIES` keyword on one of its timestamp columns. Use `ALTER TABLE` to set the primary key:

1. Set the timestamp column to `NOT NULL`:
   ```sql
   ALTER TABLE <full_table_name> ALTER COLUMN <ts_col> SET NOT NULL
   ```
2. Add the primary key constraint with `TIMESERIES`:
   ```sql
   ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1 TIMESERIES, pk_col2, ...)
   ```

After the constraint is added, the table appears in the Features UI and can be used as a feature table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using Time Series Feature Tables with AutoML

When using AutoML with time series feature tables, you must select the corresponding timestamp lookup key. The timestamp lookup key should be a column in the training dataset you provided for your AutoML experiment. Classification and regression experiments require Databricks Runtime 11.3 LTS ML and above; forecasting experiments require Databricks Runtime 12.2 LTS ML and above. ^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Centralized repository for machine learning features.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The framework for creating and managing feature tables in Unity Catalog.
- [AutoML Feature Store Integration](/concepts/automl-feature-store-integration.md) — Using feature tables with AutoML experiments.
- [Point-in-Time Lookups](/concepts/point-in-time-lookups.md) — The temporal join logic enabled by time series feature tables.
- Data Leakage — The problem that time series feature tables help prevent.

## Sources

- automl-feature-store-integration-databricks-on-aws.md
- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
2. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
