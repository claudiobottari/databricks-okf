---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4bd829e105a52016fb8548277ffa656462b62a277dcd6128baa9a1c6f5a43bbf
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-deprecation
    - Deprecation
    - Deprecate Data
    - deprecate data
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Data Deprecation
description: The practice of warning that a data asset is outdated, no longer reliable, or should not be used in new workflows, indicated by a restricted icon in the Databricks workspace.
tags:
  - data-governance
  - data-lifecycle
  - unity-catalog
timestamp: "2026-06-18T12:23:18.397Z"
---

# Data Deprecation

**Data deprecation** is the practice of marking data assets in [Unity Catalog](/concepts/unity-catalog.md) as deprecated using the system-governed tag `system.certification_status` with value `deprecated`. A deprecated asset is one that is outdated, no longer reliable, or should not be used in new workflows. In the Databricks workspace, deprecated objects display a restricted icon next to their name, warning users that the asset is not trustworthy. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## How It Works

Deprecation is one of two values of the `system.certification_status` system tag—the other being `certified`. The tag is managed by Databricks and appears alongside object names in the workspace, notebooks, and the SQL editor. The tag helps organizations enforce governance, improve data discoverability, and increase trust in analytics and AI applications. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types

You can apply the `deprecated` tag to the following securable objects: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

- Catalogs
- Schemas
- Tables
- Views
- Volumes
- Functions
- Registered models
- Dashboards
- Genie Spaces
- Databricks Apps
- Notebooks

## Permissions Required

To mark an asset as deprecated, you must meet the following permission requirements: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

- You must have the **ASSIGN** permission on the `system.certification_status` governed tag. (See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md).)
- You must own the object **or** have the following privileges on it:
  - `APPLY TAG` on the object
  - `USE SCHEMA` on the object's parent schema
  - `USE CATALOG` on the object's parent catalog

## Assigning Deprecated Status

### Using the Workspace UI

1. Navigate to a supported object.
2. Click the kebab menu (more options) and select **Assign certification**.
3. Choose **Deprecated** (or **None** to remove the status).
4. Click **Save**.

You can update or remove the status at any time. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Using SQL

Use the appropriate SQL command to assign the system tag with value `deprecated`. The exact SQL syntax is not shown on this page, but the assignment follows the standard governed tag operations for Unity Catalog. (Refer to the Unity Catalog tag management documentation for the specific SQL statements.)

## Searching for Deprecated Assets

You can filter for deprecated assets using the workspace search. Use the keyword `certificationStatus:deprecated` in the search field. For example: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

```
certificationStatus:deprecated
```

You can also combine it with object type filters, such as `type:table certificationStatus:deprecated`. In the search filters dropdown, select **Deprecated** from the **Certification status** menu.

> **Note:** It may take a few minutes for certification or deprecation updates to appear in search results. Search using tags is not supported on dashboards, Genie Spaces, or Databricks apps. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [Data Certification](/concepts/data-certification.md) — The complementary practice of marking assets as trusted.
- [System Tags](/concepts/system-tags.md) — Predefined, managed tags in Unity Catalog.
- [Governed Tags](/concepts/governed-tags.md) — Tags whose usage and permissions can be controlled.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that provides these features.
- Data Governance — The broader discipline of managing data quality and lifecycle.
- Search with Tags — Using tags to discover assets in the workspace.

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
