---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfece789fd5a67cc7e25bfbb5a9239ea034c14ebb900480109a23980f4e9498e
  pageDirectory: concepts
  sources:
    - use-apache-spark-mllib-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mllib-pipelines-api
    - MPA
    - ML Pipelines API
    - MLlib Pipeline
    - MLlib Pipelines
    - MLlib pipeline
    - ML Pipelines
    - MLlib ML Pipeline
    - Pipeline
    - Pipelines API
    - PySpark ML Pipeline
    - PySpark ML Pipelines
    - Spark ML Pipeline
    - Spark ML Pipelines
    - Spark ML pipelines
    - Spark MLlib pipeline
    - SparkML Pipelines
  citations:
    - file: use-apache-spark-mllib-on-databricks-databricks-on-aws.md
title: MLlib Pipelines API
description: A high-level API in Apache Spark MLlib for constructing and tuning machine learning workflows as composable pipeline stages.
tags:
  - machine-learning
  - apache-spark
  - pipelines
timestamp: "2026-06-19T23:20:24.293Z"
---

# MLlib Pipelines API

The **MLlib Pipelines API** is the high‑level, DataFrame‑based API within [Apache Spark MLlib](/concepts/apache-spark-mllib.md), the Apache Spark machine learning library. It provides a uniform set of tools for building and tuning machine learning pipelines, including transformers, estimators, and evaluators. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Overview

MLlib consists of common learning algorithms and utilities such as classification, regression, clustering, collaborative filtering, dimensionality reduction, and underlying optimization primitives. The Pipelines API builds on these algorithms by offering a consistent interface for assembling data preprocessing, feature extraction, model training, and evaluation into a single workflow. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Usage on Databricks

The `pyspark.ml` package from [Apache Spark MLlib](/concepts/apache-spark-mllib.md) is supported on all Databricks compute types: **serverless**, **standard**, and **dedicated** compute. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

Databricks provides example notebooks that demonstrate the Pipelines API in action:

- **Binary classification** – Building a binary classification application using the Pipelines API.
- **Decision trees** – Performing classification with decision trees (e.g., digit recognition, SFO survey data).
- **Gradient‑boosted tree (GBT) regression** – Using MLlib pipelines to predict bike rental counts per hour from features such as day of week, weather, and season.
- **Custom transformer** – Creating a custom transformer to extend the Pipelines API.

These notebooks are available in the Databricks documentation and show how to apply the Pipelines API to real‑world problems. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Reference Documentation

For a full description of the MLlib Pipelines API, Databricks recommends the following Apache Spark references:

- MLlib Programming Guide
- Python API Reference (`pyspark.ml`)
- Scala API Reference (`org.apache.spark.ml`)
- Java API (`org.apache.spark.ml`)

For using MLlib from R, see the R machine learning documentation. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) – The underlying machine learning library that the Pipelines API builds upon.
- [MLlib Pipelines](/concepts/mllib-pipelines-api.md) – The core concept of chaining transformers and estimators.
- Binary Classification – A common task demonstrated with the Pipelines API.
- Decision Trees – A model type supported in the Pipelines API.
- [Gradient Boosted Trees (GBT)](/concepts/gradient-boosted-trees-regression-with-mllib.md) – An ensemble method available via the Pipelines API.
- Custom Transformer – Extending the Pipelines API with user‑defined logic.

## Sources

- use-apache-spark-mllib-on-databricks-databricks-on-aws.md

# Citations

1. [use-apache-spark-mllib-on-databricks-databricks-on-aws.md](/references/use-apache-spark-mllib-on-databricks-databricks-on-aws-545482f3.md)
