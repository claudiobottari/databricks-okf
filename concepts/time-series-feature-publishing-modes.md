---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dead9c5f0061a74a1a118634531715b3b5d6a13d609d5498fb788f65dc075b2d
  pageDirectory: concepts
  sources:
    - point-in-time-feature-joins-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-feature-publishing-modes
    - TSFPM
  citations:
    - file: point-in-time-feature-joins-databricks-on-aws.md
title: Time series feature publishing modes
description: "Two strategies for publishing time series feature tables to online stores: snapshot mode (latest value per primary key) and window mode (all values within a time-to-live window, with automatic expiry)."
tags:
  - online-store
  - feature-serving
  - databricks
timestamp: "2026-06-19T19:56:32.015Z"
---

# Time series feature publishing modes

**Time series feature publishing modes** determine how feature values from [Time Series Feature Tables](/concepts/time-series-feature-tables.md) are published to [Online Stores](/concepts/online-feature-store.md) for low-latency serving in production applications. When publishing a time series feature table, you can choose between **snapshot mode** and **window mode**, depending on the capabilities of the online store provider and your serving requirements. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Snapshot mode

In snapshot mode, `publish_table` publishes only the latest feature values for each primary key in the feature table. The online store supports primary key lookup but does not support point-in-time lookup. This means that for any given key, only the most recent feature value is available for serving. ^[point-in-time-feature-joins-databricks-on-aws.md]

Snapshot mode is the only publish mode available for online stores that do not support Time to Live (TTL). For online stores that do support TTL, snapshot mode is the default publication mode unless a TTL is explicitly specified in the `OnlineStoreSpec` at the time of creation. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Window mode

In window mode, `publish_table` publishes all feature values for each primary key in the feature table to the online store. The online store automatically removes expired records, where a record is considered expired if its timestamp (in UTC) is older than the specified time-to-live duration. This mode stores the full history of feature values within the TTL window. ^[point-in-time-feature-joins-databricks-on-aws.md]

In window mode, the online store supports primary key lookup and automatically retrieves the feature value with the latest timestamp for each key. This enables serving the most recent feature value without requiring the calling application to perform point-in-time logic. ^[point-in-time-feature-joins-databricks-on-aws.md]

### Time to Live requirements

To use window mode, you must provide a value for time to live (`ttl`) in the `OnlineStoreSpec` when you create the online store. The TTL cannot be changed once set. All subsequent publish calls inherit the TTL and do not require it to be explicitly defined again in the `OnlineStoreSpec`. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Supported modes by provider

The following table shows the supported publish modes for each online store provider. The specific modes available depend on whether the provider supports time-to-live functionality. ^[point-in-time-feature-joins-databricks-on-aws.md]

| Online store provider | Supports TTL | Supported modes |
|---|---|---|
| Providers without TTL | No | Snapshot only |
| Providers with TTL | Yes | Snapshot (default), Window |

## Selecting the right mode

Choose **snapshot mode** when your serving use case requires only the most recent feature value for each key, and you do not need to retain historical feature values in the online store. Snapshot mode requires less storage in the online store and avoids the complexity of TTL management. ^[point-in-time-feature-joins-databricks-on-aws.md]

Choose **window mode** when you need to retain multiple feature values per key within a rolling time window, for example to support point-in-time lookups during online inference. Window mode requires the online store to support TTL, and you must configure a TTL at online store creation time. ^[point-in-time-feature-joins-databricks-on-aws.md]

## Related concepts

- [Point-in-time Joins](/concepts/point-in-time-joins.md) — How timestamp keys ensure feature values are correct for training data
- [Online Stores](/concepts/online-feature-store.md) — Low-latency feature serving infrastructure
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables with timestamp keys for point-in-time correctness
- [Feature Lookup](/concepts/feature-lookup.md) — Retrieving feature values for training and inference
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The client API for managing feature tables

## Sources

- point-in-time-feature-joins-databricks-on-aws.md

# Citations

1. [point-in-time-feature-joins-databricks-on-aws.md](/references/point-in-time-feature-joins-databricks-on-aws-2568db47.md)
