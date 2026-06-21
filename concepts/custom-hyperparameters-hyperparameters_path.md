---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4f9eeb69b387d369491cc65a88f46346fd1f47f30e0ea491c6e8037660fd7a6
  pageDirectory: concepts
  sources:
    - workload-yaml-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-hyperparameters-hyperparameters_path
    - CH(
    - Custom hyperparameters
  citations:
    - file: workload-yaml-reference-databricks-on-aws.md
title: Custom Hyperparameters (HYPERPARAMETERS_PATH)
description: Passing structured YAML configuration to training scripts via the `parameters` field in the workload YAML, accessible at runtime through the `HYPERPARAMETERS_PATH` environment variable.
tags:
  - hyperparameters
  - configuration
  - training
timestamp: "2026-06-19T23:27:12.920Z"
---

# Custom Hyperparameters (HYPERPARAMETERS_PATH)

**Custom Hyperparameters (HYPERPARAMETERS_PATH)** is a mechanism in the [AI Runtime CLI](/concepts/ai-runtime-cli.md) that allows you to pass structured configuration to a training script by defining a `parameters` block in a [Workload YAML Configuration](/concepts/workload-yaml-configuration.md). At runtime, the CLI sets the `HYPERPARAMETERS_PATH` environment variable to point to a YAML file containing the parameters, which the script can then read. ^[workload-yaml-reference-databricks-on-aws.md]

## Usage

To use custom hyperparameters, add a `parameters` block to your workload YAML definition. The block contains arbitrary YAML key-value pairs, typically organized by category (e.g., `model`, `training`). ^[workload-yaml-reference-databricks-on-aws.md]

Example YAML:

```yaml
experiment_name: parameterized-training
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
    git:
      branch: main
command: torchrun --nproc_per_node=8 train.py
parameters:
  model:
    name: 'gpt2'
    hidden_size: 768
  training:
    batch_size: 32
    learning_rate: 0.0001
```

^[workload-yaml-reference-databricks-on-aws.md]

At runtime, the CLI serializes the `parameters` block into a YAML file and sets the `HYPERPARAMETERS_PATH` environment variable with the path to that file. The training script reads this file using standard Python libraries. ^[workload-yaml-reference-databricks-on-aws.md]

Example Python code to read the parameters:

```python
import os
import yaml

with open(os.environ['HYPERPARAMETERS_PATH']) as f:
    params = yaml.safe_load(f)

learning_rate = params['training']['learning_rate']
model_name = params['model']['name']
```

^[workload-yaml-reference-databricks-on-aws.md]

## Related Concepts

- [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) – The top-level YAML file that contains the `parameters` block.
- Environment Variables – How `HYPERPARAMETERS_PATH` is made available to the script.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line tool that processes the YAML and handles the hyperparameters path.
- Python Dependencies – Required libraries (e.g., `pyyaml`) for reading the YAML file.

## Sources

- workload-yaml-reference-databricks-on-aws.md

# Citations

1. [workload-yaml-reference-databricks-on-aws.md](/references/workload-yaml-reference-databricks-on-aws-d459ba00.md)
