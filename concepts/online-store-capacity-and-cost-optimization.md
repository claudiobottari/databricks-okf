---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dfb0ae2b2981a4991dac5e4dab46b3faeb3599ab9c5454d47936569588305662
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-store-capacity-and-cost-optimization
    - Cost Optimization and Online Store Capacity
    - OSCACO
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Online Store Capacity and Cost Optimization
description: Best practices for managing online store costs including right-sizing capacity (CU_1 through CU_8), reusing stores across multiple projects, and deleting unused stores that continuously incur costs.
tags:
  - cost-optimization
  - capacity-planning
  - feature-store
timestamp: "2026-06-19T09:53:15.303Z"
---

Here is the wiki page for "Online Store Capacity and Cost Optimization".

---

## Online Store Capacity and Cost Optimization

**Online Store Capacity and Cost Optimization** refers to the best practices for configuring and managing [Databricks Online Feature Stores] to balance performance, cost, and operational overhead. These stores provide low-latency access to feature data for real-time machine learning applications and are built on [Lakebase Autoscaling] infrastructure.

### Capacity Configuration

When creating an online store, the `capacity` setting controls the amount of compute available. Valid options are `"CU_1"`, `"CU_2"`, `"CU_4"`, and `"CU_8"`. These values correspond to [Lakebase Provisioned capacity] levels. ^[databricks-online-feature-stores-databricks-on-aws.md]

For testing and development, start with `CU_2`. Scale up or down based on actual performance requirements and cost trade-offs. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Cost Optimization Best Practices

- **Reuse online stores**: Publish multiple feature tables to a single online store. For development, testing, and training scenarios, share one store across multiple projects or users rather than creating separate stores. This reduces the number of provisioned instances and associated costs. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Right-size capacity**: Begin with `CU_2` for testing. Only scale up or down based on measured performance and cost. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Delete unused online stores**: Online stores continuously incur costs. Remove stores that are no longer needed to avoid ongoing charges. See [Delete an online store]. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Read Replicas

You can add read replicas to an online store to improve performance and scalability for high-concurrency workloads. An online store supports up to three read replicas (four compute instances total, including the primary). ^[databricks-online-feature-stores-databricks-on-aws.md]

Read replicas offload read traffic from the primary and provide high availability by taking over if the primary fails. ^[databricks-online-feature-stores-databricks-on-aws.md]

You cannot add read replicas to a Lakebase Autoscaling project created using the API or the UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Updating Capacity

You can update the capacity of an online store using the `fe.update_online_store` method. Note that this does not work for an Autoscaling instance created using the projects API or the UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Related Concepts

- [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md) — The service for serving features to real-time applications.
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The underlying infrastructure for online stores.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — Endpoints that serve features to real-time applications.
- [Publish a Feature Table](/concepts/feature-table.md) — How to sync features to an online store.
- Lakebase Provisioned capacity — Capacity levels for compute.

### Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
