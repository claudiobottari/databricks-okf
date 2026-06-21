---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0914b63e69b768cd895e864cd3e34c5696a9f771093cf1e731c01b7976bf7506
  pageDirectory: concepts
  sources:
    - enable-a-workspace-for-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-admin-privileges-in-unity-catalog
    - WAPIUC
    - Admin Privileges in Unity Catalog
    - Admin privileges in Unity Catalog
    - Workspace admin privileges|Workspace admins
  citations:
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
      start: 39
      end: 40
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
      start: 40
      end: 40
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
      start: 41
      end: 41
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
      start: 37
      end: 37
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
      start: 36
      end: 36
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
      start: 43
      end: 45
title: Workspace Admin Privileges in Unity Catalog
description: How workspace admin roles differ depending on whether Unity Catalog was auto-enabled or manually assigned, including the ability to create objects and grant access.
tags:
  - unity-catalog
  - access-control
  - admin-roles
  - databricks
timestamp: "2026-06-19T18:39:05.514Z"
---

```markdown
---
title: Workspace Admin Privileges in Unity Catalog
summary: Workspace admins have varying Unity Catalog privileges depending on whether the workspace was automatically or manually enabled, and account admins can further restrict those privileges using the `RestrictWorkspaceAdmins` setting.
sources:
  - enable-a-workspace-for-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:00:00.000Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - unity-catalog
  - administration
  - access-control
  - workspace-admin
aliases:
  - workspace-admin-privileges-in-unity-catalog
  - WAPIUC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Workspace Admin Privileges in Unity Catalog

**Workspace Admin Privileges in Unity Catalog** refers to the set of permissions and capabilities that a workspace administrator holds within a Databricks workspace that is enabled for Unity Catalog. The precise scope of these privileges depends on whether the workspace was automatically enabled for Unity Catalog or manually assigned to a [[metastore|Metastore]]. Account admins can further restrict these privileges using the `RestrictWorkspaceAdmins` setting. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Workspace Admin Role Basics

Workspace admins are a privileged role that should be distributed carefully. They can manage operations for their workspace, including adding users and service principals, creating clusters, and delegating other users to be workspace admins. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Automatic Enablement vs. Manual Assignment

Since November 8, 2023, Databricks automatically enables new workspaces for Unity Catalog. If your workspace was enabled automatically, the workspace admin receives additional default privileges, including the ability to create most Unity Catalog object types (such as catalogs, schemas, tables, and models) and to grant access to the objects they create. For a complete list of these default privileges, see Admin Privileges in Unity Catalog. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

If your workspace was not automatically enabled and was later manually assigned to a Unity Catalog [[metastore|Metastore]], workspace admins have no more access to Unity Catalog objects by default than any other user. However, they do retain standard workspace management capabilities — such as managing job ownership and viewing notebooks — which may provide indirect access to data registered in Unity Catalog. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md:39-40]

## Indirect Data Access via Workspace Management

Even without direct Unity Catalog privileges, a workspace admin can indirectly access Unity Catalog data through workspace-level operations. For example, viewing a notebook that contains queries against Unity Catalog tables, or managing a job that reads from a table, can expose data content. Account admins should therefore consider the scope of data that could be reached through workspace management tasks when designating workspace admins. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md:40]

## Restricting Workspace Admin Privileges

Account admins can use the `RestrictWorkspaceAdmins` setting to limit the privileges of workspace admins. This setting helps enforce tighter control over who can manage Unity Catalog objects and indirectly access data. See [[RestrictWorkspaceAdmins Setting|Restrict Workspace Admins]] for configuration details. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md:41]

## Best Practices

- **Distribute the workspace admin role carefully** — it is a highly privileged position. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md:37]
- **Review existing workspace admin assignments** before enabling a workspace for Unity Catalog to understand who will hold these privileges. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md:36]
- **Use workspace-catalog bindings** to limit catalog access by workspace boundaries. For example, ensure that workspace admins and users can only access production data in `prod_catalog` from a production workspace environment, `prod_workspace`. The default is to share the catalog with all workspaces attached to the current [[metastore|Metastore]]. Similarly, external locations can be bound to specific workspaces. See [[Workspace-Catalog Binding]] and [Assign an external location to specific workspaces](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/manage-external-locations#workspace-binding). ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md:43-45]
- **Audit indirect data access paths**, such as job ownership and notebook content, to ensure sensitive data is not exposed through workspace management tasks.

## Related Concepts

- [[Unity Catalog]] — The data governance layer responsible for access control
- [[Unity Catalog Metastore]] — The top-level container for managed data
- Admin Privileges in Unity Catalog — Detailed list of default privileges for workspace admins
- [[RestrictWorkspaceAdmins Setting|Restrict Workspace Admins]] — Account-level setting to limit workspace admin powers
- [[Workspace-Catalog Binding]] — Mechanism to restrict catalog access by workspace
- [[Account Admin (Unity Catalog)|Account Admin Privileges]] — Roles and responsibilities for account-level governance

## Sources

- enable-a-workspace-for-unity-catalog-databricks-on-aws.md
```

# Citations

1. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
2. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md:39-40](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
3. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md:40-40](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
4. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md:41-41](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
5. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md:37-37](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
6. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md:36-36](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
7. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md:43-45](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
