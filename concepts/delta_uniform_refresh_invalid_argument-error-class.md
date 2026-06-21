---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4679bb521ebed3ba97f853b995e9e875de4ed5bbbfcc5de8721f378085d22c04
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_uniform_refresh_invalid_argument-error-class
    - DEC
title: DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT Error Class
description: A Databricks error condition raised when an invalid argument is passed to a Delta UniForm refresh operation on AWS.
tags:
  - databricks
  - error-messages
  - delta-lake
timestamp: "2026-06-19T18:28:35.410Z"
---

# DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT Error Class

The **DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT** error class is raised by Databricks when an invalid argument is passed to a [Delta Uniform](/concepts/delta-uniform.md) refresh operation. This error typically occurs when a user provides a parameter that is not recognized or is malformed in the context of refreshing a Delta table's Uniform (Lakehouse Federation) metadata. The exact invalid argument is reported in the error message returned with this class.

The source document for this error class does not contain a detailed description or example. Users encountering this error should consult the Databricks documentation for [Delta Uniform](/concepts/delta-uniform.md) and the REFRESH TABLE command to verify the allowed arguments and their correct syntax.

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — Feature for enabling Delta Lake tables to be read by other computing engines (e.g., Apache Iceberg, Apache Hudi).
- REFRESH TABLE — Command used to update metadata in Delta Uniform, such as converting to Iceberg format.
- [Databricks Error Classes](/concepts/databricks-error-classes.md) — General framework for handling structured error conditions on the platform.

## Sources

- delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
