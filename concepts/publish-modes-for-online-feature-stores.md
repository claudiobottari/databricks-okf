---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd966ad0454c2e10794744e1ff03b3ef60b7c4ac4900bfcb377a32cdf7379ec3
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - publish-modes-for-online-feature-stores
    - PMFOFS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Publish Modes for Online Feature Stores
description: Synchronization modes (TRIGGERED, CONTINUOUS) that control how and when online tables are updated with changes from offline feature tables.
tags:
  - feature-store
  - data-sync
  - streaming
timestamp: "2026-06-19T18:14:13.875Z"
---

## Publish Modes for Online Feature Stores

**Publish modes** for Databricks Online Feature Stores control how and when an online table is updated with changes from its offline feature table. The `publish_mode` parameter is passed to the `publish_table` API and determines the synchronization behaviour between the offline and online stores. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Available Modes

The following publish modes are supported:

- **`TRIGGERED`** – The online table is updated on demand. This is the default mode when no `publish_mode` is specified. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **`CONTINUOUS`** – The online table is kept in sync with the offline table by continuously applying changes as they occur. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Prerequisites

For both `CONTINUOUS` and `TRIGGERED` publish modes, the offline feature table must have [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) enabled. CDF allows the sync pipeline to detect and propagate insertions, updates, and deletions. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Backward Compatibility with the `streaming` Parameter

The `publish_mode` parameter replaces the now-deprecated `streaming` parameter. For backward compatibility, passing `streaming=True` is equivalent to setting `publish_mode="CONTINUOUS"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Limitations

The only supported publish mode (synchronisation method) is **`merge`**. This means that changes from the offline table are merged into the online table; replace or full‑refresh modes are not available. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Additional Information

For a detailed explanation of sync modes, see the Lakebase documentation on sync modes explained. The `publish_mode` parameter was introduced in `databricks-feature-engineering` v0.13.0.1 and later. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md) – The managed infrastructure for real‑time feature serving.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The Python client used to publish tables and manage online stores.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Enables delta tracking for offline tables, required for `CONTINUOUS` and `TRIGGERED` modes.
- [Unity Catalog](/concepts/unity-catalog.md) – Governs feature tables and online tables.
- Lakebase – The underlying platform backing Databricks Online Feature Stores.

### Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
