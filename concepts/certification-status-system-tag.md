---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6b7b466e0b70cf7718fcf3797055c7f6cca641c7c94a37e39c81147e8399ed0
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - certification-status-system-tag
    - CSST
    - certification status
    - unity-catalog-certification-status-system-tag
    - UCCSST
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Certification Status System Tag
description: A system-governed tag (system.certification_status) in Unity Catalog that marks data assets as certified or deprecated to indicate data quality and lifecycle status.
tags:
  - data-governance
  - unity-catalog
  - tagging
timestamp: "2026-06-19T18:52:34.272Z"
---

```markdown
---
title: Certification Status System Tag
summary: "A system-governed tag (key: system.certification_status) in Databricks Unity Catalog that marks data objects as certified or deprecated, with visual indicators in the workspace."
sources:
  - flag-data-as-certified-or-deprecated-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:22:57.415Z"
updatedAt: "2026-06-18T12:22:57.415Z"
tags:
  - data-governance
  - unity-catalog
  - tagging
aliases:
  - certification-status-system-tag
  - CSST
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Certification Status System Tag

The **Certification Status System Tag** is a system-governed tag in [[Unity Catalog]] that allows users to label objects with indicators of data quality or lifecycle status. It has two predefined values: `certified` and `deprecated`. This tag helps organizations enforce governance, improve data discoverability, and increase trust in analytics and AI applications. The tag is displayed next to object names in the workspace and influences how data appears in notebooks and the SQL editor. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Tag Key and Values

The tag key is `system.certification_status`, and it supports two tag values:

| Value | Meaning | Display |
|-------|---------|---------|
| `certified` | Indicates that a data asset has met internal standards for accuracy, completeness, and trust. | Check mark icon in the workspace |
| `deprecated` | Warns that a data asset is outdated, no longer reliable, or should not be used in new workflows. | Restricted/blocked icon in the workspace |

^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types

You can apply the certification status tag to the following [[Unity Catalog]] securable objects: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

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

To apply the certification status tag to objects, you must have the **ASSIGN** permission on the `system.certification_status` governed tag. See [[Permissions for Governed Tags|Manage permissions on governed tags]] for details.

To add tags to Unity Catalog securable objects, you must own the object or have all of the following privileges: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

- `APPLY TAG` on the object
- `USE SCHEMA` on the object's parent schema
- `USE CATALOG` on the object's parent catalog

## Assigning Certification or Deprecated Status

You can assign certification or deprecated status to objects using either the workspace UI or SQL. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Using the Workspace UI

1. Navigate to a supported object.
2. Click the kebab menu (three-dot icon) and select **Assign certification**.
3. Select **Certified**, **Deprecated**, or **None**.
4. Click **Save**.

You can update or remove the status at any time. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Searching by Certification Status

You can filter for certified or deprecated assets directly from the search page using the `certificationStatus` keyword. This is useful for data discovery and governance workflows.

### Search Examples

The following snippet returns only certified tables: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

```
type:table certificationStatus:certified
```

The following snippet returns only deprecated assets across supported object types: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

```
certificationStatus:deprecated
```

### Search Filter Options

In the search filters, you can also select **Certified** or **Deprecated** from the **Certification status** filter menu. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

> **Note:** It might take a few minutes for certification or deprecation updates to appear in search results. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

> **Note:** Search using tags is not supported on dashboards, Genie Spaces, or Databricks apps. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [[Governed Tags]] — The system for managing tags in Unity Catalog
- [[Data Classification]] — Classifying data using system tags
- [[ABAC Policies from Data Classification]] — Creating access control policies from classification results
- [[Unity Catalog]] — The data governance platform providing these capabilities

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md
```

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
