---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 908256757a1d01feb905f2c42a9860f6c7c254ab2ecec0edfa4c4c6e6535c3c9
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-travelled-source-restriction-for-clone-with-history
    - TSRFCWH
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: Time-travelled source restriction for clone with history
description: The error condition raised when cloning a Delta table with history from a source that was accessed via time travel by timestamp, which is unsupported.
tags:
  - databricks
  - delta-lake
  - cloning
  - time-travel
timestamp: "2026-06-19T10:03:11.674Z"
---

# Time-Travelled Source Restriction for Clone with History

**Time-travelled source restriction for clone with history** is an error condition that occurs when attempting to use `CLONE WITH HISTORY` on a Delta table that has been queried using a time-travel timestamp. The operation is not supported in this scenario. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Overview

When cloning a [Delta table](/concepts/delta-lake-table.md) with its full history using the `CLONE WITH HISTORY` command, the source table must satisfy certain constraints. One specific restriction is that the source table cannot have been accessed via [Delta time travel](/concepts/delta-lake-time-travel.md) using a **timestamp** prior to the clone operation. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error Condition

The error is categorized under the DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class (SQLSTATE: 0AKDC) and produces the following message: ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

> Source table time travelled by timestamp is not supported.

## Cause

This restriction applies specifically to **time travel by timestamp** (`TIMESTAMP AS OF` syntax). If the source table was queried using a point-in-time timestamp before the clone operation, the `CLONE WITH HISTORY` command will fail with this error. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Workarounds

To clone a table with history from a time-travelled state, use one of the following approaches:

- **Use version-based time travel** instead of timestamp-based time travel. The `VERSION AS OF` syntax does not trigger this restriction. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]
- Clone the table **without history** using a standard `CLONE` command (without the `WITH HISTORY` clause) from the time-travelled timestamp state. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE — The full error class containing this and other clone restrictions
- NON_DELTA source restriction — A related restriction when source is a non-Delta format
- [Delta Table Cloning](/concepts/delta-table-cloning.md) — The broader feature for creating table copies
- [Delta time travel](/concepts/delta-lake-time-travel.md) — Querying historical versions of Delta tables

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
