---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dea8ec700400462516c209a87768170debc5e6acb60470b0d9af2bacbf8705b0
  pageDirectory: concepts
  sources:
    - migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakebase-autoscaling
    - Lakebase Autoscaling project
    - Lakebase unification on Autoscaling
  citations:
    - file: migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
title: Lakebase Autoscaling
description: The latest version of Lakebase with autoscaling compute, scale-to-zero, branching, and instant restore, replacing the original Lakebase Provisioned offering.
tags:
  - oltp
  - lakebase
  - autoscaling
timestamp: "2026-06-19T19:33:57.443Z"
---

# Lakebase Autoscaling

**Lakebase Autoscaling** is the latest version of Databricks Lakebase, a managed PostgreSQL-compatible database service. It offers autoscaling compute, scale-to-zero, branching, and instant restore capabilities. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Key Features

- **Autoscaling compute**: compute capacity scales automatically based on workload demand.
- **Scale-to-zero**: the instance can scale down to zero when idle, reducing cost.
- **Branching**: enables development and testing workflows using isolated branches.
- **Instant restore**: allows quick recovery from backups without lengthy provisioning.

These features make Lakebase Autoscaling suitable for a variety of transactional and operational workloads. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Upgrade and Migration

Since March 12, 2026, all new Lakebase instances are created as Autoscaling projects. Existing Lakebase Provisioned instances are automatically upgraded to Autoscaling starting in June 2026. For details, see the upgrade guide. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Related Concepts

- Lakebase Provisioned — The original Lakebase offering, now being upgraded to Autoscaling.
- [Online Feature Stores](/concepts/online-feature-store.md) — Real-time feature serving; Lakebase Autoscaling can serve as its underlying infrastructure.
- Lakebase Projects — The resource management model for Autoscaling instances.
- [Scale-to-Zero](/concepts/scale-to-zero-in-model-serving.md) — A key Autoscaling capability that reduces costs when idle.

## Sources

- migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md

# Citations

1. [migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md](/references/migrate-from-legacy-and-third-party-online-tables-databricks-on-aws-4e5cf207.md)
