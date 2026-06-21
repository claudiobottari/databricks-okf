---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f553dd22bd8df0adb0c1745ff8862a7822194f6594d6f68019598a5efe12534
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-sharing-recipient-properties
    - DSRP
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: Delta Sharing recipient properties
description: Configurable properties on Delta Sharing recipients that can restrict or control data access
tags:
  - delta-sharing
  - access-control
  - databricks
timestamp: "2026-06-19T18:26:28.163Z"
---

# Delta Sharing Recipient Properties

**Delta Sharing recipient properties** are properties assigned to a recipient in a [Delta Sharing](/concepts/delta-sharing.md) share that restrict data access. When a query references a recipient property that has not been defined for the current recipient, the system raises the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## The `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` Error

- **SQLSTATE:** 42704  
- **Error message:**  
  ```
  The data is restricted by recipient property `<property>` that do not apply to the current recipient in the session.
  ```
  ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

This error occurs when a data provider has created a data restriction that depends on a recipient property, but that property is missing for the recipient executing the query. Because the restriction cannot be evaluated, the system denies access. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Resolution

### For the Provider

Verify that the recipient exists and that the referenced property has been set on it. Use commands such as `DESCRIBE RECIPIENT <recipient_name>` to list current properties and `ALTER RECIPIENT ... SET PROPERTIES (...)` to add missing properties. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### For the Recipient

If the recipient encounters this error, they should contact the data provider and ask them to verify or add the required recipient property. Once the provider resolves the issue, the recipient can retry the query. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across platforms
- [Recipient management](/concepts/recipient-lifecycle-management.md) – Creating and managing recipients and their properties
- [Row Filter Policies](/concepts/row-filter-policies.md) – Attribute-based restrictions that can use recipient properties
- [Column Mask Policies](/concepts/column-mask-policies.md) – Attribute-based masking that can use recipient properties

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
