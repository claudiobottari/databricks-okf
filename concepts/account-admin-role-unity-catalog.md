---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35cb348abed611e36ce2921b786bbf211f277fef63e74d87ebc73569ffa9f6d9
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-admin-role-unity-catalog
    - AAR(C
    - Account Admin Role
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Account Admin Role (Unity Catalog)
description: A highly privileged role operating at the Databricks account level, responsible for creating and linking metastores and workspaces, and assigning admin roles.
tags:
  - unity-catalog
  - admin-roles
  - account-administration
timestamp: "2026-06-19T08:54:23.264Z"
---

# Account Admin Role (Unity Catalog)

The **Account Admin Role** is the highest-level administrative role in a Databricks deployment, operating at the **Databricks account level** rather than within a single workspace or [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). Account admins have broad privileges over the entire Databricks account and are responsible for foundational infrastructure tasks such as creating and linking [metastores](/concepts/metastore.md), workspaces, and assigning admin roles to other users. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Scope of Authority

Account admins exercise control across the entire Databricks account, not within individual workspaces. Their responsibilities include:

- Creating and linking [Unity Catalog metastores](/concepts/unity-catalog-metastore.md) to workspaces.
- Creating and managing workspaces.
- Assigning admin roles to users and groups, including [workspace admin](/concepts/workspace-admin-unity-catalog.md) and [metastore admin](/concepts/metastore-admin-role.md) roles.
- Managing [account-level settings](/concepts/account-level-legacy-feature-settings.md) and [identity providers](/concepts/internal-vs-external-identity-providers.md).
- Configuring billing and account usage.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Relationship to Other Admin Roles

From a Unity Catalog permissions perspective, the three most important admin roles are account admins, workspace admins, and [Metastore](/concepts/metastore.md) admins. Account admins and workspace admins are **required** for all deployments; the [Metastore](/concepts/metastore.md) admin role is **optional**. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Account Admin vs. Workspace Admin

- **Account admins** operate at the Databricks account level, managing metastores, workspaces, and account-level resources.
- **Workspace admins** operate within a single workspace, managing workspace membership, jobs, and workspace objects.
- Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Account Admin vs. [Metastore](/concepts/metastore.md) Admin

- **Account admins** create and manage metastores at the account level.
- **Metastore admins** (optional) govern data access, ownership, and top-level Unity Catalog securable objects within a single [Metastore](/concepts/metastore.md).
- When an account admin creates a [Metastore](/concepts/metastore.md), they become its initial [metastore admin](/concepts/metastore-admin-role.md) by default. They can then assign the [Metastore](/concepts/metastore.md) admin role to a different user, group, or service principal. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Key Capabilities

Account admins have the following key capabilities:

- [Create and link metastores](/concepts/unity-catalog-metastore.md) and workspaces.
- [Assign admin roles](/concepts/assigning-the-metastore-admin-role.md) to users, groups, and service principals.
- Manage account-level settings and [identity providers](/concepts/internal-vs-external-identity-providers.md).
- Configure billing and account usage.
- Audit and monitor account activity.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Security Considerations

The account admin role is a **highly privileged** role that should be **distributed carefully**. Only trusted individuals should be granted this role, as it provides broad access to sensitive account-level resources and settings. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Best Practices

- **Use groups** for admin roles rather than individual users to simplify role management.
- **Restrict workspace admin privileges** using the `RestrictWorkspaceAdmins` setting when appropriate.
- **Distribute administrative responsibility** by assigning [metastore admin](/concepts/metastore-admin-role.md) roles to separate users or groups from account admins when possible.
- **Audit regularly** to identify and remove unnecessary admin privileges.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Workspace Admin Role](/concepts/workspace-admin-role-unity-catalog.md) – Manages a single workspace within the account.
- [Metastore Admin Role](/concepts/metastore-admin-role.md) – Optional role governing data access within a [Metastore](/concepts/metastore.md).
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer managed by [Metastore](/concepts/metastore.md) and account admins.
- Admin Roles Overview – Summary of all Databricks administrative roles.
- Account-Level Privileges – The full set of privileges held by account admins.
- Workspace-Level Privileges – The full set of privileges held by workspace admins.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
