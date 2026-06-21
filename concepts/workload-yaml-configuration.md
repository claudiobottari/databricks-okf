---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 547fff29cd5c9afbec987d1aec09962e7ba72e179694adffb27d59b648d4fcc2
  pageDirectory: concepts
  sources:
    - workload-yaml-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workload-yaml-configuration
    - WYC
    - Workload YAML configuration reference
    - Workload YAML
    - Workload YAML Reference
    - Workload YAML reference|YAML configuration
    - Workload YAML reference|workload YAML configuration
    - workload YAML
  citations:
    - file: workload-yaml-reference-databricks-on-aws.md
    - file: distributed-training-with-ray-train-databricks-on-aws.md
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Workload YAML Configuration
description: The YAML schema accepted by `air run --file` to define GPU training jobs, with fields for experiment name, environment, compute, code source, command, parameters, secrets, and reliability settings.
tags:
  - yaml
  - configuration
  - databricks
timestamp: "2026-06-19T23:27:07.459Z"
---

# Workload YAML Configuration

**Workload YAML Configuration** is a declarative format used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) to define training jobs. The configuration is written in a `.yaml` file and specifies the experiment, compute resources, environment, code source, and command to execute. ^[workload-yaml-reference-databricks-on-aws.md]

## Minimal Configuration

The simplest workload YAML requires an `experiment_name`, a `compute` block, and a `command`. The following example runs a one‑off shell command:

```yaml
experiment_name: my-training
environment:
  dependencies:
    - [[mlflow|MLflow]]
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "Hello World"
```

When submitted with `air run --file train.yaml`, the system creates a run in the [MLflow Experiments|MLflow experiment](/concepts/mlflow-experiment.md) named in `experiment_name`. ^[workload-yaml-reference-databricks-on-aws.md]

## Core Concepts

Most training configurations include five components: ^[workload-yaml-reference-databricks-on-aws.md]

| Field | Required | Description |
|-------|----------|-------------|
| `experiment_name` | Yes | Creates or appends to an [MLflow Experiments|MLflow experiment](/concepts/mlflow-experiment.md). |
| `environment` | No | Python dependencies and base environment. |
| `compute` | Yes | GPU resources (type and count). |
| `command` | Yes | The bash command used to launch training. |
| `code_source` | No | Path to training code, made available remotely. |

### Your First Training Job

```yaml
experiment_name: simple-training
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
command: torchrun --nproc_per_node=8 $CODE_SOURCE_PATH|code_source_path|$CODE_SOURCE_PATH/train.py
```

In this configuration, `environment` installs Python dependencies, `compute` allocates one H100 node (8 GPUs), `code_source` uploads the `repo` folder (available at `$CODE_SOURCE_PATH`), and `command` runs `train.py` across the 8 H100 GPUs. ^[workload-yaml-reference-databricks-on-aws.md]

## Python Dependencies

List dependencies under `environment.dependencies`:

```yaml
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
```

`environment.version` selects the [Serverless GPU Environment](/concepts/serverless-gpu-environment.md) version](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/). It is optional and defaults to `"4"`. ^[workload-yaml-reference-databricks-on-aws.md]

### Dependency Format

