---
title: What is Delta Lake in Databricks? | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta/
ingestedAt: "2026-06-18T08:05:00.890Z"
---

Delta Lake is the optimized storage layer that provides the foundation for tables in a lakehouse on Databricks. Delta Lake is [open source software](https://delta.io/) that extends Parquet data files with a file-based transaction log for [ACID transactions](https://docs.databricks.com/aws/en/lakehouse/acid) and scalable metadata handling. Delta Lake is fully compatible with Apache Spark APIs, and was developed for tight integration with Structured Streaming, allowing you to easily use a single copy of data for both batch and streaming operations and providing incremental processing at scale.

Delta Lake is the default format for all operations on Databricks. Unless otherwise specified, all tables on Databricks are Delta Lake tables. Databricks originally developed the Delta Lake protocol and continues to actively contribute to the open source project. Many of the optimizations and products in the Databricks platform build upon the guarantees provided by Apache Spark and Delta Lake. For information on optimizations on Databricks, see [Optimization recommendations on Databricks](https://docs.databricks.com/aws/en/optimizations/).

For reference information on Delta Lake SQL commands, see [Delta Lake statements](https://docs.databricks.com/aws/en/sql/language-manual/#delta-lake-statements).

The Delta Lake transaction log has a well-defined open protocol that can be used by any system to read the log. See [Delta Transaction Log Protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md).

## Getting started with Delta Lake[​](#getting-started-with-delta-lake "Direct link to getting-started-with-delta-lake")

All tables on Databricks are Delta Lake tables by default. Whether you're using Apache Spark [DataFrames](https://docs.databricks.com/aws/en/getting-started/dataframes) or SQL, you get all the benefits of Delta Lake just by saving your data to the lakehouse with default settings.

For examples of basic Delta Lake operations such as creating tables, reading, writing, and updating data, see [Tutorial: Create and manage Delta Lake tables](https://docs.databricks.com/aws/en/delta/tutorial).

For Databricks recommendations and best practices on using Delta Lake, see [Best practices: Delta Lake](https://docs.databricks.com/aws/en/delta/best-practices).

## Converting and ingesting data to Delta Lake[​](#converting-and-ingesting-data-to-delta-lake "Direct link to converting-and-ingesting-data-to-delta-lake")

Databricks has many features to accelerate and simplify loading data to your lakehouse.

*   *   [Tutorial: Build an ETL pipeline with Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/getting-started/data-pipeline-get-started)
    *   Build an end-to-end ETL pipeline using Lakeflow Spark Declarative Pipelines.
*   *   [Set up incremental ingestion from Amazon S3](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/onboard-data)
    *   Set up incremental ingestion from cloud storage using Auto Loader and Lakeflow Spark Declarative Pipelines.
*   *   [Streaming tables](https://docs.databricks.com/aws/en/ldp/concepts/streaming-tables)
    *   Use streaming tables for append-only ingestion and low-latency streaming in Lakeflow Spark Declarative Pipelines.
*   *   [Get started using COPY INTO to load data](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/copy-into/)
    *   Load data incrementally and idempotently from cloud storage using SQL.
*   *   [What is Auto Loader?](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/)
    *   Ingest files from cloud storage incrementally as they arrive.
*   *   [Create or modify a table using file upload](https://docs.databricks.com/aws/en/ingestion/create-or-modify-table)
    *   Upload files and create tables from the Databricks UI.
*   *   [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](https://docs.databricks.com/aws/en/ingestion/data-migration/clone-parquet)
    *   Incrementally clone Parquet or Apache Iceberg tables to Delta Lake.
*   *   [Convert to Delta Lake](https://docs.databricks.com/aws/en/ingestion/data-migration/convert-to-delta)
    *   One-time conversion of Parquet or Apache Iceberg tables to Delta Lake.
*   *   [Technology partners](https://docs.databricks.com/aws/en/integrations/)
    *   Connect third-party partners and tools to your Databricks lakehouse.

For a full list of ingestion options, see [Standard connectors in Lakeflow Connect](https://docs.databricks.com/aws/en/ingestion/).

## Updating and modifying Delta Lake tables[​](#updating-and-modifying-delta-lake-tables "Direct link to updating-and-modifying-delta-lake-tables")

Atomic transactions with Delta Lake allow you to use many options for updating data and metadata. To avoid corrupting your tables, Databricks recommends that you avoid interacting directly with data and transaction log files in Delta Lake file directories.

*   *   [Upsert into a Delta Lake table using merge](https://docs.databricks.com/aws/en/delta/merge)
    *   Upsert data into a Delta Lake table using the merge operation.
*   *   [Selectively overwrite data with Delta Lake](https://docs.databricks.com/aws/en/delta/selective-overwrite)
    *   Overwrite subsets of data based on filters and partitions.
*   *   [Update table schema](https://docs.databricks.com/aws/en/tables/update-schema)
    *   Manually or automatically update your table schema without rewriting data.
*   *   [Rename and drop columns with Delta Lake column mapping](https://docs.databricks.com/aws/en/tables/features/column-mapping)
    *   Rename or delete columns without rewriting data.

## Incremental and streaming workloads on Delta Lake[​](#incremental-and-streaming-workloads-on-delta-lake "Direct link to incremental-and-streaming-workloads-on-delta-lake")

Delta Lake is optimized for Structured Streaming on Databricks. [Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/) extends built-in capabilities with simplified infrastructure deployment, enhanced scaling, and managed data dependencies.

*   *   [Delta Lake table streaming reads and writes](https://docs.databricks.com/aws/en/structured-streaming/delta-lake)
    *   Use Delta Lake tables as sources and sinks for Structured Streaming with `readStream` and `writeStream`.
*   *   [Use change data feed on Databricks](https://docs.databricks.com/aws/en/tables/features/change-data-feed)
    *   Track row-level changes between versions of a Delta Lake or Apache Iceberg v3 table.

## Querying previous versions of a table[​](#querying-previous-versions-of-a-table "Direct link to Querying previous versions of a table")

Each write to a Delta Lake table creates a new table version. You can use the transaction log to review modifications to your table and query previous table versions. See [Work with table history](https://docs.databricks.com/aws/en/tables/history).

## Delta Lake schema enhancements[​](#delta-lake-schema-enhancements "Direct link to delta-lake-schema-enhancements")

Delta Lake validates schema on write, ensuring that all data written to a table matches the requirements you've set.

*   *   [Schema enforcement](https://docs.databricks.com/aws/en/tables/schema-enforcement)
    *   Validate data quality by enforcing schema on write.
*   *   [Constraints on Databricks](https://docs.databricks.com/aws/en/tables/constraints)
    *   Apply enforced integrity constraints and informational primary key, foreign key, and unique constraints.
*   *   [Delta Lake generated columns](https://docs.databricks.com/aws/en/tables/features/generated-columns)
    *   Automatically generate column values using user-specified functions.
*   *   [Enrich tables with custom metadata](https://docs.databricks.com/aws/en/tables/operations/custom-metadata)
    *   Add comments and custom metadata to tables and columns to enrich data discovery.

## Managing files and indexing data with Delta Lake[​](#managing-files-and-indexing-data-with-delta-lake "Direct link to managing-files-and-indexing-data-with-delta-lake")

Databricks sets many default parameters for Delta Lake that impact the size of data files and number of table versions that are retained in history. Delta Lake uses a combination of metadata parsing and physical data layout to reduce the number of files scanned to fulfill any query.

*   *   [Use liquid clustering for tables](https://docs.databricks.com/aws/en/tables/clustering)
    *   Simplify data layout and optimize query performance without partitioning using liquid clustering.
*   *   [Data skipping](https://docs.databricks.com/aws/en/tables/data-skipping)
    *   Skip irrelevant files at query time using column statistics, Z-order, and optimized data layout.
*   *   [Optimize data file layout](https://docs.databricks.com/aws/en/tables/operations/optimize)
    *   Compact small data files to improve query performance.
*   *   [Remove unused data files with vacuum](https://docs.databricks.com/aws/en/tables/operations/vacuum)
    *   Remove stale data files to reduce storage costs.
*   *   [Automatic row deletion with auto time-to-live](https://docs.databricks.com/aws/en/tables/operations/auto-ttl)
    *   Automatically delete rows from managed tables after a configurable time period.
*   *   [Control data file size](https://docs.databricks.com/aws/en/tables/tune-file-size)
    *   Control target file size manually or enable automatic file size tuning.

## Configuring and reviewing Delta Lake settings[​](#configuring-and-reviewing-delta-lake-settings "Direct link to configuring-and-reviewing-delta-lake-settings")

Databricks stores all data and metadata for Delta Lake tables in cloud object storage. Many configurations can be set at either the table level or within the Spark session. You can review the details of the Delta Lake table to discover what options are configured.

*   *   [Review table details with describe detail](https://docs.databricks.com/aws/en/tables/operations/table-details)
    *   View table configurations and metadata using the `DESCRIBE DETAIL` command.
*   *   [Table properties reference](https://docs.databricks.com/aws/en/tables/table-properties)
    *   Reference list of table properties available for Delta Lake tables.

## Data pipelines using Delta Lake and Lakeflow Spark Declarative Pipelines[​](#data-pipelines-using-delta-lake-and-lakeflow-spark-declarative-pipelines "Direct link to data-pipelines-using-delta-lake-and-lakeflow-spark-declarative-pipelines")

Databricks encourages users to leverage a [medallion architecture](https://docs.databricks.com/aws/en/lakehouse/medallion) to process data through a series of tables as data is cleaned and enriched. [Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/) simplifies ETL workloads through optimized execution and automated infrastructure deployment and scaling.

## Delta Lake feature compatibility[​](#delta-lake-feature-compatibility "Direct link to delta-lake-feature-compatibility")

Not all Delta Lake features are in all versions of Databricks Runtime. For information about Delta Lake versioning, see [Delta Lake feature compatibility and protocols](https://docs.databricks.com/aws/en/tables/features/feature-compatibility).

## Delta Lake API documentation[​](#delta-lake-api-documentation "Direct link to delta-lake-api-documentation")

For most read and write operations on Delta Lake tables, you can use [Spark SQL](https://docs.databricks.com/aws/en/sql/language-manual/) or Apache Spark [DataFrame](https://docs.databricks.com/aws/en/getting-started/dataframes) APIs.

For Delta Lake\-specific SQL statements, see [Delta Lake statements](https://docs.databricks.com/aws/en/sql/language-manual/#delta-lake-statements).

Databricks ensures binary compatibility with Delta Lake APIs in Databricks Runtime. To view the Delta Lake API version packaged in each Databricks Runtime version, see the **System environment** section on the relevant article in the [Databricks Runtime release notes](https://docs.databricks.com/aws/en/release-notes/runtime/). For documentation on Delta Lake APIs for Python, Scala, and Java, see the [OSS Delta Lake documentation](https://docs.delta.io/latest/delta-apidoc.html#delta-spark).
