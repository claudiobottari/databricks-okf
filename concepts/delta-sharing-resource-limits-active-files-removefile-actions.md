---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f99c9228d5b96af8f095d5273b3c932305f38e9a8928561c8548a6d3ba08cd85
  pageDirectory: concepts
  sources:
    - troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-sharing-resource-limits-active-files-removefile-actions
    - DSRL(F&RA
  citations:
    - file: troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
title: Delta Sharing Resource Limits (Active Files & RemoveFile Actions)
description: "Hard limits on shared Delta tables: 400K active files (AddFile) and 100K RemoveFile entries in the Delta log, which if exceeded produce RESOURCE_LIMIT_EXCEEDED errors."
tags:
  - delta-sharing
  - resource-limits
  - troubleshooting
timestamp: "2026-06-19T23:14:03.239Z"
---

# [Delta Sharing](/concepts/delta-sharing.md) Resource Limits (Active Files & RemoveFile Actions)

**Delta Sharing Resource Limits** define the maximum number of metadata entries that can be returned when a recipient queries a shared Delta table. Two separate limits exist: one for active data files (AddFile actions) and one for historical remove operations (RemoveFile actions). When either limit is exceeded, the query fails with a `RESOURCE_LIMIT_EXCEEDED` error. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Active Files Limit

A shared table can contain at most **400,000 active files** (that is, AddFile actions in the Delta Log that are not superseded by a RemoveFile action). If the number of active files exceeds this threshold, the recipient receives an error similar to:

```
RESOURCE_LIMIT_EXCEEDED: The number of files in the table to return exceeded limits, consider contact your provider to optimize the table
```

^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## RemoveFile Actions Limit

A shared table supports a maximum of **100,000 RemoveFile actions** in its Delta log. These actions represent files that have been deleted (e.g., through `DELETE`, `UPDATE`, or `VACUUM`). When this limit is exceeded, the error message is:

```
RESOURCE_LIMIT_EXCEEDED: The table metadata size exceeded limits
```

^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Causes and Recommended Fixes

Both limits are triggered when a table's metadata (the Delta log) grows too large to be efficiently transmitted and processed by the [Delta Sharing](/concepts/delta-sharing.md) client. The primary cause is an excessive number of small files or a long history of file removals.

The recommended first step is to contact the data provider and ask them to:

- Run OPTIMIZE to compact small files into larger ones, reducing the count of active AddFile entries.
- Run VACUUM to clean up stale RemoveFile entries from the Delta log, keeping only those needed for time travel.

These operations reduce the metadata size and bring the table back within the sharing limits. For further guidance, refer to the Databricks Knowledge Base article on the `RESOURCE_LIMIT_EXCEEDED` error. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Requesting a Limit Increase

If the table’s active file count cannot be reduced to 400,000 through optimization alone, the data provider can request a limit increase. See the Databricks documentation on Resource Limits for instructions. Note that the RemoveFile action limit is not mentioned as eligible for increase in the source material. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The protocol for sharing data across platforms.
- Delta Log – The transaction log that records all changes to a Delta table.
- OPTIMIZE – Command to compact small files and improve read performance.
- VACUUM – Command to remove old files and clean the Delta log.
- Resource Limits – General Databricks limits and how to request increases.
- Troubleshooting Delta Sharing Issues – Other common errors and solutions.

## Sources

- troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md

# Citations

1. [troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md](/references/troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws-801ba4c9.md)
