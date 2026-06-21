---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c794683ef8556614fde1a1bb146ec5687f7ce199d0731c547d3043b50eed2c59
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-store-capacity-and-read-replicas
    - Read Replicas and Online Store Capacity
    - OSCARR
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Store Capacity and Read Replicas
description: Online stores support configurable compute capacity (CU_1 through CU_8) and up to 3 read replicas for distributing read traffic and improving high-concurrency performance.
tags:
  - performance
  - scalability
  - capacity-management
timestamp: "2026-06-19T14:52:06.325Z"
---

# Online Store Capacity and Read Replicas

**Online Store Capacity and Read Replicas** are configuration options for [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md) that control the compute resources available to an online store and the number of secondary read-only instances used to distribute read traffic. These settings affect the performance, scalability, and cost of real-time feature serving.

## Overview

When you create an online store using the `create_online_store` API, you can specify a `capacity` setting that determines the compute size of the underlying Lakebase Provisioned capacity|Lakebase Provisioned instance. Additionally, when creating or updating an online store, you can add **read replicas** by setting the `read_replica_count` parameter. Read replicas offload read traffic from the primary instance, reducing latency and improving throughput for high-concurrency workloads. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Capacity Settings

The `capacity` parameter controls how much compute the online store can use. Valid options are `"CU_1"`, `"CU_2"`, `"CU_4"`, and `"CU_8"`, where each value corresponds to a specific Lakebase Provisioned capacity tier. The capacity value determines the size of the underlying Lakebase Provisioned instance. ^[databricks-online-feature-stores-databricks-on-aws.md]

For example, to create an online store with capacity `CU_2`:

```python
fe.create_online_store(
    name="my-online-store",
    capacity="CU_2"
)
```

You can later update the capacity of an existing online store using `fe.update_online_store`, as long as the store was originally created with `create_online_store`. Capacity changes are not supported for Lakebase Autoscaling instances that were created through the Lakebase API or UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Read Replicas

Read replicas are secondary compute instances that handle read requests in parallel with the primary instance. When you specify a `read_replica_count` during creation or update, read traffic is automatically distributed across all replicas, improving performance and scalability for workloads with many concurrent readers. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Limitations

- An online store supports **up to 3 read replicas**, for a total of 4 compute instances (1 primary + 3 replicas). Read replicas also provide high availability: if the primary fails, a replica can take over. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Read replicas cannot be added** to a Lakebase Autoscaling project that was created using the Lakebase API or UI. Only online stores created with `fe.create_online_store` (which uses Lakebase Provisioned instances) support read replicas. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Example

To create an online store with both capacity and 2 read replicas:

```python
fe.create_online_store(
    name="my-online-store",
    capacity="CU_4",
    read_replica_count=2
)
```

## Best Practices

- **Right-size capacity**: Start with `CU_2` for testing and only scale up or down based on observed performance and cost. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Use read replicas for high-concurrency workloads**: If your feature serving endpoint receives many simultaneous requests, increasing the `read_replica_count` can reduce latency and improve scalability. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Plan for update restrictions**: Capacity and read replica count cannot be changed for Autoscaling instances created through the API or UI. If you anticipate needing to adjust these settings, create the online store with `fe.create_online_store`. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md) – The overall infrastructure for serving features in real time.
- Lakebase Provisioned capacity|Lakebase Provisioned Capacity – The compute sizing model for online stores.
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) – Alternative compute model that does not support read replicas or capacity adjustments.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) – How online features are exposed to applications.
- [Publish a Feature Table to an Online Store](/concepts/publishing-feature-tables-to-online-stores.md) – The process of syncing offline features to the online store.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
