---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f0e131128c8aac8eecf24cd88a37896b9174d2a5263dc5bb985893700008f533
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-unsupported-apis-and-libraries
    - Libraries and Databricks Connect Unsupported APIs
    - DCUAAL
  citations:
    - file: limitations-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect Unsupported APIs and Libraries
description: Several Spark APIs and third-party libraries are unsupported in Databricks Connect, including RDDs, Spark Context, data frame display, certain Databricks Utilities, and libraries like Mosaic, GraphFrames, and GreatExpectations.
tags:
  - databricks
  - limitations
  - api-compatibility
timestamp: "2026-06-19T19:12:39.565Z"
---

# Databricks Connect Unsupported APIs and Libraries

**Databricks Connect Unsupported APIs and Libraries** refers to the set of Apache Spark APIs, Databricks-specific utilities, and third-party libraries that are not compatible with [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) when connecting a local development environment to a remote Databricks cluster. These limitations apply to both serverless compute and classic compute configurations, depending on the Databricks Runtime version in use. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Permanently Unsupported Features

The following APIs and libraries are not supported in any version of Databricks Connect:

- `dataframe.display()` API ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Databricks Utilities: `credentials`, `library`, `notebook workflow`, `widgets` ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Spark Context ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- RDDs (Resilient Distributed Datasets) ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Libraries that use RDDs, Spark Context, or access the underlying Spark JVM, such as Mosaic geospatial, [GraphFrames](/concepts/graphframes.md), or GreatExpectations ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- `CREATE TABLE <table-name> AS SELECT` (instead, use `spark.sql("SELECT ...").write.saveAsTable("table")`) ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Changing the log4j log level through `SparkContext` ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Distributed ML training ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Synchronizing the local development environment with the remote cluster ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Version-Specific Limitations

### Databricks Runtime 13.3 LTS and Below

The following features are not available when using Databricks Connect with Databricks Runtime 13.3 LTS or earlier:

- Streaming `foreachBatch` ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Creating DataFrames with an unresolved logical plan larger than 128 MB. This limit applies to the plan size, not the data itself. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Long queries over 3600 seconds ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

### Databricks Runtime 15.3 and Below

The following features are not available when using Databricks Connect with Databricks Runtime 15.3 or earlier:

- `ApplyinPandas()` and `Cogroup()` with compute using standard access mode ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

### Databricks Runtime 16.3 and Below

The following limitation applies when using Databricks Connect with Databricks Runtime 16.3 or earlier:

- On serverless compute, UDFs cannot include custom libraries. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Workarounds

For the `CREATE TABLE <table-name> AS SELECT` limitation, use the alternative approach:

```python
spark.sql("SELECT ...").write.saveAsTable("table")
```

^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The client library that enables connecting local environments to Databricks clusters.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The Scala version of the client, with its own limitations.
- Databricks Runtime Versions — Understanding version-specific feature availability.
- Apache Spark DataFrame API — The primary API supported by Databricks Connect.
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) — User-defined functions that have version-dependent support.

## Sources

- limitations-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-python-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-python-databricks-on-aws-334fca41.md)
