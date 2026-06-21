---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 530b44d6c9921bdc5fb62abad87329f715b81e3ac3003c47704b82bf9b805aa3
  pageDirectory: concepts
  sources:
    - scorer-lifecycle-management-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-lifecycle-management
    - SLM
    - Lifecycle management
    - Model Lifecycle Management
    - Model lifecycle management
    - Trace Lifecycle Management
    - Scorer lifecycle management API reference
  citations:
    - file: scorer-lifecycle-management-api-reference-databricks-on-aws.md
title: Scorer Lifecycle Management
description: Lifecycle methods (register, start, update, stop) that control MLflow scorers running continuous quality assessment on production traces
tags:
  - mlflow
  - lifecycle
  - monitoring
timestamp: "2026-06-19T20:19:35.945Z"
---

# Scorer Lifecycle Management

**Scorer Lifecycle Management** refers to the API methods and operational workflow for controlling [MLflow](/concepts/mlflow.md) scorers that perform continuous quality assessment on production traces in Databricks. The lifecycle consists of four primary operations: **register**, **start**, **update**, and **stop**, which together manage the state of a [[Scorers|Scorer]] from creation through deactivation. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Overview

The MLflow scorer lifecycle provides a structured way to manage online evaluation of [GenAI](/concepts/mlflow-genai-evaluate-api.md) application outputs. Scorers created with the `@scorer` decorator are registered with a server, then started to begin monitoring, updated to modify sampling behavior, and stopped to cease evaluation while preserving the scorer's registration. This lifecycle ensures that production monitoring is both configurable and reversible. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Lifecycle Methods

### `Scorer.register()`

**API Reference:** [`Scorer.register`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer.register)

Registers a custom scorer function with the server. This method is used for scorers created with the `@scorer` decorator. It accepts a `name` parameter (str) that provides a unique name for the scorer within the experiment. If no name is provided, it defaults to the existing name of the scorer. Returns a new `Scorer` instance with server registration. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### `Scorer.start()`

**API Reference:** [`Scorer.start`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer.start)

Begins online evaluation with the specified sampling configuration. Accepts a `sampling_config` parameter of type `ScorerSamplingConfig`, which includes:
- `sample_rate` (float): Fraction of traces to evaluate (0.0-1.0). Default: 1.0
- `filter_string` (str, optional): MLflow-compatible filter for trace selection

Returns a new `Scorer` instance in active state. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### `Scorer.update()`

**API Reference:** [`Scorer.update`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer.update)

Modifies the sampling configuration of an active scorer. This is an immutable operation, meaning it returns a new `Scorer` instance with the updated configuration while the original scorer remains unchanged. Accepts the same `sampling_config` parameters as `start()`. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### `Scorer.stop()`

**API Reference:** [`Scorer.stop`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Scorer.stop)

Stops online evaluation by setting the sample rate to 0. Keeps the scorer registered but prevents further trace evaluation. Returns a new `Scorer` instance with `sample_rate=0`. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Registry Functions

In addition to instance methods, the MLflow scorer lifecycle includes registry functions for managing existing scorers:

- **`get_scorer(name)`** – Retrieves a registered scorer by name. Returns a `Scorer` instance. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]
- **`list_scorers()`** – Lists all registered scorers for the current experiment. Returns a list of `Scorer` instances. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]
- **`delete_scorer(name)`** – Deletes a registered scorer by name. Returns None. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Scorer Properties

Active scorers expose two key properties:
- **`sample_rate`** (float, 0.0-1.0): Current sampling rate. Returns 0 for stopped scorers. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]
- **`filter_string`** (str): Current trace filter string for MLflow trace selection. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Configuration Classes

### `ScorerSamplingConfig`

A data class that holds the sampling configuration for a scorer. Includes `sample_rate` (float, optional) and `filter_string` (str, optional). ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Metric Backfill

The [BackfillScorers](/concepts/backfillscorers.md) function enables running scorers on historical trace data, which may be useful during lifecycle transitions or when adding new scorers after initial deployment. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow Scorer](/concepts/mlflow-scorers.md) – The core evaluation unit for production monitoring
- Production Quality Monitoring – The broader framework for continuous assessment
- [Scorer State Management](/concepts/scorer-state-management.md) – Active vs. stopped state transitions
- Trace Sampling – Controlling evaluation volume with sample rates
- [Scorer Registration](/concepts/scorer-registration-and-registry.md) – Server-side persistence of custom scorers

## Sources

- scorer-lifecycle-management-api-reference-databricks-on-aws.md

# Citations

1. [scorer-lifecycle-management-api-reference-databricks-on-aws.md](/references/scorer-lifecycle-management-api-reference-databricks-on-aws-55d28735.md)
