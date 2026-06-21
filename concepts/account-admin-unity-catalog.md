---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de1659bd293cafd98dca905273bd52d69a4ca830b949d4ecfe9e16ec3153f825
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-admin-unity-catalog
    - AA(C
    - Account Admin
    - Account Admin Privileges
    - Account admin
    - Account admin|account admins
    - account admin
    - account-admin-role-in-unity-catalog
    - AARIUC
    - Admin Roles in Unity Catalog
    - Admin roles in Unity Catalog
    - account-admin-role-unity-catalog
    - AAR(C
    - Account Admin Role
    - account-admins-unity-catalog
    - Account Admins
    - Account admins
    - account admins
    - account-admins-in-unity-catalog
    - AAIUC
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Account Admin (Unity Catalog)
description: A highly privileged role operating at the Databricks account level, responsible for creating and linking metastores and workspaces, and assigning admin roles.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-19T21:59:38.067Z"
---

```markdown
# Account admin (Unity Catalog)

**Account admin** is a highly privileged role that operates at the Databricks account level. From a [[Unity Catalog]] permissions perspective, account admins are responsible for creating and linking metastores and workspaces, as well as assigning administrative roles across the account.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Responsibilities

Account admins have privileges over the entire Databricks account. Their key capabilities include creating and linking metastores and workspaces, assigning admin roles, and managing account-level settings. Because of the breadth of these privileges, the role should be assigned with care.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Relationship to [[metastore|Metastore]] and workspace admins

Account admins are one of three important administrator roles in Unity Catalog, alongside [[Workspace Admin (Unity Catalog)|workspace admin]] and [[Metastore Admin Role|metastore admin]]. Account admins can assign the [[metastore|Metastore]] admin role to a user, service principal, or group. When an account admin manually creates a [[metastore|Metastore]], they become that metastore’s initial owner and [[metastore|Metastore]] admin by default. They can later transfer the [[metastore|Metastore]] admin role to another principal and relinquish it themselves.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Account admins can also restrict the privileges of workspace admins by using the `RestrictWorkspaceAdmins` setting.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assigning a [[metastore|Metastore]] admin

Only account admins can assign the [[metastore|Metastore]] admin role. Databricks recommends nominating a group as the [[metastore|Metastore]] admin so that any member of the group automatically inherits the role. The assignment can be performed in the account console under the **Catalog** section, by editing the [[metastore|Metastore]] properties. It may take up to 30 seconds for the change to be reflected across the account.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Best practices

Because the account admin role grants control over the entire Databricks account, it should be distributed carefully. Use groups for role assignments where possible, and limit the number of individual account admins.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- Workspace admin – administrator within a single workspace
- [[Metastore Admin Role|Metastore admin]] – optional role governing data access and ownership in a Unity Catalog [[metastore|Metastore]]
- [[Unity Catalog]] – the data governance layer that these admin roles manage
- [[Metastore]] – a container for Unity Catalog metadata
- Workspace – a Databricks environment tied to a [[metastore|Metastore]]

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md
```

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
