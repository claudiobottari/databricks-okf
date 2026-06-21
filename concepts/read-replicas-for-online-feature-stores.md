---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57d5c7079c73bc15413da476ceb657e4973866b9a9c8e5facc7df805a5f08294
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-replicas-for-online-feature-stores
    - RRFOFS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Read Replicas for Online Feature Stores
description: Additional read-only compute instances that can be added to an online store to distribute read traffic, reduce latency, and improve availability by failing over if the primary instance fails.
tags:
  - scaling
  - high-availability
  - performance
timestamp: "2026-06-18T11:39:39.453Z"
---

---
title: Read Replicas for Online Feature Stores
summary: Read replicas are secondary compute instances attached to a Databricks Online Feature Store that distribute read traffic, reducing latency and improving scalability for high-concurrency workloads.
sources:
  - databricks-online-feature-stores-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - databricks
  - feature-store
  - online-serving
  - performance
aliases:
  - read-replicas-for-online-feature-stores
  - RROFS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Read Replicas for Online Feature Stores

**Read replicas** are secondary compute instances attached to a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) that handle read requests independently of the primary instance. When read replicas are enabled, incoming read traffic is automatically distributed across all replicas, reducing the load on the primary and lowering overall latency for feature lookups. This makes read replicas particularly useful for high-concurrency workloads such as real-time recommendation systems, fraud detection, and personalization engines.

## Benefits

Read replicas improve performance and scalability by offloading read operations from the primary compute instance. In a high-concurrency environment, distributing requests across multiple replicas reduces queuing and response times. If the primary instance fails, a read replica can take over, providing high availability. Read traffic is automatically balanced across available replicas with no additional configuration required. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Adding Read Replicas

You can add read replicas when creating or updating an online feature store by passing the `read_replica_count` parameter to the Feature Engineering Client API. The following example creates an online store with two read replicas:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

fe.create_online_store(
    name="my-online-store",
    capacity="CU_2",
    read_replica_count=2  # adds 2 read replicas
)
```

You can also update an existing store that was created with `fe.create_online_store`:

```python
fe.update_online_store(
    name="my-online-store",
    read_replica_count=3
)
```

^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

Read replicas cannot be added to a Lakebase Autoscaling project that was created using the Projects API or the Databricks UI. The `read_replica_count` parameter only applies when the online store is created with `fe.create_online_store`. ^[databricks-online-feature-stores-databricks-on-aws.md]

Additionally, the total number of compute instances in an online store (primary + read replicas) is limited to 4. This means you can have up to **3 read replicas** attached to a single primary instance. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Considerations

Because each read replica is a separate compute instance, adding replicas increases the overall cost of the online store. Databricks recommends starting with a single instance and scaling up only when performance measurements indicate a bottleneck. Shared online stores (multiple feature tables published to one store) can reduce the need for replicas across separate stores. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md) — The primary concept that read replicas serve
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — Endpoints that consume online features with low latency
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The underlying infrastructure that does not support read replicas when created outside the Feature Engineering Client
- [Publish a Feature Table to an Online Store](/concepts/publishing-feature-tables-to-online-stores.md) — How to make features available for real-time access
- [Cost Optimization for Online Feature Stores](/concepts/cost-optimization-for-online-feature-stores.md) — Best practices for managing costs, including replica sizing

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
