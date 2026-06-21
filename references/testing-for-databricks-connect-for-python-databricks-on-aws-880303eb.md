---
title: Testing for Databricks Connect for Python | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/testing
ingestedAt: "2026-06-18T08:06:23.836Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article describes how to run tests using `pytest` with Databricks Connect for Databricks Runtime 13.3 LTS and above. To install Databricks Connect for Python, see [Install Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install).

To get started with `pytest`, see [Get Started](https://docs.pytest.org/en/8.0.x/getting-started.html) in the `pytest` documentation.

note

When running Databricks Connect from the terminal, `pytest` only works with the DEFAULT configuration profile. The profile should include the Databricks compute you want to use, either a cluster or serverless compute. For information about configuring compute, see [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).

For example, given the following file named `nyctaxi_functions.py` containing a `get_spark` function that returns a `SparkSession` instance and a `get_nyctaxi_trips` function that returns a `DataFrame` representing the `trips` table in the `samples` catalog's `nyctaxi` schema:

`nyctaxi_functions.py`:

Python

    from databricks.connect import DatabricksSessionfrom pyspark.sql import DataFrame, SparkSessiondef get_spark() -> SparkSession:  spark = DatabricksSession.builder.getOrCreate()  return sparkdef get_nyctaxi_trips() -> DataFrame:  spark = get_spark()  df = spark.read.table("samples.nyctaxi.trips")  return df

And given the following file named `main.py` that calls these `get_spark` and `get_nyctaxi_trips` functions:

`main.py`:

Python

    from nyctaxi_functions import *df = get_nyctaxi_trips()df.show(5)

The following file named `test_nyctaxi_functions.py` tests whether the `get_spark` function returns a `SparkSession` instance and whether the `get_nyctaxi_trips` function returns a `DataFrame` that contains at least one row of data:

`test_nyctaxi_functions.py`:

Python

    import pyspark.sql.connect.sessionfrom nyctaxi_functions import *def test_get_spark():  spark = get_spark()  assert isinstance(spark, pyspark.sql.connect.session.SparkSession)def test_get_nyctaxi_trips():  df = get_nyctaxi_trips()  assert df.count() > 0

To run these tests, run the `pytest` command from the code project's root, which should produce test results similar to the following:

Bash

    $ pytest=================== test session starts ====================platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0rootdir: <project-rootdir>collected 2 itemstest_nyctaxi_functions.py .. [100%]======================== 2 passed ==========================
