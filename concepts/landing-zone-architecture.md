---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: da8888b7934c642c03914768457d6a30245cf64b614917144ffdab79669c8331
  pageDirectory: concepts
  sources:
    - phase-6-design-delta-lake-architecture-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - landing-zone-architecture
    - LZA
  citations:
    - file: phase-6-design-delta-lake-architecture-databricks-on-aws.md
title: Landing Zone Architecture
description: An optional pre-ingestion layer in cloud object storage that receives raw files from external systems before processing into the bronze medallion layer, with patterns for triggers and governance.
tags:
  - data-architecture
  - data-ingestion
  - cloud-storage
timestamp: "2026-06-19T19:55:24.368Z"
---

# Landing Zone Architecture

**Landing Zone Architecture** is a data storage pattern used in [Medallion Architecture](/concepts/medallion-architecture.md) deployments where raw files from external systems are temporarily staged before ingestion into the Bronze Layer. In larger organizations, this additional layer sits between source systems and the first medallion layer, providing a controlled entry point for data arriving from outside the lakehouse. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Purpose

The landing zone receives raw files from external systems before they are processed and ingested into the bronze layer. This provides a clear boundary between external data sources and the managed lakehouse environment, enabling auditability, error handling, and decoupled ingestion pipelines. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Landing Zone Patterns

There are several common patterns for implementing a landing zone:

- **Cloud object storage**: S3, ADLS Gen2, or GCS buckets used for file drops from external systems. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Unity Catalog volumes**: Secure POSIX-style file access with full [Unity Catalog](/concepts/unity-catalog.md) governance, recommended for new deployments. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Third-party access**: External systems can write directly to landing zones without requiring direct access to the lakehouse. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Notification triggers**: Event notifications from cloud storage can trigger ingestion pipelines when new files arrive. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Best Practices

When designing a landing zone architecture, follow these recommendations:

- Use Unity Catalog Volumes for landing raw data before bronze ingestion. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Configure retention policies for landing zone data to manage storage costs. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Use Auto Loader for efficient file ingestion from cloud storage. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Implement idempotent ingestion to handle retries safely. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Monitor landing zone pipelines for failures and data quality issues. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Relationship to Medallion Architecture

The landing zone is not one of the three core medallion layers (bronze, silver, gold), but rather an optional staging area that precedes the bronze layer. Pipelines read from the landing zone, perform initial validation and transformation, and write the ingested data into the bronze layer as raw, immutable records. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

For comprehensive medallion architecture guidance, see [What is the medallion lakehouse architecture?](/concepts/medallion-architecture.md).

## Related Concepts

- [Medallion Architecture](/concepts/medallion-architecture.md) — The overall data layering pattern that the landing zone feeds into.
- Bronze Layer — The first medallion layer that receives data from the landing zone.
- [Delta Lake](/concepts/delta-lake.md) — The storage format used for lakehouse tables.
- [Data Ingestion Strategy](/concepts/data-ingestion-strategy-for-lakehouse.md) — Methods for moving data from landing zones into bronze tables.
- Phase 6: Design Delta Lake architecture — The deployment phase covering landing zone design.

## Sources

- phase-6-design-delta-lake-architecture-databricks-on-aws.md

# Citations

1. [phase-6-design-delta-lake-architecture-databricks-on-aws.md](/references/phase-6-design-delta-lake-architecture-databricks-on-aws-95b31109.md)
