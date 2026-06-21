---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 435aff6a51ac5e379c92769d572770efd020dca7fb4d91dd04f425a5df18624d
  pageDirectory: concepts
  sources:
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-on-materialized-views-and-streaming-tables
    - Streaming Tables and ABAC on Materialized Views
    - AOMVAST
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC on Materialized Views and Streaming Tables
description: Limitations and requirements for applying ABAC policies to materialized views and streaming tables, including pipeline owner exemption
tags:
  - access-control
  - unity-catalog
  - streaming
  - materialized-views
  - databricks
timestamp: "2026-06-19T20:13:49.059Z"
---

# ABAC on Materialized Views and Streaming Tables

**ABAC on Materialized Views and Streaming Tables** refers to the application of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies — specifically [Row Filters](/concepts/row-filter-policies.md) and Column Masks — to materialized views and streaming tables within [Unity Catalog](/concepts/unity-catalog.md) on Databricks. These policies are supported only under specific conditions regarding the pipeline owner and run-as identity. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Support Conditions

ABAC policies on materialized views and streaming tables are supported only when **both** the pipeline owner and the run-as identity are exempt from the policy. When a pipeline refreshes a materialized view or streaming table, the ABAC policies are evaluated using the pipeline owner's identity or the run-as identity. If that identity is subject to an ABAC policy, the pipeline refresh fails. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Preventing Refresh Failures

To prevent pipeline refresh failures when using ABAC policies on materialized views or streaming tables:

1. Add the pipeline owner or run-as identity to the `EXCEPT` clause of every ABAC policy applied to the source tables.
2. Use the `TO` clause to specify which users and groups receive masked or filtered data.

This configuration ensures that the pipeline owner (who performs the refresh) is not subject to the policy, while end users continue to see only the data they are authorized to access. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Policy Evaluation Model

When ABAC policies are applied to the underlying source tables of a materialized view or streaming table, those policies are evaluated using the pipeline owner's or run-as identity during refresh operations. This differs from the standard session user identity model used for views, where policies are evaluated against the querying user's identity. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Key Requirements

- Serverless Compute or Standard Compute on Databricks Runtime 16.4 or higher is required.
- For [Dedicated Compute](/concepts/dedicated-access-mode-for-ml-compute.md), Fine-Grained Access Control (FGAC) filtering must be enabled.
- ABAC policies use [Governed Tags](/concepts/governed-tags.md), not ungoverned tags. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Row Filters](/concepts/row-filter-policies.md)
- Column Masks
- [Unity Catalog](/concepts/unity-catalog.md)
- [Materialized Views](/concepts/materialized-views-in-databricks.md)
- Streaming Tables
- Pipeline Run-As Identity
- Delta Live Tables
- [Governed Tags](/concepts/governed-tags.md)
- Policy Evaluation Model

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)
