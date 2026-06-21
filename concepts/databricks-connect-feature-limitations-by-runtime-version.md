---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51332079a07fc264669e0ceaa9536d75c7ce7c473cf681e848527e621898a64a
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-feature-limitations-by-runtime-version
    - DCFLBRV
  citations:
    - file: limitations-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect Feature Limitations by Runtime Version
description: Databricks Connect functionality is gated by Databricks Runtime version, with certain features unavailable depending on the runtime version (13.3 LTS, 15.3, 16.3).
tags:
  - databricks
  - limitations
  - compatibility
timestamp: "2026-06-19T19:12:08.980Z"
---

# Databricks Connect Feature Limitations by Runtime Version

**Databricks Connect Feature Limitations by Runtime Version** documents the specific features that are unavailable or restricted when using [Databricks Connect](/concepts/databricks-connect.md) for [Python](/concepts/python-wheel-task.md) with different Databricks Runtime versions. These limitations vary by runtime version and affect development workflows.

## Feature Availability by Runtime Version

### Databricks Runtime 13.3 LTS and Below

The following features are not available when using Databricks Connect with Databricks Runtime 13.3 LTS and below:

- [Streaming foreachBatch](/concepts/streaming-upserts-with-foreachbatch-and-merge.md) operations
- Creating DataFrames with an unresolved logical plan larger than 128 MB (this limit applies to the plan size, not the data itself)
- Long queries exceeding 3600 seconds (1 hour)^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

### Databricks Runtime 15.3 and Below

The following features are not available when using Databricks Connect with Databricks Runtime 15.3 and below:

- `ApplyInPandas()` and `Cogroup()` operations on Compute configured with [Standard Access Mode](/concepts/standard-access-mode.md)^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

### Databricks Runtime 16.3 and Below

The following feature is not available when using Databricks Connect with Databricks Runtime 16.3 and below:

- User-Defined Functions (UDFs) that include custom libraries when running on Serverless Compute^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Permanently Unavailable Features

The following features are not available in any supported version of Databricks Connect:

- `dataframe.display()` API
- Databricks Utilities: `credentials`, `library`, `notebook workflow`, `widgets`
- Spark Context
- RDDs (Resilient Distributed Datasets)
- Libraries that use RDDs, Spark Context, or access the underlying Spark JVM, such as Mosaic geospatial, [GraphFrames](/concepts/graphframes.md), or GreatExpectations
- `CREATE TABLE <table-name> AS SELECT` (use `spark.sql("SELECT ...").write.saveAsTable("table")` instead)^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Changing the log4j log level through `SparkContext`^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- [Distributed ML Training](/concepts/workload-yaml-for-distributed-training.md) is not supported^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]
- Synchronizing the local development environment with the remote cluster^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Version Requirements

Depending on the version of Python, Databricks Runtime, and Databricks Connect being used, there may be additional version requirements for some features. See [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) for details.^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- [Databricks Runtime Compatibility](/concepts/databricks-runtime-compatibility.md)
- IDEs and Remote Development on Databricks

## Sources

- limitations-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-python-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-python-databricks-on-aws-334fca41.md)
