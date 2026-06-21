---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e910b5f5952bc33bc26c5b279019d89719610b1eca02adc5d9434764de8f493
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-environment
    - SGE
    - Serverless Environment
    - Serverless GPU Environments
    - serverless environment
    - Configure the Serverless Environment
    - GPU environment
    - serverless environment library
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Serverless GPU Environment
description: Managed compute environment for AI Runtime workloads specifying num_accelerators, accelerator_type, and environment version for running training jobs
tags:
  - compute
  - gpu
  - infrastructure
timestamp: "2026-06-18T14:22:49.982Z"
---

---

title: Serverless GPU Environment
summary: The compute environment version used by the AI Runtime CLI to run training workloads on Databricks serverless GPU infrastructure.
sources:
  - ai-runtime-cli-quickstart-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - databricks
  - machine-learning
  - ai-runtime-cli
aliases:
  - serverless-gpu-environment
  - SGE
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Serverless GPU Environment

A **Serverless GPU Environment** is a predefined runtime environment version used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) to execute training workloads on Databricks serverless GPU infrastructure. It specifies the set of pre-installed system libraries, drivers, and optimizations available to the training job.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Usage in AI Runtime CLI

When defining a workload in a YAML configuration file (e.g., `train.yaml`), the `environment.version` field selects the serverless GPU environment version. This field is optional; if omitted, it defaults to `'4'`.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
```

The version number determines which system-level components (CUDA drivers, NCCL, etc.) are available. Databricks recommends leaving the environment version unspecified or using the latest stable version unless a specific version is required for compatibility.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Available Versions

For a complete list of supported environment versions and their release notes, see the official [Serverless environment versions](/concepts/serverless-environment-versioning.md) documentation. The AI Runtime CLI quickstart notes that `environment.version` is optional and defaults to `'4'`.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Relationship to AI Runtime CLI

The serverless GPU environment is one of several configuration components in an AI Runtime CLI workload. It works together with:

- `compute` block – specifies hardware (e.g., number of accelerators, accelerator type like `GPU_1xA10`)
- `command` – the script or command to run
- `code_source` – optional code upload
- `dependencies` – Python packages installed on top of the environment

The environment version is independent of the user’s Python dependencies; the system environment is provisioned first, and then the listed packages are installed.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – the command-line tool that uses this environment
- Workload YAML reference – full field documentation for submitting jobs
- [Serverless environment versions](/concepts/serverless-environment-versioning.md) – detailed version history and changelogs
- [MLflow experiments](/concepts/mlflow-experiment.md) – runs are tracked in an MLflow experiment from the YAML config

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
