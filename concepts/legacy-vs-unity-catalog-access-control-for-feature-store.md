---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 586966015e19f0dbc4149998d29f8898d1842b58e0456c8bdee0efcc7cc24fe8
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-vs-unity-catalog-access-control-for-feature-store
    - LVUCACFFS
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Legacy vs Unity Catalog Access Control for Feature Store
description: "Databricks Feature Store offers two access control paradigms: a legacy permission system with three levels (used in workspaces without Unity Catalog) and Unity Catalog privileges (used in workspaces enabled for Unity Catalog)."
tags:
  - databricks
  - unity-catalog
  - feature-store
  - migration
timestamp: "2026-06-18T10:36:57.611Z"
---

# Legacy vs Unity Catalog Access Control for Feature Store

Databricks Feature Store supports two distinct access control models depending on whether the workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md). Workspaces **not** enabled for Unity Catalog use a legacy permission system with three levels (CAN VIEW METADATA, CAN EDIT METADATA, CAN MANAGE) applied directly to feature table metadata. Workspaces enabled for Unity Catalog use [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) and [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) for feature tables, following the same governance model as other Unity Catalog securable objects. ^[access-control-legacy-databricks-on-aws.md]

## Legacy Access Control (Non-Unity Catalog Workspaces)

In workspaces not enabled for Unity Catalog, access control is managed through a flat permission model applied to feature table metadata. Any user can create a new feature table. By default, the creator and workspace admins receive CAN MANAGE permission, while all other users have NO PERMISSIONS. ^[access-control-legacy-databricks-on-aws.md]

### Permission Levels

| Permission Level | Abilities |
|---|---|
| **CAN VIEW METADATA** | View the feature table in the UI, see its metadata |
| **CAN EDIT METADATA** | Edit the feature table's description and metadata |
| **CAN MANAGE** | Manage other users' permissions on the table, delete the table, and perform all lower-level actions |

^[access-control-legacy-databricks-on-aws.md]

### Configuring Permissions

**Per-table permissions:** On the feature table page, click the arrow next to the table name and select **Permissions**. This option is only available to users with CAN MANAGE permission for that feature table. ^[access-control-legacy-databricks-on-aws.md]

**Workspace-wide permissions:** Workspace administrators (and users with CAN MANAGE permission for the Feature Store) can set permission levels on all feature tables — including future tables — from the Feature Store UI by clicking **Permissions** on the feature store page. Permissions set at this level are inherited by individual feature tables and marked as "Some permissions cannot be removed because they are inherited." Individual table pages can add permissions beyond the inherited baseline but cannot set more restrictive permissions. ^[access-control-legacy-databricks-on-aws.md]

## Unity Catalog Access Control

In workspaces enabled for Unity Catalog, feature tables are governed by [Unity Catalog](/concepts/unity-catalog.md)'s standard privilege model. Access is controlled through:

- **[Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md)**: Standard grants such as `SELECT`, `MODIFY`, `CREATE`, and `MANAGE` on feature tables, schemas, and catalogs.
- **[Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)**: Tag-driven policies that can dynamically filter or mask data in feature tables based on governed tags.
- **[ABAC GRANT Policy](/concepts/abac-grant-policy.md)**: Dynamically grants privileges (e.g., `EXECUTE` on models) based on tag conditions — currently in Beta and limited to models, but the same ABAC framework applies to feature tables through row filter and column mask policies.

For detailed guidance on Unity Catalog access control for feature tables, refer to the [Unity Catalog](/concepts/unity-catalog.md) documentation on managing privileges.

## Key Differences

| Aspect | Legacy | Unity Catalog |
|---|---|---|
| **Permission model** | Three flat levels (VIEW, EDIT, MANAGE) | Full privilege hierarchy (SELECT, MODIFY, MANAGE, etc.) |
| **Scope** | Feature table metadata only | Full data governance including data access |
| **Inheritance** | Workspace-level defaults, overridable per table | Catalog → Schema → Table hierarchy |
| **Tag-based policies** | Not supported | Supported via ABAC (row filters, column masks) |
| **Auditing** | Limited | Full audit logging via Unity Catalog |
| **Cross-workspace** | Not supported | Supported via Unity Catalog [Metastore](/concepts/metastore.md) |

## Migration Considerations

When migrating from legacy to Unity Catalog access control:

- Legacy permissions are not automatically migrated — you must reconfigure access using Unity Catalog privileges.
- Unity Catalog provides more granular control and better auditability.
- ABAC policies can replace many manual per-table grants, reducing maintenance overhead.
- The legacy CAN MANAGE permission roughly corresponds to `MANAGE` privilege in Unity Catalog, but the mapping is not exact.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance layer for Databricks
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of privileges available in Unity Catalog
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-driven dynamic access control
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Dynamic privilege grants based on tag conditions
- [Governed Tags](/concepts/governed-tags.md) — Attributes used in ABAC policy conditions

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
