---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83eae7ddf000f240c4af35199e789bc8ced7aaf3f1e97ab1a8686fd252bdad4e
  pageDirectory: concepts
  sources:
    - publish-features-to-a-third-party-online-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - amazon-dynamodb-online-store-integration
    - ADOSI
    - Amazon DynamoDB online store
    - DynamoDB Online Store
    - DynamoDB online store
  citations:
    - file: publish-features-to-a-third-party-online-store-databricks-on-aws.md
title: Amazon DynamoDB Online Store Integration
description: Details of using Amazon DynamoDB as a third-party online store with Feature Store, including combined primary keys, automatic table creation via publish_table(), and instance profile authentication.
tags:
  - feature-store
  - aws
  - dynamodb
  - authentication
timestamp: "2026-06-19T19:59:43.853Z"
---

# Amazon DynamoDB Online Store Integration

**Amazon DynamoDB Online Store Integration** refers to the support for using Amazon DynamoDB as a target online store for publishing feature tables from Databricks Feature Store. This integration enables low-latency, real-time serving of features by making them available in DynamoDB's NoSQL database service. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Overview

Databricks Feature Store supports Amazon DynamoDB as one of its third-party online stores for serving features in production. The integration allows data teams to publish both batch-computed and streaming features to DynamoDB, where they become available for real-time inference workloads. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Schema Differences

The DynamoDB online store uses a different schema than the offline feature store. Specifically, in the online store, primary keys are stored as a combined key in the column `_feature_store_internal__primary_keys`. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Table Management

To ensure that Feature Store can access the DynamoDB online store, you must create the table using `publish_table()`. You should not manually create a table inside DynamoDB, as `publish_table()` handles this automatically. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Authentication

Databricks recommends providing authentication with write permission through an instance profile attached to a Databricks cluster when working with DynamoDB online stores. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Publishing Features

### Batch-Computed Features

You can create and schedule a Databricks job to regularly publish updated features to DynamoDB. The `AmazonDynamoDBSpec` class is used to configure the online store connection: ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
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

You do not need to pass `write_secret_prefix` if you intend to use the instance profile attached to the cluster. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Streaming Features

To continuously stream features to the DynamoDB online store, set `streaming=True` in the `publish_table` call: ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
fe.publish_table(
  name='ml.recommender_system.customer_features',
  online_store=online_store,
  streaming=True
)
```

### Publishing Selected Features

To publish only selected features to the online store, use the `features` argument to specify the feature names. Primary keys and timestamp keys are always published. If you do not specify the `features` argument, all features from the offline feature table are published. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
fe.publish_table(
  name='ml.recommender_system.customer_features',
  online_store=online_store,
  features=["total_purchases_30d"]
)
```

Note that the entire offline table must be a valid feature table even if you are publishing only a subset of features. If the offline table contains unsupported data types, you cannot publish a subset of features from that table. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Publishing to a Specific Database

In the online store spec, specify the `database_name` and `table_name` parameters to publish to a specific database in DynamoDB. If you do not specify these parameters, the offline database name and feature table name are used. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Limitations

### Mode Support

Amazon DynamoDB does not support the `overwrite` mode for `publish_table`. Only the `merge` mode is supported. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Client Version Requirements

DynamoDB support is available in all versions of Feature Engineering in Unity Catalog client, and Feature Store client v0.3.8 and above. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Deleting a Published Table

With Feature Store client v0.12.0 and above, you can use `drop_online_table` to delete a published table from DynamoDB. This action deletes the table from the online store provider and removes the online store metadata from Databricks. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
fe.drop_online_table(
  name='recommender_system.customer_features',
  online_store=online_store
)
```

Important considerations:
- `drop_online_table` does not delete the feature table in Databricks
- Before deleting, ensure the table is not used for Model Serving feature lookup and has no other downstream dependencies
- The delete is irreversible and might cause dependencies to fail
- To check for dependencies, consider rotating the keys for the published table for a day before executing `drop_online_table`

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Central repository for managing and serving machine learning features
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — Unity Catalog-managed feature engineering capabilities
- [Online Store](/concepts/online-feature-store.md) — Low-latency feature serving infrastructure for real-time inference
- Batch Feature Computation — Computing features in batch processing jobs
- Streaming Features — Continuously computed features from streaming data sources
- [Model Serving](/concepts/model-serving.md) — Serving machine learning models in production with feature lookup

## Sources

- publish-features-to-a-third-party-online-store-databricks-on-aws.md

# Citations

1. [publish-features-to-a-third-party-online-store-databricks-on-aws.md](/references/publish-features-to-a-third-party-online-store-databricks-on-aws-a5573cf3.md)
