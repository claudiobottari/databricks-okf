---
title: Limitations with Databricks Connect for Scala | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/limitations
ingestedAt: "2026-06-18T08:06:46.260Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article lists limitations with Databricks Connect for Scala. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks compute resources. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/). For the Python version of this article, see [Limitations with Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/limitations).

important

Depending on the version of Scala, Java, Databricks Runtime, and Databricks Connect that you are using, there may be version requirements for some features. See [Requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install#requirements).

## Feature availability[​](#feature-availability "Direct link to Feature availability")

Not available on Databricks Connect for Databricks Runtime 13.3 LTS and below:

*   Streaming `foreachBatch`
*   Creating DataFrames with an unresolved logical plan larger than 128 MB. This limit applies to the plan size, not the data itself.
*   Long queries over 3600 seconds
*   Scalar UDFs on compute resources that use dedicated access mode (formerly single user)

Not available:

*   Databricks Utilities: `credentials`, `library`, `notebook workflow`, `widgets`
*   Spark Context
*   RDDs
*   `CREATE TABLE <table-name> AS SELECT` (instead, use `spark.sql("SELECT ...").write.saveAsTable("table")`)
*   Changing the log4j log level through `SparkContext`
*   Distributed ML training
*   Synchronizing the local development environment with the remote compute resource