The dependency list follows the [Databricks Base Environment Specification](https://docs.databricks.com/aws/en/admin/workspace-settings/base-environment#example-environment-specification). Each entry is a pip-style package spec. The list also accepts:

- **Requirements files**: `-r '/Workspace/Shared/requirements.txt'` (environment variables such as `$HOME` are expanded).
- **Wheels**: an absolute path to a `.whl` file, e.g. `/Workspace/Shared/path/to/simplejson-3.19.3-py3-none-any.whl`.
- **Index URLs**: `--index-url https://pypi.org/simple`.

```yaml
environment:
  version: '4'
  dependencies:
    - --index-url https://pypi.org/simple
    - -r '/Workspace/Shared/requirements.txt'
    - my-library==6.1
    - /Workspace/Shared/path/to/simplejson-3.19.3-py3-none-any.whl
```

Dependencies are installed with [uv](https://docs.astral.sh/uv/). Supported pip-style flags include `--index-url`, `--extra-index-url`, `--find-links`, `--no-deps`, `--no-build-isolation`, `--no-cache-dir`, and `--force-reinstall`. ^[workload-yaml-reference-databricks-on-aws.md]

## Code Sources

The `code_source` block uploads local code. The `type` must be `snapshot`.

### Snapshot (Working Tree)

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
```

`root_path` is the local directory to snapshot. By default, the working tree is packaged as a plain tarball, including any uncommitted changes. ^[workload-yaml-reference-databricks-on-aws.md]

### Git Repositories: Pin by Branch or Commit

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    git:
      branch: main   # Uses local HEAD of that branch
```

`branch` and `commit` are mutually exclusive. `git.remote` (optional) uses the remote HEAD when set to `true` or a remote name. Without the `git:` block, the working tree is packaged as a plain tarball. ^[workload-yaml-reference-databricks-on-aws.md]

### Non‑git Directories

Omit the `git:` block — it requires `root_path` to be a git repository. Without it, a fresh tarball is uploaded for every run. ^[workload-yaml-reference-databricks-on-aws.md]

### Folder Filtering with `include_paths`

For large monorepos, snapshot only specific folders:

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    include_paths:
      - research/models
      - research/common
      - research/configs
```

Paths must be relative to the repository root (no leading `/`). `..` is not allowed. ^[workload-yaml-reference-databricks-on-aws.md]

### Path Resolution

All paths in the workload YAML are relative to the YAML file unless they are absolute paths. The `$CODE_SOURCE_PATH` environment variable resolves to the remote location of the uploaded directory. ^[workload-yaml-reference-databricks-on-aws.md]

## Environment Variables and Secrets

### Environment Variables

```yaml
environment:
  dependencies:
    - torch
    - transformers
env_variables:
  BATCH_SIZE: '32'
  LEARNING_RATE: '0.001'
```

### Secrets (API Keys, Tokens)

```yaml
secrets:
  HF_TOKEN: 'my_scope/hf_token'
  WANDB_API_KEY: 'my_scope/wandb'
```

Secrets use the format `scope/key` and must be configured in Databricks Secrets. When sharing a YAML template, other users must create their own secrets or have access to the referenced secret. ^[workload-yaml-reference-databricks-on-aws.md]

## Advanced Features

### Custom Hyperparameters

Pass structured configuration to your training script via `HYPERPARAMETERS_PATH`:

```yaml
parameters:
  model:
    name: 'gpt2'
    hidden_size: 768
  training:
    batch_size: 32
    learning_rate: 0.0001
```

Read them in your script:

```python
import os
import yaml
with open(os.environ['HYPERPARAMETERS_PATH']) as f:
    params = yaml.safe_load(f)
learning_rate = params['training']['learning_rate']
```

^[workload-yaml-reference-databricks-on-aws.md]

### Job Reliability

```yaml
max_retries: 2
timeout_minutes: 90
```

If the workload fails, it is retried twice. Each attempt has 90 minutes to complete — the total wall‑clock budget is 90 × 3 = 270 minutes. ^[workload-yaml-reference-databricks-on-aws.md]

### Cost Attribution

Attach a workload to an existing budget policy via `usage_policy_id`:

```yaml
usage_policy_id: abcd123-25b8-3e87-9a2c-f86eb19d101c
```

^[workload-yaml-reference-databricks-on-aws.md]

### [MLflow Run](/concepts/mlflow-run.md) Name

```yaml
mlflow_run_name: 'experiment-001-baseline'
```

^[workload-yaml-reference-databricks-on-aws.md]

## Distributed Training Configurations

Workload YAML supports distributed training across multiple GPUs. For example, fine-tuning with [Ray Train](/concepts/ray-train-resource-allocation.md) across 8 H100 GPUs on a single node uses the `GPU_8xH100` accelerator type: ^[distributed-training-with-ray-train-databricks-on-aws.md]

```yaml
experiment_name: air-ray-train-distributed
environment:
  version: '4'
  dependencies:
    - ray[default,train]>=2.30
    - transformers>=4.45
    - datasets>=3.0
    - fsspec>=2024.6.1
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
code_source:
  type: snapshot
  snapshot:
    root_path: .
command: |
  cd $CODE_SOURCE_PATH|code_source_path|$CODE_SOURCE_PATH
  RAY_HEAD_PORT=6379
  GPUS_PER_NODE=${LOCAL_WORLD_SIZE:-8}
  if [ "${NODE_RANK:-0}" = "0" ]; then
    echo "NODE_RANK=0: starting Ray head with $GPUS_PER_NODE GPU(s)..."
    ray start --head --port=$RAY_HEAD_PORT --num-gpus="$GPUS_PER_NODE" --dashboard-host=0.0.0.0
    python train_ray.py
    ray stop
  else
    echo "NODE_RANK=$NODE_RANK: connecting to Ray head at $MASTER_ADDR:$RAY_HEAD_PORT..."
    for i in $(seq 1 12); do
      if ray start --address="$MASTER_ADDR:$RAY_HEAD_PORT" --num-gpus="$GPUS_PER_NODE" --block 2>/dev/null; then
        break
      fi
      echo "Attempt $i failed, retrying in 5s..."
      sleep 5
    done
  fi
timeout_minutes: 90
env_variables:
  NCCL_SOCKET_IFNAME: eth0
```

In distributed configurations, the `command` block typically starts a cluster manager (such as Ray) on the head node and runs the training script. The inline command includes a worker branch that joins the head, allowing the same YAML to scale to multiple nodes. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Reference

### Supported GPU Types

For accelerator capabilities and recommended use cases, see [Hardware options](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/#hardware-options). ^[workload-yaml-reference-databricks-on-aws.md]

### Optional Fields Summary

| Field | Type | Description |
|-------|------|-------------|
| `environment.version` | string | [Serverless GPU Environment](/concepts/serverless-gpu-environment.md) version (default: `"4"`). |
| `environment.env_variables` | map | Environment variables set on the compute node. |
| `environment.secrets` | map | Databricks secrets (scope/key). |
| `code_source.snapshot.git.branch` | string | Branch name (mutually exclusive with `commit`). |
| `code_source.snapshot.git.commit` | string | Commit SHA (mutually exclusive with `branch`). |
| `code_source.snapshot.git.remote` | bool/string | Use remote HEAD (requires `branch`). |
| `code_source.snapshot.include_paths` | list | Filter included paths (relative to repo root). |
| `parameters` | map | Custom hyperparameters (exposed via `HYPERPARAMETERS_PATH`). |
| `max_retries` | integer | Maximum retry attempts on failure. |
| `timeout_minutes` | integer | Maximum runtime before cancellation. |
| `usage_policy_id` | string | Budget policy ID for cost attribution. |
| `mlflow_run_name` | string | Custom [MLflow Run](/concepts/mlflow-run.md) name. |

^[workload-yaml-reference-databricks-on-aws.md]

## Common Patterns

- **Override YAML fields from the command line**: `air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120`
- **Validate without submitting**: `air run --file train.yaml --dry-run`
- **Idempotent submission**: `air run --file train.yaml --idempotency-key my-unique-key` – if the key has been used before, the existing run is returned instead of creating a new one.

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line tool that consumes workload YAML files
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for training runs
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The compute infrastructure that provisions GPU resources
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific accelerator configuration for distributed training
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Scaling workloads across multiple accelerators
- [Ray Train](/concepts/ray-train-resource-allocation.md) – Distributed training framework used with workload YAML

## Sources

- workload-yaml-reference-databricks-on-aws.md
- distributed-training-with-ray-train-databricks-on-aws.md
- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [workload-yaml-reference-databricks-on-aws.md](/references/workload-yaml-reference-databricks-on-aws-d459ba00.md)
2. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
3. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
