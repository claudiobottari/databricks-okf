---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f1640dd4a37a082d0309f32911c672cdc5b68f4fba07f37eab70559c0a2c5fc
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-legacy-configuration-removal
    - DLLCR
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake Legacy Configuration Removal
description: Recommendation to remove explicit legacy Delta configurations from Spark configs and table properties when upgrading Databricks Runtime to enable new optimizations and default values
tags:
  - delta-lake
  - configuration
  - upgrade
timestamp: "2026-06-19T22:12:52.899Z"
---

# Delta Lake Legacy Configuration Removal

**Delta Lake Legacy Configuration Removal** refers to the recommended practice of removing most explicit legacy Delta configurations from Spark configurations and table properties when upgrading to a new Databricks Runtime version. This practice enables Databricks to apply new optimizations and default values to migrated workloads. ^[best-practices-delta-lake-databricks-on-aws.md]

## Overview

As part of Delta Lake best practices, Databricks advises users to remove explicit legacy configurations that were set in earlier versions. These legacy configurations can prevent new optimizations and default values introduced by later versions of Databricks Runtime from being applied to migrated workloads. ^[best-practices-delta-lake-databricks-on-aws.md]

## Types of Configurations to Remove

Legacy configurations that should be removed include those set in:

- **Spark configurations**: Settings applied at the Spark session or cluster level that control Delta Lake behavior.
- **Table properties**: Explicit properties set on individual Delta tables.

By removing these explicit settings, Databricks can apply its latest default values and optimization strategies, which are often improved with each runtime release. ^[best-practices-delta-lake-databricks-on-aws.md]

## Migration Process

When upgrading to a new Databricks Runtime version, the recommended approach is:

1. Review existing Spark configurations and table properties for any legacy Delta Lake settings.
2. Remove explicit configurations that are no longer necessary.
3. Allow Databricks to apply current default values automatically.

This ensures that migrated workloads benefit from the latest performance improvements and default behaviors without being constrained by outdated settings. ^[best-practices-delta-lake-databricks-on-aws.md]

## Related Best Practices

Legacy configuration removal is part of a broader set of Delta Lake best practices that include:

- Using [Unity Catalog](/concepts/unity-catalog.md) managed tables
- Enabling Predictive Optimization
- Using [Liquid Clustering](/concepts/liquid-clustering.md)
- Using `CREATE OR REPLACE TABLE` when deleting and recreating tables in the same location

## Related Concepts

- [Delta Lake Best Practices](/concepts/delta-lake-general-best-practices.md)
- Databricks Runtime Upgrades
- Delta Lake Configuration
- Spark Configuration Management
- Table Properties
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
