---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea09e9259b614291f4916ad8324c59bf0f72a6f716e9cc546df9684dc731c147
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.88
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - restricting-workspace-admin-privileges
    - RWAP
    - Workspace admin privileges
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Restricting Workspace Admin Privileges
description: Account admins can restrict workspace admin privileges using the RestrictWorkspaceAdmins setting to limit the scope of workspace-level administrative capabilities.
tags:
  - unity-catalog
  - workspace-admins
  - security
timestamp: "2026-06-19T13:54:45.049Z"
---

# Restricting Workspace Admin Privileges

**Restricting Workspace Admin Privileges** refers to the ability for [account admins](/concepts/account-admins-unity-catalog.md) to limit the set of capabilities available to [workspace admins](/concepts/workspace-admins-unity-catalog.md) within a Databricks account. This control is implemented through the `RestrictWorkspaceAdmins` setting, which account admins can configure to reduce the scope of workspace admin permissions. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Mechanism

Account admins can enable the `RestrictWorkspaceAdmins` setting to restrict workspace admin privileges. The exact set of privileges that are removed or retained under this setting is documented separately under [Restrict workspace admins](https://docs.databricks.com/aws/en/admin/workspace-settings/restrict-workspace-admins). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Context: Workspace Admin Privileges

Workspace admins normally have broad permissions within a single workspace, including managing workspace membership, jobs, and workspace objects. For workspaces that were automatically enabled for Unity Catalog (all workspaces created after November 8, 2023), workspace admins also receive default metastore-level privileges such as `CREATE CATALOG`, `CREATE EXTERNAL LOCATION`, and others. The `RestrictWorkspaceAdmins` setting can be used to reduce these privileges. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Roles

- **Account admins** – operate at the account level and can create/link metastores and workspaces, assign admin roles, and configure the `RestrictWorkspaceAdmins` setting.
- **Workspace admins** – operate within a single workspace; their privileges can be restricted by account admins.
- **Metastore admins (optional)** – govern data access and ownership within a Unity Catalog [Metastore](/concepts/metastore.md), separate from workspace admin restrictions.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
