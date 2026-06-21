---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36591a320cb9e420c7139128e851a7443da33883a1534de79c0ff4c890250f29
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-online-feature-store-cost-optimization
    - DOFSCO
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Databricks Online Feature Store Cost Optimization
description: Best practices for managing costs including reusing online stores across projects, right-sizing capacity from CU_2, and deleting unused stores to avoid continuous charges.
tags:
  - cost-optimization
  - best-practices
  - databricks
timestamp: "2026-06-18T15:08:34.565Z"
---

# Databricks Online Feature Store Cost Optimization

**Databricks Online Feature Store Cost Optimization** refers to practices and strategies for managing infrastructure costs associated with Databricks Online Feature Stores, which are high-performance, scalable solutions for serving feature data to real-time applications and machine learning models. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

Online Feature Stores continuously incur costs because they provision highly available managed infrastructure for real-time feature serving. Without proactive cost management, these costs can grow unnecessarily, particularly in development and testing environments where high-performance capacity may not be required. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Optimization Best Practices

### Reuse Online Stores

You can publish multiple feature tables to a single online store. For development, testing, and training scenarios, Databricks recommends sharing one online store across multiple projects or users rather than creating separate stores. This consolidation reduces the total number of provisioned instances and the associated infrastructure costs. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Right-Size Capacity

Start with `CU_2` capacity for testing purposes. The `capacity` setting controls how much compute your online store can use, with valid options of `CU_1`, `CU_2`, `CU_4`, and `CU_8`. Scale up or down based on actual performance requirements and cost considerations rather than provisioning capacity upfront. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Delete Unused Online Stores

Online stores continuously incur costs even when not actively serving features. Databricks recommends deleting online stores that are no longer needed, particularly for development and test instances that are used intermittently. The `fe.delete_online_store(name="my-online-store")` API removes the store and stops all associated costs. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Manage Development and Testing Stores

For development and testing workflows, actively delete Lakebase Provisioned online stores when they are not in use. This practice prevents idle resources from accumulating costs between development sessions. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md) — The core infrastructure for real-time feature serving
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — The service layer that consumes online features
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The underlying infrastructure for new online stores
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — Services that may depend on online feature stores
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md) — Broader feature management workflows

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
