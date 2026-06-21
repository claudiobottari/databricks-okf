---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6855aaef5d7e73179169178c97826bd27f3136b7a79b85c212f3082e6c88c1b
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
    - work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - feature-table-update-strategies
    - FTUS
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
    - file: work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md
title: Feature Table Update Strategies
description: Methods for updating feature tables including adding new features, merging specific rows, scheduling periodic jobs, and streaming feature computation pipelines.
tags:
  - data-pipelines
  - streaming
  - feature-store
  - scheduling
timestamp: "2026-06-18T12:19:29.596Z"
---

# Feature Table Update Strategies

Feature tables in Databricks must be kept current to reflect the latest data. Databricks supports several strategies for updating feature tables, whether they are managed in [Unity Catalog](/concepts/unity-catalog.md) (any Delta table with a primary key) or in the legacy Workspace Feature Store. The choice of strategy depends on the frequency of updates, the volume of new data, and whether historical values must be preserved. ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

## Metadata That Should Not Be Updated

The following feature table metadata must not be changed after creation, because doing so will break downstream pipelines that use the features for training and serving models: ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

- Primary key
- Partition key
- Name or data type of an existing feature

All update strategies described below preserve these constraints.

## Strategies

### 1. Adding New Features to an Existing Feature Table

New features can be added using one of two approaches: ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

1. **Update the existing feature computation function** and call `write_table` with the returned DataFrame. This updates the feature table schema and merges new feature values based on the primary key. The DataFrame must contain all primary key columns (and partition keys, if defined).
2. **Create a new feature computation function** that calculates the new feature values. The returned DataFrame must include the table’s primary keys and partition keys. Calling `write_table` with this DataFrame writes only the new features, using the same primary key for the merge.

Both approaches allow the schema to evolve as new columns are added.

### 2. Updating Only Specific Rows

To modify a subset of rows without affecting the rest, use `mode = "merge"` in `write_table`. Rows whose primary key does not appear in the input DataFrame remain unchanged. ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
fe = FeatureEngineeringClient()
fe.write_table(
  name='ml.recommender_system.customer_features',
  df=customer_features_df,
  mode='merge'
)
```

This is the same `FeatureEngineeringClient` used in Unity Catalog; in the legacy Workspace Feature Store the client is `FeatureStoreClient`. ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

### 3. Scheduling a Job for Periodic Updates

Databricks recommends creating a [scheduled job](/concepts/scheduled-jobs-with-ai-runtime.md) that runs a notebook to update a feature table on a regular basis (for example, daily). The notebook calls `write_table` with `mode='merge'` to ensure that the feature values are always up to date. ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

```python
customer_features_df = compute_customer_features(data)
fe.write_table(
  df=customer_features_df,
  name='ml.recommender_system.customer_features',
  mode='merge'
)
```

If you already have a non-scheduled job, you can convert it to a scheduled job using [Lakeflow Jobs](/concepts/lakeflow-jobs.md).

### 4. Storing Past Values of Daily Features

When historical feature values must be retained for backtesting or point-in-time lookups, define the table with a **composite primary key** that includes a date column. Optionally set the date column as a partition key for efficient reads. Databricks recommends enabling [Liquid Clustering](/concepts/liquid-clustering.md) for better read performance. ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

**Unity Catalog (SQL syntax):**

```sql
CREATE TABLE ml.recommender_system.customer_features (
  customer_id int NOT NULL,
  `date` date NOT NULL,
  feat1 long,
  feat2 varchar(100),
  CONSTRAINT customer_features_pk PRIMARY KEY (`date`, customer_id)
)
COMMENT "Customer features";
```

**Legacy Workspace Feature Store (Python syntax):**

```python
fs.create_table(
  name='recommender_system.customer_features',
  primary_keys=['date', 'customer_id'],
  partition_columns=['date'],
  schema=customer_features_df.schema,
  description='Customer features'
)
```

For point-in-time lookups during training or batch scoring, create a [Time series feature table](/concepts/time-series-feature-table.md) by designating a timestamp column as a `TIMESERIES` key (Unity Catalog) or using the `timestamp_keys` argument (legacy). The system then performs as-of timestamp joins when you call `create_training_set` or `score_batch`. ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

### 5. Streaming Feature Computation Pipeline

For continuous updates, pass a streaming `DataFrame` to `write_table`. This returns a `StreamingQuery` object. The pipeline reads from a streaming source (e.g., `spark.readStream.table(...)`) and merges new records as they arrive. ^[feature-tables-in-unity-catalog-databricks-on-aws.md, work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md]

```python
def compute_additional_customer_features(data):
  # Returns Streaming DataFrame
  pass

customer_transactions = spark.readStream.table("prod.events.customer_transactions")
stream_df = compute_additional_customer_features(customer_transactions)

fe.write_table(
  df=stream_df,
  name='ml.recommender_system.customer_features',
  mode='merge'
)
```

This approach is suitable for near-real-time feature freshness.

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md)
- Feature Tables in Workspace Feature Store (Legacy)
- [Primary Key Constraint](/concepts/primary-key-constraint-for-feature-tables.md) – Required for all feature tables
- [Merge Mode](/concepts/merge-into-delta-lake.md) – The `mode='merge'` option for upserting rows
- [Time series feature table](/concepts/time-series-feature-table.md) – Enables point-in-time lookups
- [Liquid Clustering](/concepts/liquid-clustering.md) – Recommended for efficient reads on historical data
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – For scheduling recurring updates
- Streaming DataFrames – For continuous feature computation

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md
- work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
2. [work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws.md](/references/work-with-feature-tables-in-workspace-feature-store-legacy-databricks-on-aws-083b6fcf.md)
