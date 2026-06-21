---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fc83401668a1a756ce23037c9cf5d5ec06591959d8a807cdde348fde9b69789
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-supported-objects-for-tagging
    - UCSOFT
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Unity Catalog Supported Objects for Tagging
description: The list of Unity Catalog object types that support the certification status system tag, including catalogs, schemas, tables, views, volumes, functions, registered models, dashboards, Genie Spaces, Databricks Apps, and notebooks.
tags:
  - unity-catalog
  - data-governance
timestamp: "2026-06-19T18:52:49.645Z"
---

# Unity Catalog Supported Objects for Tagging

**Unity Catalog Supported Objects for Tagging** refers to the set of securable object types in [Unity Catalog](/concepts/unity-catalog.md) that can be labeled with system-governed tags such as `system.certification_status`. Tagging improves data governance, discoverability, and trust by allowing organizations to mark assets with quality or lifecycle indicators. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types

The following Unity Catalog objects support the `system.certification_status` system tag, which can assign **certified** or **deprecated** status:

- [Catalogs](/concepts/unity-catalog.md)
- Schemas
- Tables
- Views
- [Volumes](/concepts/ucvolumedataset.md)
- Functions
- [Registered models](/concepts/functions-and-registered-models.md)
- Dashboards
- [Genie Spaces](/concepts/genie-space-snapshot.md)
- Databricks Apps
- Notebooks

^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

These objects appear in the workspace and can be filtered by certification status from the search page using the `certificationStatus` keyword (except for dashboards, Genie Spaces, and Databricks apps, which are not supported in search via tags). ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Permissions Required

To add tags to Unity Catalog securable objects, you must either own the object or have **all** of the following privileges:

- `APPLY TAG` on the object
- `USE SCHEMA` on the object’s parent schema
- `USE CATALOG` on the object’s parent catalog

Additionally, to assign a governed tag like `system.certification_status`, you need the `ASSIGN` permission on that specific governed tag. See [Manage permissions on governed tags](/concepts/permissions-for-governed-tags.md). ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [System Tags](/concepts/system-tags.md) – Governed tags provided by Databricks for governance purposes.
- [Certification Status System Tag](/concepts/certification-status-system-tag.md) – The specific tag with values `certified` and `deprecated`.
- [Governed Tags](/concepts/governed-tags.md) – Tags whose usage is controlled by administrative permissions.
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) – The full list of objects that can be managed in Unity Catalog.
- Data governance – Practices that tagging supports, such as quality labeling and lifecycle management.

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
