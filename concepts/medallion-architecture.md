---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e14642f8142e803fc36ff26f6d30d0420f4cdf8229a5a27a17b32b0912b60580
  pageDirectory: concepts
  sources:
    - phase-6-design-delta-lake-architecture-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - medallion-architecture
    - What is the medallion lakehouse architecture?
  citations:
    - file: phase-6-design-delta-lake-architecture-databricks-on-aws.md
title: Medallion Architecture
description: A data organization pattern that structures data into bronze (raw), silver (refined), and gold (business-ready) layers to progressively improve data quality as it flows through a lakehouse pipeline.
tags:
  - data-architecture
  - data-lakehouse
  - data-quality
timestamp: "2026-06-19T19:55:45.621Z"
---

# Medallion Architecture

**Medallion Architecture** is a data design pattern that organizes data into progressively refined layers as it moves through a pipeline. At each layer, data quality and structure improve, producing datasets that are increasingly trustworthy and business-ready. The pattern is fundamental to building a well-structured Lakehouse on Databricks. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

In its simplest form, the architecture consists of three layers: bronze, silver, and gold. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Architecture Layers

### Bronze Layer (Raw Data)

The bronze layer is the first layer of the lakehouse. It ingests source data exactly as it arrives from external systems and persists it in its original form, serving as the immutable source of truth for all downstream data. When all subsequent data is derived from this layer, the silver and gold layers can be reconstructed from it if needed. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Characteristics:**
- **Source of truth**: Raw data exactly as it arrives from source systems. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Minimal transformation**: Data stored in its original format or converted to [Delta Lake](/concepts/delta-lake.md) format for auditability. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Immutable**: Data is append-only and never updated or deleted. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Schema-on-read**: Flexible schema handling for diverse source systems. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Audit trail**: For regulated data (such as for GDPR), converting to Delta format may be appropriate. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Best practices:**
- Preserve all source data fields for complete auditability. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Use [Unity Catalog](/concepts/unity-catalog.md) volumes for landing raw files. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Implement incremental ingestion to avoid full reprocessing. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Partition by ingestion date for efficient data management. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Document data sources and ingestion schedules. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

### Silver Layer (Refined Data)

The silver layer holds cleansed, refined, filtered, and aggregated data. It is the foundation for reporting, dashboards, and [Machine Learning](/concepts/cicd-for-machine-learning.md) workloads. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Characteristics:**
- **Data quality**: Removes duplicates, handles missing values, and enforces schema. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Enrichment**: Joins data from multiple sources to create integrated datasets. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Standardization**: Applies consistent data types, formats, and naming conventions. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Business rules**: Implements validation rules and business logic. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Best practices:**
- Implement data quality checks and monitoring. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Use Unity Catalog managed tables for silver layer data. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Partition by business dimensions (such as date, region, product). ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Document transformation logic and business rules. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Establish SLAs for data freshness. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

### Gold Layer (Business-Ready Data)

The gold layer is organized around business or project needs and provides different views as data products to business units. It optimizes for performance through pre-aggregated and denormalized structures and applies security controls such as anonymization, row-level security, and column masking. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Characteristics:**
- **Business-specific**: Tailored to specific use cases and consumers. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Performance-optimized**: Pre-aggregated and denormalized for fast queries. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Access-controlled**: Implements row-level security and column masking. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Consumer-ready**: Structured for Business Intelligence (BI) tools, applications, and machine learning models. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- **Data products**: Published as reusable datasets across the organization. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Best practices:**
- Create separate gold tables for different business units or use cases. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Use dynamic views for row-level and column-level security. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Implement predictive optimization for frequently queried tables. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Document data lineage from bronze through gold. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Publish data products through Unity Catalog with clear ownership. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Landing Zone Consideration

Larger organizations often add a landing zone before the bronze layer. The landing zone receives raw files from external systems before ingestion into bronze. Common patterns include using cloud object storage (such as Amazon S3), [Unity Catalog](/concepts/unity-catalog.md) volumes for POSIX-style file access with governance, and event notification triggers to initiate ingestion pipelines. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Hub-and-Spoke Medallion Design

For enterprise deployments, a hub-and-spoke pattern can be combined with the medallion architecture. The central **data hub** ingests, curates, and manages organization-wide assets (such as SAP data, weather data, or financials). Individual **data domains** read from the hub and also ingest their own domain-specific raw data, then produce domain-specific data products. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

Domains can publish data products back to the hub for organization-wide consumption (centralized publishing) or keep them within their own catalogs (distributed publishing). ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Best practices:**
- Use the hub for organization-wide shared data consumed by multiple domains. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Allow domains to ingest and curate their own domain-specific data. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Establish clear data product publishing policies. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Use Unity Catalog catalogs to separate hub and domain data. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Use Databricks-managed [OpenSharing](/concepts/opensharing.md) to share data products between hub and domains. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Data Quality

Data quality must improve as data progresses through the layers, which increases business trust in the data. Tools for enforcing quality include constraints (automatic verification of data integrity), primary and foreign keys (informational relationship encoding), Expectations (prevention of downstream issues, currently supported in [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)), and [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md) (statistical monitoring of data quality across all tables). ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Best practices:**
- Implement data quality checks at bronze ingestion (schema validation, null checks). ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Enforce stricter quality rules as data moves to silver and gold. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Monitor data quality metrics and trends over time. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Define data quality SLAs for critical datasets. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Automate alerting for data quality violations. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Avoiding Data Silos

While standalone copies of data may be necessary for agility, experimentation, and innovation, they become data silos when downstream business data products depend on them. Silos quickly fall out of sync and reduce trust in the lakehouse. Recommendations to avoid silos include using Unity Catalog views and OpenSharing instead of copying data, establishing a single source of truth for each dataset, discouraging department-level copies, tracking data dependencies with lineage, and retiring redundant datasets regularly. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Recommendations

**Recommended:**
- Use the medallion architecture to structure the data lake (bronze, silver, gold). ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Use Unity Catalog managed tables for all lakehouse data. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Use Unity Catalog volumes for landing zones and raw unstructured data. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Implement data quality checks at each layer. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Enable predictive optimization for frequently queried managed tables. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Avoid:**
- Creating data silos by duplicating operational data across domains. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Using external tables unless data must remain in specific storage paths. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Skipping the bronze layer — always preserve raw data as source of truth. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Bypassing data quality checks to meet delivery deadlines. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]
- Allowing unmanaged data sprawl without Unity Catalog governance. ^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- Lakehouse
- [Unity Catalog](/concepts/unity-catalog.md)
- Data Ingestion
- Data Governance
- Data Quality
- [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md)
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- [OpenSharing](/concepts/opensharing.md)
- Business Intelligence (BI)

## Sources

- phase-6-design-delta-lake-architecture-databricks-on-aws.md

# Citations

1. [phase-6-design-delta-lake-architecture-databricks-on-aws.md](/references/phase-6-design-delta-lake-architecture-databricks-on-aws-95b31109.md)
