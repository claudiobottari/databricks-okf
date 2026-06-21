---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e0f19059d4ff6212a2d4ce69d2ebfeaa1147a56318ae92e28aa58c859eab4a4
  pageDirectory: concepts
  sources:
    - phase-6-design-delta-lake-architecture-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-in-the-medallion-pipeline
    - DQITMP
  citations:
    - file: phase-6-design-delta-lake-architecture-databricks-on-aws.md
title: Data Quality in the Medallion Pipeline
description: A strategy for progressively enforcing data quality through constraints, primary/foreign keys, expectations, and monitoring as data moves from bronze (lenient) to silver and gold (strict).
tags:
  - data-quality
  - data-pipeline
  - data-governance
timestamp: "2026-06-19T19:55:33.051Z"
---

# Data Quality in the Medallion Pipeline

Data quality in the [Medallion Architecture](/concepts/medallion-architecture.md) is a core design principle that ensures data becomes increasingly trustworthy as it flows through the bronze, silver, and gold layers. Regardless of the medallion variant, data quality must improve as data progresses through the layers, which in turn increases business confidence in the data. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Data Quality Progression Across Layers

The medallion architecture organizes data into three layers—bronze (raw), silver (refined), and gold (business-ready)—and each layer applies progressively stricter quality controls.

| Layer | Purpose | Quality Focus |
|-------|---------|---------------|
| **Bronze** | Raw data exactly as ingested, append-only | Minimal transformation; schema validation and null checks are applied at ingestion. |
| **Silver** | Cleansed, deduplicated, enriched data | Enforces schema, removes duplicates, handles missing values, standardizes formats. |
| **Gold** | Business-specific, aggregated, performance-optimized | Pre‑aggregated and denormalized; row‑level and column‑level security applied; final validation for consumption. |

^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

Data quality checks must be implemented at each layer. The bronze layer performs initial schema validation and null checks. As data moves to silver and gold, stricter rules are enforced to ensure downstream consumers receive trustworthy data. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Data Quality Tools

The Databricks lakehouse provides several tools to automate and enforce data quality:

- **Constraints**: Automatically verify the quality and integrity of data added to a table.
- **Primary and Foreign Keys**: Encode relationships between fields (informational, not enforced) to help with data modeling.
- **Expectations**: Prevent data quality issues from trickling downstream. Currently available with Lakeflow Spark Declarative Pipelines, with planned expansion to all Unity Catalog tables.
- **Lakehouse Monitoring**: Monitor the statistical properties and quality of data across all tables in the account.

^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Best Practices

- Implement data quality checks at bronze ingestion (e.g., schema validation, null checks).
- Enforce stricter quality rules as data moves to silver and gold.
- Monitor data quality metrics and trends over time.
- Define data quality SLAs for critical datasets.
- Automate alerting for data quality violations.
- Use Unity Catalog views and OpenSharing instead of copying data to avoid data silos that degrade quality.

^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Related Concepts

- [Medallion Architecture](/concepts/medallion-architecture.md) – The three‑layer structure that enforces data quality progression.
- Bronze Layer – Raw, immutable source of truth.
- Silver Layer – Refined, deduplicated datasets.
- Gold Layer – Business‑ready, aggregated data products.
- [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md) – Continuous monitoring of data quality metrics.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and lineage for quality tracking.
- [Delta Lake](/concepts/delta-lake.md) – Storage format enabling constraints and auditability.

## Sources

- phase-6-design-delta-lake-architecture-databricks-on-aws.md

# Citations

1. [phase-6-design-delta-lake-architecture-databricks-on-aws.md](/references/phase-6-design-delta-lake-architecture-databricks-on-aws-95b31109.md)
