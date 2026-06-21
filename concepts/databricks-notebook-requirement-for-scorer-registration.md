---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89fe469dd46dd57e12b1211f9603622b86d5269b33f1ed90dbf1e4e0fb4b23fb
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-notebook-requirement-for-scorer-registration
    - DNRFSR
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Databricks notebook requirement for scorer registration
description: Scorer functions used in production monitoring must be defined and registered from a Databricks notebook because the monitoring service serializes function code for remote execution.
tags:
  - databricks
  - notebook
  - serialization
  - production-monitoring
timestamp: "2026-06-19T14:13:24.487Z"
---

# Databricks Notebook Requirement for Scorer Registration

**Databricks notebook requirement for scorer registration** refers to the mandatory use of a Databricks notebook environment when defining and registering custom scorer functions for use in [Production Monitoring](/concepts/production-monitoring.md) for GenAI. This requirement ensures that the monitoring service can properly serialize the function code for remote execution. ^[code-based-scorers-databricks-on-aws.md]

## Why the Notebook Environment Is Required

Production monitoring supports two types of scoring mechanisms: [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and custom functions decorated with the `@scorer` decorator. When a `@scorer`-decorated function is used in production monitoring, the monitoring service serializes the function code for execution on remote infrastructure. This serialization process requires the notebook environment to succeed. Consequently, every `@scorer`-decorated function used in production monitoring must be defined and registered from within a Databricks notebook. ^[code-based-scorers-databricks-on-aws.md]

## Supported and Unsupported Scorer Types

- **Supported for production monitoring:** Built-in LLM judges and `@scorer`-decorated functions. ^[code-based-scorers-databricks-on-aws.md]
- **Not supported for production monitoring:** Class-based `Scorer` subclasses. If your use case requires stateful scorers in production, you must use the `@scorer` decorator and manage state inside the function body rather than relying on class instances. ^[code-based-scorers-databricks-on-aws.md]

## Workflow Summary

To register a custom scorer for production monitoring, you must:

1. Open a Databricks notebook.
2. Define your scoring logic inside a function decorated with `@scorer`.
3. Register the scorer from that notebook (for example, by calling the relevant MLflow API).
4. Once registered, the monitoring service can reference the serialized function code for remote execution.

For detailed steps, see the documentation on [Use custom scorer functions](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring#use-custom-scorer-functions). ^[code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- [@scorer decorator](/concepts/scorer-decorator.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md)
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
