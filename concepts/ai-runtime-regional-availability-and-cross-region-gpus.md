---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bf0fca1618fecb9190e2bf4a058a44192bb4d21931202d9f3e8e1bb254a013d
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-regional-availability-and-cross-region-gpus
    - Cross-Region GPUs and AI Runtime Regional Availability
    - ARRAACG
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Regional Availability and Cross-Region GPUs
description: AI Runtime availability limited to specific AWS regions (us-west, us-east, ca-central-1, sa-east-1) with potential cross-region GPU spillover during high demand, which may incur egress costs.
tags:
  - aws
  - regions
  - networking
  - cost
timestamp: "2026-06-18T10:44:26.655Z"
---

---
title: AI Runtime Regional Availability and Cross-Region GPUs
summary: Overview of supported AWS regions for AI Runtime, on-demand GPU capacity behavior, and cross-region GPU usage during high-demand periods, including associated costs and network limitations.
sources:
  - ai-runtime-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:45:00.000Z"
updatedAt: "2026-06-18T10:45:00.000Z"
tags:
  - ai-runtime
  - gpu
  - regional-availability
  - cross-region
aliases:
  - ai-runtime-regions
  - cross-region-gpus
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# AI Runtime Regional Availability and Cross-Region GPUs

**AI Runtime** is a serverless compute offering at Databricks for deep learning workloads, providing GPU support without the need to configure clusters. Its regional availability and behavior under high demand are important operational considerations. ^[ai-runtime-databricks-on-aws.md]

## Regional Availability

AI Runtime is available in the following AWS regions:

- `us-west-2`
- `us-west-1`
- `us-east-1`
- `us-east-2`
- `ca-central-1`
- `sa-east-1`

A workspace must reside in one of these regions to use AI Runtime. In addition, the AI Runtime preview must be enabled by a workspace admin via the workspace admin settings (see Manage Databricks Previews). ^[ai-runtime-databricks-on-aws.md]

## On-Demand GPU Access and Capacity Constraints

AI Runtime provides on-demand access to GPU resources within the chosen region. While this offers flexible, low-friction access to accelerators, there may be periods where GPU capacity is constrained or temporarily unavailable in that region. ^[ai-runtime-databricks-on-aws.md]

## Cross-Region GPU Usage

During moments of high demand, AI Runtime may leverage GPUs from other AWS regions to fulfill workload requests. This cross-region usage introduces two additional considerations:

- **Egress costs**: Data transferred across regions may incur egress charges.
- **Network connectivity**: Cross-region network connectivity might be limited at certain times, potentially affecting performance or reliability.

These behaviors are part of the managed fallback strategy and are not configurable by the user. ^[ai-runtime-databricks-on-aws.md]

## Related Limitations

The following limitations are relevant to regional and cross-region GPU availability:

- AI Runtime supports only A10 and H100 accelerators.
- AI Runtime is **not supported** for workspaces with a [compliance security profile](/concepts/compliance-security-profile-databricks-on-aws.md) (e.g., HIPAA or PCI). Processing regulated data is not supported on AI Runtime.
- The maximum runtime for a single workload is seven days. For longer training jobs, implement checkpointing and restart the job once the maximum runtime is reached. ^[ai-runtime-databricks-on-aws.md]

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
