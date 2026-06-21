---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71ce950f4bafc561cc2d24e26d5099fcfe80a942b4a26be8e758a62fc0cca7d4
  pageDirectory: concepts
  sources:
    - track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
    - workload-yaml-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-runtime-cli-air
    - ARC(
    - AI Runtime (AIR)
    - AI Runtime (air) CLI
  citations:
    - file: track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
    - file: workload-yaml-reference-databricks-on-aws.md
title: AI Runtime CLI (air)
description: Command-line interface for submitting and managing machine learning workloads on Databricks, currently in Beta.
tags:
  - cli
  - databricks
  - workload-management
timestamp: "2026-06-19T23:14:20.924Z"
---

---  
title: [AI Runtime CLI](/concepts/ai-runtime-cli.md) (air)  
summary: A beta command-line interface for submitting and managing AI/ML workloads on Databricks, using YAML-based configuration and integrated with [MLflow Run](/concepts/mlflow-run.md) tracking.  
sources:  
  - track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md  
  - workload-yaml-reference-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-19T22:01:36.448Z"  
updatedAt: "2026-06-19T22:01:36.448Z"  
tags:  
  - cli  
  - databricks  
  - machine-learning  
  - beta  
aliases:  
  - ai-runtime-cli-air  
  - ARC(  
confidence: 1  
provenanceState: extracted  
inferredParagraphs: 0  
---

# [AI Runtime CLI](/concepts/ai-runtime-cli.md) (air)

The **AI Runtime CLI (`air`)** is a Beta command‑line interface for submitting and managing distributed training workloads on [Databricks AI Runtime](/concepts/databricks-ai-runtime.md). Workloads are defined in YAML configuration files and submitted with a single command. The CLI integrates tightly with [MLflow](/concepts/mlflow.md): every submission creates both a [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) run and an [MLflow Run](/concepts/mlflow-run.md), providing built‑in experiment tracking, system metrics, and log streaming. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md, workload-yaml-reference-databricks-on-aws.md]

## [Workload YAML Configuration](/concepts/workload-yaml-configuration.md)

Training jobs are defined in YAML files (e.g., `train.yaml`) and passed to `air run --file`. The ground truth for configuration fields is the in‑CLI help: `air -h config` shows the top‑level structure, and `air -h config.<section>` (for example, `air -h config.environment`) gives per‑section detail. ^[workload-yaml-reference-databricks-on-aws.md]

### Core fields

Most configurations include five components:

1. **`experiment_name`** (Required) – Creates or appends to an [MLflow Experiment](/concepts/mlflow-experiment.md) with this name.
2. **`environment`** (Optional) – Python dependencies, environment variables, and secrets.
3. **`compute`** (Required) – GPU resources (accelerator type and count).
4. **`command`** (Required) – The bash command used to launch training.
5. **`code_source`** (Optional) – Local code to upload and make available on the compute node.

A minimal YAML: ^[workload-yaml-reference-databricks-on-aws.md]

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

### Python dependencies

Dependencies are listed under `environment.dependencies` using pip‑style package specs. The list supports requirements files (`-r /path/requirements.txt`), wheel paths, and index URLs (`--index-url`, `--extra-index-url`, `--find-links`). Per‑dependency flags (`--no-deps`, `--no-build-isolation`, `--no-cache-dir`, `--force-reinstall`) are placed on their own lines before the dependency. Installations use [uv](https://docs.astral.sh/uv/). ^[workload-yaml-reference-databricks-on-aws.md]

```yaml
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
```

### Code sources

The `code_source` block uploads a local directory (plain tarball) or a git repository to the remote node, accessible at the `$CODE_SOURCE_PATH` environment variable. For git repositories, a `git:` block pins code by branch or commit SHA. The `include_paths` field filters which subdirectories are included. ^[workload-yaml-reference-databricks-on-aws.md]

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    git:
      branch: main
```

### Advanced features

- **Environment variables**: `env_variables` map keys to string values.
- **Secrets**: `secrets` map keys to Databricks secret references (e.g., `'my_scope/hf_token'`).
- **Custom parameters**: `parameters` provides structured YAML passed via the `HYPERPARAMETERS_PATH` environment variable.
- **Job reliability**: `max_retries` (each retry is a new [MLflow Run](/concepts/mlflow-run.md)) and `timeout_minutes` set total wall‑clock budget.
- **Cost attribution**: `usage_policy_id` attaches the workload to an existing budget policy.

^[workload-yaml-reference-databricks-on-aws.md]

## Run tracking and [MLflow](/concepts/mlflow.md)

Each `air run` submission creates a single Databricks job run and a single [MLflow Run](/concepts/mlflow-run.md). The `experiment_name` field is required and determines the [MLflow Experiment](/concepts/mlflow-experiment.md). An optional `mlflow_run_name` sets the run name; otherwise it defaults to the experiment name. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

System metrics (GPU, CPU, memory) are captured automatically and viewable on the [MLflow](/concepts/mlflow.md) run’s **System metrics** tab. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

### Logging custom metrics

The platform injects the `MLFLOW_RUN_ID` environment variable into each compute node. For distributed (multi‑node) workloads, all nodes share the same [MLflow Run](/concepts/mlflow-run.md); log from rank 0 only to record each metric once: ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

```python
import os, [[mlflow|MLflow]]

if os.environ.get("RANK", "0") == "0":
    with [[mlflow|MLflow]].start_run(run_id=os.environ["MLFLOW_RUN_ID"]):
        [[mlflow|MLflow]].log_param("learning_rate", 3e-4)
        for step, loss in enumerate(training_losses):
            [[mlflow|MLflow]].log_metric("train_loss", loss, step=step)
```

### Logs and artifacts

Stream or download logs with `air logs <job‑run‑id>`. Use `--node` to target a specific node, and `--download-to` to write logs to a directory. Logs are also available as artifacts on the [MLflow Run](/concepts/mlflow-run.md). ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Commands

The following commands are documented in the provided sources. Run `air <command> --help` for full detail.

| Command | Purpose |
|---|---|
| `air run --file <yaml>` | Submit a workload defined by a YAML file. |
| `air get run <job‑run‑id>` | Show run metadata, status, and configuration; prints clickable links to the job, experiment, and [MLflow Run](/concepts/mlflow-run.md). |
| `air list runs` | List previous runs; filter to find a specific run. |
| `air logs <job‑run‑id>` | Stream or download logs for a run. |
| `air -h config` | Show the YAML configuration reference. |

^[workload-yaml-reference-databricks-on-aws.md, track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Related concepts

- [Workload YAML](/concepts/workload-yaml-configuration.md) – The configuration format for defining [AI Runtime](/concepts/ai-runtime.md) workloads.
- [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) – The runtime environment that executes workloads.
- [MLflow](/concepts/mlflow.md) – Tracking and logging framework integrated with runs.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) – The job system that manages run execution and retries.

## Sources

- track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
- workload-yaml-reference-databricks-on-aws.md

# Citations

1. [track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md](/references/track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws-f3444863.md)
2. [workload-yaml-reference-databricks-on-aws.md](/references/workload-yaml-reference-databricks-on-aws-d459ba00.md)
