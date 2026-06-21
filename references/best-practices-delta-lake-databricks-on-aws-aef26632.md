---
title: "Best practices: Delta Lake | Databricks on AWS"
source: https://docs.databricks.com/aws/en/delta/best-practices
ingestedAt: "2026-06-18T08:05:02.378Z"
---

This article describes best practices when using Delta Lake.

## Best practices overview[​](#best-practices-overview "Direct link to Best practices overview")

The following are general recommendations that apply to most Delta Lake workloads:

*   Use Unity Catalog managed tables. See [Unity Catalog managed tables in Databricks for Delta Lake and Apache Iceberg](https://docs.databricks.com/aws/en/tables/managed).
*   Use predictive optimization. See [Predictive optimization for Unity Catalog managed tables](https://docs.databricks.com/aws/en/optimizations/predictive-optimization).
*   Use liquid clustering. See [Use liquid clustering for tables](https://docs.databricks.com/aws/en/tables/clustering).
*   When deleting and recreating a table in the same location, you should always use a `CREATE OR REPLACE TABLE` statement. See [Drop or replace a table](https://docs.databricks.com/aws/en/tables/operations/drop-table).

## Remove legacy Delta configurations[​](#remove-legacy-delta-configurations "Direct link to Remove legacy Delta configurations")

Databricks recommends removing most explicit legacy Delta configurations from Spark configurations and table properties when upgrading to a new Databricks Runtime version. Legacy configurations can prevent new optimizations and default values introduced by Databricks from being applied to migrated workloads.

## Compact files[​](#compact-files "Direct link to compact-files")

Predictive optimization automatically runs `OPTIMIZE` and `VACUUM` commands on Unity Catalog managed tables. See [Predictive optimization for Unity Catalog managed tables](https://docs.databricks.com/aws/en/optimizations/predictive-optimization).

Databricks recommends frequently running the [OPTIMIZE](https://docs.databricks.com/aws/en/tables/operations/optimize) command to compact small files.

note

This operation does not remove the old files. To remove them, run the [VACUUM](https://docs.databricks.com/aws/en/tables/operations/vacuum) command.

## Do not use Spark caching with Delta Lake[​](#do-not-use-spark-caching-with-delta-lake "Direct link to do-not-use-spark-caching-with-delta-lake")

Databricks does not recommend that you use Spark caching for the following reasons:

*   You lose any data skipping that can come from additional filters added on top of the cached `DataFrame`.
*   The data that gets cached might not be updated if the table is accessed using a different identifier.

## Differences between Delta Lake and Parquet on Apache Spark[​](#differences-between-delta-lake-and-parquet-on-apache-spark "Direct link to differences-between-delta-lake-and-parquet-on-apache-spark")

Delta Lake handles the following operations automatically. You should never perform these operations manually:

*   **`REFRESH TABLE`**: Delta Lake tables always return the most up-to-date information, so there is no need to call `REFRESH TABLE` manually after changes.
*   **Add and remove partitions**: Delta Lake automatically tracks the set of partitions present in a table and updates the list as data is added or removed. As a result, there is no need to run `ALTER TABLE [ADD|DROP] PARTITION` or `MSCK`.
*   **Load a single partition**: Reading partitions directly is not necessary. For example, you don't need to run `spark.read.format("parquet").load("/data/date=2017-01-01")`. Instead, use a `WHERE` clause for data skipping, such as `spark.read.table("<table-name>").where("date = '2017-01-01'")`.
*   **Don't manually modify data files**: Delta Lake uses the transaction log to commit changes to the table atomically. Do not directly modify, add, or delete Parquet data files in a Delta Lake table, because this can lead to lost data or table corruption.

## Improve performance for Delta Lake merge[​](#improve-performance-for-delta-lake-merge "Direct link to improve-performance-for-delta-lake-merge")

You can reduce the time it takes to merge by using the following approaches:

*   **Reduce the search space for matches**: By default, the `merge` operation searches the entire Delta Lake table to find matches in the source table. One way to speed up `merge` is to reduce the search space by adding known constraints in the match condition. For example, suppose you have a table that is partitioned by `country` and `date` and you want to use `merge` to update information for the last day and a specific country. Adding the following condition makes the query faster, as it looks for matches only in the relevant partitions:
    
    SQL
    
        events.date = current_date() AND events.country = 'USA'
    
    Furthermore, this query also reduces the chances of conflicts with other concurrent operations. See [Isolation levels and write conflicts](https://docs.databricks.com/aws/en/optimizations/isolation/) for more details.
    
*   **Compact files**: If the data is stored in many small files, reading the data to search for matches can become slow. You can compact small files into larger files to improve read throughput. See [Optimize data file layout](https://docs.databricks.com/aws/en/tables/operations/optimize) for details.
    
*   **Control the shuffle partitions for writes**: The `merge` operation shuffles data multiple times to compute and write the updated data. The number of tasks used to shuffle is controlled by the Spark session configuration `spark.sql.shuffle.partitions`. Setting this parameter not only controls the parallelism but also determines the number of output files. Increasing the value increases parallelism but also generates a larger number of smaller data files.
    
*   **Enable optimized writes**: For partitioned tables, `merge` can produce a much larger number of small files than the number of shuffle partitions. This is because every shuffle task can write multiple files in multiple partitions, and can become a performance bottleneck. You can reduce the number of files by enabling optimized writes. See [Optimized writes](https://docs.databricks.com/aws/en/tables/tune-file-size#optimized-writes).
    
*   **Tune file sizes in table**: Databricks automatically tunes file sizes based on table size, using smaller files for smaller tables and larger files for larger tables. See the section on [tuning file sizes](https://docs.databricks.com/aws/en/tables/tune-file-size) for details.
    
*   **Low Shuffle Merge**: [Low Shuffle Merge](https://docs.databricks.com/aws/en/optimizations/low-shuffle-merge) provides an optimized implementation of `MERGE` that provides better performance for most common workloads. In addition, it preserves existing data layout optimizations such as [liquid clustering](https://docs.databricks.com/aws/en/tables/clustering) on unmodified data.
