---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dfb4759db14975f13ba634cf9c0196bc61839f21038df6d13be784b411f004e7
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-registry
    - Prompt Registration
    - Workspace Prompt Registry
  citations:
    - file: filename.md
    - file: source-a.md
    - file: source-b.md
    - file: filename.md:START-END
    - file: filename.md#LSTART-LEND
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: data-profiling-metric-tables-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Prompt Registry
description: A centralized system for registering, versioning, and managing prompt templates used in GenAI applications, with support for tracking changes via commit messages.
tags:
  - mlflow
  - prompt-management
  - genai
timestamp: "2026-06-19T18:43:08.798Z"
---

You are a wiki author. Write a clear, well-structured markdown page about "Prompt Registry".
Draw facts only from the provided source material.
Include a ## Sources section at the end listing the source document.
Suggest wikilinks to related concepts where appropriate.
Write in a neutral, informative tone. Be concise but thorough.

Source attribution: at the end of each prose paragraph, append a citation
marker showing which source file(s) the paragraph drew from.
Format: ^[filename.md] for single-source, ^[source-a.md, source-b.md] for multi-source.
When a single sentence makes a specific factual claim and you can identify the
exact line range it came from, you may use the claim-level form
^[filename.md:START-END] (or ^[filename.md#LSTART-LEND]) at the end of that
sentence — START and END are 1-indexed line numbers in the source file.
Paragraph-level citations remain the default; only switch to claim-level form
when it materially improves verifiability and the line range is unambiguous.
Place citations only at the end of prose paragraphs or sentences — not on
headings, list items, or code blocks.
Source filenames are visible as `--- SOURCE: filename.md ---` headers in the content below.

If a paragraph is your inference rather than a direct extraction, leave it
uncited — downstream lint rules will count uncited paragraphs as 'inferred'
to compute the page's provenance metadata.



Related wiki pages for cross-referencing:

---
title: 20B to 120B+ Parameter Model Training
summary: The parameter range where FSDP is particularly useful, enabling training of models between 20 billion and 120+ billion parameters
sources:
  - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - model-scaling
  - large-language-models
  - distributed-training
aliases:
  - 20b-to-120b-parameter-model-training
  - 2T1PMT
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

Here is the wiki page for "20B to 120B+ Parameter Model Training", written based solely on the provided source material.

---

## 20B to 120B+ Parameter Model Training

**20B to 120B+ Parameter Model Training** refers to the specific techniques and infrastructure required to train large language models (LLMs) and other deep learning models that contain between 20 billion and over 120 billion parameters. Due to their immense size, these models cannot fit into the memory of a single GPU, requiring specialized distributed training strategies.

### Overview

Training models in the 20B to 120B+ parameter range necessitates advanced memory optimization techniques. Standard data parallelism is often insufficient because even a single copy of the model parameters, gradients, and optimizer states exceeds the memory capacity of a single GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Recommended Approach: Fully Sharded Data Parallel (FSDP)

The primary recommended approach for training models of this scale is [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). FSDP shards model parameters, gradients, and optimizer states across multiple GPUs. This sharding significantly reduces the per-GPU memory footprint, enabling the training of very large models that would otherwise be impossible. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

FSDP offers a better trade-off for memory efficiency compared to standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md). While DDP is simpler for models that fit in a single GPU, FSDP becomes the necessary choice for models that do not. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Alternative Approaches

For models that require even more advanced memory optimization features, practitioners may consider alternatives like [DeepSpeed](/concepts/deepspeed.md), which provides additional strategies beyond what FSDP offers out-of-the-box. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### When to Use Each Strategy

- **DDP:** Best suited for models that fit within a single GPU's memory. It is simpler to implement but offers no memory efficiency improvements for the model itself. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **FSDP:** The standard choice for training models in the 20B to 120B+ parameter range to overcome single-GPU memory limitations. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **DeepSpeed:** Considered when more sophisticated memory optimization features beyond FSDP are required. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

### Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md


---

---
title: 30-Day Lookback Window Limitation
summary: For time series or inference profiles, the profile looks back 30 days from when it is created, which may cause the first analysis to include a partial window (e.g., cutting mid-week or mid-month).
sources:
  - data-profiling-metric-tables-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T18:07:30.341Z"
updatedAt: "2026-06-19T18:07:30.341Z"
tags:
  - data-profiling
  - limitations
  - time-series
aliases:
  - 30-day-lookback-window-limitation
  - 3LWL
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 1
---

# 30-Day Lookback Window Limitation

The **30-Day Lookback Window Limitation** is a property of the data profiling logic on Databricks that restricts the time window used for computing statistics in Time Series Analysis and [Inference Log Analysis](/concepts/inferencelog-analysis.md) profiles. When a profile is created or refreshed, the system computes metrics only from data that falls within the 30 days immediately preceding the profile creation time. This lookback is built into the metric computation for both the [Profile Metrics Table](/concepts/profile-metrics-table.md) and the [Drift Metrics Table](/concepts/drift-metrics-table.md). ^[data-profiling-metric-tables-databricks-on-aws.md]

## Effect on the First Analysis Window

Because the profile looks back exactly 30 days from the time of creation, the first analysis window may be a *partial window*. For example, if the aggregation granularity is weekly and the 30‑day cutoff falls in the middle of a previous week, only the portion of that week that lies within the 30‑day limit is included; the full week is not used. This partial‑window behavior affects **only the first analysis** after the profile is created. Subsequent refreshes will have complete windows because the lookback boundary moves forward with the profile creation time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Context and Applicability

The 30‑day lookback window is applied when the profile type is `TimeSeries` or `InferenceLog`. For `Snapshot` analysis, the lookback does not apply because the time window is a single point in time. Understanding this limitation is important when querying metric tables directly: the metrics for the first window may be based on a shorter time span than the requested granularity. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, time window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics tracking distribution changes over time.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – A profile type for monitoring model predictions.
- Time Series Analysis – A profile type for monitoring data over continuous time windows.
- Snapshot Analysis – A profile type with no lookback window.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md


---

---
title: 30-Day Lookback Window
summary: A profiling constraint where for time series or inference profiles, the analysis looks back 30 days from profile creation, potentially causing partial windows in the first analysis.
sources:
  - data-profiling-metric-tables-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:43:57.264Z"
updatedAt: "2026-06-19T14:43:57.264Z"
tags:
  - databricks
  - data-profiling
  - limitations
aliases:
  - 30-day-lookback-window
  - 3LW
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# 30-Day Lookback Window

The **30-Day Lookback Window** is a default time boundary applied during data profiling for Time Series Analysis and [Inference Log Analysis](/concepts/inferencelog-analysis.md) on Databricks. When a profile is created or refreshed, the system computes statistics only from data that falls within the 30 days immediately preceding the profile creation time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Effect on the First Analysis Window

Because the profile looks back exactly 30 days from the current time, the first analysis window may be a partial window. For example, if the profile is created on a Wednesday and the aggregation granularity is weekly, the 30‑day cutoff might fall in the middle of a previous week. In that case, only the portion of the week that lies within the 30‑day limit is included in the calculation; the full week is not used. ^[data-profiling-metric-tables-databricks-on-aws.md]

This partial‑window behavior applies only to the **first** analysis after the profile is created. Subsequent refreshes will have complete windows because the lookback boundary moves forward with the profile creation time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Context and Relevance

The 30‑day lookback window is built into the metric computation logic for both the [Profile Metrics Table](/concepts/profile-metrics-table.md) and the [Drift Metrics Table](/concepts/drift-metrics-table.md) when the profile type is `TimeSeries` or `InferenceLog`. It ensures that statistics are computed over a consistent, rolling historical period, but it introduces the partial‑window edge case for the initial analysis. ^[data-profiling-metric-tables-databricks-on-aws.md]

Users who query metric tables directly should be aware that the first window’s metrics may be based on a shorter time span than the requested granularity. For `Snapshot` analysis, the lookback window does not apply because the time window is a single point in time. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, time window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics that track distribution changes over time.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – A profile type for monitoring model predictions and accuracy.
- Time Series Analysis – A profile type for monitoring data over continuous time windows.
- [Data Slicing](/concepts/data-slicing-expressions.md) – Metrics are computed for data slices defined by slicing expressions.
- [Baseline Table](/concepts/baseline-table.md) – An optional reference used to compute baseline drift.

## Sources

- data-profiling-metric-tables-databricks-on-aws.md


---

---
title: 403 PERMISSION_DENIED Serverless Budget Policy Error
summary: An error that occurs when a workspace disables the default serverless budget policy and no fallback policy is available for MLflow serverless workloads.
sources:
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:08:33.206Z"
updatedAt: "2026-06-18T11:08:33.206Z"
tags:
  - databricks
  - error
  - troubleshooting
  - mlflow
aliases:
  - 403-permission_denied-serverless-budget-policy-error
  - 4PSBPE
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# 403 PERMISSION_DENIED Serverless Budget Policy Error

The **403 PERMISSION_DENIED Serverless Budget Policy Error** occurs when [MLflow](/concepts/mlflow.md) attempts to run a serverless workload — such as a scheduled scorer, synthetic evaluation set generation, or agent evaluation — against an experiment, but the workspace's default serverless budget policy is disabled and no alternative policy has been assigned to the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Error Message

When this error occurs, MLflow returns the following message:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Cause

By default, serverless workloads created by MLflow use the workspace's default serverless budget policy. If the workspace disables the default policy — for example, when each user and service principal must select a dedicated policy — MLflow cannot pick a fallback. This results in a permission denied error when attempting to register a scorer or run an evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Affected workloads include:

- Scheduled scorers (production monitoring)
- Synthetic evaluation set generation
- Agent evaluation

## Solution

Set a serverless budget policy on the MLflow experiment to control which policy MLflow uses for serverless workloads it runs against that experiment. MLflow will then use the specified policy for every serverless workload it creates for the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Requirements

Users and service principals must have permission to use the budget policy they want to set. They can only assign a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Budget Policy in the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow will use this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Budget Policy with the API

Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag on the experiment: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads from the experiment (such as `Scorer.register()`) use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To find the ID of a budget policy, see the documentation on attribute usage with serverless usage policies. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The control mechanism for serverless workload spending
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations
- [Production Monitoring](/concepts/production-monitoring.md) — Scheduled scoring workflows affected by this policy
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow affected by this policy
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) — Another affected workload type

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md


