---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5eaa3c29041c60f9db359df2dac2ff723af856b4d686dd6d7dba9b9c52aba29a
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - publish-modes-for-online-feature-tables
    - PMFOFT
    - Publish Modes for Online Tables
    - Publish Modes
    - Sync modes for online tables
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Publish Modes for Online Feature Tables
description: The publish_mode parameter (TRIGGERED, CONTINUOUS) determines how and when an online table is synced with changes from the offline feature table, replacing the older streaming parameter.
tags:
  - feature-store
  - data-synchronization
  - publishing
timestamp: "2026-06-19T09:52:59.032Z"
---

# Publish Modes for Online Feature Tables

**Publish modes** determine how and when an online feature table is updated with changes from its source offline feature table when using [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md). The `publish_mode` parameter in the `publish_table` API controls this synchronization behavior. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

When you publish a feature table to an online store, you must specify how changes from the offline feature table should be propagated to the online store. The publish mode defines the update strategy, balancing factors such as data freshness, cost, and infrastructure requirements. ^[databricks-online-feature-stores-databricks-on-aws.md]

The `publish_mode` parameter replaces the `streaming` parameter starting from v0.13.0.1 and prior versions. For backward compatibility, if `streaming=True` is passed, it is equivalent to setting `publish_mode="CONTINUOUS"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Supported Publish Modes

Two publish modes are supported:

- **`TRIGGERED`** – The online table is updated on-demand when a publish operation is explicitly triggered. This is the default mode if `publish_mode` is not specified.
- **`CONTINUOUS`** – The online table is continuously kept in sync with the offline feature table using streaming updates.

For full details on the supported modes, see Sync modes explained. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Prerequisites

### Change Data Feed (CDF)

The `CONTINUOUS` and `TRIGGERED` publish modes require the source offline feature table to have [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) enabled. CDF tracks row-level changes (inserts, updates, deletes) in Delta tables, which the sync pipeline uses to propagate changes to the online store. ^[databricks-online-feature-stores-databricks-on-aws.md]

To enable CDF on a feature table:

```sql
ALTER TABLE catalog.schema.your_feature_table
SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');
```

^[databricks-online-feature-stores-databricks-on-aws.md]

### Other Prerequisites

All feature tables must also meet these requirements before publishing:

- **Primary key constraint**: Required for online store publishing.
- **Non-nullable primary keys**: Primary key columns cannot contain NULL values.

```sql
ALTER TABLE catalog.schema.your_feature_table
ALTER COLUMN user_id SET NOT NULL;
```

^[databricks-online-feature-stores-databricks-on-aws.md]

## Using Publish Modes

### Default Behavior

If the `publish_mode` argument is not specified, the API defaults to `TRIGGERED` mode. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Specifying a Publish Mode

```python
from databricks.ml_features.entities.online_store import DatabricksOnlineStore

online_store = fe.get_online_store(name="my-online-store")

fe.publish_table(
    online_store=online_store,
    source_table_name="catalog_name.schema_name.feature_table_name",
    online_table_name="catalog_name.schema_name.online_feature_table_name",
    publish_mode="CONTINUOUS"
)
```

^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- The only supported publish mode is `"merge"`. ^[databricks-online-feature-stores-databricks-on-aws.md]
- The following parameters are not supported when publishing to a Databricks online feature store: `filter_condition`, `checkpoint_location`, `mode`, `trigger`, and `features`. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Troubleshooting

**Error message: `Skipping publishing to online table '...' because the feature sync pipeline is already running.`**

This error occurs if multiple notebooks or jobs try to publish to an online table at the same time. Only a single sync operation is allowed per online table at a time to prevent data conflicts. ^[databricks-online-feature-stores-databricks-on-aws.md]

Databricks recommends designing your workflows to use a single `publish_table` command, for example a single task at the end of a job. If your workflows cannot be coordinated in this way, use `get_status()` to wait until other publish commands have finished syncing before triggering a new publish. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md) — The infrastructure for serving features to real-time applications
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Delta table feature required for continuous and triggered sync
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — Endpoints that serve features to real-time applications
- Online Workflows — Automatic feature lookup for real-time inference
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The underlying infrastructure for online feature stores

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
