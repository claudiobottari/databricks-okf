---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d1496d8fe9ea61445a5d8cd201c101dac86cb3b3c686b9f5c200375b58d54fd
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakebase-autoscaling-for-online-feature-stores
    - LAFOFS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Lakebase Autoscaling for Online Feature Stores
description: The underlying managed infrastructure powering Databricks Online Feature Stores, providing scalability and high availability for real-time feature serving.
tags:
  - infrastructure
  - lakebase
  - scaling
timestamp: "2026-06-19T18:14:03.449Z"
---

# Lakebase Autoscaling for Online Feature Stores

**Lakebase Autoscaling for Online Feature Stores** refers to the use of Databricks Lakebase Autoscaling projects as the underlying infrastructure for powering online feature stores. As of March 23, 2026, all new online feature stores created through the Feature Engineering client API are automatically backed by Lakebase Autoscaling, providing a managed, scalable foundation for real-time feature serving. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

Databricks Online Feature Stores are a high-performance, scalable solution for serving feature data to online applications and real-time machine learning models. They are powered by Databricks Lakebase, which provides low-latency access to feature data at high scale while maintaining consistency with offline feature tables. ^[databricks-online-feature-stores-databricks-on-aws.md]

Primary use cases include serving features to real-time applications such as recommendation systems, fraud detection, and personalization engines via [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md), as well as automatic feature lookup for real-time inference in [Model Serving Endpoints](/concepts/model-serving-endpoint.md). ^[databricks-online-feature-stores-databricks-on-aws.md]

## How It Works

When you call `create_online_store()` using the Feature Engineering client, the API creates a Lakebase Autoscaling instance. The resulting online store is managed through the same Lakebase infrastructure, with similar capabilities and constraints. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Creating an Online Store

To create a new online feature store backed by Lakebase Autoscaling:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

fe.create_online_store(
    name="my-online-store",
    capacity="CU_2"  # Valid options: "CU_1", "CU_2", "CU_4", "CU_8"
)
```

The `capacity` setting controls compute resources for the online store. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Encryption with Customer-Managed Keys (CMK)

Online feature stores support encryption at rest with a customer-managed key (CMK) automatically when the backing Lakebase Autoscaling project supports it. No additional Lakebase or Feature Store configuration is required. ^[databricks-online-feature-stores-databricks-on-aws.md]

CMK applies when all of the following conditions are met:
- The workspace has a customer-managed key configured for managed services (see Customer-Managed Keys for Lakebase)
- The online feature store is backed by a Lakebase Autoscaling project (all stores created after March 23, 2026)
- The backing Lakebase project was created after CMK support became available in the region

To verify encryption status, locate the Lakebase project with the same name as your online store in the Lakebase App, and check the **Customer-managed keys** status card. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Managing Online Stores

### Retrieving and Updating

You can list all accessible online stores or get information about a specific store:

```python
# List all stores
stores = fe.list_online_stores()

# Get a specific store
store = fe.get_online_store(name="my-online-store")
```

To update the capacity of an online store created via `create_online_store()`:

```python
updated_store = fe.update_online_store(
    name="my-online-store",
    capacity="CU_4"
)
```

Note that this update method does not work for Autoscaling instances created using the projects API or the UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Read Replicas

When creating or updating an online feature store, you can add read replicas by specifying the `read_replica_count` parameter. Read traffic is automatically distributed across replicas, reducing latency for high-concurrency workloads. An online feature store supports up to 3 read replicas (4 compute instances total, including the primary). ^[databricks-online-feature-stores-databricks-on-aws.md]

You cannot add read replicas to a Lakebase Autoscaling project that was created using the API or the UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Publishing Feature Tables

After your online store reaches the **AVAILABLE** state, you can publish feature tables using `publish_table()`. The sync operation creates a table in the online store (if it doesn't exist), syncs data from the offline feature table, and sets up infrastructure for ongoing synchronization. ^[databricks-online-feature-stores-databricks-on-aws.md]

Prerequisites for publishing include:
- Primary key constraint on the source table
- Non-nullable primary key columns
- Change Data Feed (CDF) enabled for `CONTINUOUS` and `TRIGGERED` publish modes

The `publish_mode` parameter (optional, defaults to `TRIGGERED`) determines how changes are synced. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

When using Lakebase Autoscaling for online feature stores, note the following limitations:

- **Scale-to-zero is not supported**: Lakebase Autoscaling instances for online feature stores continuously incur costs.
- **Multi-store lookups**: Feature Serving and Model Serving endpoints that look up features from multiple online feature stores cannot use Lakebase Autoscaling instances.
- **API/UI-created instances**: Autoscaling instances created using the projects API or the UI do not support the `creator`, `read_replica_count`, and `capacity` fields, and cannot be updated after creation.
- **Only one sync at a time**: Only a single sync operation is allowed per online table at a time to prevent data conflicts.
- **Specific online table resolution**: When a feature table is published to multiple online tables, serving endpoints resolve to the oldest online table based on creation timestamp. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Optimization

Best practices for managing costs include:
- **Reuse online stores**: Publish multiple feature tables to a single online store
- **Right-size capacity**: Start with `CU_2` for testing and scale based on performance needs
- **Delete unused stores**: Online stores continuously incur costs, so delete them when not in use
- **For development and testing**: Delete Lakebase Provisioned online stores when not actively used ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md) — The overall concept of serving features to real-time applications
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — Endpoints for serving features to real-time applications
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — Endpoints for deploying models with automatic feature lookup
- Lakebase Postgres — The underlying Lakebase infrastructure
- Customer-Managed Keys for Lakebase — Encryption configuration for Lakebase projects
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and lineage for feature tables
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md) — The broader feature engineering ecosystem
- [Publish Modes](/concepts/publish-modes-for-online-feature-tables.md) — Options for syncing data to online stores

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
