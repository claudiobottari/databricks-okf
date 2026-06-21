---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f726eece1ac9a1c0fbbe540ffd543403b83c33605baf5b746446b9c327116dad
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - search-by-certification-status
    - SBCS
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Search by Certification Status
description: A search capability in Databricks that allows users to filter and query Unity Catalog objects by their certification status using the certificationStatus keyword or filter menu.
tags:
  - search
  - data-discovery
  - unity-catalog
timestamp: "2026-06-19T18:52:34.706Z"
---

# Search by Certification Status

**Search by Certification Status** allows users to filter [Unity Catalog](/concepts/unity-catalog.md) assets by their [certification status](/concepts/certification-status-system-tag.md) system tag (`certified` or `deprecated`) directly from the Databricks workspace search interface. This helps quickly locate trusted or deprecated data assets across catalogs, schemas, tables, views, volumes, functions, registered models, and notebooks. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## How to Search

You can filter by certification status using either the search bar or the filter menu.

### Using the Search Bar

In the **Search** field, use the `certificationStatus` keyword to narrow results. For example:

- `type:table certificationStatus:certified` returns only certified tables.
- `certificationStatus:deprecated` returns only deprecated assets across all supported object types.

^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

### Using the Filter Menu

In the search filters, select **Certified** or **Deprecated** from the **Certification status** filter menu. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Limitations

- Search by tags (including certification status) is **not supported** on dashboards, Genie Spaces, or Databricks apps. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]
- It may take a few minutes for certification or deprecation updates to appear in search results. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [Certification Status System Tag](/concepts/certification-status-system-tag.md) — The `system.certification_status` tag with values `certified` and `deprecated`
- [Governed Tags](/concepts/governed-tags.md) — Tags managed by Unity Catalog governance, including system tags
- Data Governance — Policies and practices for managing data quality and trust

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
