---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a6379be22676034d9061cd56211e7272b6c9bea7d0fe5ed1627a0f720a33eed
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-certification
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Data Certification
description: The practice of labeling data assets (catalogs, schemas, tables, etc.) as meeting internal standards for accuracy, completeness, and trust, indicated by a checkmark icon in the Databricks workspace.
tags:
  - data-governance
  - data-quality
  - unity-catalog
timestamp: "2026-06-18T12:23:03.247Z"
---

# Data Certification

**Data Certification** is the practice of labeling data assets within [Unity Catalog](/concepts/unity-catalog.md) with a standardized status indicator — either *certified* or *deprecated* — to communicate data quality, trustworthiness, and lifecycle stage to users across the organization. Databricks implements this through a system-governed tag, `system.certification_status`, that can be applied to catalogs, schemas, tables, views, volumes, functions, registered models, dashboards, Genie Spaces, Databricks apps, and notebooks. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Certification Status System Tag

The `system.certification_status` tag is a [system tag](/concepts/system-tags.md) with exactly two allowed values: `certified` and `deprecated`. When applied to an object, a visual indicator appears next to the object's name in the workspace UI. Certified assets display a check mark and deprecated assets display a restricted icon. This helps organizations enforce governance, improve data discoverability, and increase trust in analytics and AI applications. The tag also influences how data appears in notebooks and the SQL editor. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Certified

A `certified` status indicates that a data asset has met internal standards for accuracy, completeness, and trust. It signals to consumers that the asset is reliable and suitable for use in production workflows, dashboards, or machine learning pipelines. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Deprecated

A `deprecated` status warns that a data asset is outdated, no longer reliable, or should not be used in new workflows. It helps prevent users from inadvertently building on top of stale or untrusted data and encourages migration to newer, supported assets. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types

You can apply the certification status tag to the following Unity Catalog securable objects:

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

^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Permissions Required

To assign the certification status tag, you need two sets of permissions:

1. **ASSIGN permission on the `system.certification_status` governed tag** itself. See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md).
2. **Standard tag privileges on the target object**: `APPLY TAG` on the object, `USE SCHEMA` on the object's parent schema, and `USE CATALOG` on the object's parent catalog. You must own the object or have all three privileges.

^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Assigning Certification Status

You can assign or remove certification status using either the workspace UI or SQL.

### Using the UI

1. Navigate to a supported object.
2. Click the kebab menu and select **Assign certification**.
3. Choose **Certified**, **Deprecated**, or **None**.
4. Click **Save**.

You can update or remove the status at any time. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Using SQL

Although the source primarily describes the UI, you can also use `ALTER ... SET TAGS` or `ALTER ... UNSET TAGS` SQL commands to assign the governed tag. For example:

```sql
ALTER TABLE my_catalog.my_schema.my_table
  SET TAGS ('system.certification_status' = 'certified');
```

## Searching by Certification Status

You can filter assets by certification status from the Databricks search page. Use the `certificationStatus` keyword in the search bar. For example:

- `type:table certificationStatus:certified` returns only certified tables.
- `certificationStatus:deprecated` returns all deprecated assets across supported types.

You can also select **Certified** or **Deprecated** from the **Certification status** filter menu in the UI. Note that search using tags is not supported for dashboards, Genie Spaces, or Databricks apps. It may take a few minutes for certification or deprecation updates to appear in search results. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Relationship to Data Governance

Data Certification is a core component of [data governance](/concepts/ai-governance.md) in Unity Catalog. By tagging assets with a clear lifecycle indicator, organizations can:

- **Increase trust** in analytics and AI applications by guiding users toward certified data. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]
- **Prevent misuse** of deprecated datasets that may contain stale or incorrect information.
- **Enforce governance** by making certification status visible throughout the workspace.
- **Improve discoverability** so users can quickly find reliable assets and avoid outdated ones.

## Related Concepts

- [System Tags](/concepts/system-tags.md) — Managed tags provided by Databricks for governance use cases
- [Governed Tags](/concepts/governed-tags.md) — Tags with permission controls that can be used in ABAC policies
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that supports certification tagging
- Data Quality — The broader discipline that certification status helps communicate
- Data Discoverability — How certification improves findability of trusted data
- [ABAC Policies from Data Classification](/concepts/abac-policies-from-data-classification.md) — Another use of tags for access control
- Deprecation — The lifecycle phase indicated by the deprecated tag value

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
