---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07ec8147c4b2979e90767bf0d6bd8bfe22bbf1b0b7d49863f068786eee327864
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featureengineeringclient-python-client
    - F(C
    - Feature Engineering Python client
    - Feature Engineering Python API
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: FeatureEngineeringClient (Python client)
description: A Python client (databricks-feature-engineering package) for creating, reading, updating, and deleting feature tables in Unity Catalog programmatically.
tags:
  - python-api
  - feature-store
  - databricks
timestamp: "2026-06-18T12:19:20.524Z"
---

# FeatureEngineeringClient (Python client)

The **`FeatureEngineeringClient`** is the Python client for [Feature Engineering](/concepts/featureengineeringclient-api.md) in [Unity Catalog](/concepts/unity-catalog.md). It provides a programmatic interface to create, read, update, delete, and manage feature tables that are stored as Delta tables in Unity Catalog. The client is part of the `databricks-feature-engineering` package. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

- **Databricks Runtime 13.2 or above** for Feature Engineering in Unity Catalog.
- The Unity Catalog [Metastore](/concepts/metastore.md) must have [Privilege Model Version 1.0](https://docs.databricks.com/aws/en/archive/unity-catalog/upgrade-privilege-model).
- The feature table must have a **primary key constraint** (a `PRIMARY KEY` defined on one or more `NOT NULL` columns) to be recognized as a feature table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Installation

The `databricks-feature-engineering` package is **pre-installed** in Databricks Runtime 13.3 LTS ML and above. If you use a non-ML Databricks Runtime, or need a specific version, install it manually using pip:

```python
%pip install databricks-feature-engineering
dbutils.library.restartPython()
```

See the [compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix) to select the correct version for your Databricks Runtime version. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Creating a feature table

You can create a feature table in Unity Catalog using either Databricks SQL or the `FeatureEngineeringClient.create_table()` method. The client requires you to specify the three-level namespace (`catalog.schema.table_name`), a Spark DataFrame that contains the data (including primary key columns), and optionally a primary key name and tags.

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

customer_features_df = spark.createDataFrame(
    [(1, "feat1_val", "feat2_val")],
    schema="customer_id int, feat1 string, feat2 string"
)

fe.create_table(
    name="ml.recommender_system.customer_features",
    primary_keys=["customer_id"],
    df=customer_features_df,
    description="Customer features for recommendation system",
    tags={"source": "transactions", "team": "ml"}
)
```

If the table already exists as a Delta table with a primary key constraint, you can skip `create_table` and use it directly as a feature table. The `create_table` method uses Spark DataFrame to infer the schema and initial data. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Creating a time series feature table

For point-in-time lookups, define a feature table with a `TIMESERIES` keyword on one of the primary key columns. This is supported in the SQL DDL only; the Python client can write to such tables but cannot define the `TIMESERIES` constraint programmatically. Create the table with SQL first, then use the Python client to write data.

```sql
CREATE TABLE ml.recommender_system.customer_features (
  customer_id int NOT NULL,
  ts timestamp NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (customer_id, ts TIMESERIES)
);
```

Then use `fe.write_table()` to write data. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Writing to a feature table

Use `write_table()` to insert or merge data into an existing feature table. The DataFrame must contain the primary key columns. By default, the mode is `"merge"`, which updates rows whose primary key already exists and inserts new rows.

```python
fe.write_table(
    name='ml.recommender_system.customer_features',
    df=customer_features_df,
    mode='merge'
)
```

You can also pass a streaming DataFrame to create a streaming feature computation pipeline:

```python
stream_df = compute_additional_customer_features(spark.readStream.table("prod.events.customer_transactions"))
fe.write_table(
    df=stream_df,
    name='ml.recommender_system.customer_features',
    mode='merge'
)
```

This returns a `StreamingQuery` object. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Reading from a feature table

Use `read_table()` to load the full contents of a feature table as a Spark DataFrame.

```python
customer_features_df = fe.read_table(
    name='ml.recommender_system.customer_features'
)
```

For time series feature tables, you can use `create_training_set()` or `score_batch()` to perform point-in-time lookups. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Searching and browsing feature tables

Use `get_table()` to retrieve metadata about a feature table, including its features (columns) and primary keys.

```python
ft = fe.get_table(name="ml.recommender_system.customer_features")
print(ft.features)  # lists feature column names and types
```

For a searchable UI, use the **Features** page in the sidebar. You can also use tags to categorize and find tables. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Managing tags

Tags are key-value pairs that help organize and discover feature tables and features. Use the Python client to set, update, or delete tags on a feature table.

```python
# Set/upsert a tag
fe.set_feature_table_tag(
    name="ml.recommender_system.customer_features",
    key="team",
    value="recommendation"
)

# Delete a tag
fe.delete_feature_table_tag(
    name="ml.recommender_system.customer_features",
    key="team"
)
```

Tags are also supported via Catalog Explorer and SQL statements. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Deleting a feature table

Use `drop_table()` to delete a feature table and its underlying Delta table from Unity Catalog.

```python
fe.drop_table(
    name="ml.recommender_system.customer_features"
)
```

> **Warning:** Deleting a feature table can cause failures in upstream producers and downstream consumers (models, endpoints, scheduled jobs). You must also manually delete any published online stores in your cloud provider. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Troubleshooting

**Error: `Feature tables must have a primary key`**  
The Delta table must have a primary key constraint defined. If the table does not have one, use `ALTER TABLE` SQL to add the constraint. See [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) for syntax. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) – The underlying storage and governance model
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) – Point-in-time feature lookup
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) – Required for feature tables
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance layer
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – Overview of the feature engineering workflow
- [Delta Tables](/concepts/delta-lake-table.md) – Physical storage format of feature tables
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) – Alternative way to create feature tables

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
