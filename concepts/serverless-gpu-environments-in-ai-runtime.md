---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42f720e9b75279e09c44f110c6a5f81e07e8611cfce9f6275c20f98adf975a74
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-environments-in-ai-runtime
    - SGEIAR
    - GPU Environment on AI Runtime
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Serverless GPU Environments in AI Runtime
description: Pre-configured serverless GPU compute environments (e.g., GPU_1xA10) with selectable environment versions that run training workloads without managing infrastructure.
tags:
  - compute
  - gpu
  - serverless
  - databricks
timestamp: "2026-06-18T10:44:04.022Z"
---

Here is the wiki page for "Serverless GPU Environments in AI Runtime".

---

---
title: Serverless GPU Environments in AI Runtime
summary: Pre-configured, automatically managed GPU environments used by the AI Runtime CLI to execute training workloads without manual cluster setup or dependency management.
sources:
  - ai-runtime-cli-quickstart-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:35:53.100Z"
updatedAt: "2026-06-18T10:35:53.100Z"
tags:
  - serverless
  - gpu
  - ai-runtime
  - databricks
  - environments
aliases:
  - serverless-gpu-environments
  - serverless-environment-versions
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Serverless GPU Environments in AI Runtime

**Serverless GPU environments** are pre-configured, automatically managed runtime environments used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) to execute machine learning workloads. When you submit a training job via `air run`, the AI Runtime provisions a serverless compute cluster with the specified GPU resources and the selected environment version, without requiring you to manually configure clusters, install drivers, or manage dependencies. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Environment versions

Serverless GPU environments are versioned. The environment version determines the set of pre-installed libraries, CUDA drivers, and system tools available on the compute nodes. You specify the environment version in your [Workload YAML](/concepts/workload-yaml-configuration.md) configuration under the `environment.version` field. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

The current default version is `'4'`. If you omit the `environment.version` field, version `'4'` is used. You can pin a specific version to ensure reproducibility across runs:

```yaml
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
```

^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Dependency management

In addition to the pre-configured environment, you can specify additional Python dependencies in the `environment.dependencies` list. These are installed on top of the base environment at the start of each run. This allows you to extend the environment with libraries specific to your workload without building custom container images. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Available versions

For all available serverless environment versions and their contents, see [Serverless environment versions](/concepts/serverless-environment-versioning.md) in the release notes. Databricks recommends reviewing the version notes when upgrading to understand what has changed. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Best practices

- **Pin the environment version** in your workload YAML to ensure reproducibility. Without a pin, a future run may use a different default version. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]
- **List only additional dependencies** in `environment.dependencies`. The base environment includes common ML frameworks and system tools; adding only what you need keeps installations fast. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]
- **Test with `--dry-run`** to validate your configuration before submitting a GPU-bound workload. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The tool that submits workloads to serverless GPU environments
- [Workload YAML](/concepts/workload-yaml-configuration.md) — The configuration format that specifies environment and compute settings
- [AI Runtime](/concepts/ai-runtime.md) — The underlying runtime that hosts serverless GPU environments
- [Serverless environment versions](/concepts/serverless-environment-versioning.md) — Complete list of available environment versions and their contents
- Compute specification in Workload YAML — How to specify GPU count and type in your workload definition

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
