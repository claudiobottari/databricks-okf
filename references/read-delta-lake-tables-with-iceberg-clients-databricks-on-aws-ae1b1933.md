---
title: Read Delta Lake tables with Iceberg clients | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta/uniform
ingestedAt: "2026-06-18T08:05:10.527Z"
---

This article provides details for enabling Iceberg reads on tables stored with Delta Lake in Databricks. This feature requires Databricks Runtime 14.3 LTS or above.

note

This functionality was previously called Delta Lake Universal Format (UniForm).

You can configure an external connection to have Unity Catalog act as an Iceberg catalog. See [Access Databricks tables from Apache Iceberg clients](https://docs.databricks.com/aws/en/external-access/iceberg).

## How do Apache Iceberg reads (UniForm) work?[​](#how-do-apache-iceberg-reads-uniform-work "Direct link to how-do-apache-iceberg-reads-uniform-work")

Both Delta Lake and Apache Iceberg consist of Parquet data files and a metadata layer. Enabling Iceberg reads configures your tables to automatically generate Iceberg metadata asynchronously, without rewriting data, so that Iceberg clients can read Delta Lake tables written by Databricks. A single copy of the data files serves multiple formats.

important

*   Tables with Iceberg reads enabled use Zstandard instead of Snappy as the compression codec for underlying Parquet data files.
*   Iceberg metadata generation runs asynchronously on the compute used to write data to Delta Lake tables, which might increase the driver resource usage.
*   For documentation for the legacy UniForm `IcebergCompatV1` table feature, see [Legacy UniForm IcebergCompatV1](https://docs.databricks.com/aws/en/archive/legacy/uniform).

## Requirements[​](#requirements "Direct link to Requirements")

To enable Iceberg reads, the following requirements must be met:

*   The Delta Lake table must be registered to Unity Catalog. Both managed and external tables are supported.
*   The table must have column mapping enabled. See [Rename and drop columns with Delta Lake column mapping](https://docs.databricks.com/aws/en/tables/features/column-mapping).
*   The Delta Lake table must have a `minReaderVersion` >= 2 and `minWriterVersion` >= 7. See [Delta Lake feature compatibility and protocols](https://docs.databricks.com/aws/en/tables/features/feature-compatibility).
*   Writes to the table must use Databricks Runtime 14.3 LTS or above.

note

You cannot enable deletion vectors on a table with Iceberg reads enabled.

Use `REORG` to disable and purge deletion vectors while enabling Iceberg reads on an existing table with deletion vectors enabled. See [Enable or upgrade Iceberg read support using `REORG`](#reorg).

## Enable Iceberg reads (UniForm)[​](#enable-iceberg-reads-uniform "Direct link to Enable Iceberg reads (UniForm)")

important

When you enable Iceberg reads, the write protocol feature `IcebergCompatV2` is added to the table. Only clients that support this table feature can write to tables with Iceberg reads enabled. On Databricks, you must use Databricks Runtime 14.3 LTS or above to write to enabled tables.

`IcebergCompatV2` depends on column mapping. Once `IcebergCompatV2` is enabled for a table, you cannot drop the `columnMapping` table feature.

You can turn off Iceberg reads by unsetting the `delta.universalFormat.enabledFormats` table property. Upgrades to Delta Lake reader and writer protocol versions cannot be undone.

You must set the following table properties to enable Iceberg reads:

    'delta.enableIcebergCompatV2' = 'true''delta.universalFormat.enabledFormats' = 'iceberg'

When you first enable Iceberg reads, asynchronous metadata generation begins. This task must complete before external clients can query the table using Iceberg. See [Check Iceberg metadata generation status](#status).

For a list of limitations, see [Limitations](#limitations).

### Enable Iceberg reads during table creation[​](#enable-iceberg-reads-during-table-creation "Direct link to Enable Iceberg reads during table creation")

[Column mapping](https://docs.databricks.com/aws/en/tables/features/column-mapping) must be enabled to use Iceberg reads and cannot be dropped once enabled. This happens automatically if you enable Iceberg reads during table creation, as in the following example:

SQL

    CREATE TABLE T(c1 INT) TBLPROPERTIES(  'delta.columnMapping.mode' = 'id',  'delta.enableIcebergCompatV2' = 'true',  'delta.universalFormat.enabledFormats' = 'iceberg');

### Enable Iceberg reads on an existing table[​](#enable-iceberg-reads-on-an-existing-table "Direct link to enable-iceberg-reads-on-an-existing-table")

In Databricks Runtime 15.4 LTS and above, you can enable or upgrade Iceberg reads on an existing table using the following syntax:

SQL

    ALTER TABLE table_name SET TBLPROPERTIES(  'delta.columnMapping.mode' = 'name',  'delta.enableIcebergCompatV2' = 'true',  'delta.universalFormat.enabledFormats' = 'iceberg');

For details on limitations with `name` column mapping mode, see [Column mapping modes](https://docs.databricks.com/aws/en/tables/features/column-mapping#modes).

### Enable or upgrade Iceberg read support using `REORG`[​](#enable-or-upgrade-iceberg-read-support-using-reorg "Direct link to enable-or-upgrade-iceberg-read-support-using-reorg")

You can use `REORG` to enable Iceberg reads and rewrite underlying data files, as in the following example:

SQL

    REORG TABLE table_name APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2));

Use `REORG` if any of the following are true:

*   Your table has deletion vectors enabled.
*   You previously enabled the `IcebergCompatV1` version of UniForm Iceberg.
*   You need to read from Iceberg engines that don't support Hive-style Parquet files, such as Athena or Redshift.

### Verify that Iceberg reads (UniForm) are enabled[​](#verify-that-iceberg-reads-uniform-are-enabled "Direct link to verify-that-iceberg-reads-uniform-are-enabled")

Use `DESCRIBE EXTENDED` to verify that Iceberg reads (UniForm) is enabled for your table:

SQL

    DESCRIBE EXTENDED catalog_name.schema_name.table_name;

Look for the **Delta Uniform Iceberg** section in the output. If this section is present, Iceberg reads are enabled on your table.

Alternatively, you can use `SHOW TBLPROPERTIES`:

SQL

    SHOW TBLPROPERTIES catalog_name.schema_name.table_name;

Check for the following properties:

*   `delta.enableIcebergCompatV2 = true`
*   `delta.universalFormat.enabledFormats = iceberg`

If both properties are present with these values, Iceberg reads are enabled.

Databricks triggers metadata generation asynchronously after a Delta Lake write transaction completes. This metadata generation process uses the same compute that completed the Delta Lake transaction.

note

You can also manually trigger Iceberg metadata generation. See [Manually trigger Iceberg metadata conversion](#manual-trigger).

To avoid write latencies associated with metadata generation, Delta Lake tables with frequent commits might group multiple Delta Lake commits into a single commit to Iceberg metadata.

Delta Lake ensures that only one metadata generation process is in progress on a given compute resource. Commits that would trigger a second concurrent metadata generation process successfully commit to Delta Lake but don't trigger asynchronous Iceberg metadata generation. This prevents cascading latency for metadata generation for workloads with frequent commits (seconds to minutes between commits).

See [Delta and Iceberg table versions](#versions).

## Delta and Iceberg table versions[​](#delta-and-iceberg-table-versions "Direct link to delta-and-iceberg-table-versions")

Delta Lake and Iceberg allow time travel queries using table versions or timestamps stored in table metadata.

In general, Delta Lake table versions do not align with Iceberg versions by either the commit timestamp or the version ID. To verify which version of a Delta Lake table a given version of an Iceberg table corresponds to, you can use the corresponding table properties. See [Check Iceberg metadata generation status](#status).

Enabling Iceberg reads on a table adds the following fields to Unity Catalog and Iceberg table metadata to track metadata generation status:

On Databricks, you can review these metadata fields by doing one of the following:

*   Reviewing the `Delta Uniform Iceberg` section returned by `DESCRIBE EXTENDED table_name`.
*   Reviewing table metadata with Catalog Explorer.

See the documentation for your Iceberg reader client for how to review table properties outside Databricks. For OSS Apache Spark, you can see these properties using the following syntax:

SQL

    SHOW TBLPROPERTIES <table-name>;

You can manually trigger Iceberg metadata generation for the latest version of the Delta Lake table. This operation runs synchronously, meaning that when it completes, the table contents available in Iceberg reflect the latest version of the Delta Lake table available when the conversion process started.

This operation should not be necessary under normal conditions, but can help if you encounter the following:

*   A cluster terminates before automatic metadata generation succeeds.
*   An error or job failure interrupts metadata generation.
*   A client that does not support UniForm Iceberg metadata generation writes to the Delta Lake table.

Use the following syntax to trigger Iceberg metadata generation manually:

SQL

    MSCK REPAIR TABLE <table-name> SYNC METADATA

See [REPAIR TABLE](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-repair-table).

Some Iceberg clients require that you provide a path to versioned metadata files to register external Iceberg tables. Each time Databricks converts a new version of the Delta Lake table to Iceberg, it creates a new metadata JSON file.

Clients that use metadata JSON paths for configuring Iceberg include BigQuery. Refer to documentation for the Iceberg reader client for configuration details.

Delta Lake stores Iceberg metadata under the table directory using the following pattern:

    <table-path>/metadata/<version-number>-<uuid>.metadata.json

On Databricks, you can review this metadata location by doing one of the following:

*   Reviewing the `Delta Uniform Iceberg` section returned by `DESCRIBE EXTENDED table_name`.
*   Reviewing table metadata with Catalog Explorer.

important

Path-based Iceberg reader clients might require manually updating and refreshing metadata JSON paths to read current table versions. Users might encounter errors when querying Iceberg tables using out-of-date versions as Parquet data files are removed from the Delta Lake table with `VACUUM`.

## Limitations[​](#limitations "Direct link to Limitations")

The following limitations exist for all tables with Iceberg reads enabled:

*   Iceberg v2 reads don't work on tables with deletion vectors enabled. However, Apache Iceberg v3 supports deletion vectors. See [Use Apache Iceberg v3 features](https://docs.databricks.com/aws/en/iceberg/iceberg-v3) and [Deletion vectors in Databricks](https://docs.databricks.com/aws/en/tables/features/deletion-vectors).
*   The delta table must be accessed by name (not path) to automatically trigger iceberg metadata generation.
*   Iceberg reads cannot be enabled on materialized views or streaming tables.
*   Delta Lake tables with Iceberg reads enabled do not support `VOID` types.
*   Iceberg client support is read-only. Writes are not supported.
*   Iceberg reader clients might have individual limitations, regardless of Databricks support for Iceberg reads. See the documentation for your chosen client.
*   The recipients of OpenSharing can read Delta Lake tables with Iceberg reads enabled as Iceberg tables using the Iceberg REST Catalog API. This feature is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). See [Enable sharing to external Iceberg clients](https://docs.databricks.com/aws/en/delta-sharing/create-share#iceberg-clients).
*   Some Delta Lake table features used by Iceberg reads are not supported by some OpenSharing reader clients. See [What is OpenSharing?](https://docs.databricks.com/aws/en/delta-sharing/).

Change Data Feed works for Delta clients when Iceberg reads are enabled but does not have support in Iceberg.
