---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33250d603fc97b63214665cfade23236315ed91a3e90c2ded7ca6bbd908799d5
  pageDirectory: concepts
  sources:
    - data-discovery-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deprecated-data-unity-catalog
    - DD(C
  citations:
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
title: Deprecated Data (Unity Catalog)
description: System tags applied to data assets to mark them as outdated or unsuitable for new use in Unity Catalog.
tags:
  - data-governance
  - unity-catalog
  - data-lifecycle
timestamp: "2026-06-19T09:41:11.422Z"
---

# Deprecated Data (Unity Catalog)

**Deprecated Data** in [Unity Catalog](/concepts/unity-catalog.md) refers to data assets that have been marked as outdated and unsuitable for new use. Administrators apply a system tag to indicate that a table, view, or other catalog object should not be relied upon for future work, though the data remains queryable for existing consumers.

## Overview

Data depreciation is a key signal in the [data discovery](/concepts/data-discovery-in-unity-catalog.md) experience. When a data asset is marked as deprecated, users can see this status inline in the workspace, and the signal influences how the asset surfaces in search results. This helps consumers avoid accidentally relying on stale or superseded data. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Marking Data as Deprecated

To mark a data asset as deprecated, an administrator applies the appropriate system tag to the catalog object. The system tag for deprecated data is one of the built-in tags provided by Unity Catalog for certification and deprecation. The process is the same as flagging certified data — the two are complementary signals. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Effects on Data Discovery

Once a data asset is tagged as deprecated:

- A deprecation indicator appears inline in the workspace UI when users browse or view the asset’s details. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]
- The asset’s ranking in search results is influenced, typically surfacing lower than active or certified assets. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]
- Users can filter or search specifically for deprecated assets if they need to locate them, but the default discoverability emphasizes non-deprecated data. ^[data-discovery-in-unity-catalog-databricks-on-aws.md]

## Best Practices

- Mark data as deprecated only when it is effectively replaced by a newer version or is no longer maintained. Avoid overusing the tag so the signal remains meaningful.
- Combine deprecation status with [Governed Tags](/concepts/governed-tags.md) and descriptions to provide consumers with clear context on why the data is deprecated and what alternative assets to use.
- Periodically review deprecated assets to decide whether to archive or remove them entirely.

## Related Concepts

- [Certified Data (Unity Catalog)](/concepts/certified-data-unity-catalog.md) – The complementary signal for trusted, high‑quality data assets.
- [System Tags](/concepts/system-tags.md) – Built‑in tags that include certification and deprecation markers.
- [Data Discovery in Unity Catalog](/concepts/data-discovery-in-unity-catalog.md) – The full admin workflow for shaping discoverability.
- [Governed Tags](/concepts/governed-tags.md) – Custom vocabularies for organizing and categorizing data.

## Sources

- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
