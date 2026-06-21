---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dad20afc7bc6e98b53593bf9b3bb018c829c81f3c8634dddd2d570fc4d1455d3
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - certified-and-deprecated-data-signals
    - Deprecated Data Signals and Certified
    - CADDS
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Certified and Deprecated Data Signals
description: System tags applied by admins to mark data assets as certified (trusted, meeting quality standards) or deprecated (outdated, unsuitable for new use), influencing search and inline display.
tags:
  - data-governance
  - trust-signals
  - unity-catalog
timestamp: "2026-06-18T14:58:33.859Z"
---

# Certified and Deprecated Data Signals

**Certified and Deprecated Data Signals** are system tags in Unity Catalog that administrators apply to data assets to communicate their quality and suitability for use. These signals help users across an organization discover, trust, and appropriately use data by providing clear inline indicators of data reliability and lifecycle status.

## Overview

Data discovery depends on users being able to find, understand, and trust data assets in the catalog. As an administrator, you shape discoverability through the metadata, trust signals, and organization you apply. The quality of admin-side metadata directly determines how useful the discovery experience is for users. When you establish consistent certification standards and governed tag vocabularies, users can filter and search for data assets with confidence. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Certified Data

A **certified** signal indicates that a data asset is trusted and meets defined quality standards. Administrators apply this tag to data that has been validated, approved, or otherwise deemed reliable for use in analysis, reporting, or model training. Certified assets appear with inline indicators in the workspace and receive higher prominence in search results. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Deprecated Data

A **deprecated** signal indicates that a data asset is outdated, no longer maintained, or otherwise unsuitable for new use cases. Administrators apply this tag to data that should be avoided in new work, though it may remain available for backward compatibility or historical reference. Deprecated assets appear with inline warnings in the workspace and are deprioritized in search results. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## How Signals Work

Both certified and deprecated signals are implemented as system tags in Unity Catalog. They appear inline in the workspace and influence how data surfaces in search, making it easier for users to quickly assess data quality and suitability before using it. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Discovery in Unity Catalog](/concepts/data-discovery-in-unity-catalog.md) — The broader framework for helping users find and trust data.
- [Governed Tags](/concepts/governed-tags.md) — Controlled tag vocabularies for organizing and categorizing catalog objects.
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying catalog system that supports these signals.
- Data Quality Management — Processes for establishing certification standards.

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
