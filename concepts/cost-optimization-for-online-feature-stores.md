---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 771e0b853ea0a057036f3e5a43c2521e09aba8145c1e11be5195779ae4897da7
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cost-optimization-for-online-feature-stores
    - COFOFS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Cost Optimization for Online Feature Stores
description: Best practices for managing online store costs including reusing stores across projects, right-sizing capacity (starting at CU_2), and deleting unused stores that continuously incur costs.
tags:
  - cost-management
  - best-practices
  - optimization
timestamp: "2026-06-19T14:52:06.391Z"
---

# Cost Optimization for Online Feature Stores

**Cost optimization for online feature stores** involves strategies to reduce and control the recurring infrastructure costs of serving real-time feature data to applications and machine learning models. Online stores are managed, highly available compute instances that continuously incur costs while running, so careful sizing, reuse, and lifecycle management are essential.

## Overview

Online feature stores on Databricks are backed by Lakebase Autoscaling (or Lakebase Provisioned) instances, which bill continuously while active. Unlike batch compute, there is no scale‑to‑zero capability for online stores, meaning cost accrual stops only when the store is explicitly deleted. ^[databricks-online-feature-stores-databricks-on-aws.md]

The primary cost levers are the **number of online stores**, the **capacity setting** of each store, and whether stores are left running when not in use. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Best Practices

### Reuse Online Stores

Multiple feature tables can be published to a single online store. For development, testing, and training scenarios, sharing one online store across several projects or users is strongly recommended rather than creating separate stores for each purpose. This consolidates infrastructure and avoids paying for redundant compute. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Right‑Size Capacity

When creating an online store, the `capacity` parameter controls the amount of compute allocated. Valid capacity options are `"CU_1"`, `"CU_2"`, `"CU_4"`, and `"CU_8"`. Start with `"CU_2"` for testing and only scale up or down based on observed performance and actual workload demands. Over‑provisioning at the start leads to unnecessary cost. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Delete Unused Online Stores

Online stores incur costs continuously—even when idle—because they are always‑on managed instances. Deleting stores that are no longer needed is the most direct way to stop cost accrual. For development and testing, delete online stores when they are not in active use. ^[databricks-online-feature-stores-databricks-on-aws.md]

Before deleting a store, ensure that none of its online tables are referenced by [Feature Serving endpoints](/concepts/feature-serving-endpoint.md) or [Model Serving endpoints](/concepts/model-serving-endpoint.md), as deletion can cause unexpected failures in downstream dependencies. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md) – The managed infrastructure for real‑time feature serving.
- [Feature Serving endpoints](/concepts/feature-serving-endpoint.md) – The mechanism to serve features to applications.
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) – The underlying compute platform for online stores.
- [Publish a feature table to an online store](/concepts/publishing-feature-tables-to-online-stores.md) – How feature data flows from offline to online.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance layer for feature tables and lineage.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
