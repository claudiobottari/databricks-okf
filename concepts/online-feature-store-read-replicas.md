---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bdb261edb6ffba4236f22560e07117f71a7098a9dc1543c9d0b701d0d093c674
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-store-read-replicas
    - OFSRR
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Feature Store Read Replicas
description: Read replicas that distribute read traffic across multiple compute instances, reducing latency and improving scalability for high-concurrency workloads, with support for up to 3 replicas.
tags:
  - scalability
  - high-concurrency
  - databricks
timestamp: "2026-06-18T15:08:18.208Z"
---

# Online Feature Store Read Replicas

**Online Feature Store Read Replicas** are additional compute instances that serve read traffic for a Databricks online feature store. They work alongside the primary instance to distribute read requests, reducing latency and improving throughput for high-concurrency workloads. Read replicas also provide high availability by taking over if the primary instance fails. ^[databricks-online-feature-stores-databricks-on-aws.md]

## How to Add Read Replicas

When creating or updating an online feature store with the `FeatureEngineeringClient`, you can specify the number of read replicas using the `read_replica_count` parameter. Read traffic is then automatically balanced across all replicas. ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Create an online store with 2 read replicas
fe.create_online_store(
    name="my-online-store",
    capacity="CU_4",
    read_replica_count=2
)
```

The `update_online_store` API also accepts the `read_replica_count` parameter to change the number of replicas after creation. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- **Maximum replicas:** An online feature store supports up to **3 read replicas** (4 compute instances total, including the primary). ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Restriction on Lakebase Autoscaling projects:** You cannot add read replicas to a Lakebase Autoscaling project that was created using the Lakebase API or the UI. Read replicas are only configurable on stores created with `fe.create_online_store` (the Feature Engineering API). ^[databricks-online-feature-stores-databricks-on-aws.md]

## Benefits

- **Lower latency:** Read replicas offload read traffic from the primary, reducing response times for feature lookups.
- **Higher scalability:** Multiple replicas handle concurrent requests from [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) and [Model Serving Endpoints](/concepts/model-serving-endpoint.md) more effectively.
- **High availability:** If the primary instance fails, a read replica can take over, minimizing downtime. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Considerations

Each read replica incurs additional compute costs. Databricks recommends right-sizing your capacity (e.g., starting with `CU_2` and scaling up as needed) and deleting online stores that are no longer in use. You can publish multiple feature tables to a single online store to share costs across projects. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) – The underlying infrastructure for online feature stores.
- [Online Feature Store](/concepts/online-feature-store.md) – The overall feature store concept.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) – How features are served to real-time applications.
- [Publish a Feature Table to an Online Store](/concepts/publishing-feature-tables-to-online-stores.md) – How to sync data to the online store.
- Lakebase Autoscaling Projects – Projects created via the API or UI that do not support read replicas.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
