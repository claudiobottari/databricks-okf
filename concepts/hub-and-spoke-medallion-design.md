---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1cad2f40062e03cfbf79834027092a9839b502fa5a78f77895f90992883b6fd2
  pageDirectory: concepts
  sources:
    - phase-6-design-delta-lake-architecture-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hub-and-spoke-medallion-design
    - HMD
  citations:
    - file: phase-6-design-delta-lake-architecture-databricks-on-aws.md
title: Hub-and-Spoke Medallion Design
description: An enterprise deployment pattern that combines medallion architecture with a centralized data hub and domain-specific spokes, enabling shared organization-wide assets alongside domain-curated data products.
tags:
  - data-architecture
  - enterprise
  - data-governance
timestamp: "2026-06-19T19:55:14.063Z"
---

# Hub-and-Spoke Medallion Design

**Hub-and-Spoke Medallion Design** is an enterprise architecture pattern that combines the [Medallion Architecture](/concepts/medallion-architecture.md) (bronze, silver, gold layers) with a hub-and-spoke organizational model. It centralizes shared data assets in a data hub while allowing domain-specific data processing and curation within individual data domains.^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Overview

In this pattern, a central **data hub** ingests, curates, and manages organization-wide data assets — such as SAP data, financials, weather data, or other general-purpose datasets. These hub-curated datasets can be considered source-linked data products available for consumption by multiple domains.^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

Each **data domain** reads some of the hub-curated data products and also ingests and curates its own domain-specific raw data. Domains then produce domain-specific data products tailored to their business needs.^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Publishing Models

Domains can publish their data products through two models:^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

- **Centralized publishing**: Domains publish data products back to the hub for organization-wide consumption.
- **Distributed publishing**: Domains publish data products within their own catalogs for domain-specific use only.

## Example Architecture

A typical hub-and-spoke medallion deployment includes a central data hub alongside domain-specific medallion layers:^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

**Data Hub (Central)**
- Bronze: Organization-wide raw data (SAP, financials, weather)
- Silver: Curated shared datasets
- Gold: Enterprise-wide data products

**Sales Domain**
- Bronze: Sales-specific raw data + shared hub data
- Silver: Sales analytics datasets
- Gold: Sales data products (published to hub or domain)

**Engineering Domain**
- Bronze: Engineering telemetry + shared hub data
- Silver: Engineering metrics
- Gold: Engineering dashboards (published within domain)

## Best Practices

When implementing a hub-and-spoke medallion design, follow these guidelines:^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

- Use the hub for organization-wide shared data that multiple domains consume.
- Allow domains to ingest and curate their own domain-specific data.
- Establish clear data product publishing policies (centralized vs distributed).
- Use [Unity Catalog](/concepts/unity-catalog.md) catalogs to separate hub and domain data.
- Use Databricks-managed [OpenSharing](/concepts/opensharing.md) to share data products between hub and domains.

## Relationship to Medallion Architecture

The hub-and-spoke medallion design extends the standard Delta Lake Architecture by applying medallion layers (bronze, silver, gold) within both the central hub and each domain. Each domain maintains its own medallion pipeline, potentially incorporating shared hub data alongside domain-specific data. The hub itself also follows medallion layering for organization-wide assets.^[phase-6-design-delta-lake-architecture-databricks-on-aws.md]

## Related Concepts

- [Medallion Architecture](/concepts/medallion-architecture.md) — The foundational three-layer data organization pattern
- Delta Lake Architecture — Overall storage architecture recommendations
- Data Governance Strategy — Policies for managing data quality and access
- Data Product Publishing — How domains share their curated datasets
- [Unity Catalog](/concepts/unity-catalog.md) — Used to separate hub and domain data and enable data sharing

## Sources

- phase-6-design-delta-lake-architecture-databricks-on-aws.md

# Citations

1. [phase-6-design-delta-lake-architecture-databricks-on-aws.md](/references/phase-6-design-delta-lake-architecture-databricks-on-aws-95b31109.md)