---

---
title: 8xH100 Single-Node Configuration
summary: A Databricks Serverless GPU configuration providing 8 H100 GPUs on a single node for distributed workloads
sources:
  - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:44:59.232Z"
updatedAt: "2026-06-19T10:44:59.232Z"
tags:
  - databricks
  - gpu
  - configuration
  - distributed-computing
aliases:
  - 8xh100-single-node-configuration
  - 8SC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# 8xH100 Single-Node Configuration

**8xH100 Single-Node Configuration** refers to a serverless GPU compute setup on Databricks that provisions eight NVIDIA H100 80GB HBM3 GPUs on a single compute node. This configuration is designed for large model training workloads that benefit from high floating-point operations per second (FLOPS) and high-bandwidth memory (HBM). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Overview

The 8xH100 single-node configuration is available through Databricks Serverless GPU compute. When selected, a notebook session connects to eight H100 GPUs running on a single node, providing 640 GB of total GPU memory (8 × 80 GB) and substantial compute throughput for distributed training tasks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Selection

To use this configuration from a Databricks notebook:

1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab on the right panel, select **8xH100** for your accelerator.
3. Choose the **AI v5** environment, which contains all required libraries for running distributed GPU workloads.
4. Click **Apply**.

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks

# Citations

1. filename.md
2. source-a.md
3. source-b.md
4. filename.md:START-END
5. filename.md#LSTART-LEND
6. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
7. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
8. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
9. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
