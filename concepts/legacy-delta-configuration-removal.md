---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 919b5d15949b315d00aa2134590a893fa302d7865ecdc02593c457cd62509e1c
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-delta-configuration-removal
    - LDCR
    - delta-lake-legacy-configuration-removal
    - DLLCR
    - legacy-delta-configuration-migration
    - LDCM
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Legacy Delta Configuration Removal
description: Best practice of removing explicit legacy Delta configurations from Spark configs and table properties when upgrading Databricks Runtime versions to avoid blocking new optimizations.
tags:
  - delta-lake
  - configuration
  - migration
timestamp: "2026-06-19T14:08:37.515Z"
---

# Legacy Delta Configuration Removal

**Legacy Delta Configuration Removal** refers to the practice of removing explicit legacy Delta Lake configurations from Spark configurations and table properties when upgrading to a new Databricks Runtime version. This cleanup is recommended to ensure that new optimizations and default values introduced by Databricks can be properly applied to migrated workloads. ^[best-practices-delta-lake-databricks-on-aws.md]

## Overview

As Databricks releases new Runtime versions, they often introduce improved default settings and optimization techniques for [Delta Lake](/concepts/delta-lake.md) tables. Legacy configurations — whether set as Spark session configurations or as table properties — can override these new defaults, preventing workloads from benefiting from performance improvements and bug fixes. ^[best-practices-delta-lake-databricks-on-aws.md]

## Why Remove Legacy Configurations

Legacy configurations can cause the following issues:

- **Block new optimizations**: Explicit settings may prevent Databricks from applying newer, more efficient algorithms or default values. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Prevent default value updates**: When Databricks changes a default configuration to a better value, an explicit legacy setting will override that change. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Cause compatibility issues**: Older configuration values may not be compatible with newer Runtime features or may produce suboptimal behavior. ^[best-practices-delta-lake-databricks-on-aws.md]

## Configurations to Remove

While the source material does not provide an exhaustive list, the general recommendation is to remove most explicit legacy Delta configurations. Common examples include:

- `spark.databricks.delta.*` properties set in Spark configurations
- `delta.*` table properties set via `ALTER TABLE SET TBLPROPERTIES`
- Legacy compaction and file size tuning settings that are now handled automatically

## When to Remove

Databricks recommends removing legacy configurations when upgrading to a new Databricks Runtime version. This is an opportunity to audit existing configurations and let the new Runtime apply its optimized defaults. ^[best-practices-delta-lake-databricks-on-aws.md]

## Best Practices

- **Audit existing configurations**: Before upgrading, review all Spark configurations and table properties related to Delta Lake. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Test after removal**: After removing legacy configurations, test workloads to verify that the new defaults produce correct and performant results. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Use modern alternatives**: Instead of legacy configurations, adopt modern Databricks features such as [predictive optimization](/concepts/delta-lake-predictive-optimization.md), [Liquid Clustering](/concepts/liquid-clustering.md), and [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md). ^[best-practices-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Best Practices](/concepts/delta-lake-general-best-practices.md) — General recommendations for Delta Lake workloads
- Predictive Optimization — Automatically runs OPTIMIZE and VACUUM on managed tables
- [Liquid Clustering](/concepts/liquid-clustering.md) — Modern clustering approach for Delta tables
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) — Recommended table type for Delta Lake
- Databricks Runtime Upgrades — Process for upgrading to new Runtime versions

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
