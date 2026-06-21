---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7460692253e1e8a79c035fa2d430e7dac991dd43a0b407eb9b0fb2fbad4890ae
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
    - what-is-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - data-lineage-in-unity-catalog
    - DLIUC
    - Lineage in Unity Catalog
    - Track data lineage of a model in Unity Catalog
  citations:
    - file: get-started-with-unity-catalog-databricks-on-aws.md
    - file: what-is-unity-catalog-databricks-on-aws.md
title: Data Lineage in Unity Catalog
description: Automatic capture of data flow across tables, notebooks, jobs, and pipelines at the column level for tracing origins and impact analysis
tags:
  - data-lineage
  - observability
  - impact-analysis
timestamp: "2026-06-19T10:45:54.958Z"
---

# Data Lineage in Unity Catalog

**Data Lineage in Unity Catalog** automatically captures how data flows across tables, notebooks, jobs, and pipelines — down to the column level. You can trace the origin of any column, see what downstream assets depend on it, and understand the full impact of a schema change before making it. ^[get-started-with-unity-catalog-databricks-on-aws.md]

Unity Catalog also enables you to track how data transforms from source to final views and dashboards, providing a complete picture of data movement within your workspace. ^[what-is-unity-catalog-databricks-on-aws.md]

Data lineage is one of the built-in governance capabilities of [Unity Catalog](/concepts/unity-catalog.md), which is automatically enabled for workspaces created after November 8, 2023. Lineage data is available through [Catalog Explorer](/concepts/catalog-explorer.md) and can be used for impact analysis, root‑cause investigation, and compliance auditing. ^[get-started-with-unity-catalog-databricks-on-aws.md, what-is-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog object model](/concepts/unity-catalog-ai-asset-model.md) – The securable objects that lineage tracks.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI for viewing lineage graphs.
- [Data Classification](/concepts/data-classification.md) – Automatically tag sensitive data, complementing lineage.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Proactive health checks on data tracked by lineage.

## Sources

- get-started-with-unity-catalog-databricks-on-aws.md
- what-is-unity-catalog-databricks-on-aws.md

# Citations

1. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)
2. [what-is-unity-catalog-databricks-on-aws.md](/references/what-is-unity-catalog-databricks-on-aws-ea58b0e9.md)
