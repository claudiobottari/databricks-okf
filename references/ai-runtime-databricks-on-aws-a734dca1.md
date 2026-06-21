---
title: AI Runtime | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/
ingestedAt: "2026-06-18T08:08:01.412Z"
---

Public Preview

AI Runtime for single-node tasks is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). The distributed training API for multi-GPU workloads remain in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

## Overview of AI Runtime[​](#overview-of-ai-runtime "Direct link to overview-of-ai-runtime")

AI Runtime is a compute offering at Databricks intended for [deep learning](https://www.databricks.com/blog/what-is-deep-learning) workloads, and brings GPU support for Databricks Serverless. You can use AI Runtime to train and fine-tune custom models using your favorite frameworks and get state-of-the-art efficiency, performance, and quality. For an overview of how [serverless compute](https://docs.databricks.com/aws/en/getting-started/high-level-architecture#serverless-compute-plane) fits into the Databricks architecture, see [Serverless workspace architecture](https://docs.databricks.com/aws/en/getting-started/high-level-architecture#serverless-workspace-architecture).

### Key features[​](#key-features "Direct link to Key features")

*   **Fully managed GPU infrastructure** — Serverless, flexible access to GPUs and no cluster configuration, driver selection, or autoscaling policies to manage.
*   **A runtime dedicated for deep learning** — Choose either a minimal default base environment for maximum flexibility over dependencies or a full-featured AI environment pre-loaded with popular ML frameworks.
*   **Natively integrated** across notebooks, jobs, Unity Catalog, and MLflow for seamless development, data access, and experiment tracking.

### Hardware options[​](#hardware-options "Direct link to Hardware options")

All AI Runtime accelerators provision a single node. The number of GPUs on that node depends on the accelerator type:

Beta

The 1xH100 accelerator is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). To use it, a workspace admin must enable the **AI Runtime Beta Feature** preview from the **Previews** page. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).

### Recommended use cases[​](#recommended-use-cases "Direct link to Recommended use cases")

Databricks recommends AI Runtime for any custom model training use cases that involve deep learning, large-scale classic workloads, or GPUs.

For example:

*   LLM fine-tuning (LoRA, QLoRA, full fine-tuning)
*   Computer vision (object detection, image classification)
*   Deep-learning-based recommender systems
*   Reinforcement learning
*   Deep-learning-based time series forecasting

### Requirements[​](#requirements "Direct link to Requirements")

*   A workspace in one of the following AWS-supported regions:
    *   `us-west-2`
    *   `us-west-1`
    *   `us-east-1`
    *   `us-east-2`
    *   `ca-central-1`
    *   `sa-east-1`
*   The AI Runtime preview must be enabled via workspace admin settings. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).

### Limitations[​](#limitations "Direct link to Limitations")

*   AI Runtime only supports A10 and H100 accelerators.
*   AI Runtime is **not supported for [compliance security profile](https://docs.databricks.com/aws/en/security/privacy/security-profile) workspaces (like HIPAA or PCI)**. Processing regulated data is not supported.
*   Adding dependencies using the **Environments** panel is not supported for AI Runtime scheduled jobs. Install dependencies programmatically using `%pip install` in your notebook instead.
*   For scheduled jobs on AI Runtime, auto recovery behavior for incompatible package versions that are associated with your notebook is not supported.
*   The maximum runtime for a workload is seven days. For model training jobs that exceed this limit, implement checkpointing and restart the job once the maximum runtime is reached.
*   AI Runtime provides on-demand access to GPU resources. While this leads to easy, flexible access to GPUs, there may be periods where capacity is constrained or unavailable in your region.
*   AI Runtime leverages cross-region GPUs in certain cases during moments of high demand. There may be egress costs associated with such usage, and cross-region network connectivity might be limited at certain times.

## Connect to AI Runtime[​](#connect-to-ai-runtime "Direct link to connect-to-ai-runtime")

You can connect to AI Runtime interactively from notebooks, schedule notebooks as recurring jobs, or programmatically create jobs using the Jobs API and Databricks Asset Bundles. For step-by-step instructions, see [Connect to AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/connecting).

## Set up environment[​](#set-up-environment "Direct link to Set up environment")

AI Runtime offers two managed Python environments: a minimal default base environment, and a full-featured Databricks AI environment that is pre-loaded with popular ML frameworks like PyTorch and Transformers. For details on choosing an environment, caching behavior, importing custom modules, and known limitations, see [Set up your environment](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment).

## Read in data[​](#read-in-data "Direct link to Read in data")

Understanding how data access works on AI Runtime is essential for a smooth experience. For details, see [Load data on AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/dataloading).

## Distributed training[​](#-distributed-training "Direct link to -distributed-training")

AI Runtime supports distributed training across multiple GPUs on the single node your notebook is connected to. Using the `@distributed` decorator from the `serverless_gpu` Python API (Beta), you can launch multi-GPU workloads with PyTorch DDP, FSDP, or DeepSpeed with minimal configuration. For details, see [Multi-GPU workload](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/distributed-training).

## Experiment tracking and observability[​](#experiment-tracking-and-observability "Direct link to Experiment tracking and observability")

For MLflow integration, viewing logs, and model checkpoint management, see [Experiment tracking and observability](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability).

## Genie Code for deep learning[​](#genie-code-for-deep-learning "Direct link to Genie Code for deep learning")

Genie Code supports deep learning workloads on AI Runtime. It can help with generating training code, resolving library installation errors, suggesting optimizations, and debugging common issues. See [Use Genie Code for data science](https://docs.databricks.com/aws/en/notebooks/ds-agent).

## Guides[​](#guides "Direct link to Guides")

For migration from classic workloads, example notebooks, and troubleshooting, see [User guides for AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides).
