---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8fbbcd76d5d1ebaefa779a0bb7cf4c04ac85a9875f47210e08585588328367a2
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - governed-tag-databricks
    - GT(
    - governed-tags-databricks
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Governed Tag (Databricks)
description: A tag type in Databricks Unity Catalog used for governing and classifying sensitive data, with permissions, allowed values, and integration with ABAC column-level masks.
tags:
  - data-governance
  - unity-catalog
  - tags
timestamp: "2026-06-19T18:03:00.231Z"
---

# Governed Tag (Databricks)

A **Governed Tag** in Databricks is a managed metadata label used within [Unity Catalog](/concepts/unity-catalog.md) to classify sensitive data and enforce [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies. Governed tags are defined and administered at the [Metastore](/concepts/metastore.md) level and can have a set of allowed values that restrict which values can be assigned. ^[custom-classifiers-databricks-on-aws.md]

## Usage in Custom Classifiers

Governed tags serve as the target classification for [Custom Classifiers](/concepts/custom-classifiers.md). When creating a custom classifier, you select an existing governed tag (and optionally a specific allowed value) that the classifier should auto-detect and apply to matching columns. You can also create a new governed tag inline during the classifier creation workflow. ^[custom-classifiers-databricks-on-aws.md]

Once a custom classifier is created, the governed tag and tag value it uses **cannot be changed**. To switch to a different tag, you must delete the custom classifier and create a new one. If the governed tag or its value becomes invalid, the classifier is suspended and you must delete and recreate it with a valid tag. ^[custom-classifiers-databricks-on-aws.md]

## Permissions

To create or edit a custom classifier that uses a governed tag, you must be a [Metastore](/concepts/metastore.md) admin and hold the `ASSIGN` privilege on the governing tag. This ensures that only authorized users can associate a classifier with a given tag. ^[custom-classifiers-databricks-on-aws.md]

## Tag Policy

All governed tags are subject to **Tag Policy rules**, which govern naming conventions, allowed values, and other constraints. These rules are enforced when creating or modifying tags, either directly or through a custom classifier. ^[custom-classifiers-databricks-on-aws.md]

## Limitations

- A governed tag referenced by a custom classifier cannot be altered after the classifier is created; if the tag needs to change, the classifier must be deleted and recreated. ^[custom-classifiers-databricks-on-aws.md]
- Governed tags are metastore-wide resources; they are not scoped per catalog or schema. ^[custom-classifiers-databricks-on-aws.md]

## Related Concepts

- [Custom Classifiers](/concepts/custom-classifiers.md)
- [Data Classification](/concepts/data-classification.md)
- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md)
- Tag Policy rules
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- `custom-classifiers-databricks-on-aws.md`

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
