---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2592d77b010a3c5ce64f058e1cfaac56870c9d96f6141afa4731f6f65273bfd
  pageDirectory: concepts
  sources:
    - data-lineage-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-lineage
  citations:
    - file: data-lineage-in-unity-catalog-databricks-on-aws.md
title: External Lineage
description: Extension of Unity Catalog lineage beyond Databricks by registering external assets like Salesforce, MySQL, Tableau, or Power BI to appear alongside Unity Catalog tables in a single lineage graph.
tags:
  - data-governance
  - lineage
  - external-assets
timestamp: "2026-06-19T18:04:35.350Z"
---

# External Lineage

**External lineage** extends the [Unity Catalog lineage graph](/concepts/data-lineage-in-unity-catalog.md) beyond Databricks by registering upstream sources (such as Salesforce or MySQL) and downstream tools (such as Tableau or Power BI) as external assets. These external assets appear alongside Unity Catalog tables in a single, unified lineage graph, enabling end-to-end data flow visibility across the entire data ecosystem. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Overview

External lineage allows organizations to track how data moves between Databricks and external systems. By registering external metadata objects in Unity Catalog and configuring relationships with other securable objects, you can see how data flows from source systems into Databricks and from Databricks into consuming applications. This provides a complete picture of data provenance that spans both Databricks-managed and external environments. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Requirements

To use external lineage, external assets (those not registered in the Unity Catalog [Metastore](/concepts/metastore.md)) must be added as external metadata objects in Unity Catalog, configured to have relationships with other securable objects registered in your Unity Catalog [Metastore](/concepts/metastore.md). ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Viewing External Lineage

External assets appear in the same lineage graph as Unity Catalog tables when viewing lineage in Catalog Explorer. The lineage graph displays nodes representing tables and views, ML model versions, external assets, and file paths. External assets are visually distinguished from Unity Catalog-managed objects in the graph. ^[data-lineage-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — The core lineage feature that external lineage extends
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides lineage capabilities
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI for viewing lineage graphs

## Sources

- data-lineage-in-unity-catalog-databricks-on-aws.md

# Citations

1. [data-lineage-in-unity-catalog-databricks-on-aws.md](/references/data-lineage-in-unity-catalog-databricks-on-aws-84f84dd2.md)
