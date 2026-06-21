---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e2a3e57a9369e5dc1d7348d6499228b39b2f6bb021f6d84fc16a6a132ad556c
  pageDirectory: concepts
  sources:
    - manage-access-requests-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - in-product-access-request-surfaces
    - IARS
  citations:
    - file: manage-access-requests-databricks-on-aws.md
title: In-Product Access Request Surfaces
description: Multiple Databricks surfaces (Catalog Explorer, SQL editor, notebooks, AI/BI dashboards, Genie Spaces) where users can request privileges on Unity Catalog objects.
tags:
  - unity-catalog
  - access-control
  - user-interface
timestamp: "2026-06-19T19:22:15.661Z"
---

# In-Product Access Request Surfaces

**In-Product Access Request Surfaces** are the points within the Databricks workspace where users can request privileges for [Unity Catalog](/concepts/unity-catalog.md) securable objects without leaving their current workflow. After an administrator configures [Access Request Destinations](/concepts/access-request-destinations.md), users can request access directly from Catalog Explorer, the SQL editor, notebooks, AI/BI dashboards, and Genie Spaces. ^[manage-access-requests-databricks-on-aws.md]

## How It Works

The request access feature is built into several surfaces. When a user encounters a securable object they need but do not yet have privileges on, they can initiate a request from that surface. The request is pre-filled with the relevant object(s) and then routed to the configured destinations (email, Slack, Microsoft Teams, webhook, or a redirect URL). ^[manage-access-requests-databricks-on-aws.md]

If a redirect URL is configured on an object, users are taken to that external system and do not see the in-product request form. ^[manage-access-requests-databricks-on-aws.md]

## Catalog Explorer

Users with the `BROWSE` privilege on a catalog can navigate the catalog tree, open an object’s page, and request additional privileges (such as `SELECT`) from that page. Even without `BROWSE`, users can be sent a direct URL to an object’s page and request access from the same surface. ^[manage-access-requests-databricks-on-aws.md]

When a query or command fails with an `INSUFFICIENT_PERMISSIONS` error, the error message includes a **Request access** option that pre-fills the request with the referenced tables. This surface works anywhere the error appears, including the SQL editor and notebooks. ^[manage-access-requests-databricks-on-aws.md]

## AI/BI Dashboards

When an AI/BI dashboard runs without embedded credentials and a widget references datasets the viewer cannot read, the widget displays a **Request access** modal for the missing datasets. ^[manage-access-requests-databricks-on-aws.md]

## Genie Spaces

When a Genie Space references tables on which the user lacks permissions, the space shows a `PERMISSION_DENIED` banner with a **Request access** modal listing the inaccessible tables. ^[manage-access-requests-databricks-on-aws.md]

## Related Concepts

- [Access Request Destinations](/concepts/access-request-destinations.md) – The configuration that determines where requests are sent (email, Slack, Teams, webhook, or redirect URL).
- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance system for securable objects.
- [Privileges](/concepts/privileges-and-ownership.md) – The permissions (such as SELECT, MODIFY) that can be requested.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The primary browsing and management interface for Unity Catalog objects.
- AI/BI Dashboards – Dashboards that surface the request access affordance for missing datasets.
- [Genie Spaces](/concepts/genie-space-snapshot.md) – Natural-language interfaces that show the request access modal for inaccessible tables.
- SQL Editor – One of the surfaces where `INSUFFICIENT_PERMISSIONS` errors trigger the request access option.

## Sources

- manage-access-requests-databricks-on-aws.md

# Citations

1. [manage-access-requests-databricks-on-aws.md](/references/manage-access-requests-databricks-on-aws-de8a9a55.md)
