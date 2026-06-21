---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ecacc5063448bc326638a26339a02c8bdffa830227fc804accc0f92891a29982
  pageDirectory: concepts
  sources:
    - tracing-anthropic-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-anthropic-autolog-disable
    - MAAD
  citations:
    - file: tracing-anthropic-databricks-on-aws.md
title: MLflow Anthropic Autolog Disable
description: Mechanism to globally disable automatic tracing for Anthropic via mlflow.anthropic.autolog(disable=True) or mlflow.autolog(disable=True)
tags:
  - mlflow
  - tracing
  - anthropic
  - configuration
timestamp: "2026-06-19T23:09:36.927Z"
---

# [MLflow Anthropic Autolog](/concepts/mlflow-anthropic-autolog.md) Disable

**MLflow Anthropic Autolog Disable** refers to the mechanism for turning off [MLflow Tracing](/concepts/mlflow-tracing.md)](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) for Anthropic LLM calls after it has been enabled. This allows users to stop automatic trace logging to the active [MLflow Experiment](/concepts/mlflow-experiment.md) when tracing is no longer needed, or to prevent tracing in specific code paths without affecting other autolog integrations.

## Overview

[MLflow Tracing](/concepts/mlflow-tracing.md)](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) provides [Automatic Tracing](/concepts/automatic-tracing.md) capability for Anthropic LLMs. When enabled via `mlflow.anthropic.autolog()`, [MLflow](/concepts/mlflow.md) captures nested [Traces](/concepts/traces.md) upon invocation of the Anthropic Python SDK, including prompts, completion responses, latencies, model names, and metadata such as `temperature` and `max_tokens`. Disabling autolog stops this automatic trace capture. ^[tracing-anthropic-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto tracing for Anthropic can be disabled globally by calling either of the following methods: ^[tracing-anthropic-databricks-on-aws.md]

- `mlflow.anthropic.autolog(disable=True)` — Disables autolog specifically for the Anthropic integration.
- `mlflow.autolog(disable=True)` — Disables autolog globally for all supported integrations, including Anthropic.

### Example

```python
import [[mlflow|MLflow]]

# Enable auto-tracing for Anthropic
[[mlflow|MLflow]].anthropic.autolog()

# ... Anthropic SDK calls are traced ...

# Disable auto-tracing specifically for Anthropic
[[mlflow|MLflow]].anthropic.autolog(disable=True)
```

^[tracing-anthropic-databricks-on-aws.md]

## Behavior

When autolog is disabled, [MLflow](/concepts/mlflow.md) will no longer automatically capture [Traces](/concepts/traces.md) from subsequent calls to the Anthropic Python SDK. Disabling autolog does not affect existing [Traces](/concepts/traces.md) that have already been logged to the experiment. To resume tracing after disabling, call `mlflow.anthropic.autolog()` again without the `disable` argument. ^[tracing-anthropic-databricks-on-aws.md]

## Related Concepts

- [MLflow Anthropic Autolog](/concepts/mlflow-anthropic-autolog.md) — The mechanism for enabling [Automatic Tracing](/concepts/automatic-tracing.md) of Anthropic LLM calls.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader framework for capturing and logging LLM invocation [Traces](/concepts/traces.md).
- [MLflow Autolog](/concepts/mlflow-autologging.md) — The general autolog mechanism for automatic [MLflow](/concepts/mlflow.md) instrumentation.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where [Traces](/concepts/traces.md) are logged.
- [MLflow Anthropic Integrations](/concepts/mlflow-anthropic-autolog.md) — The full set of tracing capabilities for Anthropic models.

## Sources

- tracing-anthropic-databricks-on-aws.md

# Citations

1. [tracing-anthropic-databricks-on-aws.md](/references/tracing-anthropic-databricks-on-aws-085cde5b.md)
