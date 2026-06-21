---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42bd36ad7b786df662505870777216fa87632e7230cccc6a16e353e1f42cc59a
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-certification-in-unity-catalog
    - DCIUC
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Data Certification in Unity Catalog
description: The practice of labeling Unity Catalog objects as 'certified' to indicate they meet internal standards for accuracy, completeness, and trust, displayed with a check mark icon.
tags:
  - data-governance
  - data-quality
  - unity-catalog
timestamp: "2026-06-19T18:52:55.803Z"
---

---

# Data Certification in Unity Catalog

**Data Certification in Unity Catalog** refers to the practice of marking data assets with a system-governed tag to indicate they have been reviewed and meet internal standards for quality and reliability. This process helps organizations enforce data governance, improve discoverability, and increase trust in analytics and AI applications. A certified asset displays a check mark icon next to its name in the workspace, while a deprecated asset shows a restricted icon. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Certification Status System Tag

The certification status is controlled by a dedicated system tag with the key `system.certification_status`. This tag supports two values:

- **certified**: Indicates that a data asset has met internal standards for accuracy, completeness, and trust. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]
- **deprecated**: Warns that a data asset is outdated, no longer reliable, or should not be used in new workflows. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types

The certification status tag can be applied to the following Unity Catalog objects: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

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

To assign the certification status tag, you must have the **ASSIGN** permission on the `system.certification_status` governed tag. See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md) for details. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

Additionally, to add tags to Unity Catalog securable objects, you must own the object or have all of the following privileges: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

- `APPLY TAG` on the object
- `USE SCHEMA` on the object's parent schema
- `USE CATALOG` on the object's parent catalog

## Assigning Certified or Deprecated Status

You can assign a certification status using either the workspace UI or SQL. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Using the UI

1. Navigate to a supported object.
2. Click the kebab menu and select **Assign certification**.
3. Choose **Certified**, **Deprecated**, or **None**.
4. Click **Save**.

You can update or remove the status at any time. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Using SQL

[The source does not provide SQL commands for assignment; the SQL option is listed but no example code is given. The page references the UI method primarily.]

## Searching by Certification Status

You can filter for certified or deprecated assets directly from the search page. Use the `certificationStatus` keyword in the search field to query objects by their certification status. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

For example, the following query returns only certified tables:

```
type:table certificationStatus:certified
```

To return only deprecated assets across all supported object types:

```
certificationStatus:deprecated
```

Alternatively, in the search filters, you can select **Certified** or **Deprecated** from the **Certification status** filter menu. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

**Note:** Search using tags is not supported on dashboards, Genie Spaces, or Databricks apps. It may also take a few minutes for certification or deprecation updates to appear in search results. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [System Tags](/concepts/system-tags.md) – Governed tags used for system-defined metadata.
- [Governed Tags](/concepts/governed-tags.md) – Tags with controlled permission assignment.
- [Unity Catalog Data Governance](/concepts/unity-catalog-governance.md) – Broader governance framework for data assets.
- [Manage Permissions on Governed Tags](/concepts/permissions-for-governed-tags.md) – How to assign permissions for tag usage.

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
