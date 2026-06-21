---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c3285c9e94578890dd38f353d7093f135be841426e564d6e6f8f637cb6cf465c
  pageDirectory: concepts
  sources:
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-with-abac-secured-tables
    - OWAT
    - adding ABAC‑secured tables to a share
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: OpenSharing with ABAC-Secured Tables
description: How Delta Sharing (OpenSharing) works with tables governed by ABAC row filter and column mask policies
tags:
  - access-control
  - unity-catalog
  - delta-sharing
  - databricks
timestamp: "2026-06-19T20:13:48.834Z"
---

# OpenSharing with ABAC-Secured Tables

**OpenSharing with ABAC-Secured Tables** refers to the ability to share tables that have [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies applied, or views that reference such tables, through [Delta Sharing](/concepts/delta-sharing.md) (OpenSharing). This capability allows organizations to share data while maintaining access control, though with specific constraints on how policies are enforced.

## Overview

Tables with ABAC row filter or column mask policies, as well as views that reference tables with ABAC policies, can be shared through OpenSharing only if the share owner is exempt from the policy. The share owner must be listed in the `EXCEPT` clause of every ABAC policy applied to the shared tables. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Policy Enforcement Model

When sharing ABAC-secured tables through OpenSharing, the ABAC policy does **not** govern the recipient's access. Instead, the policy is evaluated only for the share owner, and the exemption ensures the data can be shared without the policy blocking the sharing operation. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

Recipients of shared data can apply their own ABAC policies to the shared tables to enforce access control on their side. This allows each organization in the data sharing relationship to manage access independently. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Provider Configuration

For share providers, the process of adding tables and schemas secured by ABAC policies to a share requires that the share owner is exempt from the policy. Detailed guidance is available in the documentation on adding ABAC-secured tables to a share. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Recipient Configuration

Share recipients can read ABAC-secured data and apply their own ABAC policies to the received tables. This enables recipients to implement their own access control rules on the shared data. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Key Considerations

- The share owner must be listed in the `EXCEPT` clause of every ABAC policy on the shared tables or views. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- ABAC policies are not enforced on the recipient side by the provider's policies. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- Recipients can independently apply their own ABAC policies to shared tables. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- Views that reference ABAC-secured tables can also be shared, following the same exemption requirement. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [OpenSharing](/concepts/opensharing.md)

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)
