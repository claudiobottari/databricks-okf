---
title: Migrate a Parquet data lake to Delta Lake | Databricks on AWS
source: https://docs.databricks.com/aws/en/migration/parquet-to-delta-lake
ingestedAt: "2026-06-18T08:13:51.114Z"
---

This article provides recommendations for converting an existing Parquet data lake to Delta Lake. Delta Lake is the underlying format in the [Databricks lakehouse](https://docs.databricks.com/aws/en/lakehouse/). See [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta/).

## Considerations before converting to Delta Lake[​](#considerations-before-converting-to-delta-lake "Direct link to considerations-before-converting-to-delta-lake")

Your Parquet data lake likely has a partitioning strategy that has been optimized for your existing workloads and systems. While you can convert to Delta Lake and maintain this partitioning structure, over-partitioned tables are one of the main culprits that cause slow workloads on Delta Lake. See [When to partition tables on Databricks](https://docs.databricks.com/aws/en/tables/partitions) and [guidelines for adapting Spark code to Databricks](https://docs.databricks.com/aws/en/migration/spark#parquet-delta).

You also need to consider whether or not the data being converted is still growing, as well as how frequently data is currently being queried. You might choose different approaches for different Parquet tables in your data lake.

## Approaches to Delta Lake conversion[​](#approaches-to-delta-lake-conversion "Direct link to approaches-to-delta-lake-conversion")

The following matrix outlines the four main approaches to converting a Parquet data lake to Delta Lake and some of the trade-offs. To clarify each column:

*   **Incremental**: Denotes functionality that supports converting additional data appended to the conversion source after conversion has begun.
*   **Duplicates data**: Indicates whether data is written to a new location or modified in place.
*   **Maintains data structure**: Indicates whether the partitioning strategy is maintained during conversion.
*   **Backfill data**: Denotes functionality that supports backfilling data that has been added to the conversion source after conversion has begun.
*   **Ease of use**: Indicates the level of user effort to configure and run the data conversion.

The following sections discuss each of these options in greater depth.

## Migrate Parquet data with `CLONE` Parquet[​](#migrate-parquet-data-with-clone-parquet "Direct link to migrate-parquet-data-with-clone-parquet")

You can use `CLONE` Parquet to incrementally copy data from a Parquet data lake to Delta Lake. Shallow clones create pointers to existing Parquet files, maintaining your Parquet table in its original location and format while providing optimized access through collected file statistics. You can write to the table created by a shallow clone without impacting the original data source.

Deep clone copies all data files from the source to a new location while converting to Delta Lake. Deep clone allows you to incrementally detect new files, including backfill operations, on subsequent execution of the logic. See [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](https://docs.databricks.com/aws/en/ingestion/data-migration/clone-parquet).

The following example demonstrates using `CLONE`:

SQL

    CREATE OR REPLACE TABLE <target-table-name> [SHALLOW] CLONE parquet.`/path/to/data`;

## Migrate Parquet data with `CONVERT TO DELTA`[​](#migrate-parquet-data-with-convert-to-delta "Direct link to migrate-parquet-data-with-convert-to-delta")

You can use `CONVERT TO DELTA` to transform a directory of Parquet files into a Delta table with a single command. Once you have converted a table to Delta Lake, you should stop reading and writing from the table using Parquet logic. Data written to the target directory after conversion has started might not be reflected in the resultant Delta table. See [Convert to Delta Lake](https://docs.databricks.com/aws/en/ingestion/data-migration/convert-to-delta).

The follow example demonstrates using `CONVERT TO DELTA`:

SQL

    CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;

## Migrate Parquet data with Auto Loader[​](#migrate-parquet-data-with-auto-loader "Direct link to migrate-parquet-data-with-auto-loader")

While Auto Loader is a product designed for incremental data ingestion from cloud object storage, you can leverage it to implement a pattern that incrementally copies all data from a given directory to a target table. See [What is Auto Loader?](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/).

The following code example includes configurations that:

*   Process all existing files in the source directory.
*   Trigger an automatic weekly backfill job to capture files that might have been missed.
*   Allow Apache Spark to use many Spark jobs to avoid spill and out-of-memory errors associated with large data partitions.
*   Provide end-to-end exactly-once processing guarantees.

Python

    (spark.readStream  .format("cloudFiles")  .option("cloudFiles.format", "parquet")  .option("cloudFiles.includeExistingFiles", "true")  .option("cloudFiles.backfillInterval", "1 week")  .option("cloudFiles.schemaLocation", checkpoint_path)  .load(file_path)  .writeStream  .option("checkpointLocation", checkpoint_path)  .trigger(availableNow=True)  .toTable(table_name))

You can use Auto Loader in Lakeflow Spark Declarative Pipelines with either Python or SQL:

*   [Load data using streaming tables (Python/SQL notebook)](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/onboard-data)

*   [Streaming tables](https://docs.databricks.com/aws/en/ldp/concepts/streaming-tables)

## Migrate Parquet data with custom Apache Spark batch logic[​](#migrate-parquet-data-with-custom-apache-spark-batch-logic "Direct link to migrate-parquet-data-with-custom-apache-spark-batch-logic")

Writing custom Apache Spark logic provides great flexibility in controlling how and when different data from your source system is migrated, but might require extensive configuration to provide capabilities built into other approaches.

At the heart of this approach is a simple Apache Spark read and write operation, such as the following:

Python

    spark.read.format("parquet").load(file_path).write.mode("append").saveAsTable(table_name)

To perform backfills or incremental migration, you might be able to rely on the partitioning structure of your data source, but might also need to write custom logic to track which files have been added since you last loaded data from the source. While you can use Delta Lake [merge](https://docs.databricks.com/aws/en/delta/merge) capabilities to avoid writing duplicate records, comparing all records from a large Parquet source table to the contents of a large Delta table is a computationally expensive task.

## When shouldn't you convert to Delta Lake?[​](#when-shouldnt-you-convert-to-delta-lake "Direct link to when-shouldnt-you-convert-to-delta-lake")

Before converting all your existing Parquet data to Delta Lake, you are likely to consider potential trade-offs.

Databricks designs many optimized features of the lakehouse around Delta Lake, and Delta Lake provides a rich open source ecosystem with [native connectors](https://delta.io/integrations/) for many languages and enterprise data systems. [OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/) extends the ability to share data stored with Delta Lake to other clients.

Delta Lake is built on top of Parquet, and as such, Databricks also has optimized readers and writers for interacting with Parquet files.

Databricks recommends using Delta Lake for all tables that receive regular updates or queries from Databricks. You might choose to maintain data in Parquet format in some cases, such as the following:

*   An upstream system that writes data to Parquet does not support native writing to Delta Lake.
*   A downstream system that reads Parquet data cannot read Delta Lake.

In both of these cases, you might want to replicate your tables to Delta Lake to leverage performance benefits while reading, writing, updating, and deleting records in the table.

note

Simultaneously modifying data in the same Delta table stored in S3 from multiple workspaces or data systems is not recommended. See [Delta Lake limitations on S3](https://docs.databricks.com/aws/en/delta/s3-limitations).
