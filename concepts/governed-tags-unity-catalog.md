---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6545c0a8639e1b738569e54145c75783d7b2606bcfa16c50a7d932eee7c808b
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tags-unity-catalog
    - GT(C
    - governed tags documentation
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Governed Tags (Unity Catalog)
description: Controlled, administrator-defined tag vocabularies that users can apply to catalog objects to organize and categorize data by topic, team, or domain.
tags:
  - data-governance
  - unity-catalog
  - metadata-management
timestamp: "2026-06-19T09:41:19.795Z"
---

Here is the wiki page for "Governed Tags (Unity Catalog)".

---

## Governed Tags (Unity Catalog)

**Governed Tags** are a feature in [Unity Catalog](/concepts/unity-catalog.md) that allows administrators to create controlled vocabularies of tags and apply them to catalog objects (such as catalogs, schemas, tables, columns, and models). By establishing consistent, curated labels, governed tags make data assets more discoverable, filterable, and searchable across the organization. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Purpose

Data discovery — the ability for users to find, understand, and trust data assets — depends on the quality of the metadata attached to catalog objects. Governed tags provide a structured way to organize and categorize data by topic, team, domain, or any other classification the organization defines. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

As an administrator, you shape discoverability through the metadata, trust signals, and organization you apply. When you establish consistent governed tag vocabularies, users can filter and search for data assets with confidence. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## How Governed Tags Work

- **Controlled vocabulary:** Administrators define the set of allowed tags and their values. Users can only apply tags from this curated list, ensuring consistency across the catalog.
- **Scope:** Tags can be applied to catalog objects including catalogs, schemas, tables, columns, and models.
- **Inheritance:** Tags on parent objects (catalogs, schemas, tables) are inherited by child objects (except columns). This allows you to tag a schema with a domain label and have all tables within that schema inherit the tag automatically.
- **Filtering and search:** Governed tags make data browseable and filterable, allowing users to locate assets by the categories that matter to them.

## Related Tag Types

While governed tags are used for organization and discovery, other tag types serve different purposes:

- **System tags** such as `certified` and `deprecated` are used to mark trust signals. Certified tags indicate data that meets quality standards; deprecated tags indicate outdated data unsuitable for new use. These signals appear inline in the workspace and influence search rankings.

## Use Cases

- **Organizing by domain:** Apply tags like `domain: finance`, `domain: marketing`, or `domain: engineering` to schemas so users can browse by business area.
- **Classifying sensitivity:** Apply tags like `pii: ssn`, `pii: email`, or `classification: internal` to columns to indicate data sensitivity. (Note: Tagged columns are referenced by [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) and [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) to apply dynamic access controls.)
- **Team ownership:** Tag tables with the owning team name so users know whom to contact with questions.

## Best Practices

- **Establish a governed tag vocabulary before broad adoption.** The quality of admin-side metadata directly determines how useful the discovery experience is for users. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]
- **Use governed tags in combination with [Data Certification](/concepts/data-certification.md).** Certification (via system tags) provides trust signals, while governed tags provide organization and filtering.
- **Leverage tag inheritance** by tagging at the schema or catalog level where possible, reducing the need to tag individual tables or columns manually.

## See Also

- [Data Certification and Deprecation](/concepts/data-certification-and-deprecation.md) — System tags for trust signals (certified/deprecated)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — How governed tags are used in ABAC policies for row filters and column masks
- [Data Discovery in Unity Catalog](/concepts/data-discovery-in-unity-catalog.md) — The user-facing browsing and searching experience

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
