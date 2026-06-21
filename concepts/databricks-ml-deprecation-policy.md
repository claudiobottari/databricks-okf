---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 335455f3732a88cd1f0cd6e5290338dd49e7fac4e994f6f3cb4fe799704bb6fd
  pageDirectory: concepts
  sources:
    - horovodrunner-examples-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-ml-deprecation-policy
    - DMDP
  citations:
    - file: horovodrunner-examples-databricks-on-aws.md
title: Databricks ML Deprecation Policy
description: The practice of removing pre-installed packages like Horovod after specific ML runtime versions (15.4 LTS ML and later).
tags:
  - databricks
  - mlops
  - lifecycle
timestamp: "2026-06-19T10:48:22.867Z"
---

# Databricks ML Deprecation Policy

**Databricks ML Deprecation Policy** defines the lifecycle for machine learning libraries, tools, and APIs that are pre-installed or officially supported in the Databricks platform. The policy governs when components are announced as deprecated, when support is removed, and what replacement technologies are recommended.

## Overview

Databricks periodically deprecates machine learning libraries and tools as newer, more capable alternatives become available. Deprecated components continue to function for a limited time but are no longer updated, and may be removed from future runtime releases. Users are expected to migrate to the recommended replacements before the deprecation period ends. ^[horovodrunner-examples-databricks-on-aws.md]

## Current Deprecation Status

### Horovod and HorovodRunner

**Horovod** and **HorovodRunner** are now deprecated as of the current documentation. These packages will not be pre-installed in releases after Databricks Runtime 15.4 LTS ML. ^[horovodrunner-examples-databricks-on-aws.md]

## Replacement Recommendations

When a component is deprecated, Databricks provides guidance on the recommended replacement tools. Users should plan their migration accordingly:

| Deprecated Component | Recommended Replacement |
|---------------------|------------------------|
| Horovod / HorovodRunner (PyTorch) | [TorchDistributor](/concepts/torchdistributor.md) |
| Horovod / HorovodRunner (TensorFlow) | `tf.distribute.Strategy` API |

^[horovodrunner-examples-databricks-on-aws.md]

### TorchDistributor

For distributed deep learning with PyTorch, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md). This tool provides native PyTorch distributed training capabilities that integrate with the Databricks platform. ^[horovodrunner-examples-databricks-on-aws.md]

### TensorFlow Distributed Strategy API

For distributed training with TensorFlow, Databricks recommends using the `tf.distribute.Strategy` API. This TensorFlow-native approach provides distributed training capabilities without requiring third-party tools like Horovod. ^[horovodrunner-examples-databricks-on-aws.md]

## Policy Implications

Users currently relying on deprecated components should:

1. **Identify dependencies**: Audit notebooks and code for usage of deprecated libraries such as Horovod and HorovodRunner.
2. **Plan migration**: Develop a migration plan to the recommended replacements before the deprecation window closes.
3. **Test thoroughly**: Validate that migrated code produces equivalent results in terms of model accuracy and training performance.
4. **Update runtime configurations**: Ensure that jobs are configured to use Databricks Runtime versions that still support the deprecated component during the transition period.

## Runtime Version Impact

The deprecation policy is tied to specific Databricks Runtime versions. After a certain release (15.4 LTS ML for Horovod), deprecated packages are no longer pre-installed. Users who upgrade to newer runtime versions may find that the deprecated libraries are absent and must use the recommended alternatives. ^[horovodrunner-examples-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The ML-specific runtime that bundles deep learning libraries and tools.
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) — Overview of distributed training approaches available on the platform.
- [TorchDistributor](/concepts/torchdistributor.md) — The recommended PyTorch distributed training tool.
- [HorovodRunner](/concepts/horovodrunner.md) — The deprecated distributed training framework (legacy).
- [Horovod](/concepts/horovod.md) — The deprecated distributed deep learning framework (legacy).
- [TensorFlow Distributed Strategy](/concepts/tensorflowdistributestrategy.md) — The recommended TensorFlow distributed training API.

## Sources

- horovodrunner-examples-databricks-on-aws.md

# Citations

1. [horovodrunner-examples-databricks-on-aws.md](/references/horovodrunner-examples-databricks-on-aws-de1151e3.md)
