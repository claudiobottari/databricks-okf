---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c17d1331b325bf99d38a18e203c78ba6db2b8440607466f09c16095e32c8f98b
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-delta-configuration-migration
    - LDCM
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Legacy Delta Configuration Migration
description: Recommendation to remove explicit legacy Delta configurations from Spark configurations and table properties when upgrading to a new Databricks Runtime version to enable new optimizations and defaults.
tags:
  - delta-lake
  - migration
  - configuration
timestamp: "2026-06-18T14:32:18.828Z"
---

# Legacy Delta Configuration Migration

**Legacy Delta Configuration Migration** refers to the process of removing most explicit legacy Delta Lake configurations from Spark configurations and table properties when upgrading to a new Databricks Runtime version. Legacy configurations can prevent new optimizations and default values introduced by Databricks from being applied to migrated workloads. ^[best-practices-delta-lake-databricks-on-aws.md]

## Overview

As Delta Lake evolves, Databricks introduces improved default behaviors and optimizations that may conflict with explicitly set legacy configurations. These configurations, if left in place, can block the automatic application of performance improvements and prevent workloads from benefiting from newer platform features. ^[best-practices-delta-lake-databricks-on-aws.md]

## Why Legacy Configurations Should Be Removed

Legacy Delta configurations can prevent new optimizations from being applied to migrated workloads. Databricks recommends removing most explicit legacy Delta configurations from both Spark configurations and table properties when upgrading to a new Databricks Runtime version. ^[best-practices-delta-lake-databricks-on-aws.md]

## Recommended Approach

When upgrading to a new Databricks Runtime version, identify and remove explicit Delta configuration settings that are no longer necessary. Allow Databricks to apply its default optimizations instead of overriding them with custom settings. ^[best-practices-delta-lake-databricks-on-aws.md]

## Related Best Practices

- Use [Unity Catalog](/concepts/unity-catalog.md) managed tables for Delta Lake workloads. ^[best-practices-delta-lake-databricks-on-aws.md]
- Enable [predictive optimization](/concepts/delta-lake-predictive-optimization.md) for Unity Catalog managed tables to automatically optimize performance. ^[best-practices-delta-lake-databricks-on-aws.md]
- Use [Liquid Clustering](/concepts/liquid-clustering.md) for improved data layout and query performance. ^[best-practices-delta-lake-databricks-on-aws.md]
- When deleting and recreating a table in the same location, always use a `CREATE OR REPLACE TABLE` statement. ^[best-practices-delta-lake-databricks-on-aws.md]

## Types of Legacy Configurations

Legacy configurations can be set at different levels:

- **Spark session configurations** – Settings applied at the cluster or session level
- **Table properties** – Settings stored in the Delta table metadata

Both levels should be reviewed and cleaned up during migration. ^[best-practices-delta-lake-databricks-on-aws.md]

## Migration Checklist

1. Review all Spark configurations related to Delta Lake
2. Review all Delta table properties for legacy settings
3. Remove configurations that override default Databricks behavior
4. Test workloads with default settings after migration
5. Monitor for performance improvements from new optimizations

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage format for data lakes
- Databricks Runtime — The execution environment for Databricks workloads
- Predictive Optimization — Automatic optimization for Unity Catalog managed tables
- [Liquid Clustering](/concepts/liquid-clustering.md) — Advanced data layout optimization
- [Unity Catalog](/concepts/unity-catalog.md) — Centralized data governance and management

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
