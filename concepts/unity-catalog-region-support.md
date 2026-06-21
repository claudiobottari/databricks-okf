---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2ba0d29912b3767e3bcfc364622e09d4bd0d35d15a7bec70944b548a647bf3b
  pageDirectory: concepts
  sources:
    - unity-catalog-requirements-and-limitations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-region-support
    - UCRS
  citations:
    - file: unity-catalog-requirements-and-limitations-databricks-on-aws.md
title: Unity Catalog Region Support
description: All regions support Unity Catalog, with further details available in Databricks' supported regions documentation.
tags:
  - unity-catalog
  - regions
  - databricks
timestamp: "2026-06-19T23:15:18.818Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) Region Support

**Unity Catalog Region Support** refers to the availability of [Unity Catalog](/concepts/unity-catalog.md) across all geographic regions where Databricks operates. [Unity Catalog](/concepts/unity-catalog.md) is fully supported in all regions where the Databricks platform is available. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Overview

[Unity Catalog](/concepts/unity-catalog.md) does not impose any region-specific restrictions on its functionality. All Databricks regions support [Unity Catalog](/concepts/unity-catalog.md), enabling organizations to deploy and use [Unity Catalog](/concepts/unity-catalog.md) regardless of their geographic location or data residency requirements. For a complete list of supported regions, see the official Databricks documentation on clouds and regions. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Regional Consistency

Because [Unity Catalog](/concepts/unity-catalog.md) support is uniform across all regions, there are no region-specific feature gaps or limitations. This means that all [Unity Catalog](/concepts/unity-catalog.md) capabilities — including [Managed Tables](/concepts/managed-tables-in-databricks.md), External Tables, Dynamic Views, and [Resource Quotas](/concepts/unity-catalog-resource-quotas.md) — are available regardless of the region where the workspace is deployed. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Multi-Region Considerations

When using [Unity Catalog](/concepts/unity-catalog.md) across workspaces in multiple regions, there is an important limitation: writing to the same path or [Delta Lake](/concepts/delta-lake.md) table from workspaces in different regions can lead to unreliable performance if some clusters access [Unity Catalog](/concepts/unity-catalog.md) and others do not. This should be considered when designing cross-region data architectures. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Related Concepts

- Unity Catalog Requirements and Limitations — Complete list of compute, format, and naming requirements
- Databricks Clouds and Regions — Official documentation on region availability
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — Catalogs, schemas, tables, and other objects managed by [Unity Catalog](/concepts/unity-catalog.md)
- [Resource Quotas](/concepts/unity-catalog-resource-quotas.md) — Usage limits enforced by [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- unity-catalog-requirements-and-limitations-databricks-on-aws.md

# Citations

1. [unity-catalog-requirements-and-limitations-databricks-on-aws.md](/references/unity-catalog-requirements-and-limitations-databricks-on-aws-0188dbe0.md)
