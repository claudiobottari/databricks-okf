---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a843ca5966b6355c1523b3c95a83e6dcfe52f62be99bfff35885d6a9924d0cc2
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-release-types-public-preview-and-beta
    - "Beta and Databricks Release Types: Public Preview"
    - DRTPPAB
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
title: "Databricks Release Types: Public Preview and Beta"
description: "Databricks categorizes features by maturity: Public Preview (generally available for evaluation) and Beta (still under active development, for early adopters)."
tags:
  - databricks
  - release-management
timestamp: "2026-06-19T14:58:08.287Z"
---

# Databricks Release Types: Public Preview and Beta

**Databricks Release Types: Public Preview and Beta** refers to the two pre-general-availability release stages that Databricks uses to make features available to customers before they reach full production readiness. These release types allow users to access and test new functionality while acknowledging that the feature may have limitations or ongoing development.

## Public Preview

**Public Preview** is a release stage where a feature is made available for general customer use, but it is not yet considered fully GA (General Availability). Features in Public Preview are typically stable enough for evaluation and non-production workloads, but they may have incomplete documentation, limited support, or known limitations. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

For example, AI Runtime for single-node tasks is designated as being in **Public Preview**, meaning customers can use it for evaluation and development purposes while understanding it has not reached full production maturity. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Beta

**Beta** is a more limited release stage compared to Public Preview. Beta features are typically available to a subset of customers or for specific use cases and may have more significant limitations, instability, or incomplete functionality. Beta releases are intended for early testing and feedback collection before broader availability. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

The distributed training API for multi-GPU workloads is described as remaining in **Beta**, indicating it is available for testing but not yet ready for broad production use. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Key Differences

| Aspect | Public Preview | Beta |
|--------|---------------|------|
| Availability | Generally available to all customers | Limited availability (subset of users or use cases) |
| Stability | More stable, suitable for evaluation | Less stable, may have significant limitations |
| Use case | Non-production workloads and evaluation | Early testing and feedback collection |
| Maturity | Closer to GA readiness | Earlier in the development cycle |

## Related Concepts

- Databricks Release Notes — Official documentation for release types and versioning.
- General Availability (GA) — The full production release stage that follows Public Preview and Beta.
- [AI Runtime](/concepts/ai-runtime.md) — Databricks runtime for machine learning tasks, with different release stages for different components.
- [Deep learning based recommender systems](/concepts/deep-learning-based-recommender-systems.md) — Example of a feature where the single-node API is in Public Preview while multi-GPU remains in Beta.

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
