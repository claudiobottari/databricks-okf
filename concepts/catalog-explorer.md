---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b95433c7d1e72bb39838b97fa29ea570ef5f59eb3ddd028408fbfec06e56f49
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
    - manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
    - what-is-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - catalog-explorer
    - Databricks Catalog Explorer
  citations:
    - file: what-is-unity-catalog-databricks-on-aws.md
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
    - file: manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
title: Catalog Explorer
description: The Databricks UI tool for navigating, discovering, and managing Unity Catalog assets including tables and their quality configurations.
tags:
  - unity-catalog
  - user-interface
  - data-discovery
timestamp: "2026-06-19T09:28:43.128Z"
---

# Catalog Explorer

**Catalog Explorer** is the primary Databricks user interface for discovering, managing, and interacting with all securable objects governed by [Unity Catalog](/concepts/unity-catalog.md), including tables, views, volumes, functions, models, and more. It serves as the data and AI asset browser within the Databricks workspace. ^[what-is-unity-catalog-databricks-on-aws.md]

## Accessing Catalog Explorer

To open Catalog Explorer, click the Data icon in the workspace left sidebar. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md] The interface provides a navigable tree of catalogs, schemas, and objects, and supports direct actions such as viewing table details, managing permissions, and configuring governance features. ^[what-is-unity-catalog-databricks-on-aws.md]

## Capabilities

### Data Discovery

Catalog Explorer allows users to browse and search across all Unity Catalog objects, making it the primary tool for data discovery within a workspace. ^[what-is-unity-catalog-databricks-on-aws.md]

### Data Quality Monitoring

Users can navigate to any table and access its **Quality** tab to configure [Data Profiling](/concepts/data-profiling.md) and anomaly detection. From Catalog Explorer, a user can enable or configure data quality monitoring, select a profile type (e.g., TimeSeries, Inference), set schedules, and view refresh history. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### OpenSharing Management

For [Delta Sharing](/concepts/delta-sharing.md) providers, Catalog Explorer supports the full lifecycle of managing OpenSharing shares and recipients:

- **Add recipients to a share** — From a share’s detail page, click **Add recipient** and select existing recipients. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]
- **Grant shares to a recipient** — From a recipient’s page, click **Grant share** and select the share. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]
- **Revoke access** — Remove a recipient’s access to a share either from the share’s **Recipients** tab or from the recipient’s **Shares** tab by using the kebab menu. ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]
- **View grants** — See all recipients who have access to a share (via the share’s **Recipients** tab) or all shares granted to a recipient (via the recipient’s **Shares** tab). ^[manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md]

### Access Control and Lineage

Catalog Explorer provides the interface to manage [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md), view [Data Lineage](/concepts/data-lineage.md), browse [Governed Tags](/concepts/governed-tags.md), and configure ABAC policies and other access control mechanisms. ^[what-is-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog object model](/concepts/unity-catalog-ai-asset-model.md) – The three-level namespace (`catalog.schema.object`) that Catalog Explorer navigates.
- [Data Profiling](/concepts/data-profiling.md) – Configuring profiles via the **Quality** tab.
- [OpenSharing](/concepts/opensharing.md) – Managing shares and recipients through the **OpenSharing** section.
- [Table details view](/concepts/table-quality-details-ui.md) – Detailed metadata view for any table in Catalog Explorer.

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md
- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
- what-is-unity-catalog-databricks-on-aws.md

# Citations

1. [what-is-unity-catalog-databricks-on-aws.md](/references/what-is-unity-catalog-databricks-on-aws-ea58b0e9.md)
2. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
3. [manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md](/references/manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws-738fc31c.md)
