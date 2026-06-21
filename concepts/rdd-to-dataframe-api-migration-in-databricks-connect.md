---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4afdccb70fc75f8b99dc38d4ee8eb2f4ad547f62ca5fc8ffcfc55512ac738c27
  pageDirectory: concepts
  sources:
    - migrate-to-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rdd-to-dataframe-api-migration-in-databricks-connect
    - RTDAMIDC
  citations:
    - file: migrate-to-databricks-connect-for-python-databricks-on-aws.md
      start: 23
      end: 24
    - file: migrate-to-databricks-connect-for-python-databricks-on-aws.md
      start: 20
      end: 22
    - file: migrate-to-databricks-connect-for-python-databricks-on-aws.md
      start: 28
      end: 31
title: RDD to DataFrame API Migration in Databricks Connect
description: The migration from RDD APIs to DataFrame APIs required when upgrading Databricks Connect, as RDD and SparkContext usage must be replaced.
tags:
  - databricks
  - api-migration
  - python
  - spark
timestamp: "2026-06-19T19:34:50.980Z"
---

# RDD to DataFrame API Migration in Databricks Connect

**RDD to DataFrame API Migration in Databricks Connect** refers to the process of transitioning existing PySpark code that uses Resilient Distributed Datasets (RDDs) to use DataFrame APIs when migrating from Databricks Connect for Databricks Runtime 12.2 LTS and below to Databricks Connect for Databricks Runtime 13.3 LTS and above.

## Overview

When migrating to Databricks Connect for Databricks Runtime 13.3 LTS and above, users must migrate their RDD APIs to use DataFrame APIs and migrate their `SparkContext` to use alternatives.^[migrate-to-databricks-connect-for-python-databricks-on-aws.md#L23-L24] This change is necessary because [Databricks Connect](/concepts/databricks-connect.md) for newer runtime versions has different requirements for how client connections interact with the remote Spark cluster.

## Migration Steps

### Initialize the Spark Session

After upgrading the Databricks Connect client, update Python code to initialize the `spark` variable using `DatabricksSession` instead of the traditional SparkSession initialization used with PySpark.^[migrate-to-databricks-connect-for-python-databricks-on-aws.md#L20-L22] See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) for details on cluster configuration.

### Replace RDD Operations

Convert existing RDD-based operations to their DataFrame equivalents. Common replacements include:

- **RDD transformations** (`map`, `filter`, `flatMap`, `reduceByKey`) should be replaced with [DataFrame transformations](/concepts/remote-dataframe-operations.md) (`select`, `filter`, `groupBy`, `agg`)
- **RDD actions** (`collect`, `count`, `take`, `saveAsTextFile`) should be replaced with [DataFrame actions](/concepts/remote-dataframe-operations.md) (`collect`, `count`, `show`, `write`)
- **Pair RDD operations** (`groupByKey`, `reduceByKey`, `join`) should be replaced with DataFrame join and aggregation operations

### Replace SparkContext Usage

Migrate any code that directly uses `SparkContext` to use alternatives available through the [DatabricksSession](/concepts/databrickssession.md) or `SparkSession` APIs.^[migrate-to-databricks-connect-for-python-databricks-on-aws.md#L23-L24] This includes:

- Setting Hadoop configuration properties
- Accessing broadcast variables and [accumulators](/concepts/gradient-accumulation-fusion.md)
- Working with Spark configuration settings

## Setting Hadoop Configurations

On the client, Hadoop configurations can be set using the `spark.conf.set` API, which applies to SQL and DataFrame operations.^[migrate-to-databricks-connect-for-python-databricks-on-aws.md#L28-L31] However, Hadoop configurations set on `sparkContext` that are not related to user sessions must be set in the cluster configuration or using a notebook, because `sparkContext` configurations apply to the entire cluster rather than individual user sessions.^[migrate-to-databricks-connect-for-python-databricks-on-aws.md#L28-L31]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that connects IDEs and custom applications to Databricks clusters
- PySpark Migration — General guidance for migrating PySpark code between runtime versions
- DataFrame vs RDD Performance — Performance considerations when choosing between APIs
- [SparkSession Initialization](/concepts/databrickssession-initialization-for-authentication.md) — Setting up the Spark session in modern Databricks Connect
- Databricks Runtime Migration — Comprehensive guidance for migrating between Databricks Runtime versions

## Sources

- migrate-to-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [migrate-to-databricks-connect-for-python-databricks-on-aws.md:23-24](/references/migrate-to-databricks-connect-for-python-databricks-on-aws-5b63ea6f.md)
2. [migrate-to-databricks-connect-for-python-databricks-on-aws.md:20-22](/references/migrate-to-databricks-connect-for-python-databricks-on-aws-5b63ea6f.md)
3. [migrate-to-databricks-connect-for-python-databricks-on-aws.md:28-31](/references/migrate-to-databricks-connect-for-python-databricks-on-aws-5b63ea6f.md)
