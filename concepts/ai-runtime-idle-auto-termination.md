---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a413ac09b4d30a717e037840acac4bb399dfec39b556dec021c0a02fc62af840
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-idle-auto-termination
    - ARIA
    - ARIMA
    - auto-termination
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime idle auto-termination
description: AI Runtime compute auto-terminates after 60 minutes of inactivity to preserve resources.
tags:
  - databricks
  - ai-runtime
  - resource-management
timestamp: "2026-06-18T11:08:51.874Z"
---

# AI Runtime idle auto-termination

**AI Runtime idle auto-termination** is a feature of [AI Runtime](/concepts/ai-runtime.md) on Databricks that automatically disconnects serverless GPU compute after 60 minutes of inactivity when connected through interactive notebooks. This helps preserve GPU resources for workloads that require them.^[connect-to-ai-runtime-databricks-on-aws.md]

## Auto-termination behavior

When you connect an interactive notebook to AI Runtime via the **Serverless GPU** compute option, the connection to your compute auto-terminates after 60 minutes of inactivity.^[connect-to-ai-runtime-databricks-on-aws.md]

This auto-termination applies only to interactive notebook sessions. Scheduled jobs using AI Runtime are not subject to this idle timeout — they run until completion, with a maximum runtime of 7 days.^[connect-to-ai-runtime-databricks-on-aws.md]

## Best practices

### Preserve GPU resources for GPU-intensive work

For operations that do not require GPUs — such as cloning a Git repository, converting data formats, or exploratory data analysis — attach your notebook to a CPU cluster instead of using serverless GPU. This preserves GPU resources for workloads that benefit from them.^[connect-to-ai-runtime-databricks-on-aws.md]

### Handle auto-termination in long-running notebook sessions

If you are working interactively and expect to be idle for more than 60 minutes, save your work and state before the auto-termination occurs. For workloads that may exceed the 7-day maximum runtime for scheduled jobs, implement manual checkpointing to allow resumption. Databricks recommends using Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data` for model checkpointing.^[connect-to-ai-runtime-databricks-on-aws.md]

## Related concepts

- [AI Runtime](/concepts/ai-runtime.md) — The serverless GPU compute environment for machine learning workloads
- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute type used by AI Runtime
- [AI Runtime Environments](/concepts/ai-runtime-environments.md) — The base environments available for AI Runtime
- Model checkpointing — Techniques for saving and resuming long-running workloads
- Unity Catalog volumes — Storage for checkpoint data

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
