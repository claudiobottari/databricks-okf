---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95f9df0f82c498b24f8abd518f90657d86bb17f7ae78316b1a7360a7b7d1fee2
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-compatibility-location-requirements
    - DUCLR
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: Delta UniForm compatibility location requirements
description: "The set of conditions an error location must satisfy for Delta UniForm compatibility: must exist, must be a directory, must not be blank, must be empty, and must be accessible."
tags:
  - error-messages
  - databricks
  - delta-lake
  - validation
timestamp: "2026-06-19T18:27:42.520Z"
---

# Delta UniForm Compatibility Location Requirements

**Delta UniForm compatibility location requirements** define the constraints for the `delta.universalFormat.compatibility.location` table property in a Delta table. This property stores an empty directory used as a staging or compatibility location for [Universal Format](/concepts/delta-universal-format-uniform.md) operations such as [Delta Uniform](/concepts/delta-uniform.md) to Iceberg. If the location does not meet the requirements, the `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error is raised. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Location Requirements

The `delta.universalFormat.compatibility.location` property must point to an **empty directory** that is accessible and writable by the Delta table. The directory must exist, be a directory (not a file), and be empty. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Sub‑conditions

The `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error class includes the following sub‑conditions, each describing a specific failure reason:

| Sub‑condition | Description |
|---------------|-------------|
| `ACCESS_DENIED` | Cannot access the specified location. The underlying error is appended. |
| `CANNOT_BE_BLANK` | The location value is blank. |
| `DIRECTORY_NOT_EMPTY` | The specified directory path is not empty. |
| `DOES_NOT_EXIST` | The specified location path does not exist. |
| `NOT_DIRECTORY` | The specified location path is not a directory. |
| `NOT_SET` | The configuration property has not been set at all. |

^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Resolution

To resolve the error, set the `delta.universalFormat.compatibility.location` property to a value that satisfies all requirements:

- The property must be set to a non‑blank string.
- The path must point to an existing directory.
- The directory must be empty.
- The user or service principal must have access permissions to the directory.

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – Overview of the Universal Format feature for interoperability.
- [Universal Format](/concepts/delta-universal-format-uniform.md) – The framework enabling Delta tables to be read by other table formats.
- Delta table properties – Configuration options for Delta tables.
- [Error handling in Databricks](/concepts/error-handling-in-databricks-notebook-workflows.md) – General error resolution guidance.

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
