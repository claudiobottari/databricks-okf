---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a1a724e5c16f0521eb1ebdbf417713ec358b3c4089011353fac268144961e5c
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-error-classes-pattern
    - DECP
title: Databricks error classes pattern
description: The structured error classification system used in Databricks, where error classes group multiple specific error conditions under a single identifier with SQLSTATE codes
tags:
  - databricks
  - error-messages
  - architecture
timestamp: "2026-06-19T18:22:38.171Z"
---

# Databricks Error Classes Pattern

Databricks error messages are organized into **error classes**, each with a unique name, a SQLSTATE code, and a set of sub‑conditions that provide specific failure details. This structured pattern allows users to identify the general category of an error and then drill into the precise cause.

## Structure

Every Databricks error class page follows a consistent layout:

- **Error class name** – A capitalized, underscore‑delimited identifier, for example `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`.  
- **SQLSTATE** – A five‑character code following the SQL standard (e.g., `0AKDC` for feature‑not‑supported errors). The documentation links to the [SQLSTATE reference](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported) for the class.  
- **Sub‑conditions** – One or more named conditions that refine the failure reason. Each condition has a short title and a human‑readable message.  

An example from the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` class shows two sub‑conditions:

- `NON_DELTA` – “Source table of `<format>` format is not supported.”  
- `TIME_TRAVELLED_BY_TIMESTAMP` – “Source table time travelled by timestamp is not supported.”

## Usage

When an error occurs, Databricks typically returns the error class name, the SQLSTATE, and the specific sub‑condition that triggered the failure. This lets downstream code handle errors programmatically by switching on the class name or sub‑condition, and also gives human readers a clear diagnostic message.  

The error class documentation is part of a broader set of Error classes in Databricks pages. Each class page explains the error’s cause and, in some cases, corrective actions.

## Related Concepts

- SQLSTATE codes – The standard codes that categorize error severity and class.
- Error classes in Databricks – The top‑level index of all defined error classes.

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
