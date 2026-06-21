---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0f34093a3e054aa557715097bfb0f3701fc6e173b81857443b34de6b82189b71
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
  confidence: 0.6
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-refresh
    - DUR
    - Delta Lake uniform refresh
    - Delta Uniform REFRESH Syntax
  citations:
    - file: delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
title: Delta Uniform Refresh
description: A Databricks operation to synchronize or update the metadata of a Delta table's Uniform representation so external engines can read the latest data.
tags:
  - databricks
  - delta-lake
  - operations
timestamp: "2026-06-19T15:08:56.423Z"
---

# Delta Uniform Refresh

**Delta Uniform Refresh** is an operation in Databricks that updates the metadata or data files of a Delta table configured with [Delta Universal Format (UniForm)](https://docs.databricks.com/en/delta-uniform.html). UniForm enables Delta tables to be read by Iceberg and Hudi clients by writing additional metadata in those formats. The refresh operation synchronizes this secondary metadata, ensuring that external readers see the latest table state.

## Error Condition

When a Delta Uniform Refresh is invoked with incorrect parameters, Databricks raises a `DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT` error. This error class indicates that the arguments supplied to the refresh operation are not valid for the table’s current configuration or the refresh workflow. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

### Common Causes

- Specifying a table path that does not have UniForm enabled.
- Providing an unsupported or mis-typed refresh mode.
- Passing arguments that conflict with the table’s existing UniForm settings.

### Resolution

- Verify that the target table has UniForm enabled (check the table properties).
- Review the refresh command syntax and available arguments in the [Databricks SQL language reference](https://docs.databricks.com/en/sql/language-manual/index.html).
- Ensure that the Delta table is not being concurrently modified by other write operations during the refresh.

## Related Concepts

- [Delta Universal Format (Uniform)](/concepts/delta-universal-format-uniform.md)
- [Iceberg compatibility](/concepts/icebergcompatv.md)
- Hudi compatibility
- Refresh Table
- [Delta Lake table properties](/concepts/delta-lake-reader-table-features.md)

## Sources

- delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws-592e817e.md)
