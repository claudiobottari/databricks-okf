---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7090e0206e24ff29c1e420f38dc9c2ff32d3232be257c17cdcb5ce33931fb3db
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-universal-format-uniform
    - DUF(
    - Delta Universal Format
    - Universal Format (UniForm)
    - Universal Format
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: Delta Universal Format (Uniform)
description: A Delta Lake feature for format compatibility that requires a valid empty directory location configuration
tags:
  - delta-lake
  - format-compatibility
  - databricks
timestamp: "2026-06-19T10:09:01.084Z"
---

Here is the wiki page for "Delta Universal Format (Uniform)", written based solely on the provided source material.

---

## Delta Universal Format (Uniform)

**Delta Universal Format (Uniform)** is a compatibility layer for [Delta Lake](/concepts/delta-lake.md) tables that enables interoperability with other table formats, such as Apache Iceberg or Apache Hudi. When Uniform compatibility is enabled, Delta Lake shares table metadata through a common location, allowing other ecosystem tools to read the Delta table. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

To activate this feature, a table property named `delta.universalFormat.compatibility.location` must be set. This property specifies an empty directory on cloud storage (e.g., Amazon S3, Azure Blob Storage, or Google Cloud Storage) that acts as the staging area for the compatibility format's metadata. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### Configuration Property

| Property | Description |
|----------|-------------|
| `delta.universalFormat.compatibility.location` | An empty directory path used as a staging area for the Universal Format compatibility layer. The directory must exist, be empty, and be accessible by the user or workload. |

### Error Condition

If the specified location is missing, blank, inaccessible, or invalid, Databricks raises the `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error (SQLSTATE 42601). The error message includes one of the following sub-reasons: ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

| Sub-reason | Description |
|---|---|
| `ACCESS_DENIED` | The user or workload cannot access the location. |
| `CANNOT_BE_BLANK` | The property value is empty or not provided. |
| `DIRECTORY_NOT_EMPTY` | The specified directory exists but contains files or subdirectories. |
| `DOES_NOT_EXIST` | The specified path does not exist. |
| `NOT_DIRECTORY` | The specified path exists but is not a directory (e.g., it points to a file). |
| `NOT_SET` | The configuration property `delta.universalFormat.compatibility.location` has not been set at all. |

### Resolution

To resolve the error, set the `delta.universalFormat.compatibility.location` table property to an empty, existing directory to which the user has read/write access. The directory must be truly empty — any contents will trigger the `DIRECTORY_NOT_EMPTY` sub-error. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### Related Concepts

- Delta Lake Table Properties
- [Delta Universal Format (Uniform) Configuration](/concepts/deltauniversalformatenabledformats-configuration.md)
- Error Messages in Databricks
- Delta Lake Compatibility

### Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
