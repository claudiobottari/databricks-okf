---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f9b36f6f7986c7d314d0d2690652112cef1261cff7f6399325c097e628fdf5b4
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - notebook-required-function-serialization
    - NFS
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Notebook-required function serialization
description: "@scorer-decorated functions for production monitoring must be defined and registered from a Databricks notebook due to serialization requirements"
tags:
  - databricks
  - serialization
  - notebook
timestamp: "2026-06-19T17:45:03.036Z"
---

# Notebook-Required Function Serialization

**Notebook-required function serialization** is a constraint in Databricks production monitoring that requires custom scorer functions defined with the `@scorer` decorator to be created and registered from within a **Databricks notebook** environment. This requirement exists because the monitoring service must serialize the function code for remote execution, and this serialization process depends on the notebook runtime. ^[code-based-scorers-databricks-on-aws.md]

## Overview

When using custom scorer functions in Databricks production monitoring, the functions must be defined and registered from a Databricks notebook. The production monitoring system serializes the function's code to execute it remotely during inference monitoring. This serialization mechanism requires the notebook environment to function correctly. ^[code-based-scorers-databricks-on-aws.md]

## Scope and Limitations

The notebook requirement applies specifically to `@scorer`-decorated functions used in production monitoring. Class-based `Scorer` subclasses are **not supported** for production monitoring at all, regardless of the environment. If a stateful scorer is needed in production, the recommended approach is to use the `@scorer` decorator and manage state inside the function body. ^[code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) — The inference monitoring system that requires notebook-based registration for custom scorers
- [Custom Scorer Functions](/concepts/custom-scorer-definition-in-mlflow.md) — User-defined functions decorated with `@scorer` for evaluating model outputs
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-built evaluation functions that do not require custom serialization
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit that may contain registered scorers

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
