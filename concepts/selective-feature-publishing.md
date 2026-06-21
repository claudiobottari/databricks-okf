---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b22021c0309500359d07355f37e4460d3e546fab4d7870ef305002b529df414
  pageDirectory: concepts
  sources:
    - publish-features-to-a-third-party-online-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - selective-feature-publishing
    - SFP
  citations:
    - file: publish-features-to-a-third-party-online-store-databricks-on-aws.md
title: Selective Feature Publishing
description: Publishing only a subset of features from an offline feature table to an online store using the 'features' argument in publish_table(), while primary keys and timestamp keys are always included.
tags:
  - feature-store
  - data-management
timestamp: "2026-06-19T19:59:42.218Z"
---

# Selective Feature Publishing

**Selective Feature Publishing** is a capability in [Databricks Feature Store](/concepts/databricks-feature-store.md) that allows you to publish only a chosen subset of features from an offline feature table to a [Third-Party Online Store](/concepts/third-party-online-stores-for-feature-serving.md), rather than publishing the entire feature set. This is useful when different online serving applications require different columns or when you want to minimize storage and latency in the online store. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Usage

To publish selected features, pass the `features` argument to the `publish_table()` method, specifying a list of feature column names to publish. The following example publishes only the `total_purchases_30d` feature from the `customer_features` table: ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

```python
fe.publish_table( # or fs.publish_table for Workspace Feature Store
  name='ml.recommender_system.customer_features',
  online_store=online_store,
  features=["total_purchases_30d"])
```

If the `features` argument is omitted or set to `None`, all features from the offline feature table are published. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Always-Published Columns

Primary keys and timestamp keys are always published regardless of the `features` argument. You do not need to include them in the `features` list; they are automatically included in the published data. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Notes and Limitations

- The entire offline table must be a valid feature table. If the offline table contains data types that are unsupported by the Feature Store, you cannot publish a subset of features from that table to an online store — even if the unsupported columns are not included in the subset. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]
- Selective publishing works with both batch and streaming Publishing Features|publishing workflows; the same `features` parameter can be used in streaming mode. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The central repository for managing feature tables.
- [Third-Party Online Store](/concepts/third-party-online-stores-for-feature-serving.md) — Target stores such as Amazon DynamoDB, Amazon RDS, or other SQL databases.
- Primary Keys and [Timestamp Keys](/concepts/feature-lookup-with-timestamp-keys.md) — Key columns always included in the published data.
- [Publishing Features](/concepts/publishing-feature-tables-to-online-stores.md) — General process of publishing feature tables to online stores.

## Sources

- publish-features-to-a-third-party-online-store-databricks-on-aws.md

# Citations

1. [publish-features-to-a-third-party-online-store-databricks-on-aws.md](/references/publish-features-to-a-third-party-online-store-databricks-on-aws-a5573cf3.md)
