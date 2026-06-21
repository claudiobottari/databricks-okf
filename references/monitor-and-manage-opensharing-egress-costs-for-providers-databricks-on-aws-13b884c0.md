---
title: Monitor and manage OpenSharing egress costs (for providers) | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/manage-egress
ingestedAt: "2026-06-18T08:05:25.280Z"
---

This page describes tools that you can use to monitor and manage cloud vendor egress costs when you share data and AI assets using OpenSharing.

Unlike other data sharing platforms, OpenSharing does not require data replication. This model has many advantages, but your cloud vendor might charge data egress fees when you share data across clouds or regions. If you use OpenSharing to share data and AI assets within a region, you incur no egress cost.

If you use [SecureConnect](https://docs.databricks.com/aws/en/delta-sharing/secureconnect-provider#billing), Databricks bills the data transfer rather than your cloud vendor.

To monitor and manage egress charges, Databricks provides:

*   [Notebooks that you can use to run a Lakeflow Spark Declarative Pipelines query that monitors egress usage patterns and cost](#notebooks).
*   [Instructions for replicating data between regions to avoid egress fees](#replicate).
*   [Support for Cloudflare R2 storage to avoid egress fees](#r2).

tip

Ensure your recipients use VPC gateway endpoints or [interface endpoints for S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3) instead of NAT gateways for in-region storage access whenever possible to reduce costs and enhance security.

## OpenSharing egress pipeline notebooks[​](#opensharing-egress-pipeline-notebooks "Direct link to opensharing-egress-pipeline-notebooks")

In Databricks Marketplace, the listing [OpenSharing Egress Pipeline](https://marketplace.databricks.com/details/a6f2e062-3084-4976-9eb0-47b2c8244d43/Databricks_Delta-Sharing-Egress-Pipeline) includes two notebooks that you can clone and use to monitor egress usage patterns and costs associated with OpenSharing. Both of these notebooks create and execute Lakeflow Spark Declarative Pipelines:

*   IP Ranges Mapping Pipeline notebook
*   Egress Cost Analysis Pipeline notebook

When you run these notebooks as a Lakeflow Spark Declarative Pipelines template, they will automatically generate a detailed cost report. Logs are joined with cloud provider IP range tables and OpenSharing system tables to generate egress bytes transferred, attributed by share and recipient.

Complete requirements and instructions are available in the listing.

## Replicate data to avoid egress costs[​](#replicate-data-to-avoid-egress-costs "Direct link to replicate-data-to-avoid-egress-costs")

One approach to avoiding egress costs is for the provider to create and sync local replicas of shared data in regions that their recipients are using. Another approach is for recipients to clone the shared data to local regions for active querying, setting up syncs between the shared table and the local clone. This section discusses a number of replication patterns.

### Use Delta deep clone for incremental replication[​](#use-delta-deep-clone-for-incremental-replication "Direct link to Use Delta deep clone for incremental replication")

Providers can use `DEEP CLONE` to replicate Delta tables to external locations across the regions that they share to. Deep clones copy the source table data and metadata to the clone target. Deep clones also enable incremental updates by identifying new data in the source table and refreshing the target accordingly.

SQL

    CREATE TABLE [IF NOT EXISTS] table_name DEEP CLONE source_table_name   [TBLPROPERTIES clause] [LOCATION path];

You can schedule a Databricks job to refresh target table data incrementally with recent updates in the shared table, using the following command:

SQL

    CREATE OR REPLACE TABLE table_name DEEP CLONE source_table_name;

See [Clone a table on Databricks](https://docs.databricks.com/aws/en/tables/operations/clone) and [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/).

### Enable change data feed (CDF) on shared tables for incremental replication[​](#enable-change-data-feed-cdf-on-shared-tables-for-incremental-replication "Direct link to Enable change data feed (CDF) on shared tables for incremental replication")

When a table is shared with its CDF, the recipient can access the changes and merge them into a local copy of the table, where users perform queries. In this scenario, recipient access to the data does not cross region boundaries, and egress is limited to refreshing a local copy. If the recipient is on Databricks, they can use a Databricks workflow job to propagate changes to a local replica.

To share a table with CDF, you must enable CDF on the table and share it `WITH HISTORY`.

For more information about using CDF, see [Use change data feed on Databricks](https://docs.databricks.com/aws/en/tables/features/change-data-feed) and [Add tables to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-tables).

## Use Cloudflare R2 replicas or migrate storage to R2[​](#use-cloudflare-r2-replicas-or-migrate-storage-to-r2 "Direct link to use-cloudflare-r2-replicas-or-migrate-storage-to-r2")

Cloudflare R2 object storage incurs no egress fees. Replicating or migrating data that you share to R2 enables you to share data using OpenSharing without incurring egress fees. However, this does not apply to view sharing, which might still incur egress costs. This section describes how to replicate data to an R2 location and enable incremental updates from source tables.

### Requirements[​](#requirements "Direct link to Requirements")

*   Databricks workspace enabled for Unity Catalog.
*   Databricks Runtime 14.3 or above, or SQL warehouse 2024.15 or above.
*   Cloudflare account. See [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up).
*   Cloudflare R2 Admin role. See the [Cloudflare roles documentation](https://developers.cloudflare.com/fundamentals/setup/manage-members/roles/#account-scoped-roles).
*   `CREATE STORAGE CREDENTIAL` privilege on the Unity Catalog metastore attached to the workspace. Account admins and metastore admins have this privilege by default.
*   `CREATE EXTERNAL LOCATION` privilege on both the metastore and the storage credential referenced in the external location. Metastore admins have this privilege by default.
*   `CREATE MANAGED STORAGE` privilege on the external location.
*   `CREATE CATALOG` on the metastore. Metastore admins have this privilege by default.

### Limitations for Cloudflare R2[​](#limitations-for-cloudflare-r2 "Direct link to Limitations for Cloudflare R2")

Providers can't share R2 tables that use liquid clustering and V2 checkpoint.

### Mount an R2 bucket as an external location in Databricks[​](#mount-an-r2-bucket-as-an-external-location-in-databricks "Direct link to mount-an-r2-bucket-as-an-external-location-in-databricks")

1.  Create a Cloudflare R2 bucket.
    
    See [Step 1: Configure an R2 bucket](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/external-locations-r2#bucket).
    
2.  Create a storage credential in Unity Catalog that gives access to the R2 bucket.
    
    See [Step 2: Create the storage credential](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/external-locations-r2#credential).
    
3.  Use the storage credential to create an external location in Unity Catalog.
    
    See [Step 3: Create the external location](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/external-locations-r2#location).
    

### Create a new catalog using the external location[​](#create-a-new-catalog-using-the-external-location "Direct link to Create a new catalog using the external location")

Create a catalog that uses the new external location as its managed storage location.

See [Create catalogs](https://docs.databricks.com/aws/en/catalogs/create-catalog).

When you create the catalog, do the following:

*   Catalog Explorer
*   SQL

*   Select a **Standard** catalog type.
*   Under **Storage location**, select **Select a storage location** and enter the path to the R2 bucket you defined as an external location. For example, `r2://mybucket@my-account-id.r2.cloudflarestorage.com`

Use `DEEP CLONE` to replicate tables in S3 to the new catalog that uses R2 for managed storage. Deep clones copy the source table data and metadata to the clone target. Deep clones also enable incremental updates by identifying new data in the source table and refreshing the target accordingly.

SQL

    CREATE TABLE IF NOT EXISTS new_catalog.schema1.new_table DEEP CLONE old_catalog.schema1.source_table  LOCATION 'r2://mybucket@my-account-id.r2.cloudflarestorage.com';

You can schedule a Databricks job to refresh target table data incrementally with recent updates in the source table, using the following command:

SQL

    CREATE OR REPLACE TABLE new_catalog.schema1.new_table DEEP CLONE old_catalog.schema1.source_table;

See [Clone a table on Databricks](https://docs.databricks.com/aws/en/tables/operations/clone) and [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/).

When you create the share, add the tables that are in the new catalog, stored in R2. The process is the same as adding any table to a share.

See [Create shares for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/create-share).
