---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aed41e1d9326deae92820de8818e0d7712a6ca7fe1f8e33e6fec7cd30c9b544c
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code_source_path
    - code_source_path|$CODE_SOURCE_PATH
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: $CODE_SOURCE_PATH
description: A Databricks-resolved environment variable that points to the uploaded code location on the remote compute node, used to reference training scripts without hardcoding paths.
tags:
  - databricks
  - environment-variable
  - code-execution
timestamp: "2026-06-19T22:03:25.876Z"
---

# `$CODE_SOURCE_PATH`

`$CODE_SOURCE_PATH` is a **resolved environment variable** used within the [AI Runtime CLI](/concepts/ai-runtime-cli.md) workload configuration system. It automatically expands to the absolute path of the uploaded code directory on the remote execution node, enabling portable training scripts that do not depend on hardcoded local paths. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Purpose

When submitting a training job via the AI Runtime CLI, the YAML configuration file may include a `code_source` block that uploads a local directory to the remote node (see Workload YAML reference). The `$CODE_SOURCE_PATH` variable provides a dynamic reference to that uploaded location, so the `command` field can invoke the user's script without knowing the remote filesystem path in advance. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Databricks recommends using `$CODE_SOURCE_PATH` rather than hardcoding a path, because the remote directory name is assigned automatically and may differ between runs. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Usage Example

In the following YAML snippet, the `command` field uses `$CODE_SOURCE_PATH` to point to `train.py`:

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: .
command: python $CODE_SOURCE_PATH/train.py
```

This instructs the AI Runtime to upload the current directory (`.`) and then run `train.py` from the uploaded location. The variable is resolved only on the remote compute node, not on the local machine. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line interface that submits workloads and interprets `$CODE_SOURCE_PATH`.
- Workload YAML reference – The full field specification for YAML config files, including the `code_source` block.
- [Serverless environment versions](/concepts/serverless-environment-versioning.md) – The environment version selector (e.g. `'4'`) that controls which libraries are available on the remote node.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The container that holds the run’s metrics, parameters, and artifacts.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
