---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7eabb9810aa163c3212ebd1db10241606241f30fbc4ba1b3bfe53b003d58c1fe
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-lineage
    - Lineage
    - lineage
  citations:
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Data Lineage
description: Automatic column-level tracking of how data flows across tables, notebooks, jobs, and pipelines, enabling impact analysis and origin tracing.
tags:
  - data-governance
  - lineage
  - observability
timestamp: "2026-06-19T19:01:22.173Z"
---

# Data Lineage

**Data Lineage** is a capability within [Unity Catalog](/concepts/unity-catalog.md) that automatically captures the flow of data across tables, notebooks, jobs, and pipelines, down to the column level. It is part of Databricks’ unified governance layer for data and AI. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Capabilities

Data lineage provides detailed visibility into how data assets are connected. Users can:

- **Trace the origin of any column** – identify which upstream tables, notebooks, or jobs produced a given column.
- **See downstream dependencies** – find all assets that depend on a specific column or table, such as downstream dashboards, models, or reports.
- **Understand the impact of a schema change before making it** – assess how renaming, dropping, or altering a column will affect downstream systems enabling safer schema modifications.

All of this tracking is performed automatically by Unity Catalog without requiring manual instrumentation. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Scope

Lineage is captured for a variety of asset types in the Databricks environment:

| Asset Type | Description |
|------------|-------------|
| Tables | Lineage between source and target tables, including views and materialized views. |
| Notebooks | Data flow into and out of notebook cells. |
| Jobs | Dependencies introduced by scheduled or triggered jobs. |
| Pipelines | Lineage through Delta Live Tables pipelines and other ETL processes. |

Lineage is recorded at the **column level**, meaning you can see exactly which columns in a source table flow to which columns in a downstream table. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Integration with Governance

Data lineage is one of the extended governance capabilities built on top of the core Unity Catalog setup. It complements other features such as [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md), [Data Classification](/concepts/data-classification.md), and [Data Quality Monitoring](/concepts/data-quality-monitoring.md). Together, these tools give data teams full observability into who has access to what data, how the data is classified, how its quality changes over time, and how it moves through the environment. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The unified governance layer that provides data lineage.
- [Column-Level Lineage](/concepts/column-level-lineage.md) – The specific granularity at which lineage is tracked.
- Data governance – The overarching discipline of managing data assets.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI where lineage can be visualized.
- Impact analysis – The practice of evaluating the effect of schema changes using lineage.

## Sources

- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)
