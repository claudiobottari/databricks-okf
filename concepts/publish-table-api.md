---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef1a77d73e4e43735607f1d3320639bae9fb233a0e90cd96f52ab43cae3ee094
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - publish-table-api
    - PTA
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Publish Table API
description: The API operation (publish_table) that creates an online table, syncs feature data from an offline feature table to the online store, and sets up infrastructure for ongoing synchronization.
tags:
  - api
  - feature-store
  - data-synchronization
timestamp: "2026-06-18T11:40:05.605Z"
---

# Publish Table API

The **Publish Table API** (`publish_table`) is a method in the Databricks Feature Engineering client that synchronizes feature data from an offline feature table to an online feature store, making the features available for low-latency serving to real-time applications and machine learning models. The API creates a table in the online store if it doesn’t already exist, syncs the feature data from the source offline table, and sets up the necessary infrastructure to keep the online store in sync with the offline table. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Prerequisites

Before calling `publish_table`, the source offline feature table must meet the following requirements: ^[databricks-online-feature-stores-databricks-on-aws.md]

- **Primary key constraint**: Required for publishing to an online store.
- **Non-nullable primary keys**: Primary key columns cannot contain `NULL` values.
- **Change Data Feed (CDF) enabled**: Required for the `CONTINUOUS` and `TRIGGERED` publish modes. See [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) for how to enable Delta Table CDF.

Example SQL to satisfy these prerequisites: ^[databricks-online-feature-stores-databricks-on-aws.md]

```sql
-- Enable CDF if not already enabled
ALTER TABLE catalog.schema.your_feature_table
SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

-- Ensure primary key columns are not nullable
ALTER TABLE catalog.schema.your_feature_table
ALTER COLUMN user_id SET NOT NULL;
```

## Usage

The `publish_table` API is part of the `FeatureEngineeringClient`. Call it after creating an online store and retrieving it via `get_online_store`. ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
from databricks.ml_features.entities.online_store import DatabricksOnlineStore

# Get the online store instance
online_store = fe.get_online_store(name="my-online-store")

# Publish the feature table to the online store
fe.publish_table(
    online_store=online_store,
    source_table_name="catalog_name.schema_name.feature_table_name",
    online_table_name="catalog_name.schema_name.online_feature_table_name",
    # publish_mode argument is optional and defaults to "TRIGGERED" mode if not specified
)
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `online_store` | The online store instance returned by `get_online_store`. For Lakebase Autoscaling projects created via the Lakebase API or UI, `name` is the last part of the resource name: `projects/{online_store_name}`. |
| `source_table_name` | The full three-level name of the offline feature table in Unity Catalog (e.g., `catalog.schema.feature_table`). Only Unity Catalog tables are supported. |
| `online_table_name` | The name of the table to create in the online store. Catalog, schema, and table name each limited to 63 bytes. |
| `publish_mode` | Optional. Determines how and when the online table is updated with changes from the offline table. Defaults to `"TRIGGERED"`. Supported modes are described below. |

### Naming constraints

The catalog name, schema name, and table name in `online_table_name` are each limited to a maximum of 63 bytes. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Publish Modes

The `publish_mode` parameter controls the sync strategy. It replaces the deprecated `streaming` parameter starting from v0.13.0. For backward compatibility, `streaming=True` is equivalent to `publish_mode="CONTINUOUS"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

| Mode | Behavior |
|------|----------|
| `TRIGGERED` | Syncs data from the offline table to the online store on demand. The pipeline runs once per `publish_table` call and then stops. |
| `CONTINUOUS` | Sets up a continuous sync pipeline that automatically propagates changes from the offline feature table (via Change Data Feed) to the online store in near-real time. |
| `TRIGGERED` (default) | If not specified, the API uses `TRIGGERED` mode. |

For full details on sync modes, see [Sync modes for online tables](/concepts/publish-modes-for-online-feature-tables.md).

## Behavior

When `publish_table` is called, the API performs the following operations: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. Creates a table in the online store if it does not already exist.
2. Syncs the feature data from the offline feature table to the online store.
3. Sets up the necessary infrastructure for keeping the online store in sync with the offline table (based on the selected `publish_mode`).

The API always uses the default branch of the Lakebase Autoscaling project backing the online store. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- Specifying a specific online table is not supported. When a feature table is published to multiple online tables, model serving and feature serving endpoints always resolve to the oldest online table based on the creation timestamp. ^[databricks-online-feature-stores-databricks-on-aws.md]
- The following parameters are **not supported** when publishing to a Databricks online feature store: `filter_condition`, `checkpoint_location`, `mode`, `trigger`, and `features`. ^[databricks-online-feature-stores-databricks-on-aws.md]
- Only feature tables in Unity Catalog are supported. ^[databricks-online-feature-stores-databricks-on-aws.md]
- The only supported publish mode is `"merge"` (no other sync strategies like `"overwrite"`). ^[databricks-online-feature-stores-databricks-on-aws.md]

## Troubleshooting

**Error message:** `Skipping publishing to online table '...' because the feature sync pipeline is already running.` ^[databricks-online-feature-stores-databricks-on-aws.md]

This occurs when multiple notebooks or jobs try to publish to the same online table concurrently. Only one sync operation is allowed per online table at a time to prevent data conflicts. Databricks recommends designing workflows to use a single `publish_table` command (e.g., a single task at the end of a job). If workflows cannot be coordinated, use `get_status()` to wait until previous publish commands have finished before triggering a new one. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md) — The infrastructure that hosts published features
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The client providing `publish_table` and other APIs
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — How online features are served to applications
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for feature tables
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Enables continuous sync modes
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The underlying compute for online stores

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
