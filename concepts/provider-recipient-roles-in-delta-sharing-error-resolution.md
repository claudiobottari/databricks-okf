---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60cb062e99e88f9c5efb105848f772d970391d29dbe514e25cd103ec523aed52
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-recipient-roles-in-delta-sharing-error-resolution
    - PRIDSER
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: Provider-Recipient roles in Delta Sharing error resolution
description: The separation of responsibilities between data providers and data recipients when resolving Delta Sharing access errors
tags:
  - delta-sharing
  - roles
  - troubleshooting
  - databricks
timestamp: "2026-06-19T18:26:28.761Z"
---

# Provider-Recipient Roles in Delta Sharing Error Resolution

When a [Delta Sharing](/concepts/delta-sharing.md) recipient encounters the error condition `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED`, resolution depends on whether the user is acting as a **data provider** or a **data recipient**. The error indicates that data access is restricted by a recipient property that does not apply to the current recipient in the session. This error has the SQLSTATE `42704` (Class 42 – Syntax error or access rule violation). ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Provider Responsibilities

The data provider must verify that the recipient or the recipient property referenced in the sharing configuration actually exists. This may involve checking that the recipient has been correctly defined in the sharing system and that any conditional property (such as a token or attribute) is properly assigned to the intended recipient. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Recipient Responsibilities

The data recipient should contact the data provider to resolve the issue. The recipient cannot fix the misconfigured property themselves because the restriction is enforced on the provider side. The provider must adjust the sharing policy so that the recipient property matches the current recipient’s identity. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Role-Based Resolution Summary

| Role | Action |
|------|--------|
| PROVIDER | Verify the recipient or recipient property exists. |
| RECIPIENT | Contact the data provider to resolve the issue. |

Both parties must collaborate to ensure that the recipient’s session is associated with a property that matches the provider’s access rule. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Delta Sharing Recipient](/concepts/delta-sharing-recipient-object.md)
- Delta Sharing Provider
- [Error handling in Databricks](/concepts/error-handling-in-databricks-notebook-workflows.md)

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
