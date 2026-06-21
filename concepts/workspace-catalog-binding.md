---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c240aa06c6bf6771c32a4397acf712ab2d4e95e99cb762b8bc35908e7f81480
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
    - enable-a-workspace-for-unity-catalog-databricks-on-aws.md
    - workspace-catalog-binding-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - workspace-catalog-binding
    - Workspace‑catalog binding
    - Workspace Catalog
    - Workspace catalog
    - default workspace catalog
  citations:
    - file: workspace-catalog-binding-databricks-on-aws.md
    - file: access-control-in-unity-catalog-databricks-on-aws.md
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
title: Workspace-Catalog Binding
description: Workspace-level restrictions that limit which workspaces can access specific catalogs, external locations, and storage credentials.
tags:
  - unity-catalog
  - workspace
  - binding
timestamp: "2026-06-19T21:55:09.982Z"
---

```markdown
---
title: Workspace-Catalog Binding
summary: A mechanism to limit catalog and external location access to specific workspaces, enabling data isolation by workspace boundaries.
sources:
  - workspace-catalog-binding-databricks-on-aws.md
  - access-control-in-unity-catalog-databricks-on-aws.md
  - enable-a-workspace-for-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:36:46.769Z"
updatedAt: "2026-06-19T18:39:23.616Z"
tags:
  - unity-catalog
  - access-control
  - data-isolation
aliases:
  - workspace-catalog-binding
confidence: 0.95
provenanceState: merged
inferredParagraphs: 0
---

# Workspace-Catalog Binding

**Workspace-Catalog Binding** is a Unity Catalog access control mechanism that restricts a catalog to one or more specific workspaces, overriding the default behavior where all catalogs are accessible from any workspace attached to the same [[metastore|Metastore]]. When a catalog is bound to a subset of workspaces, access from unbound workspaces is denied even for users who hold explicit privilege grants on the catalog. ^[workspace-catalog-binding-databricks-on-aws.md]

Workspace-level restrictions are one of four complementary models in Unity Catalog's access control system, alongside privileges/ownership, attribute-based policies (ABAC), and table-level filtering/masking. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Why Use Workspace-Catalog Binding

Organizational and compliance requirements often specify that certain data must remain accessible only in designated environments. Use cases include:

- Isolating production data from development or test environments.
- Preventing certain data domains from being joined together.
- Ensuring that sensitive data can only be processed in specific workspaces.

Because the workspace is the primary data processing environment and the catalog is the primary data domain, workspace-catalog binding lets catalog owners and users with the `MANAGE` privilege define which workspaces can access which catalogs. ^[workspace-catalog-binding-databricks-on-aws.md]

## How Workspace-Catalog Binding Works

When you bind a catalog to specific workspaces, only the workspaces you assign can access the catalog. Any workspace not in the assigned list receives an error when users try to access the catalog, overriding any individual privilege grants those users hold. ^[workspace-catalog-binding-databricks-on-aws.md]

![Catalog-workspace binding diagram](https://docs.databricks.com/aws/en/assets/images/workspace-catalog-binding-example-80fd4c0c839905a034c0c98302f01229.png)

In the example diagram, `prod_catalog` is bound to two production workspaces. Even if a user holds a `SELECT` grant on a table in `prod_catalog`, they cannot access that table from the Dev workspace. ^[workspace-catalog-binding-databricks-on-aws.md]

### Read-Only Access

When binding a catalog to a workspace, you can optionally restrict that workspace to **read-only access**. All write operations from that workspace to the catalog are blocked. You can change this selection at any time by editing the catalog. ^[workspace-catalog-binding-databricks-on-aws.md]

### Default Workspace Catalog Behavior

The exception to the default open behavior is the [[Workspace-Catalog Binding|default workspace catalog]] created automatically for all new workspaces. This workspace catalog is bound only to its own workspace by default. ^[workspace-catalog-binding-databricks-on-aws.md]

If you unbind this catalog or extend access to other workspaces, you must grant any required permissions manually because the workspace admins group is workspace-local and cannot be used across workspaces. ^[workspace-catalog-binding-databricks-on-aws.md]

For workspaces that were enabled for Unity Catalog automatically, workspace admins own the default catalog and have all permissions on that catalog **in the workspace only**. If you unbind that catalog or bind it to other catalogs, you must grant the required permissions manually to members of the workspace admins group as individual users or using account-level groups. ^[workspace-catalog-binding-databricks-on-aws.md, enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

### Platform-Wide Enforcement

Workspace-catalog bindings are enforced consistently across the platform:

- **Information schema** queries return only the catalogs accessible in the current workspace.
- **Data lineage** and **Catalog Explorer** show only catalogs assigned to the current workspace.

^[workspace-catalog-binding-databricks-on-aws.md]

## What Can Be Bound to Workspaces

Workspace binding applies beyond catalogs. You can also bind the following to specific workspaces:

- **External locations**: restrict which workspaces can access specific cloud storage paths. ^[workspace-catalog-binding-databricks-on-aws.md]
- **Storage credentials**: restrict which workspaces can use specific cloud credentials. ^[workspace-catalog-binding-databricks-on-aws.md]
- **Service credentials**: restrict which workspaces can use specific cloud service credentials. ^[workspace-catalog-binding-databricks-on-aws.md]

## Bind a Catalog to One or More Workspaces

**Permissions required**: [[metastore|Metastore]] admin, catalog owner, or `MANAGE` and `USE CATALOG` on the catalog. ^[workspace-catalog-binding-databricks-on-aws.md]

Regardless of whether a catalog is assigned to the current workspace, [[metastore|Metastore]] admins can see all catalogs in a [[metastore|Metastore]], and catalog owners can see all catalogs they own in a [[metastore|Metastore]]. Catalogs that are not assigned to the workspace appear grayed out, and no child objects are visible or queryable. ^[workspace-catalog-binding-databricks-on-aws.md]

### Using Catalog Explorer

1. Log in to a workspace linked to the [[metastore|Metastore]].
2. Click **Catalog**.
3. In the Catalog pane on the left, click the catalog name.
4. On the **Workspaces** tab, clear the **All workspaces have access** checkbox. (If already bound, this checkbox is already cleared.)
5. Click **Assign to workspaces** and enter or find the workspaces you want to assign.
6. (Optional) To limit workspace access to read-only, on the **Manage Access Level** menu, select **Change access to read-only**. You can reverse this later by editing the catalog and selecting **Change access to read & write**.

To revoke access from a workspace, go to the **Workspaces** tab, select the workspace, and click **Revoke**. ^[workspace-catalog-binding-databricks-on-aws.md]

### Using the CLI

The `workspace-bindings` CLI command group can be used to bind, list, and remove workspace assignments for catalogs. ^[workspace-catalog-binding-databricks-on-aws.md]

## Unbind a Catalog from a Workspace

Instructions for revoking workspace access using Catalog Explorer or the CLI are included in the binding section above. ^[workspace-catalog-binding-databricks-on-aws.md]

## Related Concepts

- [[Unity Catalog]] — The data governance solution that provides workspace-catalog binding
- [[Metastore]] — The top-level container for data in Unity Catalog
- [[Unity Catalog Privilege Management|Unity Catalog Privileges]] — `MANAGE`, `USE CATALOG`, and other privileges required for binding
- Default Workspace Catalog — The automatically created catalog bound to a single workspace
- [[External location|External Location Binding]] — Restricting external location access to specific workspaces
- Storage Credential Binding — Restricting storage credential access to specific workspaces
- Access Control Models in Unity Catalog — How workspace-catalog binding fits with privileges, ABAC, and row/column filters

## Sources

- workspace-catalog-binding-databricks-on-aws.md
- access-control-in-unity-catalog-databricks-on-aws.md
- enable-a-workspace-for-unity-catalog-databricks-on-aws.md
```

# Citations

1. [workspace-catalog-binding-databricks-on-aws.md](/references/workspace-catalog-binding-databricks-on-aws-b9573786.md)
2. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
3. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
