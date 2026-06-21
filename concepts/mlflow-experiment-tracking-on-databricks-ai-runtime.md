---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f681139f05723494cc46428cb07fa46678f4bde83b6dcfb51a432dcf7628f63c
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-tracking-on-databricks-ai-runtime
    - METODAR
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: MLflow Experiment Tracking on Databricks AI Runtime
description: Integration of MLflow for logging metrics, parameters, and artifacts from distributed training workloads submitted via the air CLI on Databricks
tags:
  - mlflow
  - experiment-tracking
  - logging
timestamp: "2026-06-19T22:02:38.698Z"
---

# MLflow Experiment Tracking on Databricks AI Runtime

**MLflow Experiment Tracking on Databricks AI Runtime** refers to the integrated logging of training metrics, parameters, and artifacts when running distributed workloads using the Databricks AI Runtime CLI (`air`). The AI Runtime ecosystem uses [MLflow](/concepts/mlflow.md) as the default experiment tracking service, enabling teams to record runs, compare results, and manage model checkpoints from jobs submitted via `air run -f train.yaml`. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Integration with AI Runtime CLI Workloads

The AI Runtime CLI includes end-to-end example workloads that demonstrate real distributed‑training patterns on H100 GPUs. One such example — multi‑node LLM fine‑tuning with [PyTorch Fully Sharded Data Parallel (FSDP)](/concepts/pytorch-fully-sharded-data-parallel-fsdp.md) — explicitly logs training runs to **MLflow** and saves model checkpoints to a [Unity Catalog](/concepts/unity-catalog.md) volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]

This integration means that any custom workload defined in a YAML configuration file and submitted via `air run` can leverage MLflow’s tracking capabilities without additional setup. Users can view experiment runs, compare hyperparameters, and manage model versions directly from the Databricks workspace.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command‑line interface for submitting and managing distributed training runs on Databricks AI Runtime.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for grouping related runs.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — A memory‑efficient distributed training strategy that is used in conjunction with MLflow tracking.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer used for storing checkpoints and artifacts.

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
