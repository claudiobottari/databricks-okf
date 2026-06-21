---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d96ec0859cfda123e188342936161c64ee78def50c1beee25728254f66e4af31
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-source-snapshot
    - CSS
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Code Source Snapshot
description: Mechanism to upload local code to the remote execution node using a snapshot block in the YAML config, with $CODE_SOURCE_PATH as the recommended reference path.
tags:
  - code-deployment
  - snapshot
  - machine-learning
timestamp: "2026-06-19T17:31:00.863Z"
---

---

title: Code Source Snapshot
summary: Mechanism for uploading local code directories to the remote execution environment using the `snapshot` type and the `$CODE_SOURCE_PATH` variable
sources:
  - ai-runtime-cli-quickstart-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:22:33.527Z"
updatedAt: "2026-06-18T14:22:33.527Z"
tags:
  - code-upload
  - deployment
  - snapshot
aliases:
  - code-source-snapshot
  - CSS
---

# Code Source Snapshot

A **Code Source Snapshot** is a YAML configuration block used with the [AI Runtime CLI](/concepts/ai-runtime-cli.md) that instructs the CLI to package a local directory and upload it to a serverless GPU environment for execution. It is required when the workload runs a user-supplied training script rather than a built-in command. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Configuration

The code source is defined under the `code_source` key in the YAML config. The snapshot method is specified with `type: snapshot`. The only required subfield is `snapshot.root_path`, which points to the local directory containing the training script and any supporting files. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Minimal Example

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: .
```

This uploads the current working directory (the directory where the YAML file resides) to the remote compute node. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Referencing the Uploaded Code

On the remote node, the location of the uploaded code is made available through the environment variable `$CODE_SOURCE_PATH`. Databricks recommends using this variable instead of hardcoding a path in the `command` field, because it ensures the command always refers to the correct remote directory regardless of how the CLI manages the upload and extraction. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Example Command

```yaml
command: python $CODE_SOURCE_PATH/train.py
```

This runs `train.py` from the uploaded snapshot on the remote node. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Full Workflow Example

The following complete YAML config defines an experiment, environment dependencies, compute resources, a code source snapshot, and the command. It installs `torch` and `transformers`, uploads the current directory, and runs `train.py` on a single A10 GPU. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

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

The expected project structure is: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```
my-project/
├── train.yaml
└── train.py
```

## Behavior

When the AI Runtime CLI processes a config with a code source snapshot, it uploads the directory specified in `root_path`, submits the job to a serverless GPU environment, and executes the command. The run is tracked in the [MLflow Experiment](/concepts/mlflow-experiment.md) named in `experiment_name`. Metrics, parameters, artifacts, and logs are captured and are viewable in the workspace MLflow UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line interface that processes snapshot configurations
- AI Runtime CLI Quickstart – End-to-end walkthrough for first-time users
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Full field reference for all configuration options
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – Mechanism for capturing and viewing run results
- Serverless GPU Training – The remote compute environment where snapshots are executed
- Environment Dependencies – Python packages specified alongside the code source

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
