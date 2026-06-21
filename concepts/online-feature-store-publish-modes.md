---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07591f5a9ce0c65a69abc43c4b45be8dd7ed21a44a609b29696011468faa1f55
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-store-publish-modes
    - OFSPM
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Feature Store Publish Modes
description: The publish_mode parameter (TRIGGERED, CONTINUOUS, etc.) that controls how and when online tables are synced with offline feature tables, replacing the legacy streaming parameter.
tags:
  - feature-store
  - data-synchronization
  - databricks
timestamp: "2026-06-18T15:07:59.788Z"
---

# Online Feature Store Publish Modes

**Online Feature Store Publish Modes** control how and when an online table is updated with changes from its source offline feature table. The publish mode is set via the `publish_mode` parameter when calling `publish_table()` in the Databricks Feature Engineering client.

## Overview

The `publish_mode` parameter determines the synchronization strategy between an offline feature table and the online store. Different modes offer trade-offs between freshness, cost, and complexity. The default mode is `"TRIGGERED"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Supported Modes

The following publish modes are supported by Databricks Online Feature Stores. For full details on each mode, including differences in behavior and configuration, see the Lakebase documentation on [sync modes explained](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table#sync-modes-explained). ^[databricks-online-feature-stores-databricks-on-aws.md]

- **`CONTINUOUS`** – The online table is continuously updated as changes occur in the source offline table. This mode requires that [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) is enabled on the source table. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **`TRIGGERED`** – The online table is updated on a scheduled or manual trigger basis. This is the default mode. It also requires CDF to be enabled on the source table. ^[databricks-online-feature-stores-databricks-on-aws.md]

> **Note:** The `publish_mode` parameter replaced the older `streaming` parameter starting from Feature Engineering client v0.13.0.1. For backward compatibility, passing `streaming=True` is equivalent to setting `publish_mode="CONTINUOUS"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Prerequisites

All publish modes require the source offline feature table to meet the following conditions before publishing:

1. **Primary key constraint** – The table must have a primary key defined.
2. **Non-nullable primary keys** – Primary key columns cannot contain NULL values.
3. **Change Data Feed enabled** – Required for both `CONTINUOUS` and `TRIGGERED` modes. CDF tracks row-level changes (inserts, updates, deletes) which are then propagated to the online store.

Example of enabling CDF and setting non-null constraints:  
```sql
ALTER TABLE catalog.schema.your_feature_table
SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

ALTER TABLE catalog.schema.your_feature_table
ALTER COLUMN user_id SET NOT NULL;
```
^[databricks-online-feature-stores-databricks-on-aws.md]

## Publishing Behavior

When `publish_table()` is called, it:

- Creates a table in the online store if one does not already exist.
- Synchronizes the feature data from the offline table to the online store.
- Sets up the infrastructure required to keep the online store in sync according to the chosen publish mode.

The operation always uses the default branch of the [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) project backing the online store. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md) – The infrastructure that hosts online feature tables.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Required for continuous and triggered sync modes.
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) – The underlying database engine for online stores.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The API for managing feature stores and publishing tables.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
