---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74a5840ecb5987b25e676ab8c438cf9ef3b5ec87ae8499578a62e63035de24f4
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - jobs-api-and-databricks-asset-bundles-for-ai-runtime
    - Databricks Asset Bundles for AI Runtime and Jobs API
    - JAADABFAR
    - Jobs API and Databricks Asset Bundles
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Jobs API and Databricks Asset Bundles for AI Runtime
description: Programmatic creation and management of AI Runtime jobs using the Databricks Jobs API or Asset Bundles with YAML configuration
tags:
  - databricks
  - API
  - infrastructure-as-code
timestamp: "2026-06-19T17:51:28.088Z"
---

Here is the wiki page for "Jobs API and Databricks Asset Bundles for AI Runtime", written based solely on the provided source material.

---

## Jobs API and Databricks Asset Bundles for AI Runtime

**Jobs API and Databricks Asset Bundles for AI Runtime** refers to the programmatic mechanisms for creating, configuring, and managing [AI Runtime](/concepts/ai-runtime.md) jobs on Databricks. By using the Databricks Jobs API or Databricks Asset Bundles, you can automate deployment pipelines that run AI Runtime workloads on serverless GPU compute.

### Overview

You can programmatically create and manage AI Runtime jobs using the Databricks Jobs API or Databricks Asset Bundles. Configure the compute type as serverless GPU in your job or bundle definition to automate deployment pipelines. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Databricks Asset Bundle Configuration

The following YAML example shows a Databricks Asset Bundle configuration for an AI Runtime job on serverless GPU using the Default Environment|default base environment:

```yaml
resources:
  jobs:
    sample_job:
      name: sample_job_h100
      trigger:
        periodic:
          interval: 1
          unit: DAYS
      parameters:
        - name: catalog
          default: ${var.catalog}
        - name: schema
          default: ${var.schema}
      environments:
        - environment_key: default
          spec:
            environment_version: '4'
      tasks:
        - task_key: notebook_task
          notebook_task:
            notebook_path: /Workspace/Users/your_email/your_notebook
          environment_key: default
          compute:
            hardware_accelerator: GPU_8xH100
```

^[connect-to-ai-runtime-databricks-on-aws.md]

To use the [AI Environment](/concepts/ai-runtime-environments.md) (for example, AI v5) instead of the default base environment, set `base_environment` to the AI environment identifier in the environment `spec` and reference it from the task’s `environment_key`:

```yaml
resources:
  jobs:
    sample_job:
      name: sample_job_aiv5_h100
      trigger:
        periodic:
          interval: 1
          unit: DAYS
      parameters:
        - name: catalog
          default: ${var.catalog}
        - name: schema
          default: ${var.schema}
      environments:
        - environment_key: aiv5
          spec:
            base_environment: databricks_ai_v5
      tasks:
        - task_key: notebook_task
          notebook_task:
            notebook_path: /Workspace/Users/your_email/your_notebook
          environment_key: aiv5
          compute:
            hardware_accelerator: GPU_8xH100
```

^[connect-to-ai-runtime-databricks-on-aws.md]

### Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The runtime environment for single-node and multi-GPU deep learning tasks.
- [Serverless GPU](/concepts/serverless-gpu-compute.md) – The compute type used by AI Runtime jobs; see [Hardware options](/concepts/ai-runtime-hardware-options.md).
- Databricks Jobs API – REST API for creating and managing jobs programmatically.
- Databricks Asset Bundles – Infrastructure-as-code tool for defining and deploying Databricks resources.
- Default Environment – The base environment (`environment_version: '4'`) for serverless GPU.
- [AI Environment](/concepts/ai-runtime-environments.md) – Pre-configured environment (e.g., `databricks_ai_v5`) with additional libraries and dependencies.

### Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
