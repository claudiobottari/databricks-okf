---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e09a22a47af0ea8ec0df725e6e5f45c5e1ade7780574bd007ab4d062fa6134e0
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-admins-in-unity-catalog
    - AAIUC
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Account Admins in Unity Catalog
description: Account-level admin role in Databricks that creates and links metastores and workspaces, assigns admin roles, and operates across the entire Databricks account.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-19T13:54:30.493Z"
---

# Account Admins in Unity Catalog

**Account admins** are one of the three core administrator roles in [Unity Catalog](/concepts/unity-catalog.md), alongside Workspace Admins and [Metastore Admins](/concepts/metastore-admin-role.md). They operate at the Databricks account level and have privileges that span the entire account. This role is highly privileged and should be assigned carefully. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Responsibilities

Account admins are responsible for the following key capabilities across the Databricks account:

- Creating and linking [metastores](/concepts/metastore.md) to workspaces.
- Creating and managing workspaces.
- Assigning administrator roles (including the [Metastore](/concepts/metastore.md) admin role) to users, groups, or service principals.
- Restricting workspace admin privileges through the `RestrictWorkspaceAdmins` setting.

For a full description of the account admin role, see the Databricks documentation on [What are account admins?](https://docs.databricks.com/aws/en/admin/admin-concepts#what-are-account-admins). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Relationship with [Metastore](/concepts/metastore.md) Admins

Account admins and [Metastore](/concepts/metastore.md) admins are distinct roles. When an account admin manually creates a [Metastore](/concepts/metastore.md), that account admin becomes the [Metastore](/concepts/metastore.md)'s initial owner and [Metastore](/concepts/metastore.md) admin. However, the account admin can later assign the [Metastore](/concepts/metastore.md) admin role to a different user, group, or service principal and relinquish the role themselves.

For metastores that are provisioned automatically (in workspaces created after November 8, 2023), the initial [Metastore](/concepts/metastore.md) is created without a [Metastore](/concepts/metastore.md) admin. In that case, an account admin can assign the [Metastore](/concepts/metastore.md) admin role if needed. Databricks recommends using a group for the [Metastore](/concepts/metastore.md) admin role so that any member of the group automatically inherits the privilege. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assigning the [Metastore](/concepts/metastore.md) Admin Role

Only account admins can assign the [Metastore](/concepts/metastore.md) admin role. The steps are:

1. Log in to the [account console](https://accounts.cloud.databricks.com/) as an account admin.
2. Click the **Catalog** icon.
3. Click the name of a [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Select a group from the drop-down (search is supported).
6. Click **Save**.

It can take up to 30 seconds for the assignment change to be reflected, and longer to take effect in some workspaces due to caching. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Relationship with Workspace Admins

Account admins can use the `RestrictWorkspaceAdmins` setting to control the scope of workspace admin privileges. This setting is managed at the account level. For details, see [Restrict workspace admins](https://docs.databricks.com/aws/en/admin/workspace-settings/restrict-workspace-admins). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Best Practices

Because account admins hold broad privileges, Databricks recommends distributing this role carefully. Key recommendations include:

- Use groups rather than individual users for admin roles whenever possible.
- Assign the [Metastore](/concepts/metastore.md) admin role to a group so that membership changes are automatically reflected.
- Leverage the optional [Metastore](/concepts/metastore.md) admin role to delegate metastore-level governance without granting full account admin access.

## Related Concepts

- [Metastore Admins](/concepts/metastore-admin-role.md)
- Workspace Admins
- [Unity Catalog](/concepts/unity-catalog.md)
- Account Console
- [RestrictWorkspaceAdmins](/concepts/restrictworkspaceadmins-setting.md)
- Metastore Management

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
