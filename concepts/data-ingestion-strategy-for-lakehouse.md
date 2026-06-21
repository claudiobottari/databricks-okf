---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9535f3376a6427d3ab6e8aef59aed8015d1e9a7485a24fb9e245e2ece8e5f818
  pageDirectory: concepts
  sources:
    - phase-6-design-delta-lake-architecture-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-ingestion-strategy-for-lakehouse
    - DISFL
    - Data Ingestion Strategy
  citations:
    - file: phase-6-design-delta-lake-architecture-databricks-on-aws.md
title: Data Ingestion Strategy for Lakehouse
description: Methods and patterns for ingesting data into the bronze layer, including Lakeflow Connect, partner tools, custom pipelines, batch/streaming ingestion, and change data capture (CDC).
tags:
  - data-ingestion
  - data-pipeline
  - lakehouse
timestamp: "2026-06-19T19:55:20.742Z"
---

# Data Ingestion Strategy for Lakehouse

**Data Ingestion Strategy for Lakehouse** refers to the set of architectural decisions, patterns, and tools used to load data from external systems into the lakehouse, typically into the bronze layer of the [Medallion Architecture](/concepts/medallion-architecture.md). The strategy determines how raw data is captured, where it lands, and how it is made available for subsequent refinement in the silver and gold layers. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Ingestion Methods

Databricks provides multiple methods for ingesting data into the lakehouse, chosen based on the source system, data volume, and transformation requirements. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

- **Lakeflow Connect**: A managed data ingestion service that can regularly sync data from external sources into Databricks without writing code. It is the recommended first choice for sources it supports. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Partner ingestion tools**: Tools such as Fivetran can ingest data from sources not supported by Lakeflow Connect. Raw and unstructured data from these tools should be stored in Unity Catalog volumes rather than external locations. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Custom ingestion pipelines**: For complex transformation requirements or unsupported sources, build custom pipelines using Lakeflow Spark Declarative Pipelines or notebooks. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Ingestion Patterns

The ingestion pattern is selected based on latency requirements, data volume, and the nature of updates from the source system. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

- **Batch ingestion**: Scheduled data loads (e.g., hourly, daily, weekly). Best for large volumes of historical data, lower cost than streaming, and acceptable latency for analytical workloads. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Streaming ingestion**: Continuous data ingestion with low latency. Use Lakeflow Spark Declarative Pipelines with Auto Loader for streaming file ingestion. Best for real-time analytics and operational use cases, though it incurs higher compute costs. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Change data capture (CDC)**: Captures and applies incremental changes from source systems. Efficient for large tables with frequent updates, preserves data lineage and audit trail. Supported by Lakeflow Connect and Lakeflow Spark Declarative Pipelines. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Best Practices for Data Ingestion

A well-designed ingestion strategy follows these best practices to ensure reliability, auditability, and ease of management: ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

- Use Unity Catalog volumes for landing raw data before bronze ingestion.
- Implement idempotent ingestion to handle retries safely.
- Use Auto Loader for efficient file ingestion from cloud storage.
- Configure retention policies for landing zone data.
- Monitor ingestion pipelines for failures and data quality issues.

## Landing Zone Architecture

In larger organizations, pipelines often include an additional landing zone in the cloud that receives raw files from external systems before they are ingested into the bronze layer. Common patterns include: ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

- **Cloud object storage**: S3 buckets for file drops.
- **Unity Catalog volumes**: Secure POSIX-style file access governed by Unity Catalog.
- **Third-party access**: External systems that write directly to landing zones.
- **Notification triggers**: Event notifications that trigger ingestion pipelines.

The landing zone is separate from the bronze layer itself and acts as a staging area that can be governed with retention policies. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Medallion Architecture Context

Ingested data is the foundation of the [Medallion Architecture](/concepts/medallion-architecture.md). The bronze layer stores raw data exactly as it arrives, with minimal transformation and an append-only, immutable approach. All downstream data in silver and gold layers is derived from this source of truth. At bronze ingestion, data quality checks such as schema validation and null checks should be applied, with stricter rules enforced as data moves to silver and gold. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Related Concepts

- Bronze Layer (Raw Data)
- Silver Layer (Refined Data)
- Gold Layer (Business-Ready Data)
- Lakeflow Connect
- Auto Loader
- Unity Catalog Volumes
- [Medallion Architecture](/concepts/medallion-architecture.md)
- Data Quality Strategy
- Table Management Strategy

## Sources

- phase-6-design-delta-lake-architecture-databricks-on-aws.md

# Citations

1. [phase-6-design-delta-lake-architecture-databricks-on-aws.md](/references/phase-6-design-delta-lake-architecture-databricks-on-aws-95b31109.md)
