---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbade18d51ca8219a2adf86a46f6102f71d8b8a127d4a12a8dc111ba62a0fa35
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-side-resolution-for-delta-sharing-access-errors
    - RRFDSAE
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: Recipient-side resolution for Delta Sharing access errors
description: Troubleshooting guidance where the data recipient must contact the data provider to resolve property misconfiguration issues.
tags:
  - delta-sharing
  - troubleshooting
  - databricks
timestamp: "2026-06-18T15:21:50.358Z"
---

# Recipient-Side Resolution for Delta Sharing Access Errors

**Recipient-Side Resolution for Delta Sharing Access Errors** refers to the actions a data recipient can take when they encounter the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error condition while querying a Delta Share.

## Overview

Delta Sharing uses recipient properties to control data access. When a recipient tries to query a share, the provider may have defined a restriction based on a specific recipient property (e.g., `region` or `department`). If the current recipient’s session does not have that property defined, or the property does not match, Databricks raises the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Error Details

| Field | Value |
|-------|-------|
| **SQLSTATE** | `42704` (Class 42 – Syntax error or access rule violation) |
| **Error class** | `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` |
| **Error message** | The data is restricted by recipient property `<property>` that do not apply to the current recipient in the session. |

The property name is substituted in the message at the placeholder `<property>`. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Recipient-Side Resolution

When a recipient sees this error, they have one recommended action:

**Contact the data provider.** The recipient cannot resolve the issue on their own because it involves changes to the share configuration or the recipient’s properties within the provider’s [Delta Sharing](/concepts/delta-sharing.md) setup. The provider must verify that the recipient exists and that the required recipient property (e.g., a tag or attribute) is correctly defined for that recipient. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Provider-Side Resolution

While the recipient cannot fix the error, it is useful to understand what the provider can do:

- **Verify the recipient** exists in the provider’s Databricks account.
- **Verify the recipient property** exists and is set to an expected value. The property that appears in the error message must be defined for the recipient’s configuration.

If the provider resolves the missing or mismatched property, the recipient will be able to query the share without this error. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across platforms
- [Recipient Properties](/concepts/recipient-properties.md) – Key-value attributes used to control data access in Delta Sharing
- Error Classes in Databricks – The classification of error messages, including SQLSTATE codes
- [SQLSTATE 42704](/concepts/sqlstate-42704.md) – The syntax error or access rule violation class

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
