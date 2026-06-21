---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a9395eac2d50f7fcdae17d2de5c7514fb5e32af9f434760db3020c9939f26b4
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-metadata-versioning-in-delta-uniform
    - IMVIDU
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: Iceberg Metadata Versioning in Delta Uniform
description: The requirement that Iceberg metadata locations used to refresh a Delta Uniform table must have monotonically increasing version numbers, and UUID consistency must be maintained.
tags:
  - databricks
  - delta-uniform
  - apache-iceberg
  - versioning
timestamp: "2026-06-18T15:23:31.119Z"
---

# Iceberg Metadata Versioning in Delta Uniform

**Iceberg Metadata Versioning in Delta Uniform** refers to the mechanisms and constraints that govern how Delta Uniform manages Apache Iceberg metadata files when enabling read compatibility with Iceberg readers. Proper versioning ensures consistency and prevents errors when Iceberg metadata is generated or refreshed from Delta table state.

## Overview

Delta Uniform automatically generates Apache Iceberg metadata files to make Delta tables readable by Iceberg-compatible engines. These metadata files follow Iceberg's versioning conventions, where each metadata file has a version number embedded in its filename (e.g., `00001-<uuid>.metadata.json`). Delta Uniform must correctly parse and track these version numbers to maintain compatibility.^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Version Parsing

When Delta Uniform reads or generates Iceberg metadata, it parses the version number from the metadata file location. If the file name does not follow the expected Iceberg convention, the operation fails with an error. This ensures that only properly formatted Iceberg metadata files are used.^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

The relevant error condition states:

> Failed to parse version from existing metadata location `<existingLocation>` or current metadata location `<currentLocation>`.

This error indicates that the Iceberg writer producing the metadata file did not follow the required file naming convention.^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Versioning Constraints for Refresh Operations

When Delta Uniform refreshes existing Iceberg metadata for a table, the metadata location to be refreshed must have a higher version number than the existing metadata location. This monotonic versioning requirement prevents conflicts and ensures that readers always progress forward through metadata versions.^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

If a refresh attempt uses metadata from a different Iceberg table (identified by a different table UUID), the operation is rejected:

> Refresh existing Apache Iceberg table UUID `<existingId>`, with metadata from different Apache Iceberg table UUID `<currentId>` is not supported.^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Common Errors

### DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION

This error class covers violations of Iceberg metadata versioning rules. Key sub-errors include:^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

| Sub-error | Cause |
|-----------|-------|
| Version parse failure | Iceberg metadata file name does not follow expected versioning convention |
| Must refresh same table | Attempting to refresh metadata from a different Iceberg table (different UUID) |
| Missing version increment | Refresh metadata version is not higher than existing metadata version |

## Troubleshooting

- **Check file naming**: Verify that Iceberg metadata files follow the standard naming convention (`<version>-<uuid>.metadata.json`). The version number must be a monotonically increasing integer.^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- **Verify table identity**: Ensure that refresh operations reference metadata from the same Iceberg table (same UUID) as the existing metadata.^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- **Check version progression**: Confirm that the new metadata location has a version number strictly greater than the existing metadata location.^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature that enables Iceberg read compatibility for Delta tables
- Apache Iceberg Metadata — The metadata layer that tracks table versions and snapshots
- Delta Lake Table Properties — Table properties that store Iceberg metadata references
- Iceberg Table UUID — Unique identifier for an Iceberg table
- [Delta Uniform Compatibility Errors](/concepts/delta-uniform-compatibility-format.md) — Other error conditions related to Delta Uniform

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)
