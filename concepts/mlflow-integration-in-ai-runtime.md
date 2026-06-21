---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5137f6043e5f63917d41b44ac8e02cdc522eace5516cdd0c13bc0efb1fa8d031
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-in-ai-runtime
    - MIIAR
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: MLflow Integration in AI Runtime
description: Automatic tracking of training runs as MLflow experiments, capturing metrics, parameters, artifacts, and logs visible in the Databricks workspace MLflow UI.
tags:
  - mlflow
  - experiment-tracking
  - machine-learning
timestamp: "2026-06-19T17:30:42.822Z"
---

# MLflow Integration in AI Runtime

Each AI Runtime run is automatically tracked as an [MLflow Run](/concepts/mlflow-run.md) under a named experiment, capturing metrics, parameters, artifacts, and logs accessible via the workspace UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## How Tracking Works

When you submit a workload using `air run --file <config>.yaml`, the CLI creates a run in the MLflow experiment specified by the `experiment_name` field in the YAML configuration. That run captures the workload’s metrics, parameters, artifacts, and logs, all viewable in the workspace MLflow UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

After submission, the CLI prints a run ID and provides clickable links to the MLflow experiment and the specific [MLflow Run](/concepts/mlflow-run.md) in the workspace UI. This allows you to quickly inspect training metrics, compare runs, and review artifacts without leaving the browser. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Accessing Logs Outside MLflow

While logs are included in the [MLflow Run](/concepts/mlflow-run.md), you can also stream or download them directly using the `air logs` command, independent of the MLflow interface. This is useful for real‑time monitoring during training or for offline debugging. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Configuration Example

The experiment name is configured in the YAML workload file under the `experiment_name` field. This name can reference an existing experiment, or MLflow will create one if it does not exist: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```yaml
experiment_name: my-first-air-run
compute:
  num_accelerators: 1
  accelerator_type: GPU_1xA10
command: echo "hello AIR!"
```

When you submit this configuration, the CLI automatically creates an [MLflow Run](/concepts/mlflow-run.md) under the specified experiment, capturing the command output, any metrics, and associated metadata. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Viewing Runs

The MLflow UI in the Databricks workspace provides a centralized view of all runs associated with each experiment. From the UI you can: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

- Compare metrics across different runs
- View logged parameters and artifacts
- Access training logs
- Navigate directly from CLI output links

The output from `air run` and `air list runs` includes clickable links to the MLflow experiment and run pages in the workspace UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Next Steps

The AI Runtime documentation provides further guidance on tracking runs with MLflow alongside the Databricks Jobs run page. See the [Track runs with MLflow and the Jobs run page](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/track-runs) guide for details. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool for submitting workloads and managing MLflow tracking
- [AI Runtime](/concepts/ai-runtime.md) — The execution environment for AI workloads on Databricks
- [MLflow](/concepts/mlflow.md) — The open-source platform for ML lifecycle management
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for grouping related MLflow runs
- [MLflow Runs](/concepts/mlflow-run.md) — Individual executions tracked within an experiment

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
