---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 61d1a092ba5eca06125261d5edac7482aa6cc9dc7ebf5a145c0248f45cd47e8b
  pageDirectory: concepts
  sources:
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-quotas-and-service-limits
    - Service Limits and ABAC Policy Quotas
    - APQASL
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Policy Quotas and Service Limits
description: Quotas governing the number and scope of ABAC row filter and column mask policies in Unity Catalog
tags:
  - access-control
  - unity-catalog
  - limits
  - databricks
timestamp: "2026-06-19T20:13:42.164Z"
---

# ABAC Policy Quotas and Service Limits

**ABAC Policy Quotas and Service Limits** refers to the resource constraints, compute requirements, and operational limitations that govern the use of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) row filter and column mask policies in [Unity Catalog](/concepts/unity-catalog.md) on Databricks. Understanding these boundaries is essential for planning policy deployments and avoiding runtime failures.

## Compute Requirements

To apply ABAC policies, queries must run on one of the following compute configurations:

- **Serverless compute**
- **Standard compute** on Databricks Runtime 16.4 or above
- **Dedicated compute** on Databricks Runtime 16.4 or above with [fine-grained access control (FGAC) filtering](/concepts/dynamic-views-for-fine-grained-access-control.md) enabled

ABAC policies use **governed tags**, not ungoverned tags. Governed tags are defined at the account level and carry their own access controls and quotas. After assigning or modifying a governed tag, it can take a few minutes for the change to take effect. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Policy Quotas

Databricks enforces specific quotas on the number of ABAC policies, governed tags, and related resources. These are documented in the Service Limits (Databricks) page. For full details, see the official service limits documentation. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## ABAC Limitations

### Access from Older Runtimes
Standard and dedicated compute on Databricks Runtime versions earlier than 16.4 cannot access ABAC-secured tables. To continue running workloads on an older runtime, scope the ABAC policy to a specific group using the `TO` clause and exclude the principal that runs the older-runtime workload using the `EXCEPT` clause. Users outside the group retain full table access. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### ABAC Policies on Views
ABAC policies cannot be applied directly to views. However, when a query accesses a view that references tables with ABAC policies, those policies are evaluated using the **session user's identity** — the person running the query. Base table access checks and dependency checks use the view owner’s identity. The same session-user model applies when tables with ABAC policies are accessed through functions. This behavior was introduced alongside the ABAC GA release (April 2026). ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### ABAC Policies on Materialized Views and Streaming Tables
ABAC policies on materialized views and streaming tables are supported only when the pipeline owner and the run-as identity are exempt from the policy (listed in the `EXCEPT` clause). If the pipeline owner or run-as identity is subject to an ABAC policy, the pipeline refresh fails. To prevent failure, add those identities to the `EXCEPT` clause and use the `TO` clause to specify which users and groups receive masked or filtered data. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### OpenSharing Tables with ABAC Policies
Tables with ABAC policies, or views that reference such tables, can be shared through OpenSharing only if the share owner is exempt from the policy (listed in the `EXCEPT` clause). The policy does not govern the recipient’s access; recipients may apply their own ABAC policies on the shared tables. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Time Travel and Cloning
ABAC policies cannot be evaluated against historical table snapshots. Consequently, time travel queries fail on tables with active row filters or column masks. Deep and shallow clones are also unsupported. To enable these operations, create a service principal or group and add it to the policy’s `EXCEPT` clause. Exempted principals will see unfiltered, unmasked data, so only trusted identities should be exempted. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### AI Search Indexes
ABAC policies on a source table do **not** apply to AI Search indexes created from that table. The index syncs all rows and does not enforce row filter or column mask policies when serving queries. For tables with column masks, you can exclude masked columns from the index using the columns-to-sync setting. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Multiple Policies on the Same Table or Column
Only one distinct row filter can resolve at runtime for a given table and user, and only one distinct column mask for a given column and user. If multiple distinct row filters or column masks apply to the same user and table or column, Databricks blocks access and returns an error. Multiple policies are allowed if they resolve to the same row filter or column mask user-defined function (UDF) with identical arguments. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### ABAC Policies and Information Schema
There is no information schema table for ABAC policies. The `information_schema.row_filters` and `information_schema.column_masks` tables show only [Table-Level Row Filters and Column Masks](/concepts/table-level-row-filters-and-column-masks.md), not ABAC-derived policies. To list ABAC policies, use the Unity Catalog REST API. Policy lifecycle events are captured in the audit log system table. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### ABAC on Dedicated Compute
Additional limitations apply when using ABAC on dedicated compute. See the dedicated compute FGAC limitations page. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Limitations Common to ABAC and Table-Level Filters/Masks
Many general limitations of [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) apply equally to ABAC policies. Consult the row filters and column masks limitations page for the full list. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md)
- Service Limits (Databricks)
- [ABAC Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)
