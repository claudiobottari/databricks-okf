---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd604fc36ecd304fd3c9bb00451dc7d3e5e7b0934c29439ad4c602633d315435
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-table-publishing
    - OFTP
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Feature Table Publishing
description: The process of synchronizing offline feature tables to online stores using the publish_table API, including prerequisites like primary keys and Change Data Feed.
tags:
  - feature-store
  - publishing
  - data-sync
timestamp: "2026-06-19T18:14:05.914Z"
---

# Online Feature Table Publishing

**Online Feature Table Publishing** is the process of synchronizing feature data from an offline [Feature Table](/concepts/feature-table.md) to an [Online Feature Store](/concepts/online-feature-store.md) to enable low-latency access for real-time machine learning inference and applications. This operation is a core capability of [Databricks Feature Engineering](/concepts/databricks-feature-engineering-client.md), allowing feature data to be served to production systems such as recommendation engines, fraud detection models, and personalization services. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

The `publish_table` API synchronizes data from an offline feature table to an online store created using the `create_online_store` API. When a feature table is published, the system creates a table in the online store (if it doesn't already exist), syncs the feature data from the offline table, and sets up the necessary infrastructure to keep the online store in sync with the offline source. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Prerequisites

Before publishing a feature table to an online store, the source offline table must meet the following requirements: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. **Primary key constraint**: The table must have a defined primary key, which is required for online store publishing.
2. **Non-nullable primary keys**: Primary key columns cannot contain NULL values.
3. **Change Data Feed enabled**: Required for the `CONTINUOUS` and `TRIGGERED` publish modes. This enables the system to track changes and sync them to the online store.

To configure these requirements, use SQL commands such as: ^[databricks-online-feature-stores-databricks-on-aws.md]

```sql
-- Enable CDF if not already enabled
ALTER TABLE catalog.schema.your_feature_table
SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

-- Ensure primary key columns are not nullable
ALTER TABLE catalog.schema.your_feature_table
ALTER COLUMN user_id SET NOT NULL;
```

## Publishing a Feature Table

To publish a feature table to an online store: ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.ml_features.entities.online_store import DatabricksOnlineStore

fe = FeatureEngineeringClient()

# Get the online store instance
online_store = fe.get_online_store(name="my-online-store")

# Publish the feature table to the online store
fe.publish_table(
    online_store=online_store,
    source_table_name="catalog_name.schema_name.feature_table_name",
    online_table_name="catalog_name.schema_name.online_feature_table_name",
)
```

The `online_table_name` parameter has a maximum length of 63 bytes for the catalog name, schema name, and table name each. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Publish Modes

The `publish_mode` parameter controls how the online table is updated with changes from the offline feature table. Starting from v0.13.0, this parameter replaces the earlier `streaming` parameter. For backward compatibility, `streaming=True` is equivalent to `publish_mode="CONTINUOUS"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

Supported modes include:
- **CONTINUOUS**: Continuous streaming updates
- **TRIGGERED**: Triggered updates (default if not specified)

The only supported publish mode for online stores is "merge". ^[databricks-online-feature-stores-databricks-on-aws.md]

## Managing Published Tables

### Verifying Publication Status

After publishing, the table status shows as "AVAILABLE" when the sync is complete. You can explore the published data through: ^[databricks-online-feature-stores-databricks-on-aws.md]

- **Unity Catalog UI**: View sample data and verify the schema.
- **SQL Editor**: Run PostgreSQL queries directly against the online feature tables.

### Deleting an Online Table

To delete an online table, use the Databricks SDK: ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.feature_store.delete_online_table(
    online_table_name="catalog_name.schema_name.online_feature_table_name"
)
```

This is the only recommended method for deletion, as it removes the table from both [Unity Catalog](/concepts/unity-catalog.md) and the underlying database. Other methods such as `DROP TABLE` SQL commands do not properly clean up database storage. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Important Considerations

- Deleting a published online table can cause failures in downstream dependencies such as [Model Serving](/concepts/model-serving.md) and Feature Serving endpoints that depend on those features. ^[databricks-online-feature-stores-databricks-on-aws.md]
- `publish_table` always uses the default branch of the Lakebase Autoscaling project. ^[databricks-online-feature-stores-databricks-on-aws.md]
- Only a single sync operation is allowed per online table at a time to prevent data conflicts. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Using Published Features

After publishing, you can serve features to real-time applications by creating a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md). Models trained using Databricks features automatically track lineage to those features. When deployed as model serving endpoints, these models use [Unity Catalog](/concepts/unity-catalog.md) to find appropriate features in online stores. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Troubleshooting

**Error message: `Skipping publishing to online table '...' because the feature sync pipeline is already running.`**

This error occurs when multiple notebooks or jobs attempt to publish to the same online table simultaneously. Since only one sync operation is allowed per table at a time, Databricks recommends designing workflows to use a single `publish_table` command, such as a single task at the end of a job. If coordination isn't possible, use `get_status()` to wait for ongoing syncs to complete before triggering a new publish. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- An online feature store supports up to 3 read replicas (4 compute instances total, including the primary). ^[databricks-online-feature-stores-databricks-on-aws.md]
- Specifying a specific online table is not supported; when a feature table is published to multiple online tables, model serving and feature serving endpoints always resolve to the oldest online table based on the creation timestamp. ^[databricks-online-feature-stores-databricks-on-aws.md]
- The following parameters are not supported when publishing to a Databricks online feature store: `filter_condition`, `checkpoint_location`, `mode`, `trigger`, and `features`. ^[databricks-online-feature-stores-databricks-on-aws.md]
- Only feature tables in Unity Catalog are supported. ^[databricks-online-feature-stores-databricks-on-aws.md]
- Lakebase scale-to-zero is not supported. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)
- [Online Feature Store](/concepts/online-feature-store.md)
- [Feature Table](/concepts/feature-table.md)
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md)

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
