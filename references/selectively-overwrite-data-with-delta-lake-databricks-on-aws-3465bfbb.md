---
title: Selectively overwrite data with Delta Lake | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta/selective-overwrite
ingestedAt: "2026-06-18T08:05:07.070Z"
---

Delta Lake has the following distinct options for selective overwrites:

For most use cases, Databricks recommends using `REPLACE USING` or `REPLACE WHERE`. Use `REPLACE ON` only if your use case requires complex or NULL-safe matching conditions.

For detail on each option's replacement behavior, see [`INSERT`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into). For a complete list of `DataFrameWriter` Delta Lake options, see [Delta Lake and Apache Iceberg](https://docs.databricks.com/aws/en/spark/api-options#batch-writer-delta).

In Scala and Python, `replaceOn` and `replaceUsing` can't be used in combination with `replaceWhere`, `partitionOverwriteMode`, or `overwriteSchema`.

For empty source queries, both `REPLACE USING` and `REPLACE ON` do not delete data, however, `REPLACE WHERE` might delete data.

important

If data has been accidentally overwritten, you can use [restore](https://docs.databricks.com/aws/en/tables/history#restore) to undo the change.

## `REPLACE WHERE`[​](#replace-where "Direct link to replace-where")

You can selectively overwrite only the data that matches an arbitrary expression with `REPLACE WHERE`.

To atomically replace events in January in the target table, which is partitioned by `start_date`, with the data in `replace_data`:

*   Python
*   Scala
*   SQL

Python

    (replace_data.write  .mode("overwrite")  .option("replaceWhere", "start_date >= '2017-01-01' AND end_date <= '2017-01-31'")  .saveAsTable("events"))

This sample code writes out the data in `replace_data`, validates that all rows match the predicate, and performs an atomic replacement using `overwrite` semantics. If any values in the operation fall outside the predicate, this operation fails with an error by default.

On classic compute, to change this behavior to `overwrite` values within the predicate range and `insert` records outside the specified range, remove the constraint check by setting `spark.databricks.delta.replaceWhere.constraintCheck.enabled` to `false`:

*   Python
*   Scala
*   SQL

Python

    spark.conf.set("spark.databricks.delta.replaceWhere.constraintCheck.enabled", False)

note

`REPLACE WHERE` accepts a `boolean_expression` with some restrictions. See [`INSERT`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into) in the SQL language reference.

For empty source queries, `REPLACE WHERE` might delete table rows.

#### Legacy behavior[​](#legacy-behavior "Direct link to Legacy behavior")

Legacy `replaceWhere` is only available on classic compute. See [Classic compute overview](https://docs.databricks.com/aws/en/compute/use-compute).

If you use the legacy behavior of `replaceWhere`, queries overwrite data that matches a predicate only over partition columns. The following command would atomically replace the month January in the target table, which is partitioned by `date`, with the data in `df`:

*   Python
*   Scala

Python

    (df.write  .mode("overwrite")  .option("replaceWhere", "birthDate >= '2017-01-01' AND birthDate <= '2017-01-31'")  .saveAsTable("people10m"))

To use legacy behavior, set `spark.databricks.delta.replaceWhere.dataColumns.enabled` to `false`:

*   Python
*   Scala
*   SQL

Python

    spark.conf.set("spark.databricks.delta.replaceWhere.dataColumns.enabled", False)

## Dynamic data overwrites[​](#dynamic-data-overwrites "Direct link to dynamic-data-overwrites")

Dynamic data overwrites selectively replace data that match the specified key columns or boolean expression, leaving all other data unchanged. Partitioned tables, unpartitioned tables, and tables with liquid clustering are all supported.

Dynamic partition overwrites are a subset of dynamic data overwrite behavior. Dynamic partition overwrites replace all the existing data in each partition for which the write will commit new data and leaves all other partitions unchanged. Only partitioned tables are supported.

### `REPLACE USING`[​](#replace-using "Direct link to replace-using")

SQL supported in Databricks Runtime 16.3 and above. Python and Scala supported in Databricks Runtime 18.2 and above. For behavior differences in Databricks Runtime 16.3 to 17.1 see [Legacy behavior](#replace-using-legacy).

`REPLACE USING` enables compute-independent, atomic overwrite behavior that works on Databricks SQL warehouses, serverless compute, and classic compute. `REPLACE USING` doesn't require that you set a Spark session configuration.

`REPLACE USING` replaces rows when the specified columns compare equal under equality. All other data remains unchanged.

Use dynamic data overwrite with `REPLACE USING`:

*   Python
*   Scala
*   SQL

Python

    (sourceDataDF.write  .mode("overwrite")  .option("replaceUsing", "event_id, start_date")  .saveAsTable("events"))

For empty source queries, `REPLACE USING` does not delete any table rows.

For complex or NULL-safe matching conditions, use `REPLACE ON` instead. See [`REPLACE ON`](https://docs.databricks.com/aws/en/delta/selective-overwrite#dpo-replaceon).

See [`INSERT`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into) in the SQL language reference.

#### Legacy behavior[​](#legacy-behavior-1 "Direct link to legacy-behavior-1")

In Databricks Runtime 16.3 to 17.1, `REPLACE USING` uses legacy behavior and only allows dynamic partition overwrites, whereas Databricks Runtime 17.2 and above allows for dynamic data overwrites.

Keep the following constraints and behaviors in mind for `REPLACE USING` legacy behavior:

*   You must specify the full set of the table's partition columns in the `USING` clause.
*   Always validate that the data written touches only the expected partitions. A single row in the wrong partition can unintentionally overwrite the entire partition.

### `REPLACE ON`[​](#replace-on "Direct link to replace-on")

SQL supported in Databricks Runtime 17.1 and above. Python and Scala supported in Databricks Runtime 18.2 and above.

`REPLACE ON` replaces rows when they match a user-defined condition, unlike `REPLACE USING`, which replaces rows when the specified columns compare equal under equality. Use `REPLACE ON` when you need matching logic that `REPLACE USING` does not support, such as treating `NULL` values as equal.

Optionally, use the `targetAlias` option to specify an alias for the target table and the `.as()` or `.alias()` APIs to specify an alias for the source data.

For SQL syntax, see [`INSERT`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into).

*   Python
*   Scala
*   SQL

Python

    (sourceDataDF.alias("s")  .write  .mode("overwrite")  .option("targetAlias", "t")  .option("replaceOn", "s.event_id <=> t.event_id AND s.start_date <=> t.start_date")  .saveAsTable("events"))

For empty source queries, `REPLACE ON` does not delete any table rows.

## Dynamic partition overwrites with `partitionOverwriteMode` (legacy)[​](#dynamic-partition-overwrites-with-partitionoverwritemode-legacy "Direct link to dynamic-partition-overwrites-with-partitionoverwritemode-legacy")

Databricks Runtime 11.3 LTS and above supports dynamic partition overwrites for partitioned tables using overwrite mode: either `INSERT OVERWRITE` in SQL, or a DataFrame write with `df.write.mode("overwrite")`. This type of overwrite is only available for classic compute, not Databricks SQL warehouses or serverless compute.

warning

When possible, use `INSERT REPLACE USING` instead of partition overwrite `INSERT OVERWRITE PARTITION` and `spark.sql.sources.partitionOverwriteMode=dynamic`. Partition overwrite may use stale data when partitioning changes.

To use dynamic partition overwrite mode, set the Spark session configuration `spark.sql.sources.partitionOverwriteMode` to `dynamic`. Alternatively, you can set the `DataFrameWriter` option `partitionOverwriteMode` to `dynamic`. If present, the query-specific option overrides the mode defined in the session configuration. The default value for `spark.sql.sources.partitionOverwriteMode` is `static`.

The following example uses `partitionOverwriteMode`:

*   SQL
*   Python
*   Scala

SQL

    SET spark.sql.sources.partitionOverwriteMode=dynamic;INSERT OVERWRITE TABLE default.people10m SELECT * FROM morePeople;

Keep the following constraints and behaviors in mind for `partitionOverwriteMode`:

*   You can't set `overwriteSchema` to `true`.
*   You can't specify both `partitionOverwriteMode` and `replaceWhere` in the same `DataFrameWriter` operation.
*   If you specify a `replaceWhere` condition using a `DataFrameWriter` option, Delta Lake applies that condition to control which data is overwritten. This option takes precedence over the `partitionOverwriteMode` session-level configuration.
*   Always validate that the data written touches only the expected partitions. A single row in the wrong partition can unintentionally overwrite the entire partition.
