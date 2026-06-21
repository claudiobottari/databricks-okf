---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41bc7e097aa1bea494f746d3d0c2cae06140b377fbc5b7fb88a672a8841597fa
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - workspace-based-code-workflows
    - WCW
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: Workspace-based code workflows
description: Approach for submitting training workloads using code stored in the Databricks workspace.
tags:
  - databricks
  - workflow
  - code-management
timestamp: "2026-06-19T17:30:14.590Z"
---

# Workspace-based Code Workflows

**Workspace-based code workflows** refer to one of the code submission methods supported by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) on Databricks. When using a workspace-based workflow, the CLI runs training jobs directly from code stored in the Databricks workspace (such as notebooks or Python scripts), rather than from an external Git repository. ^[ai-runtime-cli-databricks-on-aws.md]

## Context

The AI Runtime CLI (`air`) is a command‑line tool for submitting and managing distributed training workloads on the serverless GPU platform. It accepts YAML job configurations, integrates with [MLflow](/concepts/mlflow.md) for experiment tracking, and supports both workspace‑based and git‑based code workflows. The workspace‑based approach allows users to reference code that already exists in the Databricks workspace, eliminating the need to clone or manage a separate Git repository. ^[ai-runtime-cli-databricks-on-aws.md]

## Usage

When defining a workload in the CLI, users can specify the source of their training code. A workspace‑based workflow typically points to a path in the workspace (e.g., `/Users/.../train.py` or a notebook path). The CLI then uploads or directly references that workspace‑hosted code for execution on the cluster. The exact configuration syntax is covered in the [Workload YAML reference](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config). ^[ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The CLI that provides workspace‑based and git‑based workflows.
- [Git-based code workflows](/concepts/git-based-code-workflows.md) — The alternative workflow that references code from a Git repository.
- Workspace — The Databricks environment where notebooks and files are stored.
- [AI Runtime](/concepts/ai-runtime.md) — The serverless GPU compute platform on which the CLI runs jobs.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
