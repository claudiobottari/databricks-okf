---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fbd2c272675e9868eb07f3d8e78751076504c9b274ac0ffb0970e2b05a858c04
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-object-types-for-unity-catalog-certification-tags
    - SOTFUCCT
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Supported Object Types for Unity Catalog Certification Tags
description: The list of Unity Catalog objects that support the certification status tag, including catalogs, schemas, tables, views, volumes, functions, registered models, dashboards, Genie Spaces, apps, and notebooks.
tags:
  - unity-catalog
  - data-assets
  - tagging
timestamp: "2026-06-19T10:36:23.640Z"
---

# Supported Object Types for Unity Catalog Certification Tags

**Supported Object Types for Unity Catalog Certification Tags** refers to the specific Unity Catalog objects that can be assigned a `system.certification_status` tag with values of `certified` or `deprecated` to indicate data quality or lifecycle status. This governed tag helps organizations enforce governance, improve data discoverability, and increase trust in analytics and AI applications.^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Overview

The certification status system tag is a system-governed tag with two possible values: `certified` (displays a check mark in the workspace) and `deprecated` (displays a restricted icon). The tag appears next to object names in the workspace and influences how data appears in notebooks and the SQL editor.^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Objects

You can apply the certification status tag to the following object types in Unity Catalog:^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

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

## Unsupported Operations

Search using tags is not supported on dashboards, Genie Spaces, or Databricks apps. However, you can still assign certification status to these objects.^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) – The system for managing tags like `system.certification_status`
- Unity Catalog Objects – The full hierarchy of securable objects in Unity Catalog
- Data Governance – Organizational policies for data quality and lifecycle management
- [Certification Status System Tag](/concepts/certification-status-system-tag.md) – The governed tag with `certified` and `deprecated` values
- [Manage Permissions on Governed Tags](/concepts/permissions-for-governed-tags.md) – How to assign the `ASSIGN` permission

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
