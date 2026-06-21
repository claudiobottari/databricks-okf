---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95d1edc351ae4d52463e4dc3ac731e271400c020d942d4659a8b1c4bd1d65953
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-notebook-serialization-requirement-for-scorers
    - DNSRFS
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Databricks notebook serialization requirement for scorers
description: Custom scorer functions used in production monitoring must be defined and registered from a Databricks notebook because the monitoring service requires the notebook environment for code serialization.
tags:
  - databricks
  - production-monitoring
  - serialization
timestamp: "2026-06-18T14:37:04.605Z"
---

# Databricks Notebook Serialization Requirement for Scorers

**Databricks notebook serialization requirement for scorers** refers to the mandatory use of Databricks notebooks when defining and registering `@scorer`-decorated functions for use in production monitoring. The production monitoring service serializes scorer function code for remote execution, and this serialization process depends on the notebook runtime environment. ^[code-based-scorers-databricks-on-aws.md]

## Overview

Production monitoring for GenAI agents supports built-in LLM judges and `@scorer`-decorated custom functions. However, class-based `Scorer` subclasses are **not supported** for production monitoring. For stateful scorers in production, developers must use the `@scorer` decorator and manage state within the function body. ^[code-based-scorers-databricks-on-aws.md]

## The Notebook Requirement

`@scorer`-decorated functions used in production monitoring must be defined and registered from a **Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization process requires the notebook environment. Attempting to register scorers from outside a notebook environment will fail due to serialization limitations. ^[code-based-scorers-databricks-on-aws.md]

## Supported Scorer Types for Production Monitoring

| Scorer Type | Supported for Production Monitoring | Notes |
|-------------|-------------------------------------|-------|
| Built-in LLM judges | Yes | No serialization required |
| `@scorer`-decorated functions | Yes | Must be defined in a Databricks notebook |
| Class-based `Scorer` subclasses | No | Not supported for production monitoring |

^[code-based-scorers-databricks-on-aws.md]

## Alternatives for Non-Notebook Workflows

If you need to develop custom scoring logic outside of a notebook environment, you have the following options:

- **Develop and test in notebooks first.** Create and test your `@scorer` functions in a Databricks notebook, then register them for production monitoring from the same notebook.
- **Use built-in LLM judges.** For common evaluation criteria, leverage the [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that Databricks provides, which do not require custom serialization.
- **Use class-based scorers for offline evaluation.** Class-based `Scorer` subclasses are still available for offline evaluation via `mlflow.genai.evaluate()`, even though they cannot be used in production monitoring.

## Best Practices

- **Define scorers in notebooks from the start.** Build your custom scoring functions directly in Databricks notebooks to ensure compatibility with production monitoring serialization.
- **Manage state within the function body.** If you need stateful behavior, use closures or module-level variables inside the `@scorer`-decorated function rather than instance state.
- **Test serialization early.** After defining your scorer in a notebook, register it for production monitoring to verify that serialization succeeds before building complex evaluation pipelines.

## Related Concepts

- [Custom Scorers for GenAI Agents](/concepts/custom-scorers-mlflow-genai.md) — Overview of custom scoring in MLflow GenAI
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-built judges that don't require custom serialization
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- [@scorer decorator](/concepts/scorer-decorator.md) — The decorator for defining custom scoring functions
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
