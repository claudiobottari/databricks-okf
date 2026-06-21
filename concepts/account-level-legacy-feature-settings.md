---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a79f311828aa4e6eb1ef6a76216d43e93e667b232bd692690c172bc0355eb58f
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-level-legacy-feature-settings
    - ALFS
    - Account-level settings
    - Legacy features account setting
    - account-level settings
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Account-Level Legacy Feature Settings
description: An account-level setting to disable legacy features, including the Hive metastore, for new workspaces before they are created
tags:
  - databricks
  - admin
  - account-settings
timestamp: "2026-06-19T15:12:26.572Z"
---

# Account-Level Legacy Feature Settings

**Account-Level Legacy Feature Settings** refers to a configuration option available to Databricks account administrators that controls whether newly created workspaces have access to legacy Hive [Metastore](/concepts/metastore.md) features. This setting operates at the account level, applying to all new workspaces created after the setting is enabled.

## Overview

Account-level legacy feature settings allow administrators to disable legacy Hive [Metastore](/concepts/metastore.md) features for new workspaces at the account level, rather than requiring individual workspace-by-workspace configuration. When enabled, this setting prevents new workspaces from using the legacy Hive [Metastore](/concepts/metastore.md) by default. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Relationship to Workspace-Level Settings

The account-level setting complements workspace-level controls. While workspace admins can disable Hive [Metastore](/concepts/metastore.md) access for their specific workspace through the **Disable legacy access** workspace admin setting, the account-level setting proactively applies this restriction to all newly provisioned workspaces. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Typical Use Cases

This setting is particularly useful during and after a Unity Catalog migration. Organizations that have completed migrating tables from the Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md) can use this account-level setting to ensure that all new workspaces automatically operate without legacy Hive [Metastore](/concepts/metastore.md) access, enforcing Unity Catalog governance from the start. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Prerequisites and Effects

Before disabling legacy Hive [Metastore](/concepts/metastore.md) features at the account level, Databricks recommends the following criteria be met:

- All tables registered in the legacy [Metastore](/concepts/metastore.md) have been migrated to Unity Catalog.
- Users should be forced to stop using tables registered in the legacy [Metastore](/concepts/metastore.md).
- All jobs have been upgraded to Databricks Runtime 13.3 LTS or above.

^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

When legacy access is disabled:

- Any jobs running against tables registered to the Hive [Metastore](/concepts/metastore.md) will fail.
- Fallback to Hive [Metastore](/concepts/metastore.md) is disabled.
- Jobs running on Databricks Runtime versions below 13.3 will fail.
- The **Legacy** heading and `hive_metastore` catalog disappear from the Catalog Explorer browser pane.
- SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail.

^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Disable Access to the Hive Metastore](/concepts/disable-legacy-hive-metastore-access.md) — Workspace-level setting for disabling legacy Hive [Metastore](/concepts/metastore.md) access.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that replaces the legacy Hive [Metastore](/concepts/metastore.md).
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Allows Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md).
- Account Settings and Configuration — Account-level administrative controls in Databricks.
- Supported Databricks Runtime Versions — Runtime compatibility requirements for legacy feature settings.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
