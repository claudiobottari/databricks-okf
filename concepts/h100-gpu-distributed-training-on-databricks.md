---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb158b0e6919c637ea6181f91cb93310e2c374dd98c3806be16cee121100dc88
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - h100-gpu-distributed-training-on-databricks
    - HGDTOD
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: H100 GPU distributed training on Databricks
description: Pattern for leveraging H100 GPUs in multi-node distributed training workloads on Databricks AI Runtime, supporting both FSDP and Ray Train backends.
tags:
  - gpu
  - databricks
  - distributed-training
  - infrastructure
timestamp: "2026-06-18T10:43:04.390Z"
---

# H100 GPU distributed training on Databricks

**H100 GPU distributed training on Databricks** enables running multi-node, multi-GPU machine learning workloads using NVIDIA H100 accelerators on the [AI Runtime](/concepts/ai-runtime.md) serverless GPU compute platform. Workloads are submitted through the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) using YAML-based configuration, with support for popular distributed training frameworks including PyTorch FSDP and Ray Train. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Supported distributed training patterns

Databricks supports several distributed training frameworks on H100 GPUs through AI Runtime: ^[ai-runtime-cli-examples-databricks-on-aws.md]

- **PyTorch Fully Sharded Data Parallel (FSDP)**: Used for multi-node LLM fine-tuning, such as supervised fine-tuning of Llama-3.1-8B across 16 H100 GPUs (2 nodes) using `torchrun`. This approach shards model parameters, gradients, and optimizer states across all GPUs to handle large models that wouldn't fit on a single GPU. ^[ai-runtime-cli-examples-databricks-on-aws.md]
- **Ray Train**: Used for distributed data-parallel fine-tuning with Ray Train's `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Workload configuration

H100 distributed training workloads are defined in YAML configuration files that specify compute requirements, code source, environment dependencies, and the training command. The compute section specifies the number of accelerators and accelerator type: ^[ai-runtime-cli-examples-databricks-on-aws.md]

```yaml
compute:
  num_accelerators: 16
  accelerator_type: GPU_H100
```

For multi-node training, the `num_accelerators` value is distributed across nodes based on the accelerator type. For example, 16 H100 GPUs with 8 GPUs per node results in a 2-node cluster configuration. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Training workflow

### Submit a training workload

Training workloads are submitted using the `air run` command with a YAML configuration file: ^[ai-runtime-cli-examples-databricks-on-aws.md]

```bash
air run --file train.yaml
```

The CLI uploads local code, submits the job, and returns a run ID for tracking. To watch logs until completion, use the `--watch` flag. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Monitor training

Track training progress and inspect runs using: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

- `air get run <run-id>` — Check status and get links to the MLflow experiment and run
- `air logs <run-id>` — Stream logs from the default node 0
- `air logs <run-id> --node 2` — Stream logs from a specific node in multi-node workloads
- `air logs <run-id> --download-to ./logs/` — Download logs to a local directory

### Cancel a workload

Running workloads can be cancelled: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air cancel <run-id>
```

## Common patterns

- **Override compute configuration from the command line**: Use `--override` to change the number of accelerators or other parameters without modifying the YAML file: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

  ```bash
  air run --file train.yaml --override compute.num_accelerators=32
  ```

- **Validate configuration before submission**: Use `--dry-run` to check the configuration without actually submitting the workload. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

- **Idempotent submissions**: Use `--idempotency-key` to make submissions safely retryable. If the same key has been used before, the existing run is returned rather than creating a new one. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Integration with MLflow

Every training run submitted through AI Runtime is automatically tracked in an [MLflow](/concepts/mlflow.md) experiment. The experiment name is specified in the YAML configuration file: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
experiment_name: my-training-experiment
```

The run captures metrics, parameters, artifacts, and logs, all viewable in the workspace MLflow UI. For workloads that checkpoint model weights, checkpoints can be stored in a [Unity Catalog](/concepts/unity-catalog.md) volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## See also

- [AI Runtime](/concepts/ai-runtime.md) — The serverless GPU compute platform
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The `air` command-line tool for submitting workloads
- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md) — Full CLI documentation
- AI Runtime CLI quickstart — Getting started guide
- Multi-GPU workload — In-notebook Python API alternative
- Track runs with MLflow and the Jobs run page — Monitoring and tracking submitted runs
- [MLflow](/concepts/mlflow.md) — Experiment tracking platform
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance for AI assets

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md
- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
2. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
