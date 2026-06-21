---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04a1c95f460074ccb803e17c60a6c40bcbafa4b49013700e48c6d7b2e8bb9fad
  pageDirectory: concepts
  sources:
    - troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema-mismatch-with-open-source-spark-and-delta-sharing
    - Delta Sharing and Schema Mismatch with Open Source Spark
    - SMWOSSADS
  citations:
    - file: troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
title: Schema Mismatch with Open Source Spark and Delta Sharing
description: Schema mismatch errors occur in OSS Spark when Delta table schema or partition columns change after DataFrame creation; fixable by setting spark.delta.sharing.client.useStructuralSchemaMatch to true (requires client 1.2.3+ and Spark 4.0+).
tags:
  - delta-sharing
  - apache-spark
  - schema-evolution
  - troubleshooting
timestamp: "2026-06-19T23:14:04.896Z"
---

# Schema Mismatch with Open Source Spark and [Delta Sharing](/concepts/delta-sharing.md)

**Schema Mismatch with Open Source Spark and Delta Sharing** is an error that occurs when reading [OpenSharing](/concepts/opensharing.md) tables using Open Source Spark (OSS). The error indicates that the schema or partition columns of the Delta table have changed after the DataFrame was initially created.

## Error Message

When this issue occurs, the following error is returned:

```
py4j.protocol.Py4JJavaError: An error occurred while calling o85.count.: org.apache.spark.SparkException: The schema or partition columns of your Delta table has changed since your DataFrame was created. Please redefine your DataFrame
```

^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Cause

The schema mismatch error occurs because the schema or partition columns of the Delta table changed after the DataFrame was created. This is a known issue when using Open Source Spark (OSS) to read [OpenSharing](/concepts/opensharing.md) tables. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Recommended Fix

Set the Spark configuration flag `spark.delta.sharing.client.useStructuralSchemaMatch` to `true`: ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

```python
spark.conf.set("spark.delta.sharing.client.useStructuralSchemaMatch", "true")
```

## Version Requirements

The `spark.delta.sharing.client.useStructuralSchemaMatch` configuration is only available in **delta-sharing-client 1.2.3 or above**, which requires **Apache Spark 4.0.0 or above**. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms
- [OpenSharing](/concepts/opensharing.md) — The open-source implementation of the [Delta Sharing](/concepts/delta-sharing.md) protocol
- Delta table schema evolution — How [Delta Lake](/concepts/delta-lake.md) handles schema changes over time
- Delta sharing client configuration — Available Spark configuration flags for the [Delta Sharing](/concepts/delta-sharing.md) client
- Troubleshooting Delta Sharing issues — Common errors when accessing data in a share

## Sources

- troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md

# Citations

1. [troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md](/references/troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws-801ba4c9.md)
