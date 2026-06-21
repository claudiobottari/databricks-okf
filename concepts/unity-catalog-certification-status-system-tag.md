---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 133484e0f5cfb2122ec27e90978b3f44410860756de8c3704707ebf1591dd134
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-certification-status-system-tag
    - UCCSST
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Unity Catalog Certification Status System Tag
description: A system-governed tag (system.certification_status) in Databricks Unity Catalog that marks data assets as certified or deprecated to indicate data quality and lifecycle status.
tags:
  - data-governance
  - unity-catalog
  - tagging
timestamp: "2026-06-19T10:36:09.414Z"
---

# Unity Catalog Certification Status System Tag

The **Unity Catalog Certification Status System Tag** (`system.certification_status`) is a system-governed tag that allows users to label objects with indicators of data quality or lifecycle status. It supports two values – `certified` and `deprecated` – and helps organizations enforce [governance](/concepts/ai-governance.md), improve [data discoverability](/concepts/data-discovery-in-unity-catalog.md), and increase trust in analytics and AI applications. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Tag Values

| Value | Meaning | Icon in Workspace |
|-------|---------|-------------------|
| `certified` | The data asset has met internal standards for accuracy, completeness, and trust. | Check mark |
| `deprecated` | The data asset is outdated, no longer reliable, or should not be used in new workflows. | Restricted icon |

The tag key is `system.certification_status`. The tag values are the only two values available; there is no other certification level. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types

You can apply the certification status tag to the following Unity Catalog objects: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

- [Catalog](/concepts/unity-catalog.md)
- Schema
- Table
- View
- Volume
- Function
- [Registered model](/concepts/functions-and-registered-models.md)
- Dashboard
- Genie Space
- Databricks App
- Notebook

## Permissions Required

To apply the certification status tag to an object, you must have:

1. The `ASSIGN` permission on the `system.certification_status` [governed tag](/concepts/governed-tags.md). (See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md).)
2. One of the following:
   - Ownership of the object, **or**
   - All of these privileges on the object:
     - `APPLY TAG`
     - `USE SCHEMA` on the parent schema
     - `USE CATALOG` on the parent catalog

^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Assigning Certification Status

You can assign, update, or remove the status using the workspace UI or SQL.

- **Workspace UI**: Navigate to a supported object, click the kebab menu, select **Assign certification**, then choose **Certified**, **Deprecated**, or **None**. Click **Save**.
- **SQL**: Use the `ALTER ... SET TAGS` or related SQL commands to set the `system.certification_status` tag with the desired value.

You can change the status at any time. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Searching by Certification Status

You can filter for certified or deprecated assets directly from the search page using the `certificationStatus` keyword. For example: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

```sql
type:table certificationStatus:certified
certificationStatus:deprecated
```

You can also select **Certified** or **Deprecated** from the **Certification status** filter menu in the search filters. Note that search using tags is not supported on dashboards, Genie Spaces, or Databricks apps. It may take a few minutes for certification or deprecation updates to appear in search results. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog system tags](/concepts/unity-catalog-system-governed-tags.md)
- [Governed Tags](/concepts/governed-tags.md)
- Data lineage and certification
- Data quality management in Unity Catalog

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
