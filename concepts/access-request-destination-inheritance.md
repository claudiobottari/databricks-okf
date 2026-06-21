---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21d36cffaf0509312e694d7291d96c0b37e130ac6016a01451e921643bd6dc36
  pageDirectory: concepts
  sources:
    - manage-access-requests-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-request-destination-inheritance
    - ARDI
  citations:
    - file: manage-access-requests-databricks-on-aws.md
title: Access Request Destination Inheritance
description: Destinations configured at higher levels of the Unity Catalog hierarchy automatically apply to child objects that lack explicit destinations.
tags:
  - unity-catalog
  - access-control
  - hierarchy
timestamp: "2026-06-19T19:21:26.492Z"
---

# Access Request Destination Inheritance

**Access Request Destination Inheritance** is a behavior in [Unity Catalog](/concepts/unity-catalog.md) where an access request destination configured at a higher level in the object hierarchy automatically applies to all child objects that do not have their own explicitly configured destination. This inheritance simplifies the management of where Access Requests are routed, especially in large metastores. ^[manage-access-requests-databricks-on-aws.md]

## How Inheritance Works

When you configure a destination — such as an email address, Slack channel, webhook, or redirect URL — on a parent object (e.g., a catalog), that destination is inherited by all nested child objects (e.g., schemas, tables, views, volumes, functions) that do *not* have their own destination setting. If a child object already has an explicit destination configured, the inherited destination does not override it; the child’s explicit destination takes precedence. ^[manage-access-requests-databricks-on-aws.md]

This inheritance applies to most securable objects in Unity Catalog, including metastores, catalogs, schemas, tables, views, volumes, functions, models, storage credentials, service credentials, external locations, and connections. ^[manage-access-requests-databricks-on-aws.md]

## Example

If you set an access request destination on the catalog `sales_catalog`, that destination is automatically inherited by all schemas and objects (tables, views, etc.) inside `sales_catalog` that do not have their own destination. The inherited destinations are visible in the user interface — for example, when creating a new schema under a catalog that has destinations, the "Create a new schema" modal lists the inherited destinations. ^[manage-access-requests-databricks-on-aws.md]

![Access request destination inheritance example](https://docs.databricks.com/aws/en/assets/images/rfa-destination-inheritance-17adc9489357e4d5effff29172068e49.png)
*Diagram: Destinations configured at the catalog level are inherited by schemas and objects, except where an explicit destination is set.*

## Implications

- **Reduced administrative overhead:** Administrators can set destinations at the catalog or schema level rather than on every individual table or view. ^[manage-access-requests-databricks-on-aws.md]
- **Partial overrides:** Child objects with explicit destinations break the inheritance chain for themselves, but siblings without destinations still inherit from the parent. ^[manage-access-requests-databricks-on-aws.md]
- **Default email destinations:** As an alternative to manual configuration, [Metastore](/concepts/metastore.md) admins and workspace admins can enable default email destinations. When enabled, requests for catalog objects are sent to the catalog owner’s email, and requests for objects outside a catalog (e.g., external locations) are sent to the object owner’s email. This ensures delivery even when no destination is explicitly configured. ^[manage-access-requests-databricks-on-aws.md]

## Related Concepts

- [Access Request Destinations](/concepts/access-request-destinations.md) — The types of destinations and how to configure them on objects.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance framework that supports access requests.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI surface where users can request access and admins configure destinations.
- [Default Email Destinations](/concepts/default-email-destinations.md) — A fallback that delivers requests to object owners when no destination is set.
- Access Requests — The overall feature for requesting and granting permissions.

## Sources

- manage-access-requests-databricks-on-aws.md

# Citations

1. [manage-access-requests-databricks-on-aws.md](/references/manage-access-requests-databricks-on-aws-de8a9a55.md)
