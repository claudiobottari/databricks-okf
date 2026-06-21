---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41e8b8d0a269a5bf98e180c9dacc6b8b439d7fe659516650c4722960e1b74646
  pageDirectory: concepts
  sources:
    - workload-yaml-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - job-reliability-configuration
    - JRC
  citations:
    - file: workload-yaml-reference-databricks-on-aws.md
title: Job Reliability Configuration
description: Settings for workload resilience including `max_retries` (number of automatic retries on failure) and `timeout_minutes` (wall-clock budget per attempt) in AI Runtime YAML configs.
tags:
  - reliability
  - retries
  - timeout
timestamp: "2026-06-19T23:27:43.385Z"
---

# Job Reliability Configuration

**Job Reliability Configuration** refers to settings within a [workload YAML](/concepts/workload-yaml-configuration.md) configuration that control how a training job behaves in the event of failure, including retry limits and timeouts. These settings ensure that distributed training jobs on Databricks can complete even when nodes or processes fail intermittently. ^[workload-yaml-reference-databricks-on-aws.md]

## Core Fields

A reliable job configuration uses two key fields within the workload YAML:

### `max_retries`

The **`max_retries`** field specifies the number of times the system will re-attempt a failed workload. If the workload exits with a non‑zero status, the [AI Runtime](/concepts/ai-runtime.md) retries the entire job — including all nodes — up to `max_retries` additional times. ^[workload-yaml-reference-databricks-on-aws.md]

- **Type:** integer
- **Default:** `0` (no retries)
- **The total number of attempts is 1 + `max_retries`** (the original run plus `max_retries` retries). ^[workload-yaml-reference-databricks-on-aws.md]

### `timeout_minutes`

The **`timeout_minutes`** field sets a wall‑clock time limit for each individual attempt. If a single attempt runs longer than this limit, the runtime terminates that attempt and (if `max_retries` permits) starts a new one. ^[workload-yaml-reference-databricks-on-aws.md]

- **Type:** integer
- **Default:** no timeout (the job runs indefinitely)
- **The total wall‑clock budget** for the entire job is `timeout_minutes × (1 + max_retries)`. ^[workload-yaml-reference-databricks-on-aws.md]

## Example Configuration

```yaml
experiment_name: reliable-training
environment:
  dependencies:
    - torch
    - transformers
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    git:
      branch: main
command: torchrun --nproc_per_node=8 train.py
max_retries: 2
timeout_minutes: 90
```

^[workload-yaml-reference-databricks-on-aws.md]

In this example, if the workload fails, it is retried twice. Each attempt has 90 minutes to complete — the total wall‑clock budget is 90 × 3 = 270 minutes. ^[workload-yaml-reference-databricks-on-aws.md]

## Relationship Between Retries and Timeouts

The runtime treats `max_retries` and `timeout_minutes` as independent but complementary controls: ^[workload-yaml-reference-databricks-on-aws.md]

- **`max_retries`** governs the *number* of attempts.
- **`timeout_minutes`** governs the *duration* of each attempt.

A job that exceeds its per‑attempt timeout counts as a failed attempt and consumes one of the retry slots. ^[workload-yaml-reference-databricks-on-aws.md]

## Use Cases

Job reliability configuration is particularly valuable for:

- **Long‑running distributed training jobs** that are susceptible to node failures or preemption in serverless GPU environments. ^[workload-yaml-reference-databricks-on-aws.md]
- **[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)** or **[Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)]]**-based workloads where a single node failure causes the entire job to stall.
- **Multi‑node training** where network errors or spot instance terminations can interrupt intermediate attempts. ^[workload-yaml-reference-databricks-on-aws.md]

## Related Concepts

- Workload YAML reference — Full specification of all YAML fields for [AI Runtime](/concepts/ai-runtime.md) workloads.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command‑line interface (`air`) that executes these configurations.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The infrastructure layer that provides the GPU nodes for these jobs.
- Cost attribution — The `usage_policy_id` field that applies budget policies to the same YAML configuration.
- Custom Hyperparameters (HYPERPARAMETERS_PATH)|Custom hyperparameters — Another YAML field that passes structured parameters via `HYPERPARAMETERS_PATH`.

## Sources

- workload-yaml-reference-databricks-on-aws.md

# Citations

1. [workload-yaml-reference-databricks-on-aws.md](/references/workload-yaml-reference-databricks-on-aws-d459ba00.md)
