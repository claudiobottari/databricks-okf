---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e608526417a2e4137c773d29dac0c9ad91aa53c257fccf97ef24d5aebf00020
  pageDirectory: concepts
  sources:
    - testing-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-testing-with-pytest
    - DCTWP
  citations:
    - file: testing-for-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect Testing with pytest
description: How to write and run pytest tests for PySpark code using Databricks Connect, where tests execute on a remote Databricks cluster or serverless compute.
tags:
  - databricks
  - testing
  - pytest
  - pyspark
timestamp: "2026-06-19T23:06:26.423Z"
---

# [Databricks Connect](/concepts/databricks-connect.md) Testing with pytest

**Databricks Connect Testing with pytest** describes how to run unit and integration tests against [Databricks Connect](/concepts/databricks-connect.md) for Python ([Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) and above) using the `pytest` framework. It allows developers to validate Spark code locally while the actual execution happens on a remote Databricks compute resource (cluster or serverless compute). ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Prerequisites

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) must be installed. See [Install Databricks Connect for Python](/concepts/databricks-connect-for-python.md).
- When running `pytest` from the terminal, it only works with the **DEFAULT** configuration profile. The profile must include the Databricks compute you want to use (either a cluster or serverless compute). For configuration details, see [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Example Test Files

The following example consists of three files: a module of helper functions (`nyctaxi_functions.py`), an application entry point (`main.py`), and a test suite (`test_nyctaxi_functions.py`).

**`nyctaxi_functions.py`** creates a `SparkSession` using `DatabricksSession.builder.getOrCreate()` and returns a `DataFrame` from the `samples.nyctaxi.trips` table: ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from pyspark.sql import DataFrame, SparkSession

def get_spark() -> SparkSession:
  spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
  return spark

def get_nyctaxi_trips() -> DataFrame:
  spark = get_spark()
  df = spark.read.table("samples.nyctaxi.trips")
  return df
```

**`main.py`** consumes the functions and displays the first five rows: ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from nyctaxi_functions import *

df = get_nyctaxi_trips()
df.show(5)
```

**`test_nyctaxi_functions.py`** contains two test functions. The first verifies that `get_spark()` returns an instance of `pyspark.sql.connect.session.SparkSession`. The second checks that the returned `DataFrame` has at least one row: ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

```python
import pyspark.sql.connect.session
from nyctaxi_functions import *

def test_get_spark():
  spark = get_spark()
  assert isinstance(spark, pyspark.sql.connect.session.SparkSession)

def test_get_nyctaxi_trips():
  df = get_nyctaxi_trips()
  assert df.count() > 0
```

## Running Tests

From the root of the code project, run the `pytest` command: ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

```bash
pytest
```

Expected output showing two passed tests:

```
=================== test session starts ====================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: <project-rootdir>
collected 2 items

test_nyctaxi_functions.py .. [100%]
======================== 2 passed ==========================
```

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- pytest
- [DatabricksSession](/concepts/databrickssession.md)
- SparkSession
- DataFrame (PySpark)
- DEFAULT configuration profile
- Databricks cluster

## Sources

- testing-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [testing-for-databricks-connect-for-python-databricks-on-aws.md](/references/testing-for-databricks-connect-for-python-databricks-on-aws-880303eb.md)
