---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 178f5fc6c7cc9638f29ef6e905f697c3c9a66c435286f383404a7e1ba559ac66
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-iceberg-metadata-location-file-naming-convention
    - DUIMLFNC
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Iceberg Metadata Location File Naming Convention
description: The expected file naming convention for Apache Iceberg metadata files that must be followed by the Iceberg writer for Delta Uniform to correctly parse version information from metadata locations.
tags:
  - databricks
  - delta-uniform
  - apache-iceberg
  - file-conventions
timestamp: "2026-06-18T15:23:33.211Z"
---

# Delta Uniform Iceberg Metadata Location File Naming Convention

The **Delta Uniform Iceberg Metadata Location File Naming Convention** refers to the expected format and versioning pattern that Apache Iceberg metadata files must follow when used with Delta Lake's Uniform feature. Databricks enforces this convention when reading Iceberg metadata through Delta Uniform. Violating the naming convention results in a `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Error Condition

The `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error (SQLSTATE: KD00E) occurs when the Apache Iceberg writer used to generate metadata does not follow the required file naming convention. The error message indicates that Databricks failed to parse the version from either the existing metadata location or the current metadata location:

```
Read Apache Iceberg with Delta Uniform has failed.

Failed to parse version from existing metadata location <existingLocation>
or current metadata location <currentLocation>;

Check the file name convention on Apache Iceberg writer.
```

^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Required Naming Convention

The exact file naming format is enforced when Delta Uniform attempts to read Iceberg metadata. If the version number cannot be extracted from the metadata file path — for example, because the file name does not follow the expected pattern — the operation fails with this error condition. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

The metadata file names must be parseable to extract a version number that determines ordering. The version number in the filename is critical because it determines the metadata lineage and ensures that refresh operations apply only to newer versions. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Error Conditions

### MISSING_UNIFORM_TBL_PROPERTIES

This sub-error occurs when necessary Delta table properties are missing, which can happen if there is manual tampering with `_delta_log`:

```
At least one of tableId <tableId>, snapshotId <snapshotId>,
metadataLocation <location> is missing from Delta table properties;
Is there manual change to the _delta_log?
```

^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

### MUST_REFRESH_SAME_TABLE

This sub-error occurs when attempting to refresh an existing Iceberg table with metadata from a different Iceberg table UUID:

```
Refresh existing Apache Iceberg table UUID <existingId>,
with metadata from different Apache Iceberg table UUID <currentId>
is not supported.

Metadata location to be refreshed must have a higher version
than existing metadata location.

Existing metadata location <existingLocation>;
current metadata location <currentLocation>;
```

^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Preventing the Error

To avoid the `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error:

- Ensure any Apache Iceberg writer used to produce metadata files follows the convention that the metadata file name contains a parseable, monotonically increasing version number. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- Avoid manual changes to `_delta_log` that could corrupt the required Delta table properties (`tableId`, `snapshotId`, `metadataLocation`). ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- When refreshing Iceberg metadata, always point to a metadata location with a strictly higher version than the existing metadata location. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- Do not attempt to refresh metadata from a different Iceberg table (different UUID). ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature that enables reading Iceberg metadata from Delta tables.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The table format being read through Delta Uniform.
- Delta Table Properties — Metadata properties required for Uniform to function.
- _delta_log — The transaction log directory in Delta Lake.

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)
