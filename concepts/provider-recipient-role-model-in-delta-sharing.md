---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9f1d8fa065f7ddf08fcb577c1fca0e948e2c45522a88fc75fc42f69fbdcd120
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 0.75
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - provider-recipient-role-model-in-delta-sharing
    - PRMIDS
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: Provider-Recipient Role Model in Delta Sharing
description: The two-party governance model in Delta Sharing where providers configure data access rules and recipients verify or contact providers when access issues arise.
tags:
  - databricks
  - delta-sharing
  - architecture
timestamp: "2026-06-18T11:55:15.647Z"
---

# Provider-Recipient Role Model in Delta Sharing

**Delta Sharing** defines a clear separation of responsibilities between the **provider** (data owner) and the **recipient** (data consumer). The **Provider-Recipient Role Model** describes how these two parties interact within the Delta Sharing protocol, including how [Recipient Properties](/concepts/recipient-properties.md) are used to control access and how the recipient must respond when a property condition fails.

## Overview

In Delta Sharing, the provider is the party that grants access to shared data, while the recipient is the party that consumes the shared data. The provider controls access by creating managed shares and [recipient objects](/concepts/recipient-object-delta-sharing.md) that define which data the recipient can access. The recipient connects to the provider's sharing endpoint and reads the data using the credentials and properties assigned by the provider.

## Recipient Properties

Recipient properties are key-value attributes that the provider attaches to a recipient object. These properties serve multiple purposes:

- **Access control**: The provider can use recipient properties in [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md) to restrict what data the recipient sees.
- **Auditing**: Properties help identify which recipient is making requests.
- **Configuration**: Properties can convey connection-specific settings.

The provider sets these properties when creating or modifying the recipient. The recipient does not have the ability to change them.

## Error Condition: DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED

The error `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` (SQLSTATE: 42704) occurs when a Delta Sharing operation references a recipient property that does not exist for the current recipient in the session. This means the provider has defined a restriction or condition that depends on a property, but the recipient does not have that property defined. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### SQLSTATE

This error has SQLSTATE 42704, which falls under the [Class 42 — Syntax Error or Access Rule Violation](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation) category. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Role Responsibilities

### Provider Responsibilities

As the data owner, the provider is responsible for: ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

1. **Defining recipient properties**: The provider must create and maintain the recipient properties that govern data access.
2. **Ensuring property consistency**: The provider must verify that any recipient property referenced in ABAC policies or [GRANT policies](/concepts/grant-policies-beta.md) actually exists on the recipient.
3. **Diagnosing errors**: When the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error occurs, the provider should verify the recipient or recipient property exists. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]
4. **Correcting property assignments**: If a property is missing, the provider must add it or update the policies that reference it.

### Recipient Responsibilities

As the data consumer, the recipient is responsible for: ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

1. **Contacting the provider**: When a property-related error occurs, the recipient cannot resolve it independently. The recipient must contact the data provider to address the issue. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]
2. **Reporting the error**: The recipient should provide the provider with enough context about the failed operation (such as the query or data request that triggered the error) to help the provider diagnose the missing property.
3. **Waiting for provider action**: The recipient cannot modify recipient properties. Only the provider can make changes.

## Common Scenarios

### Scenario A: Provider Missing a Property

A provider sets up a [row filter policy](/concepts/row-filter-policies.md) that uses `has_tag_value('department', 'engineering')`. The provider then creates a recipient for a marketing team but forgets to add the `department` tag. When the marketing recipient queries the data, they receive `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED`. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

**Provider response**: Add the missing tag to the recipient or adjust the policy to remove the requirement.

### Scenario B: Recipient Property in a GRANT Policy

A provider uses an [ABAC GRANT Policy](/concepts/abac-grant-policy.md) that grants `EXECUTE` on models only when `has_tag_value('lifecycle', 'production')`. If the production team recipient does not have the `lifecycle` tag, the policy does not grant access, and the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error may appear. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

**Provider response**: Add the `lifecycle` tag with value `production` to the recipient, or change the policy to use a different condition.

### Scenario C: Recipient Property in a Column Mask Policy

A provider has a [column mask policy](/concepts/column-mask-policies.md) that masks columns unless the recipient has a specific governing tag. If the tag is missing from the recipient, the column is masked instead of showing the data. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

**Provider response**: Add the required tag to the recipient, or change the policy to use a different condition.

## Best Practices

### For Providers

- **Document all recipient properties** that are required for access. Maintain a clear list of which properties each recipient must have.
- **Validate property existence** before granting access. Use [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md) to check that policies will apply correctly.
- **Test with a development recipient** first to confirm property configurations work.
- **Communicate property requirements** to recipients so they know what to expect.

### For Recipients

- **Keep a record of granted properties** so you can track which properties are expected.
- **Report errors promptly** to the provider when you encounter `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED`.
- **Do not attempt to bypass** property checks. The provider controls access, and any attempt to bypass it may violate security policies.

## Relationship to Other Delta Sharing Concepts

- Managed shares — The way providers package data for sharing
- [Recipient objects](/concepts/recipient-object-delta-sharing.md) — The target that receives the shared data
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that can use recipient properties
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask data based on recipient properties
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Grant policies that use recipient properties for access control
- [Governed Tags](/concepts/governed-tags.md) — Tags that drive ABAC policy evaluation

## Sources

- [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](https://docs.databricks.com/aws/en/error-messages/delta-sharing-current-recipient-property-undefined-error-class)

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
