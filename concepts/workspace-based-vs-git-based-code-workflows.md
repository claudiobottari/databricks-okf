---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a298aa01e2e77744996379764d55a5156e1eaf2200f949af0065f6b3fe8de5ba
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-based-vs-git-based-code-workflows
    - WVGCW
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: Workspace-based vs git-based code workflows
description: AI Runtime CLI supports both Databricks workspace-based code and git-based code workflows for submitting training jobs.
tags:
  - workflow
  - git
  - databricks-workspace
timestamp: "2026-06-19T13:56:42.336Z"
---

# Workspace-based vs git-based code workflows

**Workspace-based vs git-based code workflows** refers to two distinct approaches for managing and submitting distributed training code using the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`). The choice of workflow determines how code is packaged, where it is stored, and how it is shared during job execution.

## Overview

The `air` CLI supports two modes for providing code to a training job: workspace-based and git-based. These workflows address different developer preferences for code management and collaboration. Both approaches integrate with [MLflow](/concepts/mlflow.md) for run tracking and support YAML-based job configuration.^[ai-runtime-cli-databricks-on-aws.md]

## Workspace-based workflow

In a workspace-based workflow, training code is stored in the Databricks workspace itself. Users write or upload their code to the workspace file system, and the `air` CLI references the code by its workspace path when submitting a job.^[ai-runtime-cli-databricks-on-aws.md]

### Characteristics

- Code resides in the Databricks workspace environment, accessible directly from notebooks and the workspace UI.
- No external version control integration is required; files are managed within the Databricks platform.
- Jobs reference code using workspace file paths.

This approach is well-suited for interactive development and quick experimentation where code changes happen directly within the Databricks environment.

## Git-based workflow

In a git-based workflow, training code is hosted in a remote [git repository](/concepts/databricks-connect-github-examples.md), such as GitHub, GitLab, or Bitbucket. The `air` CLI clones the repository on demand when the job is submitted, allowing teams to manage code through standard version control practices.^[ai-runtime-cli-databricks-on-aws.md]

### Characteristics

- Code is managed through external git providers with full version control history.
- Jobs are defined declaratively in YAML configuration files that specify the repository URL, branch, and path to the training script.
- Multiple team members can collaborate using pull requests, code reviews, and branching strategies.

This workflow is ideal for production-grade training pipelines where reproducibility, code review, and audit trails are important.

## Choosing a workflow

The following considerations guide the choice between workspace-based and git-based workflows:

| Consideration | Workspace-based | Git-based |
|---------------|-----------------|-----------|
| Development speed | Faster for interactive exploration | Requires commit/push cycle |
| Collaboration | Limited to workspace sharing | Full version control collaboration |
| Reproducibility | Code changes tracked within workspace | Exact commit history available |
| Code review | Manual or notebook-based | Pull request workflows |
| CI/CD integration | Limited | Standard git-based pipelines |

The `air` CLI supports both workflows, allowing teams to choose the approach that best fits their development process.^[ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface for submitting and managing distributed training workloads.
- [AI Runtime](/concepts/ai-runtime.md) — The on-demand serverless GPU compute platform that runs the training jobs.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Run tracking and experiment management integrated with both workflow types.
- Declarative job definitions in YAML — YAML-based configuration for specifying training jobs.
- Multi-GPU workload — The in-notebook Python API alternative using `@distributed` and `@ray_launch`.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
