---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a768ba6f3f3d31d1cb49c892eba19a7e47f3935b17d8c51ea39ffa7fbcbee363
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cannot_finalize_redirect-sub-error
title: CANNOT_FINALIZE_REDIRECT Sub-Error
description: Sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED triggered when redirect configuration is missing during table migration
tags:
  - error-messages
  - databricks
  - rollback
timestamp: "2026-06-19T18:21:19.461Z"
---

# CANNOT_FINALIZE_REDIRECT Sub-Error

The **CANNOT_FINALIZE_REDIRECT** sub-error is an error condition that occurs when an `ALTER TABLE SET MANAGED` operation fails because the redirect configuration required to finalize the table migration doesn't exist. This error is part of the broader DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class.

## Error Message

When this error occurs, the system returns:

```
CANNOT_FINALIZE_REDIRECT: It cannot finalize redirect on the external location because redirect configuration doesn't exist.
```

This can happen if the table is currently rolling back to external. Otherwise, contact Databricks support.

## Context

The `ALTER TABLE SET MANAGED` command attempts to convert an external table to a managed table, which requires a redirect configuration to track the migration. The CANNOT_FINALIZE_REDIRECT error indicates that the redirect configuration is missing or has been removed during the migration process.

## Related Sub-Errors

Other sub-errors in the same error class include:

- FILE_VALIDATION_FAILED - When file migration fails
- REDIRECT_READY_ALREADY_EXISTS - When the table already has RedirectReady state
- VERSION_MISMATCH - When the managed DeltaLog version doesn't match

## Troubleshooting

To resolve this error:

1. Check if the table is currently rolling back to external by using `DESC EXTENDED <table>`.
2. If the table is rolling back, wait for the rollback to complete before retrying.
3. If the issue persists, contact Databricks support for assistance.

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
