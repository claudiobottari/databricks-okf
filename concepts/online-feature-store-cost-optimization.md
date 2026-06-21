---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84467bd6981876ca76b6e893218d4007f5a5d0658cd41d5819c6b283fdbb92b4
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-store-cost-optimization
    - OFSCO
    - online-feature-store-capacity-and-cost-optimization
    - Cost Optimization and Online Feature Store Capacity
    - OFSCACO
    - online-store-capacity-and-cost-optimization
    - Cost Optimization and Online Store Capacity
    - OSCACO
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Feature Store Cost Optimization
description: Best practices for managing costs including reusing online stores across projects, right-sizing capacity starting with CU_2, and deleting unused stores to avoid continuous charges.
tags:
  - cost-management
  - best-practices
  - optimization
timestamp: "2026-06-18T11:39:49.604Z"
---

# Online Feature Store Cost Optimization

**Online Feature Store Cost Optimization** refers to the set of practices and strategies for minimizing the cost of running [Online Feature Store](/concepts/online-feature-store.md) instances in Databricks. Because online stores are continuously provisioned infrastructure that do not support scale-to-zero, active cost management is essential for development, testing, and production workloads. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Key Cost Drivers

Online stores are backed by [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) instances that run 24/7. The primary cost drivers are the number of stores, their capacity (compute size), and the usage of read replicas. The `capacity` parameter — available as `CU_1`, `CU_2`, `CU_4`, or `CU_8 —` controls how much compute the store can use. Read replicas improve read throughput but add additional compute costs. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Optimization Strategies

### Reuse Online Stores

A single online store can host multiple published feature tables. For development, testing, and training scenarios, Databricks recommends sharing one online store across multiple projects or users rather than creating separate stores. This consolidation reduces the number of continuously running instances and the associated compute cost. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Right-Size Capacity

Start with `CU_2` for testing and experimentation. Monitor performance and cost metrics, then scale up or down as needed. Over-provisioning capacity unnecessarily increases cost, while under-provisioning may impact latency. The `update_online_store` API allows changing capacity after creation. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Delete Unused Online Stores

Online stores incur cost continuously as long as they exist, because Lakebase does not support scale-to-zero. Delete stores that are no longer needed using `fe.delete_online_store()`. This is especially important for ephemeral development and testing stores. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Manage Read Replicas

Read replicas distribute read traffic and improve performance for high-concurrency workloads, but each replica adds compute cost. Only add replicas when required by actual traffic patterns; start without replicas and add only if latency or throughput targets are not met. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Monitoring and Governance

- **Audit usage**: Use `list_online_stores()` to track which stores exist and their capacity. Regularly review stores to identify idle or underutilized instances.
- **Tag online stores**: Apply workspace-level tags to online stores to attribute costs to teams or projects. Tags are inherited from the workspace.
- **Set budgets**: Use Databricks budget policies or cloud provider cost alerts to detect unexpected spending spikes.

## Best Practices Summary

| Practice | Action |
|----------|--------|
| **Reuse** | Publish multiple feature tables to one online store; avoid creating a separate store per project during development. |
| **Right-size** | Start with `CU_2` and adjust based on observed latency and throughput. |
| **Delete** | Remove stores that are no longer needed; online stores continuously incur costs. |
| **Replicas** | Add read replicas only when necessary; each replica adds cost. |

## Limitations That Affect Cost

- **No scale-to-zero**: Lakebase Autoscaling instances do not automatically shut down when idle. An online store will continue to incur costs even when no queries are being served. This makes deletion of unused stores the only way to stop charges. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Capacity cannot be updated for Autoscaling instances created via the projects API or UI**: Only stores created with `fe.create_online_store()` support in-place capacity changes. For other stores, you must delete and recreate with a different capacity. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md)
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md)
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Capacity Sizing

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
