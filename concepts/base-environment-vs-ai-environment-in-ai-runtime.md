---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d072fd6d4caba31d94e947678e7521d22da7d758cd09935635b09e09339cb6c8
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - base-environment-vs-ai-environment-in-ai-runtime
    - BEVAEIAR
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Base Environment vs AI Environment in AI Runtime
description: "Two environment options for AI Runtime: the default base environment (None) and the pre-configured AI environment (AI v4 / databricks_ai_v5)"
tags:
  - databricks
  - environments
  - configuration
timestamp: "2026-06-19T17:52:02.764Z"
---

# Base Environment vs AI Environment in AI Runtime

**Base Environment vs AI Environment in AI Runtime** refers to the two distinct environment options available when configuring [AI Runtime](/concepts/ai-runtime.md) for serverless GPU compute on Databricks. These environments determine which pre-installed libraries and frameworks are available for machine learning and deep learning workloads.

## Overview

When connecting to AI Runtime, users can choose between two base environment options from the **Base environment** field in the Environment side panel: **None** (which selects the default base environment) or an **AI environment** (such as **AI v4** or **AI v5**). ^[connect-to-ai-runtime-databricks-on-aws.md]

## Default Base Environment

The default base environment is selected when you choose **None** for the base environment. This environment provides a standard set of libraries optimized for general-purpose GPU computing but does not include the specialized AI/ML frameworks bundled with the AI environment. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Using the Default Environment

In the UI, select **None** from the **Base environment** field when configuring your notebook environment. ^[connect-to-ai-runtime-databricks-on-aws.md]

In Databricks Asset Bundles, specify the environment version without a base environment reference:

```yaml
environments:
  - environment_key: default
    spec:
      environment_version: '4'
```

^[connect-to-ai-runtime-databricks-on-aws.md]

## AI Environment

The AI environment is a pre-configured environment that includes additional libraries and tools specifically for AI and machine learning workloads. Available versions include **AI v4** (selected in the UI as **AI v4**) and **AI v5** (referenced programmatically as `databricks_ai_v5`). ^[connect-to-ai-runtime-databricks-on-aws.md]

### Using the AI Environment

In the UI, select **AI v4** (or the appropriate version) from the **Base environment** field. ^[connect-to-ai-runtime-databricks-on-aws.md]

In Databricks Asset Bundles, set `base_environment` to the AI environment identifier:

```yaml
environments:
  - environment_key: aiv5
    spec:
      base_environment: databricks_ai_v5
```

^[connect-to-ai-runtime-databricks-on-aws.md]

## Key Differences

| Aspect | Default Base Environment | AI Environment |
|--------|-------------------------|----------------|
| **UI Selection** | **None** | **AI v4** (or later version) |
| **Bundle Identifier** | `environment_version: '4'` | `base_environment: databricks_ai_v5` |
| **Library Set** | Standard GPU libraries | Specialized AI/ML frameworks |
| **Use Case** | General GPU workloads | AI-specific workloads |

^[connect-to-ai-runtime-databricks-on-aws.md]

## Selecting the Right Environment

- Choose the **default base environment** for workloads that do not require specialized AI frameworks or when you need full control over package installations.
- Choose the **AI environment** for AI and machine learning workloads that benefit from pre-installed libraries like PyTorch, TensorFlow, Transformers, and other ML frameworks.

Both environments support the same hardware accelerator options, including [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) for multi-GPU distributed training. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Configuration in Jobs and Bundles

For scheduled jobs using Databricks Asset Bundles, the environment configuration differs between the two options:

- **Default environment**: Set `environment_version` in the environment spec without specifying `base_environment`.
- **AI environment**: Set `base_environment` to the AI environment identifier (e.g., `databricks_ai_v5`) and reference it from the task's `environment_key`.

^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- Databricks Asset Bundles

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
