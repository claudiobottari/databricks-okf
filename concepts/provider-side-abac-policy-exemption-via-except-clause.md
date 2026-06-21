---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b74a7d49930f163b5a73c7db0d3f8bf85a079310ab81a67e7087cf9e321cd0e3
  pageDirectory: concepts
  sources:
    - opensharing-and-abac-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-side-abac-policy-exemption-via-except-clause
    - PAPEVEC
  citations:
    - file: opensharing-and-abac-databricks-on-aws.md
title: Provider-Side ABAC Policy Exemption via EXCEPT Clause
description: The mechanism by which share owners are exempted from ABAC row filter and column mask policies on the provider side using the EXCEPT clause in CREATE POLICY statements, enabling them to share protected data.
tags:
  - sql
  - unity-catalog
  - delta-sharing
timestamp: "2026-06-19T19:50:37.633Z"
---

## Provider-Side ABAC Policy Exemption via `EXCEPT` Clause

The **Provider-Side ABAC Policy Exemption via `EXCEPT` Clause** is a mechanism that allows share owners to share tables and views protected by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies through [OpenSharing](/concepts/opensharing.md). By listing a share owner group in the `EXCEPT` clause of a row filter or column mask policy, the provider exempts the share owner from those policies, enabling recipient users to consume unfiltered or unmasked data. The provider's ABAC policies do not apply on the recipient side; recipients can enforce their own policies locally. ^[opensharing-and-abac-databricks-on-aws.md]

### Prerequisites

- Databricks Runtime 16.4 or above, or serverless compute.
- Account admin or workspace admin permissions (to create governed tags).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` on the User-Defined Functions (UDFs) used in policies.
- OpenSharing configured between provider and recipient. ^[opensharing-and-abac-databricks-on-aws.md]

### Sharing Tables Protected by ABAC Policies

To share a table through OpenSharing when it has ABAC policies applied, the share owner must be exempted from those policies via the `EXCEPT` clause. The following example creates a row filter policy that hides EU customers from most users but exempts the `share_owner_group`:

```sql
-- Provider: row filter policy with the share owner exempted
CREATE POLICY hide_eu_customers
  ON CATALOG provider_catalog
  ROW FILTER hide_eu
  TO `account users`
  EXCEPT 'share_owner_group'
  FOR TABLES
  MATCH COLUMNS has_tag('geo_region') AS region
  USING COLUMNS (region);

-- Add the table to the share
CREATE SHARE employees_share;
ALTER SHARE employees_share ADD TABLE provider_catalog.hr.employees;
GRANT SELECT ON SHARE employees_share TO RECIPIENT `recipient_org`;
```

Because the share owner is exempt, the recipient sees all rows without the row filter. Recipients can apply their own ABAC policies on the shared tables to enforce access control on their side. ^[opensharing-and-abac-databricks-on-aws.md]

### Sharing Views Protected by ABAC Policies

Share owners can also share views that reference ABAC-protected base tables, provided the share owner is exempt from policies on the underlying tables. The same `EXCEPT` clause pattern applies:

```sql
CREATE POLICY hide_eu_customers
  ON CATALOG provider_catalog
  ROW FILTER hide_eu
  TO `account users`
  EXCEPT 'share_owner_group'
  FOR TABLES
  MATCH COLUMNS has_tag('geo_region') AS region
  USING COLUMNS (region);

ALTER SHARE employees_share ADD VIEW provider_catalog.hr.employees_view AS hr.employees_view;
GRANT SELECT ON SHARE employees_share TO RECIPIENT `recipient_org`;
```

> **Important date:** If you were sharing views before April 23, 2026, you might need to update your ABAC policies. Before this date, the **view owner** needed to be exempt from policies on the underlying tables. Starting April 23, 2026, the **share owner** must be exempt instead. If Databricks contacted you as a potentially impacted customer, you have until July 22, 2026 to update your `EXCEPT` clauses. ^[opensharing-and-abac-databricks-on-aws.md]

### Recommended Alternative: Share Base Tables and Apply Policies on Recipient Side

If you need recipient-side users to consume data through views and sensitive data must be protected, Databricks recommends sharing only the base tables (not the views) and applying ABAC policies on those shared tables. The recipient then creates views locally in a separate schema (because OpenSharing schemas are read-only). The provider’s ABAC policies are respected when data is accessed through those recipient-local views. ^[opensharing-and-abac-databricks-on-aws.md]

### Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [OpenSharing](/concepts/opensharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- Column Masking
- [Row Filters](/concepts/row-filter-policies.md)
- [Unity Catalog](/concepts/unity-catalog.md)

### Sources

- opensharing-and-abac-databricks-on-aws.md

# Citations

1. [opensharing-and-abac-databricks-on-aws.md](/references/opensharing-and-abac-databricks-on-aws-143be106.md)
