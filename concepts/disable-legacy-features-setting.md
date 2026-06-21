---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04046fe3c629756caf8597872c2113a6187b486f2ccec75eb51925b02203d476
  pageDirectory: concepts
  sources:
    - migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disable-legacy-features-setting
    - DLFS
    - Disable Legacy Features
    - Disable legacy features
    - Disable legacy features account setting
    - Disable access to legacy features in new workspaces
    - Disable legacy features (account level)
    - Disabling access to legacy features in new workspaces
    - Disabling access to legacy features in your workspaces
    - Legacy features
    - disable access to legacy features
  citations:
    - file: migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md
title: Disable legacy features setting
description: An account console setting that allows organizations to test the new UC-only default behavior before the September 30, 2026 deadline by disabling legacy features in new workspaces.
tags:
  - unity-catalog
  - administration
  - testing
timestamp: "2026-06-19T19:36:17.835Z"
---

# Disable Legacy Features Setting

The **Disable legacy features setting** is an account-level toggle in the Databricks account console that, when enabled, causes all new workspaces to be provisioned without access to a set of legacy features. This setting exists to allow organizations to test the post–September 30, 2026 default workspace behavior before the mandatory change takes effect. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## What the Setting Disables

Enabling the **Disable legacy features** setting removes access to the following features in newly created workspaces:

- [DBFS root and DBFS mounts](/concepts/dbfs-root-and-dbfs-mounts-deprecation.md)
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md)
- Databricks Runtime versions prior to 13.3 LTS

^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Context and Deadline

Accounts created before December 18, 2025 that still use legacy features are affected. Starting **September 30, 2026**, all new workspaces in every account — regardless of whether the setting is enabled — will be provisioned without access to those legacy features. Existing workspaces and their workflows are not impacted by this change. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

By enabling the setting early, administrators can validate that their workspace provisioning automation and operational procedures do not depend on the legacy features that will eventually be unavailable. ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## How to Enable the Setting

Admins can enable the **Disable legacy features** setting in the account console. For detailed instructions, refer to the related documentation page: [Disable access to legacy features in new workspaces](/concepts/disable-legacy-features-setting.md). ^[migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance solution that replaces legacy Hive [Metastore](/concepts/metastore.md) capabilities.
- [UC-only workspaces](/concepts/uc-only-workspaces.md) — Workspaces provisioned without legacy features, also known as Unity Catalog–only workspaces.
- [DBFS root and DBFS mounts](/concepts/dbfs-root-and-dbfs-mounts-deprecation.md) — Legacy file storage features that are disabled when the setting is on.
- [Hive metastore](/concepts/built-in-hive-metastore.md) — Legacy [Metastore](/concepts/metastore.md) that is disabled.
- [No Isolation Shared Clusters](/concepts/no-isolation-shared-clusters.md) — Legacy compute access mode that is disabled.

## Sources

- migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md

# Citations

1. [migrate-your-account-to-uc-only-workspaces-databricks-on-aws.md](/references/migrate-your-account-to-uc-only-workspaces-databricks-on-aws-222dccd3.md)
