---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e82d28a32c7e46e2bea740fa4713a331f0abdf8b3971373c573c872b5de16624
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-limitations-and-constraints
    - Constraints and AI Runtime Limitations
    - ARLAC
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Limitations and Constraints
description: Key operational constraints for AI Runtime including no support for compliance security profiles (HIPAA/PCI), maximum 7-day runtime, limited accelerator types (A10/H100 only), potential capacity constraints, and cross-region egress costs.
tags:
  - databricks
  - compliance
  - limitations
  - operations
timestamp: "2026-06-19T22:03:58.242Z"
---

---
title: AI Runtime Limitations and Constraints
summary: Key restrictions including only A10/H100 support, no HIPAA/PCI compliance, 7‑day max runtime, dependency install limitations, and potential cross‑region GPU usage.
sources:
  - ai-runtime-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - limitations
  - constraints
  - compliance
aliases:
  - ai-runtime-limitations-and-constraints
  - AI Runtime Constraints
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AI Runtime Limitations and Constraints

This page documents the known limitations and constraints of [AI Runtime](/concepts/ai-runtime.md) on Databricks. Understanding these restrictions helps in planning workloads and avoiding unexpected failures.

## Release Stage

Single‑node tasks on AI Runtime are in **Public Preview**; the distributed training API for multi‑GPU workloads remains in **Beta**. The 1×H100 accelerator is also in **Beta** and requires a workspace admin to enable the **AI Runtime Beta Feature** preview from the **Previews** page. ^[ai-runtime-databricks-on-aws.md]

## Hardware Constraints

AI Runtime supports only **A10** and **H100** accelerators. All accelerators provision a **single node**; distributed training is limited to multiple GPUs on that single node. Multi‑node clusters are not supported. ^[ai-runtime-databricks-on-aws.md]

## Regional Availability

AI Runtime is available only in the following AWS regions:
- `us-west-2`
- `us-west-1`
- `us-east-1`
- `us-east-2`
- `ca-central-1`
- `sa-east-1`

Workspaces in other regions cannot use AI Runtime. ^[ai-runtime-databricks-on-aws.md]

## Compliance Profile Restriction

AI Runtime is **not supported for compliance security profile workspaces** such as those requiring HIPAA or PCI compliance. Processing regulated data on AI Runtime is not allowed. ^[ai-runtime-databricks-on-aws.md]

## Environment Management Limitations

Adding dependencies using the **Environments** panel is **not supported for AI Runtime scheduled jobs**. Users must install dependencies programmatically with `%pip install` in the notebook instead. For scheduled jobs, **auto recovery behaviour for incompatible package versions** associated with the notebook is not supported. ^[ai-runtime-databricks-on-aws.md]

## Runtime Limits

The **maximum runtime for a single workload is seven days**. For training jobs that exceed this limit, implement checkpointing and restart the job once the maximum runtime is reached. ^[ai-runtime-databricks-on-aws.md]

## Capacity and Networking Constraints

AI Runtime provides **on‑demand access** to GPU resources. While this offers flexibility, there **may be periods where capacity is constrained or unavailable** in your region. During moments of high demand, AI Runtime may **leverage cross‑region GPUs**, which can incur **egress costs**. Cross‑region network connectivity might be limited at certain times. ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – Overview of the compute offering
- [AI Runtime environment](/concepts/ai-runtime-environments.md) – Managed Python environments for AI Runtime
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance for ML assets, used with AI Runtime
- [MLflow](/concepts/mlflow.md) – Experiment tracking integrated with AI Runtime
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – Command‑line tool for submitting workloads (Beta)

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
