---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c968ca7b457e647f43e72149ccd15e77dd450a53a2e9452529d87a321f128246
  pageDirectory: concepts
  sources:
    - migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakebase-synced-table
    - LST
    - Lakebase Synced Tables
    - Lakebase synced tables
  citations:
    - file: migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
title: Lakebase Synced Table
description: A Unity Catalog read-only Postgres table that automatically synchronizes data from a Unity Catalog table to a Lakebase database instance for OLTP workloads.
tags:
  - oltp
  - lakebase
  - data-synchronization
timestamp: "2026-06-19T19:33:29.700Z"
---

# Lakebase Synced Table

A **Lakebase Synced Table** is a read-only Postgres table in [Unity Catalog](/concepts/unity-catalog.md) that automatically synchronizes data from a Unity Catalog table to a Lakebase database instance. It is designed to serve lakehouse data for online transaction processing (OLTP) workloads, such as low-latency queries, while keeping the data in sync with its source table. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Overview

Synced tables are part of the Lakebase offering, which provides a managed Postgres-compatible database on Databricks. They are created from an existing Unity Catalog table and remain synchronized with it, meaning any changes to the source table are automatically reflected in the synced table. Because the synced table is read-only, all writes must go through the source Unity Catalog table. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

Lakebase synced tables can be used as a migration target for legacy [Online Tables](/concepts/online-tables.md) when the goal is to support OLTP-style access rather than serving features for machine learning models.

## Lakebase Provisioned vs. Autoscaling

Two variants of Lakebase exist:

- **Lakebase Provisioned** (the original offering) uses provisioned compute that you scale manually.  
- **Lakebase Autoscaling** (the latest version) provides autoscaling compute, scale-to-zero, branching, and instant restore.  

Since March 12, 2026, new Lakebase instances are created as Autoscaling projects. Existing Provisioned instances are being upgraded automatically starting in June 2026. When working with synced tables, you should use an Autoscaling instance if available. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Creating a Lakebase Synced Table

To create a synced table:

1. **Create a Lakebase database instance** (see Create and manage a database instance). Optionally register the database in Unity Catalog to use Unity Catalog privileges for data access. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

2. **Navigate to the source table** of the legacy online table in the Catalog Explorer.  
3. **Create the synced table** from that source table. The synced table can be stored in the same catalog location as the original online table, and you can share a pipeline between multiple synced tables. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

After creation, you can connect to the database instance and query the synced table directly via Postgres-compatible clients.

## Use Cases

Synced tables are primarily used for **OLTP scenarios** where low-latency reads on synchronized data are required. Common use cases include:

- Powering real-time dashboards or applications.
- Replacing legacy [Online Tables](/concepts/online-tables.md) when the workload is transactional rather than feature-serving.
- Providing a read-only copy of a Unity Catalog table for external services or tools that connect to Postgres.

## Related Concepts

- Lakebase – The managed Postgres database service on Databricks.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance and metadata layer for tables.
- [Online Table](/concepts/online-tables.md) – The legacy feature-serving table type that synced tables can replace.
- [Online Feature Store](/concepts/online-feature-store.md) – An alternative migration target for feature-serving endpoints.
- Data synchronization – The mechanism keeping the synced table up to date.

## Sources

- migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md

# Citations

1. [migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md](/references/migrate-from-legacy-and-third-party-online-tables-databricks-on-aws-4e5cf207.md)
