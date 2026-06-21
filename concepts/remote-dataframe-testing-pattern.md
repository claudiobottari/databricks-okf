---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56e212649bad553448d49f70519471024224e280bc774f8e3701c32c7de3cbd1
  pageDirectory: concepts
  sources:
    - testing-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - remote-dataframe-testing-pattern
    - RDTP
  citations:
    - file: testing-for-databricks-connect-for-python-databricks-on-aws.md
title: Remote DataFrame Testing Pattern
description: A testing pattern where PySpark DataFrame operations (like count, show) execute on remote Databricks compute, and tests assert on results using standard pytest assertions.
tags:
  - databricks
  - testing
  - pyspark
  - pattern
timestamp: "2026-06-19T23:06:43.424Z"
---

# Remote DataFrame Testing Pattern

The **Remote DataFrame Testing Pattern** is a testing approach that uses pytest with [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) to validate PySpark DataFrame operations against a remote Databricks cluster or serverless compute environment. This pattern enables developers to write and run tests that execute Spark operations on a remote compute target rather than requiring a local Spark installation. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Overview

When developing PySpark applications that interact with data on Databricks, developers need a reliable way to verify that their functions return correct results. The Remote DataFrame Testing Pattern provides this capability by connecting to a remote Databricks compute resource through the [Databricks Connect](/concepts/databricks-connect.md) library, allowing test frameworks like pytest to run Spark operations remotely. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

This pattern is particularly valuable for testing data transformation logic, table reads, and DataFrame operations without needing to deploy code to a cluster first. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Requirements

To use the Remote DataFrame Testing Pattern, the following requirements must be met:

- [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) or above
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) installed
- A configured Databricks compute target (cluster or serverless compute)
- pytest installed

^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

### Configuration Profile

When running pytest from the terminal, it only works with the **DEFAULT** configuration profile. This profile must include the Databricks compute resource you want to use for testing. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Implementation

The pattern follows a standard structure where test files import and call functions that use [DatabricksSession](/concepts/databrickssession.md) to create a SparkSession and perform DataFrame operations. The tests then assert on the results of those operations. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

### Example Test Structure

Given a module `nyctaxi_functions.py` defining functions that use [Databricks Connect](/concepts/databricks-connect.md):

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

^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

A corresponding test file `test_nyctaxi_functions.py` validates these functions:

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

^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

### Running Tests

Tests are executed by running the `pytest` command from the project's root directory:

```bash
pytest
```

This produces output similar to:

```
=================== test session starts ====================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: <project-rootdir>
collected 2 items

test_nyctaxi_functions.py .. [100%]

======================== 2 passed ==========================
```

^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Best Practices

- Organize test files using standard pytest conventions with filenames prefixed with `test_`. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]
- Test both that functions return the correct types (e.g., `SparkSession` or `DataFrame`) and that they return non-empty or valid results. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]
- Ensure the DEFAULT configuration profile is properly configured with the target compute resource before running tests. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The library that enables remote Spark execution
- [DatabricksSession](/concepts/databrickssession.md) — The entry point for creating a remote Spark session
- SparkSession — The unified entry point for Spark functionality
- pytest — The testing framework used with this pattern
- DataFrame Testing Strategies — Broader approaches to testing DataFrame operations
- Remote Spark Execution — The general concept of running Spark operations on remote compute

## Sources

- testing-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [testing-for-databricks-connect-for-python-databricks-on-aws.md](/references/testing-for-databricks-connect-for-python-databricks-on-aws-880303eb.md)
