---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d047c1b8f84a9cfe8df2fed7a6e5fc6cbd0765258fdc9a76436e087591184425
  pageDirectory: concepts
  sources:
    - publish-features-to-a-third-party-online-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-feature-publishing
    - SFP
  citations:
    - file: publish-features-to-a-third-party-online-store-databricks-on-aws.md
title: Streaming Feature Publishing
description: Continuous streaming of features from Databricks Feature Store to an online store by setting the streaming=True parameter in publish_table().
tags:
  - feature-store
  - streaming
  - real-time
timestamp: "2026-06-19T19:59:49.813Z"
---

# Streaming Feature Publishing

**Streaming Feature Publishing** is a capability in the [Databricks Feature Store](/concepts/databricks-feature-store.md) that enables continuous, low-latency updates of features to online stores for real-time serving. Unlike batch publishing, which updates features on a scheduled basis, streaming publishing pushes feature changes to the online store as they occur in near real-time. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Overview

Streaming feature publishing allows feature tables to be continuously published to a third-party online store, such as Amazon DynamoDB or SQL-based stores like Amazon RDS MySQL or PostgreSQL. This approach is essential for use cases requiring up-to-date features for Real-Time Model Serving, Low-Latency Inference, and [Online Feature Lookup](/concepts/featurelookup.md). ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Configuration

To enable streaming publishing, set `streaming=True` in the `publish_table()` call. This instructs the Feature Store to continuously stream feature updates from the offline feature table to the specified online store. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
fe.publish_table(
  name='ml.recommender_system.customer_features',
  online_store=online_store,
  streaming=True
)
```

The streaming mode works with both [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) and [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) clients. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Supported Online Stores

Streaming publishing supports the following third-party online stores: ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

- Amazon DynamoDB — A fully managed NoSQL key-value database
- SQL stores — Including Amazon RDS MySQL, Amazon RDS PostgreSQL, and other SQL-compatible online stores

## Considerations

When using DynamoDB as the online store, note that the schema differs from the offline store. Primary keys in the online store are stored as a combined key in the column `_feature_store_internal__primary_keys`. DynamoDB tables must be created using `publish_table()` rather than manually, as the method handles automatic table creation. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

For SQL Stores, authentication requires creating Databricks Secrets for online store credentials. For DynamoDB, authentication can be provided through an instance profile attached to the Databricks cluster. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Related Features

- Batch Feature Publishing — Scheduled publishing of features to online stores at defined intervals
- [Feature Store Publishing](/concepts/feature-table-publishing.md) — General overview of publishing feature tables to online stores
- [Publishing Selected Features](/concepts/online-store-publishing-of-features.md) — Publishing only a subset of features to the online store
- Publishing to Specific Databases — Routing feature tables to specific databases in the online store
- [Online Feature Store](/concepts/online-feature-store.md) — The target store for low-latency feature access

## Sources

- publish-features-to-a-third-party-online-store-databricks-on-aws.md

# Citations

1. [publish-features-to-a-third-party-online-store-databricks-on-aws.md](/references/publish-features-to-a-third-party-online-store-databricks-on-aws-a5573cf3.md)
