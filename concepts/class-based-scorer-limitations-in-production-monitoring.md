---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b9a6c65f60fc10100aebf522c5faf8051dd0ca71e1baddaf7c97d34aa3b3545
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - class-based-scorer-limitations-in-production-monitoring
    - CSLIPM
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Class-based Scorer limitations in production monitoring
description: Class-based Scorer subclasses are not supported for production monitoring in Databricks MLflow; only @scorer-decorated functions work.
tags:
  - mlflow
  - production-monitoring
  - limitations
timestamp: "2026-06-19T14:13:15.538Z"
---

# Class-based Scorer Limitations in Production Monitoring

**Class-based `Scorer` limitations in production monitoring** refer to the restriction that production monitoring on Databricks does not support `Scorer` subclasses (class-based scorers). Only built-in LLM judges and functions decorated with the `@scorer` decorator are supported for production use. ^[code-based-scorers-databricks-on-aws.md]

## Limitation Overview

[Production Monitoring](/concepts/production-monitoring.md) allows custom scoring logic through two mechanisms: built-in [LLM Judges](/concepts/llm-judges.md) and user-defined scorer functions. However, class-based scorers — that is, any subclass of `Scorer` — are explicitly **not supported** for production monitoring. This restriction applies regardless of whether the scorer is stateful or stateless. ^[code-based-scorers-databricks-on-aws.md]

## Workaround for Stateful Scorers

If your scoring logic requires maintaining state (e.g., caching, counters, or configuration), you must use the `@scorer` decorator pattern instead of a class-based `Scorer` subclass. State should be managed **inside the function body** rather than through class attributes or instance variables. This ensures that the function can be serialized and executed by the monitoring service. ^[code-based-scorers-databricks-on-aws.md]

## Notebook Requirement for Scorer Functions

All `@scorer`-decorated functions that are used in production monitoring must be **defined and registered from a Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization process depends on the notebook environment. Functions defined outside a notebook (e.g., in Python scripts or packages) cannot be serialized reliably for production monitoring. For details, see the documentation on [custom scorer functions](/concepts/custom-scorers-for-llm-evaluation.md). ^[code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [@scorer decorator](/concepts/scorer-decorator.md) — The recommended approach for creating custom production scorers.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-built scorers that work without custom code.
- [Production Monitoring](/concepts/production-monitoring.md) — The monitoring system that enforces this limitation.
- [Custom scorer functions](/concepts/custom-scorer-definition-in-mlflow.md) — How to define and register scorer functions from a notebook.
- Databricks notebook — The required environment for defining production scorers.

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
