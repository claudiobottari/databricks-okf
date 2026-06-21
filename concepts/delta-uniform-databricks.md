---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1db375279a452d9de698755c64607d148d486b53722d8c80b6d8c8e221bdd01
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
  confidence: 0.5
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-databricks
    - DU(
    - Delta Uniform (Delta Sharing)
  citations:
    - file: delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
title: Delta Uniform (Databricks)
description: A Databricks feature enabling Delta Lake tables to be read by other query engines through a unified format
tags:
  - databricks
  - delta-lake
  - interoperability
timestamp: "2026-06-19T10:09:34.776Z"
---

# Delta Uniform (Databricks)

**Delta Uniform** is a Databricks feature that enables Delta tables to be read by other table formats, such as Apache Iceberg and Apache Hudi, by automatically generating the corresponding metadata files. This allows cross-engine interoperability without duplicating data. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT Error

The `DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT` error condition occurs when the arguments supplied to a `REFRESH` operation on a Delta Uniform table are invalid or inconsistent. This error is raised at the start of the refresh operation. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

### Error Message

The error message follows this pattern:

```
DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT: <reason>
```

Where `<reason>` describes the specific invalid argument, such as an incompatible type, out-of-range value, or missing required parameter. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

### Common Causes

- Providing an unrecognized option key to the `REFRESH` statement.
- Supplying a value of the wrong data type for an option (e.g., a string instead of an integer).
- Using an invalid table identifier (e.g., a non-existent or non-Delta table).
- Passing a path that does not point to a valid Delta Uniform table.
- Attempting to refresh a table that does not have Uniform enabled. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

### Resolution

1. **Verify the table is a Delta Uniform table** by checking that the table property `delta.universalFormat.enabledFormats` is set appropriately (e.g., `iceberg`).
2. **Check the REFRESH command syntax** – ensure all options are spelled correctly and use the expected types. Refer to the [Delta Uniform REFRESH Syntax](/concepts/delta-uniform-refresh.md) documentation.
3. **Confirm the table path or identifier** exists and is accessible.
4. **Review the error reason** in the full message for specific guidance. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Universal Format (Uniform)](/concepts/delta-universal-format-uniform.md) – The overarching feature for multi-format table sharing.
- [Delta Uniform Refresh](/concepts/delta-uniform-refresh.md) – The command that triggers metadata regeneration.
- [Delta Sharing](/concepts/delta-sharing.md) – Another interoperability feature for sharing Delta data.
- Iceberg Compatibility – How Delta Uniform enables Iceberg readers.

## Sources

- delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws-592e817e.md)
