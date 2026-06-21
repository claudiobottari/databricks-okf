---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2321a4daa3164762048a4fc4890115ca1cbbd5ed0657c4be1a67e63961ff235f
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deltauniversalformatcompatibilitylocation
    - Table property delta.universalFormat.compatibility.location
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: delta.universalFormat.compatibility.location
description: A configuration property in Databricks Delta Lake that must point to an empty directory for Delta UniForm compatibility format to work.
tags:
  - configuration
  - databricks
  - delta-lake
timestamp: "2026-06-19T18:27:38.348Z"
---

# delta.universalFormat.compatibility.location

**`delta.universalFormat.compatibility.location`** is a table property in [Delta Lake](/concepts/delta-lake.md) that specifies the directory to be used for [Uniform format compatibility](/concepts/delta-uniform-universal-format-compatibility.md) mode. When set, this property must point to an existing, empty directory that serves as the compatibility location for writing or reading in a universal format such as Iceberg or Parquet. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Class

If the property is missing, blank, or points to an invalid location, Delta Lake raises the error class `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` with SQLSTATE `42601`. The standard error message is: ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

> Missing or invalid location for Uniform compatibility format. Please set an empty directory for delta.universalFormat.compatibility.location.

## Sub‑Reasons

Each failure is accompanied by one of the following sub‑reasons, which provide additional detail about the root cause. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### ACCESS_DENIED

The runtime cannot access the specified location. The error includes the underlying reason: `Cannot access the location. Error: <error>`. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### CANNOT_BE_BLANK

The property was set to an empty string or a blank value. A non‑blank path is required. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DIRECTORY_NOT_EMPTY

The specified directory `<path>` already contains files or subdirectories. The location must be empty. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### DOES_NOT_EXIST

The specified path `<path>` does not exist in the storage system. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_DIRECTORY

The specified path `<path>` exists but is not a directory (for example, it is a file). ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### NOT_SET

The configuration property `delta.universalFormat.compatibility.location` has not been set at all. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Resolution

To resolve any of these errors, ensure that: ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

1. The property is set to a non‑blank, valid path.
2. The path refers to an existing directory (not a file) in the storage system.
3. The directory is empty before the table property is used.
4. The caller has appropriate read/write permissions on the location.

## Related Concepts

- [Uniform format compatibility](/concepts/delta-uniform-universal-format-compatibility.md) — the feature that this property enables
- [Delta Lake table properties](/concepts/delta-lake-reader-table-features.md) — other configuration options for Delta tables
- [Iceberg and Delta Lake interoperability](/concepts/delta-lake-table-features-and-iceberg-compatibility.md)

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
