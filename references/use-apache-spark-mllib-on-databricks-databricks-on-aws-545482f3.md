---
title: Use Apache Spark MLlib on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/mllib
ingestedAt: "2026-06-18T08:13:31.859Z"
---

This page provides example notebooks showing how to use MLlib on Databricks.

Apache Spark MLlib is the Apache Spark machine learning library consisting of common learning algorithms and utilities, including classification, regression, clustering, collaborative filtering, dimensionality reduction, and underlying optimization primitives. For reference information about MLlib features, Databricks recommends the following Apache Spark API references:

*   [MLlib Programming Guide](https://spark.apache.org/docs/latest/ml-guide.html)
*   [Python API Reference](https://spark.apache.org/docs/latest/api/python/)
*   [Scala API Reference](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html)
*   [Java API](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)

The `pyspark.ml` package from Apache Spark MLlib is supported on serverless, standard, and dedicated compute.

For information about using Apache Spark MLlib from R, see the [R machine learning](https://docs.databricks.com/aws/en/sparkr/overview#r-ml) documentation.

## Binary classification example notebook[​](#binary-classification-example-notebook "Direct link to Binary classification example notebook")

This notebook shows you how to build a binary classification application using the Apache Spark MLlib Pipelines API.

#### Binary classification notebook

## Decision trees example notebooks[​](#decision-trees-example-notebooks "Direct link to Decision trees example notebooks")

These examples demonstrate various applications of decision trees using the Apache Spark MLlib Pipelines API.

### Decision trees[​](#decision-trees "Direct link to Decision trees")

These notebooks show you how to perform classifications with decision trees.

#### Decision trees for digit recognition notebook

#### Decision trees for SFO survey notebook

### GBT regression using MLlib pipelines[​](#gbt-regression-using-mllib-pipelines "Direct link to GBT regression using MLlib pipelines")

This notebook shows you how to use MLlib pipelines to perform a regression using gradient boosted trees to predict bike rental counts (per hour) from information such as day of the week, weather, season, and so on.

#### Bike sharing regression notebook

## Advanced Apache Spark MLlib notebook example[​](#advanced-apache-spark-mllib-notebook-example "Direct link to advanced-apache-spark-mllib-notebook-example")

This notebook illustrates how to create a custom transformer.

#### Custom transformer notebook
