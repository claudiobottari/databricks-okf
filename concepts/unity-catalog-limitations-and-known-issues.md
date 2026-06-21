---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c9a5faa0640662cdaad611c3c4cce2335714954118884d936b126504ac17260
  pageDirectory: concepts
  sources:
    - unity-catalog-requirements-and-limitations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-limitations-and-known-issues
    - Known Issues and Unity Catalog Limitations
    - UCLAKI
  citations:
    - file: unity-catalog-requirements-and-limitations-databricks-on-aws.md
title: Unity Catalog Limitations and Known Issues
description: Unity Catalog has various limitations including restrictions on workspace-level groups in GRANT statements, bucketing, R workload dynamic views, Python/Scala UDF support by runtime version, cloning constraints, and cross-region write reliability.
tags:
  - unity-catalog
  - limitations
  - compatibility
timestamp: "2026-06-19T23:16:53.327Z"
---

Here is the wiki page for "[Unity Catalog](/concepts/unity-catalog.md) Limitations and Known Issues".

---

## [Unity Catalog](/concepts/unity-catalog.md) Limitations and Known Issues

**Unity Catalog** is Databricks’ unified data governance solution. While it provides comprehensive metadata, access control, and auditing capabilities, it has several limitations and known issues that affect compute, file formats, naming, and certain workloads. Databricks regularly releases new functionality to shrink this list. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

### Compute Requirements

[Unity Catalog](/concepts/unity-catalog.md) is supported on clusters running Databricks Runtime 11.3 LTS or above. It is also supported by default on all SQL Warehouse compute versions. Clusters running on earlier versions of Databricks Runtime do not provide support for all [Unity Catalog](/concepts/unity-catalog.md) GA features and functionality. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

To access data in [Unity Catalog](/concepts/unity-catalog.md), clusters must be configured with a standard or dedicated access mode. [Unity Catalog](/concepts/unity-catalog.md) is secure by default; if a cluster is not configured with the correct access mode, it cannot access data in [Unity Catalog](/concepts/unity-catalog.md). ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

### File Format Support

[Unity Catalog](/concepts/unity-catalog.md) supports the following table formats:

- **Managed tables** must use the `delta` or `iceberg` table format.
- **External tables** can use `delta`, `CSV`, `JSON`, `avro`, `parquet`, `ORC`, or `text`.

^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

Incorrect format choices can lead to errors or unsupported operations. For example, using overwrite mode for tables not in Delta format requires the user to have the `CREATE TABLE` privilege on the parent schema and to be the owner of the existing object or have the `MODIFY` privilege. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

### Securable Object Naming Constraints

All object names in [Unity Catalog](/concepts/unity-catalog.md) are subject to the following constraints:

- Names cannot exceed 255 characters.
- The following special characters are **not allowed**: period (`.`), space ( ), forward slash (`/`), all ASCII control characters (00-1F hex), and the DELETE character (7F hex).
- [Unity Catalog](/concepts/unity-catalog.md) stores all object names as lowercase.
- When referencing [Unity Catalog](/concepts/unity-catalog.md) names in SQL, use backticks to escape names that contain special characters such as hyphens (`-`).

Column names can use special characters but must be escaped with backticks in all SQL statements. [Unity Catalog](/concepts/unity-catalog.md) preserves column name casing, but queries are case-insensitive. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

### General Limitations

#### Groups and Grants

Workspace-level groups cannot be used in [Unity Catalog](/concepts/unity-catalog.md) `GRANT` statements. To ensure a consistent view of groups that can span across workspaces, create groups at the account level and update any automation for principal or group management to reference account endpoints instead of workspace endpoints. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

#### Dynamic Views on R

Workloads in R do not support dynamic views for row-level or column-level security on compute running Databricks Runtime 15.3 and below. Use a dedicated compute resource running Databricks Runtime 15.4 LTS or above, and a workspace enabled for [serverless compute](/concepts/serverless-gpu-compute.md), for such workloads. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

#### Cloning and Bucketing

- A **managed table** can be shallow cloned to another managed table (Databricks Runtime 13.3 LTS+), but **not** to an external table. An external table can be shallow cloned to another external table (Databricks Runtime 14.2+), but **not** to a managed table.
- **Bucketing** is not supported for [Unity Catalog](/concepts/unity-catalog.md) tables; commands that attempt to create a bucketed table throw an exception.

^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

#### Partition Management

Manipulating partitions for external tables using `ALTER TABLE ADD PARTITION` requires partition metadata logging to be enabled. See External Partition Discovery. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

#### Multi-Region Writes

Writing to the same path or [Delta Lake Table](/concepts/delta-lake-table.md) from workspaces in multiple regions can lead to unreliable performance if some clusters access [Unity Catalog](/concepts/unity-catalog.md) and others do not. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

#### UDF and Thread Pool Support

- **Python UDFs** (including UDAFs, UDTFs, and Pandas on Spark) are not supported in Databricks Runtime 12.2 LTS and below. They are supported in [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) and above.
- **Scala UDFs** are not supported in Databricks Runtime 14.1 and below on compute with [Standard Access Mode](/concepts/standard-access-mode.md). They are supported in Databricks Runtime 14.2 and above.
- **Standard Scala thread pools** are not supported. Use `org.apache.spark.util.ThreadUtils.newDaemonFixedThreadPool` instead. `ThreadUtils.newForkJoinPool` and any `ScheduledExecutorService` thread pool are also not supported.

^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

#### Structured Streaming

[Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) workloads have additional limitations depending on Databricks Runtime and access mode. See the dedicated compute limitations pages for details. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

#### Models

Models registered in [Unity Catalog](/concepts/unity-catalog.md) have additional limitations. See the model lifecycle documentation for details. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

### Resource Quotas

[Unity Catalog](/concepts/unity-catalog.md) enforces resource quotas on all securable objects. If you expect to exceed these limits, contact your Databricks account team. You can monitor your quota usage using the Unity Catalog Resource Quotas APIs. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

### Sources

- unity-catalog-requirements-and-limitations-databricks-on-aws.md

# Citations

1. [unity-catalog-requirements-and-limitations-databricks-on-aws.md](/references/unity-catalog-requirements-and-limitations-databricks-on-aws-0188dbe0.md)
