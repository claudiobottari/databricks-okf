---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b00f3532dc00ce548e21fb0281b7327f3f764ee3c470700efdd9d05d84e9d9db
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_uniform_compatibility_missing_or_invalid_location
    - DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION
    - delta_uniform_compatibility_missing_or_invalid_location-error-class
    - DEC
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION
description: A Databricks error class raised when the Delta UniForm compatibility location configuration is missing, empty, inaccessible, or not a valid empty directory.
tags:
  - error-messages
  - databricks
  - delta-lake
timestamp: "2026-06-19T18:27:37.938Z"
---

Here is the wiki page for "DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION", drawing only from the provided source material.

---

# DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION

**DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION** is an error condition that occurs when the `delta.universalFormat.compatibility.location` configuration is missing, blank, or points to an invalid path. This configuration is required for [Delta Uniform](/concepts/delta-uniform.md) compatibility format to function correctly. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Details

- **SQLSTATE**: 42601 (Syntax error or access rule violation) ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]
- **Error class**: `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Message

The error returns the following message:

```
Missing or invalid location for Uniform compatibility format. Please set an empty directory for delta.universalFormat.compatibility.location. Failed reason: <sub-reason>
```

^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Sub-Reasons

The error includes one of the following sub-reasons that further describes the specific issue:

### ACCESS_DENIED

```
Cannot access the location. Error: <error>
```

The system cannot access the specified location due to permission issues. The underlying error message provides additional details about the access failure. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### CANNOT_BE_BLANK

```
The location cannot be blank.
```

The configuration value is an empty string. A valid path must be provided. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DIRECTORY_NOT_EMPTY

```
The specified directory <path> is not empty.
```

The specified path points to a directory that already contains files. The compatibility location requires an empty directory. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DOES_NOT_EXIST

```
The specified location <path> does not exist.
```

The provided path does not point to an existing location in the filesystem. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_DIRECTORY

```
The specified location <path> is not a directory.
```

The provided path exists but is not a directory. The compatibility location must be a directory. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_SET

```
The config is not set.
```

The `delta.universalFormat.compatibility.location` configuration has not been set at all. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, set the `delta.universalFormat.compatibility.location` configuration to an empty directory path that is accessible to the system. Ensure that:

- The path is not blank.
- The path points to an existing directory.
- The directory is empty.
- The system has appropriate access permissions to the location.

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The universal format compatibility feature that requires this configuration.
- Delta Lake Configuration Properties — How to set [Delta Lake Table](/concepts/delta-lake-table.md) properties.
- Error Conditions in Databricks — Other error classes and their resolutions.

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
