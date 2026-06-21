---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9904d35cddf87966e0ae751197dbd973130060241da7ef52ba2a5b49e5dccb36
  pageDirectory: concepts
  sources:
    - testing-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession
    - Databricks Session
    - DatabricksSession create()
    - Spark Session
  citations:
    - file: testing-for-databricks-connect-for-python-databricks-on-aws.md
title: DatabricksSession
description: The primary entry point for creating a SparkSession when using Databricks Connect, bridging local Python code to a remote Databricks compute environment.
tags:
  - databricks
  - pyspark
  - api
timestamp: "2026-06-19T23:06:42.540Z"
---

```yaml
---
title: DatabricksSession
summary: The primary entry point for [[databricks-connect-for-python|Databricks Connect for Python]], used to create a Spark session that connects to a remote Databricks cluster. This page focuses on testing with pytest.
sources:
  - testing-for-databricks-connect-for-python-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - databricks
  - python
  - spark
  - connectivity
  - testing
aliases:
  - databrickssession
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# DatabricksSession

**DatabricksSession** is the primary entry-point class in [[Databricks Connect]] for Python ([[databricks-runtime-133-lts|Databricks Runtime 13.3 LTS]] and above). It replaces or wraps SparkSession to provide a connection to a remote Databricks cluster from local development environments such as an IDE or terminal. All Spark execution is offloaded to the remote cluster. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Basic Usage

A `SparkSession` instance is obtained by calling `DatabricksSession.builder.getOrCreate()`. The following example reads the `samples.nyctaxi.trips` table:

```python
from databricks.connect import DatabricksSession
from pyspark.sql import DataFrame, SparkSession

def get_spark() -> SparkSession:
    spark = DatabricksSession.builder.getOrCreate()
    return spark

def get_nyctaxi_trips() -> DataFrame:
    spark = get_spark()
    df = spark.read.table("samples.nyctaxi.trips")
    return df
```

^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Testing with pytest

[[databricks-connect-for-python|Databricks Connect for Python]] supports testing with `pytest`. When running tests from the terminal, `pytest` works only with the **DEFAULT** configuration profile. The profile must include the Databricks compute you want to use (a cluster or serverless compute). For configuration details, see the [[[compute-configuration-for-databricks-connect|Compute configuration for Databricks Connect]]](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config) documentation. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

### Example Test File

Given the functions defined above in `nyctaxi_functions.py`, the following test file `test_nyctaxi_functions.py` validates that `get_spark` returns a `SparkSession` instance and that `get_nyctaxi_trips` returns a non-empty DataFrame:

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

Run the tests with `pytest` from the project root:

```bash
$ pytest
=================== test session starts ====================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: <project-rootdir>
collected 2 items
test_nyctaxi_functions.py .. [100%]
======================== 2 passed ==========================
```

^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

## Requirements

- [Databricks Connect](/concepts/databricks-connect.md) for [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) and above.
- The `pytest` framework (see [pytest documentation](https://docs.pytest.org/en/8.0.x/getting-started.html) for installation).

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The framework that DatabricksSession is part of
- SparkSession – The Apache Spark session that DatabricksSession replaces
- [Databricks Configuration Profiles](/concepts/databricks-configuration-profiles.md) – Authentication configuration for Databricks tools
- Serverless Compute – Running DatabricksSession against serverless compute

## Sources

- testing-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [testing-for-databricks-connect-for-python-databricks-on-aws.md](/references/testing-for-databricks-connect-for-python-databricks-on-aws-880303eb.md)
