---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f47ed6e45ec32230a076e2d5c976522b925050af349f82c018da3cce2ae0d50
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-delta-log-location
    - DUDLL
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Delta Log Location
description: The delta_log directory within a Delta Uniform table that is critical for ingress operations; errors occur when it is missing, unexpected, or when the metadata path cannot be found.
tags:
  - delta-uniform
  - delta-log
  - table-metadata
  - databricks
timestamp: "2026-06-19T10:09:30.011Z"
---

---
title: Delta Uniform Delta Log Location
summary: The location of the Delta log directory for a table being read via the Delta Uniform format, which must exist and be at an expected path for a uniform ingress table.
sources:
  - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - delta-uniform
  - iceberg
  - error-messages
  - metadata
aliases:
  - delta-uniform-delta-log-location
  - DUDLL
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Uniform Delta Log Location

**Delta Uniform Delta Log Location** refers to the metadata path (the `_delta_log` directory) that Delta Uniform requires when reading a table that was ingested via the [uniform ingress](/concepts/uniform-ingress-table.md) protocol. The Delta log location must be present and at the expected path for a [Uniform Ingress Table](/concepts/uniform-ingress-table.md); otherwise, reads fail with a `DELTA_UNIFORM_INGRESS_VIOLATION` error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Conditions

When the Delta log location is missing or unexpected, Databricks raises one of two sub-errors under the `DELTA_UNIFORM_INGRESS_VIOLATION` error class:

### DELTA_LOG_LOCATION_NOT_FOUND

Raised when the `_delta_log` directory does not exist for the table. The error message states:

```
The delta_log location is missing for table <tableName>.
Cannot find metadata path for table <tableName>.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

Raised when the Delta log path for the table does not match the expected location. The error message states:

```
Unexpected delta_log location <tablePath> for table <tableName>.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The protocol for reading and writing Delta tables with Iceberg compatibility.
- [Uniform Ingress](/concepts/uniform-ingress-table.md) – The process of writing Iceberg metadata into a Delta table so it can be read by Iceberg clients.
- [Uniform Ingress Table](/concepts/uniform-ingress-table.md) – A Delta table that has been set up with uniform ingress, generating Iceberg metadata.
- DELTA_UNIFORM_INGRESS_VIOLATION – The parent error class covering all uniform ingress read failures.
- Delta Log – The `_delta_log` directory containing transaction commits and metadata for Delta Lake tables.

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)
