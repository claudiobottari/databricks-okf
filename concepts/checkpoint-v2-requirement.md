---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fddbce22e71e5051166e265c751327edf007a6d0e23ebdc98b2e6c5610f74564
  pageDirectory: concepts
  sources:
    - reorg-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - checkpoint-v2-requirement
    - CVR
    - checkpoint
  citations:
    - file: reorg-table-databricks-on-aws.md
title: Checkpoint V2 requirement
description: APPLY (CHECKPOINT) requires the table to have Checkpoint V2 enabled to prevent corruption caused by race conditions.
tags:
  - checkpointing
  - delta-lake
  - corruption-prevention
  - checkpoint-v2
timestamp: "2026-06-19T20:13:25.577Z"
---

# Checkpoint V2 Requirement

The **Checkpoint V2 requirement** is a prerequisite for using the `APPLY (CHECKPOINT)` operation in the `REORG TABLE` command on Delta Lake tables. Checkpoint V2 must be enabled on a table before performing a Delta checkpoint via `REORG TABLE` to prevent corruption caused by race conditions. ^[reorg-table-databricks-on-aws.md]

## Overview

Delta Lake checkpointing is a metadata management operation that creates checkpoint files summarizing the transaction log. The `REORG TABLE ... APPLY (CHECKPOINT)` command performs checkpointing on a table's latest Delta version. However, this operation requires the table to have Checkpoint V2 enabled. ^[reorg-table-databricks-on-aws.md]

## Purpose

The Checkpoint V2 requirement exists to prevent corruption that can occur due to race conditions during the checkpointing process. Without Checkpoint V2, concurrent operations on the table could lead to inconsistent metadata states when checkpoints are created. ^[reorg-table-databricks-on-aws.md]

## Applicability

The `APPLY (CHECKPOINT)` operation and its Checkpoint V2 requirement apply to Databricks Runtime 16.3 and above. ^[reorg-table-databricks-on-aws.md]

## Usage

To perform a checkpoint on a Delta table, the table must first have Checkpoint V2 enabled. Once enabled, you can run:

```sql
REORG TABLE table_name APPLY (CHECKPOINT);
```

^[reorg-table-databricks-on-aws.md]

## Related Concepts

- [REORG TABLE](/concepts/reorg-table.md) — The command that performs checkpointing and other table reorganization operations
- Delta Lake checkpointing — The metadata management mechanism that Checkpoint V2 enhances
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The core metadata structure that checkpointing optimizes
- VACUUM — A related operation for physically deleting old data files after purging soft-deleted data

## Sources

- reorg-table-databricks-on-aws.md

# Citations

1. [reorg-table-databricks-on-aws.md](/references/reorg-table-databricks-on-aws-58d61683.md)
