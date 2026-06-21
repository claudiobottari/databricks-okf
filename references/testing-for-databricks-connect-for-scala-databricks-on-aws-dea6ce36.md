---
title: Testing for Databricks Connect for Scala | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/testing
ingestedAt: "2026-06-18T08:06:49.928Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article describes how to run tests using ScalaTest with Databricks Connect for Databricks Runtime 13.3 LTS and above. To install Databricks Connect for Scala, see [Install Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install).

To get started with ScalaTest and run it locally, see [Getting started](https://www.scalatest.org/user_guide) in the ScalaTest documentation.

For example, given the following file `src/main/scala/NYCTaxiFunctions.scala` containing a `getSpark` function that returns a `SparkSession` instance and a `getTaxis` function that returns a `DataFrame` representing the `trips` table in the `samples` catalog's `nyctaxi` schema:

`NYCTaxiFunctions.scala`:

Scala

    package org.example.applicationimport com.databricks.connect.DatabricksSessionimport org.apache.spark.sql.{DataFrame, SparkSession}class NYCTaxiFunctions {  def getSpark: SparkSession = {    DatabricksSession.builder().getOrCreate()  }  def getTaxis: DataFrame = {    val spark = getSpark    spark.read.table("samples.nyctaxi.trips")  }}

And given the following file `src/main/scala/Main.scala` that calls these `getSpark` and `getTaxis` functions:

`Main.scala`:

Scala

    package org.example.applicationobject Main {  def main(args: Array[String]): Unit = {    val nycTaxiFunctions = new NYCTaxiFunctions()    val df = nycTaxiFunctions.getTaxis    df.show(5)  }}

The following file `src/test/scala/NYCTaxiFunctionsTest.scala` tests whether the `getSpark` function returns a `SparkSession` instance and whether the `getTaxis` function returns a `DataFrame` that contains at least one row of data:

`NYCTaxiFunctionsTest.scala`:

Scala

    package org.example.applicationimport org.apache.spark.sql.SparkSessionimport org.scalatest.flatspec.AnyFlatSpecimport org.scalatest.matchers.should.Matchersclass SparkSessionTypeTest extends AnyFlatSpec with Matchers {  "The session" should "be of type SparkSession" in {    val nycTaxiFunctions = new NYCTaxiFunctions()    val spark = nycTaxiFunctions.getSpark    spark shouldBe a [SparkSession]  }}class GetTaxisRowCountTest extends AnyFlatSpec with Matchers {  "The DataFrame" should "have at least one row" in {    val nycTaxiFunctions = new NYCTaxiFunctions()    val df = nycTaxiFunctions.getTaxis    df.count() should be > (0L)  }}

To run these tests, see [ScalaTest quick start](https://www.scalatest.org/quick_start) or your IDE's documentation. For example, for IntelliJ IDEA, see [Test Scala applications](https://www.jetbrains.com/help/idea/run-debug-and-test-scala.html#test_scala_app) in the IntelliJ IDEA documentation.
