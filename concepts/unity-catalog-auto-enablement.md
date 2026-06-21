---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 107afa05e73efcef3d8ae3d71809ae09cf1f55251cf0012efebd13d6eedb1d3d
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-auto-enablement
    - UCA
  citations:
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Unity Catalog Auto-enablement
description: Automatic enablement of Unity Catalog for all Databricks workspaces created after November 8, 2023
tags:
  - databricks
  - workspace-setup
  - migration
timestamp: "2026-06-19T10:45:44.284Z"
---

# Unity Catalog Auto-enablement

**Unity Catalog Auto-enablement** refers to the automatic activation of [Unity Catalog](/concepts/unity-catalog.md) for all new Databricks workspaces created after a specific cutoff date. This feature ensures that every new workspace starts with the unified governance layer for data and AI already enabled, eliminating the need for manual setup during workspace creation.

## Overview

Starting with workspaces created after **November 8, 2023**, Unity Catalog is automatically enabled. This applies to all Databricks workspaces on AWS, Azure, and GCP. Workspaces created before this date or those that were not enabled at creation time require a manual upgrade to Unity Catalog. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Implications

### For new workspaces

Workspaces that have Unity Catalog auto-enabled can immediately begin configuring admin roles, users, compute, permissions, and catalogs using the standard [Unity Catalog setup guide](https://docs.databricks.com/aws/en/data-governance/unity-catalog/setup-uc). ^[get-started-with-unity-catalog-databricks-on-aws.md]

### For existing workspaces

Workspaces created before November 8, 2023 (or those that were not enabled at creation) follow the [Upgrade to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/) process to enable Unity Catalog and migrate existing data. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance layer for data and AI.
- Unity Catalog setup guide – Steps for configuring a workspace that already has Unity Catalog enabled.
- [Upgrade to Unity Catalog](/concepts/upgrading-jobs-to-unity-catalog.md) – Migration path for workspaces not yet on Unity Catalog.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – A governance capability that can be applied after Unity Catalog is enabled.
- [Data Classification](/concepts/data-classification.md) – AI-driven tagging of sensitive data, integrable with Unity Catalog.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Anomaly detection and profiling available in Unity Catalog.
- [Data Lineage](/concepts/data-lineage.md) – Column-level tracking of data flow across assets.
- [Unity AI Gateway](/concepts/unity-ai-gateway.md) – Extends Unity Catalog governance to AI endpoints and agents.

## Sources

- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)
