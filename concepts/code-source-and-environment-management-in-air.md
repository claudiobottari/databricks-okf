---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f3c2ede5e045b9b9089c372bb1cdbc6103b0a747944be7a7b5abb36d6d1ad43
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-source-and-environment-management-in-air
    - Environment Management in AIR and Code Source
    - CSAEMIA
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Code Source and Environment Management in AIR
description: Mechanisms for packaging local code (snapshot with root_path) and declaring Python dependencies (environment block with version and dependency list) for serverless GPU training runs.
tags:
  - databricks
  - code-packaging
  - dependencies
  - python
timestamp: "2026-06-19T08:56:32.127Z"
---

---
title: Code Source and Environment Management in AIR
summary: Configuring code source and environment for AI Runtime CLI training jobs, including snapshot uploads, dependency management, and serverless GPU environment versions.
sources:
  - ai-runtime-cli-quickstart-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:08:15.084Z"
updatedAt: "2026-06-18T08:08:15.084Z"
tags:
  - ai-runtime-cli
  - code-source
  - environment
  - training
  - yaml
aliases:
  - code-source-and-environment-management-in-air
  - CSEMIA
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Code Source and Environment Management in AIR

**Code Source and Environment Management in AIR** covers how to specify the training code and Python dependencies for jobs submitted via the [AI Runtime CLI](/concepts/ai-runtime-cli.md). These configuration blocks are defined in a YAML workload file (typically `train.yaml`) and control which local code is uploaded to the remote node and what packages are installed before execution.

## Environment Block

The `environment` block lists Python dependencies to be installed and optionally selects the serverless GPU environment version. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The `environment.version` field selects the serverless GPU environment version. It is optional and defaults to `'4'`. For all available versions, see [Serverless environment versions](/concepts/serverless-environment-versioning.md). ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The `environment.dependencies` field is a list of Python package specifiers (e.g., `torch`, `transformers`). These packages are installed before the training command runs. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Example:

```yaml
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
```

## Code Source Block

The `code_source` block specifies how local code is uploaded to the remote execution node. The only documented type in this source is `snapshot`, which uploads a directory from the local filesystem. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Inside the `snapshot` block, the `root_path` field points to the local directory to upload (e.g., `.` for the current directory). ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Example:

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: .
```

## Running the Training Script

The `command` field specifies the command to run on the remote node. The environment variable `$CODE_SOURCE_PATH` resolves to the location where the uploaded code is placed. Databricks recommends using `$CODE_SOURCE_PATH` rather than hardcoding a path. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Example:

```yaml
command: python $CODE_SOURCE_PATH/train.py
```

## Putting It Together: Minimal Example with Code and Dependencies

A complete `train.yaml` that runs a local training script with dependencies on a single A10 GPU might look like:

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

The AI Runtime CLI uploads the local directory (`.`), installs the listed packages, and executes `train.py` on a single A10 GPU. Logs, metrics, and parameters are captured in the MLflow experiment named in `experiment_name`. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – Command-line tool for submitting training jobs.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Full field reference for the YAML config.
- [Serverless environment versions](/concepts/serverless-environment-versioning.md) – Available environment versions for serverless GPU jobs.
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – How AIR jobs are tracked in MLflow.
- Train.yaml structure – Complete structure of the YAML workload file.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
