---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 484b91a794d273b39d1617edfa3db589e78ca173c6eb601084c729a1ffed3d2f
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_clone_with_history_unsupported_target
    - DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE
    - DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET
description: A Databricks error raised when cloning a Delta table with history into an unsupported target table type.
tags:
  - databricks
  - error-messages
  - delta-lake
timestamp: "2026-06-19T15:02:24.088Z"
---

---

title: DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET
summary: An error class raised in Databricks when a CLONE WITH HISTORY operation targets an unsupported table type.
sources:
  - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:51:18.061Z"
updatedAt: "2026-06-18T11:51:18.061Z"
tags:
  - databricks
  - error-message
  - delta-lake
aliases:
  - delta_clone_with_history_unsupported_target
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET Error Condition

**`DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET`** is a runtime error in Databricks with SQLSTATE `0AKDC` (Feature Not Supported). The error is raised when a `CLONE WITH HISTORY` operation specifies a target table that is not supported for history preservation. The error message lists the unsupported target type under one of three sub-reasons. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## SQLSTATE

`0AKDC`

## Sub-reasons and Messages

The error condition has three distinct sub-reasons, each returning a specific message:

### NON_DELTA

```
Target table of non-delta format is not supported.
```

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### PATH_BASED

```
Path-based target table is not supported.
```

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

### SESSION_TEMPORARY

```
Session temporary target table is not supported.
```

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Sub-reason Summary

| Sub-reason | Meaning (from message) |
|------------|------------------------|
| `NON_DELTA` | Target table is not in Delta format. |
| `PATH_BASED` | Target table is referenced by a file path. |
| `SESSION_TEMPORARY` | Target is a session‑temporary table. |

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
