---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a0a103c8d8b4796baa8cf781c16a7c7f814004b734109f6214e55f2326fcb3a
  pageDirectory: concepts
  sources:
    - opensharing-and-abac-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-owner-exemption-from-abac-policies
    - SOEFAP
    - Share Owner Exemption
  citations:
    - file: opensharing-and-abac-databricks-on-aws.md
title: Share Owner Exemption from ABAC Policies
description: The share owner must be listed in the EXCEPT clause of ABAC policies on the provider side to share tables and views protected by row filters and column masks through OpenSharing.
tags:
  - data-governance
  - unity-catalog
  - delta-sharing
timestamp: "2026-06-19T19:50:21.784Z"
---

## Share Owner Exemption from ABAC Policies

**Share Owner Exemption from ABAC Policies** refers to the requirement that a share owner on the provider side must be explicitly exempted from ABAC policies (such as row filters and column masks) to share tables or views protected by those policies through [OpenSharing](/concepts/opensharing.md). Without this exemption, the share owner cannot grant access to protected data to recipients, because the provider-side policies would block the data. ^[opensharing-and-abac-databricks-on-aws.md]

### Overview

When sharing tables secured by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies via OpenSharing, the share owner must satisfy two conditions: they must have the required OpenSharing permissions, and they must be listed in the `EXCEPT` clause of the ABAC policy—effectively being exempt from the policy. If the share owner is exempt, the recipient sees unfiltered or unmasked data by default, because the provider‑side ABAC policy does not govern the recipient’s access. ^[opensharing-and-abac-databricks-on-aws.md]

### Prerequisites

- Databricks Runtime 16.4 or above, or serverless compute.
- Account admin or workspace admin permissions (to create [Governed Tags](/concepts/governed-tags.md)).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` on the UDFs used by the policy.
- OpenSharing configured between the provider and recipient. ^[opensharing-and-abac-databricks-on-aws.md]

### Sharing Tables Protected by ABAC Policies

The provider creates a row filter or column mask policy with an `EXCEPT` clause that names the share owner (for example, a group like `'share_owner_group'`). The share owner can then add the table to a share and grant `SELECT` to recipients. Because the owner is exempt from the policy, the recipient receives the full data.

**Example:**

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

Recipients can apply their own ABAC policies to the shared tables to enforce access control on their side. ^[opensharing-and-abac-databricks-on-aws.md]

### Sharing Views Protected by ABAC Policies

Share owners can also share views that reference ABAC-protected base tables. The same exemption requirement applies: the share owner must be listed in the `EXCEPT` clause of the policies on the underlying tables.

**Important compatibility note:** If you were sharing views before April 23, 2026, the **view owner** needed to be exempt. After that date, the **share owner** must be exempt instead. If Databricks has contacted you as a potentially impacted customer, you have until July 22, 2026 to update your `EXCEPT` clauses. ^[opensharing-and-abac-databricks-on-aws.md]

### Recipient-Side Enforcement

Because ABAC policies can only be set on tables (not views), a recommended pattern for recipient‑side control is:

1. Share only the base tables (not the views).
2. Apply ABAC policies to the source tables on the provider side and to the shared tables on the recipient side.
3. Create views in a separate schema on the recipient side over the shared tables. The policies on the shared tables are respected when users query those views.

This allows the recipient to enforce their own ABAC policies on the data while using familiar views. ^[opensharing-and-abac-databricks-on-aws.md]

### Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The protocol for sharing data across Databricks workspaces.
- ABAC policies – Attribute‑based access control using row filters and column masks.
- [Row Filters](/concepts/row-filter-policies.md) and Column Masks – Types of ABAC policies that can be exempted.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where ABAC policies are defined.
- Share Owner – The principal that manages a share in OpenSharing.

### Sources

- opensharing-and-abac-databricks-on-aws.md

# Citations

1. [opensharing-and-abac-databricks-on-aws.md](/references/opensharing-and-abac-databricks-on-aws-143be106.md)
