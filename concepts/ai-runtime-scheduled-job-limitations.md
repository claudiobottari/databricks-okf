---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3423030bcc8c097dc3b36b1c4e90d515fb05ea21bff276cc5f7a9bd91861f3b
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-scheduled-job-limitations
    - ARSJL
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime scheduled job limitations
description: "Scheduled jobs using serverless GPU have key limitations: no Environments panel for dependencies (must use %pip install), no auto-recovery on failure, and a 7-day maximum runtime requiring manual checkpointing."
tags:
  - databricks
  - ai-runtime
  - jobs
  - limitations
timestamp: "2026-06-18T11:09:16.182Z"
---

# AI Runtime scheduled job limitations

**AI Runtime scheduled job limitations** describes the constraints and behavioral differences that apply when running recurring serverless GPU jobs on [AI Runtime](/concepts/ai-runtime.md), compared to interactive notebook usage or traditional cluster-based jobs. These limitations are particularly relevant when automating model training, evaluation, or batch inference through scheduled notebooks.^[connect-to-ai-runtime-databricks-on-aws.md]

## Dependency installation restrictions

In interactive notebooks, dependencies can be added using the **Environments** panel in the notebook UI. For serverless GPU scheduled jobs, this panel is **not supported**. All dependencies must be installed programmatically within the notebook code, for example using `%pip install` at the top of the notebook.^[connect-to-ai-runtime-databricks-on-aws.md]

## No auto-recovery on job failure

If a scheduled job fails due to incompatible packages or other reasons, automatic recovery is not available. You must manually fix the issue (for example, by adjusting dependency versions) and re-run the job. There is no built-in retry mechanism that resolves dependency conflicts.^[connect-to-ai-runtime-databricks-on-aws.md]

## Maximum runtime of 7 days

Scheduled AI Runtime jobs have a maximum runtime of 7 days (168 hours). For workloads that may exceed this limit — such as long-running model training with frequent checkpointing — you must implement manual checkpointing to allow the job to be interrupted and resumed. The recommended approach is to use Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`. See [model checkpointing](/concepts/ai-runtime-model-checkpointing.md) for details.^[connect-to-ai-runtime-databricks-on-aws.md]

## Hardware accelerator selection

When configuring a scheduled job through the Jobs UI or Databricks Asset Bundles, you must specify an accelerator (for example, `GPU_8xH100`). The available hardware options are the same as for interactive use, but the selection is made at the job definition level rather than at runtime.^[connect-to-ai-runtime-databricks-on-aws.md]

## Environment selection in Jobs API

When using the Jobs API or Databricks Asset Bundles, you can choose between the default base environment (specified by `environment_version: '4'`) or the AI environment (e.g., `databricks_ai_v5`) by setting `base_environment` in the task's environment spec. This selection must be explicit; there is no automatic fallback if an environment version is unavailable.^[connect-to-ai-runtime-databricks-on-aws.md]

## Related concepts

- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute model used by AI Runtime jobs
- [AI Runtime environment](/concepts/ai-runtime-environments.md) — The preset environments available for AI Runtime
- Model checkpointing — Recommended method for handling jobs that may exceed the 7-day limit
- Unity Catalog volumes — Storage used for checkpoint data
- Scheduled notebook jobs — General guidance on scheduling notebooks on Databricks
- Databricks Asset Bundles — Infrastructure-as-code tool for job definitions

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
