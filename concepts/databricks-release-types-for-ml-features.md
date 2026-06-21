---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56db157e7a1658b895573cd0d95a3125a5ea62628bf0f676d0631f0406eeafeb
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-release-types-for-ml-features
    - DRTFMF
    - Databricks release types
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
title: Databricks release types for ML features
description: The distinction between Public Preview and Beta release stages for Databricks machine learning features, indicating maturity and support levels
tags:
  - databricks
  - release-management
  - mlops
timestamp: "2026-06-18T15:13:17.317Z"
---

# Databricks Release Types for ML Features

**Databricks release types for ML features** define the maturity and stability levels of machine learning capabilities within the Databricks platform. These release types help users understand which features are ready for production use and which are still under development.

## Overview

Databricks categorizes its ML features into distinct release types that communicate the feature's stability, support level, and suitability for production workloads. Understanding these release types is essential for planning ML workflows and selecting appropriate tools for different stages of development and deployment. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Release Types

### Public Preview

**Public Preview** features are available for use in production environments but may have limitations in terms of functionality, performance, or support. These features are considered stable enough for broader testing and adoption, though users should be aware that changes may occur before general availability. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

Features in Public Preview include:
- [AI Runtime](/concepts/ai-runtime.md) for single-node tasks
- Various ML evaluation and monitoring capabilities

### Beta

**Beta** features are earlier-stage releases that are available for testing and feedback but are not recommended for production use. Beta features may have incomplete functionality, known issues, or significant changes planned before reaching a stable release. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

Features in Beta include:
- Distributed training APIs for multi-GPU workloads
- Experimental ML capabilities

## Feature Examples by Release Type

| Feature | Release Type | Description |
|---------|-------------|-------------|
| AI Runtime (single-node) | Public Preview | Runtime optimized for single-node ML tasks |
| Distributed Training API (multi-GPU) | Beta | API for training models across multiple GPUs |

^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Best Practices

- **Production workloads**: Use features in Public Preview or General Availability (GA) for production deployments.
- **Experimentation**: Beta features are suitable for prototyping and providing feedback to Databricks.
- **Monitoring**: Track release notes for changes to feature maturity levels, as features may transition between release types over time.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The ML-optimized runtime environment for Databricks
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Multi-GPU training capabilities
- [MLflow](/concepts/mlflow.md) – ML lifecycle management platform
- Databricks Release Notes – Official documentation for release changes

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
