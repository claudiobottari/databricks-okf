---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47d6c3cbf8d833cc81db5d8263753492279a8c77ee8267bc27b9dfd8a4180e3f
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_uniform_iceberg_ingress_violation
    - DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION
description: A Databricks error class that occurs when reading Apache Iceberg via Delta Uniform fails due to version parsing problems in metadata locations.
tags:
  - databricks
  - error-messages
  - delta-uniform
  - apache-iceberg
timestamp: "2026-06-19T15:08:23.542Z"
---

```yaml
---
title: DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION error condition
summary: An error that occurs when reading an Apache Iceberg table that uses Delta Uniform fails, typically due to incompatible metadata locations, missing table properties, or refresh version conflicts.
sources:
  - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:56:27.675Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - error-class
  - delta-uniform
  - iceberg
  - troubleshooting
aliases:
  - delta_uniform_iceberg_ingress_violation
  - duiiv
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION error condition

The **DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION** error (SQLSTATE: KD00E) occurs when a read operation against an Apache Iceberg table that uses [[Delta Uniform]] fails. Delta Uniform enables Iceberg readers to access Delta Lake tables by exposing a compatible Iceberg metadata layer. This error indicates that the metadata layer is malformed, inconsistent, or cannot be parsed by the reader. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## General Error Message

The root error appears as:

```
Read Apache Iceberg with Delta Uniform has failed.
Failed to parse version from existing metadata location <existingLocation> or current metadata location <currentLocation>;
```

The file name convention used by the Apache Iceberg writer must follow the Iceberg specification for versioned metadata files. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Sub-Errors

The error class includes two sub‑conditions that provide more specific diagnostics.

### MISSING_UNIFORM_TBL_PROPERTIES

Triggered when at least one of the required Delta table properties — `tableId`, `snapshotId`, or `metadataLocation` — is missing from the Delta table. The error message lists the missing identifier:

```
At least one of tableId <tableId>, snapshotId <snapshotId>, metadataLocation <location> is missing from Delta table properties; Is there manual change to the _delta_log?
```

This suggests that the `_delta_log` may have been manually altered, removing properties that Delta Uniform relies on to generate the Iceberg metadata. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

### MUST_REFRESH_SAME_TABLE

Triggered when attempting to refresh an existing Delta Uniform–enabled Apache Iceberg table using metadata from a different Iceberg table UUID. The error message includes both the existing UUID and the current UUID:

```
Refresh existing Apache Iceberg table UUID <existingId>, with metadata from different Apache Iceberg table UUID <currentId> is not supported.
```

Additionally, the metadata location used for the refresh must have a higher version number than the existing metadata location. If the version is not higher, an error is raised detailing both locations:

```
Metadata location to be refreshed must have a higher version than existing metadata location.
Existing metadata location <existingLocation>; current metadata location <currentLocation>.
```

^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Root Causes

Common causes inferred from the error messages include:

- **Manual changes to the Delta transaction log** (`_delta_log`) that delete or alter the table properties required by Delta Uniform.
- **Failed version parsing** from metadata locations, often due to file names that do not follow the Iceberg versioning convention.
- **Attempting to refresh the Iceberg metadata from a different table** (different UUID) or from a metadata version that is older than the current version. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [[Delta Uniform]] — The feature that exposes Delta Lake tables as Iceberg-compatible sources.
- [[Uniform (Apache Iceberg) Format|Apache Iceberg]] — The open table format that Delta Uniform targets for interoperability.
- [[Delta Lake]] — The underlying storage format.
- [[SQLSTATE KD00E]] — The datasource-specific error class for this condition.
- MISSING_UNIFORM_TBL_PROPERTIES — Sub‑error for missing table properties.
- MUST_REFRESH_SAME_TABLE — Sub‑error for refresh conflicts.

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)
