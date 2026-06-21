---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4bd6ece71acbf8d3bd262a6bacce56c1fef5d50be50e2762455301816336c56
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - enforce-table-access-control
    - ETAC
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Enforce Table Access Control
description: The practice of restricting users to clusters with table access control enabled by denying cluster creation permissions and CAN ATTACH TO permissions for non-compliant clusters.
tags:
  - databricks
  - security
  - enforcement
  - access-control
timestamp: "2026-06-19T18:39:53.402Z"
---

# Enforce Table Access Control

**Enforce Table Access Control** refers to the administrative practice of restricting users to clusters that have [Table Access Control](/concepts/table-access-control-tacl.md) enabled, ensuring that users access only the data they are authorized to see. This is a critical step in data governance for Databricks workspaces using the built-in [Hive Metastore](/concepts/built-in-hive-metastore.md) (legacy).

## Overview

After a workspace admin enables table access control for the workspace, enforcing that control requires additional measures. Simply enabling the feature does not automatically restrict users—admins must actively prevent users from accessing clusters that lack table access control. If a user can attach to or create a cluster without table access control, they can access any data from that cluster, bypassing the intended restrictions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Administrative Actions

To enforce table access control, workspace administrators must ensure two conditions:

1. **Users do not have permission to create clusters.** If a user creates a cluster without table access control enabled, they can access any data from that cluster regardless of any configured privileges. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

2. **Users do not have CAN ATTACH TO permission for any cluster that is not enabled for table access control.** Even if users cannot create clusters, they could bypass restrictions by attaching to an existing cluster that lacks table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Relationship to Workspace Settings

Enforcing table access control builds on the workspace-level **Table Access Control** setting in the admin settings page. The workspace admin must:

1. Go to the **settings page**.
2. Click the **Security** tab.
3. Turn on the **Table Access Control** option.

After enabling this setting, the admin must apply the enforcement measures described above. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Important Consideration

Even when table access control is enabled and enforced for a cluster, Databricks workspace administrators retain access to file-level data. The enforcement protects against unauthorized users but does not restrict workspace admins. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- [Table Access Control](/concepts/table-access-control-tacl.md) — The feature that restricts access to Hive [Metastore](/concepts/metastore.md) securable objects.
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — The legacy [Metastore](/concepts/metastore.md) to which table access control applies.
- Cluster Access Modes — Standard access mode enables table access control by default.
- [Compute Permissions](/concepts/can-manage-permission.md) — Permissions that control who can create, attach to, and manage clusters.
- [Hive Metastore Privileges and Securable Objects](/concepts/hive-metastore-privileges-and-securable-objects.md) — The privilege system used once table access control is enabled.
- Data Governance — The broader discipline of managing data access and security.

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
