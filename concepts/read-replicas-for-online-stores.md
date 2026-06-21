---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b4e9c25c77079887c146e0b4386a066b687e1ebe3a121be4554cd69ec2673598
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-replicas-for-online-stores
    - RRFOS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Read Replicas for Online Stores
description: A feature that distributes read traffic across multiple compute instances to reduce latency and improve scalability for high-concurrency workloads.
tags:
  - performance
  - scalability
  - high-availability
timestamp: "2026-06-19T18:14:22.607Z"
---

# Read Replicas for Online Stores

**Read Replicas for Online Stores** are secondary compute instances that can be attached to a Databricks Online Feature Store to distribute read traffic, reduce latency, improve performance and scalability for high‑concurrency workloads, and provide high availability. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

When you create or update an online feature store, you can add read replicas by specifying the `read_replica_count` parameter. Read traffic is automatically distributed across the replicas, which offloads query processing from the primary instance. This setup is particularly beneficial for real‑time applications such as recommendation systems, fraud detection, and personalization engines that require low‑latency feature lookups. ^[databricks-online-feature-stores-databricks-on-aws.md]

Read replicas also contribute to high availability: if the primary instance fails, a read replica can take over, minimising service disruption. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Usage

Read replicas are configured through the Databricks Feature Engineering client. The `read_replica_count` parameter can be supplied when calling `fe.create_online_store()` or `fe.update_online_store()`.

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Create an online store with 2 read replicas
fe.create_online_store(
    name="my-online-store",
    capacity="CU_2",
    read_replica_count=2
)
```

For existing stores, the count can be updated:

```python
fe.update_online_store(
    name="my-online-store",
    capacity="CU_4",
    read_replica_count=3
)
```

After the online store is in the **AVAILABLE** state, feature tables can be published to it using `fe.publish_table()`. Read replicas automatically serve traffic from the moment they are provisioned. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- **Maximum count**: An online feature store supports up to **3 read replicas**, for a total of 4 compute instances (primary + 3 replicas). ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Lakebase Autoscaling projects created via API or UI**: Read replicas **cannot be added** to a Lakebase Autoscaling project that was created using the Lakebase projects API or the Databricks UI. The `read_replica_count` field is not used for such instances. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Updating capacity**: The `fe.update_online_store()` method (which can modify `read_replica_count`) **does not work** for an Autoscaling instance that was created using the projects API or the UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md) – The high‑performance feature serving infrastructure that read replicas support.
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) – The backing project type for new online stores; restrictions apply for read replicas.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) – The endpoint type that serves features to real‑time applications.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The Python client used to manage online stores and publish tables.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer for feature tables used with online stores.
- [Publish Modes](/concepts/publish-modes-for-online-feature-tables.md) – Configurations for synchronising offline feature tables to online stores.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
