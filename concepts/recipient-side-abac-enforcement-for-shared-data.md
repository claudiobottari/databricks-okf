---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c779dae243e3c3d629063a17cf824d9dd5e69e68170c10d616442a2dc4951a23
  pageDirectory: concepts
  sources:
    - opensharing-and-abac-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-side-abac-enforcement-for-shared-data
    - RAEFSD
  citations:
    - file: opensharing-and-abac-databricks-on-aws.md
title: Recipient-Side ABAC Enforcement for Shared Data
description: Recipients of OpenSharing can apply their own ABAC policies (row filters, column masks) to shared tables to enforce access control on their side, independent of provider-side policies.
tags:
  - data-governance
  - unity-catalog
  - delta-sharing
timestamp: "2026-06-19T19:50:30.417Z"
---

Here is the wiki page for "Recipient-Side ABAC Enforcement for Shared Data", written solely from the provided source material.

---

## Recipient-Side ABAC Enforcement for Shared Data

**Recipient-Side ABAC Enforcement for Shared Data** refers to the ability of a data recipient to apply [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies—such as [Row Filters](/concepts/row-filter-policies.md) and Column Masks—on tables shared through [OpenSharing](/concepts/opensharing.md). This allows the recipient organization to enforce its own access controls independently of the provider’s policies, ensuring that sensitive data is protected even after it has been shared.

### Overview

When a provider shares a table or view that is protected by ABAC policies, the provider's policies do not automatically govern access on the recipient side. By default, if the share owner is exempt from the provider-side policies (via an `EXCEPT` clause), the recipient sees the unfiltered, unmasked data. The recipient can then create and apply their own ABAC policies to the shared tables to enforce access control for their users. ^[opensharing-and-abac-databricks-on-aws.md]

This pattern is supported for both tables and views, but there are important differences in how views are handled because ABAC policies can only be set on tables, not on views.

### Prerequisites

- Databricks Runtime 16.4 or above, or serverless compute.
- Account admin or workspace admin permissions (to create governed tags).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` on the user-defined functions (UDFs) used in policies.
- OpenSharing configured between the provider and recipient. ^[opensharing-and-abac-databricks-on-aws.md]

### Sharing Tables Protected by ABAC Policies

A share owner can share tables secured by ABAC policies through OpenSharing if they meet two conditions:

1. They have the required OpenSharing permissions.
2. They are exempt from the ABAC policies (listed in the `EXCEPT` clause of the row filter or column mask policy).

The recipient then sees the unfiltered data by default because the provider-side policy does not govern the recipient's access. To enforce access control, the recipient applies their own ABAC policies on the shared tables. ^[opensharing-and-abac-databricks-on-aws.md]

**Provider-side example (exempting the share owner):**

```sql
CREATE POLICY hide_eu_customers
ON CATALOG provider_catalog
ROW FILTER hide_eu
TO `account users`
EXCEPT 'share_owner_group'
FOR TABLES
MATCH COLUMNS has_tag('geo_region') AS region
USING COLUMNS (region);
```

**Recipient-side application of ABAC:**

The recipient creates a similar policy on the shared table in their own catalog. ^[opensharing-and-abac-databricks-on-aws.md]

### Sharing Views Protected by ABAC Policies

Views that reference ABAC-protected base tables can also be shared. However, ABAC policies cannot be applied directly to views—only to underlying tables. Therefore, if the recipient needs users to consume data through views and sensitive data must be protected, the recommended approach is:

1. **Share only the base tables**, not the provider-side views.
2. **Apply ABAC policies to the shared tables on the recipient side** to control access for recipient users.
3. **Create local views at the recipient** on top of the shared base tables in a separate schema. Because OpenSharing schemas are read-only, recipient-local views must be created in a different schema. The ABAC policies on the shared tables are respected when data is accessed through these recipient-local views. ^[opensharing-and-abac-databricks-on-aws.md]

**Recipient-side example:**

```sql
-- Apply ABAC policy to the shared table
CREATE POLICY hide_eu_customers
ON CATALOG recipient_catalog
ROW FILTER hide_eu
TO `account users`
EXCEPT 'recipient_admins'
FOR TABLES
MATCH COLUMNS has_tag('geo_region') AS region
USING COLUMNS (region);

-- Create a view in a separate schema (delta share schema is read-only)
CREATE VIEW recipient_catalog.analytics.employees_view AS
  SELECT * FROM recipient_catalog.delta_share_schema.employees;
```

#### Update for Shared Views (April 2026)

If views were shared before April 23, 2026, the **view owner** needed to be exempt from policies on the underlying tables. Starting April 23, 2026, the **share owner** must be exempt instead. Customers contacted by Databricks as potentially impacted have until July 22, 2026 to update their `EXCEPT` clauses. ^[opensharing-and-abac-databricks-on-aws.md]

### Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [OpenSharing](/concepts/opensharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Row Filters](/concepts/row-filter-policies.md)
- Column Masks
- [Delta Sharing](/concepts/delta-sharing.md)
- [Share Owner Exemption](/concepts/share-owner-exemption-from-abac-policies.md)

### Sources

- opensharing-and-abac-databricks-on-aws.md

# Citations

1. [opensharing-and-abac-databricks-on-aws.md](/references/opensharing-and-abac-databricks-on-aws-143be106.md)
