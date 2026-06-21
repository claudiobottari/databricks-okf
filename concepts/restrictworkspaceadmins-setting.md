---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56e1cb8982b515e9f87d3a1fa20dfb418b15223fec3258cc6fb8e88c39112295
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - restrictworkspaceadmins-setting
    - Restrict Workspace Admins
    - Restrict workspace admins
    - RestrictWorkspaceAdmins
    - Workspace Admin|Workspace admins
    - Workspace admin|workspace admins
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: RestrictWorkspaceAdmins Setting
description: A setting that account admins can use to restrict workspace admin privileges in Unity Catalog.
tags:
  - unity-catalog
  - admin-roles
  - security
timestamp: "2026-06-19T08:54:23.309Z"
---

# RestrictWorkspaceAdmins Setting

**RestrictWorkspaceAdmins** is an account-level setting in Databricks that enables account admins to restrict the privileges of workspace admins.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Overview

Account admins can use the `RestrictWorkspaceAdmins` setting to limit the scope of workspace admin authority. Workspace admins normally have broad administrative capabilities within a single workspace, including managing workspace membership, jobs, and workspace objects.^[admin-privileges-in-unity-catalog-databricks-on-aws.md] The setting provides a mechanism for account-level administrators to enforce more centralized governance over workspace-level operations.

## Administration

Only account admins can enable or disable the `RestrictWorkspaceAdmins` setting. The setting is managed at the account level, through the account console under workspace settings.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Impact on Workspace Admins

When `RestrictWorkspaceAdmins` is enabled, workspace admins lose certain privileges that they would otherwise have by default. This includes restrictions on workspace-level administrative capabilities that could affect account-wide resources or metastore-level operations.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Account Admin (Unity Catalog)](/concepts/account-admin-unity-catalog.md) — the role that manages this setting
- Workspace admin — the role whose privileges are affected by this setting
- [Metastore admin](/concepts/metastore-admin-role.md) — an optional role that can be used when workspace admin privileges are restricted
- [Unity Catalog](/concepts/unity-catalog.md) — the data governance layer that workspace admins interact with
- [Account-level settings](/concepts/account-level-legacy-feature-settings.md) — broader category of configuration options managed at the account level

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
