---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d4e26529e9d1eeb7d7ed3712d8fd8f63c1ea1f62af91a3878b95e0c4dadb2a25
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-universal-format-compatibility
    - DU(FC
    - Uniform format compatibility
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: Delta Uniform (Universal Format) Compatibility
description: A Databricks feature that enables Delta tables to be read by non-Delta engines through a compatibility format, requiring a dedicated empty directory location
tags:
  - databricks
  - delta-lake
  - interoperability
  - data-formats
timestamp: "2026-06-18T11:56:10.236Z"
---

# Delta Uniform (Universal Format) Compatibility

**Delta Uniform (Universal Format) Compatibility** refers to the configuration setting `delta.universalFormat.compatibility.location` in [Delta Lake](/concepts/delta-lake.md) that enables tables to be read by external query engines that do not natively support the Delta format. This compatibility layer allows Delta tables to be accessed through formats like Apache Parquet while maintaining Delta's transactional guarantees.

## Overview

The Delta Universal Format compatibility feature allows Delta tables to expose their data in a format compatible with non-Delta readers. When configured, Delta writes data in a secondary format alongside the Delta log, enabling external engines to read the table without Delta Lake support. The compatibility is controlled by setting the `delta.universalFormat.compatibility.location` table property to an empty directory path. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Configuration

To enable Delta Uniform compatibility, set the `delta.universalFormat.compatibility.location` property on a Delta table. This property must point to an empty directory where Delta will write the compatible format data. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

```sql
ALTER TABLE my_table SET TBLPROPERTIES (
  'delta.universalFormat.compatibility.location' = '/path/to/empty/directory'
);
```

## Error Conditions

When the `delta.universalFormat.compatibility.location` configuration is missing or invalid, Delta Lake raises the `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error (SQLSTATE: 42601). This error occurs under the following conditions: ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### ACCESS_DENIED

The system cannot access the specified location. This typically occurs when the user or service principal lacks the necessary permissions on the storage path. The error message includes the specific access failure details. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### CANNOT_BE_BLANK

The location value is an empty string. The configuration requires a non-blank path to a directory. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DIRECTORY_NOT_EMPTY

The specified directory already contains files or subdirectories. Delta requires the compatibility location to be an empty directory to avoid conflicts with existing data. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DOES_NOT_EXIST

The specified path does not exist in the storage system. The directory must be created before setting the configuration. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_DIRECTORY

The specified path points to a file rather than a directory. The compatibility location must be a directory, not a file. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_SET

The `delta.universalFormat.compatibility.location` configuration has not been set on the table. This occurs when attempting to use Universal Format compatibility features without first configuring the location property. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Troubleshooting

To resolve the `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error:

1. **Verify the path exists**: Ensure the specified directory exists in your storage system.
2. **Confirm it is a directory**: Check that the path points to a directory, not a file.
3. **Ensure the directory is empty**: Remove any existing files or subdirectories from the target location.
4. **Check permissions**: Verify that the user or service principal has read and write access to the storage location.
5. **Set the configuration**: If `NOT_SET`, add the `delta.universalFormat.compatibility.location` table property with a valid path.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that provides ACID transactions
- [Delta Universal Format](/concepts/delta-universal-format-uniform.md) — The feature enabling cross-format compatibility
- Table Properties — Configuration settings for Delta tables
- [Delta Sharing](/concepts/delta-sharing.md) — Another approach to sharing Delta data across platforms

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
