---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b083575a08ba1991812ad8c2b7d079f12253398e6c956c66a48970a5c1dec6e0
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - administrators-role-in-data-discoverability
    - ARIDD
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Administrator's Role in Data Discoverability
description: Administrators shape discoverability by applying metadata, trust signals, and organization to make it easier for users to locate and assess data quality.
tags:
  - data-governance
  - administration
  - unity-catalog
timestamp: "2026-06-19T14:40:36.029Z"
---

# Administrator's Role in Data Discoverability

**Data discoverability** is the ability for users across an organization to find, understand, and trust data assets in the catalog. As an administrator, you shape discoverability through the metadata, trust signals, and organization you apply, making it easier for users to locate the right data and assess its quality before using it. The quality of admin-side metadata directly determines how useful the discovery experience is for users. When you establish consistent certification standards and governed tag vocabularies, users can filter and search for data assets with confidence. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Manage Data Discoverability

Administrators have two primary tools for managing data discoverability in [Unity Catalog](/concepts/unity-catalog.md): certification/deprecation signals and governed tags.

### Flag Certified and Deprecated Data

Apply system tags to mark data assets as **certified** (trusted, meeting quality standards) or **deprecated** (outdated, unsuitable for new use). These signals appear inline in the workspace and influence how data surfaces in search. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

See [Certify and Deprecate Data](/concepts/certified-and-deprecated-data-flags.md) for detailed instructions.

### Governed Tags

Create controlled tag vocabularies that users can apply to catalog objects to organize and categorize data by topic, team, or domain. Governed tags make data browsable and filterable across the catalog. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

See [Governed Tags](/concepts/governed-tags.md) for implementation guidance.

## Impact on User Experience

When administrators consistently apply certification and governed tags, users benefit from:

- **Trust signals** — Certified data appears as trustworthy, deprecated data warns against reuse.
- **Browseable categorization** — Tag-based organization lets users filter by domain, team, or topic.
- **Improved search relevance** — Certified and well-tagged assets surface more prominently in search results.

For the user-facing experience of browsing and searching the catalog, see Discover Data.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Data Discovery](/concepts/data-discovery-in-unity-catalog.md)
- [Certify and Deprecate Data](/concepts/certified-and-deprecated-data-flags.md)
- [Governed Tags](/concepts/governed-tags.md)
- Data Governance

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
