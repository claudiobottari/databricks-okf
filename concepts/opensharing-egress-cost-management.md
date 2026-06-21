---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 484ee974d33f00b3cc2cf35b8a514855bfa778308ac9592506e2fe3069b17074
  pageDirectory: concepts
  sources:
    - monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-egress-cost-management
    - OECM
  citations:
    - file: monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
title: OpenSharing Egress Cost Management
description: Strategies and tools provided by Databricks to monitor, manage, and minimize cloud vendor data egress fees when sharing data across regions using OpenSharing.
tags:
  - delta-sharing
  - cost-management
  - cloud-infrastructure
timestamp: "2026-06-19T19:45:36.698Z"
---

# OpenSharing Egress Cost Management

**OpenSharing Egress Cost Management** refers to the tools and strategies that data and AI asset providers can use to monitor, reduce, or eliminate cloud vendor data egress fees incurred when sharing data across clouds or regions using [OpenSharing](/concepts/opensharing.md) (the Databricks implementation of [Delta Sharing](/concepts/delta-sharing.md)). Unlike other data sharing platforms, OpenSharing does not require data replication, which can lead to egress charges when recipients are in a different cloud or region than the provider’s storage. Sharing within the same region incurs no egress cost.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

When providers use [SecureConnect](/concepts/secureconnect.md), Databricks bills the data transfer directly rather than the cloud vendor, providing an alternative billing model for managed egress.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Monitoring Egress with Notebooks

Databricks provides two Lakeflow Spark Declarative Pipeline notebooks, available in the [OpenSharing Egress Pipeline](https://marketplace.databricks.com/details/a6f2e062-3084-4976-9eb0-47b2c8244d43/Databricks_Delta-Sharing-Egress-Pipeline) listing on Databricks Marketplace, to monitor egress usage patterns and costs:^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

- **IP Ranges Mapping Pipeline notebook** – Joins logs with cloud provider IP range tables.
- **Egress Cost Analysis Pipeline notebook** – Generates a detailed cost report showing egress bytes transferred, attributed by share and recipient.

Both notebooks create and execute a Lakeflow Spark Declarative Pipeline that joins logs with cloud provider IP range tables and OpenSharing system tables. When run, they automatically produce the cost report.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

To reduce costs regardless of monitoring, Databricks recommends that recipients use VPC gateway endpoints or VPC Interface Endpoints for S3 instead of NAT gateways for in-region storage access.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Replicating Data to Avoid Egress Costs

Providers can avoid egress fees by creating and syncing local replicas of shared data in the regions where their recipients are located. Alternatively, recipients can clone the shared data to their local region and set up synchronization between the shared table and the local clone. Two primary replication patterns are described below.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

### Use Delta Deep Clone for Incremental Replication

Providers can use `DEEP CLONE` to replicate Delta tables to external locations in other regions. The deep clone copies the source table’s data and metadata to the target. Incremental updates are supported: a scheduled Databricks job can identify new data in the source table and refresh the target accordingly using `CREATE OR REPLACE TABLE ... DEEP CLONE ...`.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

```sql
CREATE TABLE [IF NOT EXISTS] table_name DEEP CLONE source_table_name
  [TBLPROPERTIES clause] [LOCATION path];

-- Refresh incrementally:
CREATE OR REPLACE TABLE table_name DEEP CLONE source_table_name;
```

### Enable Change Data Feed (CDF) on Shared Tables for Incremental Replication

When a table is shared with its [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) enabled, the recipient can access changes and merge them into a local copy, keeping queries local and limiting egress to refreshing the local copy. If the recipient uses Databricks, they can schedule a [Lakeflow Jobs](/concepts/lakeflow-jobs.md) workflow to propagate changes. To share a table with CDF, the provider must enable CDF on the table and share it `WITH HISTORY`.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Using Cloudflare R2 Storage

Cloudflare R2 object storage has no egress fees. By replicating or migrating shared data to an R2 bucket, providers can share via OpenSharing without incurring egress costs. This approach does not apply to view sharing, which may still incur egress fees.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

### Requirements

- Databricks workspace enabled for [Unity Catalog](/concepts/unity-catalog.md).
- Databricks Runtime 14.3 or later, or SQL Warehouse 2024.15 or later.
- Cloudflare account with R2 Admin role.
- `CREATE STORAGE CREDENTIAL` privilege on the [Metastore](/concepts/metastore.md).
- `CREATE EXTERNAL LOCATION` privilege on the [Metastore](/concepts/metastore.md) and storage credential.
- `CREATE MANAGED STORAGE` privilege on the external location.
- `CREATE CATALOG` privilege on the [Metastore](/concepts/metastore.md).^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

### Limitation

Providers cannot share R2 tables that use liquid clustering and V2 checkpoint.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

### Steps to Set Up R2 for OpenSharing

1. **Create a Cloudflare R2 bucket** and configure it as an external location in Unity Catalog by creating a storage credential and then an external location pointing to the R2 bucket.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]
2. **Create a new catalog** that uses the R2 external location as its managed storage location. The storage location path follows the pattern `r2://mybucket@my-account-id.r2.cloudflarestorage.com`.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]
3. **Use `DEEP CLONE`** to replicate existing S3 tables into the new R2‑backed catalog. A scheduled Databricks job can incrementally refresh the R2 table copies.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]
4. **Create a share** and add the tables that are stored in the R2 catalog, following the standard process for Creating shares for OpenSharing.^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol underlying OpenSharing.
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) – Used by the egress monitoring notebooks.
- [SecureConnect](/concepts/secureconnect.md) – Managed egress billing option from Databricks.
- [Unity Catalog](/concepts/unity-catalog.md) – Required for R2 integration.
- [External location](/concepts/external-location.md) – Unity Catalog object pointing to cloud storage.
- [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) – Credentials used to authenticate to cloud storage.
- [Deep Clone](/concepts/deep-clone.md) – Replication method for Delta tables.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Enables incremental replication for recipients.

## Sources

- monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md

# Citations

1. [monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md](/references/monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws-13b884c0.md)
