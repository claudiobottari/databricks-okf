---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 575b0e89a050a91bc22a79ecf60077299559774928f26d3a8c2be441ff076b22
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - governed-tags-for-abac-policies
    - GTFAP
    - Core concepts for ABAC
    - Governed Tag Policy
    - governed tag policies
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Governed Tags for ABAC Policies
description: Tags applied to securable objects (catalogs, schemas, tables, columns) that policies use to match targets for row filtering or column masking.
tags:
  - data-governance
  - unity-catalog
  - abac
  - tagging
timestamp: "2026-06-19T14:35:03.900Z"
---

# Governed Tags for ABAC Policies

**Governed Tags** are account-level metadata labels in [Unity Catalog](/concepts/unity-catalog.md) that drive [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy evaluation. Unlike ungoverned tags, governed tags have access controls that determine who can create, assign, and manage them, making them a security boundary for ABAC policies. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Overview

Governed tags are the mechanism by which ABAC policies determine which securable objects a policy applies to. When creating a row filter or column mask policy, you specify conditions that match columns or tables using tag keys or tag key‑value pairs. At query time, Unity Catalog evaluates these conditions against the governed tags on each object and applies the policy only to objects whose tags match. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Access Control

Governed tags are defined at the account level, and their creation, assignment, and management are restricted to authorized users. This ensures that only trusted administrators and data stewards can modify tag assignments, preventing unauthorized users from altering which policies apply to a given object. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Propagation Delay

After assigning or modifying a governed tag, it can take a few minutes for the change to take effect in ABAC policy evaluation. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Usage in ABAC Policies

Governed tags are referenced in ABAC policies through two built‑in functions:

- `has_tag(tag_key)` — returns `TRUE` if the target object has the specified tag key, regardless of its value.
- `has_tag_value(tag_key, tag_value)` — returns `TRUE` if the object has the specified tag key with the specified value.

These functions can be combined with `AND`, `OR`, and `NOT` to build custom matching expressions. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### In Row Filter Policies

For row filter policies, the function inputs can be columns matched by tags. The policy’s filter UDF receives the column values from rows whose tag conditions are satisfied. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### In Column Mask Policies

Column mask policies can identify target columns in two ways:

- **Columns matching any of these tags** – specify a list of tag keys or key‑value pairs; any column with one of those tags is masked.
- **Columns matching a custom expression** – build a boolean expression using `has_tag()` and `has_tag_value()` combined with `AND`, `OR`, and `NOT`. Columns where the expression evaluates to `TRUE` are masked.

Both methods rely on governed tags assigned to catalog columns. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging

Databricks logs governed tag operations in the audit log system table. The following query retrieves all tag assignment and deletion events: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SELECT
  event_time,
  action_name,
  user_identity.email AS actor,
  request_params.workspace_id,
  request_params.metastore_id,
  request_params.tag_assignment,
  response.status_code,
  source_ip_address
FROM system.access.audit
WHERE service_name = 'unityCatalog'
  AND action_name IN (
    'createEntityTagAssignment',
    'deleteEntityTagAssignment'
  )
ORDER BY event_time DESC;
```

## Requirements for Policy Creation

To create an ABAC policy that uses governed tags, you must have:

- `MANAGE` on the securable object (catalog, schema, or table) where the policy is attached, or own the object.
- `EXECUTE` on the user‑defined function (UDF) that implements the filtering or masking logic.
- Governed tags applied to the target objects. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The access control model that uses governed tags for dynamic policy evaluation.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where governed tags are defined and managed.
- [Row Filter Policies](/concepts/row-filter-policies.md) – ABAC policies that restrict data rows based on tag conditions.
- [Column Mask Policies](/concepts/column-mask-policies.md) – ABAC policies that mask sensitive columns identified by tags.
- User-Defined Functions (UDFs) – Functions that implement the filtering or masking logic used by policies.
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) – System table for auditing governed tag and ABAC policy operations.

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)
2. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
