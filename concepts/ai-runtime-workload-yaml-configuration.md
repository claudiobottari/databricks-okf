---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6fb4bf1ec109adc1b6d32b48715527244e249757f4b8f96d70b8fd9a660a505
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-workload-yaml-configuration
    - ARWYC
    - AI Runtime CLI YAML Configuration
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
    - file: install-the-ai-runtime-cli-databricks-on-aws.md
    - file: ai-runtime-cli-examples-databricks-on-aws.md
    - file: ai-runtime-cli-command-reference-databricks-on-aws.md
title: AI Runtime Workload YAML Configuration
description: A YAML-based configuration format that defines training workloads including experiment name, compute specs, code source, environment dependencies, and execution command.
tags:
  - configuration
  - yaml
  - databricks
timestamp: "2026-06-18T10:43:22.801Z"
---

# AI Runtime [Workload YAML Configuration](/concepts/workload-yaml-configuration.md)

**AI Runtime Workload YAML Configuration** is the declarative format used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) to define machine learning workloads that run on Databricks AI Runtime. The configuration is written in standard YAML and specifies compute resources, training code, dependencies, and runtime parameters. Submitting a YAML file via `air run` triggers the workload directly from the terminal without manual cluster setup.^[ai-runtime-cli-quickstart-databricks-on-aws.md, install-the-ai-runtime-cli-databricks-on-aws.md]

The feature is currently in **Beta**.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Minimal Configuration

A minimal workload YAML must contain three top-level fields: `experiment_name`, `compute`, and `command`. The following example runs a simple echo command without any local code:^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
experiment_name: my-first-air-run
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "hello AIR!"
```

## Full Configuration Structure

When running your own training code, add an `environment` block for Python dependencies and a `code_source` block to upload local files. The `command` field invokes the uploaded script using the `$CODE_SOURCE_PATH` environment variable, which resolves to the remote root of the uploaded code.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

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

### Top-Level Fields

| Field | Required | Description |
|---|---|---|
| `experiment_name` | Yes | The [MLflow](/concepts/mlflow.md) experiment name under which the run is tracked.^[ai-runtime-cli-quickstart-databricks-on-aws.md] |
| `compute` | Yes | Specifies accelerator resources. Must include `num_accelerators` (integer) and `accelerator_type` (string, e.g., `GPU_1xA10`).^[ai-runtime-cli-quickstart-databricks-on-aws.md] |
| `command` | Yes | The shell command to execute on the compute node. Use `$CODE_SOURCE_PATH` to reference the uploaded code directory.^[ai-runtime-cli-quickstart-databricks-on-aws.md] |
| `environment` | No | Dictionary with optional `version` (string, defaults to `'4'`) and `dependencies` (list of pip-installable packages). See [Serverless environment versions](/concepts/serverless-environment-versioning.md).^[ai-runtime-cli-quickstart-databricks-on-aws.md] |
| `code_source` | No | Defines how local code is uploaded. Currently supports `type: snapshot` with a `snapshot.root_path` pointing to the directory containing the code.^[ai-runtime-cli-quickstart-databricks-on-aws.md] |
| `timeout_minutes` | No | Maximum runtime before the job is terminated. Overridable from CLI.^[ai-runtime-cli-quickstart-databricks-on-aws.md] |

Additional fields may appear in more advanced workloads, such as those using `torchrun` or [Ray Train](/concepts/ray-train-resource-allocation.md), but the above are the core building blocks documented in the quickstart.^[ai-runtime-cli-examples-databricks-on-aws.md]

## Code Upload and Dependency Management

When a `code_source` block is present, the CLI uploads the local directory specified by `root_path` to the remote compute node. The `environment.dependencies` list is used to install Python packages via pip before the `command` runs. Databricks recommends referencing the uploaded files through `$CODE_SOURCE_PATH` rather than hardcoding paths.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Working with the Configuration

The YAML is submitted with the `air run` command:

```bash
air run --file train.yaml
```

Use `--dry-run` to validate the configuration without launching the workload. Override any YAML field from the command line with `--override <field>=<value>` — for example, `--override compute.num_accelerators=32 timeout_minutes=120`.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The CLI provides inline help for YAML fields:

```bash
air -h config               # Full YAML config reference
air -h config.compute       # Per-field help for compute section
```

^[ai-runtime-cli-command-reference-databricks-on-aws.md]

## Example: Distributed Training with Multiple Nodes

Advanced configurations can specify multi-node training with frameworks like PyTorch FSDP or Ray Train. These YAML files include additional fields such as `num_workers`, `framework`, and cluster-level settings. For complete examples, see the [AI Runtime CLI examples](/concepts/ai-runtime-cli.md) page.^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool that consumes the YAML configuration.
- AI Runtime CLI quickstart — Step-by-step guide for writing and submitting a first workload.
- [AI Runtime CLI command reference](/concepts/ai-runtime-cli-commands.md) — Full list of `air` subcommands and flags.
- [MLflow](/concepts/mlflow.md) — Experiment tracking and logging for AI Runtime runs.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for managing code volumes and models.
- [Serverless environment versions](/concepts/serverless-environment-versioning.md) — Available GPU environment versions for the `environment.version` field.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md
- ai-runtime-cli-command-reference-databricks-on-aws.md
- ai-runtime-cli-examples-databricks-on-aws.md
- install-the-ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
2. [install-the-ai-runtime-cli-databricks-on-aws.md](/references/install-the-ai-runtime-cli-databricks-on-aws-22b6c9fd.md)
3. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
4. [ai-runtime-cli-command-reference-databricks-on-aws.md](/references/ai-runtime-cli-command-reference-databricks-on-aws-a236d04f.md)
