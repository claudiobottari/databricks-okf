---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: be100be76266c8d63829fc162f43e9efaa412e7bfe362e525272589d28d0409c
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-store-capacity-and-compute-sizing
    - Compute Sizing and Online Feature Store Capacity
    - OFSCACS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Feature Store Capacity and Compute Sizing
description: The capacity setting (CU_1, CU_2, CU_4, CU_8) that controls compute power for an online store, corresponding to Lakebase Provisioned capacity levels.
tags:
  - compute-sizing
  - capacity
  - databricks
timestamp: "2026-06-18T15:08:31.945Z"
---

# Online Feature Store Capacity and Compute Sizing

**Online Feature Store Capacity and Compute Sizing** refers to the configuration of compute resources allocated to a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) to balance performance, latency, and cost for real-time feature serving workloads.

## Capacity Units

When creating an online feature store, the `capacity` parameter controls how much compute the store can use. Capacity is specified using predefined capacity units (CU) that correspond to underlying Lakebase Provisioned instance sizes. ^[databricks-online-feature-stores-databricks-on-aws.md]

The valid capacity options are:

| Capacity Setting | Description |
|-----------------|-------------|
| `CU_1` | Smallest capacity, suitable for low-throughput workloads |
| `CU_2` | Recommended starting point for testing and development |
| `CU_4` | Medium capacity for production workloads |
| `CU_8` | Largest capacity for high-throughput, low-latency requirements |

^[databricks-online-feature-stores-databricks-on-aws.md]

## Right-Sizing Best Practices

Databricks recommends starting with `CU_2` for testing and development purposes. From there, you can scale up or down based on observed performance metrics and cost considerations. ^[databricks-online-feature-stores-databricks-on-aws.md]

Key considerations for capacity sizing include:

- **Throughput requirements**: Higher capacity units support more concurrent read and write operations.
- **Latency SLAs**: Larger capacity reduces response times for real-time inference.
- **Number of feature tables**: Multiple feature tables can share a single online store, so capacity should account for aggregate load.
- **Cost management**: Online stores continuously incur costs, so right-sizing is essential for cost optimization.

## Updating Capacity

For online stores created using `fe.create_online_store()`, you can update the capacity using `fe.update_online_store()`. This allows you to scale compute resources as workload demands change. ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
# Upgrade from CU_2 to CU_4
updated_store = fe.update_online_store(
    name="my-online-store",
    capacity="CU_4"
)
```

Note that capacity updates are not supported for [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) instances that were created using the projects API or the UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Read Replicas for Scaling

To further improve performance for high-concurrency workloads, you can add read replicas to an online store by specifying the `read_replica_count` parameter during creation or update. Read traffic is automatically distributed across replicas, reducing latency and improving scalability. ^[databricks-online-feature-stores-databricks-on-aws.md]

An online feature store supports up to 3 read replicas, for a total of 4 compute instances including the primary. Read replicas also provide high availability by taking over if the primary instance fails. ^[databricks-online-feature-stores-databricks-on-aws.md]

Read replicas cannot be added to Lakebase Autoscaling projects created using the API or UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Optimization Strategies

To manage costs effectively with online feature stores:

- **Reuse online stores**: Publish multiple feature tables to a single online store rather than creating separate stores for each table.
- **Right-size capacity**: Start with `CU_2` for testing and only scale up based on actual performance needs.
- **Delete unused stores**: Online stores continuously incur costs, so delete stores that are no longer needed.
- **Delete during development**: For development and testing, delete online stores when not in use to avoid unnecessary charges.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- Lakebase scale-to-zero is not supported for online feature stores.
- Autoscaling instances created using the projects API or the UI do not use the `capacity` field.
- You cannot update an Autoscaling instance created using the projects API or the UI.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md) — Overview of online feature serving infrastructure
- Lakebase Provisioned — Underlying compute architecture for online stores
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — Alternative provisioning model for online stores
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — Serving features to real-time applications
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md) — Complete feature management workflow

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
