---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df8706b91007fe9a9d2aebe5b7c9ef0919287226712b99990f43b1f0f6f7e861
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-requests-in-unity-catalog
    - ARIUC
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Access Requests in Unity Catalog
description: Configurable destinations (email, Slack, Teams, webhooks) for access requests on Unity Catalog securable objects.
tags:
  - unity-catalog
  - access-requests
  - workflow
timestamp: "2026-06-19T21:55:18.159Z"
---

# Access Requests in Unity Catalog

**Access Requests in Unity Catalog** allow users to request access to securable objects directly within the Databricks environment. Administrators configure *destinations* for these requests so that they are routed to the appropriate team or individual for approval and granting of privileges.

## Overview

Access requests are part of the [Manage privileges](/concepts/manage-privilege.md) workflow in [Unity Catalog](/concepts/unity-catalog.md). Instead of manually granting access, administrators can define where incoming access requests should be sent. This enables a self-service model where users request access and designated recipients are notified. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Supported Destinations

Unity Catalog supports the following destinations for access requests, as listed under the **Manage access** section of the access control documentation: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Email**
- **Slack**
- **Microsoft Teams**
- **Webhooks**

These destinations can be configured per securable object or at the catalog level, depending on the setup.

## Context in Access Control

Access requests complement the broader access control model in Unity Catalog, which includes:

- [Privileges and Ownership](/concepts/privileges-and-ownership.md) – The base layer controlling who can access what.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – Tag-driven, centralized policies for dynamic data filtering and masking.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) – Per-table logic for fine-grained data visibility.
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) – Restrictions on which workspaces can access certain catalogs, external locations, and storage credentials.

Access requests provide a mechanism for users to initiate the privilege-granting process, which is then handled through the configured destination.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Securable objects in Unity Catalog](/concepts/securable-objects-in-unity-catalog.md)
- Privileges reference
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
