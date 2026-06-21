---
title: AI Runtime CLI | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/
ingestedAt: "2026-06-18T08:08:03.221Z"
---

Beta

The AI Runtime CLI is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

The `air` command-line interface submits and manages distributed training workloads on [AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/), the on-demand serverless GPU compute platform. The CLI uses YAML-based job configuration, integrates with MLflow, and supports workspace-based and git-based code workflows.

## When to use the CLI[​](#when-to-use-the-cli "Direct link to When to use the CLI")

Use the AI Runtime CLI when you want to:

*   Submit GPU training workloads from your laptop and code editor without opening a notebook.
*   Define training jobs declaratively in YAML so they can be checked into source control.

For the in-notebook Python API (`@distributed` and `@ray_launch`), see [Multi-GPU workload](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/distributed-training) instead.

## In this section[​](#in-this-section "Direct link to In this section")

*   [Install the AI Runtime CLI](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/installation)
*   [AI Runtime CLI quickstart](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/quickstart)
*   [AI Runtime CLI command reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/command-reference)
*   [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config)
*   [Track runs with MLflow and the Jobs run page](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/track-runs)
*   [AI Runtime CLI examples](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/examples/)
