---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2ecd125d2edff808760cfb30f59b3ef52edd8cfa053e9c89d785a791582114b
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-sharing-security-model
    - DSSM
    - Delta Sharing Security
    - Shared View Security
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
title: Delta Sharing Security Model
description: The overarching security approach in Delta Sharing that uses function whitelisting, column-level security, and view definitions rather than raw table access to protect shared data.
tags:
  - delta-sharing
  - security
  - data-governance
timestamp: "2026-06-19T10:42:14.904Z"
---

# Delta Sharing Security Model

**Delta Sharing Security Model** describes the access control, data protection, and function‑restriction mechanisms that govern data sharing via the [Delta Sharing](/concepts/delta-sharing.md) protocol. On Databricks, the security model enforces fine‑grained controls to ensure that shared data is exposed only as intended by the data provider. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Key Principles

- **Provider‑controlled access**: Data providers define which recipients can access which tables, views, and volumes. Recipients cannot bypass the provider’s access policies.
- **Secure view materialisation**: When a provider shares a view, the recipient sees only the result of the view’s query. The provider can restrict the SQL functions available in that view to prevent unintended data leakage or code execution. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]
- **Function whitelisting**: In [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md), the system only allows a predefined subset of built‑in SQL functions and operators. This restriction is applied “to keep your data secure” and reduces the attack surface that an untrusted view definition could introduce. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Function Restriction in Databricks‑to‑Databricks View Sharing

The most visible security control in Delta Sharing on Databricks is the **whitelist of functions** permitted inside shared views. The allowed list includes common operators (`+`, `-`, `*`, `/`, `=`, `>`, etc.), mathematical functions (`abs`, `ceil`, `floor`, `round`, `sqrt`), string functions (`concat`, `substr`, `replace`, `regexp_extract`), date/time functions (`date_add`, `date_diff`, `date_format`), aggregation functions (`count`, `sum`, `avg`, `min`, `max`), array and map functions, JSON‑related functions, H3 geospatial functions, cryptographic functions (`md5`, `sha2`, `aes_encrypt`), and many others. A full listing is maintained in the Databricks documentation. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

Functions that are *not* in the whitelist—including certain system functions, user‑defined functions, and potentially dangerous operations—are blocked from execution inside a shared view. This prevents a view from being used as a vector to read arbitrary metadata, execute arbitrary code, or access resources beyond the intended scope. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Recipient‑Side Security

Once a share is created, recipients access the data through their own Delta Sharing client. The recipient’s environment is responsible for enforcing its own security policies (e.g., authentication, network controls) when connecting to the provider’s sharing endpoint. Databricks‑to‑Databricks sharing adds mutual TLS authentication and uses the recipient’s Unity Catalog identity to enforce row‑level and column‑level filters that the provider may have defined on the shared objects.

> **Note**: The source material focuses on the function‑restriction aspect of the security model for Databricks‑to‑Databricks view sharing. Other security facets (authentication, encryption, audit logging) are documented in the broader Delta Sharing documentation but are not detailed in the provided sources.

## Related Concepts

- [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Delta Sharing Recipient](/concepts/delta-sharing-recipient-object.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)

## Sources

- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
