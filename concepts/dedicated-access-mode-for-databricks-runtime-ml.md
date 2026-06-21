---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1835bd2d8964d75ca9798ee38ef7e085e62f840fdf46129be330acc0075f416a
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dedicated-access-mode-for-databricks-runtime-ml
    - DAMFDRM
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Dedicated Access Mode for Databricks Runtime ML
description: A required access mode for Unity Catalog access on Databricks Runtime ML, automatically set when selecting Machine Learning compute, which can be scoped to a single user or group.
tags:
  - databricks
  - security
  - access-control
  - unity-catalog
timestamp: "2026-06-19T18:14:51.589Z"
---

```markdown
---
title: Dedicated Access Mode for Databricks Runtime ML
summary: The required compute access mode for accessing Unity Catalog data, automatically set when selecting Machine Learning, supporting single-user or group assignment with automatic permission down-scoping.
sources:
  - databricks-runtime-for-machine-learning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:41:19.824Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - security
  - access-control
  - databricks
  - unity-catalog
aliases:
  - dedicated-access-mode-for-databricks-runtime-ml
  - DAMFDRM
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# Dedicated Access Mode for Databricks Runtime ML

**Dedicated Access Mode** is the mandatory compute access mode for accessing data in [[Unity Catalog]] on any compute resource running [[Databricks Runtime ML]]. When you create a compute resource with the **Machine learning** checkbox selected, the access mode is automatically set to **Dedicated** with your account as the dedicated user. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Overview

In dedicated access mode, the compute resource can be assigned to a single user or to a group. If the resource is assigned to a group, the user’s permissions automatically down‑scope to the group’s permissions. This allows the user to securely share the resource with other members of the group without granting broader access. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

You can manually reassign the compute resource to a different user or group in the **Advanced** section of the create compute UI. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Requirements

To access data in Unity Catalog on a compute resource running Databricks Runtime ML, you **must** set the access mode to **Dedicated**. This is enforced automatically when you select the **Machine learning** checkbox during compute creation. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Feature Availability

When using dedicated access mode, the following features are available only on **Databricks Runtime 15.4 LTS ML and above**: ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- Fine-grained access control – Granular permission management for data access.
- Querying tables created using [[Lakeflow Spark Declarative Pipelines]], which includes streaming tables and [[Materialized views in Databricks|materialized views]].

## Related Concepts

- [[Databricks Runtime ML]] – The pre‑configured runtime for machine learning workloads.
- [[Unity Catalog]] – The unified data governance solution on Databricks.
- Compute access modes – Overview of all access modes available in the Databricks compute model.
- Fine-grained access control – Advanced permission management for dedicated mode.
- Photon – Performance engine that can be enabled with Databricks Runtime 15.2 ML and above.

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md
```

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
