---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 027c28bf97012505c4e0dac271295ff786af1618fd3fdd1b06e094fd0c4d2e3a
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-store-lifecycle-management
    - OFSLM
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Feature Store Lifecycle Management
description: Full CRUD operations for online stores and tables including creation, listing, retrieval, capacity updates, and deletion via the FeatureEngineeringClient and Databricks SDK.
tags:
  - api
  - operations
  - lifecycle
timestamp: "2026-06-19T14:52:09.526Z"
---

# Online Feature Store Lifecycle Management

**Online Feature Store Lifecycle Management** encompasses the end‑to‑end operations needed to create, configure, publish to, query, serve from, and eventually decommission an online feature store in Databricks. An online feature store provides low‑latency access to feature data for real‑time applications such as recommendation systems, fraud detection, and personalization engines. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

All online feature stores on Databricks are now created as [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) projects. The lifecycle begins with provisioning a managed infrastructure (the online store), continues with publishing feature tables from offline stores, and ends with deletion of the store when it is no longer needed. Throughout the lifecycle, administrators can adjust capacity, add read replicas, and manage encryption at rest with customer‑managed keys. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Creation

An online store is created using the `create_online_store` API of the `FeatureEngineeringClient`. The store is backed by a Lakebase Autoscaling instance. The required arguments are a name (maximum 63 bytes) and a capacity setting that controls the compute power of the store. Valid capacities are `"CU_1"`, `"CU_2"`, `"CU_4"`, and `"CU_8"`. ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
fe = FeatureEngineeringClient()

fe.create_online_store(
    name="my-online-store",
    capacity="CU_2"
)
```

### Encryption with Customer-Managed Keys

Online feature stores support encryption at rest with a customer‑managed key (CMK) automatically, provided the workspace has a CMK configured for managed services and the backing Lakebase project was created after CMK support became available in the region. No additional configuration is needed. To verify encryption, locate the Lakebase project with the same name as the online store and check its **Customer-managed keys** status card. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Management

After creation, stores can be listed, retrieved, and updated. The `list_online_stores` method returns all accessible stores with their state and capacity; `get_online_store` retrieves information about a specific store. Capacity can be changed with `update_online_store`, though this does not apply to Autoscaling instances created via the Lakebase API or UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
stores = fe.list_online_stores()
for store in stores:
    print(f"Store: {store.name}, State: {store.state}, Capacity: {store.capacity}")

store = fe.get_online_store(name="my-online-store")
updated_store = fe.update_online_store(name="my-online-store", capacity="CU_4")
```

### Read Replicas

To improve read performance for high‑concurrency workloads, read replicas can be added to an online store during creation or update by specifying the `read_replica_count` parameter. Each store supports up to 3 read replicas (4 compute instances total). Read traffic is automatically distributed across replicas. This feature is not available for Autoscaling instances created via the Lakebase API or UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Publishing Feature Tables

Once the online store is in the `AVAILABLE` state, feature tables can be published to make them available for low‑latency access.

### Prerequisites

Before publishing, the offline feature table must satisfy these conditions:

1. A **primary key constraint** must be defined.
2. **Primary key columns must be non‑nullable** (use `ALTER COLUMN ... SET NOT NULL`).
3. **[Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) must be enabled** on the table for the `CONTINUOUS` and `TRIGGERED` publish modes.

^[databricks-online-feature-stores-databricks-on-aws.md]

```sql
ALTER TABLE catalog.schema.your_feature_table
SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

ALTER TABLE catalog.schema.your_feature_table
ALTER COLUMN user_id SET NOT NULL;
```

### Publishing

Publishing is done with `fe.publish_table()`:

- It creates the online table if it does not exist.
- It syncs feature data from the offline table to the online store.
- It sets up infrastructure to keep the online store in sync.

```python
online_store = fe.get_online_store(name="my-online-store")

fe.publish_table(
    online_store=online_store,
    source_table_name="catalog_name.schema_name.feature_table_name",
    online_table_name="catalog_name.schema_name.online_feature_table_name",
    publish_mode="TRIGGERED"   # defaults to TRIGGERED if not specified
)
```

The `publish_mode` parameter replaces the legacy `streaming` parameter. Supported modes are documented in the Lakebase sync modes documentation. The mode determines how the online table is updated with changes from the offline feature table. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Deleting an Online Table

To delete an online table, use the Databricks SDK:

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
w.feature_store.delete_online_table(
    online_table_name="catalog_name.schema_name.online_feature_table_name"
)
```

This is the only recommended method; it removes the table from both Unity Catalog and the underlying database. Other methods (e.g., `DROP TABLE` SQL or SDK commands for deleting synced tables) do not clean up the database storage. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Querying Online Features

Once an online table is published and in the `AVAILABLE` state, users can explore and query the data through:

- **[Unity Catalog](/concepts/unity-catalog.md) UI** – browse sample data and schema.
- **SQL Editor** – run PostgreSQL queries directly against the online table for complex analysis and joins.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Serving Features to Real-Time Applications

Feature data stored in online tables can be served to real‑time applications in two ways:

1. **[Feature Serving Endpoints](/concepts/feature-serving-endpoint.md)** – create endpoints to serve features to recommendation engines, fraud detection, personalization, etc.
2. **Model Serving Endpoints** – models trained with Databricks automatically track feature lineage and can look up features from online stores at inference time.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Deletion

When an online store is no longer needed, it should be deleted to avoid ongoing costs. The `delete_online_store` method removes the store and its infrastructure:

```python
fe.delete_online_store(name="my-online-store")
```

Before deletion, ensure that the store’s features are not referenced by any model serving or feature serving endpoints, because deleting a published table can cause unexpected failures. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Optimization

- **Reuse online stores** – publish multiple feature tables to a single store, especially for development and testing.
- **Right‑size capacity** – start with `CU_2` for testing; scale up or down as needed.
- **Delete unused stores** – online stores incur continuous costs.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- Only Unity Catalog tables are supported as source feature tables.
- When a feature table is published to multiple online tables, model serving and feature serving endpoints always resolve to the oldest online table (by creation timestamp).
- The only supported publish mode is `"merge"`.
- Lakebase scale‑to‑zero is not supported.
- Feature Serving and Model Serving endpoints that look up features from multiple online stores cannot use Lakebase Autoscaling instances.
- Autoscaling instances created via the Lakebase API or UI do not support `creator`, `read_replica_count`, and `capacity` fields, and cannot be updated.
- Customer‑managed keys only apply to online stores created after CMK support became available in the region.
- Parameters such as `filter_condition`, `checkpoint_location`, `mode`, `trigger`, and `features` are not supported when publishing to a Databricks online store.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Troubleshooting

### Error: "Skipping publishing to online table ... because the feature sync pipeline is already running."

This occurs when multiple notebooks or jobs attempt to publish to the same online table simultaneously. Only one sync operation is allowed at a time. The recommended mitigation is to design workflows with a single `publish_table` call, or use `get_status()` to wait until an ongoing sync finishes before triggering a new one. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md)
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md)
- Lakebase Postgres
- [Unity Catalog](/concepts/unity-catalog.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md)
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- Databricks SDK

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
