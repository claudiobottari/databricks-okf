---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1cdc8f8d6ef798901f82d543cfcd0aa5288e34a0a17b609c13122f9ef1c02e2f
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-lakebase-autoscaling
    - DLA
    - Lakebase Autoscaling project
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Databricks Lakebase Autoscaling
description: The underlying infrastructure for Online Feature Stores—a Lakebase Autoscaling project that provisions highly available managed compute for real-time feature serving.
tags:
  - infrastructure
  - autoscaling
  - databricks
timestamp: "2026-06-18T15:08:04.101Z"
---

# Databricks Lakebase Autoscaling

**Databricks Lakebase Autoscaling** is the default project type for new [Online Feature Stores](/concepts/online-feature-store.md) created on Databricks. It provides a managed, high-performance infrastructure for serving feature data to real-time applications, with automatic scaling capabilities that adjust compute resources based on workload demands. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

Lakebase Autoscaling powers the [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md), which serves features to real-time applications such as recommendation systems, fraud detection, and personalization engines. When you create an online feature store using the `create_online_store` API, it creates a Lakebase Autoscaling instance. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Key Characteristics

### Automatic Scaling

Unlike Lakebase Provisioned instances, Lakebase Autoscaling instances automatically adjust their compute capacity based on demand. This eliminates the need to manually manage capacity settings through the projects API or UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Capacity Options

When creating an online feature store, you specify a `capacity` setting that controls compute resources. Valid options are `CU_1`, `CU_2`, `CU_4`, and `CU_8`, which correspond to Lakebase Provisioned capacity units. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Customer-Managed Key (CMK) Support

Lakebase Autoscaling instances support encryption at rest with customer-managed keys (CMK). This applies automatically when:
- The workspace has a customer-managed key configured for managed services
- The online feature store is backed by a Lakebase Autoscaling project
- The backing Lakebase project was created after CMK support became available in the region

No additional Lakebase or Feature Store configuration is required for CMK. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- **Scale-to-zero**: Lakebase Autoscaling does not support scale-to-zero. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Multi-store lookups**: Feature Serving and Model Serving endpoints that look up features from multiple online feature stores cannot use Lakebase Autoscaling instances. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **API/UI-created instances**: Autoscaling instances created using the projects API or the UI do not support the `creator`, `read_replica_count`, and `capacity` fields. ^[databricks-online-feature-stores-databricks-on-aws.md]
- **Update restrictions**: You cannot update an Autoscaling instance that was created using the projects API or the UI. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Cost Management

To manage costs, Databricks recommends:
- **Reusing online stores**: Publish multiple feature tables to a single online store rather than creating separate stores for development, testing, and training.
- **Right-sizing capacity**: Start with `CU_2` for testing and scale up or down based on performance and cost needs.
- **Deleting unused stores**: Online stores continuously incur costs, so delete stores that are no longer needed. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Migration

For details on differences between Lakebase Autoscaling and Lakebase Provisioned instances, and guidance on migrating, see the documentation on [Lakebase unification on Autoscaling](/concepts/lakebase-autoscaling.md). ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md) – The feature store powered by Lakebase Autoscaling
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) – How features are served to real-time applications
- Lakebase Provisioned – The alternative project type with fixed capacity
- [Databricks Feature Engineering Client](/concepts/databricks-feature-engineering-client.md) – The API for creating and managing online stores
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – Endpoints that can perform automatic feature lookup

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
