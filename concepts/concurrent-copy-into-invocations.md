---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9653d2eb10336c36229f5bf9344198ec40ef6c36fc825352f87abd319ed8c2b
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - concurrent-copy-into-invocations
    - CCII
    - Concurrent write operations
  citations:
    - file: copy-into-databricks-on-aws.md
title: Concurrent COPY INTO Invocations
description: COPY INTO supports concurrent runs on distinct file sets, with transaction conflicts on overlapping files. Single invocation with many files outperforms concurrent single-file runs.
tags:
  - databricks
  - concurrency
  - performance
  - delta-lake
timestamp: "2026-06-19T17:53:25.671Z"
---

# Concurrent COPY INTO Invocations

**Concurrent COPY INTO invocations** refers to running multiple `COPY INTO` commands simultaneously against the same Delta table. `COPY INTO` supports concurrent invocations as long as each invocation operates on a **distinct** set of input files. Under this condition, each invocation should eventually succeed; otherwise, a transaction conflict occurs. ^[copy-into-databricks-on-aws.md]

## When to use concurrent invocations

Concurrent `COPY INTO` invocations are appropriate in specific scenarios:
- **Multiple data producers** that cannot easily coordinate and cannot make a single invocation. ^[copy-into-databricks-on-aws.md]
- **Very large directories** that can be ingested sub-directory by sub-directory. ^[copy-into-databricks-on-aws.md]

## Performance considerations

`COPY INTO` should not be invoked concurrently to improve performance. A single `COPY INTO` command with multiple files typically performs better than running concurrent `COPY INTO` commands with a single file each. ^[copy-into-databricks-on-aws.md]

For directories with a very large number of files, Databricks recommends using Auto Loader when possible instead of concurrent `COPY INTO` invocations. ^[copy-into-databricks-on-aws.md]

## Transaction conflicts

If concurrent `COPY INTO` invocations attempt to load the same input files, a transaction conflict occurs. To avoid this, ensure that each concurrent invocation targets a distinct set of files. ^[copy-into-databricks-on-aws.md]

## Related concepts

- [COPY INTO](/concepts/copy-into-command.md) — The SQL command for loading data into Delta tables
- Auto Loader — Recommended alternative for ingesting directories with very large numbers of files
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides transactional guarantees for concurrent operations
- [Idempotent Data Loading](/concepts/idempotent-data-loading.md) — The retryable, idempotent behavior of COPY INTO

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
