---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4cc9d4c82649453f77e723a03c8cc520e7f1d04f7af2d9eb5a6b8cb5bea18aba
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_sharing_current_recipient_property_undefined-error-condition
    - DEC
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED Error Condition
description: A Databricks error (SQLSTATE 42704) raised when a Delta Sharing query references a recipient property that does not apply to the current recipient in the session.
tags:
  - error-message
  - delta-sharing
  - databricks
  - access-control
timestamp: "2026-06-19T15:07:10.404Z"
---

Here is the wiki page for **DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED Error Condition**, written based solely on the provided source material.

---

# DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED Error Condition

**DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED** is a runtime error condition in [Delta Sharing](/concepts/delta-sharing.md) that occurs when a query references a recipient property that is not defined for the recipient currently logged into the session. The error is raised because the data provider has restricted data access based on a property that does not apply to the active recipient.

## Error Details

- **SQLSTATE**: `42704` (class 42 — syntax error or access rule violation) ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]
- **Error class**: `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]
- **Error message**: "The data is restricted by recipient property `<property>` that do not apply to the current recipient in the session." ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Common Scenarios

This error typically occurs when:

- A data provider defines [row filters](/concepts/row-filter-policies.md) or [column masks](/concepts/delta-lake-column-masks.md) that depend on recipient-specific properties (such as organization-level attributes or custom tags) ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]
- The recipient property referenced in the sharing policy does not exist or is not properly configured for the current user session ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]
- A recipient attempts to query shared data without having the required property defined in their recipient profile ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Resolution

### For Data Providers

**PROVIDER** error code guidance: ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

- Verify that the recipient property specified in the sharing configuration actually exists for the intended recipients
- Check that the recipient has been properly configured with the required properties
- Ensure that any properties referenced in [Delta Sharing](/concepts/delta-sharing.md) policies are correctly defined and assigned to recipients

### For Data Recipients

**RECIPIENT** error code guidance: ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

- Contact the data provider to verify that the required recipient property exists and is correctly configured
- Ask the provider to check that your recipient profile includes all necessary properties for accessing the shared data

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms
- [Recipient Properties](/concepts/recipient-properties.md) — Configuration attributes that define access permissions for shared data
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Access control mechanisms that can reference recipient properties
- Delta Sharing error classes — Collection of related error conditions in Databricks

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
