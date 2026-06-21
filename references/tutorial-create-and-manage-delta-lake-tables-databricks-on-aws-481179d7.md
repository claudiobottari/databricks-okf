---
title: "Tutorial: Create and manage Delta Lake tables | Databricks on AWS"
source: https://docs.databricks.com/aws/en/delta/tutorial
ingestedAt: "2026-06-18T08:05:08.995Z"
---

This tutorial demonstrates common Delta Lake table operations using sample data. [Delta Lake](https://docs.databricks.com/aws/en/delta/) is the optimized storage layer that provides the foundation for tables on Databricks. Unless otherwise specified, all tables on Databricks are Delta Lake tables.

## Before you begin[​](#before-you-begin "Direct link to Before you begin")

To complete this tutorial, you need:

*   Permission to use an existing compute resource or create a new compute resource. See [Compute](https://docs.databricks.com/aws/en/compute/).
*   Unity Catalog permissions: `USE CATALOG`, `USE SCHEMA`, and `CREATE TABLE` on the `workspace` catalog. To set these permissions, see your Databricks administrator or [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference).

These examples rely on a dataset called _Synthetic Person Records: 10K to 10M Records_. This dataset contains fictitious records of people, including their first and last names, gender, and age.

First, download the dataset for this tutorial.

1.  Visit the [Synthetic Person Records: 10K to 10M Records](https://www.kaggle.com/datasets/swainproject/synthetic-data-person/) page on Kaggle.
2.  Click **Download** and then **Download dataset as zip**. This downloads a file named `archive.zip` to your local machine.
3.  Extract the `archive` folder from the `archive.zip` file.

Next, upload the `person_10000.csv` dataset to a Unity Catalog [volume](https://docs.databricks.com/aws/en/volumes/) within your Databricks workspace. Databricks recommends uploading your data to a Unity Catalog volume because volumes provide capabilities for accessing, storing, governing, and organizing files.

1.  Open Catalog Explorer by clicking ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** in the sidebar.
2.  In Catalog Explorer, click ![Add or plus icon](data:image/png;base64,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) **Add data** and **Create a volume**.
3.  Name the volume `my-volume` and select **Managed volume** as the volume type.
4.  Select the `workspace` catalog and the `default` schema, and then click **Create**.
5.  Open `my-volume` and click **Upload to this volume**.
6.  Drag and drop or browse to and select the `person_10000.csv` file from within the `archive` folder on your local machine.
7.  Click **Upload**.

Last, create a notebook for running the sample code.

1.  Click ![Add or plus icon](data:image/png;base64,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) **New** in the sidebar.
2.  Click ![Notebook icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zIDEuNzVDMyAxLjMzNTc5IDMuMzM1NzkgMSAzLjc1IDFIMTQuMjVDMTQuNjY0MiAxIDE1IDEuMzM1NzkgMTUgMS43NVYxNC4yNUMxNSAxNC42NjQyIDE0LjY2NDIgMTUgMTQuMjUgMTVIMy43NUMzLjMzNTc5IDE1IDMgMTQuNjY0MiAzIDE0LjI1VjEyLjVIMVYxMUgzVjguNzVIMVY3LjI1SDNWNUgxVjMuNUgzVjEuNzVaTTQuNSAyLjVWMTMuNUg2VjIuNUg0LjVaTTcuNSAyLjVWMTMuNUgxMy41VjIuNUg3LjVaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Notebook** to create a new notebook.
3.  Choose a language for the notebook.

## Create a table[​](#create-a-table "Direct link to create-a-table")

Create a new Unity Catalog managed table named `workspace.default.people_10k` from `person_10000.csv`. Delta Lake is the default for all table creation, read, and write commands in Databricks.

*   Python
*   Scala
*   SQL

Python

    from pyspark.sql.types import StructType, StructField, IntegerType, StringTypeschema = StructType([  StructField("id", IntegerType(), True),  StructField("firstName", StringType(), True),  StructField("lastName", StringType(), True),  StructField("gender", StringType(), True),  StructField("age", IntegerType(), True)])df = spark.read.format("csv").option("header", True).schema(schema).load("/Volumes/workspace/default/my-volume/person_10000.csv")# Create the table if it does not exist. Otherwise, replace the existing table.df.writeTo("workspace.default.people_10k").createOrReplace()# If you know the table does not already exist, you can use this command instead.# df.write.saveAsTable("workspace.default.people_10k")# View the new table.df = spark.read.table("workspace.default.people_10k")display(df)

There are several different ways to create or clone tables. For more information, see [CREATE TABLE](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table).

In Databricks Runtime 13.3 LTS and above, you can use [CREATE TABLE LIKE](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-like) to create a new empty Delta Lake table that duplicates the schema and table properties of a source Delta Lake table. This can be useful when promoting tables from a development environment into production.

SQL

    CREATE TABLE workspace.default.people_10k_prod LIKE workspace.default.people_10k

Use the `DeltaTableBuilder` API for [Python](https://docs.delta.io/latest/api/python/spark/index.html) and [Scala](https://docs.delta.io/latest/api/scala/spark/io/delta/tables/DeltaTableBuilder.html) to create an empty table. Compared to `DataFrameWriter` and `DataFrameWriterV2`, the `DeltaTableBuilder` API makes it easier to specify additional information like column comments, table properties, and [generated columns](https://docs.databricks.com/aws/en/tables/features/generated-columns).

*   Python
*   Scala

Python

    from delta.tables import DeltaTable(  DeltaTable.createIfNotExists(spark)    .tableName("workspace.default.people_10k_2")    .addColumn("id", "INT")    .addColumn("firstName", "STRING")    .addColumn("lastName", "STRING", comment="surname")    .addColumn("gender", "STRING")    .addColumn("age", "INT")    .execute())display(spark.read.table("workspace.default.people_10k_2"))

## Upsert to a table[​](#upsert-to-a-table "Direct link to upsert-to-a-table")

Modify existing records in a table or add new ones using an operation called _upsert_. To merge a set of updates and insertions into an existing Delta Lake table, use the `DeltaTable.merge` method in [Python](https://docs.delta.io/latest/api/python/spark/index.html) and [Scala](https://docs.delta.io/latest/api/scala/spark/io/delta/tables/DeltaTable.html) and the [MERGE INTO](https://docs.databricks.com/aws/en/sql/language-manual/delta-merge-into) statement in SQL.

For example, merge data from the source table `people_10k_updates` to the target Delta Lake table `workspace.default.people_10k`. When there is a matching row in both tables, Delta Lake updates the data column using the given expression. When there is no matching row, Delta Lake adds a new row.

*   Python
*   Scala
*   SQL

Python

    from pyspark.sql.types import StructType, StructField, StringType, IntegerTypefrom delta.tables import DeltaTableschema = StructType([  StructField("id", IntegerType(), True),  StructField("firstName", StringType(), True),  StructField("lastName", StringType(), True),  StructField("gender", StringType(), True),  StructField("age", IntegerType(), True)])data = [  (10001, 'Billy', 'Luppitt', 'M', 55),  (10002, 'Mary', 'Smith', 'F', 98),  (10003, 'Elias', 'Leadbetter', 'M', 48),  (10004, 'Jane', 'Doe', 'F', 30),  (10005, 'Joshua', '', 'M', 90),  (10006, 'Ginger', '', 'F', 16),]# Create the source table if it does not exist. Otherwise, replace the existing source table.people_10k_updates = spark.createDataFrame(data, schema)people_10k_updates.createOrReplaceTempView("people_10k_updates")# Merge the source and target tables.deltaTable = DeltaTable.forName(spark, 'workspace.default.people_10k')(deltaTable.alias("people_10k")  .merge(    people_10k_updates.alias("people_10k_updates"),    "people_10k.id = people_10k_updates.id")  .whenMatchedUpdateAll()  .whenNotMatchedInsertAll()  .execute())# View the additions to the table.df = spark.read.table("workspace.default.people_10k")df_filtered = df.filter(df["id"] >= 10001)display(df_filtered)

In SQL, the `*` operator updates or inserts all columns in the target table, assuming that the source table has the same columns as the target table. If the target table does not have the same columns, the query throws an analysis error. Also, you must specify a value for every column in your table when you perform an insert operation. The column values can be empty, for example, `''`. When you perform an insert operation, you do not need to update all values.

## Read a table[​](#read-a-table "Direct link to read-a-table")

Use the table name or path to access data in Delta Lake tables. To access Unity Catalog managed tables, use a fully-qualified table name. Path-based access is only supported for volumes and external tables, not for managed tables. For more information, see [Path rules and access in Unity Catalog volumes](https://docs.databricks.com/aws/en/volumes/paths).

*   Python
*   Scala
*   SQL

Python

    people_df = spark.read.table("workspace.default.people_10k")display(people_df)

## Write to a table[​](#write-to-a-table "Direct link to write-to-a-table")

Delta Lake uses the standard syntax for writing data to tables. To add new data to an existing Delta Lake table, use the append mode. Unlike upserting, writing to a table does not check for duplicate records.

*   Python
*   Scala
*   SQL

Python

    from pyspark.sql.types import StructType, StructField, StringType, IntegerTypefrom pyspark.sql.functions import colschema = StructType([  StructField("id", IntegerType(), True),  StructField("firstName", StringType(), True),  StructField("lastName", StringType(), True),  StructField("gender", StringType(), True),  StructField("age", IntegerType(), True)])data = [  (10007, 'Miku', 'Hatsune', 'F', 25)]# Create the new data.df  = spark.createDataFrame(data, schema)# Append the new data to the target table.df.write.mode("append").saveAsTable("workspace.default.people_10k")# View the new addition.df = spark.read.table("workspace.default.people_10k")df_filtered = df.filter(df["id"] == 10007)display(df_filtered)

Databricks notebook cell outputs display a maximum of 10,000 rows or 2 MB, whichever is lower. Because `workspace.default.people_10k` contains more than 10,000 rows, only the first 10,000 rows appear in the notebook output for `display(df)`. The additional rows are present in the table, but are not rendered in the notebook output due to this limit. You can view the additional rows by specifically filtering for them.

To replace all the data in a table, use the overwrite mode.

*   Python
*   Scala
*   SQL

Python

    df.write.mode("overwrite").saveAsTable("workspace.default.people_10k")

## Update a table[​](#update-a-table "Direct link to update-a-table")

Update data in a Delta Lake table based on a predicate. For example, change the values in the `gender` column from `Female` to `F`, from `Male` to `M`, and from `Other` to `O`.

*   Python
*   Scala
*   SQL

Python

    from delta.tables import *from pyspark.sql.functions import *deltaTable = DeltaTable.forName(spark, "workspace.default.people_10k")# Declare the predicate and update rows using a SQL-formatted string.deltaTable.update(  condition = "gender = 'Female'",  set = { "gender": "'F'" })# Declare the predicate and update rows using Spark SQL functions.deltaTable.update(  condition = col('gender') == 'Male',  set = { 'gender': lit('M') })deltaTable.update(  condition = col('gender') == 'Other',  set = { 'gender': lit('O') })# View the updated table.df = spark.read.table("workspace.default.people_10k")display(df)

## Delete from a table[​](#delete-from-a-table "Direct link to delete-from-a-table")

Remove data that matches a predicate from a Delta Lake table. For example, the code below demonstrates two delete operations: first deleting rows where age is less than 18, then deleting rows where age is less than 21.

*   Python
*   Scala
*   SQL

Python

    from delta.tables import *from pyspark.sql.functions import *deltaTable = DeltaTable.forName(spark, "workspace.default.people_10k")# Declare the predicate and delete rows using a SQL-formatted string.deltaTable.delete("age < '18'")# Declare the predicate and delete rows using Spark SQL functions.deltaTable.delete(col('age') < '21')# View the updated table.df = spark.read.table("workspace.default.people_10k")display(df)

important

Deletion removes the data from the latest version of the Delta Lake table but does not remove it from physical storage until the old versions are explicitly vacuumed. For more information, see [vacuum](https://docs.databricks.com/aws/en/tables/operations/vacuum).

## Display table history[​](#display-table-history "Direct link to display-table-history")

Use the `DeltaTable.history` method in [Python](https://docs.delta.io/latest/api/python/spark/index.html) and [Scala](https://docs.delta.io/latest/api/scala/spark/io/delta/tables/DeltaTable.html) and the [DESCRIBE HISTORY](https://docs.databricks.com/aws/en/tables/history) statement in SQL to view the provenance information for each write to a table.

*   Python
*   Scala
*   SQL

Python

    from delta.tables import *deltaTable = DeltaTable.forName(spark, "workspace.default.people_10k")display(deltaTable.history())

## Query an earlier version of the table using time travel[​](#query-an-earlier-version-of-the-table-using-time-travel "Direct link to query-an-earlier-version-of-the-table-using-time-travel")

Query an older snapshot of a Delta Lake table using Delta Lake time travel. To query a specific version, use the table's version number or timestamp. For example, query version `0` or timestamp `2026-01-05T23:09:47.000+00:00` from the table's history.

*   Python
*   Scala
*   SQL

Python

    from delta.tables import *deltaTable = DeltaTable.forName(spark, "workspace.default.people_10k")deltaHistory = deltaTable.history()# Query using the version number.display(deltaHistory.where("version == 0"))# Query using the timestamp.display(deltaHistory.where("timestamp == '2026-01-05T23:09:47.000+00:00'"))

For timestamps, only date or timestamp strings are accepted. For example, strings must be formatted as `"2026-01-05T22:43:15.000+00:00"` or `"2026-01-05 22:43:15"`.

Use `DataFrameReader` options to create a DataFrame from a Delta Lake table that is fixed to a specific version or timestamp of the table.

*   Python
*   Scala
*   SQL

Python

    # Query using the version number.df = spark.read.option('versionAsOf', 0).table("workspace.default.people_10k")# Query using the timestamp.df = spark.read.option('timestampAsOf', '2026-01-05T23:09:47.000+00:00').table("workspace.default.people_10k")display(df)

For more information, see [Work with table history](https://docs.databricks.com/aws/en/tables/history).

## Optimize a table[​](#optimize-a-table "Direct link to optimize-a-table")

Multiple changes to a table can create several small files, which slows read query performance. Use the optimize operation to improve speed by combining small files into larger ones. See [OPTIMIZE](https://docs.databricks.com/aws/en/sql/language-manual/delta-optimize).

*   Python
*   Scala
*   SQL

Python

    from delta.tables import *deltaTable = DeltaTable.forName(spark, "workspace.default.people_10k")deltaTable.optimize().executeCompaction()

## Use liquid clustering[​](#use-liquid-clustering "Direct link to use-liquid-clustering")

To further improve read performance, use liquid clustering to colocate related data. For example, enable clustering on the high cardinality column `firstName`. Use `OPTIMIZE FULL` to apply clustering to all existing data. For more information, see [Use liquid clustering for tables](https://docs.databricks.com/aws/en/tables/clustering).

*   Python
*   Scala
*   SQL

Python

    spark.sql("ALTER TABLE workspace.default.people_10k CLUSTER BY (firstName)")spark.sql("OPTIMIZE FULL workspace.default.people_10k")

## Clean up snapshots with the vacuum operation[​](#clean-up-snapshots-with-the-vacuum-operation "Direct link to clean-up-snapshots-with-the-vacuum-operation")

Delta Lake has snapshot isolation for reads, which means that it is safe to run an optimize operation while other users or jobs are querying the table. However, you should eventually clean up old snapshots because doing so reduces storage costs, improves query performance, and ensures data compliance. Run the `VACUUM` operation to clean up old snapshots. See [VACUUM](https://docs.databricks.com/aws/en/sql/language-manual/delta-vacuum).

*   Python
*   Scala
*   SQL

Python

    from delta.tables import *deltaTable = DeltaTable.forName(spark, "workspace.default.people_10k")deltaTable.vacuum()

For more information on using the vacuum operation effectively, see [Remove unused data files with vacuum](https://docs.databricks.com/aws/en/tables/operations/vacuum).

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Use liquid clustering for tables](https://docs.databricks.com/aws/en/tables/clustering)
*   [Best practices: Delta Lake](https://docs.databricks.com/aws/en/delta/best-practices)

*   [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta/)
