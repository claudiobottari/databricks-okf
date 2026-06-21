---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad15eb898f11b06eee8efa94bd3bb0b02286f1c6cf703964cf40495dbf61ba3a
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - certified-data-unity-catalog
    - CD(C
    - Certified data
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Certified Data (Unity Catalog)
description: System tags applied to data assets to mark them as trusted and meeting quality standards in Unity Catalog.
tags:
  - data-governance
  - unity-catalog
  - data-quality
timestamp: "2026-06-19T09:41:15.032Z"
---

# Certified Data (Unity Catalog)

**Certified Data** refers to data assets in Unity Catalog that an administrator has explicitly marked as trusted, meaning they meet defined quality standards and are suitable for production use. When administrators certify data, they provide a strong signal to downstream users that the asset is reliable and appropriate for consumption.

## Overview

Data certification is a data discovery feature in Unity Catalog that helps users find, understand, and trust data assets across the organization. By marking specific tables or other catalog objects as certified, administrators create trust signals that influence how data surfaces in search results and appear inline in the workspace. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

The quality of admin-side metadata — including certification — directly determines how useful the discovery experience is for users. When administrators establish consistent certification standards and governed tag vocabularies, users can filter and search for data assets with confidence. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## How Certification Works

Administrators apply system tags to mark data assets as certified. These certification signals serve two purposes:

- They appear **inline in the workspace**, giving users immediate visual feedback about data quality when browsing.
- They **influence search ranking**, helping certified datasets surface more prominently when users search for data. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Related Concepts: Deprecated Data

Certified data is often contrasted with [Deprecated Data (Unity Catalog)](/concepts/deprecated-data-unity-catalog.md), which is marked as outdated and unsuitable for new use cases. Administrators can also apply system tags to deprecate data assets, providing the opposite signal to users. Both certification and deprecation use the same system tag mechanism and both influence discoverability. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Benefits

- **Trust**: Users can quickly identify which datasets are approved for use without needing to verify quality independently.
- **Discoverability**: Certified data surfaces more prominently in search, reducing the time users spend finding reliable datasets.
- **Governance**: Certification standards provide a consistent framework for data quality across the organization.

## See Also

- [Data Discovery in Unity Catalog](/concepts/data-discovery-in-unity-catalog.md) — The broader admin-side features for making data findable.
- [Deprecated Data (Unity Catalog)](/concepts/deprecated-data-unity-catalog.md) — The complementary mechanism for marking unsuitable data.
- [Governed Tags](/concepts/governed-tags.md) — Controlled tag vocabularies that organize and categorize data by topic, team, or domain.
- [System Tags](/concepts/system-tags.md) — The underlying tag mechanism used for certification and deprecation signals.

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
