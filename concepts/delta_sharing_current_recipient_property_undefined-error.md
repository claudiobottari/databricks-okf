---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6be3264aeb69b56461bc5044e12fff053c80cece5967982414b87f4621adc366
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_sharing_current_recipient_property_undefined-error
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED error
description: A Databricks error raised when a Delta Sharing recipient property restricting data access does not apply to the current recipient session
tags:
  - error-handling
  - databricks
  - delta-sharing
timestamp: "2026-06-19T18:26:28.544Z"
---

Here is the wiki page for "DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED error", written based solely on the provided source material.

---

# DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED Error

The **DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED error** (SQLSTATE: 42704) is a [Delta Sharing](/concepts/delta-sharing.md) error condition that occurs when a query attempts to access data that is restricted by a recipient property that does not apply to the current recipient in the session. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Error Details

When this error occurs, a [Delta Sharing](/concepts/delta-sharing.md) recipient has initiated a session, but the data they are trying to access has been restricted using a recipient property that is not defined or applicable to them. The property was likely set up by the data provider to control access, but the current recipient either does not have that property assigned or the property does not match. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

The error belongs to SQLSTATE class 42, which indicates a syntax error or access rule violation. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Roles and Responsibilities

### For Data Providers

If you encounter this error as a data provider, verify that the recipient or recipient property exists. Check that the recipient property has been correctly defined and assigned to the intended [Delta Sharing recipient](/concepts/delta-sharing-recipient-object.md). The property name referenced in the query or view definition must match exactly with an existing property on the recipient. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### For Data Recipients

If you encounter this error as a data recipient, contact the data provider to resolve the issue. The recipient property was defined by the provider and controls the data accessible to your session. You cannot modify these properties yourself. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Common Causes

- **Missing recipient property**: The data provider defined a property-based restriction on a [Delta Sharing view](/concepts/opensharing-views.md) or table, but the recipient does not have that property assigned.
- **Typographical errors**: A mismatch between the property name used in a view definition and the property assigned to the recipient.
- **Stale session**: The recipient's property assignment was changed after the session was established.

## Resolution Steps

### For Providers

1. Verify that the recipient property referenced in the error message has been created.
2. Check that the property is correctly assigned to the recipient that is getting the error.
3. Ensure there are no typographical differences between the property name in the view definition and the property assigned to the recipient.
4. After making corrections, ask the recipient to reconnect to establish a new session.

### For Recipients

1. Note the property name referenced in the error message.
2. Contact your data provider and share the error details, including the property name.
3. Reconnect to [Delta Sharing](/concepts/delta-sharing.md) after the provider confirms the issue is resolved.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms
- [Delta Sharing Recipient](/concepts/delta-sharing-recipient-object.md) — The entity that receives access to shared data
- [Recipient Properties](/concepts/recipient-properties.md) — Configurable attributes that control data access for recipients
- Delta Sharing Error Classes — The complete list of Delta Sharing error conditions
- [SQLSTATE 42704](/concepts/sqlstate-42704.md) — The SQL standard error code for undefined objects

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
