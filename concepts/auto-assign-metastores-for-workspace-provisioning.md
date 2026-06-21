---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bac0005fe1050ddac3e1e6fef6f14715cf6f4a3b494df3f5bc88642e8f6aec83
  pageDirectory: concepts
  sources:
    - migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-assign-metastores-for-workspace-provisioning
    - AMFWP
  citations:
    - file: migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
title: Auto-assign metastores for workspace provisioning
description: Admins must set a Unity Catalog metastore to auto-assign for every region where workspaces are deployed, ensuring new workspaces automatically receive a metastore.
tags:
  - unity-catalog
  - metastore
  - workspace-provisioning
timestamp: "2026-06-19T19:36:32.396Z"
---

# Auto-assign metastores for workspace provisioning

**Auto-assign metastores for workspace provisioning** is a configuration step that account administrators must perform to prepare for the September 30, 2026 change when new workspaces will be provisioned without access to legacy features including the [Hive metastore](/concepts/built-in-hive-metastore.md). Setting a [Metastore](/concepts/metastore.md) to auto-assign ensures that new workspaces are automatically associated with a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) upon creation, removing the need for manual [Metastore](/concepts/metastore.md) assignment during workspace provisioning.

## Overview

When provisioning new workspaces, Databricks requires each workspace to be associated with a [Metastore](/concepts/metastore.md). If a [Metastore](/concepts/metastore.md) is not set to auto-assign for the region in which a workspace is deployed, an administrator must manually assign a [Metastore](/concepts/metastore.md) when the workspace is created. To streamline provisioning — especially for organizations that use automation and CI/CD pipelines — Databricks recommends enabling auto-assign for at least one [Metastore](/concepts/metastore.md) in each region where workspaces are deployed. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Requirement

As part of preparing for the September 30, 2026 migration to [UC-only workspaces](/concepts/uc-only-workspaces.md), account administrators must set a [Metastore](/concepts/metastore.md) to auto-assign for **every region** in which they deploy workspaces. Failure to do so will require manual [Metastore](/concepts/metastore.md) assignment at workspace creation time, which can interrupt automated provisioning workflows. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## How to configure

To enable auto-assign for a [Metastore](/concepts/metastore.md), administrators use the account console. The specific procedure is documented in the guide on how to enable a metastore to be automatically assigned to new workspaces. Once enabled, any new workspace created in the designated region will automatically be associated with that [Metastore](/concepts/metastore.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Relationship to broader migration

Setting metastores to auto-assign is one of several preparation steps for the UC-only workspace migration. Other required steps include:

- Removing dependency on [DBFS root and DBFS mounts](/concepts/dbfs-root-and-dbfs-mounts-deprecation.md) in workspace provisioning automation
- Migrating workflows to non-legacy access modes (away from no-isolation shared clusters)
- Testing the new default behavior by enabling the **Disable legacy features** setting in the account console

^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that replaces the Hive [Metastore](/concepts/metastore.md)
- [UC-only workspaces](/concepts/uc-only-workspaces.md) — Workspaces provisioned without access to legacy features
- [Hive metastore](/concepts/built-in-hive-metastore.md) — A legacy [Metastore](/concepts/metastore.md) that will not be available in new workspaces after September 30, 2026
- Workspace provisioning — The process of creating new Databricks workspaces
- Account console — The administrative interface for managing account-level settings

## Sources

- migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md

# Citations

1. [migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md](/references/migrate-your-account-to-uc-only-workspaces-databricks-on-aws-222dccd3.md)
