---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b56430977b911f9169079fc0f87e14b4209cb0d00b9d1d7385994a7939797c1
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-release-tiers-public-preview-vs-beta
    - DRTPPVB
  citations:
    - file: computer-vision-databricks-on-aws.md
title: "Databricks Release Tiers: Public Preview vs Beta"
description: "AI Runtime features are split across two release stages: single-node serverless GPU tasks are in Public Preview, while the distributed multi-GPU training API remains in Beta."
tags:
  - databricks
  - release-management
  - preview
timestamp: "2026-06-18T11:05:31.895Z"
---

# Databricks Release Tiers: Public Preview vs Beta

**Databricks Release Tiers** define the maturity and support level of features during their development lifecycle. The two primary pre‑general‑availability (pre‑GA) tiers are **Public Preview** and **Beta**. Understanding the distinction between these tiers is important for planning production deployments and managing risk.

## Public Preview

**Public Preview** is a release tier for features that are feature‑complete and have passed internal testing but are not yet fully supported for production use. Features in Public Preview are available to all customers and are considered stable enough for evaluation and early adoption. ^[computer-vision-databricks-on-aws.md]

### Characteristics

- **Availability**: Enabled by default in most workspaces; some features may require opt‑in.
- **Support**: Backed by standard Databricks support, but service‑level agreements (SLAs) for performance and availability may not apply.
- **Production use**: Not recommended for production workloads, though some customers choose to use Public Preview features in non‑critical production scenarios.
- **API stability**: APIs may change between releases; breaking changes are possible.

### Examples

- AI Runtime for single‑node tasks is in Public Preview. ^[computer-vision-databricks-on-aws.md]

## Beta

**Beta** is an earlier release tier for features that are still under active development and may not be feature‑complete. Beta features are made available for early customer feedback and testing but come with fewer guarantees. ^[computer-vision-databricks-on-aws.md]

### Characteristics

- **Availability**: Typically opt‑in only; may require manual activation by a Databricks representative.
- **Support**: Limited or no support; features may have known bugs or incomplete documentation.
- **Production use**: Not intended for production workloads.
- **API stability**: APIs are subject to change without notice; breaking changes are expected.

### Examples

- The distributed training API for multi‑GPU workloads in AI Runtime remains in Beta. ^[computer-vision-databricks-on-aws.md]

## Key Differences

| Aspect | Public Preview | Beta |
|--------|----------------|------|
| Maturity | Feature‑complete, tested | Under active development |
| Availability | Enabled by default or simple opt‑in | Opt‑in, often by request |
| Support | Standard Databricks support | Limited or no support |
| Production suitability | Not recommended | Not intended |
| API stability | May change between releases | Subject to breaking changes |

## Recommended Usage

- **Public Preview**: Suitable for evaluation, proof‑of‑concept projects, and non‑critical internal tooling. Teams can begin integrating with Public Preview features while planning for potential API changes before General Availability (GA).
- **Beta**: Best for providing early feedback to Databricks, exploring new capabilities, and testing integration paths. Not suitable for any production or customer‑facing workload.

## Transitioning to General Availability

When a feature graduates from Public Preview or Beta to **General Availability (GA)**, it becomes fully supported, covered by SLAs, and recommended for production use. APIs are stable, and breaking changes require formal deprecation notices. Databricks typically communicates GA transitions through release notes and product announcements.

## Related Concepts

- Databricks Release Notes — Official documentation of feature releases and changes
- [AI Runtime](/concepts/ai-runtime.md) — Databricks ML runtime that includes features at various release tiers
- Feature Maturity Lifecycle — The complete lifecycle from development through GA to end‑of‑life

## Sources

- computer-vision-databricks-on-aws.md

# Citations

1. [computer-vision-databricks-on-aws.md](/references/computer-vision-databricks-on-aws-14d18d47.md)
