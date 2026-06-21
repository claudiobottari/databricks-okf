---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 77ccb374f0280160add61f2e88e2caf487ad962076b0257ff3eee9ed0759e4ab
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workload-yaml-configuration-trainyaml
    - WYC(
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
    - file: ai-runtime-cli-databricks-on-aws.md
title: Workload YAML configuration (train.yaml)
description: Pattern for defining distributed training workloads declaratively using a train.yaml file submitted via `air run -f train.yaml`.
tags:
  - configuration
  - yaml
  - workload-management
timestamp: "2026-06-18T10:43:50.114Z"
---

# [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) (train.yaml)

The **workload YAML configuration** (`train.yaml`) is the declarative configuration file used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) to define and submit distributed training workloads to the AI Runtime serverless GPU compute platform. The YAML file describes the complete job specification, including compute resources, code source, environment dependencies, and the command to execute. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Structure overview

A `train.yaml` file consists of several top-level sections that collectively define the workload. The minimal configuration requires an `experiment_name`, a `compute` spec, and a `command`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Top-level fields

### `experiment_name`

The name of the [MLflow](/concepts/mlflow.md) experiment that will track the run. This is a required field. All metrics, parameters, artifacts, and logs from the training run are captured under this experiment and are viewable in the workspace MLflow UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### `compute`

Defines the hardware resources for the workload. The compute block specifies the number and type of accelerators (GPUs) to allocate. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
```

The `num_accelerators` field specifies how many accelerators the workload requires. The `accelerator_type` field specifies the GPU hardware type, such as `GPU_1xA10` for a single A10 GPU or `GPU_1xH100` for a single H100 GPU. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### `command`

The shell command to execute on the provisioned compute. This is a required field. For workloads that include code files, Databricks recommends using the `$CODE_SOURCE_PATH` variable instead of hardcoding a path to your code directory. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
command: python $CODE_SOURCE_PATH/train.py
```

### `environment`

Defines the runtime environment and Python dependencies for the workload. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
```

The `version` field specifies the [Serverless environment versions|serverless environment version](/concepts/serverless-environment-versioning.md) and is optional, defaulting to `'4'`. The `dependencies` field lists Python packages to install, using standard pip package names. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### `code_source`

Specifies how the workload code is provided to the runtime. The most common type is `snapshot`, which uploads local code from your filesystem. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: .
```

The `root_path` field under `snapshot` specifies the local directory to upload. The code is uploaded to the AI Runtime when you submit the workload with `air run`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Minimal example

A complete minimal `train.yaml` that runs a simple echo command on a single A10 GPU:

```yaml
experiment_name: my-first-air-run
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "hello AIR!"
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Example with code and dependencies

A more realistic example that trains a model using local code with Python dependencies, assuming a directory structure where `train.yaml` and `train.py` are in the same folder:

```yaml
experiment_name: my-first-air-run
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
code_source:
  type: snapshot
  snapshot:
    root_path: .
command: python $CODE_SOURCE_PATH/train.py
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Project directory layout

When using a `snapshot` code source, your project directory typically contains the YAML configuration file alongside your training scripts:

```text
my-project/
├── train.yaml
└── train.py
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Submitting the workload

Submit a workload defined in a YAML file using the `air run` command:

```bash
air run --file train.yaml
```

To stream logs to the terminal until the run completes, add the `--watch` flag:

```bash
air run --file train.yaml --watch
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Overriding YAML fields

You can override specific YAML fields at submission time without modifying the file, using the `--override` flag:

```bash
air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120
```

This allows you to reuse the same YAML file with different resource allocations or parameters. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Validation without submission

Use the `--dry-run` flag to validate the configuration without actually submitting the workload:

```bash
air run --file train.yaml --dry-run
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Idempotency

To make a submission safely retryable, use the `--idempotency-key` flag with a unique key. If the same key has been used before, the existing run is returned rather than creating a new one:

```bash
air run --file train.yaml --idempotency-key my-unique-key
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related commands

After submitting a workload, you can manage it with other `air` CLI commands:

| Command | Purpose |
|---|---|
| `air get run <run-id>` | Display metadata, status, and configuration for a specific run |
| `air list runs` | List recent runs (optionally only active ones) |
| `air logs <run-id>` | Stream or download logs for a run |
| `air cancel <run-id>` | Cancel a running workload |

^[ai-runtime-cli-quickstart-databricks-on-aws.md, ai-runtime-cli-databricks-on-aws.md]

## See also

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface for submitting workloads
- AI Runtime CLI quickstart — Getting started guide
- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md) — Full list of available commands
- [AI Runtime CLI global flags](/concepts/ai-runtime-cli-global-flags.md) — Shared flags across all `air` commands
- [AI Runtime](/concepts/ai-runtime.md) — The underlying serverless GPU compute platform
- Track runs with MLflow and the Jobs run page — Monitoring and tracking submitted runs
- Multi-GPU workload — The in-notebook Python API alternative
- [Serverless environment versions](/concepts/serverless-environment-versioning.md) — Available environment versions for the `environment.version` field
- [MLflow](/concepts/mlflow.md) — Experiment tracking integration

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md
- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
2. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
