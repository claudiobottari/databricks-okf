---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 221c2218685639401e7c6d2284c6164e851330467ca7ee3a3cc1923db406660d
  pageDirectory: concepts
  sources:
    - use-apache-spark-mllib-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mllib-support
    - DMS
    - Databricks Support
    - Databricks support
  citations:
    - file: use-apache-spark-mllib-on-databricks-databricks-on-aws.md
title: Databricks MLlib Support
description: Databricks supports Apache Spark MLlib on serverless, standard, and dedicated compute, with integration for Python, Scala, Java, and R.
tags:
  - databricks
  - mllib
  - compute
timestamp: "2026-06-19T23:20:25.168Z"
---

# Databricks MLlib Support

**Apache Spark MLlib** is the machine learning library built on top of Apache Spark. It provides common learning algorithms and utilities, including classification, regression, clustering, collaborative filtering, dimensionality reduction, and underlying optimization primitives. On Databricks, MLlib is fully supported and can be used across serverless, standard, and dedicated compute clusters. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Supported APIs

The primary API for using MLlib on Databricks is `pyspark.ml` from the Python package. Databricks recommends consulting the official Apache Spark references for detailed information:

- [MLlib Programming Guide](https://spark.apache.org/docs/latest/ml-guide.html)
- [Python API Reference](https://spark.apache.org/docs/latest/api/python/)
- [Scala API Reference](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html)
- [Java API Reference](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)

For R users, see the R machine learning documentation on Databricks. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Example Notebooks

Databricks provides several example notebooks demonstrating MLlib pipelines:

### Binary Classification

A notebook showing how to build a binary classification application using the [MLlib Pipelines API](/concepts/mllib-pipelines-api.md). ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Decision Trees

Example notebooks for classification with decision trees, including digit recognition and SFO survey data. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Gradient Boosted Tree (GBT) Regression

A notebook using MLlib pipelines to predict bike rental counts per hour from features such as day of week, weather, and season. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Custom Transformer

An advanced notebook that illustrates how to create a custom transformer using the MLlib API. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Related Concepts

- Apache Spark – The distributed computing framework underlying MLlib.
- PySpark – The Python API for Spark, which includes `pyspark.ml`.
- [Machine Learning Pipelines](/concepts/mlops-machine-learning-operations.md) – The API pattern used in the example notebooks.
- Databricks Compute Types – Serverless, standard, and dedicated compute supported for MLlib.

## Sources

- use-apache-spark-mllib-on-databricks-databricks-on-aws.md

# Citations

1. [use-apache-spark-mllib-on-databricks-databricks-on-aws.md](/references/use-apache-spark-mllib-on-databricks-databricks-on-aws-545482f3.md)
