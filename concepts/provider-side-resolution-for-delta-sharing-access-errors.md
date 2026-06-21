---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b01adf764b1f66d64636116b048351f71f01bee36655381a5d145c4f875dadb3
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-side-resolution-for-delta-sharing-access-errors
    - PRFDSAE
    - recipient-side-resolution-for-delta-sharing-access-errors
    - RRFDSAE
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: Provider-side resolution for Delta Sharing access errors
description: Troubleshooting guidance where the data provider must verify that the recipient or recipient property exists and is correctly configured.
tags:
  - delta-sharing
  - troubleshooting
  - databricks
timestamp: "2026-06-18T15:21:45.472Z"
---

# Provider-side resolution for Delta Sharing access errors

When a Delta Sharing recipient encounters access errors, the resolution typically requires action from the data provider who owns and manages the shared data. This page describes common provider-side remedies for Delta Sharing access errors, focusing on the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error condition.

## Overview

Delta Sharing access errors can occur when a recipient attempts to access shared data but the sharing configuration contains conditions that cannot be satisfied by the current recipient's session or properties. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Common Error: Recipient Property Undefined

The `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error occurs with SQLSTATE 42704 (syntax error or access rule violation) when data is restricted by a [recipient property](/concepts/recipient-properties.md) that does not apply to the current recipient in the session. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### Error Message

The error message states that the data is restricted by a recipient property that is not defined for the current recipient: ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

```
DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED: The data is restricted by recipient property `<property>` that does not apply to the current recipient in the session.
```

## Provider-Side Resolution

### Verify Recipient or Recipient Property Exists

The provider should verify that the recipient or the recipient property referenced in the sharing configuration actually exists: ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

1. **Check recipient existence**: Confirm that the recipient identified in the error is a valid, active recipient in the [Delta Sharing](/concepts/delta-sharing.md) provider's system.
2. **Verify property definitions**: Ensure any [Recipient Properties](/concepts/recipient-properties.md) referenced in the sharing configuration are properly defined and have the expected values.
3. **Review property assignments**: Check that the recipient has been assigned all properties required by the sharing configuration.

### Ensure Property Exists

If the property is missing, define it for the recipient by: ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

- Adding the required property to the recipient's configuration
- Ensuring the property value matches what the sharing definition expects
- Verifying the property is spelled correctly and uses the correct format

## Recipient-Side Actions

### Contact the Data Provider

If you are a recipient experiencing this error, contact the data provider to report the issue: ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

- Provide the full error message, including the property name
- Share your recipient identifier or other identifying information
- Describe the data you are trying to access

The provider can then take the steps described above to resolve the issue. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms
- [Recipient Properties](/concepts/recipient-properties.md) — Configuration attributes assigned to Delta Sharing recipients
- [Delta Sharing providers and recipients](/concepts/delta-sharing-recipient-object.md) — The roles in a Delta Sharing relationship
- [SQLSTATE 42704](/concepts/sqlstate-42704.md) — Syntax error or access rule violation class

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
