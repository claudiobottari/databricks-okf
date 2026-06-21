---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c2be0adfe0d6e84d7110c2dc24a9e5790e252750df068ea348d372e57852923
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tags-vocabulary
    - GTV
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
    - file: data-classification-databricks-on-aws.md
title: Governed Tags Vocabulary
description: Controlled tag vocabularies that administrators create for users to organize and categorize catalog objects by topic, team, or domain, making data browseable and filterable.
tags:
  - data-governance
  - tagging
  - organization
timestamp: "2026-06-18T11:27:53.051Z"
---

# Governed Tags Vocabulary

A **governed tags vocabulary** is a controlled set of tags that administrators define in Unity Catalog to organize and categorize data assets by topic, team, or domain. Governed tags are discoverable metadata keys (with possible values) that users can apply to catalog objects, making data browseable and filterable across the catalog.^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Purpose

Governed tags vocabularies serve two primary functions:

- **Discovery**: Users can find data by filtering on tags (e.g., `department = "finance"`), improving the search experience in the workspace.
- **Governance**: Tags become the foundation for attribute-based access control (ABAC) policies, such as row filters, column masks, and [GRANT policies](/concepts/abac-grant-policy.md). When a tag is applied to a securable object, any ABAC policy referencing that tag automatically applies to that object.

## Relationship to Governed Tags

A governed tag is a specific key-value pair that belongs to a governed tags vocabulary. The vocabulary defines which keys and values are permissible; administrators create and manage the vocabulary to ensure consistency. Users can then assign governed tags from the approved vocabulary to catalog objects such as schemas, tables, columns, models, and notebooks.^[data-discovery-in-unity-catalog-databricks-on-aws.md]

Governed tags are distinct from unstructured user-defined tags: only tags from the official vocabulary are eligible for ABAC policy evaluation.^[abac-grant-policies-for-models-beta-databricks-on-aws.md, best-practices-for-abac-policies-databricks-on-aws.md]

## Usage in Access Control

ABAC policies in Unity Catalog use governed tags as condition expressions. For example, a column mask policy can match a column that carries a specific classification tag (e.g., `class.email_address`), and a GRANT policy can grant `EXECUTE` on models whose tags match a certain condition. Because the tag vocabulary is centrally managed, administrators can control which tags are available for security decisions.^[abac-grant-policies-for-models-beta-databricks-on-aws.md, data-classification-databricks-on-aws.md]

## Best Practices

- **Define tags before scaling ABAC policies.** Create a governed tags vocabulary first, then author policies that reference those tags. This prevents drift between tag usage and policy conditions.
- **Document the taxonomy.** Maintain a written description of each tag’s meaning and intended use so that data stewards apply them consistently.
- **Restrict tag creation.** Limit the ability to create or modify governed tags to governance administrators. Users should only be able to apply tags from the approved vocabulary.
- **Audit tag assignments.** Monitor `createEntityTagAssignment` and `deleteEntityTagAssignment` events in the audit log to detect unauthorized tag changes that could affect security boundaries.^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The key-value pairs that belong to a controlled vocabulary
- [Data Classification in Unity Catalog](/concepts/data-classification-in-unity-catalog.md) — Automatic tag assignment for sensitive data
- ABAC Policies — Access control policies driven by governed tags
- Certified and Deprecated Data — System tags for data quality signals
- Discover Data — The user-facing catalog browsing experience

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md
- data-classification-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
3. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
4. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
