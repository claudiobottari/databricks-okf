---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f003ea4962a673116081850a10cd5ceb1af10f443f70c359552cf122abb58924
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - git-based-code-workflows
    - GCW
    - Git-Based Workflows
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: Git-based code workflows
description: Approach for submitting training workloads using code stored in git repositories.
tags:
  - git
  - workflow
  - code-management
timestamp: "2026-06-19T17:30:20.863Z"
---

## Git-based Code Workflows

**Git-based code workflows** refer to a development paradigm where training code and job configurations are managed with Git and checked into a source control repository, rather than being stored as notebooks in a workspace. This approach enables declarative job definitions that are reproducible, reviewable, and versioned alongside the rest of the codebase. ^[ai-runtime-cli-databricks-on-aws.md]

## Relationship with the AI Runtime CLI

The `air` command‑line interface ([AI Runtime CLI](/concepts/ai-runtime-cli.md)) supports both workspace-based and git-based code workflows. With a git-based workflow, users define training jobs in [YAML configuration files](/concepts/yaml-based-job-configuration.md) that can be committed to a Git repository, making it easy to track changes, collaborate via pull requests, and integrate with CI/CD pipelines. ^[ai-runtime-cli-databricks-on-aws.md]

The CLI is designed for users who want to submit GPU training workloads from their laptop and code editor without opening a notebook. The YAML job configuration can be checked into source control, preserving a full history of job definitions. ^[ai-runtime-cli-databricks-on-aws.md]

## Benefits

- **Version control**: All training jobs are versioned alongside the code they depend on.
- **Declarative configuration**: YAML files provide a clean, human‑readable definition of job parameters (e.g., number of GPUs, entry point, environment).
- **Reproducibility**: Running a job from a specific Git commit ensures consistent behavior.
- **Collaboration**: Changes to job definitions go through the same review process as code changes.

## Comparison with Workspace-Based Workflows

In workspace-based workflows, code resides in Databricks notebooks stored in the workspace. Git-based workflows shift the primary artifact to files outside the workspace, typically managed through a Git provider such as GitHub, GitLab, or Bitbucket. The AI Runtime CLI accommodates both patterns. ^[ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line tool that submits and manages distributed training jobs.
- [YAML Job Configuration](/concepts/yaml-based-job-configuration.md) – The declarative format used to define training jobs in git-based workflows.
- [MLflow](/concepts/mlflow.md) – Integrated experiment tracking for runs launched via the CLI.
- [Workspace-based code workflows](/concepts/workspace-based-code-workflows.md) – The alternative approach where notebooks are stored in the Databricks workspace.
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md) – Automating training pipelines with Git integration.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
