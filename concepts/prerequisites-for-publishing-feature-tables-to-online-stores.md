---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21b6aea828033013266cf81f14bba8501566c5acf88db0c0e73afbf6566fad72
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-publishing-feature-tables-to-online-stores
    - PFPFTTOS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
      start: 65
      end: 78
    - file: databricks-online-feature-stores-databricks-on-aws.md
      start: 67
      end: 67
    - file: databricks-online-feature-stores-databricks-on-aws.md
      start: 68
      end: 68
    - file: databricks-online-feature-stores-databricks-on-aws.md
      start: 69
      end: 70
    - file: databricks-online-feature-stores-databricks-on-aws.md
      start: 73
      end: 78
    - file: databricks-online-feature-stores-databricks-on-aws.md
      start: 70
      end: 70
title: Prerequisites for Publishing Feature Tables to Online Stores
description: Feature tables must satisfy primary key constraints, non-nullable primary key columns, and Change Data Feed (CDF) enablement before they can be published to an online store for real-time serving.
tags:
  - feature-store
  - prerequisites
  - data-governance
timestamp: "2026-06-19T09:53:15.202Z"
---

# Prerequisites for Publishing Feature Tables to Online Stores

Before a feature table can be published to a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) for low-latency serving, the offline source table must satisfy a set of structural and configuration requirements. These prerequisites apply to all feature tables – both with and without time series support. ^[databricks-online-feature-stores-databricks-on-aws.md#L65-L78]

## Primary Key Constraint

The feature table must have a defined primary key. Databricks Online Feature Stores require that every published table includes a primary key constraint; this constraint is used to identify the rows that need to be synchronized between the offline table and the online store. ^[databricks-online-feature-stores-databricks-on-aws.md#L67]

## Non‑nullable Primary Key Columns

All columns that belong to the primary key must be declared as `NOT NULL`. Primary key columns cannot contain `NULL` values because the online store uses the primary key as the lookup key for real-time serving. If any primary key column is nullable, publishing will fail. ^[databricks-online-feature-stores-databricks-on-aws.md#L68]

## Change Data Feed (CDF) Enabled

The offline feature table must have the **Delta Change Data Feed** (CDF) enabled if you intend to use the `CONTINUOUS` or `TRIGGERED` publish modes. CDF captures incremental changes (inserts, updates, deletes) so that the sync pipeline can efficiently propagate updates without re‑reading the entire table. ^[databricks-online-feature-stores-databricks-on-aws.md#L69-L70]

For an existing table, you can enable CDF and enforce `NOT NULL` with the following SQL statements:

```sql
-- Enable CDF if not already enabled
ALTER TABLE catalog.schema.your_feature_table
SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');

-- Ensure primary key columns are not nullable
ALTER TABLE catalog.schema.your_feature_table
ALTER COLUMN user_id SET NOT NULL;
```

^[databricks-online-feature-stores-databricks-on-aws.md#L73-L78]

If you do not need incremental sync (e.g., you are using a one‑time or batch‑only publish mode), CDF may not be strictly required. However, the documentation strongly recommends enabling CDF for all feature tables that will be published to an online store to allow the most flexible publish mode selection. ^[databricks-online-feature-stores-databricks-on-aws.md#L69-L70]

## Additional Considerations

- The `publish_mode` parameter of the `publish_table` API determines how and when the online table is updated. The supported modes are documented in the online store publish modes section. Starting from version 0.13.0.1, the `publish_mode` parameter replaces the older `streaming` parameter; `streaming=True` is treated as equivalent to `publish_mode="CONTINUOUS"`. ^[databricks-online-feature-stores-databricks-on-aws.md#L70]
- Publishing always uses the default branch of the underlying [Lakebase Autoscaling project](/concepts/databricks-lakebase-autoscaling.md). ^[databricks-online-feature-stores-databricks-on-aws.md#L70]

## Summary Checklist

| Requirement | Description |
|-------------|-------------|
| Primary key constraint | A defined primary key on the feature table. |
| Non‑nullable PK columns | Primary key columns must be `NOT NULL`. |
| Change Data Feed enabled | Required for `CONTINUOUS` and `TRIGGERED` modes. |

Meeting these three prerequisites ensures that the offline feature table can be synchronized to an online store with minimal manual intervention.

## Related Concepts

- [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md)
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The client used to publish tables.
- Change Data Feed on Delta Tables – How to enable and use CDF.
- Publish Modes for Online Tables – Explanation of `CONTINUOUS`, `TRIGGERED`, and other modes.
- Lakebase Autoscaling Projects – The compute infrastructure backing online stores.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md:65-78](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
2. [databricks-online-feature-stores-databricks-on-aws.md:67-67](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
3. [databricks-online-feature-stores-databricks-on-aws.md:68-68](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
4. [databricks-online-feature-stores-databricks-on-aws.md:69-70](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
5. [databricks-online-feature-stores-databricks-on-aws.md:73-78](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
6. [databricks-online-feature-stores-databricks-on-aws.md:70-70](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
