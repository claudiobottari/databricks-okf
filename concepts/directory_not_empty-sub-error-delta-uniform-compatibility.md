---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51b273dae5eeb2de6956298c0b64ab7c00636d7f99f61970bd77b6fa90f55336
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - directory_not_empty-sub-error-delta-uniform-compatibility
    - DS(UC
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: DIRECTORY_NOT_EMPTY sub-error (Delta Uniform Compatibility)
description: A specific reason code under the DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION error class indicating the configured directory must be empty
tags:
  - error-messages
  - databricks
  - delta-lake
timestamp: "2026-06-18T11:56:17.605Z"
---

# DIRECTORY_NOT_EMPTY sub-error (Delta Uniform Compatibility)

The **DIRECTORY_NOT_EMPTY** sub-error occurs when configuring Delta Uniform Compatibility and the value of `delta.universalFormat.compatibility.location` points to a directory that already contains files or subdirectories. This sub-error is part of the parent error `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` (SQLSTATE: 42601). ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Message

When this sub-error is encountered, Databricks returns the following message:

```
The specified directory <path> is not empty.
```

Where `<path>` is the location provided in the configuration. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Cause

The `delta.universalFormat.compatibility.location` table property must point to an empty directory. If you set this property to a directory that already contains data (files or subdirectories), Databricks rejects the configuration with the `DIRECTORY_NOT_EMPTY` sub-error. This requirement ensures that the Uniform compatibility format can write its metadata and auxiliary files without conflicting with existing content. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Solution

To resolve the error, choose one of the following approaches:

- **Use an empty directory.** Point the `delta.universalFormat.compatibility.location` property to a new, empty directory that has not been used before.
- **Clear the existing directory.** If you must reuse a specific path, delete all contents of the directory before setting the property. Ensure the directory is completely empty — Databricks checks for any files or subdirectories.
- **Change the location.** Update the table property to reference a different, empty path on the same storage location.

After the directory is empty, re-apply the configuration. The property must be set at the table level using the `ALTER TABLE` statement or during table creation.

## Related Concepts

- [Delta Uniform Compatibility](/concepts/delta-uniform-compatibility-format.md) — The feature that enables Delta tables to be read by other formats (e.g., Iceberg, Hudi)
- [delta.universalFormat.compatibility.location](/concepts/deltauniversalformatcompatibilitylocation.md) — The table property that specifies the directory for compatibility metadata
- DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION — The parent error class containing this and other sub-errors
- [SQLSTATE 42601](/concepts/sqlstate-42601.md) — The SQL error class for syntax or access rule violations
- Managed tables and external locations — Understanding how Delta table storage works

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
