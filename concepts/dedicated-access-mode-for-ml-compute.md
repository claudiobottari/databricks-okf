---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8792ae5231d5aafdae6cc10c2db0b37c468edc5f92da24a1a98d9a8035267dfe
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dedicated-access-mode-for-ml-compute
    - DAMFMC
    - Dedicated Access Mode Compute
    - Dedicated access mode compute
    - Dedicated Access Mode
    - Dedicated Compute
    - Dedicated access mode
    - dedicated compute
    - dedicated group access mode
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Dedicated Access Mode for ML Compute
description: Databricks Runtime ML requires Dedicated access mode for Unity Catalog data access, assigning compute to a single user or group with automatic permission down-scoping, with fine-grained access control available from Runtime 15.4 LTS ML.
tags:
  - security
  - access-control
  - unity-catalog
  - databricks
timestamp: "2026-06-19T14:53:11.406Z"
---

# Dedicated Access Mode for ML Compute

**Dedicated Access Mode for ML Compute** is a security setting on Databricks that restricts a compute resource to a single user or group. It is automatically applied when a compute resource is created with the **Machine learning** checkbox selected in the create compute UI, and is required for accessing data in [Unity Catalog](/concepts/unity-catalog.md) when using [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Overview

When a compute resource has **Dedicated** access mode, it can be assigned to a single user or to a group. If assigned to a group, the user's permissions automatically down‑scope to the group's permissions, allowing the user to securely share the resource with other group members. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Automatic Assignment

In the create compute UI, selecting the **Machine learning** checkbox automatically sets the access mode to **Dedicated** with your account as the dedicated user. You can manually reassign the compute resource to a different user or group in the **Advanced** section of the create compute UI. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Features Supported on Databricks Runtime 15.4 LTS ML and Above

When using dedicated access mode, the following features are only available on Databricks Runtime 15.4 LTS ML and above:

- Fine-grained access control
- Querying tables that were created using [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md), including streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md)

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime that automates ML/DL infrastructure and requires dedicated access mode for Unity Catalog access.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that requires dedicated access mode on ML compute.
- Fine-grained access control — A feature that controls access at the row or column level, available only with dedicated access mode on Runtime 15.4 LTS ML+.
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — A pipeline framework whose tables (streaming tables, materialized views) can be queried with dedicated access mode on Runtime 15.4 LTS ML+.
- Photon — An optional performance engine that can be enabled with Databricks Runtime 15.2 ML and above.
- GPU-based compute — GPU instances can be selected for ML compute; dedicated access mode still applies.
- AutoML and [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) — ML training options available on Databricks Runtime ML, which uses dedicated access mode.

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
