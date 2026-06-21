---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eaa5a4ca5472b14200626b3ae87a6cfcc381df85469999d07584a3b62f2e9e77
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-query-timeout
    - DCQT
  citations:
    - file: limitations-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect Query Timeout
description: Long queries over 3600 seconds are not available in Databricks Connect for Databricks Runtime 13.3 LTS and below.
tags:
  - databricks
  - limitations
  - timeout
timestamp: "2026-06-19T19:12:10.982Z"
---

# Databricks Connect Query Timeout

**Databricks Connect Query Timeout** refers to a hard limit on the maximum duration of a query sent through [Databricks Connect for Python](/concepts/databricks-connect-for-python.md). Queries that exceed the timeout threshold fail with an error, preventing long-running operations from completing via the client connection.

## Timeout Limit

Databricks Connect imposes a query timeout of **3600 seconds (1 hour)**. Any query that runs longer than this limit is not supported and will not complete.^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Version Applicability

The 3600‑second query timeout applies to Databricks Connect for **Databricks Runtime 13.3 LTS and below**. For later versions of Databricks Runtime, this limitation may be removed or extended.^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Impact and Workarounds

Users executing long-running transformations or aggregations through Databricks Connect must ensure the query completes within one hour. If a query is expected to exceed this limit, users should consider:

- Breaking the query into smaller, incremental steps.
- Using alternative execution paths such as Databricks SQL or running the logic directly on the cluster via notebooks or jobs.

The timeout affects only the client‑to‑cluster connection through Databricks Connect; cluster‑side execution is not bounded by this limit.

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The client library subject to this timeout.
- Databricks Runtime — The runtime version determines whether the timeout applies.
- [Query Timeout](/concepts/query-timeout-3600-seconds.md) — General concept of execution time limits in database systems.
- [Databricks Connect Limitations](/concepts/databricks-connect-limitations.md) — Full list of restrictions for the Python connector.

## Sources

- limitations-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-python-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-python-databricks-on-aws-334fca41.md)
