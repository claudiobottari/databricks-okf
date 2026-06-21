---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf8ceffce66b59bf54a2024c0b68890938ef29bb4f8041a2af20772e378df0bc
  pageDirectory: concepts
  sources:
    - migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-online-tables
    - LOT
  citations:
    - file: migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
title: Legacy Online Tables
description: The original Databricks online table product being deprecated; users are instructed to migrate to Online Feature Store or Lakebase synced tables.
tags:
  - migration
  - deprecation
timestamp: "2026-06-19T19:33:45.450Z"
---

# Legacy Online Tables

**Legacy Online Tables** were a Databricks feature for synchronizing Unity Catalog tables to a low-latency serving store, enabling real-time inference use cases. As of the migration documentation, these tables have been superseded by newer architectures: the [Online Feature Store](/concepts/online-feature-store.md) for model and feature serving endpoints, and [Lakebase synced tables](/concepts/lakebase-synced-table.md) for OLTP workloads.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## History and Deprecation

Online tables provided a mechanism to automatically sync data from Unity Catalog tables into an online store for low-latency retrieval. However, Databricks has since introduced more robust solutions. Since March 12, 2026, new Lakebase instances are created as [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) projects, and existing Provisioned instances have been undergoing automatic upgrades to Autoscaling starting in June 2026.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Migration Paths

Databricks provides two primary migration paths from legacy online tables depending on the use case.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

### Migration to Online Feature Store

For users who need low-latency feature serving for model endpoints, the recommended migration is to the [Online Feature Store](/concepts/online-feature-store.md). This approach involves:

1. **Create an online feature store:** Use the `FeatureEngineeringClient` to create a store (e.g., with capacity `CU_2`). Databricks recommends a single online store per workspace for testing, with additional stores for production isolation.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]
2. **Publish feature tables:** Publish the relevant feature tables to the new online store.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]
3. **Redeploy serving endpoints:** Set the `FEATURE_SOURCE` environment variable to `DATABRICKS_ONLINE_STORE` on each served entity and redeploy. After publishing, any subsequent change to serving endpoints (including scaling operations) automatically switches them to use the Online Feature Store as the default source.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]
4. **Verify and clean up:** Check endpoint events for messages like "Linked to Online Feature Store table" to confirm the switch, then delete the legacy online table.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

### Migration to Lakebase Synced Tables

For OLTP (online transaction processing) workloads, the recommended migration is to [Lakebase synced tables](/concepts/lakebase-synced-table.md):

1. **Create a database instance:** Set up a Lakebase database instance to store synced tables. Optionally register the database in Unity Catalog for privilege management.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]
2. **Create a synced table:** A synced table is a Unity Catalog read-only Postgres table that automatically synchronizes data from a Unity Catalog table to the Lakebase database instance. To migrate, use the source table of the legacy online table as the basis for the new synced table — this table is visible in the **Catalog** UI under the online table's **Overview** tab.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]
3. **Query directly:** After creation, connect to the database instance and query the synced table directly.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]
4. **Clean up:** Delete the legacy online table after confirming the synced table is working.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Identifying Existing Online Tables

To inventory all existing legacy online tables in a workspace, users can query the `system.billing.usage` table, filtering for `billing_origin_product = 'ONLINE_TABLES'`. This query shows the pipeline URLs and usage quantities for online table-related billing over the past 7 days.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Cleanup

After migration, legacy online tables can be deleted through the UI (using the kebab menu on the online table page) or via the Databricks SDK (`w.online_tables.delete('catalog.schema.table_name')`) or REST API. Deleting the online table stops any ongoing data synchronization and releases all its resources.^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md) — The replacement for model and feature serving use cases
- [Lakebase synced tables](/concepts/lakebase-synced-table.md) — The replacement for OLTP use cases
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The latest version of Lakebase with autoscaling compute
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) — Endpoints that consume feature stores
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system underlying both legacy and new table architectures

## Sources

- migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md

# Citations

1. [migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md](/references/migrate-from-legacy-and-third-party-online-tables-databricks-on-aws-4e5cf207.md)
