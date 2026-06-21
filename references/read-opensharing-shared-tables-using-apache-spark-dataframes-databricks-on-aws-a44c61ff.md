---
title: Read OpenSharing shared tables using Apache Spark DataFrames | Databricks on AWS
source: https://docs.databricks.com/aws/en/query/formats/deltasharing
ingestedAt: "2026-06-18T08:18:32.645Z"
---

This article provides syntax examples of using Apache Spark to query data shared using [OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/). Use the `deltasharing` keyword as a format option for DataFrame operations.

You can also create queries that use shared table names in OpenSharing catalogs registered in the metastore, such as those in the following examples:

*   SQL
*   Python

SQL

    SELECT * FROM shared_table_name

For more on configuring OpenSharing in Databricks and querying data using shared table names, see [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).

You can use Structured Streaming to process records in shared tables incrementally. To use Structured Streaming, you must enable history sharing for the table. See [ALTER SHARE](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-alter-share). History sharing requires Databricks Runtime 12.2 LTS or above.

If the shared table has change data feed enabled on the source Delta table and history enabled on the share, you can use change data feed while reading an OpenSharing share with Structured Streaming or batch operations. See [Use change data feed on Databricks](https://docs.databricks.com/aws/en/tables/features/change-data-feed).

## Read with the OpenSharing format keyword[​](#read-with-the-opensharing-format-keyword "Direct link to read-with-the-opensharing-format-keyword")

The `deltasharing` keyword is supported for Apache Spark DataFrame read operations, as shown in the following example:

Python

    df = (spark.read  .format("deltasharing")  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))

For tables that have history shared and change data feed enabled, you can read change data feed records using Apache Spark DataFrames. History sharing requires Databricks Runtime 12.2 LTS or above.

Python

    df = (spark.read  .format("deltasharing")  .option("readChangeFeed", "true")  .option("startingTimestamp", "2021-04-21 05:45:46")  .option("endingTimestamp", "2021-05-21 12:00:00")  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))

For tables that have history shared, you can use the shared table as a source for Structured Streaming. History sharing requires Databricks Runtime 12.2 LTS or above.

Python

    streaming_df = (spark.readStream  .format("deltasharing")  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))# If CDF is enabled on the source tablestreaming_cdf_df = (spark.readStream  .format("deltasharing")  .option("readChangeFeed", "true")  .option("startingTimestamp", "2021-04-21 05:45:46")  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
