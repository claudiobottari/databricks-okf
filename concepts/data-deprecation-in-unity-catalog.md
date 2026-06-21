---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9309952da14052959c6594ecc01329860f5a9466eba90806789e760da4fb63fc
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-deprecation-in-unity-catalog
    - DDIUC
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Data Deprecation in Unity Catalog
description: The practice of labeling Unity Catalog objects as 'deprecated' to warn users that a data asset is outdated, unreliable, or should not be used in new workflows, displayed with a restricted icon.
tags:
  - data-governance
  - data-lifecycle
  - unity-catalog
timestamp: "2026-06-19T18:52:52.468Z"
---

# Data Deprecation in Unity Catalog

**Data deprecation in Unity Catalog** refers to the practice of marking a data asset as outdated, unreliable, or unsuitable for new use by applying the `system.certification_status` system-governed tag with the value `deprecated`. Deprecated assets display a restricted icon in the workspace, notebook, and SQL editor, signaling that the asset should not be used in new workflows. This mechanism helps organizations enforce governance, retire obsolete data, and improve data discoverability and trust. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## How Deprecation Works

Deprecation is implemented through the `system.certification_status` system tag, which is governed by Unity Catalog and accepts two values: `certified` and `deprecated`. When you apply the `deprecated` value to an object, a restricted icon appears next to the object’s name in the workspace, notebook, or SQL editor. The tag key is `system.certification_status`. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types

You can apply the `deprecated` status to the following object types: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

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

To apply the `deprecated` tag, you must have the `ASSIGN` permission on the `system.certification_status` governed tag. See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md).

Alternatively, if you own the object, you must have all of the following privileges: `APPLY TAG` on the object, `USE SCHEMA` on the object’s parent schema, and `USE CATALOG` on the object’s parent catalog. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Assigning Deprecated Status

You can assign deprecated status using the workspace UI or SQL.

### Using the UI

1. Navigate to a supported object.
2. Click the kebab menu and select **Assign certification**.
3. Choose **Deprecated** (or **None** to remove the status).
4. Click **Save**.

^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Using SQL

You can also assign the `deprecated` status using SQL commands, as described in the Unity Catalog documentation. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md] The exact SQL syntax is not shown in the source material, but it follows standard Unity Catalog tag assignment patterns.

## Searching for Deprecated Data

You can filter for deprecated assets from the search page using the `certificationStatus` keyword. For example:

```
certificationStatus:deprecated
```

This returns all deprecated assets across supported object types. You can combine with other filters, such as `type:table certificationStatus:deprecated`. In the search filters UI, select **Deprecated** from the **Certification status** menu. Note that tag-based search is not supported on Dashboards, Genie Spaces, or Databricks Apps, and updates may take a few minutes to appear in search results. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Removing Deprecated Status

You can update or remove the deprecated status at any time by reassigning **None** in the UI or setting the tag value to `NULL` using SQL. After removal, the restricted icon disappears. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [Certified data](/concepts/certified-data-unity-catalog.md) – The counterpart status indicating a trustworthy asset.
- [Governed Tags](/concepts/governed-tags.md) – The tagging system that powers certification and deprecation.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance platform where these tags are applied.
- [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md) – Required permissions for assigning certification status.

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
