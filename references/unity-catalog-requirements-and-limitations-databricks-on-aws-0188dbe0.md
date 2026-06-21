---
title: Unity Catalog requirements and limitations | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/requirements
ingestedAt: "2026-06-18T08:04:50.191Z"
---

This page describes the compute requirements, supported file formats, naming constraints, and known limitations for Unity Catalog.

## Region support[​](#-region-support "Direct link to -region-support")

All regions support Unity Catalog. For details, see [Databricks clouds and regions](https://docs.databricks.com/aws/en/resources/supported-regions).

## Compute requirements[​](#-compute-requirements "Direct link to -compute-requirements")

Unity Catalog is supported on clusters that run Databricks Runtime 11.3 LTS or above. Unity Catalog is supported by default on all [SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/) compute versions.

Clusters running on earlier versions of Databricks Runtime do not provide support for all Unity Catalog GA features and functionality.

To access data in Unity Catalog, clusters must be configured with the correct _access mode_. Unity Catalog is secure by default. If a cluster is not configured with standard or dedicated access mode, the cluster can't access data in Unity Catalog. See [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-mode).

For detailed information about Unity Catalog functionality changes in each Databricks Runtime version, see the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/).

## File format support[​](#-file-format-support "Direct link to -file-format-support")

Unity Catalog supports the following table formats:

*   [Managed tables](https://docs.databricks.com/aws/en/tables/managed) must use the `delta` or `iceberg` table format.
*   [External tables](https://docs.databricks.com/aws/en/tables/external) can use `delta`, `CSV`, `JSON`, `avro`, `parquet`, `ORC`, or `text`.

## Securable object naming requirements[​](#-securable-object-naming-requirements "Direct link to -securable-object-naming-requirements")

The following limitations apply for all object names in Unity Catalog:

*   Object names cannot exceed 255 characters.
*   The following special characters are not allowed:
    *   Period (`.`)
    *   Space ( )
    *   Forward slash (`/`)
    *   All ASCII control characters (00-1F hex)
    *   The DELETE character (7F hex)
*   Unity Catalog stores all object names as lowercase.
*   When referencing UC names in SQL, you must use backticks to escape names that contain special characters such as hyphens (`-`).

note

Column names can use special characters, but the name must be escaped with backticks in all SQL statements if special characters are used. Unity Catalog preserves column name casing, but queries against Unity Catalog tables are case-insensitive.

## Limitations[​](#-limitations "Direct link to -limitations")

Unity Catalog has the following limitations. Some of these are specific to older Databricks Runtime versions and compute access modes.

Structured Streaming workloads have additional limitations, depending on Databricks Runtime and access mode. See [Standard compute requirements and limitations](https://docs.databricks.com/aws/en/compute/standard-limitations) and [Dedicated compute requirements and limitations](https://docs.databricks.com/aws/en/compute/dedicated-limitations).

Databricks releases new functionality that shrinks this list regularly.

*   Groups that were previously created in a workspace (that is, workspace-level groups) cannot be used in Unity Catalog `GRANT` statements. This is to ensure a consistent view of groups that can span across workspaces. To use groups in `GRANT` statements, create your groups at the account level and update any automation for principal or group management (such as SCIM, Okta and Microsoft Entra ID connectors, and Terraform) to reference account endpoints instead of workspace endpoints. See [Group sources](https://docs.databricks.com/aws/en/admin/users-groups/groups#sources).
*   Workloads in R do not support the use of dynamic views for row-level or column-level security on compute running Databricks Runtime 15.3 and below.
    *   Use a dedicated compute resource running Databricks Runtime 15.4 LTS or above for workloads in R that query dynamic views. Such workloads also require a workspace that is enabled for serverless compute. For details, see [Fine-grained access control on dedicated compute](https://docs.databricks.com/aws/en/compute/single-user-fgac).
*   A managed table can be shallow cloned to another managed table on Databricks Runtime 13.3 LTS and above. An external table can be shallow cloned to another external table on Databricks Runtime 14.2 and above. A managed table cannot be shallow cloned to an external table. Also, an external table cannot be shallow cloned to a managed table. For more information, see [Shallow clone for Unity Catalog tables](https://docs.databricks.com/aws/en/tables/operations/clone-unity-catalog).
*   Bucketing is not supported for Unity Catalog tables. If you run commands that try to create a bucketed table in Unity Catalog, it will throw an exception.
*   Writing to the same path or Delta Lake table from workspaces in multiple regions can lead to unreliable performance if some clusters access Unity Catalog and others do not.
*   Manipulating partitions for external tables using commands like `ALTER TABLE ADD PARTITION` requires partition metadata logging to be enabled. See [Partition discovery for external tables](https://docs.databricks.com/aws/en/tables/external-partition-discovery).
*   When using overwrite mode for tables not in Delta format, the user must have the CREATE TABLE privilege on the parent schema and must be the owner of the existing object OR have the MODIFY privilege on the object.
*   Python UDFs are not supported in Databricks Runtime 12.2 LTS and below. This includes UDAFs, UDTFs, and Pandas on Spark (`applyInPandas` and `mapInPandas`). Python scalar UDFs are supported in Databricks Runtime 13.3 LTS and above.
*   Scala UDFs are not supported in Databricks Runtime 14.1 and below on compute with standard access mode. Scalar UDFs are supported in Databricks Runtime 14.2 and above on compute with standard access mode.
*   Standard Scala thread pools are not supported. Instead, use the special thread pools in `org.apache.spark.util.ThreadUtils`, for example, `org.apache.spark.util.ThreadUtils.newDaemonFixedThreadPool`. However, the following thread pools in `ThreadUtils` are not supported: `ThreadUtils.newForkJoinPool` and any `ScheduledExecutorService` thread pool.

Models registered in Unity Catalog have additional limitations. See [Limitations](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#limitations).

## Resource quotas[​](#-resource-quotas "Direct link to -resource-quotas")

Unity Catalog enforces resource quotas on all securable objects. These quotas are listed in [Resource limits](https://docs.databricks.com/aws/en/resources/limits). If you expect to exceed these resource limits, contact your Databricks account team.

You can monitor your quota usage using the Unity Catalog resource quotas APIs. See [Monitor your usage of Unity Catalog resource quotas](https://docs.databricks.com/aws/en/resources/manage-resource-quotas).
