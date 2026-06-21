---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b695645d32d7ab8001db50a9d47c548b188005a608ee02ab605b3a41c6eaca51
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
  confidence: 0.6
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta_uniform_refresh_invalid_argument-error
  citations:
    - file: delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
title: DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT Error
description: A Databricks error class raised when invalid arguments are provided during a Delta Uniform refresh operation
tags:
  - databricks
  - error-messages
  - delta-lake
  - uniform
timestamp: "2026-06-19T10:09:20.385Z"
---

Here is the wiki page for "DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT Error".

---

## DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT Error

The **DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT** error occurs when an attempt to refresh a [Delta Uniform](/concepts/delta-sharing.md) share fails because of invalid or malformed arguments supplied by the caller. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Error Message

The error condition is raised with the following class and message:

```
DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT
```

The specific text and arguments will vary depending on the exact reason for the invalidity. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Cause

This error is triggered when a uniform refresh operation receives an argument that is not valid. The validation failure may be due to:

- **Incorrect action type**: The [`SHOW`](https://docs.databricks.com/aws/en/error-messages/delta-uniform-refresh-invalid-argument-error-class) command may be passed an invalid action argument. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]
- **Malformed source table path**: The path provided for the source table may be syntactically invalid. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Solution

Correct the argument(s) causing the failure. Specific remediation steps depend on the particular argument flagged in the error message. Review the error details to identify which part of the command is malformed and ensure all identifiers, paths, and action types are valid. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for sharing live data
- [Delta Uniform](/concepts/delta-uniform.md) — The feature enabling the refresh operation
- Error Conditions — Other Databricks error messages and troubleshooting guides
- SHOW Command — The syntactical construct associated with this error

## Sources

- delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws-592e817e.md)
