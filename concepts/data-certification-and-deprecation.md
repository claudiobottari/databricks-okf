---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 13a0d92e028f8f8b95e70372f077e223bfd89e7f7fcd95411dbbe433b2ea507f
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-certification-and-deprecation
    - Deprecation and Data Certification
    - DCAD
    - Certification and Deprecation
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Data Certification and Deprecation
description: A system in Unity Catalog that allows administrators to flag data assets as certified (trusted, meeting quality standards) or deprecated (outdated, unsuitable for new use), with signals appearing in the workspace and influencing search results.
tags:
  - data-governance
  - data-quality
  - trust-signals
timestamp: "2026-06-19T18:04:26.006Z"
---

# Data Certification and Deprecation

**Data Certification and Deprecation** is an admin-side data discovery feature in [Unity Catalog](/concepts/unity-catalog.md) that allows administrators to mark data assets with trust signals using **system tags**. These signals help users across the organization quickly identify which datasets are reliable and which are outdated, improving the overall discoverability experience. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Mechanism

Administrators apply system tags to catalog objects to indicate one of two states:

- **Certified** – The data asset is trusted and meets organizational quality standards. It is suitable for use in new projects and analyses.
- **Deprecated** – The data asset is outdated or no longer maintained and should not be used for new work.

These tags are applied through the Unity Catalog interface. Once set, the certification or deprecation status appears inline in the workspace (e.g., in the catalog browser, notebooks, and dashboards) and influences how the asset surfaces in search results. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

Certification and deprecation are part of a broader set of metadata management tools that also include [Governed Tags](/concepts/governed-tags.md), which provide controlled vocabularies for organizing data by topic, team, or domain. Together, these features give administrators fine‑grained control over data discoverability. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Discovery in Unity Catalog](/concepts/data-discovery-in-unity-catalog.md) – The overall framework for helping users find, understand, and trust data.
- [Governed Tags](/concepts/governed-tags.md) – Controlled vocabularies that complement certification and deprecation by adding organizational context.
- [Unity Catalog](/concepts/unity-catalog.md) – The underlying catalog system that hosts these metadata features.

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
