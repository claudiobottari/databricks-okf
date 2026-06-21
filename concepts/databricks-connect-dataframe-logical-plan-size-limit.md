---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46cb2e985b5a8900e0a0d6ba382cbc38ff477fd0f7d4c4aa1cd7db48bbcb3eac
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-dataframe-logical-plan-size-limit
    - DCDLPSL
  citations:
    - file: limitations-with-databricks-connect-for-python-databricks-on-aws.md
      start: 21
      end: 23
    - file: limitations-with-databricks-connect-for-python-databricks-on-aws.md
      start: 20
      end: 23
title: Databricks Connect DataFrame Logical Plan Size Limit
description: Databricks Connect cannot create DataFrames with an unresolved logical plan larger than 128 MB (applies to plan size, not data) for Runtime 13.3 LTS and below.
tags:
  - databricks
  - limitations
  - performance
timestamp: "2026-06-19T19:12:09.758Z"
---

# Databricks Connect DataFrame Logical Plan Size Limit

The **Databricks Connect DataFrame Logical Plan Size Limit** is a restriction in [Databricks Connect](/concepts/databricks-connect.md) that prevents the creation of DataFrames with an unresolved logical plan larger than 128 MB. This limit applies to the size of the query plan itself, not to the underlying data. It is enforced only for Databricks Connect for Python when using Databricks Runtime 13.3 LTS or earlier. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md:21-23]

## Scope of the Limit

The 128 MB limit specifically targets the **unresolved logical plan**—the tree of operations (e.g., projections, filters, joins) that Spark builds before analysis. If the combined size of these operations exceeds 128 MB, creating the DataFrame will fail. This is distinct from the volume of data the plan would process; a small dataset can still trigger the limit if the query logic itself is excessively complex or repetitive. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md:21-23]

The limit applies only when using [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) with **Databricks Runtime 13.3 LTS and below**. In later versions of Databricks Runtime, the restriction may be removed or increased. The limitation is listed alongside other unavailable features such as streaming `foreachBatch` and long queries over 3600 seconds. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md:20-23]

## Implications

Users who rely on [Databricks Connect](/concepts/databricks-connect.md) to develop against older Databricks Runtime versions must ensure their DataFrame construction does not produce an unresolved logical plan larger than 128 MB. This can become an issue when:

- Using deeply nested or heavily chained transformations.
- Programmatically generating thousands of columns or conditionals.
- Applying the same large set of operations repeatedly in a single plan.

A workaround is to break the logic into smaller intermediate DataFrames, persist them, and then combine results. Alternatively, upgrading to a newer Databricks Runtime version may eliminate the restriction entirely.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- Logical Plan
- Unresolved Logical Plan
- [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md)
- DataFrame
- Limitations with Databricks Connect for Python

## Sources

- limitations-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-python-databricks-on-aws.md:21-23](/references/limitations-with-databricks-connect-for-python-databricks-on-aws-334fca41.md)
2. [limitations-with-databricks-connect-for-python-databricks-on-aws.md:20-23](/references/limitations-with-databricks-connect-for-python-databricks-on-aws-334fca41.md)
