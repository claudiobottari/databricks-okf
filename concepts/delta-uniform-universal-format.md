---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 058c8773ef0f984c16a8bae4724b9090a5dae1b140abe09e86ffe80dc974fc48
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 0.6
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-uniform-universal-format
    - DU(F
    - delta-uniform-delta-universal-format
    - DU(UF
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: Delta UniForm (Universal Format)
description: A Databricks Delta Lake feature enabling interoperability with other table formats like Apache Iceberg and Apache Hive by writing metadata in those formats alongside Delta metadata.
tags:
  - delta-lake
  - databricks
  - table-formats
timestamp: "2026-06-19T18:27:45.993Z"
---

# Delta UniForm (Universal Format)

The **DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION** error class is returned when the location specified for Uniform compatibility format is missing or invalid. This error occurs when setting the Delta table property `delta.universalFormat.compatibility.location`. The property must point to an empty directory that Databricks can use for compatibility metadata. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Reasons ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### ACCESS_DENIED

```
Cannot access the location. Error: <error>
```

The system does not have permission to read from or write to the specified location.

### CANNOT_BE_BLANK

The location string is empty. A non‑empty path must be provided.

### DIRECTORY_NOT_EMPTY

```
The specified directory <path> is not empty.
```

The directory already contains files or subdirectories. The compatibility location must be an empty directory.

### DOES_NOT_EXIST

```
The specified location <path> does not exist.
```

The provided path does not correspond to an existing location in the cloud storage.

### NOT_DIRECTORY

```
The specified location <path> is not a directory.
```

The path resolves to a file or object, not a directory.

### NOT_SET

The configuration `delta.universalFormat.compatibility.location` has not been set.

## Related Concepts

- [Delta Lake table properties](/concepts/delta-lake-reader-table-features.md)
- Storage locations on Databricks
- Apache Iceberg compatibility

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
