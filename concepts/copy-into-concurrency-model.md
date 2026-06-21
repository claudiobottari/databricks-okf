---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22f0b41df295ea8b678b048fc63fb5c276a0568ef0e65f601a651134683297ef
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-concurrency-model
    - CICM
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO Concurrency Model
description: Concurrent COPY INTO invocations are supported against the same table as long as they operate on distinct input file sets
tags:
  - databricks
  - concurrency
  - performance
timestamp: "2026-06-19T09:25:14.506Z"
---

# COPY INTO Concurrency Model

**COPY INTO Concurrency Model** describes how multiple invocations of the `COPY INTO` command can run simultaneously against the same Delta table, the conditions under which they succeed or fail, and the recommended usage patterns for concurrent data ingestion.

## Overview

`COPY INTO` supports concurrent invocations against the same table. As long as each invocation loads a **distinct** set of input files, each concurrent execution will eventually succeed. If two concurrent invocations attempt to load the same file, a transaction conflict occurs and one of them fails. ^[copy-into-databricks-on-aws.md]

## Performance Considerations

Concurrent `COPY INTO` commands should **not** be used to improve throughput. A single `COPY INTO` statement that processes multiple files in one invocation typically performs far better than running several concurrent `COPY INTO` commands, each handling a single file. ^[copy-into-databricks-on-aws.md]

## When to Use Concurrent `COPY INTO`

Concurrent invocations are appropriate in two scenarios: ^[copy-into-databricks-on-aws.md]

1. **Uncoordinated data producers** – When multiple independent sources write files to the same location and cannot coordinate to make a single `COPY INTO` call.
2. **Very large directory ingestion** – When a source directory contains an extremely large number of files, it may be practical to ingest the data sub-directory by sub-directory using separate `COPY INTO` commands.

For directories with a very large number of files, Databricks recommends using Auto Loader instead of `COPY INTO`. ^[copy-into-databricks-on-aws.md]

## Idempotency and the `force` Option

`COPY INTO` is idempotent by default: files that have already been loaded are skipped, even if the files have been modified since they were first loaded. This default behavior prevents duplicate data when rerunning the same command. ^[copy-into-databricks-on-aws.md]

The `force` copy option (`force = true`) disables idempotency. When `force` is enabled, all files in the source location are re‑loaded, regardless of whether they have been loaded before. This option is useful for reprocessing data but can increase the likelihood of transaction conflicts in concurrent scenarios. ^[copy-into-databricks-on-aws.md]

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) – The complete command reference
- [Delta Lake](/concepts/delta-lake.md) – Transactional storage layer underlying the concurrency model
- Auto Loader – Recommended alternative for very large file directories
- File metadata column – Metadata available when reading file-based sources
- [Idempotent Data Ingestion](/concepts/idempotent-data-loading.md) – Ensuring repeatable loads without duplicates

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
