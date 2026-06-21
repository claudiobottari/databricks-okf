---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7f01383a092de26ca6e2b62594242ca30c43fea78e103c683cc26e19989024e
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - large-language-models-llms-on-databricks
    - LLM(OD
    - Large Language Models on Databricks
    - LLM (Large Language Model)
    - LLMOps
    - Large Language Model (LLM)
    - Large Language Models
    - Large Language Models (LLMs)
    - Large Language Models (LLMs) on AI Runtime
    - Large Language Models (LLMs)|large language model
    - Large language models (LLMs)
    - Large language models and generative AI on Databricks
    - large language model
    - large language models
    - large language models (LLMs)
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Large language models (LLMs) on Databricks
description: Notebook examples for fine-tuning large language models on Databricks AI Runtime, including parameter-efficient methods.
tags:
  - databricks
  - llm
  - fine-tuning
  - notebooks
timestamp: "2026-06-19T22:04:13.777Z"
---

# Large language models (LLMs) on Databricks

Databricks provides a variety of tools and infrastructure for working with large language models (LLMs), including fine-tuning, distributed training, evaluation, and production monitoring. These capabilities are built on the Databricks AI Runtime, serverless GPU compute, and MLflow integration.

## AI Runtime for LLMs

The AI Runtime includes example notebooks for fine-tuning large language models, including parameter-efficient methods. These examples are part of the **GPU LLM** notebook collection available in the AI Runtime examples documentation. ^[ai-runtime-example-notebooks-databricks-on-aws.md] The AI Runtime for single-node tasks is in **Public Preview**, while the distributed training API for multi‑GPU workloads remains in **Beta**. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Serverless GPU Compute for LLM Training

To train LLMs, Databricks offers serverless GPU compute with H100 GPUs. An **8xH100 Single-Node Configuration** provides eight NVIDIA H100 80GB HBM3 GPUs on a single node, delivering 640 GB of total GPU memory and high FLOPS for large model training. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md] This configuration is selected from the notebook compute selector by choosing **Serverless GPU**, then the **8xH100** accelerator, and the **AI v5** environment. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md] H100 GPUs are recommended for LLM training tasks where high throughput and large memory are needed. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs on a single node, enabling distributed training code that uses local and global GPU ranks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Training Large LLMs (20B to 120B+ Parameters)

For training models between 20 billion and over 120 billion parameters, standard data parallelism is insufficient because model parameters, gradients, and optimizer states exceed the memory of a single GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md] The recommended approach is **Fully Sharded Data Parallel (FSDP)**, which shards these components across multiple GPUs to reduce per‑GPU memory footprint. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

Alternatives to FSDP include **DeepSpeed**, which offers additional memory optimization features beyond FSDP. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md] The choice between FSDP, DeepSpeed, and standard Distributed Data Parallel (DDP) depends on model size and memory requirements.

## MLflow Integration for LLM Workflows

MLflow is tightly integrated with LLM workflows on Databricks, enabling experiment tracking, evaluation, and production monitoring. Serverless workloads created by MLflow—such as scheduled scorers for production monitoring, synthetic evaluation set generation, and agent evaluation—require a serverless budget policy to be assigned to the MLflow experiment. If the default budget policy is disabled and no alternative is set, MLflow returns a **403 PERMISSION_DENIED Serverless Budget Policy Error**. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To resolve this, users can set a budget policy via the experiment UI or by using `mlflow.set_experiment_tag()` with the key `mlflow.workload_creation_policy_id`. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md] This policy controls which budget policy MLflow uses for all serverless workloads created for that experiment, including those related to LLM evaluation and monitoring. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The runtime environment for ML workloads on Databricks.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On‑demand GPU resources provisioned without managing clusters.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific H100 GPU configuration for LLM training.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Sharding strategy for training models with 20B+ parameters.
- [DeepSpeed](/concepts/deepspeed.md) – Alternative distributed training library with advanced memory optimization.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Simpler parallelism strategy for models that fit in a single GPU.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational unit for tracking LLM runs and evaluations.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Controls spending for serverless workloads.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
3. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
4. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
