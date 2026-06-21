---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2223271543352721365596507366c3f1e4094ac8a5870c865d991c1ee84e35ed
  pageDirectory: concepts
  sources:
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session-user-identity-model-for-abac-on-views
    - SUIMFAOV
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Session User Identity Model for ABAC on Views
description: ABAC policies on underlying tables are evaluated using the session user's identity when querying through views and functions
tags:
  - access-control
  - unity-catalog
  - views
  - databricks
timestamp: "2026-06-19T20:13:29.781Z"
---

# Session User Identity Model for ABAC on Views

The **Session User Identity Model for ABAC on Views** describes how [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) row filters and column masks are evaluated when a user queries a view in [Unity Catalog](/concepts/unity-catalog.md). When a view references underlying tables that have ABAC policies applied, the policies are evaluated using the **session user's identity** — meaning the person who runs the query — rather than the view owner's identity. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## How Policies Are Evaluated

When a user queries a view that references tables with ABAC policies, those policies are respected when accessing data through the view. ABAC row filters and column masks on the underlying tables are evaluated using the session user's identity. The user sees only the rows and column values they are authorized to access, as defined by the ABAC policies on the base tables. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

Base table access checks and dependency access checks use the **view owner's identity**, so users can query views without direct privileges on the underlying tables. This separation allows views to serve as controlled access layers while ABAC policies still enforce fine-grained restrictions based on the end user's identity. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

The same session user identity model applies when tables with ABAC policies are accessed through [functions](/concepts/ai-functions.md). This ensures consistent behavior across different access patterns. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Important Notes

- You **cannot** apply ABAC policies directly to views themselves. ABAC policies are only applied to base tables and evaluated through views. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- The session user identity model was introduced alongside the ABAC General Availability (GA) release. Previously, policies were evaluated using the view owner's or function definer's identity. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- ABAC policies on views and functions
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- Unity Catalog Views
- Policy Evaluation Rules
- Requirements for ABAC Policies

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)
