---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7bd368a2523b00153fdefca2cf01d32a8c315e1dcab97cac465a265c8cb607c9
  pageDirectory: concepts
  sources:
    - publish-features-to-a-third-party-online-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-publishing-to-online-stores
    - FPTOS
  citations:
    - file: publish-features-to-a-third-party-online-store-databricks-on-aws.md
title: Feature Publishing to Online Stores
description: The process of publishing Databricks feature tables to third-party online stores (DynamoDB, SQL stores) for low-latency, real-time serving of machine learning features.
tags:
  - feature-store
  - machine-learning
  - data-publishing
timestamp: "2026-06-19T20:00:23.593Z"
---

# Feature Publishing to Online Stores

**Feature Publishing to Online Stores** is the process of making feature tables from the [Databricks Feature Store](/concepts/databricks-feature-store.md) available in a third-party online store for low-latency, real-time serving. This allows machine learning models to access feature values with minimal delay during inference, without needing to query the offline catalog at prediction time. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

---

## Overview

Databricks Feature Store supports publishing both batch-computed and streaming features to supported online stores. Supported providers include Amazon DynamoDB, Amazon RDS MySQL, and other SQL-compatible stores. When publishing, you can control which features, which partitions, and which target database or table receive the data. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

**Important:** For DynamoDB, the online store uses a different schema than the offline store. Specifically, primary keys are stored as a combined key in the column `_feature_store_internal__primary_keys`. You must create the table by using `publish_table()` — do not create it manually inside DynamoDB. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

---

## Prerequisites

Before publishing, you must:

1. **Create a database** in the online store that matches the name of the offline store (for SQL stores). If no table named `customer_features` exists in that database, the publish call creates one. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]
2. **Provide credentials** — use [Databricks secrets](/concepts/databricks-secret-scopes.md) to store read/write credentials, or attach an instance profile to the cluster (DynamoDB). ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]
3. **Ensure the offline table** is a valid feature table with supported data types. Even if you publish only a subset of features, the offline table must be entirely valid. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

---

## Publishing Batch-Computed Features

Use `publish_table()` to publish features computed daily, stored in a partitioned column (e.g., `_dt`). Example for DynamoDB: ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
import datetime
from databricks.feature_engineering.online_store_spec import AmazonDynamoDBSpec

online_store = AmazonDynamoDBSpec(
    region='<region>',
    read_secret_prefix='<read-scope>/<prefix>',
    write_secret_prefix='<write-scope>/<prefix>'
)

fe.publish_table(
    name='ml.recommender_system.customer_features',
    online_store=online_store,
    filter_condition=f"_dt = '{str(datetime.date.today())}'",
    mode='merge'
)
```

- `filter_condition` selects only today’s partition.
- `mode='merge'` upserts new rows into the existing online table.

---

## Publishing Streaming Features

Set `streaming=True` to continuously stream feature updates into the online store without requiring a scheduled batch job: ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
fe.publish_table(
    name='ml.recommender_system.customer_features',
    online_store=online_store,
    streaming=True
)
```

---

## Publishing Selected Features

Use the `features` argument to publish only a subset of features to the online store. Primary keys and timestamp keys are always published. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
fe.publish_table(
    name='ml.recommender_system.customer_features',
    online_store=online_store,
    features=["total_purchases_30d"]
)
```

---

## Publishing to a Specific Database

In the online store spec, specify `database_name` and `table_name` to override the default database/table name derived from the offline catalog: ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
online_store = AmazonRdsMySqlSpec(
    hostname='<hostname>',
    port='<port>',
    database_name='<database-name>',
    table_name='<table-name>',
    read_secret_prefix='<read-scope>/<prefix>',
    write_secret_prefix='<write-scope>/<prefix>'
)
```

`database_name` must already exist in the online store.

---

## Overwrite Mode

Use `mode='overwrite'` to completely replace the online table with offline data. DynamoDB does **not** support overwrite mode. To overwrite only specific rows, combine `mode='merge'` with `filter_condition`. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

---

## Deleting a Published Table

Use `drop_online_table()` (available in Feature Store client v0.12.0+) to remove a published table from the online store. This deletes the table from the provider and removes its metadata from Databricks. It does **not** delete the offline feature table in Databricks. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
fe.drop_online_table(
    name='recommender_system.customer_features',
    online_store=online_store
)
```

**Caution:** Before deleting, ensure the table has no downstream dependencies for [Model Serving feature lookup](/concepts/model-serving-with-automatic-feature-lookup.md). Consider rotating keys for the published table for one day before executing the delete to verify no active consumers. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

---

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – The offline catalog of feature tables.
- Real-Time Serving – The low-latency endpoint for feature retrieval.
- Online Store Spec – Python API for configuring online store connections.
- [Model Serving](/concepts/model-serving.md) – Production inference that consumes published features.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – Client version for UC-managed feature stores.

---

## Sources

- publish-features-to-a-third-party-online-store-databricks-on-aws.md

# Citations

1. [publish-features-to-a-third-party-online-store-databricks-on-aws.md](/references/publish-features-to-a-third-party-online-store-databricks-on-aws-a5573cf3.md)
