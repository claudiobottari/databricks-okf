---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66c375708a3879352267e31c44c7db4ca23c836c50572ec7a78d298f0e5d2da6
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access_denied-delta-uniform-error
    - A(UE
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: ACCESS_DENIED (Delta Uniform error)
description: A sub-error of DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION indicating the location cannot be accessed.
tags:
  - databricks
  - error-messages
  - delta-uniform
  - permissions
timestamp: "2026-06-19T15:08:24.599Z"
---

# ACCESS_DENIED (Delta Uniform error)

**ACCESS_DENIED** is a sub-error condition of the `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error class in Databricks. It occurs when attempting to set a [Uniform Format](/concepts/delta-uniform-uniform.md) compatibility location that cannot be accessed due to insufficient permissions. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Message

The ACCESS_DENIED error returns the following message:

```
Cannot access the location. Error: <error>
```

^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Cause

This error occurs when the [delta.universalFormat.compatibility.location](/concepts/deltauniversalformatcompatibilitylocation.md) configuration property is set to a path that the requesting identity does not have permission to access. The specific access failure details are included in the `<error>` portion of the message. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

The error belongs to [SQLSTATE class 42|SQLSTATE: 42601](/concepts/sqlstate-42601.md) (syntax error or access rule violation). ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Related Sub-Errors

The ACCESS_DENIED error is one of several sub-conditions under the `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error class. Other related sub-errors include:

- **CANNOT_BE_BLANK (Delta Uniform error) | CANNOT_BE_BLANK** – The location cannot be blank.
- **DIRECTORY_NOT_EMPTY (Delta Uniform error)|DIRECTORY_NOT_EMPTY (Delta Uniform error) | DIRECTORY_NOT_EMPTY** – The specified directory is not empty.
- **DOES_NOT_EXIST (Delta Uniform error) | DOES_NOT_EXIST** – The specified location does not exist.
- **NOT_DIRECTORY (Delta Uniform error) | NOT_DIRECTORY** – The specified location is not a directory.
- **NOT_SET (Delta Uniform error) | NOT_SET** – The configuration is not set.

## Resolution

To resolve the ACCESS_DENIED error, ensure that the location specified in `delta.universalFormat.compatibility.location` is accessible by the identity executing the operation. Verify that the necessary permissions are granted and that the path is valid and accessible. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Related Concepts

- [Uniform Format](/concepts/delta-uniform-uniform.md) – The feature that requires the compatibility location configuration.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format for which Uniform compatibility is configured.
- Cloud Storage Permissions – General guidance on accessing cloud storage from Databricks.

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
