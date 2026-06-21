---
title: Update jobs when you upgrade legacy workspaces to Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/jobs-update
ingestedAt: "2026-06-18T08:04:37.019Z"
---

When you [upgrade legacy workspaces to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/), you might need to update existing jobs to reference upgraded tables and filepaths. The main table on this page lists typical scenarios and suggestions for updating your jobs. Scenarios that require code examples link to the [Detailed scenarios](#detailed-scenarios) section.

For a demo of updating jobs to Unity Catalog, see [Upgrading a Job to Unity Catalog](https://app.getreprise.com/launch/m6ErgVn/).

## Overview of scenarios[​](#overview-of-scenarios "Direct link to overview-of-scenarios")

## Detailed scenarios[​](#detailed-scenarios "Direct link to detailed-scenarios")

The following scenarios require code examples.

### Job notebooks use `spark.catalog.X` on a shared cluster[​](#job-notebooks-use-sparkcatalogx-on-a-shared-cluster "Direct link to job-notebooks-use-sparkcatalogx-on-a-shared-cluster")

Use Databricks Runtime 14.2 or above.

If a Databricks Runtime upgrade is not possible, use the following workarounds.

Instead of `tableExists`, use:

Python

    # SQL workarounddef tableExistsSql(tablename):    try:        spark.sql(f"DESCRIBE TABLE {tablename};")    except Exception as e:        return False    return TruetableExistsSql("jakob.jakob.my_table")

Instead of `listTables`, use `SHOW TABLES` (which also supports restricting by database or pattern matching):

For `setDefaultCatalog`, run:

Python

    spark.sql("USE CATALOG <catalog_name>")

### Job notebooks use `sc.parallelize` and `spark.read.json()` on a shared cluster[​](#job-notebooks-use-scparallelize-and-sparkreadjson-on-a-shared-cluster "Direct link to job-notebooks-use-scparallelize-and-sparkreadjson-on-a-shared-cluster")

Use `json.loads` instead.

**Before:**

Python

    json_content1 = "{'json_col1': 'hello', 'json_col2': 32}"json_content2 = "{'json_col1': 'hello', 'json_col2': 'world'}"json_list = []json_list.append(json_content1)json_list.append(json_content2)df = spark.read.json(sc.parallelize(json_list))display(df)

**After:**

Python

    from pyspark.sql import Rowimport json# Sample JSON data as a list of dictionaries (similar to JSON objects)json_data_str = response.textjson_data = [json.loads(json_data_str)]# Convert dictionaries to Row objectsrows = [Row(**json_dict) for json_dict in json_data]# Create DataFrame from list of Row objectsdf = spark.createDataFrame(rows)df.display()

### Job notebooks create empty DataFrames using `sc.emptyRDD()` on a shared cluster[​](#job-notebooks-create-empty-dataframes-using-scemptyrdd-on-a-shared-cluster "Direct link to job-notebooks-create-empty-dataframes-using-scemptyrdd-on-a-shared-cluster")

**Before:**

Scala

    val schema = StructType( StructField("k", StringType, true) :: StructField("v", IntegerType, false) :: Nil)spark.createDataFrame(sc.emptyRDD[Row], schema)

**After:**

Scala

    import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType}val schema = StructType( StructField("k", StringType, true) :: StructField("v", IntegerType, false) :: Nil)spark.createDataFrame(new java.util.ArrayList[Row](), schema)

Python

    from pyspark.sql.types import StructType, StructField, StringTypeschema = StructType([StructField("k", StringType(), True)])spark.createDataFrame([], schema)

### Job notebooks use `input_file_name()` on a shared cluster[​](#job-notebooks-use-input_file_name-on-a-shared-cluster "Direct link to job-notebooks-use-input_file_name-on-a-shared-cluster")

`input_file_name()` is not supported in Unity Catalog for shared clusters.

To get the file name:

Python

    .withColumn("RECORD_FILE_NAME", col("_metadata.file_name"))

To get the full file path:

Python

    .withColumn("RECORD_FILE_PATH", col("_metadata.file_path"))

Both options work with `spark.read`.

### Job notebooks perform data operations on DBFS on a shared cluster[​](#job-notebooks-perform-data-operations-on-dbfs-on-a-shared-cluster "Direct link to job-notebooks-perform-data-operations-on-dbfs-on-a-shared-cluster")

When using DBFS with a shared cluster through the FUSE service, the cluster cannot reach the filesystem and generates a file-not-found error.

The following examples fail on a shared cluster:

Bash

    with open('/dbfs/test/sample_file.csv', 'r') as file:ls -ltr /dbfs/testcat /dbfs/test/sample_file.csv

Use one of the following solutions:

*   Use a Databricks Unity Catalog Volume instead of DBFS (preferred).
*   Update the code to use `dbutils` or `spark`, which use the direct-to-storage access path and are granted access to DBFS from shared clusters.
