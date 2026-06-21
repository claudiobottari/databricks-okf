---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 341f41c717ef5457dfb5e4185a5493e59994f37bca6bb2dc55a0fca4644dbb72
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-store-capacity-and-cost-optimization
    - Cost Optimization and Online Feature Store Capacity
    - OFSCACO
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Feature Store Capacity and Cost Optimization
description: Best practices for managing online store capacity settings (CU_1 through CU_8) and minimizing costs by reusing stores, right-sizing, and deleting unused stores.
tags:
  - cost-management
  - capacity-planning
  - best-practices
timestamp: "2026-06-19T18:14:30.288Z"
---

Here is the wiki page for "Online Feature Store Capacity and Cost Optimization".

---

## Online Feature Store Capacity and Cost Optimization

**Online Feature Store Capacity and Cost Optimization** refers to the set of best practices for managing the compute capacity and ongoing expenses of a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md). Because online stores provision Lakebase Autoscaling instances that continuously incur costs while active, careful planning around capacity sizing, reuse, and lifecycle management is essential for cost-effective deployment. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Capacity Sizing

The `capacity` parameter on an [Online Feature Store](/concepts/online-feature-store.md) controls how much compute the store can use and is expressed as a Lakebase Provisioned capacity unit (e.g., `CU_1`, `CU_2`, `CU_4`, `CU_8`). Higher values provide more throughput for read and write operations but also increase cost. ^[databricks-online-feature-stores-databricks-on-aws.md]

**Recommended approach**:
- Start with `CU_2` for development and testing.
- Scale up or down only after measuring actual workload performance and cost.
- Capacity can be changed after creation using `fe.update_online_store()` (but this only works for stores created with the `fe.create_online_store` API, not for stores created via the Lakebase UI or projects API). ^[databricks-online-feature-stores-databricks-on-aws.md]

### Reuse Online Stores

A single online store can host multiple feature tables. For development, testing, and training scenarios, share one store across multiple projects or users rather than creating separate stores per team or experiment. This reduces the number of provisioned instances and lowers total cost. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Delete Unused Stores

Online stores continuously incur costs while they exist. Any store that is no longer needed should be deleted promptly:

```python
fe.delete_online_store(name="my-online-store")
```

Deleting a store also removes its backing Lakebase project. Before deletion, verify that no model serving or feature serving endpoints depend on the store’s online tables – otherwise downstream workflows will fail. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Read Replicas and Scale-Out

When creating or updating a store, the `read_replica_count` parameter can add up to three read replicas (four compute instances total including the primary). Read replicas offload read traffic from the primary and provide high availability if the primary fails. Replicas are **not** supported on stores created via the Lakebase API or UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Limitations That Affect Cost

- **Scale-to-zero** is not supported. Once provisioned, the store’s compute is always on until explicitly deleted. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Customer-managed keys (CMK)** for encryption at rest apply automatically only if the backing Lakebase project was created after CMK became available in the region. Stores created before that cannot be encrypted with a CMK even if the workspace later enables one. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Related Concepts

- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) – The underlying compute model that powers online feature stores.
- [Online Feature Store](/concepts/online-feature-store.md) – Definition, creation, and management of online stores.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) – The front-end that consumes features from an online store.
- [Publish Modes](/concepts/publish-modes-for-online-feature-tables.md) – Controls how data is synced from offline to online stores (`CONTINUOUS` vs `TRIGGERED`).
- Read Replicas – Additional compute instances that improve read throughput and availability.

### Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
