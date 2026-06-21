---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3baf00b469c1022f13c0817379c8cf555a1cd44ff01ff41db7f18fd51b8d9499
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_sharing_current_recipient_property_undefined
    - delta_sharing_current_recipient_property_undefined-error-condition
    - DEC
    - delta_sharing_current_recipient_property_undefined-error
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED
description: A Databricks error condition raised when a Delta Sharing recipient property referenced in a query does not apply to the current recipient in the session.
tags:
  - databricks
  - delta-sharing
  - error-messages
timestamp: "2026-06-18T11:54:48.834Z"
---

# DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED

The **DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED** error condition occurs when a [Delta Sharing](/concepts/delta-sharing.md) query attempts to enforce a recipient property that does not apply to the current recipient in the session. The error indicates that the data is restricted by a recipient property that is either missing, misconfigured, or not applicable to the recipient making the request. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Error Details

| Property | Value |
|----------|-------|
| SQLSTATE | `42704` (Syntax error or access rule violation) |
| Error class | `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` |

The SQLSTATE 42704 belongs to class 42, which covers syntax errors or access rule violations. In this context, the error reflects an access rule violation caused by a mismatch between the recipient property used in a data restriction and the properties associated with the current recipient. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Cause

The data provider has defined a [recipient property](/concepts/recipient-properties.md) as a condition on a share or view (for example, filtering data based on a property such as `department` or `region`). When a recipient connects and runs a query, Delta Sharing evaluates the property against the current recipient's properties. If the property referenced in the restriction does not exist for the current recipient, the query fails with this error. Common causes include:

- The recipient property was removed or renamed after the share was created.
- The recipient does not have the property assigned at all.
- A typo in the property name on the provider side.

## Resolution

### For Providers

Verify that the recipient has the required property defined. You can list and manage recipient properties using the `ALTER RECIPIENT` SQL command or the Catalog Explorer. Ensure the property name used in the share or view condition exactly matches the property assigned to the recipient. If the property is missing, either assign it to the recipient or update the data restriction to use a property that all intended recipients possess. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### For Recipients

Contact the data provider to resolve the issue. As a recipient, you cannot modify the recipient properties; the provider must ensure that the property exists and is correctly configured for your recipient. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms
- [Recipient Properties](/concepts/recipient-properties.md) — Key-value pairs attached to a Delta Sharing recipient for row-level security
- [SQLSTATE 42704](/concepts/sqlstate-42704.md) — The SQL standard error code for this condition
- Error Classes in Databricks — The error classification system used in Databricks
- [Delta Sharing Provider and Recipient Management](/concepts/delta-sharing-providerrecipient-error-resolution.md) — How to create and manage recipients and their properties

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
