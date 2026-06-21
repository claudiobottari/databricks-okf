---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72562a94788575769748861e4f889681d3372f314fb26c255207aa8551515cd9
  pageDirectory: concepts
  sources:
    - external-lineage-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakeflow-connect-source-lineage
    - LCSL
  citations:
    - file: external-lineage-databricks-on-aws.md
title: Lakeflow Connect Source Lineage
description: Automatic recording of source lineage from external source tables to destination tables in Unity Catalog via managed ingestion pipelines using Lakeflow Connect.
tags:
  - ingestion
  - automation
  - lakeflow
timestamp: "2026-06-19T18:47:22.039Z"
---

# Lakeflow Connect Source Lineage

**Lakeflow Connect Source Lineage** refers to the automatic recording of source data lineage from managed ingestion pipelines created with Lakeflow Connect into [Unity Catalog](/concepts/unity-catalog.md). When you use Lakeflow Connect to ingest data from external sources into Databricks, the system automatically captures lineage from the source tables to the destination tables, providing an end-to-end view of data provenance. ^[external-lineage-databricks-on-aws.md]

## Overview

Unity Catalog automatically captures runtime data lineage across queries executed on Databricks. However, workloads that run outside Databricks (such as first-mile ETL or last-mile BI) are not captured automatically. Lakeflow Connect fills this gap by recording source lineage from external source tables to the destination tables in Unity Catalog as part of the managed ingestion pipeline. This automatic lineage recording is one of two ways to add external lineage metadata in Unity Catalog; the other is manual using the Catalog Explorer UI, the External Metadata and External Lineage APIs, or the Databricks SDK for Python. ^[external-lineage-databricks-on-aws.md]

## How It Works

When you configure a Lakeflow Connect managed ingestion pipeline, the system automatically records lineage relationships between:

- **Upstream sources**: External tables in systems such as MySQL, PostgreSQL, Salesforce, or other data sources supported by Lakeflow Connect.
- **Downstream destinations**: [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md) where the ingested data is stored.

The lineage graph shows how data flows from external source tables through transformations into Unity Catalog tables, and optionally to downstream consumers such as external reports. ^[external-lineage-databricks-on-aws.md]

## Related Concepts

- [External Lineage](/concepts/external-lineage.md) — General concept of adding lineage metadata for external systems
- [Unity Catalog Data Lineage](/concepts/unity-catalog-data-lineage.md) — Automatic lineage capture for Databricks queries
- Lakeflow Connect — Managed ingestion pipelines that trigger source lineage recording
- [External Metadata](/concepts/external-metadata-api.md) — Securable objects representing entities in external systems
- [External Lineage API](/concepts/external-lineage-api.md) — Programmatic interface for adding external lineage relationships

## Sources

- external-lineage-databricks-on-aws.md

# Citations

1. [external-lineage-databricks-on-aws.md](/references/external-lineage-databricks-on-aws-d8bef4f2.md)
