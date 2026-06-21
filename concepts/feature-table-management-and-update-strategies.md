---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60efdfba6dd6273006fb050a497d8c45afe159f70aad48a0206624f87d00e243
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - feature-table-management-and-update-strategies
    - update strategies and Feature table management
    - FTMAUS
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Feature table management and update strategies
description: Methods for updating feature tables including merge mode for upserts, streaming pipelines for real-time updates, scheduled jobs for periodic refreshes, and composite primary keys (date + ID) for storing historical feature values.
tags:
  - feature-engineering
  - data-pipelines
  - streaming
timestamp: "2026-06-19T10:31:31.895Z"
---

# Feature table management and update strategies

**Feature table management and update strategies** encompass the operations and best practices for creating, maintaining, updating, and deleting feature tables in [Unity Catalog](/concepts/unity-catalog.md). Feature tables are Delta tables with a primary key constraint that serve as the foundation for [feature engineering](/concepts/featureengineeringclient-api.md) in machine learning workflows.

## Creating feature tables

Feature tables in Unity Catalog are [Delta tables](/concepts/delta-lake-table.md) that must have a primary key constraint. You can create them using Databricks SQL, the Python `FeatureEngineeringClient`, or Lakeflow Spark Declarative Pipelines. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

The following example creates a feature table with a primary key using SQL: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
CREATE TABLE ml.recommender_system.customer_features (
  customer_id int NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id)
);
```

For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), add a time column as a primary key column and specify the `TIMESERIES` keyword, which requires Databricks Runtime 13.3 LTS or above. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Using existing Delta tables as feature tables

Any Delta table in Unity Catalog with a primary key can serve as a feature table. If an existing table lacks a primary key, you must: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

1. Set primary key columns to `NOT NULL` using `ALTER COLUMN`.
2. Add the primary key constraint using `ALTER TABLE ... ADD CONSTRAINT`.

Views are also supported as feature tables starting from `databricks-feature-engineering` version 0.7.0, built into Databricks Runtime 16.0 ML. However, feature tables based on views can only be used for offline model training and evaluation — they cannot be published to online stores or served. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Updating feature tables

### Adding new features

You can add new features to an existing feature table in two ways: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

- Update the existing feature computation function and run `write_table` with the returned DataFrame, which updates the schema and merges new feature values based on the primary key.
- Create a new feature computation function that calculates new feature values. The returned DataFrame must contain the table's primary and partition keys. Run `write_table` to write the new features.

### Modifying specific rows

Use `mode = "merge"` in `write_table` to update only specific rows. Rows whose primary key does not exist in the DataFrame remain unchanged. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
fe.write_table(
  name='ml.recommender_system.customer_features',
  df = customer_features_df,
  mode = 'merge'
)
```

### Scheduled updates

Databricks recommends creating a scheduled job to run a notebook that updates your feature table regularly, such as every day, to ensure feature values remain current. You can convert a non-scheduled job to a scheduled one using [Lakeflow Jobs](/concepts/lakeflow-jobs.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Streaming pipelines

To create a streaming feature computation pipeline, pass a streaming DataFrame to `write_table`. This method returns a `StreamingQuery` object. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Storing historical values

Define a feature table with a composite primary key that includes a date column. For example, use a composite primary key (`date`, `customer_id`). Databricks recommends enabling [Liquid Clustering](/concepts/liquid-clustering.md) for efficient reads. If you do not use liquid clustering, set the date column as a partition key for better read performance. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Managing metadata

The following feature table metadata should not be updated after creation, as doing so will break downstream pipelines: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

- Primary key
- Partition key
- Name or data type of an existing feature

## Searching and browsing

Use the Features UI to search for or browse feature tables in Unity Catalog. You can search by feature table name, feature name, comment, or tag key-value pairs. Search text is case-insensitive. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Use `get_table` to retrieve feature table metadata, and use tags (key-value pairs) to categorize and manage feature tables and their features. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Deleting feature tables

Deleting a feature table can cause unexpected failures in upstream producers and downstream consumers (models, endpoints, and scheduled jobs). You must also delete published online stores with your cloud provider. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Use `DROP TABLE` (SQL) or `FeatureEngineeringClient.drop_table` (Python) to delete a feature table. When you delete a feature table, the underlying Delta table is also dropped. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- [Feature Store](/concepts/feature-store.md)
- [Feature Engineering Python API](/concepts/featureengineeringclient-python-api.md)
- Supported data types
- [Delta tables](/concepts/delta-lake-table.md)
- [Primary key constraints](/concepts/primary-key-constraints-for-feature-tables.md)
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md)
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- Streaming queries

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
