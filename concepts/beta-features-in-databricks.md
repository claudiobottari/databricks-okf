---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ed811f1bd72470df052187ff452412ca1cec788a8ef93070cb0135e4c62d4f3
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - beta-features-in-databricks
    - BFID
    - Legacy features in Databricks
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: Beta features in Databricks
description: Databricks release process designates certain features as Beta, indicating they are not yet generally available and may have limitations.
tags:
  - databricks
  - release-management
  - beta
timestamp: "2026-06-19T13:56:27.105Z"
---

# Beta Features in Databricks

**Beta features** are early-stage capabilities that Databricks releases for customer evaluation. Databricks may limit support for beta features and applies fewer availability guarantees compared to Generally Available (GA) features. Users should not rely on them for production workloads unless explicitly advised otherwise.

## AI Runtime CLI – A Current Beta Feature

The [AI Runtime CLI (`air`)](/concepts/ai-runtime-cli.md) is one example of a Databricks feature currently in Beta. The CLI submits and manages distributed training workloads on [AI Runtime](/concepts/ai-runtime.md), the on-demand serverless GPU compute platform. It supports YAML-based job definitions, integrates with [MLflow](/concepts/mlflow.md), and accepts both workspace-based and git-based code workflows.^[ai-runtime-cli-databricks-on-aws.md]

Because the AI Runtime CLI is in Beta, its API, command set, and behavior may change without a standard deprecation notice.

## Using Beta Features

Databricks typically marks Beta features with a badge or label in the documentation. To identify all current Beta features, see the [Databricks release types](/concepts/databricks-release-types-for-ml-features.md) documentation.

## Related Concepts

- [Databricks release types](/concepts/databricks-release-types-for-ml-features.md) – Describes Beta, Generally Available, and other release stages.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The Beta command-line interface for distributed GPU training.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The infrastructure underlying AI Runtime.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Integration supported by the AI Runtime CLI.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
