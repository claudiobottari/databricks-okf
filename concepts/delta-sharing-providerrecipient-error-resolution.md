---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa5c2be1c56f434cf2e51058fef18fa7269e452dc1431d303fd3eca308138dea
  pageDirectory: concepts
  sources:
    - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-sharing-providerrecipient-error-resolution
    - DSPER
    - Delta Sharing Provider and Recipient Management
  citations:
    - file: delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
title: Delta Sharing Provider/Recipient Error Resolution
description: The bilateral error resolution approach in Delta Sharing where providers verify recipient property existence and recipients contact the data provider when property mismatches occur.
tags:
  - delta-sharing
  - troubleshooting
  - databricks
timestamp: "2026-06-19T15:06:54.748Z"
---

---
title: Delta Sharing Provider/Recipient Error Resolution
summary: How to resolve DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED, an error that occurs when a query references a recipient property that does not apply to the current Delta Sharing recipient.
sources:
  - delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md
kind: guide
createdAt: "2026-06-19T14:43:57.264Z"
updatedAt: "2026-06-19T14:43:57.264Z"
tags:
  - databricks
  - delta-sharing
  - error-resolution
  - troubleshooting
aliases:
  - delta-sharing-provider-recipient-error-resolution
  - DS-PRER
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Sharing Provider/Recipient Error Resolution

This page describes the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error condition that can occur in [Delta Sharing](/concepts/delta-sharing.md) queries, and provides steps for both the **provider** and the **recipient** to resolve it.

## Error Overview

The error is raised when a query references a recipient property that does not apply to the current recipient in the active session. The full error message states:

```
The data is restricted by recipient property <property> that do not apply to the current recipient in the session.
```

The error class is `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` with SQLSTATE `42704` (syntax error or access rule violation). ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Cause

A Delta Sharing Provider can define recipient properties on a share to restrict which recipients can access certain data. When a [recipient](/concepts/data-recipient.md) runs a query that depends on a property that has not been set for their specific recipient identity, the engine throws the `DELTA_SHARING_CURRENT_RECIPIENT_PROPERTY_UNDEFINED` error. This typically happens when the provider uses recipient‑property‑based row filters or column masks inside the shared view or table. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Resolution Steps

The resolution depends on which side of the sharing relationship you are on.

### For Providers

The provider must verify that the recipient property referenced in the share definition actually exists for the intended recipient. Check the following:

- Confirm that the recipient object exists in the provider’s [Metastore](/concepts/metastore.md).
- For the specific recipient, ensure that the property name used in the filter or mask is defined (e.g., `region`, `department`, `tenant_id`).
- If the property was recently added or renamed, verify the recipient’s property mapping is up‑to‑date.

After making corrections, the recipient can re‑run the query. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

### For Recipients

When you encounter this error as a recipient, contact the data provider and report the exact property name shown in the error message. The provider will need to either:

- Define the missing recipient property, or
- Adjust the sharing policy to remove the dependency on that property.

No changes can be made at the recipient side to resolve this error directly. ^[delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for secure data sharing across platforms.
- Delta Sharing Provider – The party that shares data using Delta Sharing.
- [Delta Sharing Recipient](/concepts/delta-sharing-recipient-object.md) – The party that receives access to shared data.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) – Data governance mechanisms that can rely on recipient properties.
- [SQLSTATE 42704](/concepts/sqlstate-42704.md) – The underlying SQL error code for undefined objects or properties.

## Sources

- delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md

# Citations

1. [delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws.md](/references/delta_sharing_current_recipient_property_undefined-error-condition-databricks-on-aws-847b80f0.md)
