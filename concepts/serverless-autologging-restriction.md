---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43cf819e5a0b2e631b3b0c3d1e3f78d90c62ddb9ffc3462ee0a81b3cfd397446
  pageDirectory: concepts
  sources:
    - tracing-groq-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-autologging-restriction
    - SAR
  citations:
    - file: tracing-groq-databricks-on-aws.md
title: Serverless Autologging Restriction
description: On Databricks serverless compute clusters, autologging is not automatically enabled and requires explicit invocation
tags:
  - databricks
  - serverless
  - autologging
  - mlflow
timestamp: "2026-06-19T23:11:57.215Z"
---

# Serverless Autologging Restriction

The **Serverless Autologging Restriction** refers to the behavior of [MLflow Tracing](/concepts/mlflow-tracing.md) on Databricks serverless compute clusters, where [Automatic Tracing](/concepts/automatic-tracing.md) integrations are not automatically enabled and require explicit code to activate. This contrasts with non-serverless environments where autologging is typically enabled by default. ^[tracing-groq-databricks-on-aws.md]

## Overview

On serverless compute clusters, [MLflow](/concepts/mlflow.md)'s autologging functionality is not automatically enabled. Users must explicitly call the integration-specific autolog function to enable [Automatic Tracing](/concepts/automatic-tracing.md) for that integration. ^[tracing-groq-databricks-on-aws.md]

## How to Enable

To enable auto-tracing on a serverless compute cluster, explicitly call the autolog function for the specific integration. For example, with Groq Tracing: ^[tracing-groq-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

# Explicitly enable auto-tracing for Groq on serverless compute
[[mlflow|MLflow]].groq.autolog()
```

This explicit call activates automatic trace recording for subsequent usage of the Groq SDK. ^[tracing-groq-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto-tracing can be disabled globally using: ^[tracing-groq-databricks-on-aws.md]

```python
# Disable for a specific integration
[[mlflow|MLflow]].groq.autolog(disable=True)

# Or disable all autologging
[[mlflow|MLflow]].autolog(disable=True)
```

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that provides automatic trace recording
- Groq Tracing — Specific tracing integration for Groq SDK
- Serverless Compute — The compute environment where this restriction applies
- [MLflow Autologging](/concepts/mlflow-autologging.md) — The broader autologging system in [MLflow](/concepts/mlflow.md)

## Sources

- tracing-groq-databricks-on-aws.md

# Citations

1. [tracing-groq-databricks-on-aws.md](/references/tracing-groq-databricks-on-aws-121d088c.md)
