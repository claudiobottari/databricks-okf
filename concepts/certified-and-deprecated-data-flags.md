---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3cd15af16fc8dbfbaefc430377be9cafda89ae0994b57d9e5a9de8d204cb2e4b
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - certified-and-deprecated-data-flags
    - Deprecated Data Flags and Certified
    - CADDF
    - Certified and Deprecated Data
    - Flag certified and deprecated data
    - Certify and Deprecate Data
    - Certify and deprecate data
    - Flag data as certified or deprecated
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Certified and Deprecated Data Flags
description: System tags that mark data assets as certified (trusted, meeting quality standards) or deprecated (outdated, unsuitable for new use), influencing search and inline display.
tags:
  - data-governance
  - trust-signals
  - metadata
timestamp: "2026-06-19T14:40:49.439Z"
---



# Certified and Deprecated Data Flags

**Certified and Deprecated Data Flags** are [System Tags](/concepts/system-tags.md) in [Unity Catalog](/concepts/unity-catalog.md) that allow data administrators to signal the trustworthiness and lifecycle status of data assets. These flags function as **metadata trust signals** that appear inline in the Databricks workspace and influence how data surfaces in search results, helping users quickly identify high-quality, reliable data and avoid outdated or unsuitable assets.^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Overview

Data discovery depends on users being able to find, understand, and trust data assets. As an administrator, you shape discoverability through the metadata, trust signals, and organization you apply. Certified and deprecated flags are the primary trust signals you can apply:^[data-discovery-in-unity-catalog-databricks-on-aws.md]

- **Certified** — marks a data asset as trusted and meeting quality standards. Certified assets are promoted in search results.
- **Deprecated** — marks a data asset as outdated or otherwise unsuitable for new use. Deprecated assets are demoted in search results.

The quality of admin-side metadata directly determines how useful the discovery experience is for users. When you establish consistent certification standards and governed tag vocabularies, users can filter and search for data assets with confidence.^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## When to Set Flags

Set the **certified** flag on data assets that have been validated against quality criteria — for example, tables that pass data quality checks, have complete documentation, or are approved for use by a data governance team. Set the **deprecated** flag on data that is no longer maintained, has been superseded by a newer version, or should not be used for new projects.^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## How Flags Appear

When applied, these flags appear directly in the workspace UI on the relevant data asset:^[data-discovery-in-unity-catalog-databricks-on-aws.md]

- **Certified** — appears as **CERTIFIED** with a green checkmark badge.
- **Deprecated** — appears as **DEPRECATED** with a yellow warning badge.

Both flags also influence the asset's ranking in search results: certified assets are boosted, deprecated assets are demoted. This makes it easier for users to find trusted data and avoid outdated or low-quality sources before they invest time in analysis.^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data discovery](/concepts/data-discovery-in-unity-catalog.md) — The broader practice of making data findable and understandable across an organization.
- [Governed Tags](/concepts/governed-tags.md) — Controlled tag vocabularies that organize data by topic, team, or domain.
- Browse and search the catalog — The user-facing experience of discovering data assets.
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying catalog that stores and manages data assets.

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
