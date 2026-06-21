---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44f742734dc06f5297444b0257fe80998dea41c7764edbd933ecd28498e1a825
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - memalign-optimizer
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: MemAlign Optimizer
description: The default alignment optimizer used by MLflow's judge alignment system, automatically applied when calling align() without specifying an optimizer.
tags:
  - optimizer
  - mlflow
  - alignment
timestamp: "2026-06-19T17:32:14.414Z"
---

# MemAlign Optimizer

**MemAlign Optimizer** is the default optimization algorithm used when calling the `align()` method on an [LLM judge](/concepts/llm-judges.md) without explicitly specifying an optimizer. It is designed to improve agreement between automated judges and human assessments by 30 to 50 percent compared to baseline judges. ^[align-judges-with-humans-databricks-on-aws.md]

## Overview

The MemAlign Optimizer is included in the `mlflow.genai.judges.optimizers` package within the [MLflow](/concepts/mlflow.md) GenAI evaluation framework. When the `align()` method is called without specifying an optimizer, the MemAlign optimizer is automatically used as the default. ^[align-judges-with-humans-databricks-on-aws.md]

This optimizer is part of the standard [Judge Alignment](/concepts/judge-alignment.md) workflow, which transforms generic evaluators into domain-specific experts that understand unique quality criteria. The alignment process can improve judge performance on both [Built-in Judges](/concepts/built-in-judges.md) (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [Custom Judges](/concepts/custom-judges.md) created with `make_judge()`.

## How It Works

The MemAlign Optimizer is automatically invoked when calling `align()` on a judge without specifying an optimizer:

```python
aligned_judge = initial_judge.align(traces_for_alignment)
```

To use an explicit optimizer, you can pass it as an argument:

```python
from mlflow.genai.judges.optimizers import MemAlignOptimizer
aligned_judge = initial_judge.align(traces_with_feedback, MemAlignOptimizer())
```

## Requirements

- Requires at least 10 traces for reasonable alignment, with 50-100 traces recommended for better results. ^[align-judges-with-humans-databricks-on-aws.md]
- Requires [MLflow](/concepts/mlflow.md) 3.4.0 or above. ^[align-judges-with-humans-databricks-on-aws.md]
- Works with both built-in judges and custom judges created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]
- The human feedback assessment name must exactly match the judge's `name` attribute. ^[align-judges-with-humans-databricks-on-aws.md]

## Alignment Process

The MemAlign Optimizer follows the standard three-step [Judge Alignment](/concepts/judge-alignment.md) workflow:

1. **Generate initial assessments**: Use a built-in or custom judge to evaluate traces and establish a baseline.
2. **Collect human feedback**: Domain experts review and correct judge assessments.
3. **Align and deploy**: Invoke the judge's `align()` method to create a new judge that is more aligned with human feedback.

## Debugging

To monitor the alignment process, enable debug logging for the MemAlign Optimizer:

```python
import logging
logging.getLogger("mlflow.genai.judges.optimizers.memalign").setLevel(logging.DEBUG)
```

## Related Concepts

- [Judge Alignment](/concepts/judge-alignment.md) — The process of teaching LLM judges to match human evaluation standards
- [Built-in Judges](/concepts/built-in-judges.md) — Pre-configured judges available in MLflow (e.g., `RelevanceToQuery`, `Safety`, `Correctness`)
- [Custom Judges](/concepts/custom-judges.md) — LLM-based evaluators created with `make_judge()`
- [AlignmentOptimizer](/concepts/alignment-optimizers.md) — The base class for creating custom alignment optimizers
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying aligned judges at scale

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
