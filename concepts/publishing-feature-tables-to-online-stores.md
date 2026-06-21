---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a13bdd899c5400704c6447a9261eb7cd4c5bfe734cec30e4d185b873f7c87fe1
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - publishing-feature-tables-to-online-stores
    - PFTTOS
    - Publish Features to Online Store
    - Publish a Feature Table to an Online Store
    - Publish a feature table to an online store
    - Publishing Feature Tables to Third-Party Online Stores
    - Publishing Feature Tables to an Online Store
    - Feature Store — Publish Features to Online Store
    - Looking Up Features from Online Stores
    - Publish Features to a Third‑Party Online Store
    - Publish Features to an Online Store
    - Publish batch-computed features to an online store
    - Publish features to a third-party online store
    - Publish features to a third-party online store|Publish features to a third-party online store
    - Publish features to a third‑party online store
    - Publish streaming features to an online store
    - Publishing Features
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Publishing Feature Tables to Online Stores
description: The publish_table API that synchronizes data from offline feature tables to an online store, including prerequisites like primary key constraints, non-nullable keys, and Change Data Feed.
tags:
  - feature-store
  - data-publishing
  - databricks
timestamp: "2026-06-18T15:08:25.213Z"
---

# Publishing Feature Tables to Online Stores

**Publishing Feature Tables to Online Stores** is the process of synchronizing an offline Delta feature table in Unity Catalog to a Databricks Online Feature Store, making the feature data available for low‑latency real‑time access by inference endpoints and online applications. The operation is performed using the `publish_table` API of the `FeatureEngineeringClient`. ^[databricks-online-feature-stores-databricks-on-aws.md]

After the target online store is in the **AVAILABLE** state, `publish_table` creates a table in the online store (if it does not already exist), copies the feature data from the offline source table, and sets up the infrastructure needed to keep the online store in sync with the offline table. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Prerequisites for Publishing

All offline feature tables must meet the following requirements before they can be published to an online store:

1. **Primary key constraint** – The table must have a primary key defined.
2. **Non‑nullable primary keys** – Primary key columns cannot contain `NULL` values.
3. **Change Data Feed (CDF) enabled** – Required for the `CONTINUOUS` and `TRIGGERED` publish modes. CDF can be enabled by setting the table property `delta.enableChangeDataFeed = true`. ^[databricks-online-feature-stores-databricks-on-aws.md]

```sql
ALTER TABLE catalog.schema.your_feature_table
  SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

ALTER TABLE catalog.schema.your_feature_table
  ALTER COLUMN user_id SET NOT NULL;
```

^[databricks-online-feature-stores-databricks-on-aws.md]

Only feature tables in [Unity Catalog](/concepts/unity-catalog.md) are supported for online publishing. ^[databricks-online-feature-stores-databricks-on-aws.md]

## How to Publish a Feature Table

The `publish_table` API takes the online store instance (obtained via `get_online_store`), the fully qualified name of the offline source table, a name for the online table (catalog, schema, and table name each limited to 63 bytes), and an optional `publish_mode` argument (defaults to `"TRIGGERED"`). ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.ml_features.entities.online_store import DatabricksOnlineStore

fe = FeatureEngineeringClient()
online_store = fe.get_online_store(name="my-online-store")

fe.publish_table(
    online_store=online_store,
    source_table_name="catalog_name.schema_name.feature_table_name",
    online_table_name="catalog_name.schema_name.online_feature_table_name",
    # publish_mode defaults to "TRIGGERED" if omitted
)
```

^[databricks-online-feature-stores-databricks-on-aws.md]

`publish_table` always uses the default branch of the underlying Lakebase Autoscaling project. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Publish Modes

The `publish_mode` parameter controls how and when the online table is updated with changes from the offline feature table. The supported modes are:

| Mode | Description |
|------|-------------|
| `CONTINUOUS` | Streaming sync – changes are propagated continuously to the online store. Requires CDF enabled. |
| `TRIGGERED` | Batch sync on demand – the pipeline runs once and then stops. Requires CDF enabled. |
| (Other modes) | See Sync modes explained for full details. |

The `publish_mode` parameter (introduced in v0.13.0) replaces the deprecated `streaming` parameter. For backward compatibility, passing `streaming=True` is equivalent to `publish_mode="CONTINUOUS"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

Only the `merge` publish mode is supported when publishing to a Databricks online feature store. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Managing Published Online Tables

### Deleting an Online Table

The only recommended method to delete an online table is using the Databricks SDK `delete_online_table` method. This removes the table from both Unity Catalog and the underlying database. SQL commands such as `DROP TABLE` or the Python SDK command to delete a synced table do **not** clean up database storage. ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.feature_store.delete_online_table(
    online_table_name="catalog_name.schema_name.online_feature_table_name"
)
```

^[databricks-online-feature-stores-databricks-on-aws.md]

Deleting an online table while it is in use by model serving or feature serving endpoints can cause unexpected failures. Verify that no downstream dependencies exist before deletion. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Exploring and Querying Published Features

After the published table status shows **AVAILABLE**, you can inspect the data in the [Unity Catalog](/concepts/unity-catalog.md) UI or run PostgreSQL queries using the Lakebase SQL Editor. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Handling Concurrent Publishing

If multiple notebooks or jobs attempt to publish to the same online table simultaneously, the operation is skipped with the error:  
`Skipping publishing to online table '...' because the feature sync pipeline is already running.`

Only a single sync operation is allowed per online table at a time. Coordinate workflows to use a single `publish_table` call or use `get_status()` to wait for completion before triggering a new publish. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Read Replicas and Publishing

When creating or updating an online store, you can specify a `read_replica_count` (up to 3 read replicas) to distribute read traffic and improve scalability for high‑concurrency workloads. This setting applies to the online store itself, not to individual published tables. Read replicas cannot be added to a Lakebase Autoscaling project created via the API or UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Optimization Best Practices

- **Reuse online stores**: Multiple feature tables can be published to a single online store. For development and testing, share one store across projects rather than creating separate ones.
- **Right‑size capacity**: Start with `CU_2` and scale up or down based on performance needs and cost.
- **Delete unused online stores**: Online stores incur continuous costs. Remove stores that are no longer needed. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- Specifying a specific online table when multiple online tables are published from the same offline table is not supported; model serving and feature serving endpoints always resolve to the oldest online table by creation timestamp.
- The following parameters are **not** supported when publishing to a Databricks online feature store: `filter_condition`, `checkpoint_location`, `mode`, `trigger`, and `features`.
- Only the `merge` publish mode is supported.
- Lakebase scale‑to‑zero is not supported.
- Feature Serving and Model Serving endpoints that look up features from multiple online feature stores cannot use Lakebase Autoscaling instances.
- Autoscaling instances created via the projects API or UI do not support the `creator`, `read_replica_count`, and `capacity` fields and cannot be updated.
- Customer‑managed keys (CMK) apply only to online stores created after CMK became available in the region. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md) – The target infrastructure for published tables.
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md) – Creation and management of offline feature tables.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – Automatic feature lookup from published online tables.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) – Direct feature serving to real‑time applications.
- Lakebase – Backing database technology for online stores.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and lineage for feature tables.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Required for continuous and triggered sync modes.
- Customer‑Managed Keys for Lakebase – Encryption for online stores.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
