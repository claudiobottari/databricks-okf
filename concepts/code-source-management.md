---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5d7a89ed1c7aba223a060a2315d11bc3e80cd8149d0a8e8d10425fb714ced1d
  pageDirectory: concepts
  sources:
    - workload-yaml-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-source-management
    - CSM
  citations:
    - file: workload-yaml-reference-databricks-on-aws.md
title: Code Source Management
description: Uploading local code to remote training nodes via the `code_source` block, supporting plain tarball snapshots, git-versioned snapshots, and folder filtering with `include_paths`.
tags:
  - code
  - deployment
  - databricks
timestamp: "2026-06-19T23:27:07.462Z"
---

# Code Source Management

**Code Source Management** refers to the configuration and handling of training code within the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (Beta) workload definitions. In a workload YAML file, the `code_source` block defines how local code is packaged, uploaded, and made available to remote compute nodes during training jobs. ^[workload-yaml-reference-databricks-on-aws.md]

## Overview

The `code_source` block is an optional component of a [Workload YAML Configuration](/concepts/workload-yaml-configuration.md). When specified, it uploads the contents of a local directory to the training node, making the code accessible via the `$CODE_SOURCE_PATH` environment variable. If omitted, any referenced scripts must already exist on the node or be installed as dependencies. ^[workload-yaml-reference-databricks-on-aws.md]

The only supported code source type is `snapshot`. A snapshot packages the working tree as a plain tarball and transfers it to the remote cluster. ^[workload-yaml-reference-databricks-on-aws.md]

## Configuration Fields

### Core Fields

- **`type`**: Must be `snapshot`.
- **`snapshot.root_path`** (Required): Local path to the root of the directory or git repository to snapshot. For example, `/home/username/repo`.
- **`snapshot.git`** (Optional): A block that pins a specific branch or commit. Available only when `root_path` is a git repository.
- **`snapshot.include_paths`** (Optional): A list of relative paths to include from the repository, filtering out all other files.

### Git Integration

When `root_path` points to a git repository, an optional `git:` block can be added to control which version of the code is used:

- **`git.branch`** – Pin to a branch. Uses the local HEAD of that branch; no remote fetch is performed. Mutually exclusive with `git.commit`.
- **`git.commit`** – Pin to a specific commit SHA for exact reproducibility. Mutually exclusive with `git.branch`.
- **`git.remote`** – (Used only with `git.branch`) When set to `true`, auto‑detects the remote and uses the remote’s HEAD instead of the local one. Can also be set to a remote name (e.g., `upstream`) to fetch from a specific remote.

If the `git:` block is omitted entirely, the working tree is packaged as a plain tarball including any uncommitted changes. For non‑git directories, the `git:` block is not allowed and version caching is not available. ^[workload-yaml-reference-databricks-on-aws.md]

### Folder Filtering with `include_paths`

For large repositories, `include_paths` reduces upload and download time by snapshotting only a subset of files. Paths must be relative to the repository root (no leading `/`) and cannot contain `..`. When omitted, the entire repository is included by default. ^[workload-yaml-reference-databricks-on-aws.md]

### Path Resolution

All paths in the workload YAML are resolved relative to the location of the YAML file itself, unless an absolute path is used. This allows portable configurations where the `root_path` can be `.` to refer to the same directory as the YAML file. ^[workload-yaml-reference-databricks-on-aws.md]

## Usage

The packaged code is placed at `/databricks/code_source/<directory_name>` on the remote node, where `<directory_name>` is the final path component of `root_path`. The environment variable `$CODE_SOURCE_PATH` is set to this absolute path and should be used in the `command` field rather than hard‑coding the location. ^[workload-yaml-reference-databricks-on-aws.md]

### Minimal Example

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
command: python $CODE_SOURCE_PATH|code_source_path|$CODE_SOURCE_PATH/train.py
```

### Git Repository Pinned to a Branch

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    git:
      branch: main
command: train.sh
```

### Filtered Include Paths

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: /home/username/repo
    include_paths:
      - research/models
      - research/common
      - research/configs
command: python $CODE_SOURCE_PATH|code_source_path|$CODE_SOURCE_PATH/research/models/launch_training.py
```

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command‑line tool that processes the workload YAML and manages code snapshots.
- [Workload YAML](/concepts/workload-yaml-configuration.md) – Full reference for all configuration fields, including compute, environment, secrets, and parameters.
- Databricks Secrets – Used with the `secrets` block to securely pass API keys and tokens.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The infrastructure that runs the training workloads with the uploaded code source.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit for runs created by the workload.
- Attribute Usage with Serverless Usage Policies – Cost attribution using `usage_policy_id`.

## Sources

- workload-yaml-reference-databricks-on-aws.md

# Citations

1. [workload-yaml-reference-databricks-on-aws.md](/references/workload-yaml-reference-databricks-on-aws-d459ba00.md)
