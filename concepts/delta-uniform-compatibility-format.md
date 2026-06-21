---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b3fd75ad5605f9c267cdfd39106f78d642776852bee78fd81e983828f09999c5
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 0.6
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-compatibility-format
    - DUCF
    - Delta UniForm Compatibility
    - Delta Uniform Compatibility
    - Delta Uniform Compatibility Errors
    - Uniform compatibility format
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: Delta Uniform Compatibility Format
description: A Delta Lake feature in Databricks requiring a dedicated empty directory for compatibility format configuration.
tags:
  - databricks
  - delta-uniform
  - delta-lake
timestamp: "2026-06-19T15:08:12.285Z"
---

# Delta Uniform Compatibility Format

**Delta Uniform Compatibility Format** is a configuration setting in [Delta Lake](/concepts/delta-lake.md) that enables compatibility with external query engines by writing table data in a universally readable format. It is configured through the `delta.universalFormat.compatibility.location` table property.

## Overview

The Delta Uniform Compatibility Format allows Delta tables to be read by non-Delta engines by maintaining a secondary copy of the data in a format like Apache Parquet. This enables interoperability between Delta Lake and other data processing systems without requiring them to understand the Delta transaction log. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Configuration

To enable the compatibility format, set the `delta.universalFormat.compatibility.location` property on a Delta table to point to an empty directory. This directory will store the compatibility-format data that external engines can read. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Conditions

When the compatibility location is missing or invalid, the `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error (SQLSTATE: 42601) is raised. The error includes a specific reason for the failure. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### ACCESS_DENIED

The system cannot access the specified location. The error message includes details about the access failure. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### CANNOT_BE_BLANK

The location value is empty or blank. A valid path must be provided. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DIRECTORY_NOT_EMPTY

The specified directory already contains files. The compatibility format requires an empty directory to write its data. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DOES_NOT_EXIST

The specified path does not exist in the storage system. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_DIRECTORY

The specified path exists but is not a directory. The compatibility location must be a directory. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_SET

The `delta.universalFormat.compatibility.location` configuration has not been set on the table. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Requirements

The compatibility location must meet the following requirements:
- It must be a valid, accessible path in the storage system
- It must be a directory (not a file)
- The directory must be empty
- The path must not be blank

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Delta tables
- [Delta Uniform](/concepts/delta-uniform.md) — The broader feature for universal format compatibility
- Table Properties — Configuration properties that control Delta table behavior
- [Delta Sharing](/concepts/delta-sharing.md) — Another mechanism for cross-engine data access

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
