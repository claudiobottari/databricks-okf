---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41d15a145bbd1752a643937714281e1788be2e14382575c78f7918e6fec98a1f
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - ai-runtime-data-loading
    - ARDL
    - Data loading
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Data Loading
description: The mechanism for reading data into AI Runtime workloads, requiring an understanding of how data access works on the serverless platform for a smooth experience.
tags:
  - databricks
  - data-access
  - serverless
timestamp: "2026-06-19T08:57:14.815Z"
---

---
title: AI Runtime Data Loading
summary: The data access patterns and mechanisms for reading data into AI Runtime workloads on Databricks.
sources:
  - ai-runtime-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:23:21.771Z"
updatedAt: "2026-06-18T14:23:21.771Z"
tags:
  - databricks
  - data-access
  - dataloading
aliases:
  - ai-runtime-data-loading
  - ARDL
confidence: 1
provenanceState: extracted
inferredParagraphs: 2
---

# AI Runtime Data Loading

**AI Runtime Data Loading** refers to the mechanisms and best practices for reading and accessing data within Databricks AI Runtime — a compute offering optimized for deep learning workloads. AI Runtime provides fully managed GPU infrastructure for training and fine‑tuning models, and its data access capabilities are designed to work seamlessly with Databricks’ data governance and experiment tracking tools. ^[ai-runtime-databricks-on-aws.md]

## Overview

AI Runtime brings GPU support to Databricks Serverless, eliminating the need to configure clusters or manage autoscaling policies. Data loading is a core part of any deep‑learning pipeline, and AI Runtime integrates directly with Unity Catalog for governed data access and with MLflow for experiment tracking. ^[ai-runtime-databricks-on-aws.md]

## Environment Considerations

AI Runtime offers two managed Python environments: a minimal default base environment and a full‑featured Databricks AI environment that is pre‑loaded with popular ML frameworks such as PyTorch and Transformers. The pre‑loaded frameworks include standard data‑loading utilities (for example, PyTorch’s `DataLoader`), which can be used directly in notebooks and jobs. ^[ai-runtime-databricks-on-aws.md]

## Data Access Integration

AI Runtime is natively integrated across notebooks, jobs, Unity Catalog, and MLflow, enabling seamless development, data access, and experiment tracking. Users can read data from Unity Catalog tables, cloud storage, or other sources using familiar APIs, and the associated data lineage and permissions are governed by Unity Catalog. ^[ai-runtime-databricks-on-aws.md]

## Loading Data

For step‑by‑step instructions on how to load data into AI Runtime — including reading from cloud storage, Unity Catalog, and other common sources — see the dedicated guide: [Load data on AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/dataloading). ^[ai-runtime-databricks-on-aws.md]

## Limitations That Affect Data Loading

- AI Runtime only supports A10 and H100 accelerators and is not available for compliance security profile workspaces (e.g., HIPAA or PCI). ^[ai-runtime-databricks-on-aws.md]
- Adding dependencies using the **Environments** panel is not supported for scheduled jobs; install dependencies programmatically using `%pip install` in your notebook. ^[ai-runtime-databricks-on-aws.md]
- The maximum runtime for a workload is seven days. For longer training jobs, implement checkpointing and restart the job. ^[ai-runtime-databricks-on-aws.md]
- AI Runtime is limited to single‑node tasks; distributed data loading across multiple nodes is not supported. ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- [AI Runtime Environment](/concepts/ai-runtime-environments.md)
- [Deep Learning on Databricks](/concepts/deep-learning-on-databricks.md)
- Serverless Compute
- PyTorch DataLoader

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
