---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc6054fd421ba45b66e3a51a202fb1464f9c5afd06cf34448fea54e218897778
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata-quality-and-discoverability
    - Discoverability and Metadata Quality
    - MQAD
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Metadata Quality and Discoverability
description: The principle that the quality of admin-side metadata directly determines how useful the data discovery experience is for users.
tags:
  - data-governance
  - metadata-management
  - data-discovery
timestamp: "2026-06-19T09:41:23.048Z"
---

# Metadata Quality and Discoverability

**Metadata Quality and Discoverability** refers to the ability of users across an organization to find, understand, and trust data assets in a data catalog. In the context of [Unity Catalog](/concepts/unity-catalog.md), discoverability is shaped by the metadata, trust signals, and organization that administrators apply to catalog objects. The quality of this administrative metadata directly determines how useful the discovery experience is for end users. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## The Role of the Administrator

Administrators shape discoverability by establishing consistent certification standards and controlled tag vocabularies. When these practices are in place, users can filter and search for data assets with confidence, knowing that the metadata they see reflects the data’s quality and intended use. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## How Metadata Quality Impacts Discovery

The quality of admin-side metadata directly determines how useful the discovery experience is for users. High-quality metadata makes data assets easier to locate and evaluate, while poor or inconsistent metadata hinders findability and trust. Two primary tools for improving metadata quality are:

### 1. Certification and Deprecation Signals

Administrators can apply system tags to mark data assets as **certified** (trusted, meeting quality standards) or **deprecated** (outdated, unsuitable for new use). These signals appear inline in the workspace and influence how data surfaces in search results. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

### 2. Governed Tag Vocabularies

Administrators can create controlled tag vocabularies that users apply to catalog objects to organize and categorize data by topic, team, or domain. [Governed Tags](/concepts/governed-tags.md) make data browseable and filterable across the catalog, enabling users to quickly narrow down assets that match their interests. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying data catalog where metadata and discoverability features are managed.
- [Governed Tags](/concepts/governed-tags.md) – Controlled vocabularies for organizing and filtering data assets.
- Certify Data – Applying trusted quality signals to data assets.
- [Deprecate Data](/concepts/data-deprecation.md) – Marking assets as outdated to guide users away from unsuitable data.
- [Data Discovery](/concepts/data-discovery-in-unity-catalog.md) – The user-facing experience of browsing and searching the catalog.

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
