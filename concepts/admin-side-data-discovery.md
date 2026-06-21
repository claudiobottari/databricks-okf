---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 512409d2f0eefc21eae5244a427099db9225068359c4996773249532b8a1b839
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - admin-side-data-discovery
    - ADD
    - Sensitive Data Discovery
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Admin-Side Data Discovery
description: Administrator tools and configurations in Unity Catalog that shape data discoverability through metadata, trust signals, and organization, directly determining the quality of the user discovery experience.
tags:
  - data-governance
  - administration
  - discovery
timestamp: "2026-06-19T18:04:21.399Z"
---

# Admin-Side Data Discovery

**Admin-Side Data Discovery** refers to the set of administrative capabilities in [Unity Catalog](/concepts/unity-catalog.md) that shape how users across an organization find, understand, and trust data assets. While users experience data discovery through browsing and searching the catalog, administrators define the metadata, trust signals, and organizational structure that make discovery effective. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Overview

Data discovery is the ability for users across your organization to find, understand, and trust data assets in the catalog. As an administrator, you shape discoverability through the metadata, trust signals, and organization you apply, making it easier for users to locate the right data and assess its quality before using it. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

The quality of admin-side metadata directly determines how useful the discovery experience is for users. When administrators establish consistent certification standards and governed tag vocabularies, users can filter and search for data assets with confidence. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Key Administrative Capabilities

### Flag Certified and Deprecated Data

Administrators can apply system tags to mark data assets as certified (trusted, meeting quality standards) or deprecated (outdated, unsuitable for new use). These signals appear inline in the workspace and influence how data surfaces in search results. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

For more details, see [Certify and Deprecate Data](/concepts/certified-and-deprecated-data-flags.md).

### Governed Tags

Administrators can create controlled tag vocabularies that users can apply to catalog objects to organize and categorize data by topic, team, or domain. Governed tags make data browseable and filterable across the catalog, enabling users to navigate data assets by consistent, predefined categories. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

For more details, see [Governed Tags](/concepts/governed-tags.md).

## User-Facing Discovery

The admin-side features described on this page complement the user-facing experience of browsing and searching the catalog. Users interact with the metadata and signals that administrators configure to discover the data they need. For the user-facing experience, see Discover Data. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Best Practices

- **Establish consistent certification standards** to build user trust in data quality.
- **Develop a governed tag vocabulary** that reflects your organization's domains, teams, and data categories.
- **Regularly review and update deprecated data flags** to prevent users from relying on outdated assets.
- **Combine certification and tagging** to provide both quality signals and organizational context for data assets.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The underlying catalog system for data governance
- Data Governance — Broader framework for managing data assets
- Metadata Management — Practices for maintaining high-quality metadata
- Data Quality — Standards for assessing data trustworthiness

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
