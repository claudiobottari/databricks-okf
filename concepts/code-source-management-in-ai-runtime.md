---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 538022c403ad97264ed49349f003180f7eab881b6f6592a04992b67e4f7efe42
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-source-management-in-ai-runtime
    - CSMIAR
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Code Source Management in AI Runtime
description: Mechanism for uploading local code directories to remote execution nodes using the code_source block and $CODE_SOURCE_PATH variable in workload configurations.
tags:
  - code-deployment
  - databricks
  - workflow
timestamp: "2026-06-18T10:43:26.248Z"
---

# [Code Source Management](/concepts/code-source-management.md) in AI Runtime

**Code source management** in AI Runtime refers to how the [AI Runtime CLI (air)](/concepts/ai-runtime-cli-air.md) uploads and references local training code when submitting workloads. When a [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) includes a `code_source` block, the CLI packages the specified local directory, uploads it to the remote execution environment, and makes it available to the training command at a predictable path.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## How Code Sources Work

The `code_source` section in a [Workload YAML](/concepts/workload-yaml-configuration.md) configuration tells the AI Runtime CLI which local files to upload and where to find them on the remote node. Currently, the supported method is the `snapshot` type, which takes a snapshot of a local directory and uploads it as part of the job submission.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

When `code_source` is configured, the CLI:

1. Reads the `root_path` from the `snapshot` block (defaulting to `.`, the current directory).
2. Packages and uploads the contents of that directory to the remote compute cluster.
3. Makes the uploaded code available at the `$CODE_SOURCE_PATH` environment variable on the remote node.

## Snapshot Code Source

The `snapshot` code source type captures a point-in-time copy of a local directory. It is defined in the YAML configuration as follows:^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: .
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The `root_path` field specifies the directory to upload. This can be an absolute path or a path relative to the YAML configuration file. Using `.` uploads the directory containing the YAML file.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Using `$CODE_SOURCE_PATH`

The `$CODE_SOURCE_PATH` environment variable resolves to the location of the uploaded code on the remote execution node. Databricks recommends using this variable instead of hardcoding a path in the `command` field. This ensures commands work correctly regardless of where the code is placed in the remote environment.^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Example usage in a YAML command:^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
command: python $CODE_SOURCE_PATH/train.py
```

## YAML Configuration Example

A complete YAML configuration with [Code Source Management](/concepts/code-source-management.md) typically looks like:^[ai-runtime-cli-quickstart-databricks-on-aws.md]

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

## Project Directory Structure

When using [Code Source Management](/concepts/code-source-management.md), the training script should be placed alongside the YAML configuration file. A typical project structure looks like:^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```
my-project/
├── train.yaml
└── train.py
```

## Workloads Without Code Sources

If a workload does not require any local code, the `code_source` block can be omitted entirely. The `command` field can run any command available in the remote environment, such as simple shell commands:^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
experiment_name: my-first-air-run
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "hello AIR!"
```

## Related Concepts

- [AI Runtime CLI (air)](/concepts/ai-runtime-cli-air.md) — The command-line tool for submitting and managing AI workloads
- [Workload YAML](/concepts/workload-yaml-configuration.md) — The configuration format for defining AI Runtime workloads
- AI Runtime CLI quickstart — Step-by-step guide for first-time users
- [AI Runtime](/concepts/ai-runtime.md) — The runtime environment that executes submitted workloads
- Databricks CLI — Authentication and management tool used alongside the AI Runtime CLI

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
