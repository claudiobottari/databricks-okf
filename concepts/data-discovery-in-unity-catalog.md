---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c193b386d688df8e9743636f18cf1d67c86b2b4b5d34f469a8d3f5ba10a41911
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-discovery-in-unity-catalog
    - DDIUC
    - Data Discovery
    - Data discovery
    - data discoverability
    - data discovery
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Data Discovery in Unity Catalog
description: The capability for users across an organization to find, understand, and trust data assets in Databricks Unity Catalog, shaped by administrator-defined metadata, trust signals, and organization.
tags:
  - data-governance
  - unity-catalog
  - discovery
timestamp: "2026-06-19T18:04:20.082Z"
---

```yaml
---
title: Data Discovery in Unity Catalog
summary: The practice and tooling that enables users across an organization to find, understand, and trust data assets within Databricks' Unity Catalog.
sources:
  - data-discovery-in-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:40:50.504Z"
updatedAt: "2026-06-19T14:40:50.504Z"
tags:
  - data-governance
  - unity-catalog
  - data-discovery
aliases:
  - data-discovery-in-unity-catalog
  - DDIUC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Data Discovery in Unity Catalog

**Data discovery** in [[Unity Catalog]] is the ability for users across an organization to find, understand, and trust data assets in the catalog. As an administrator, you shape discoverability through the metadata, trust signals, and organization you apply, making it easier for users to locate the right data and assess its quality before using it. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

> **Note:** This page covers admin-side data discovery features. For the user-facing experience of browsing and searching the catalog, see Discover data. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

The quality of admin-side metadata directly determines how useful the discovery experience is for users. When you establish consistent certification standards and governed tag vocabularies, users can filter and search for data assets with confidence. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Manage data discoverability

Administrators can manage discoverability through two primary mechanisms: certification/deprecation signals and governed tag vocabularies. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

### Flag certified and deprecated data

Use [[system tags]] to mark data assets as **certified** (trusted, meeting quality standards) or **deprecated** (outdated, unsuitable for new use). These signals appear inline in the workspace and influence how data surfaces in search. See [Flag certified and deprecated data](https://docs.databricks.com/aws/en/data-governance/unity-catalog/certify-deprecate-data). ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

### Governed tags

Create controlled [[governed tags]] vocabularies that users can apply to catalog objects to organize and categorize data by topic, team, or domain. Governed tags make data browsable and filterable across the catalog. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [[Unity Catalog]] — The data governance platform that provides data discovery features.
- [[system tags]] — Predefined tags used to mark certification and deprecation status.
- [[governed tags]] — Custom tag vocabularies for organizing and categorizing data assets.
- certify data — Marking data assets as trusted and meeting quality standards.
- [[Data Deprecation|deprecate data]] — Marking data assets as outdated and unsuitable for new use.
- Discover data — The user-facing experience for browsing and searching the catalog.

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md
```

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
