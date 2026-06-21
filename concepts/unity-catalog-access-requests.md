---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fab383b388cd391e4d2aeba9e02fc6894fb811d64a0964c62056737c77d4824f
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-access-requests
    - UCAR
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Access Requests
description: Configurable destinations (email, Slack, Teams, webhooks) for receiving access requests on Unity Catalog securable objects.
tags:
  - access-control
  - unity-catalog
  - workflow
timestamp: "2026-06-19T17:23:57.886Z"
---

# Unity Catalog Access Requests

**Unity Catalog Access Requests** enable users to request access to securable objects in [Unity Catalog](/concepts/unity-catalog.md), while administrators can configure how and where those requests are delivered. The feature is part of the broader access control framework and is managed under the **Manage privileges** section of the Unity Catalog documentation. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Configuration

Administrators configure destinations for access requests on Unity Catalog securable objects. Supported destinations include email, Slack, Microsoft Teams, and webhooks. ^[access-control-in-unity-catalog-databricks-on-aws.md]

This mechanism complements other access control models such as:

- [Privileges and Ownership](/concepts/privileges-and-ownership.md) — granting specific permissions on objects
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — tag-driven dynamic policies
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — table-level data filtering

For detailed configuration steps, see the official documentation on [Access Request Destinations](/concepts/access-request-destinations.md).

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- Securable Objects
- [Manage Privileges](/concepts/manage-privilege.md)
- Access Control in Unity Catalog

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
