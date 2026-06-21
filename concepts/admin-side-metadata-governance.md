---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b193f4d1450021eb6571909c8dddeb825871667b5fbc3ff55bc83db98cb77fe
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - admin-side-metadata-governance
    - AMG
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Admin-side Metadata Governance
description: Administrators shape data discoverability by applying metadata, trust signals, and organizational structures to catalog objects.
tags:
  - data-governance
  - administration
  - metadata
timestamp: "2026-06-18T11:28:15.310Z"
---

# Admin-side Metadata Governance

**Admin-side Metadata Governance** refers to the set of tools and practices that administrators use to shape how data assets are discovered, understood, and trusted across an organization in [Unity Catalog](/concepts/unity-catalog.md). The quality of admin-side metadata directly determines the usefulness of the discovery experience for end users. When administrators establish consistent certification standards and governed tag vocabularies, users can filter and search for data assets with confidence. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Core Components

### Certification and Deprecation Signals

Administrators can apply [System Tags](/concepts/system-tags.md) to mark data assets as **certified** (trusted, meeting quality standards) or **deprecated** (outdated, unsuitable for new use). These signals appear inline in the workspace and influence how data surfaces in search results. Certification helps users identify authoritative data sources, while deprecation flags guide users away from obsolete assets. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

### Governed Tag Vocabularies

[Governed Tags](/concepts/governed-tags.md) are controlled tag vocabularies that administrators create for users to apply to catalog objects. These tags organize and categorize data by topic, team, or domain. Governed tags make data browsable and filterable across the catalog, enabling users to narrow their search to relevant subsets of data. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Relationship to Access Control

Admin-side metadata governance works in concert with [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md). While metadata governance focuses on discoverability and trust signals, ABAC policies control who can access specific assets. Governed tags serve both purposes: they organize data for discovery and drive ABAC policy evaluation for access control.

## Discovery Experience

The admin-side metadata features described on this page shape the user-facing discovery experience. When administrators curate metadata effectively, users can:

- Find data assets more quickly through filtered search
- Assess data quality before using it through certification signals
- Navigate the catalog by domain or topic using governed tags

For the user-facing experience of browsing and searching the catalog, see Discover data. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Best Practices

- **Establish consistent certification standards** so users can trust the certified and deprecated signals.
- **Create governed tag vocabularies** before users begin tagging, rather than applying tags ad hoc.
- **Document the tagging taxonomy** and governance model so teams understand expected tag usage patterns.
- **Audit tag changes regularly** to detect unauthorized modifications, as tags are a security boundary in ABAC policies. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that provides metadata management
- [Governed Tags](/concepts/governed-tags.md) — Controlled vocabularies for organizing catalog objects
- [Data Classification](/concepts/data-classification.md) — Automatic detection and tagging of sensitive columns
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Access control driven by tags and metadata
- [ABAC Policies from Data Classification](/concepts/abac-policies-from-data-classification.md) — Creating access policies based on classification results
- [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) — Tracking tag and policy changes for compliance

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
2. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
