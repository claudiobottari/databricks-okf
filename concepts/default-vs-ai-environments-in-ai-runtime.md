---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9644f41df3f2bf209a71500602c6be3a4187dcf8bd2f8febd67f7e6bd620d7e1
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-vs-ai-environments-in-ai-runtime
    - DVAEIAR
    - default environment
    - base-environment-vs-ai-environment-in-ai-runtime
    - BEVAEIAR
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Default vs AI Environments in AI Runtime
description: "Two base environment options: 'None' (default environment) and 'AI v4/v5' (Databricks AI environment), configurable in notebook and job definitions."
tags:
  - databricks
  - environments
  - ai-runtime
timestamp: "2026-06-18T14:43:46.325Z"
---

# Default vs AI Environments in AI Runtime

**Default vs AI Environments in AI Runtime** describes the two base environment options available when connecting to [AI Runtime](/concepts/ai-runtime.md) on Databricks. When configuring AI Runtime for serverless GPU workloads—whether from interactive notebooks, scheduled jobs, or the Jobs API—you can choose between the **default environment** and the **AI environment** (e.g., AI v4 or AI v5). ^[connect-to-ai-runtime-databricks-on-aws.md]

## Overview

When setting up the environment for an AI Runtime notebook or job, the **Base environment** field offers two choices:

- **None** – Selects the [default environment](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment#default-env) for AI Runtime.
- **AI v4** (or **AI v5**) – Selects the [AI environment](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment#ai-env).

Both environments provide the foundational runtime for serverless GPU workloads, but they differ in the pre-installed packages and configurations they include. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Default Environment

The default environment is the standard base environment for AI Runtime. It is selected by setting the **Base environment** to **None** in the Environment side panel. ^[connect-to-ai-runtime-databricks-on-aws.md]

In the Jobs API and Databricks Asset Bundles, the default environment is specified by omitting the `base_environment` field from the environment `spec`, or by setting `environment_version: '4'` without a `base_environment`:

```yaml
environments:
  - environment_key: default
    spec:
      environment_version: '4'
```

^[connect-to-ai-runtime-databricks-on-aws.md]

## AI Environment

The AI environment is a specialized base environment that includes additional pre-installed packages and configurations for AI/ML workloads. It is selected by setting the **Base environment** to **AI v4** (or **AI v5**) in the Environment side panel. ^[connect-to-ai-runtime-databricks-on-aws.md]

In Databricks Asset Bundles, the AI environment is specified by setting `base_environment` to the appropriate identifier, such as `databricks_ai_v5` for AI v5:

```yaml
environments:
  - environment_key: aiv5
    spec:
      base_environment: databricks_ai_v5
```

The task then references this environment key in its `environment_key` field:

```yaml
tasks:
  - task_key: notebook_task
    notebook_task:
      notebook_path: /Workspace/Users/your_email/your_notebook
    environment_key: aiv5
    compute:
      hardware_accelerator: GPU_8xH100
```

^[connect-to-ai-runtime-databricks-on-aws.md]

## Key Differences

| Aspect | Default Environment | AI Environment |
|--------|--------------------|----------------|
| Selection in UI | **Base environment** set to **None** | **Base environment** set to **AI v4** (or **AI v5**) |
| Bundle configuration | `environment_version: '4'` without `base_environment` | `base_environment: databricks_ai_v5` |
| Pre-installed packages | Minimal set for basic runtime | Expanded set for AI/ML workloads |
| Use case | General-purpose serverless GPU workloads | Workloads requiring AI-specific libraries |

^[connect-to-ai-runtime-databricks-on-aws.md]

## Choosing Between Environments

The choice depends on the specific requirements of your workload:

- Use the **default environment** for general-purpose serverless GPU tasks where you want to install only the dependencies you need.
- Use the **AI environment** when your workload benefits from pre-installed AI/ML libraries, reducing the need for additional package installations.

For jobs, dependencies can be installed programmatically within the notebook (e.g., `%pip install`), as the Environments panel is not supported for serverless GPU scheduled jobs. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The serverless GPU compute environment for AI/ML workloads
- Connect to AI Runtime – How to connect from notebooks, jobs, and APIs
- Databricks Asset Bundles – Infrastructure-as-code for deploying Databricks resources
- Hardware Options for AI Runtime – Available accelerators like 8xH100

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
