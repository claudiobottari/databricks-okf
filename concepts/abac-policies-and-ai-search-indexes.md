---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b45e556c439aab08ad4f06823611ae474c2e5578891a7a7cb4cfc917f806713
  pageDirectory: concepts
  sources:
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policies-and-ai-search-indexes
    - AI Search Indexes and ABAC Policies
    - APAASI
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Policies and AI Search Indexes
description: AI Search indexes created from ABAC-secured tables do not enforce row filter or column mask policies when serving queries
tags:
  - access-control
  - unity-catalog
  - ai-search
  - databricks
timestamp: "2026-06-19T20:13:56.537Z"
---

# ABAC Policies and AI Search Indexes

**ABAC Policies and AI Search Indexes** describes the interaction between attribute-based access control ([ABAC Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)) and Databricks AI Search indexes. A key limitation is that ABAC policies defined on a source table are **not enforced** when data is served through an AI Search index created from that table.

## Overview

When an AI Search index is built from a table that has ABAC row filters or column masks, the index syncs **all rows** from the source table and serves query results without applying the ABAC policies. This means that any user querying the index sees data that would otherwise be filtered or masked if queried directly against the table. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Details

- **Row filters:** ABAC row filters are ignored by AI Search indexes. All rows from the source table are indexed and returned in search results. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Column masks:** ABAC column masks are also not enforced when serving queries from the index. However, there is a mitigation available: you can exclude masked columns from the index using the **columns to sync** setting when creating the AI Search index. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Mitigation

For tables with column masks, a system administrator can choose **not to include** the masked columns in the AI Search index. This prevents the masked data from being exposed through the index. There is no equivalent mitigation for row filters — if a table has ABAC row filters, the index will still contain all rows. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — The core access control policies that do not propagate to indexes.
- Databricks AI Search — The indexing and search service affected by this limitation.
- Columns to Sync — The index configuration setting that can exclude columns from being indexed.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages ABAC policies.

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)
