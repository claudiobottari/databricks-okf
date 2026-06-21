---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aea4e084aa01787b0173c3cc54f0c3f79847fdfb30330a960588941ee35507ee
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - yaml-based-job-configuration-for-training
    - YJCFT
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: YAML-based job configuration for training
description: Pattern of defining distributed training jobs declaratively in YAML files so they can be checked into source control, used by the AI Runtime CLI.
tags:
  - yaml
  - configuration
  - mlops
timestamp: "2026-06-19T13:56:16.044Z"
---

# YAML-based Job Configuration for Training

**YAML-based job configuration for training** refers to the practice of defining distributed GPU training workloads declaratively using YAML files. This approach is supported by the AI Runtime CLI (`air`), which submits and manages training jobs on [AI Runtime](/concepts/ai-runtime.md), the on-demand serverless GPU compute platform. The CLI uses YAML-based job configuration, integrates with [MLflow](/concepts/mlflow.md), and supports workspace-based and git-based code workflows.^[ai-runtime-cli-databricks-on-aws.md]

## Use Cases

Use YAML-based job configuration when you want to:

- Submit GPU training workloads from your laptop and code editor without opening a notebook.
- Define training jobs declaratively in YAML so they can be checked into source control.^[ai-runtime-cli-databricks-on-aws.md]

## How It Works

The `air` command-line interface accepts a YAML file that specifies the training job's parameters, including compute resources, code sources (workspace or git), dependencies, and MLflow tracking settings. The job is then executed on AI Runtime's serverless GPU infrastructure. For in-notebook Python APIs (such as `@distributed` and `@ray_launch`), see Multi-GPU Workload on AI Runtime instead.^[ai-runtime-cli-databricks-on-aws.md]

## Benefits

- **Declarative definition**: Job configuration is written once and can be version-controlled alongside your code.
- **Reproducibility**: The same YAML file can be reused across runs or environments, ensuring consistent training setups.
- **Integration**: YAML files work with the full AI Runtime CLI command set, including run tracking via MLflow and the Jobs run page.^[ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md)
- Workload YAML reference
- AI Runtime CLI quickstart
- [AI Runtime CLI examples](/concepts/ai-runtime-cli.md)
- Track runs with MLflow and the Jobs run page
- [Distributed Training on AI Runtime](/concepts/distributed-training-on-ai-runtime.md)

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
