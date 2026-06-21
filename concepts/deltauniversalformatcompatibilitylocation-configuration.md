---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07b9bb88fb21e4860967b387ca9c78134913652b3eaa66a61625a9b621f32900
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deltauniversalformatcompatibilitylocation-configuration
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: delta.universalFormat.compatibility.location Configuration
description: A Databricks Delta Lake configuration property that must point to an empty directory for Uniform compatibility format
tags:
  - configuration
  - databricks
  - delta-lake
  - uniform-format
timestamp: "2026-06-18T11:56:03.330Z"
---

# `delta.universalFormat.compatibility.location` Configuration

The `delta.universalFormat.compatibility.location` configuration property specifies the directory path where Delta UniForm compatibility files (such as Iceberg metadata) are stored. This property must be set to an empty directory for Delta UniForm compatibility to function correctly. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Purpose

When [Delta UniForm Compatibility](/concepts/delta-uniform-compatibility-format.md) is enabled for a [Delta Lake](/concepts/delta-lake.md) table, the `delta.universalFormat.compatibility.location` configuration tells Delta where to write metadata files that allow external systems to read the Delta table in a different format, such as [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md). This directory must be empty and dedicated solely to this compatibility metadata. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Requirements

The specified location must meet the following criteria:

- **Must be a directory.** The path must point to an existing directory, not a file.
- **Must be empty.** The directory must contain no files or subdirectories.
- **Must be accessible.** The user or service principal must have read and write access to the location.
- **Must exist.** The directory must already exist at the specified path.

If any of these conditions are not met, Delta returns the `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Conditions

When the `delta.universalFormat.compatibility.location` configuration is invalid, the error class `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` is raised with one of the following causes: ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

| Error Subtype | Description |
|---------------|-------------|
| `ACCESS_DENIED` | The user cannot access the location. The error message includes details about the access failure. |
| `CANNOT_BE_BLANK` | The location value is empty or blank. |
| `DIRECTORY_NOT_EMPTY` | The specified directory already contains files or subdirectories. |
| `DOES_NOT_EXIST` | The specified path does not exist on the filesystem. |
| `NOT_DIRECTORY` | The specified path points to an existing file, not a directory. |
| `NOT_SET` | The configuration property has not been set at all. |

## Error Classification

The `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error class has SQLSTATE code `42601`, which falls under the class of syntax errors or access rule violations (Class 42). ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta UniForm Compatibility](/concepts/delta-uniform-compatibility-format.md) — The feature that requires this configuration
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that enforces this configuration requirement
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — One of the formats supported by UniForm compatibility
- SQLSTATE — The SQL standard error classification system
- Table Properties in Delta Lake — How table and session properties like this one are managed

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
