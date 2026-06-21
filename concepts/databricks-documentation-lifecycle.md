---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78cf84e7b4ec170a9ab649798f773052decdba1557dd430b6bb29698b6d34a97
  pageDirectory: concepts
  sources:
    - migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-documentation-lifecycle
    - DDL
  citations:
    - file: migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md
title: Databricks Documentation Lifecycle
description: The practice of Databricks marking documentation as 'retired' when products or services are no longer supported or superseded, serving as an archival notice for users.
tags:
  - documentation
  - lifecycle
  - databricks
timestamp: "2026-06-19T19:34:16.037Z"
---

# Databricks Documentation Lifecycle

**Databricks Documentation Lifecycle** refers to the stages through which product documentation passes as features are introduced, updated, and eventually retired. Understanding this lifecycle helps users identify whether a given article reflects the current product behavior or describes a deprecated capability.

## Stages

### Active Documentation
Most Databricks documentation is kept up to date with the latest product releases. Active articles describe currently supported features and are regularly reviewed and revised. New documentation is published when features are introduced or when the user experience changes. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

### Retired Documentation
When a product, service, or technology is no longer supported, the corresponding documentation is marked as **retired**. Retired documentation carries a prominent notice indicating that it is no longer maintained and might not be updated. These articles often reside in an archive section of the documentation site (e.g., under `/archive/`). ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

The exact notice reads:
> This documentation has been retired and might not be updated. The products, products, services, or technologies mentioned in this content are no longer supported. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

### Migration Guides
When a feature is superseded by a new experience, Databricks publishes migration documentation to help users transition from the old approach to the new one. These migration guides are themselves subject to the lifecycle: once the migration period is over, the migration guide may be retired. ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Example: Optimized LLM Serving Endpoints

A concrete example of the lifecycle is the documentation for optimized LLM serving endpoints. Databricks introduced a new **provisioned throughput** experience for serving LLMs, simplifying configuration by using tokens-per-second instead of concurrency and removing the need for customers to select GPU workload types. The older documentation was moved to the archive and marked as retired. Users are directed to the new [Provisioned Throughput](/concepts/provisioned-throughput.md) documentation and to [Foundation Model APIs](/concepts/foundation-model-apis.md). ^[migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md]

## Identifying the Lifecycle Stage of a Page

- **Retired pages** are clearly labeled with a warning banner at the top of the article and are typically hosted under an `archive` path in the URL.
- **Active pages** may still mention older features in a historical context, but will not carry a retirement notice.
- **Migration pages** explicitly describe how to move from an old feature to a new one and are often timed to coincide with the deprecation announcement.

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Model Serving](/concepts/model-serving.md)

## Sources

- migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md

# Citations

1. [migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws.md](/references/migrate-optimized-llm-serving-endpoints-to-provisioned-throughput-databricks-on-aws-b1657ebd.md)
