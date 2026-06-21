---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9d1fa1101df8619c68e305ad3c980e93a69527dc398ebf6babd375c4326b8ad
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-replicas-in-online-feature-stores
    - RRIOFS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Read Replicas in Online Feature Stores
description: Read replicas distribute read traffic across multiple compute instances for high-concurrency workloads, supporting up to 3 replicas (4 total instances including primary), and are configured via the read_replica_count parameter during create or update.
tags:
  - scalability
  - feature-store
  - high-availability
timestamp: "2026-06-19T09:52:55.129Z"
---

#Read Replicas in Online Feature Stores

**Read replicas in online feature stores** are secondary compute instances that handle read-only queries, improving scalability, latency, and availability for real-time feature serving. Databricks Online Feature Stores support up to three read replicas per online store, automatically distributing read traffic across them. ^[databricks-online-feature-stores-databricks-on-aws.md]

## How Read Replicas Work

When you create or update an online feature store, you can specify a `read_replica_count` parameter (currently 0 to 3). The primary instance continues to handle writes and relational database updates, while read replicas offload read traffic. This distribution reduces latency under high-concurrency workloads and enhances overall throughput. Read replicas also provide high availability: if the primary fails, a read replica can take over. ^[databricks-online-feature-stores-databricks-on-aws.md]

The total number of compute instances is the primary plus all replicas. For example, setting `read_replica_count=2` results in a total of three instances. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Adding Read Replicas

Read replicas are configured at the time of online store creation or by updating an existing store using the `update_online_store` API. The following Python pseudocode illustrates adding replicas:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
fe.create_online_store(
    name="my-online-store",
    capacity="CU_2",
    read_replica_count=2  # Adds two read replicas
)
```

Read traffic is automatically balanced across all replicas; no application-level changes are required. ^[databricks-online-feature-stores-databricks-on-aws.md]

> [!IMPORTANT]
> You **cannot** add read replicas to a Lakebase Autoscaling project that was created using the Lakebase API or the Lakebase UI. Read replicas are only supported on online stores created with the `create_online_store` API. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Benefits

- **Lower latency**: Read replicas reduce the load on the primary instance, speeding up feature lookups for real-time applications.
- **High throughput**: Concurrent read requests are spread across multiple instances, increasing aggregate query capacity.
- **High availability**: If the primary instance fails, a read replica automatically takes over, minimising downtime.
- **Elastic scaling**: You can adjust the replica count as workload demands change. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- **Maximum replicas**: An online feature store supports **up to 3 read replicas** (4 compute instances total, including the primary). ^[databricks-online-feature-stores-databricks-on-aws.md]
- **No support for API/UI-created Autoscaling projects**: Online stores provisioned via the Lakebase API or UI cannot use read replicas. The `read_replica_count` parameter is ignored for those stores. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **No scale‑to‑zero**: Lakebase scale-to-zero is not supported on online feature stores; replicas incur continuous cost. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Best Practices

- **Match replica count to workload**: For low-concurrency testing, start with no replicas. For production workloads with high read volume, add replicas incrementally while monitoring latency.
- **Combine with right-sized capacity**: Choose an appropriate `capacity` (e.g., `CU_2` for testing) before adding replicas.
- **Delete unused stores**: Online stores (including replicas) incur continuous costs. Delete stores that are no longer needed.
- **Consider sharing**: Where possible, publish multiple feature tables to a single online store to maximise resource utilisation. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md)
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md)
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md)
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
