---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9dc5ff3b577af8874eead7f7f47239f4b03a5607c897211560fc5505d82b7039
  pageDirectory: concepts
  sources:
    - monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-deep-clone-for-cross-region-replication
    - DDCFCR
  citations:
    - file: monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
title: Delta Deep Clone for Cross-Region Replication
description: Technique using DEEP CLONE to replicate Delta tables to external locations across regions, enabling incremental updates and avoiding egress costs when recipients access local replicas.
tags:
  - delta-sharing
  - data-replication
  - delta-lake
timestamp: "2026-06-19T19:45:37.292Z"
---

# Delta Deep Clone for Cross-Region Replication

**Delta Deep Clone for Cross-Region Replication** is a technique used by [OpenSharing](/concepts/opensharing.md) providers to replicate Delta tables to external storage locations in different cloud regions. The goal is to avoid cloud vendor egress fees that would otherwise be incurred when recipients access shared data across regions. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Overview

When sharing data with [OpenSharing](/concepts/opensharing.md), a provider can use the `DEEP CLONE` operation to copy a Delta table—including both its data and metadata—to a target location. The clone can be placed in an external storage location that is in a different cloud region. Recipients in that region can then query the replicated copy locally, eliminating cross-region egress charges. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

Deep clones support **incremental updates**: subsequent runs of the clone operation identify only the new data in the source table and refresh the target accordingly. This makes them suitable for ongoing replication without re-copying the entire table each time. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Usage

### Initial replication

The `CREATE TABLE ... DEEP CLONE` syntax is used to create a new table from an existing source table, placing the clone at a specified location:

```sql
CREATE TABLE [IF NOT EXISTS] table_name
  DEEP CLONE source_table_name
  [TBLPROPERTIES clause]
  [LOCATION path];
```

^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

For example, a provider might clone a table from a catalog stored in one region into a catalog whose managed storage location is in another region.

### Incremental refresh

To keep the clone up to date with changes in the source, you can schedule a recurring job that runs the following command:

```sql
CREATE OR REPLACE TABLE table_name DEEP CLONE source_table_name;
```

^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

This command replaces the target table with the latest state of the source, applying only the incremental changes since the last clone. The job can be orchestrated with [Lakeflow Jobs](/concepts/lakeflow-jobs.md) or [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md). ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Replication to Cloudflare R2

Deep clone can also be used to replicate Delta tables to Cloudflare R2 object storage, which charges no egress fees. By cloning source tables into a catalog that uses an R2 bucket as its managed storage location, providers can share the replicated tables via OpenSharing without incurring any cloud-vendor egress costs. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

The same incremental refresh pattern (`CREATE OR REPLACE TABLE ... DEEP CLONE`) applies to keep the R2 copies in sync. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Related concepts

- [OpenSharing](/concepts/opensharing.md) – Delta Sharing protocol for sharing data and AI assets.
- [Delta Sharing](/concepts/delta-sharing.md) – Data sharing platform built on Delta Lake.
- Data egress costs – Charges for transferring data out of a cloud region.
- Cloudflare R2 – Object storage with zero egress fees.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – Workflow automation in Databricks.
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – Alternative approach for incremental replication.
- Clone a table on Databricks – Official documentation for the clone operation.

## Sources

- monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md

# Citations

1. [monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md](/references/monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws-13b884c0.md)
