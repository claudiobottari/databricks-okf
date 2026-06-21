---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 041cd9847c1791b1642adaa9eb73b76eec4b6eca41ec3c188a5567b10d6ad746
  pageDirectory: concepts
  sources:
    - opensharing-and-abac-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-view-sharing-ownership-change-april-2026
    - AVSOC(2
  citations:
    - file: opensharing-and-abac-databricks-on-aws.md
title: ABAC View Sharing Ownership Change (April 2026)
description: A policy change effective April 23, 2026, shifting the exemption requirement from the view owner to the share owner for sharing views protected by ABAC policies, with a grace period until July 22, 2026.
tags:
  - migration
  - unity-catalog
  - delta-sharing
  - breaking-change
timestamp: "2026-06-19T19:50:38.626Z"
---

# ABAC View Sharing Ownership Change (April 2026)

The **ABAC View Sharing Ownership Change (April 2026)** refers to a shift in how [Delta Sharing](/concepts/delta-sharing.md) handles [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies for views shared through [OpenSharing](/concepts/opensharing.md). Starting April 23, 2026, the **share owner** must be exempted from ABAC policies on the underlying tables — a change from the previous rule, which required the **view owner** to be exempted. This change affects providers who share views protected by ABAC policies and may require updates to existing `EXCEPT` clauses. ^[opensharing-and-abac-databricks-on-aws.md]

## Historical Behavior (Before April 23, 2026)

Before April 23, 2026, when a provider shared a view that referenced ABAC‑protected base tables, the **view owner** needed to be listed in the `EXCEPT` clause of the ABAC policy on those base tables. Only if the view owner was exempted would the recipient receive unfiltered data. ^[opensharing-and-abac-databricks-on-aws.md]

## Current Behavior (Start April 23, 2026)

As of April 23, 2026, the requirement has changed: the **share owner** (rather than the view owner) must be exempted from the ABAC policies on the underlying tables. The share owner is the entity that owns the share in the provider’s Unity Catalog. If the share owner is listed in the `EXCEPT` clause, the recipient sees the data as if the policies are not applied on the provider side. Recipients may then apply their own ABAC policies to the shared tables on their side. ^[opensharing-and-abac-databricks-on-aws.md]

## Migration Deadline

Databricks has identified potentially impacted customers and contacted them. Affected providers have until **July 22, 2026** to update the `EXCEPT` clauses of their ABAC policies so that the share owner — instead of the view owner — is exempted. ^[opensharing-and-abac-databricks-on-aws.md]

## Recommended Approach for Recipient‑Side Enforcement

Because ABAC policies can only be set on tables, not views, if the provider needs to ensure that recipient‑side users access data through views with enforced policies, the recommended approach is:

1. Share only the base tables (not the provider‑side views).
2. Apply ABAC policies to the shared tables on the recipient side.
3. Create local views in a separate schema on the recipient side over the shared tables. Because OpenSharing schemas are read‑only, recipient‑local views must be created in a different schema. ABAC policies on the shared tables are respected when data is accessed through those recipient‑created views. ^[opensharing-and-abac-databricks-on-aws.md]

## Requirements

- Databricks Runtime 16.4 or above, or serverless compute.
- Account admin or workspace admin permissions (to create governed tags).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` on the UDFs used in ABAC policies.
- OpenSharing configured between provider and recipient. ^[opensharing-and-abac-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The access control framework that uses row filters and column masks.
- [OpenSharing](/concepts/opensharing.md) – The Delta Sharing protocol that enables cross‑platform data sharing.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying open protocol for sharing data.
- [Unity Catalog](/concepts/unity-catalog.md) – The central catalog that governs tables and shares.
- [View Sharing](/concepts/delta-sharing.md) – Sharing views instead of base tables via Delta Sharing.

## Sources

- opensharing-and-abac-databricks-on-aws.md

# Citations

1. [opensharing-and-abac-databricks-on-aws.md](/references/opensharing-and-abac-databricks-on-aws-143be106.md)
