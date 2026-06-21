---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4931e30c48fd7306788b0695c2c3be1d529d8fcc24629776eba7a3f9f33b291
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - yaml-based-job-configuration-for-ai-runtime
    - YJCFAR
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: YAML-based job configuration for AI Runtime
description: Declarative YAML configuration format used by the AI Runtime CLI to define training jobs, enabling source-control integration.
tags:
  - yaml
  - configuration
  - devops
timestamp: "2026-06-18T10:42:51.334Z"
---

# YAML-based job configuration for AI Runtime

The **YAML-based job configuration** is a core feature of the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (Beta). It allows users to define distributed training workloads on [AI Runtime](/concepts/ai-runtime.md) — the on-demand serverless GPU compute platform — using a declarative YAML file that can be checked into source control. The CLI integrates with [MLflow](/concepts/mlflow.md) for tracking and supports both workspace-based and git-based code workflows.^[ai-runtime-cli-databricks-on-aws.md]

## Purpose and benefits

Declarative job configuration lets you specify the compute resources, code, environment, and runtime parameters for a training run in a single file. This enables reproducibility, version control, and automation. Rather than configuring a job interactively in a notebook, you write a YAML file and submit it with the `air run` command.^[ai-runtime-cli-databricks-on-aws.md]

## Where to find the full YAML reference

Detailed documentation of every supported YAML field — including `compute`, `code`, `environment`, `model`, `experiment`, and `run_config` — is available in the dedicated **Workload YAML reference**. That reference describes the schema, data types, constraints, and examples for each configuration section.^[ai-runtime-cli-databricks-on-aws.md]

## How YAML configuration fits into the CLI workflow

1. **Write** a YAML configuration file (e.g., `workload.yaml`) that defines the training job.
2. **Submit** the job with `air run workload.yaml`.
3. **Monitor** the run using `air get run`, `air list runs`, or `air logs`.
4. **Cancel** the run if needed with `air cancel`.^[ai-runtime-cli-databricks-on-aws.md]

The CLI also supports workspace‑based code (code stored in Databricks Repos or workspace files) and git‑based code (code pulled from a remote repository), both specified in the YAML configuration.^[ai-runtime-cli-databricks-on-aws.md]

## When to use YAML job configuration

Use the YAML‑based approach when you want to:

- Submit GPU training workloads from your laptop or code editor without opening a notebook.
- Store job definitions in source control for traceability and reuse.

If you prefer an in‑notebook Python API, use the `@distributed` or `@ray_launch` decorators instead of the CLI and YAML configuration.^[ai-runtime-cli-databricks-on-aws.md]

## Related concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command‑line interface that consumes the YAML configuration
- [air run command](/concepts/air-run-command.md) — The command that submits a YAML‑defined workload
- Workload YAML reference — Complete field‑by‑field documentation of the YAML schema
- AI Runtime CLI quickstart — Step‑by‑step guide to creating and running a YAML‑based job
- [AI Runtime](/concepts/ai-runtime.md) — The serverless GPU compute platform on Databricks
- [MLflow](/concepts/mlflow.md) — Experiment tracking integrated with AI Runtime jobs

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
