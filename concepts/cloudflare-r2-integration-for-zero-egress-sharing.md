---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe2693063049f4046cca335c503e38b75991fb0686e034019f8e25e897bd7a15
  pageDirectory: concepts
  sources:
    - monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cloudflare-r2-integration-for-zero-egress-sharing
    - CRIFZS
    - Cloudflare R2 storage for egress-free sharing
  citations:
    - file: monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
title: Cloudflare R2 Integration for Zero-Egress Sharing
description: Using Cloudflare R2 object storage as the backing store for OpenSharing shares to eliminate cloud vendor egress fees, including setup steps for mounting R2 buckets as external locations in Unity Catalog.
tags:
  - delta-sharing
  - cloudflare-r2
  - storage
  - cost-management
timestamp: "2026-06-19T19:46:05.219Z"
---

# Cloudflare R2 Integration for Zero-Egress Sharing

**Cloudflare R2 Integration for Zero-Egress Sharing** refers to the use of Cloudflare R2 object storage as a backend for [OpenSharing](/concepts/opensharing.md) (Delta Sharing) on Databricks to eliminate cloud vendor egress fees. Because Cloudflare R2 charges no egress fees, replicating or migrating shared data to R2 enables providers to share data without incurring the per-byte egress costs that typically apply when sharing across clouds or regions. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Overview

When sharing data using OpenSharing, cloud vendors may charge data egress fees for data transferred across cloud boundaries or geographic regions. If data is shared within the same region, no egress cost applies. Cloudflare R2 object storage natively incurs no egress fees, making it an attractive option for multi-region or multi-cloud sharing scenarios. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

Using R2 does not eliminate egress costs for view sharing, which may still incur charges. The integration applies specifically to table-based sharing. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Requirements

- Databricks workspace enabled for [Unity Catalog](/concepts/unity-catalog.md).
- Databricks Runtime 14.3 or above, or SQL Warehouse 2024.15 or above.
- Cloudflare account. See [sign up](https://dash.cloudflare.com/sign-up).
- Cloudflare R2 Admin role. See the [Cloudflare roles documentation](https://developers.cloudflare.com/fundamentals/setup/manage-members/roles/#account-scoped-roles).
- `CREATE STORAGE CREDENTIAL` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) (account admins and [Metastore](/concepts/metastore.md) admins have this by default).
- `CREATE EXTERNAL LOCATION` privilege on both the [Metastore](/concepts/metastore.md) and the storage credential ([Metastore](/concepts/metastore.md) admins have this by default).
- `CREATE MANAGED STORAGE` privilege on the external location.
- `CREATE CATALOG` on the [Metastore](/concepts/metastore.md) ([Metastore](/concepts/metastore.md) admins have this by default).

^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Limitations

Providers cannot share R2 tables that use [Liquid Clustering](/concepts/liquid-clustering.md) and V2 checkpoint. This limitation applies only to tables stored in R2 that use these specific features. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Setup Process

### 1. Mount an R2 Bucket as an External Location

First, create a Cloudflare R2 bucket. See external location documentation for step-by-step guidance. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

Create a storage credential in Unity Catalog that grants access to the R2 bucket. Then use that credential to create an external location in Unity Catalog pointing to the R2 bucket path. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

### 2. Create a Catalog Using the External Location

Create a new catalog that uses the external location as its managed storage location. When creating the catalog, under **Storage location**, select the path to the R2 bucket. For example: `r2://mybucket@my-account-id.r2.cloudflarestorage.com`. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

### 3. Replicate Tables to R2 Using Deep Clone

Use `DEEP CLONE` to replicate tables from Amazon S3 (or another source) to the new catalog that uses R2 for managed storage. Deep clones copy the source table data and metadata to the clone target, and they support incremental updates. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

To create an initial clone:

```sql
CREATE TABLE IF NOT EXISTS new_catalog.schema1.new_table
DEEP CLONE old_catalog.schema1.source_table
LOCATION 'r2://mybucket@my-account-id.r2.cloudflarestorage.com';
```

To refresh the target table incrementally with recent updates:

```sql
CREATE OR REPLACE TABLE new_catalog.schema1.new_table
DEEP CLONE old_catalog.schema1.source_table;
```

^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

Schedule a [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) workflow to run the incremental refresh on a recurring basis. See [Lakeflow Jobs](/concepts/lakeflow-jobs.md) documentation for scheduling details. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

### 4. Share the R2-Based Tables

When creating a share for OpenSharing, add the tables that reside in the new catalog stored in R2. The process is identical to adding any table to a share. See Create shares for OpenSharing for detailed instructions. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Alternatives for Reducing Egress Costs

Databricks provides multiple approaches for managing egress costs, which can be used independently or in combination with the R2 integration:

- **Replicate data using [Delta Deep Clone](/concepts/deep-clone.md)** – Providers can create local replicas of shared data in recipient regions and use incremental refresh to keep them synchronized. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]
- **Enable [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) on shared tables** – Recipients can access changes and merge them into a local copy, limiting cross-region data transfer to the change stream only. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]
- **Use [OpenSharing Egress Pipeline Notebooks](/concepts/opensharing-egress-pipeline-notebooks.md)** – Two notebooks available from Databricks Marketplace that monitor egress usage patterns and costs using [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md). ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]
- **Use [SecureConnect](/concepts/secureconnect.md)** – When using SecureConnect, Databricks bills data transfer directly rather than the cloud vendor. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol (Delta Sharing) that this integration supports.
- Egress costs – The cloud vendor charges that R2 integration helps avoid.
- External locations in Unity Catalog – The mechanism for connecting R2 buckets to Databricks.
- Storage credentials – Unity Catalog objects that grant access to cloud storage.
- [Deep Clone](/concepts/deep-clone.md) – The SQL command used to replicate tables to R2.
- [Cloudflare R2 external location setup](/concepts/external-location.md) – Detailed steps for connecting R2.

## Sources

- monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md

# Citations

1. [monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md](/references/monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws-13b884c0.md)
