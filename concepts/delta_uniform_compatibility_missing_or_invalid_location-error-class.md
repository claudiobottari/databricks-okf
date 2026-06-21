---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8608277dbf8ed80b24452007ca0bf5be8061a39038da7d6e9aaaeef5683135df
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_uniform_compatibility_missing_or_invalid_location-error-class
    - DEC
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION Error Class
description: A Databricks error class raised when the delta.universalFormat.compatibility.location configuration is missing, blank, inaccessible, or points to an invalid path
tags:
  - error-messages
  - databricks
  - delta-lake
  - configuration
timestamp: "2026-06-18T11:56:13.533Z"
---

# DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION Error Class

The `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error occurs when the [`delta.universalFormat.compatibility.location`](/delta-universal-format) configuration is missing, invalid, or inaccessible for a Unity Catalog-enabled table that uses the [Delta Uniform](/concepts/delta-uniform.md) format. This error class has SQLSTATE `42601`, which falls under the syntax error or access rule violation category. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Message

The error presents the following message structure:

```
Missing or invalid location for Uniform compatibility format.
Please set an empty directory for delta.universalFormat.compatibility.location.
Failed reason:
```

The failure reason is provided as a sub-error that specifies the exact nature of the problem. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Sub-Error Conditions

### ACCESS_DENIED

The location exists but the current user or service principal cannot access it. The error message includes the specific access error:

```
Cannot access the location. Error: <error>
```

^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### CANNOT_BE_BLANK

The location value is an empty string. The configuration requires a non-blank value. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DIRECTORY_NOT_EMPTY

The specified directory contains existing files or subdirectories. The compatibility location must be an empty directory. The error includes the path:

```
The specified directory <path> is not empty.
```

^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DOES_NOT_EXIST

The specified path does not exist in the underlying storage system. The error includes the path:

```
The specified location <path> does not exist.
```

^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_DIRECTORY

The specified path points to a file rather than a directory. The compatibility location must be a directory. The error includes the path:

```
The specified location <path> is not a directory.
```

^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_SET

The `delta.universalFormat.compatibility.location` configuration has not been set at all. This is the most basic sub-error, indicating the required configuration is absent. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Resolution

1. **For NOT_SET**: Set the `delta.universalFormat.compatibility.location` configuration on the table to an appropriate empty directory path.
2. **For CANNOT_BE_BLANK**: Provide a non-empty path for the configuration.
3. **For DOES_NOT_EXIST**: Create the directory in your storage location before setting the configuration.
4. **For NOT_DIRECTORY**: Ensure the specified path points to a directory, not a file.
5. **For DIRECTORY_NOT_EMPTY**: Specify a different directory that is empty, or clear the existing directory.
6. **For ACCESS_DENIED**: Verify that the user or service principal has the necessary permissions to read the specified storage location.

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The format that requires the compatibility location configuration
- [Delta Sharing](/concepts/delta-sharing.md) — A feature that works with Delta Uniform for cross-platform data access
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enforces table configuration requirements
- Iceberg Compatibility — Delta Uniform provides compatibility with Apache Iceberg readers

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
