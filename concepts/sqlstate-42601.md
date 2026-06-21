---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 650104ee11669e06d5797f8cb581bee19050838b56eb6e72d7c779779eea145a
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-42601
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: SQLSTATE 42601
description: A SQL state code indicating a syntax error or access rule violation, used as the parent error class for the DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION error.
tags:
  - error-messages
  - sql
  - standard
timestamp: "2026-06-19T18:27:38.394Z"
---

# SQLSTATE 42601

**SQLSTATE 42601** is a five-character SQL state code that classifies a **syntax error or access rule violation** (class 42). It is a standard ANSI/ISO code used by database systems to indicate a problem with SQL syntax or a violation of access rules. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Usage in Databricks

On Databricks, SQLSTATE 42601 is returned by the **DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION** error condition. This error occurs when the configuration setting `delta.universalFormat.compatibility.location` is missing, blank, or points to an invalid directory. The error is raised when trying to enable Uniform format compatibility for a [Delta table](/concepts/delta-lake-table.md). ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

### Sub‑conditions

The error provides one of the following detailed failure reasons in the message body: ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

| Reason | Description |
|--------|-------------|
| `ACCESS_DENIED` | Cannot access the location. Error: `<error>` |
| `CANNOT_BE_BLANK` | The location cannot be blank. |
| `DIRECTORY_NOT_EMPTY` | The specified directory `<path>` is not empty. |
| `DOES_NOT_EXIST` | The specified location `<path>` does not exist. |
| `NOT_DIRECTORY` | The specified location `<path>` is not a directory. |
| `NOT_SET` | The config is not set. |

These sub‑conditions help identify the exact cause of the invalid location. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, set the `delta.universalFormat.compatibility.location` configuration to an empty directory path that is accessible. The specified location must exist, must be a directory, must be empty, and must be accessible by the user or service principal performing the operation. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Related Concepts

- SQLSTATE – Overview of SQL state codes and their classifications.
- [Delta Sharing Uniform Format](/concepts/delta-uniform-uniform.md) – Feature that uses the compatibility location setting.
- Delta table configuration – How settings like `delta.universalFormat.compatibility.location` are managed.
- [Error handling in Databricks](/concepts/error-handling-in-databricks-notebook-workflows.md) – General approach to diagnosing and resolving Databricks errors.

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
