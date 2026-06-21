---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40dd3e6f153d6cdbb9aa609b5aba7e2811683eee3a3b0e4604c4c95f20016110
  pageDirectory: concepts
  sources:
    - delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - directory_not_empty-delta-uniform-error
    - D(UE
    - DIRECTORY_NOT_EMPTY (Delta Uniform error) | DIRECTORY_NOT_EMPTY
  citations:
    - file: delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md
title: DIRECTORY_NOT_EMPTY (Delta Uniform error)
description: A sub-error of DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION indicating the specified directory already contains files.
tags:
  - databricks
  - error-messages
  - delta-uniform
timestamp: "2026-06-19T15:08:06.919Z"
---

# DIRECTORY_NOT_EMPTY (Delta Uniform error)

**DIRECTORY_NOT_EMPTY** is a sub‑condition of the DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION error class that occurs when configuring the [Uniform compatibility format](/concepts/delta-uniform-compatibility-format.md) for a Delta table. The error indicates that the directory specified by the configuration parameter `delta.universalFormat.compatibility.location` already contains files and is therefore not empty. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Error Message

When the condition is triggered, the error message is:

```
DIRECTORY_NOT_EMPTY: The specified directory <path> is not empty.
```

^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Cause

The Uniform compatibility format requires the location set for `delta.universalFormat.compatibility.location` to be an empty directory. If the directory contains any files or subdirectories, the system raises the `DIRECTORY_NOT_EMPTY` error to prevent unintended data mixing or conflicts. ^[delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md]

## Related Conditions

The `DELTA_UNIFORM_COMPATIBILITY_MISSING_OR_INVALID_LOCATION` error class includes several other sub‑conditions that may be encountered:

- **ACCESS_DENIED** – The location cannot be accessed.
- **CANNOT_BE_BLANK** – The location value is blank.
- **DOES_NOT_EXIST** – The specified path does not exist.
- **NOT_DIRECTORY** – The specified path is not a directory.
- **NOT_SET** – The configuration parameter is not set.

## Resolution

To resolve the error, ensure that the directory referenced by `delta.universalFormat.compatibility.location` is an existing, empty directory prior to setting the configuration. The source material does not provide further steps beyond stating the condition.

## Sources

- delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws.md](/references/delta_uniform_compatibility_missing_or_invalid_location-error-condition-databricks-on-aws-4606cc9c.md)
