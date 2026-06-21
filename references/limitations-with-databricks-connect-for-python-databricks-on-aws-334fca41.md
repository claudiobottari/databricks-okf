---
title: Limitations with Databricks Connect for Python | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/limitations
ingestedAt: "2026-06-18T08:06:19.209Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article lists limitations with Databricks Connect for Python. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/). For the Scala version of this article, see [Limitations with Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/limitations).

important

Depending on the version of Python, Databricks Runtime, and Databricks Connect that you are using, there may be version requirements for some features. See [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).

## Feature availability[​](#feature-availability "Direct link to Feature availability")

Not available on Databricks Connect for Databricks Runtime 13.3 LTS and below:

*   Streaming `foreachBatch`
*   Creating DataFrames with an unresolved logical plan larger than 128 MB. This limit applies to the plan size, not the data itself.
*   Long queries over 3600 seconds

Not available on Databricks Connect for Databricks Runtime 15.3 and below:

*   `ApplyinPandas()` and `Cogroup()` with compute with standard access mode

Not available on Databricks Connect for Databricks Runtime 16.3 and below:

*   On serverless compute, UDFs cannot include custom libraries.

Not available:

*   `dataframe.display()` API
*   Databricks Utilities: `credentials`, `library`, `notebook workflow`, `widgets`
*   Spark Context
*   RDDs
*   Libraries that use RDDs, Spark Context, or access the underlying Spark JVM, such as Mosaic geospatial, GraphFrames, or GreatExpectations
*   `CREATE TABLE <table-name> AS SELECT` (instead, use `spark.sql("SELECT ...").write.saveAsTable("table")`)
*   Changing the log4j log level through `SparkContext`
*   Distributed ML training is not supported.
*   Synchronizing the local development environment with the remote cluster
