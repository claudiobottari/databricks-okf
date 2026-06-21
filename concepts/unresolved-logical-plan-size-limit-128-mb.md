---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62a37a773bfeb3c546a6a2ac7bf74f8e70dc698dd3d26c3d75605d706b739f29
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unresolved-logical-plan-size-limit-128-mb
    - ULPSL(M
  citations:
    - file: limitations-with-databricks-connect-for-scala-databricks-on-aws.md
title: Unresolved Logical Plan Size Limit (128 MB)
description: Databricks Connect for Scala cannot create DataFrames with an unresolved logical plan larger than 128 MB, a limit on plan size not data size.
tags:
  - databricks-connect
  - limitations
  - scala
timestamp: "2026-06-19T19:12:24.062Z"
---

# Unresolved Logical Plan Size Limit (128 MB)

The **Unresolved Logical Plan Size Limit (128 MB)** is a constraint in [Databricks Connect](/concepts/databricks-connect.md) that prevents creating DataFrames whose unresolved logical plan exceeds 128 megabytes. The limit applies to the size of the plan representation, not to the size of the underlying data. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Applicability

This limitation is documented for [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) on Databricks Runtime 13.3 LTS and below. It is listed among features that are **not available** in that version range. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Impact

When a DataFrame’s unresolved logical plan exceeds 128 MB, the operation fails before any data is read or computed. This typically occurs when constructing highly complex queries, such as those with a very large number of columns, deeply nested subqueries, or extensive joins that produce an overly large plan tree. The limit is independent of the actual data volume; a small dataset can still trigger the error if its plan representation is large.

## Workarounds

To avoid hitting the limit, consider simplifying the plan by:

- Reducing the number of columns or transformations before materializing.
- Breaking the query into multiple stages using intermediate tables or views.
- Using persisted intermediate results (e.g., `.cache()` or `.write.saveAsTable()`) to reduce plan depth.

Users on newer Databricks Runtime versions (14.x and above) should check the release notes to determine whether the limit has been increased or removed.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library for connecting remote IDEs and applications to Databricks clusters.
- Logical Plan – The unresolved, resolved, and optimized plans in Spark SQL.
- DataFrame – The primary distributed data abstraction in Spark.
- [Databricks Connect Limitations](/concepts/databricks-connect-limitations.md) – The full list of known limitations for [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md).

## Sources

- limitations-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-scala-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-scala-databricks-on-aws-8e97ac24.md)
