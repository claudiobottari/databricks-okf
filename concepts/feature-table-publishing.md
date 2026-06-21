---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0a323fad077dfa80110c47d3071688bc1e541a541b2740be29514088afc86d4
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-publishing
    - FTP
    - Feature Store Publishing
    - Feature publishing
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Feature Table Publishing
description: The process of synchronizing offline feature tables to an online store using the publish_table API, with support for CONTINUOUS, TRIGGERED, and SNAPSHOT publish modes.
tags:
  - feature-engineering
  - data-synchronization
  - real-time
timestamp: "2026-06-19T14:53:03.953Z"
---

# Feature Table Publishing

**Feature Table Publishing** is the process of synchronizing feature data from an offline feature table in Unity Catalog to an online feature store, making it available for low-latency access by real-time applications and machine learning model serving endpoints. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

After an [Online Feature Store](/concepts/online-feature-store.md) is created and in the **AVAILABLE** state, you can publish feature tables to it. The `publish_table` API synchronizes data from the offline feature table to the online store, creating the necessary infrastructure for keeping the online store in sync with the offline table. ^[databricks-online-feature-stores-databricks-on-aws.md]

The publishing operation performs the following:
1. Creates a table in the online store if it doesn't already exist.
2. Syncs the feature data from the offline feature table to the online store.
3. Sets up the necessary infrastructure for ongoing synchronization. ^[databricks-online-feature-stores-databricks-on-aws.md]

`publish_table` always uses the default branch of the Lakebase Autoscaling project. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Prerequisites

All feature tables (with or without time series) must meet these requirements before publishing:

1. **Primary key constraint**: Required for online store publishing.
2. **Non-nullable primary keys**: Primary key columns cannot contain NULL values.
3. **Change Data Feed enabled**: Required for the `CONTINUOUS` and `TRIGGERED` publish modes. ^[databricks-online-feature-stores-databricks-on-aws.md]

To enable Change Data Feed and set primary key columns as non-nullable:

```sql
-- Enable CDF if not already enabled
ALTER TABLE catalog.schema.your_feature_table
SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

-- Ensure primary key columns are not nullable
ALTER TABLE catalog.schema.your_feature_table
ALTER COLUMN user_id SET NOT NULL;
```

^[databricks-online-feature-stores-databricks-on-aws.md]

## Publishing a Feature Table

To publish a feature table to an online store:

```python
from databricks.ml_features.entities.online_store import DatabricksOnlineStore

# Get the online store instance
# For Lakebase Autoscaling projects created using the Lakebase API or UI,
# `name` is the last part of the resource name: projects/{online_store_name}
online_store = fe.get_online_store(name="my-online-store")

# Publish the feature table to the online store
fe.publish_table(
    online_store=online_store,
    source_table_name="catalog_name.schema_name.feature_table_name",
    # For online_table_name, the catalog name, schema name, and table name
    # each are limited to a maximum of 63 bytes
    online_table_name="catalog_name.schema_name.online_feature_table_name",
    # `publish_mode` argument is optional and defaults to "TRIGGERED" mode
)
```

^[databricks-online-feature-stores-databricks-on-aws.md]

### Online Table Name Limitations

When specifying the `online_table_name`, the catalog name, schema name, and table name each are limited to a maximum of 63 bytes. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Publish Modes

The `publish_mode` parameter determines how and when the online table is updated with changes from the offline feature table. The supported modes are:

- **TRIGGERED** (default): Updates the online table on a schedule or when explicitly triggered.
- **CONTINUOUS**: Continuously streams changes from the offline feature table to the online store.

The `publish_mode` parameter replaces the `streaming` parameter starting from version 0.13.0.1 and prior versions. For backward compatibility, if `streaming=True` is passed, it is equivalent to setting `publish_mode="CONTINUOUS"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

See the Sync Modes Explained documentation for full details on the supported modes. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Unsynchronized Parameters

The following parameters are not supported when publishing to a Databricks online feature store: `filter_condition`, `checkpoint_location`, `mode`, `trigger`, and `features`. ^[databricks-online-feature-stores-databricks-on-aws.md]

The only supported publish mode is **merge**. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Deleting an Online Table

To delete an online table, use the Databricks SDK:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.feature_store.delete_online_table(
    online_table_name="catalog_name.schema_name.online_feature_table_name"
)
```

This is the *only* recommended method for deleting an online table. It removes the table from both Unity Catalog and the database. Other methods such as the Databricks SQL command `DROP TABLE` or the Python SDK command to delete a synced table do not delete the table from underlying database storage. ^[databricks-online-feature-stores-databricks-on-aws.md]

> **Warning**: Deleting an online published table can lead to unexpected failures in downstream dependencies. Before deleting a table, ensure that its online features are no longer used by [Model Serving](/concepts/model-serving.md) or Feature Serving endpoints. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Troubleshooting

**Error message:** `Skipping publishing to online table '...' because the feature sync pipeline is already running.`

This error occurs if multiple notebooks or jobs try to publish to an online table at the same time. Only a single sync operation is allowed per online table at a time to prevent data conflicts. ^[databricks-online-feature-stores-databricks-on-aws.md]

Databricks recommends designing your workflows to use a single `publish_table` command, such as a single task at the end of a job. If workflows cannot be coordinated in this way, use `get_status()` to wait until other publish commands have finished syncing before triggering a new publish. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md)
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md)
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Lakebase
- [Model Serving](/concepts/model-serving.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
