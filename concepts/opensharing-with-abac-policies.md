---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1796d0c01b18e75c119652833e378a5ab70e5dcbfcdf504161b60f8f83e766dc
  pageDirectory: concepts
  sources:
    - opensharing-and-abac-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-with-abac-policies
    - OWAP
  citations:
    - file: opensharing-and-abac-databricks-on-aws.md
title: OpenSharing with ABAC Policies
description: The capability to share Databricks tables and views protected by Attribute-Based Access Control (ABAC) row filters and column masks through OpenSharing, requiring Databricks Runtime 16.4+ or serverless compute.
tags:
  - data-governance
  - unity-catalog
  - delta-sharing
timestamp: "2026-06-19T19:50:38.035Z"
---

# OpenSharing with ABAC Policies

**OpenSharing with ABAC Policies** describes how to share tables and views protected by [ABAC Policies|attribute-based access control (ABAC)](/concepts/attribute-based-access-control-abac.md) (row filters and column masks) through [OpenSharing](/concepts/opensharing.md) on Databricks. When the share owner is exempted from the provider-side ABAC policies, the recipient can receive unfiltered data and apply their own ABAC policies on the recipient side. ^[opensharing-and-abac-databricks-on-aws.md]

## Prerequisites

To use OpenSharing with ABAC-protected assets, the following are required:

- Databricks Runtime 16.4 or above, or serverless compute.
- Account admin or workspace admin permissions (to create governed tags used by ABAC policies).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` on the user-defined functions (UDFs) used in the ABAC policies.
- OpenSharing configured between the provider and recipient (see [Delta Sharing](/concepts/delta-sharing.md) documentation). ^[opensharing-and-abac-databricks-on-aws.md]

## Sharing tables protected by ABAC policies

Share owners can share tables secured by ABAC policies through OpenSharing if they meet **both** of these conditions:

1. They have the required OpenSharing permissions.
2. They are exempt from the ABAC policies on the underlying tables (i.e., listed in the `EXCEPT` clause of the policy definition).

The provider's ABAC policy does not govern the recipient's access. Because the share owner is exempt from the provider-side policy, the recipient sees unfiltered or unmasked data by default. Recipients can apply their own ABAC policies to the shared tables to enforce access control on their side. ^[opensharing-and-abac-databricks-on-aws.md]

The following example shows a provider-side row filter policy where the share owner group is exempted, and the protected table is added to a share:

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

^[opensharing-and-abac-databricks-on-aws.md]

For detailed instructions, see the Databricks documentation on [adding ABAC‑secured tables to a share](/concepts/opensharing-with-abac-secured-tables.md) and reading ABAC‑secured data as a recipient. ^[opensharing-and-abac-databricks-on-aws.md]

## Sharing views protected by ABAC policies

Share owners can also share views that reference ABAC‑protected base tables. As with direct table sharing, the share owner must be exempt from the ABAC policies on the underlying tables.

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

-- Add the view to the share
ALTER SHARE employees_share ADD VIEW provider_catalog.hr.employees_view AS hr.employees_view;
GRANT SELECT ON SHARE employees_share TO RECIPIENT `recipient_org`;
```

^[opensharing-and-abac-databricks-on-aws.md]

### Important change after April 23, 2026

If you were sharing views protected by ABAC policies before April 23, 2026, you might need to update your ABAC policies. Before this date, the **view owner** needed to be exempt from policies on the underlying tables. Starting April 23, 2026, the **share owner** must be exempt instead. If Databricks has contacted you as a potentially impacted customer, you have until July 22, 2026 to update your `EXCEPT` clauses. ^[opensharing-and-abac-databricks-on-aws.md]

### Recipient-side enforcement with recipient-local views

Because ABAC policies can only be set on tables (not views), if you need recipient-side users to consume data through views and sensitive data must be protected, share only the base tables and set ABAC policies on them. The recipient creates views locally over the shared tables, and the policies on the base tables are respected when data is accessed through those views. You do not need to share provider-side views in this case. ^[opensharing-and-abac-databricks-on-aws.md]

The approach works as follows:

1. **Share only the base tables, not the views.** On the recipient side, the shared tables appear in a read‑only delta share schema.
2. **Apply ABAC policies to the source tables on the provider side and to the shared tables on the recipient side.** The provider's policy controls access on the provider side. The recipient creates a policy to control access for users on the recipient side.
3. **Create views at the recipient on top of the shared base tables in a separate schema.** Because OpenSharing schemas are read‑only, recipient‑local views must be created in a different schema. The ABAC policies set on the OpenSharing tables are respected when users query data through the recipient‑local views.

```sql
-- Recipient: apply an ABAC policy to the shared table
CREATE POLICY hide_eu_customers
ON CATALOG recipient_catalog
ROW FILTER hide_eu
TO `account users`
EXCEPT 'recipient_admins'
FOR TABLES
MATCH COLUMNS has_tag('geo_region') AS region
USING COLUMNS (region);

-- Create a view in a separate schema (delta share schema is read‑only)
CREATE VIEW recipient_catalog.analytics.employees_view AS
  SELECT * FROM recipient_catalog.delta_share_schema.employees;
```

^[opensharing-and-abac-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages ABAC policies.
- [Row Filters](/concepts/row-filter-policies.md) – A type of ABAC policy that restricts rows.
- Column Masks – A type of ABAC policy that masks column values.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across platforms.
- [OpenSharing](/concepts/opensharing.md) – Databricks’ implementation of Delta Sharing for real‑time access.

## Sources

- opensharing-and-abac-databricks-on-aws.md

# Citations

1. [opensharing-and-abac-databricks-on-aws.md](/references/opensharing-and-abac-databricks-on-aws-143be106.md)
