---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1708b3c4dd27b05c03cca0c678ca573ef81a19b32695d849db88005cf1eb8f42
  pageDirectory: concepts
  sources:
    - trace-agents-deployed-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - git-folder-limitation-with-mlflow-3-tracing
    - GFLWM3T
  citations:
    - file: trace-agents-deployed-on-databricks-databricks-on-aws.md
title: Git Folder Limitation with MLflow 3 Tracing
description: Known limitation where MLflow 3 real-time tracing does not work by default when deploying agents from notebooks stored in Databricks Git folders, requiring explicit experiment assignment via mlflow.set_experiment() to a non-Git-associated experiment.
tags:
  - limitation
  - git
  - tracing
  - databricks
timestamp: "2026-06-19T23:07:28.614Z"
---

# Git Folder Limitation with [MLflow 3](/concepts/mlflow-3.md) Tracing

**Git Folder Limitation with [MLflow 3](/concepts/mlflow-3.md) Tracing** refers to a known restriction: when deploying a GenAI agent from a notebook stored in a [Databricks Git folder](/concepts/databricks-git-folders-for-cicd.md), [MLflow 3](/concepts/mlflow-3.md) real-time tracing does **not** work by default. This limitation applies specifically to deployments using Custom Agents (the recommended deployment method). ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Limitation

If you deploy an agent using `agents.deploy()` from a notebook that resides in a Databricks Git folder (e.g., a repo synced from GitHub, GitLab, or Bitbucket), the real-time tracing of production [Traces](/concepts/traces.md) is disabled automatically. The agent still deploys and serves requests, but [Traces](/concepts/traces.md) are not logged to the [MLflow Experiment](/concepts/mlflow-experiment.md) for real-time viewing. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

## Workaround

To enable real-time tracing, you must explicitly set the [MLflow Experiment](/concepts/mlflow-experiment.md) to a **non-Git-associated** experiment before calling `agents.deploy()`. Use `mlflow.set_experiment()` with an experiment that was created in the workspace (not linked to a Git folder). After setting the experiment, [Traces](/concepts/traces.md) will be captured correctly. ^[trace-agents-deployed-on-databricks-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

# Choose a workspace experiment not associated with a Git folder
[[mlflow|MLflow]].set_experiment("/Workspace/Users/your-user/my-production-traces")

# Then deploy the agent
from agents import deploy
deploy(...)
```

> **Note:** The same workaround applies if you are using custom CPU serving as an alternative deployment method — the experiment must not be Git-associated.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of tracing GenAI applications.
- Custom Agents — Recommended method for deploying agents on Databricks.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for runs and [Traces](/concepts/traces.md).
- Databricks Git Folders (Repos) — How notebooks are stored in version-controlled folders.
- [Production Monitoring](/concepts/production-monitoring.md) — Optional long-term storage of [Traces](/concepts/traces.md) in Delta tables.

## Sources

- trace-agents-deployed-on-databricks-databricks-on-aws.md

# Citations

1. [trace-agents-deployed-on-databricks-databricks-on-aws.md](/references/trace-agents-deployed-on-databricks-databricks-on-aws-962e29f6.md)
