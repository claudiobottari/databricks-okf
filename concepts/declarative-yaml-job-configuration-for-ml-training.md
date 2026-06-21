---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4315713951f57286526ce0b0c7d11c1584892e8c4fcc80fb96bacbc35cf8d428
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-yaml-job-configuration-for-ml-training
    - DYJCFMT
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: Declarative YAML Job Configuration for ML Training
description: The pattern of defining ML training jobs declaratively in YAML configuration files that can be checked into source control
tags:
  - yaml
  - mlops
  - configuration-management
  - reproducibility
timestamp: "2026-06-19T22:01:57.099Z"
---

```yaml
---
title: Declarative YAML Job Configuration for ML Training
summary: Defining training jobs declaratively in YAML so they can be checked into source control, used by the AI Runtime CLI.
sources:
  - ai-runtime-cli-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:21:26.237Z"
updatedAt: "2026-06-18T14:21:26.237Z"
tags:
  - databricks
  - yaml
  - mlops
  - configuration
aliases:
  - declarative-yaml-job-configuration-for-ml-training
  - DYJCFMT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Declarative YAML Job Configuration for ML Training

**Declarative YAML Job Configuration for ML Training** is a configuration-driven approach to defining and submitting machine learning training workloads using YAML files. This method allows practitioners to specify training job parameters in a structured, version-controllable format, rather than through imperative code or notebook-based workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## Overview

The [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) is the primary interface for declarative YAML job configuration on Databricks. It submits and manages distributed training workloads on AI Runtime, an on-demand serverless GPU compute platform. The CLI uses YAML-based job configuration, integrates with [MLflow Tracking](/concepts/mlflow-tracking.md), and supports workspace-based and git-based code workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## When to Use

Use the AI Runtime CLI with YAML configuration when you want to:

- Submit GPU training workloads from your laptop and code editor without opening a notebook. ^[ai-runtime-cli-databricks-on-aws.md]
- Define training jobs declaratively in YAML so they can be checked into source control. ^[ai-runtime-cli-databricks-on-aws.md]

## Benefits

- **Version control**: YAML files can be committed to git repositories, enabling change tracking, code review, and rollback. ^[ai-runtime-cli-databricks-on-aws.md]
- **Declarative syntax**: Focus on *what* the job should look like, not *how* to execute it. The CLI handles orchestration on the target compute platform. ^[ai-runtime-cli-databricks-on-aws.md]
- **Separation from notebooks**: Works directly from a code editor, avoiding the need to open a notebook for GPU training submission. ^[ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line interface that reads and submits YAML configurations.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment management integrated with YAML job configurations.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Multi-GPU workloads that can be configured via YAML.
- [Git-Based Workflows](/concepts/git-based-code-workflows.md) – Code management approach supported by declarative YAML configurations.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – Full specification of YAML configuration fields used by the CLI.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
