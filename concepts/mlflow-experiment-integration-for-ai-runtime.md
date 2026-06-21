---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73c33254e0b934472fbaaedb5d753c292a68a3f07dbb5f7971db92c759726e38
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-integration-for-ai-runtime
    - MEIFAR
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: MLflow Experiment Integration for AI Runtime
description: Each AI Runtime CLI run creates a run within a named MLflow experiment, capturing metrics, parameters, artifacts, and logs viewable in the Databricks workspace MLflow UI.
tags:
  - databricks
  - mlflow
  - experiment-tracking
timestamp: "2026-06-19T22:03:25.431Z"
---

Based on the provided source material, here is a clear and concise wiki page about MLflow Experiment Integration for AI Runtime.

---

## MLflow Experiment Integration for AI Runtime

The **AI Runtime CLI** (in Beta) allows you to submit training jobs directly from the command line. When you submit a job using the `air run --file train.yaml` command, the system creates an [MLflow Run](/concepts/mlflow-run.md) within the [MLflow Experiment](/concepts/mlflow-experiment.md) named in the `experiment_name` field of your YAML config. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Each [MLflow Run](/concepts/mlflow-run.md) captures the workload's **metrics**, **parameters**, **artifacts**, and **logs**, all viewable in the workspace's MLflow UI. This integration provides a centralized way to track and compare the results of different training runs. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Tracking Runs

The [MLflow Run](/concepts/mlflow-run.md) is created as part of the submission process. The output of `air run` includes clickable links to the run's MLflow experiment and [MLflow Run](/concepts/mlflow-run.md) in the workspace UI, allowing you to easily navigate to the tracking data. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The [AI Runtime CLI](/concepts/ai-runtime-cli.md) provides commands to inspect the run's status, stream or download logs, list recent runs, and cancel a run. For example, you can use `air logs <run-id>` to view logs from a specific node. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Configuring MLflow Integration

You can configure the MLflow experiment integration within your YAML config file by setting the `experiment_name` field. This field specifies the name of the MLflow experiment that will contain the run. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md)
- [MLflow Experiment](/concepts/mlflow-experiment.md)
- [MLflow Run](/concepts/mlflow-run.md)
- YAML Config
- Workload YAML reference

### Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
