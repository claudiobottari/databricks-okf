---
title: Convert to Delta Lake | Databricks on AWS
source: https://docs.databricks.com/aws/en/ingestion/data-migration/convert-to-delta
ingestedAt: "2026-06-18T08:07:50.897Z"
---

The `CONVERT TO DELTA` SQL command performs a one-time conversion for Parquet and Apache Iceberg tables to Delta Lake tables. For incremental conversion of Parquet or Iceberg tables to Delta Lake, see [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](https://docs.databricks.com/aws/en/ingestion/data-migration/clone-parquet).

Unity Catalog supports the `CONVERT TO DELTA` SQL command for Parquet and Iceberg tables stored in external locations managed by Unity Catalog.

You can configure existing Parquet data files as external tables in Unity Catalog and then convert them to Delta Lake to unlock all features of the Databricks lakehouse.

For the technical documentation, see [CONVERT TO DELTA](https://docs.databricks.com/aws/en/sql/language-manual/delta-convert-to-delta).

## Converting a directory of Parquet or Iceberg files in an external location to Delta Lake[​](#converting-a-directory-of-parquet-or-iceberg-files-in-an-external-location-to-delta-lake "Direct link to converting-a-directory-of-parquet-or-iceberg-files-in-an-external-location-to-delta-lake")

note

*   Converting Iceberg tables is supported in Databricks Runtime 10.4 LTS and above.
*   Converting Iceberg metastore tables is not supported.
*   Converting Iceberg tables that have experienced [partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution) is not supported.
*   The following are limitations for converting Iceberg tables with partitions defined on truncated columns:
    *   In Databricks Runtime 12.2 LTS and below, the only truncated column type supported is `string`.
    *   In Databricks Runtime 13.3 LTS and above, you can work with truncated columns of types `string`, `long`, or `int`.
    *   Databricks does not support working with truncated columns of type `decimal`.

You can convert a directory of Parquet data files to a Delta Lake table as long as you have write access on the storage location. For information on configuring access with Unity Catalog, see [Connect to cloud object storage using Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/).

SQL

    CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;CONVERT TO DELTA iceberg.`s3://my-bucket/iceberg-data`;

To load converted tables as external tables to Unity Catalog, you need the `CREATE EXTERNAL TABLE` permission on the external location.

note

For Databricks Runtime 11.3 LTS and above, `CONVERT TO DELTA` automatically infers partitioning information for tables registered to the Hive metastore. You must provide partitioning information for Unity Catalog external tables.

## Converting managed and external tables to Delta Lake on Unity Catalog[​](#converting-managed-and-external-tables-to-delta-lake-on-unity-catalog "Direct link to converting-managed-and-external-tables-to-delta-lake-on-unity-catalog")

`CONVERT TO DELTA` syntax can only be used for creating Unity Catalog external tables. Use a `CTAS` statement to convert a legacy Hive metastore managed Parquet table directly to a managed Unity Catalog Delta Lake table, see [Upgrade a Hive table to a Unity Catalog managed table using CREATE TABLE AS SELECT](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate#create-table-as-select).

To upgrade an external Parquet table to a Unity Catalog external table, see [Upgrade a schema or tables from the Hive metastore to Unity Catalog external tables using the upgrade wizard](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate#wizard-bulk).

After you've registered an external Parquet table to Unity Catalog, you can convert it to an external Delta Lake table. You must provide partitioning information if the Parquet table is partitioned.

SQL

    CONVERT TO DELTA catalog_name.database_name.table_name;CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
