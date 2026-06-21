---
title: AI Runtime CLI quickstart | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/quickstart
ingestedAt: "2026-06-18T08:08:15.084Z"
---

Beta

The AI Runtime CLI is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This page walks through submitting your first training job with the AI Runtime CLI. Before starting, [install the CLI and configure authentication](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/installation).

## Step 1: Write a YAML config[​](#step-1-write-a-yaml-config "Direct link to Step 1: Write a YAML config")

Create `train.yaml` describing the workload. The minimal config requires an experiment name, a compute spec, and a command. The command below runs without any local code, so you can submit your first run right away:

YAML

    experiment_name: my-first-air-runcompute:  num_accelerators: 1  accelerator_type: GPU_1xA10command: echo "hello AIR!"

### Run your own code[​](#run-your-own-code "Direct link to Run your own code")

To run a local training script, add an `environment` block that lists your Python dependencies and a `code_source` block that uploads your local code. Place your script alongside `train.yaml`:

Text

    my-project/├── train.yaml└── train.py

YAML

    experiment_name: my-first-air-runenvironment:  version: '4'  dependencies:    - torch    - transformerscompute:  num_accelerators: 1  accelerator_type: GPU_1xA10code_source:  type: snapshot  snapshot:    root_path: .command: python $CODE_SOURCE_PATH/train.py

This config installs the listed dependencies, uploads the current directory (`root_path: .`), and runs `train.py` on a single A10 GPU. `$CODE_SOURCE_PATH` resolves to the uploaded code location on the remote node. Databricks recommends using this rather than hardcoding a path. `environment.version` selects the serverless GPU environment version and is optional (defaults to `'4'`). For all available versions, see [Serverless environment versions](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/).

For the full field reference, see [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config).

## Step 2: Submit the run[​](#step-2-submit-the-run "Direct link to Step 2: Submit the run")

Submit the workload:

Bash

    air run --file train.yaml

The CLI uploads your local code (if you configured a `code_source`), submits the job, and prints a run ID. Use that ID to inspect, watch, and cancel the run in later commands.

The submission creates a run in the MLflow experiment named in `experiment_name` (an experiment can hold many runs). That run captures the workload's metrics, parameters, artifacts, and logs, all viewable in the workspace MLflow UI. Logs are also available outside MLflow: stream them to your terminal or a file, or download them later with `air logs` (see [Step 3](#step-3-inspect-the-run)).

To watch logs until completion, add `--watch`:

Bash

    air run --file train.yaml --watch

## Step 3: Inspect the run[​](#step-3-inspect-the-run "Direct link to Step 3: Inspect the run")

Check status:

The output includes clickable links to the run's MLflow experiment and MLflow run in the workspace UI.

Stream or download logs:

Bash

    air logs <run-id>air logs <run-id> --node 2air logs <run-id> --download-to ./logs/

Distributed workloads run across multiple nodes. By default, `air logs` streams from node 0. To view logs from a specific node, pass `--node`. Use `--download-to` to write logs to a local directory instead of streaming them.

List recent runs:

Bash

    air list runs --limit 10air list runs --active

Cancel a run:

## Common patterns[​](#common-patterns "Direct link to Common patterns")

**Override YAML fields from the command line:**

Bash

    air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120

**Validate the config without submitting:**

Bash

    air run --file train.yaml --dry-run

**Make a submission safely retryable:**

Bash

    air run --file train.yaml --idempotency-key my-unique-key

If the same key has been used before, the existing run is returned instead of creating a new one.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [AI Runtime CLI command reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/command-reference)
*   [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config)
*   [Track runs with MLflow and the Jobs run page](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/track-runs)
