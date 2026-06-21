---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8733e1b5594187ecd1bd2cd5889469a39ae244451918f3384f7447ddc5b3fe5c
  pageDirectory: concepts
  sources:
    - tracing-groq-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-autolog-disable-mechanism
    - MADM
  citations:
    - file: tracing-groq-databricks-on-aws.md
title: MLflow Autolog Disable Mechanism
description: Method to globally disable automatic tracing for Groq via mlflow.groq.autolog(disable=True) or mlflow.autolog(disable=True)
tags:
  - mlflow
  - autologging
  - configuration
timestamp: "2026-06-19T23:12:09.146Z"
---

# [MLflow](/concepts/mlflow.md) Autolog Disable Mechanism

The **MLflow Autolog Disable Mechanism** is a built‑in feature that allows users to globally or selectively turn off [Automatic Tracing](/concepts/automatic-tracing.md) (and other autologging behavior) for [MLflow](/concepts/mlflow.md) integrations. The mechanism is controlled by the `disable` parameter of the `autolog` function.

## Mechanism

To disable auto‑tracing, call the `autolog` function with `disable=True`. This works at two levels:  

1. **Integration‑specific** – For example, `mlflow.groq.autolog(disable=True)` disables tracing for the Groq integration only.  
2. **Global** – Calling `mlflow.autolog(disable=True)` disables autologging for all registered integrations.  

Once set, the disable flag persists for the lifetime of the Python process (or until re‑enabled by calling `autolog()` again without the disable flag). ^[tracing-groq-databricks-on-aws.md]

## Usage Example

```python
import [[mlflow|MLflow]]

# Disable auto‑tracing for Groq specifically
[[mlflow|MLflow]].groq.autolog(disable=True)

# Or disable autologging for all integrations
[[mlflow|MLflow]].autolog(disable=True)
```

## Important Notes

- On serverless compute clusters, autologging is not automatically enabled. Users must explicitly call `mlflow.groq.autolog()` (without disable) to enable tracing. The disable mechanism is still available to turn it off when needed. ^[tracing-groq-databricks-on-aws.md]

- The disable parameter works for synchronous tracing only; asynchronous API and streaming methods are not traced regardless of the disable setting. ^[tracing-groq-databricks-on-aws.md]

## Related Concepts

- [MLflow Autolog](/concepts/mlflow-autologging.md) – General autologging framework.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – How [Traces](/concepts/traces.md) are generated and recorded.
- Tracing Groq – Specific integration for Groq SDK calls.

## Sources

- tracing-groq-databricks-on-aws.md

# Citations

1. [tracing-groq-databricks-on-aws.md](/references/tracing-groq-databricks-on-aws-121d088c.md)
