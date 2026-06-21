---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bee8cb51266d1f9ac316483af78f281e3b2e63d5e421eb0d3bbba73b287c4491
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-42704
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: SQLSTATE 42704
description: A SQL standard error code (class 42) indicating a syntax error or access rule violation, associated with undefined objects
tags:
  - sql-standard
  - error-codes
  - databricks
timestamp: "2026-06-19T18:26:46.317Z"
---

Here is the wiki page for "SQLSTATE 42704" based solely on the provided source material.

# SQLSTATE 42704

**SQLSTATE 42704** is a SQL standard error code indicating a syntax error or access rule violation. It is assigned to the **Class 42 – Syntax Error or Access Rule Violation** category within the SQL standard classification system and is used by Databricks to signal an undefined object or data type. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Databricks Usage

In Databricks, SQLSTATE 42704 is raised by the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error condition. This error occurs when a recipient property referenced by a query does not apply to the current recipient in the session. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### Error Message

The full error message associated with this error condition is:

> The data is restricted by recipient property `<property>` that do not apply to the current recipient in the session.

The placeholder `<property>` identifies the missing or mismatched recipient property. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### Context

This error is specific to [Delta Sharing](/concepts/delta-sharing.md) scenarios where a data provider has defined a recipient property to restrict access to shared data, but the recipient making the query does not have that property defined or the property does not match. The error condition name explicitly includes `DELTA_SHARING`, indicating the context in which it occurs. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### Provider Actions

The data provider should verify that the recipient or the recipient property exists in the [Delta Sharing](/concepts/delta-sharing.md) configuration. If the property is missing, the provider must define it and assign it to the appropriate recipient. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### Recipient Actions

The data recipient should contact the data provider to resolve the issue, as the property is not defined for the recipient's session. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Related Concepts

- SQLSTATE Error Classes – The classification system for SQL error codes.
- [Delta Sharing](/concepts/delta-sharing.md) – The data sharing protocol where this error commonly occurs.
- [Recipient Properties](/concepts/recipient-properties.md) – Properties that define access permissions in Delta Sharing.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog system that enforces recipient-based access restrictions.

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
