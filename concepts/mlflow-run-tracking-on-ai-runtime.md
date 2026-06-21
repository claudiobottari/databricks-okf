---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adf722a52140f2e640744201c9b17c5ff825ca059a307ded1243cf22947df19b
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-tracking-on-ai-runtime
    - MRTOAR
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: MLflow Run Tracking on AI Runtime
description: The integration between AI Runtime CLI training jobs and MLflow for tracking experiment runs, accessible via the Jobs run page.
tags:
  - mlflow
  - experiment-tracking
  - databricks
timestamp: "2026-06-19T08:56:13.367Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Tracking on AI Runtime

**MLflow Run Tracking on AI Runtime** refers to the integration between the [AI Runtime CLI](/concepts/ai-runtime-cli.md) and [MLflow](/concepts/mlflow.md) that enables automatic logging and monitoring of distributed training workloads submitted via the `air` command-line interface. This integration provides a unified view of training runs across both the MLflow tracking UI and the Databricks Jobs run page.

## Overview

When you submit a distributed training workload using the AI Runtime CLI, the platform automatically logs key run metadata to MLflow. This allows you to track parameters, metrics, artifacts, and other experiment data without adding explicit logging code to your training scripts. ^[ai-runtime-cli-databricks-on-aws.md]

## Tracking Capabilities

### Automatic Run Creation

The AI Runtime CLI creates an [MLflow Run](/concepts/mlflow-run.md) for each submitted workload. The run is associated with the experiment specified in the [Workload YAML Configuration](/concepts/workload-yaml-configuration.md). If no experiment is specified, the run is logged to the default experiment. ^[ai-runtime-cli-databricks-on-aws.md]

### Logged Information

The following information is automatically captured for each training run:

- **Run parameters**: Including the distributed training configuration (number of workers, GPU type, worker node type) and workload-specific parameters.
- **Metrics**: Training and evaluation metrics logged from your training code, such as loss, accuracy, and learning rate.
- **Artifacts**: Model checkpoints, logs, and any other files saved to the MLflow tracking directory.
- **Source code**: Information about the code version, including git commit hash when using git-based workflows.
- **Run status**: The current state of the run (running, completed, failed) with timestamps.

### Jobs Run Page Integration

Each [MLflow Run](/concepts/mlflow-run.md) is linked to its corresponding [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) run. You can navigate directly from the MLflow experiment view to the Jobs run page to see detailed logs, cluster metrics, and distributed training status. ^[ai-runtime-cli-databricks-on-aws.md]

## Configuration

### Workload YAML

Run tracking behavior can be configured in the workload YAML file. Key settings include:

```yaml
name: my-training-workload
mlflow:
  experiment_name: /Users/me/my-experiment
  experiment_id: "1234567890"
  tags:
    team: ml
    project: llm-training
```

### Environment Variables

You can also configure MLflow tracking through environment variables in the workload YAML:

```yaml
env_vars:
  MLFLOW_EXPERIMENT_NAME: /Users/me/my-experiment
  MLFLOW_TRACKING_URI: databricks
```

### Explicit Logging in Code

While the AI Runtime CLI provides automatic logging, you can add additional tracking calls in your training script using the standard MLflow Python API: ^[ai-runtime-cli-databricks-on-aws.md]

```python
import mlflow

# Log additional parameters
mlflow.log_param("batch_size", 32)
mlflow.log_param("learning_rate", 0.001)

# Log metrics during training
mlflow.log_metric("train_loss", loss, step=epoch)

# Log artifacts
mlflow.log_artifact("/path/to/model.pt")
```

## Viewing Runs

### MLflow Experiment UI

Navigate to the MLflow experiment to view all runs associated with a workload. The UI shows:

- Run comparison tables
- Parameter and metric visualizations
- Artifact browser for downloaded model checkpoints
- Source code links and environment information

### Jobs Run Page

From the [MLflow Run](/concepts/mlflow-run.md) details, click the **View Jobs Run** link to access the Databricks Jobs run page. This page provides: ^[ai-runtime-cli-databricks-on-aws.md]

- Real-time driver and worker logs
- Cluster utilization metrics
- Distributed training status
- Error messages and stack traces

## Best Practices

- **Set unique experiment names**: Organize related workloads under the same experiment for easier comparison across runs.
- **Tag runs meaningfully**: Use tags to filter and search for runs by project, team, or training objective.
- **Log early and often**: Add `mlflow.log_metric()` calls at each epoch or validation step to capture training dynamics.
- **Monitor from the Jobs run page**: Use the Jobs page for real-time monitoring during long-running jobs, and the MLflow UI for post-hoc analysis.
- **Version control YAML files**: Check workload configuration files into source control alongside training code for reproducibility.
- **Use consistent naming**: Establish a naming convention for experiments, runs, and tags to make cross-referencing easier across the organization.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool for submitting distributed training jobs
- [AI Runtime CLI YAML Configuration](/concepts/ai-runtime-cli-yaml-configuration-help-system.md) — Declarative job definition format
- AI Runtime CLI Quickstart — Getting started with the CLI
- Multi-GPU Distributed Training on AI Runtime — The underlying compute platform
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for tracking runs
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — Job orchestration platform linked to MLflow runs
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concepts for multi-GPU model training

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
