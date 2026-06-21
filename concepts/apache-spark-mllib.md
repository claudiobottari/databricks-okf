---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 61dd436167e6cdb35c4f9cc655ddad2f26357d205d7855ba64b7271ad683ca69
  pageDirectory: concepts
  sources:
    - use-apache-spark-mllib-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apache-spark-mllib
    - ASM
    - Apache Spark's MLlib
    - PySpark MLlib
    - Spark MLlib
  citations:
    - file: use-apache-spark-mllib-on-databricks-databricks-on-aws.md
title: Apache Spark MLlib
description: The scalable machine learning library in Apache Spark, providing common algorithms for classification, regression, clustering, collaborative filtering, dimensionality reduction, and optimization primitives.
tags:
  - machine-learning
  - apache-spark
  - big-data
timestamp: "2026-06-19T23:20:16.122Z"
---

# Apache Spark MLlib

**Apache Spark MLlib** is the machine learning library built into Apache Spark, providing a collection of common learning algorithms and utilities for large-scale data processing. It includes tools for classification, regression, clustering, collaborative filtering, dimensionality reduction, and underlying optimization primitives. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Overview

MLlib is designed to work natively with Spark's distributed computing framework, enabling machine learning workflows to scale across clusters. The library provides a high-level [ML Pipelines API](/concepts/mllib-pipelines-api.md) that allows users to construct and tune practical machine learning pipelines. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

The `pyspark.ml` package from Apache Spark MLlib is supported on serverless, standard, and dedicated compute environments. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Key Capabilities

MLlib covers a broad range of machine learning tasks:

- **Classification** — Including binary classification and decision tree-based classifiers
- **Regression** — Including gradient boosted tree (GBT) regression
- **Clustering**
- **Collaborative filtering**
- **Dimensionality reduction**
- **Feature transformers and custom transformers**

## API References

For detailed reference information about MLlib features, Databricks recommends the following Apache Spark API references: ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

- [MLlib Programming Guide](https://spark.apache.org/docs/latest/ml-guide.html)
- [Python API Reference](https://spark.apache.org/docs/latest/api/python/)
- [Scala API Reference](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html)
- [Java API](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)

For information about using Apache Spark MLlib from R, see the R machine learning documentation. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Example Applications

MLlib includes example notebooks demonstrating common use cases: ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

- **Binary classification** — Building a binary classification application using the [MLlib Pipelines API](/concepts/mllib-pipelines-api.md)
- **Decision trees** — Performing classifications with decision trees, including digit recognition and survey data analysis
- **GBT regression** — Using gradient boosted trees to predict bike rental counts based on features such as day of the week, weather, and season
- **Custom transformers** — Creating custom transformer components for specialized preprocessing

## Related Concepts

- Apache Spark — The distributed computing framework underlying MLlib
- [ML Pipelines API](/concepts/mllib-pipelines-api.md) — The high-level API for constructing machine learning workflows
- PySpark ML — The Python interface to MLlib
- Databricks Machine Learning — The platform environment for running MLlib workloads
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Scaling machine learning across clusters

## Sources

- use-apache-spark-mllib-on-databricks-databricks-on-aws.md

# Citations

1. [use-apache-spark-mllib-on-databricks-databricks-on-aws.md](/references/use-apache-spark-mllib-on-databricks-databricks-on-aws-545482f3.md)
