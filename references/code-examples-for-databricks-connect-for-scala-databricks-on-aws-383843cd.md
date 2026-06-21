---
title: Code examples for Databricks Connect for Scala | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/examples
ingestedAt: "2026-06-18T08:06:41.590Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article provides code examples that use Databricks Connect for Scala. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/). For the Python version of this article, see [Code examples for Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/examples).

Before you begin to use Databricks Connect, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install).

The following examples assume that you are using default authentication for Databricks Connect client setup.

## Example: Read a table[​](#example-read-a-table "Direct link to Example: Read a table")

This simple code example queries the specified table and then shows the specified table's first 5 rows.

Scala

    import com.databricks.connect.DatabricksSessionimport org.apache.spark.sql.SparkSessionobject Main {  def main(args: Array[String]): Unit = {    val spark = DatabricksSession.builder().getOrCreate()    val df = spark.read.table("samples.nyctaxi.trips")    df.limit(5).show()  }}

## Create a DataFrame[​](#create-a-dataframe "Direct link to Create a DataFrame")

This code example below:

1.  Creates an in-memory DataFrame.
2.  Creates a table with the name `zzz_demo_temps_table` within the `default` schema. If the table with this name already exists, the table is deleted first. To use a different schema or table, adjust the calls to `spark.sql`, `temps.write.saveAsTable`, or both.
3.  Saves the DataFrame's contents to the table.
4.  Runs a `SELECT` query on the table's contents.
5.  Shows the query's result.
6.  Deletes the table.

Scala

    import com.databricks.connect.DatabricksSessionimport org.apache.spark.sql.SparkSessionimport org.apache.spark.sql.types._import java.time.LocalDateobject Main {  def main(args: Array[String]): Unit = {    val spark = DatabricksSession.builder().getOrCreate()    // Create a Spark DataFrame consisting of high and low temperatures    // by airport code and date.    val schema = StructType(      Seq(        StructField("AirportCode", StringType, false),        StructField("Date", DateType, false),        StructField("TempHighF", IntegerType, false),        StructField("TempLowF", IntegerType, false)      )    )    val data = Seq(      ( "BLI", LocalDate.of(2021, 4, 3), 52, 43 ),      ( "BLI", LocalDate.of(2021, 4, 2), 50, 38),      ( "BLI", LocalDate.of(2021, 4, 1), 52, 41),      ( "PDX", LocalDate.of(2021, 4, 3), 64, 45),      ( "PDX", LocalDate.of(2021, 4, 2), 61, 41),      ( "PDX", LocalDate.of(2021, 4, 1), 66, 39),      ( "SEA", LocalDate.of(2021, 4, 3), 57, 43),      ( "SEA", LocalDate.of(2021, 4, 2), 54, 39),      ( "SEA", LocalDate.of(2021, 4, 1), 56, 41)    )    val temps = spark.createDataFrame(data).toDF(schema.fieldNames: _*)    // Create a table on the Databricks cluster and then fill    // the table with the DataFrame 's contents.    // If the table already exists from a previous run,    // delete it first.    spark.sql("USE default")    spark.sql("DROP TABLE IF EXISTS zzz_demo_temps_table")    temps.write.saveAsTable("zzz_demo_temps_table")    // Query the table on the Databricks cluster, returning rows    // where the airport code is not BLI and the date is later    // than 2021-04-01.Group the results and order by high    // temperature in descending order.    val df_temps = spark.sql("SELECT * FROM zzz_demo_temps_table " +      "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' " +      "GROUP BY AirportCode, Date, TempHighF, TempLowF " +      "ORDER BY TempHighF DESC")    df_temps.show()    // Results:    // +------------+-----------+---------+--------+    // | AirportCode|       Date|TempHighF|TempLowF|    // +------------+-----------+---------+--------+    // |        PDX | 2021-04-03|      64 |     45 |    // |        PDX | 2021-04-02|      61 |     41 |    // |        SEA | 2021-04-03|      57 |     43 |    // |        SEA | 2021-04-02|      54 |     39 |    // +------------+-----------+---------+--------+    // Clean up by deleting the table from the Databricks cluster.    spark.sql("DROP TABLE zzz_demo_temps_table")  }}

## Example: Use DatabricksSesssion or SparkSession[​](#example-use-databrickssesssion-or-sparksession "Direct link to Example: Use DatabricksSesssion or SparkSession")

The following example describes how to use the `SparkSession` class in cases where the `DatabricksSession` class in Databricks Connect is unavailable.

This example queries the specified table and returns the first 5 rows. This example uses the `SPARK_REMOTE` environment variable for authentication.

Scala

    import org.apache.spark.sql.{DataFrame, SparkSession}object Main {  def main(args: Array[String]): Unit = {    getTaxis(getSpark()).show(5)  }  private def getSpark(): SparkSession = {    SparkSession.builder().getOrCreate()  }  private def getTaxis(spark: SparkSession): DataFrame = {    spark.read.table("samples.nyctaxi.trips")  }}

## Additional resources[​](#additional-resources "Direct link to Additional resources")

Databricks provides additional example applications that show how to use Databricks Connect in the [Databricks Connect GitHub repository](https://github.com/databricks-demos/dbconnect-examples), including:

*   [A simple ETL application](https://github.com/databricks-demos/dbconnect-examples/tree/main/scala/ETL)
*   [Charts visualizations with JFreeChart](https://github.com/databricks-demos/dbconnect-examples/tree/main/scala/Charts)
