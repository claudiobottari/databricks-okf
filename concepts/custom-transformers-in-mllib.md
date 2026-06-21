---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37b69e8fe4fafc73883e08d346cd74557bee7d87a1d3b252e7aebbb4caea7474
  pageDirectory: concepts
  sources:
    - use-apache-spark-mllib-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-transformers-in-mllib
    - CTIM
  citations:
    - file: use-apache-spark-mllib-on-databricks-databricks-on-aws.md
title: Custom Transformers in MLlib
description: The ability to create custom pipeline transformers in Apache Spark MLlib for domain-specific feature transformations.
tags:
  - machine-learning
  - mllib
  - transformers
timestamp: "2026-06-19T23:20:33.865Z"
---

## Custom Transformers in MLlib

**Custom Transformers** in [Apache Spark MLlib](/concepts/apache-spark-mllib.md) allow users to define their own transformation logic within an ML Pipeline. A transformer is an algorithm that transforms one DataFrame into another — for example, adding a new column by applying a user‑defined function. When the built‑in transformers provided by the `pyspark.ml` package are insufficient, a custom transformer can be implemented to encapsulate arbitrary preprocessing or feature engineering steps. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Creating a Custom Transformer

To create a custom transformer, a class must extend `pyspark.ml.Transformer` and implement the `_transform` method. The full API is documented in the official [Apache Spark MLlib](/concepts/apache-spark-mllib.md) Programming Guide](https://spark.apache.org/docs/latest/ml-guide.html) and the [Python API Reference](https://spark.apache.org/docs/latest/api/python/). Databricks recommends consulting those references for implementation details. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Databricks Example Notebook

Databricks provides an **Advanced [Apache Spark MLlib](/concepts/apache-spark-mllib.md) notebook example** that illustrates how to create a custom transformer. This notebook is part of the MLlib documentation on Databricks and can be used as a practical starting point for building custom transformers. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Compute Support

The `pyspark.ml` package, which includes custom transformers, is supported on serverless, standard, and dedicated compute on Databricks. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Related Concepts

- [ML Pipelines](/concepts/mllib-pipelines-api.md) – The framework that chains transformers and estimators.
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) – The machine learning library that provides the `Transformer` API.
- [Feature Engineering](/concepts/featureengineeringclient-api.md) – Common use case for custom transformers.
- pyspark.ml – The Python package containing the base classes for transformers.

### Sources

- use-apache-spark-mllib-on-databricks-databricks-on-aws.md

# Citations

1. [use-apache-spark-mllib-on-databricks-databricks-on-aws.md](/references/use-apache-spark-mllib-on-databricks-databricks-on-aws-545482f3.md)
