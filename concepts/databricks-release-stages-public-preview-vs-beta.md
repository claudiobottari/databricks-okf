---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b4211d455688c1f2f53a7cb1a9c69bb66c0ac8fd2d1cd78a1d7ce68713d97c4
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-release-stages-public-preview-vs-beta
    - DRSPPVB
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: "Databricks Release Stages: Public Preview vs Beta"
description: Databricks distinguishes between Public Preview (feature-complete and ready for broader adoption) and Beta (still under active development) release stages for its AI Runtime capabilities.
tags:
  - databricks
  - release-management
  - platform
timestamp: "2026-06-19T13:58:16.826Z"
---

# Databricks Release Stages: Public Preview vs Beta

**Public Preview** and **Beta** are two distinct release stages used by Databricks to indicate the maturity and stability of features. The source document highlights a concrete example: AI Runtime for single-node tasks is in **Public Preview**, while the distributed training API for multi-GPU workloads remains in **Beta**. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Differences

Databricks defines these stages in its [release types documentation](https://docs.databricks.com/aws/en/release-notes/release-types). Based on the example provided:

- **Public Preview** – Applied to features that are more broadly available and have a higher level of stability. In this case, single-node AI Runtime tasks are designated as Public Preview.
- **Beta** – Refers to features that are still under active development and may have more limited support or stability guarantees. The distributed training API for multi-GPU workloads is currently in Beta.

These classifications help users understand the risk profile and support expectations for each feature. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example from the Source

| Feature | Stage |
|---------|-------|
| [AI Runtime](/concepts/ai-runtime.md) for single-node tasks | Public Preview |
| Distributed training API for multi-GPU workloads | Beta |

The table reflects the exact designations given in the source document. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The runtime environment for machine learning workloads on Databricks.
- [Serverless GPU API](/concepts/serverless-gpu-api.md) – The API used for distributed training, currently in Beta.
- Release notes – The official Databricks documentation detailing release stages.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
